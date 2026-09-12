from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

#loader = PyPDFLoader('Loaders/DirectoryLoader/AIBooks/271_AI Lect Notes.pdf')
#docs = loader.load()

text = """My name is Tushar
I am 33 Years old
I live in Gurgaon
How are you
"""


#Recursive Character Tex tSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=51,
    chunk_overlap=0
)


result = splitter.split_text(text) # For text splitter

#result = splitter.split_documents(docs) # For doc splitter
print(result)
