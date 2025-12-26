from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(file_path: str):
    reader = PdfReader(file_path)
    documents = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text:
            continue

        chunks = splitter.split_text(text)

        for chunk in chunks:
            documents.append({
                "content": chunk,
                "page": page_number
            })

    return documents
