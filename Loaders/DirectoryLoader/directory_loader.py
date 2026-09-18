from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(path='Loaders/DirectoryLoader/AIBooks', glob="**/*.pdf", loader_cls= PyPDFLoader)

#docs = loader.load() #Eager Loading

docs = loader.lazy_load() #Lazy Loading

print(docs) #Printed correct Count(516) just ignore the fontTools warninh

for doc in docs:
    print(doc.metadata) 