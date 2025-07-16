import pdfplumber
file_path = "QS Report BPM.pdf"
def parse_pdf(file_path):
    all_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"
    return all_text

#text = parse_pdf("QS Report BPM.pdf")
#print(text)
