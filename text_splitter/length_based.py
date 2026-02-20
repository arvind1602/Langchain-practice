from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    separator=''
)

loader = PyPDFLoader("DSA_QBA.pdf")
docs = loader.load()

chunks = splitter.split_documents(docs)
test = """the 
relaƟonship between them. Some examples of D' metadata={'producer': 'Microsoft: Print To PDF', 'creator': 'PyPDF', 'creationdate': '2024-11-07T00:17:55+05:30', 'author': 'GANESH KUMAR VISHWAKARMA', 'moddate': '2024-11-07T00:17:55+05:30', 'title': 'Microsoft Word - DSA Interviews Question', 'source': 'DSA_QBA.pdf', 'total_pages': 13, 'page': 0, 'page_label': '1'}"""
print(test[48])

print(len(chunks))
print(chunks[4])