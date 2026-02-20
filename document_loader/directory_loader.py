from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=".",          # current directory
    glob="*.pdf",      # match all PDF files
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))
