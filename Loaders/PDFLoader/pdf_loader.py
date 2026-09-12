from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path


pdf_path = Path(__file__).parent / "AIEducation.pdf"

loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

# print(docs) #to get the content of doc
#print(len(docs)) #length of pdf pages
#print(docs[0].page_content)   #To get the content
print(docs[0].metadata)  #To get the metadata