import streamlit as st
from llm import get_llm_chain
from dotenv import load_dotenv


load_dotenv()
st.title("IKIGAI")
quesLove = "What do you love ?"
quesGoodAt = "What are you good at ?"
quesWorldNeed = "What does the world need ?"
quesPaidFor = "What can you get paid for ?"
submitted = False
with st.form("ikigai_form"):
    love = st.text_area(quesLove)
    goodAt = st.text_area(quesGoodAt)
    worldNeed = st.text_area(quesWorldNeed)
    paidFor = st.text_area(quesPaidFor)
    submitted = st.form_submit_button("Submit")

if submitted:
    chain = get_llm_chain("be very concise")
    query = f"""
    {quesLove}
    {love}
    {quesGoodAt}
    {goodAt}
    {quesWorldNeed}
    {worldNeed}
    {quesPaidFor}
    {paidFor}
    What is my ikigai, be very concise
    """
    res = chain.invoke({"query": query})

    st.write(res)
