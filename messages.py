from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

messages=[
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)