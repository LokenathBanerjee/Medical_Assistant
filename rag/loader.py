from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_documents(data_dir: str = "data"):
    docs = []
    base = Path(data_dir)

    if not base.exists():
        return docs

    for pdf_path in base.glob("*.pdf"):
        try:
            # ✅ Skip empty files
            if pdf_path.stat().st_size == 0:
                print(f"Skipping empty PDF: {pdf_path.name}")
                continue

            loader = PyPDFLoader(str(pdf_path))
            docs.extend(loader.load())

        except Exception as e:
            # ✅ Skip corrupted/locked PDFs
            print(f"Skipping bad PDF: {pdf_path.name} -> {e}")
            continue

    return docs


