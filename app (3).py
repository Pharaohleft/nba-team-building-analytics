import streamlit as st
from transformers import pipeline
from rouge_score import rouge_scorer

@st.cache_resource
def load_models():
    bart = pipeline("summarization", model="facebook/bart-large-cnn")
    t5 = pipeline("summarization", model="t5-small")
    return bart, t5

bart_model, t5_model = load_models()

st.set_page_config(page_title="LLM Summary Comparator", layout="wide")
st.title("LLM Summary Comparator")
st.markdown("Paste any text to compare BART and T5 summaries, with ROUGE-L + word count.")

text = st.text_area("Enter input text here:", height=200)

if st.button("Generate Summaries") and text.strip():
    bart_summary = bart_model(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    t5_summary = t5_model("summarize: " + text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    bart_rouge = scorer.score(text, bart_summary)['rougeL'].fmeasure
    t5_rouge = scorer.score(text, t5_summary)['rougeL'].fmeasure

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("BART")
        st.write(bart_summary)
        st.caption(f"Length: {len(bart_summary.split())} words")
        st.caption(f"ROUGE-L: {round(bart_rouge, 3)}")

    with col2:
        st.subheader("T5")
        st.write(t5_summary)
        st.caption(f"Length: {len(t5_summary.split())} words")
        st.caption(f"ROUGE-L: {round(t5_rouge, 3)}")
