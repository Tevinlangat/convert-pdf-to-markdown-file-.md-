# pip install pdfplumber

import pdfplumber

pdf_file = '' # replace with the pdf to convert

with pdfplumber.open(pdf_file) as pdf:
    markdown_text = ""
    for page in pdf.pages:
        markdown_text += page.extract_text()
        
with open("./md/output.md", "w",encoding="utf-8") as file:
    file.write(markdown_text)