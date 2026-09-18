from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Loaders/DirectoryLoader/AIBooks/271_AI Lect Notes.pdf')
docs = loader.load()

text = """
Artificial Intelligence in Modern Software Engineering
Artificial Intelligence is changing the way software applications are designed, developed, tested, and maintained. Modern development teams increasingly use large language models to assist with code generation, documentation, debugging, testing, and knowledge retrieval. However, building a reliable AI-powered application requires more than simply connecting an application to an LLM.
Retrieval-Augmented Generation, commonly called RAG, combines information retrieval with text generation. Instead of asking a language model to answer a question using only the knowledge contained in its training data, a RAG system first searches a collection of documents for relevant information. The retrieved content is then provided to the language model as additional context.
For developers learning RAG, it is useful to experiment with different chunk sizes and overlap values and then inspect the resulting chunks manually. Understanding exactly how a document is transformed before it reaches the language model provides a strong foundation for building reliable retrieval systems.
"""

splitter = CharacterTextSplitter(
    chunk_size=100, chunk_overlap=0, separator=''
)

#Recursive Character Tex tSplitter
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )


#result = splitter.split_text(text) # For text splitter

result = splitter.split_documents(docs) # For doc splitter
#print(result[0])
print(result[0].page_content)
#print(len(result[0]))
#print(len(result[1]))
#print(len(result[2]))