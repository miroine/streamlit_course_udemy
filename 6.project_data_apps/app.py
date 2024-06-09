import streamlit as st
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd


# Opening files Pkgs

import exifread

# For Audio
import mutagen


# for PDF
from PyPDF2 import PdfReader

import os
from datetime import datetime

from app_utils import *
from db_utils import *


import time

# HTML stuff


import sqlite3

conn = sqlite3.connect("metadata.db")
c = conn.cursor()


metadata_wiki = """
Metadata is data that provides information about other data. 
It serves to describe the characteristics, content, 
and context of the data it refers to, making 
it easier to find, use, and manage.
"""

HTML_BANNER = """
    <div style="background-color: #464e5f; padding: 10px; border-radius: 10px;">
    <h1 style="color: white; font-size: 30px; text-align: center;">Meta Data Extraction App</h1>
    </div>
"""


#  main app function
def main():
    """Meta Data Extraction App"""
    # st.title("MetaData Extraction App")
    stc.html(HTML_BANNER, height=100)

    menu = ["Home", "Image", "Audio", "DocumentFiles", "Analytics", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_uploaded_files_table()
    if choice == "Home":
        st.subheader("Home")
        st.image(load_image("images/image.png"), use_column_width=True)
        st.write(metadata_wiki)

        col1, col2, col3 = st.columns(3)
        with col1:
            with st.expander("Get Image Metadata 🏞️"):
                st.info("Image Metadata ")
                st.text("Upload JPEG, JPG, PNG image")

        with col2:
            with st.expander("Get Audio Metadata ⛲"):
                st.info("Audio Metadata")
                st.text("Upload Mp3, MP4, WAV")

        with col3:
            with st.expander("Get Documents Metadata 🗃️"):
                st.info("Image Metadata")
                st.text("Upload PDF, DOC, DOCX")

    elif choice == "Image":
        st.subheader("Images Metadata Extraction")
        image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
        if image_file is not None:

            file_details = {
                "filename": image_file.name,
                "filetype": image_file.type,
                "filesize": image_file.size,
            }
            with st.expander("File Details"):
                st.write(file_details)

                statinfo = os.stat(image_file.readable())
                exif_data = exifread.process_file(image_file)
                stats_details = {
                    "Accessed_Time": get_readable_time(statinfo.st_atime),
                    "Created_Time": get_readable_time(statinfo.st_ctime),
                    "Modify_time": get_readable_time(statinfo.st_mtime),
                }
                st.write(stats_details)

                file_details_combined = {**file_details, **stats_details}
                df_file_details = pd.DataFrame(
                    file_details_combined, index=[0]
                ).T.reset_index(0)
                df_file_details.columns = ["metadata", "values"]
                st.dataframe(df_file_details, use_container_width=True)
            c1, c2 = st.columns(2)
            with c1:
                with st.expander("Show image"):
                    img = load_image(image_file)
                    st.image(img, width=250)
            with c2:
                with st.expander("Show PILLOW Data"):
                    st.info("Using PILLOW")
                    img_details = {
                        "format": img.format,
                        "format_desc": img.format_description,
                        "size": img.size,
                        "mode": img.mode,
                        "height": img.height,
                        "width": img.width,
                        "encoder": img.encoderinfo,
                        "info": img.info,
                    }
                    df_file_details = pd.DataFrame(
                        list(img_details.items()), columns=["metadata", "value"]
                    )
                    st.dataframe(df_file_details, use_container_width=True)

            # layout for forensic

            fcol1, fcol2 = st.columns(2)
            with fcol1:
                with st.expander("Exifread Tool"):
                    meta_tags = exifread.process_file(image_file)
                    # meta_tags = get_exif(image_file)
                    st.write(meta_tags)
                    try:
                        df_img_details = pd.DataFrame(
                            list(meta_tags.items()), columns=["metadata", "value"]
                        )
                        st.dataframe(df_img_details, use_container_width=True)
                    except:
                        df_img_details = None
                        st.info("No metadata found")

            with fcol2:
                with st.expander("Image Geo-Coordinates"):
                    img_details_with_exif = get_exif(image_file)
                    try:
                        gps_info = get_decimal_coordinates(img_details_with_exif)
                        st.write(gps_info)
                    except:
                        gps_info = None
                        st.info("No GPS data found")

            with st.expander("Download results"):
                final_df = pd.concat([df_file_details, df_img_details], axis=0)
                st.dataframe(final_df, use_container_width=True)

                # add trackback
                add_file_details(
                    image_file.name, image_file.type, image_file.size, datetime.now()
                )
                timestr = time.strftime("%Y%m%d-%H%M%S")
                st.download_button(
                    "Download CSV",
                    data=final_df.to_csv(index=False),
                    file_name=f"metadata_{timestr}.csv",
                    mime="text/csv",
                )

    elif choice == "Audio":
        st.subheader("Audio Meta Extraction")
        # File Uploader
        # extraction Process using mutagen
        audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "mp4"])
        if audio_file is not None:
            with st.expander("Show Audio"):
                st.audio(audio_file.read(), format="audio")
            # layouts
            col1, col2 = st.columns(2)
            with col1:
                with st.expander("Show Audio Metadata"):
                    file_details = {
                        "filename": audio_file.name,
                        "filetype": audio_file.type,
                        "filesize": audio_file.size,
                    }
                    # st.write(file_details)
                    statinfo = os.stat(audio_file.readable())
                    stat_details = {
                        "Accessed_Time": get_readable_time(statinfo.st_atime),
                        "Created_Time": get_readable_time(statinfo.st_ctime),
                        "Modified_Time": get_readable_time(statinfo.st_mtime),
                    }
                    # st.write(stat_details)
                    file_details_combined = {**file_details, **stat_details}
                    df_file_details = pd.DataFrame(
                        file_details_combined, index=[0]
                    ).T.reset_index(0)
                    df_file_details.columns = ["metadata", "value"]
                    st.dataframe(df_file_details, use_container_width=True)
                    add_file_details(
                        audio_file.name,
                        audio_file.type,
                        audio_file.size,
                        datetime.now(),
                    )

            with col2:
                with st.expander("Show Audio Metadata"):
                    audio_meta = mutagen.File(audio_file)
                    df_audio_meta = pd.DataFrame(
                        list(audio_meta.items()), columns=["metadata", "value"]
                    )
                    df_audio_meta["value"] = df_audio_meta["value"].apply(
                        convert_txxx_to_string
                    )
                    st.dataframe(df_audio_meta, use_container_width=True)

            with st.expander("Download results"):
                final_df = pd.concat([df_file_details, df_audio_meta], axis=0)
                st.dataframe(final_df, use_container_width=True)
                timestr = time.strftime("%Y%m%d-%H%M%S")
                st.download_button(
                    "Download CSV",
                    data=final_df.to_csv(index=False),
                    file_name=f"metadata_{timestr}.csv",
                    mime="text/csv",
                )

    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles MetaData Extraction")
        text_file = st.file_uploader("Upload Documents", type=["pdf"])
        if text_file is not None:
            with st.expander("Show Document"):
                st.write(text_file.read())

            # layouts
            col1, col2 = st.columns(2)
            with col1:
                with st.expander("Show Audio Metadata"):
                    file_details = {
                        "filename": text_file.name,
                        "filetype": text_file.type,
                        "filesize": text_file.size,
                    }
                    # st.write(file_details)
                    add_file_details(
                        text_file.name, text_file.type, text_file.size, datetime.now()
                    )
                    statinfo = os.stat(text_file.readable())
                    stat_details = {
                        "Accessed_Time": get_readable_time(statinfo.st_atime),
                        "Created_Time": get_readable_time(statinfo.st_ctime),
                        "Modified_Time": get_readable_time(statinfo.st_mtime),
                    }
                    # st.write(stat_details)
                    file_details_combined = {**file_details, **stat_details}
                    df_file_details = pd.DataFrame(
                        file_details_combined, index=[0]
                    ).T.reset_index(0)
                    df_file_details.columns = ["metadata", "value"]
                    st.dataframe(df_file_details, use_container_width=True)

            with col2:
                with st.expander("Show Document Metadata"):
                    pdf_file = PdfReader(text_file)
                    pdf_meta = pdf_file.metadata
                    df_pdf_meta = pd.DataFrame(
                        list(pdf_meta.items()), columns=["metadata", "value"]
                    )
                    st.dataframe(df_pdf_meta, use_container_width=True)

            with st.expander("Download results"):
                final_df = pd.concat([df_file_details, df_pdf_meta], axis=0)
                st.dataframe(final_df, use_container_width=True)
                timestr = time.strftime("%Y%m%d-%H%M%S")
                st.download_button(
                    "Download CSV",
                    data=final_df.to_csv(index=False),
                    file_name=f"metadata_{timestr}.csv",
                    mime="text/csv",
                )

    elif choice == "Analytics":
        st.subheader("Analytics")
        st.image(load_image("images/image.png"), use_column_width=True)
        all_uploaded_files = view_all_files()
        df = pd.DataFrame(
            all_uploaded_files,
            columns=["filename", "filetype", "filesize", "uploaded_time"],
        )

        st.info("Statistics of uploaded files")
        with st.expander("Monitoring"):
            st.success("View all uploaded files")
            st.dataframe(df, use_container_width=True)

    else:
        st.subheader("About")
        st.image(load_image("images/image.png"), use_column_width=True)
        st.info(
            "This is a simple app to extract metadata from images, audio and documents."
        )


if __name__ == "__main__":
    main()
