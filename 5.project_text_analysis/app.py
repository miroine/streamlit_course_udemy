import streamlit as st
import streamlit.components.v1 as stc


from app_utils import *

# Load NLP Pkgs
import spacy

nlp = spacy.load("en_core_web_sm")

# Text cleaning Pkgs
import neattext as nt
import neattext.functions as ntf

# plotting Pkgs
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("agg")

import base64
import time

timestr = time.strftime("%Y%m%d-%H%M")


def main():
    st.title("NL languages App")
    menu = ["Home", "NLP(files)", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home: Analysis Text")
        raw_text = st.text_area("Enter Text")
        num_of_most_common = st.sidebar.number_input("Most common words", 5, 15)
        if st.button("Analyze"):
            with st.expander("Orignial Text"):
                st.write(raw_text)
            with st.expander("Text Analysis"):
                token_result_df = text_analyzer(raw_text)
                st.dataframe(token_result_df)
            with st.expander("Entities"):
                entity_results = render_entities(raw_text)
                stc.html(entity_results, height=300)

            # Layouts
            col1, col2 = st.columns(2)

            with col1:
                with st.expander("Words statistics"):
                    st.info("Words statistics")
                    docx = nt.TextFrame(raw_text)
                    st.write(docx.word_stats())
                with st.expander("Top Keywords"):
                    st.info("Top Keywords")
                    processed_text = ntf.remove_stopwords(raw_text)
                    keywords = get_most_common_tokens(
                        processed_text, num_of_most_common=num_of_most_common
                    )
                    st.dataframe(keywords, use_container_width=True)
                with st.expander("Sentiment Analysis"):
                    st.info("Sentiment Analysis")
                    sent_results = get_sentiments(raw_text)
                    st.write(sent_results)
            with col2:
                with st.expander("Plot Word Freq"):
                    keywords_word = get_most_common_tokens(
                        processed_text, num_of_most_common=num_of_most_common
                    )
                    # st.write(keywords)
                    keywords_word["count"] = keywords_word["count"].astype(int)
                    keywords_word = keywords_word.sort_values(
                        by="count", ascending=True
                    )
                    st.plotly_chart(
                        px.bar(y=keywords_word["token"], x=keywords_word["count"])
                    )

                with st.expander("Plot part speech"):
                    fig = plt.figure()
                    sns.countplot(token_result_df["pos"])
                    st.pyplot(fig)
                with st.expander("Plot Wordcloud"):
                    get_word_cloud(raw_text)

            with st.expander("Download Test analysis results"):
                make_download_button(token_result_df, "token_result_df.csv")

    elif choice == "NLP(files)":
        st.subheader("NLP(files): Analysis Text")
    else:
        pass


if __name__ == "__main__":
    main()
