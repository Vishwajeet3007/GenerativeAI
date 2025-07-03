from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = 'LangChain_Document_Loader\Books',
    glob ='*.pdf',
    loader_cls=PyPDFLoader
)
docs = loader.lazy_load()
for doc in docs:
    print(doc.metadata)