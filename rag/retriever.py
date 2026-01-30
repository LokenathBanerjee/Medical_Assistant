import streamlit as st
from rag.vectorstore import build_vectorstore

@st.cache_resource
def get_retriever(data_dir="data"):
    vs = build_vectorstore(data_dir=data_dir)
    if vs is None:
        return None
    return vs.as_retriever(search_kwargs={"k": 3})
