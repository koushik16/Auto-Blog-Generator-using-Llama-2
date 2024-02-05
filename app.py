import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


def responce(input_text,no_words,blog_style):
    lm = CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                       model_type='llama',
                       config = {'max_new_tokens':256,
                                 'temperature':0.01})
    
    template=""" Write a blog {blog_style} job profile for a topic {input_text} within {no_words} words"""


    prompt = PromptTemplate(input_variables=['blog_style','input_text','no_words'], template= template)


    responce=lm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))

    print(responce)
    return responce


st.set_page_config(page_title='Blog-Gen',
                   layout='centered',initial_sidebar_state='collapsed')

st.header("Blog Generator")

input_text = st.text_input("Enter the topic:")

col1,col2 = st.columns([5,5])


with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox("writing blog for the",('Researchers', 'Data Scientists', 'Common People'),index=0)

submit=st.button("Submit and generate blog")

if submit==True:
    st.write(responce(input_text,no_words,blog_style))
