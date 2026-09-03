from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

prompt = PromptTemplate(
    template='Write a summary of the following poem - \n {poem}', 
    input_variables=['poem']
)
parser = StrOutputParser()
loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()
#print(docs)
#print(type(docs))
#Document will be divided into multiple parts 
# and stores in list hence type = <class 'list'>

#print(len(docs)) #Length of total docs item

# To print Docs Page Content and Meta Data
#print((docs[0].page_content))
#print((docs[0].metadata))


chain = prompt | model | parser
print(chain.invoke({'poem': docs[0].page_content}))
