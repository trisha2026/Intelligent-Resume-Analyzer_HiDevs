from pypdf import PdfReader


def extract_text_from_pdf(file_path):
    """Extract text from all pages of a PDF resume."""

    try:
        reader = PdfReader(file_path)
    except Exception as error:
        raise ValueError(f"Could not open PDF: {error}")

    if not reader.pages:
        raise ValueError("PDF contains no pages.")

    text = []

    for page in reader.pages:
        try:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
        except Exception as error:
            raise ValueError(f"Could not extract text from PDF: {error}")

    resume_text = "\n".join(text).strip()

    if not resume_text:
        raise ValueError("Could not extract any text from the PDF.")

    return resume_text