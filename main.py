from langchain_helper import create_vector_db,get_qa_chain
import streamlit as st

st.title("FAQs from Custom Datasets")

btn = st.button("Create a knowlegdebase")

if btn:
    pass

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain.invoke(question)

    st.header("Answer:")
    st.write(response["result"])