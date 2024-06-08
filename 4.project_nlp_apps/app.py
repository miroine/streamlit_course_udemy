# Core Pkg 
import streamlit as st 

#Additional Pkg / Summary Pkgs 
#TextRank Algorithm
#from gensim.summarization import summarize
import nltk
#LexRank Algorithm
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#import Eda Pkgs 
import pandas as pd 
from rouge import Rouge 
#DataVis 
import plotly.express as px 
import seaborn as sns 

nltk.download('punkt')
def smr_summarizer(docx, num=2):
    parser = PlaintextParser.from_string(docx,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,num)
    summary_list = [str(sentence) for sentence in lex_summarizer(parser.document,2)]
    result = " ".join(summary_list)
    return result

def evaluate_summary(summary, reference):
    r= Rouge()
    eval_score = r.get_scores(summary, reference, avg=True)
    eval_score_df = pd.DataFrame(eval_score)
    return eval_score_df
    
def main():
    """
    Simple Summarization app
    """ 
    st.title("Summarization App")
    
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter Text")
        if st.button("Summarize"):
            with st.expander("Raw Text"):
                st.write(raw_text)
            
            c1, c2 = st.columns(2)
            with c1:
                with st.expander("TextRank"):
                    st.write("Not working")
                #st.write(summarize(raw_text, ratio=0.1))
            with c2:
                with st.expander("LexRank"):
                    my_summary = smr_summarizer(raw_text)
                    document_len = {
                        "Original" : len(raw_text),
                        "Summary": len(my_summary)
                    }
                    st.write(document_len)
                    st.write(my_summary)
                    st.info("Rouge Score")
                    score= evaluate_summary(my_summary, raw_text)
                    st.dataframe(score)

    else:
        st.subheader("About")
        st.text("This is a simple summarization app")



if __name__ == '__main__':
    main()