import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

## langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']="Simple Q&A Chatbot "
# prompt
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a assistant. Please response to the user queries"),
    ("user","Question:{question}")

])
def generate_response(question,api_key,llm,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer
##title
st.title("Q&A Chatbot")
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter Your Key:",type="password")
llm=st.sidebar.selectbox("Select an OpenAI model",["gpt-4o","gpt-4-turbo","gpt-4"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.5)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)


st.write("ask any question")
user_input=st.text_input("you:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")   