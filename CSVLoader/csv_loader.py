from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='CSVLoader/username-password-recovery-code.csv')
doc = loader.load()
print(doc) #To Print Document