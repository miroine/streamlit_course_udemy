import streamlit as st
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd
import numpy as np

# Plotting Pkgs
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

matplotlib.use("agg")

# Opening files Pkgs
# For images
from PIL import Image
import exifread

# For Audio
import mutagen
from mutagen.id3 import TXXX

# for PDF
from PyPDF2 import PdfReader

import os
from datetime import datetime
import base64
import sqlite3

conn = sqlite3.connect("metadata.db")
c = conn.cursor()


# Functions
@st.cache_data(persist=True)
def load_image(image_file):
    img = Image.open(image_file)
    return img


# Fxns to get humain readable time
def get_readable_time(mytime):
    return datetime.fromtimestamp(mytime).strftime("%Y-%m-%d %H:%M:%S")


from PIL.ExifTags import TAGS, GPSTAGS


def get_exif(image_file):
    exif = Image.open(image_file)._getexif()
    if exif is not None:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)
        return exif


def get_decimal_coordinates(exif_data):
    for key in ["Latitude", "Longitude"]:
        if "GPS" + key in exif_data and "GPS" + key + "Ref" in exif_data:
            e = exif_data["GPS" + key]
            ref = exif_data["GPS" + key + "Ref"]
            exif_data[key] = (
                e[0][0] / e[0][1] + e[1][0] / e[1][1] / 60 + e[2][0] / e[2][1] / 3600
            ) * (-1 if ref in ["S", "W"] else 1)
    if "Latitude" in exif_data and "Longitude" in exif_data:
        return (exif_data["Latitude"], exif_data["Longitude"])


def make_download_button(df, filename):
    csvfile = df.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()
    st.markdown("### ** Download CSV File ** ")
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" download="{filename}">Download File</a>'
    st.markdown(href, unsafe_allow_html=True)


def convert_txxx_to_string(obj):
    if isinstance(obj, TXXX):
        return f"desc='{obj.desc}', text='{obj.text}'"
    return str(obj)


# database management
def create_uploaded_files_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS filestable(file_name TEXT, file_type TEXT, file_size INTEGER, file_uploaded_on TEXT)"
    )
    conn.commit()


# add details
def add_file_details(file_name, file_type, file_size, file_uploaded):
    c.execute(
        "INSERT INTO filestable(file_name, file_type, file_size, file_uploaded_on) VALUES (?,?,?,?)",
        (file_name, file_type, file_size, file_uploaded),
    )
    conn.commit()


# view the details
def view_all_files():
    c.execute("SELECT * FROM filestable")
    data = c.fetchall()
    return data


def delete_all_files():
    c.execute("DELETE FROM filestable")
    conn.commit()
