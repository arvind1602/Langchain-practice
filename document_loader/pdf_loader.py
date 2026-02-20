from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("OS_Full_Notes.pdf")

docs = loader.load()



print(docs[0])

# print(docs[0].page_content)