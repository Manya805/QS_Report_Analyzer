from agents.extraction_agent import extract_fields
from agents.parsing_agent import parse_pdf  # adjust path if needed

# Path to your sample PDF
pdf_path = "QS Report BPM.pdf"

# Step 1: Parse PDF to get raw text
text = parse_pdf(pdf_path)

# Step 2: Extract structured data using LLM
extracted_data = extract_fields(text)

# Step 3: Print result
import json
print(json.dumps(extracted_data, indent=2))
