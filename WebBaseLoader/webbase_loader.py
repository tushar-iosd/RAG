from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser #Output Parsing
from langchain_core.prompts import PromptTemplate #Prompt Creation
from dotenv import load_dotenv #Env Variables
from langchain_google_genai import ChatGoogleGenerativeAI #LLMIntegration

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text -\n {text}', 
    input_variables=['question','text']
)
parser = StrOutputParser()


url = 'https://www.amazon.in/Apple-MacBook-Laptop-18%E2%80%91core-40%E2%80%91core/dp/B0GR1LB81D/'
loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser
print(chain.invoke({'question':'How much core CPU and GPU this product has? ', 'text':docs[0].page_content}))
#print(len(docs))
#print(docs[0].page_content)