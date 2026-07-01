from pathlib import Path
from docx import Document

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOB_FILE = PROJECT_ROOT / "data" / "job_description.docx"


def load_job_description(file_path):
    doc = Document(file_path)

    text = []

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text.strip())

    return "\n".join(text)


if __name__ == "__main__":

    job_description = load_job_description(JOB_FILE)

    print("=" * 80)
    print(job_description)
    print("=" * 80)