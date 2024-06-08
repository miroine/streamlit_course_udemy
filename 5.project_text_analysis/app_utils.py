import streamlit as st

import base64

# Load EDA Pkgs
import pandas as pd


# Text cleaning Pkgs
import neattext as nt
import neattext.functions as ntf

# Load NLP Pkgs
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

# utils
from collections import Counter
from textblob import TextBlob

# plotting Pkgs
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("agg")


# Fxns
def text_analyzer(my_text):
    docx = nlp(my_text)
    allData = [
        (
            token.text,
            token.shape_,
            token.pos_,
            token.tag_,
            token.lemma_,
            token.is_alpha,
            token.is_stop,
        )
        for token in docx
    ]
    return pd.DataFrame(
        allData,
        columns=["token", "shape", "pos", "tag", "lemma", "is_alpha", "is_stop"],
    )


def get_entities(my_text):
    docx = nlp(my_text)
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    return pd.DataFrame(entities, columns=["entity", "label"])


HTML_WRAPPER = """<div style="overflow-y: scroll;  border: 1px solid #e6">{}</div>"""


def render_entities(raw_text):
    docx = nlp(raw_text)
    html = displacy.render(docx, style="ent")
    html = html.replace("\n\n", "\n")
    result = HTML_WRAPPER.format(html)
    return result


# Fxns to get most common tokkens
def get_most_common_tokens(my_text, num_of_most_common=4):
    word_tokens = Counter(my_text.split())
    most_common_tokens = Counter(word_tokens).most_common(num_of_most_common)
    return pd.DataFrame(most_common_tokens, columns=["token", "count"])


# Fxn to get sentiments
def get_sentiments(my_text):
    blob = TextBlob(my_text)
    return blob.sentiment


# Fxns to get word cloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def get_word_cloud(my_text):
    wordcloud = WordCloud(
        stopwords=STOPWORDS, background_color="white", max_words=1000
    ).generate(my_text)
    fig = plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)


# Fxns to Download Results
def make_download_button(df, filename):
    csv_file = df.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    new_filename = f"nlp_results_{timestr}.csv"
    st.markdown("#### Download Results 🙂‍↕️ ####")
    href = f'<a href="data:file/csv;base64,{b64}" download = "{new_filename}" > Click here --> >'
    st.markdown(href, unsafe_allow_html=True)
