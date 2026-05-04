from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

chat_template=ChatPromptTemplate=([
    ('system','you are a helpful {domain} expert '),
    ('human','Explain in simple terms, what is {topic}')
    

])

prompt=chat_template.invoke({'domain':'cricket','topic':'test cricket'})

print(prompt)