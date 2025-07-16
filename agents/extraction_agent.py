import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from my_config import OPENAI_API_KEY
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#from my_config import OPENAI_API_KEY

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

# Load prompt template
prompt_template = PromptTemplate.from_file(
    "prompts/extract_fields_prompt.txt"
)

# Create the chain
chain = prompt_template | llm

def extract_fields(text: str) -> dict:
    """Extracts structured fields from PDF text using an LLM."""
    output = chain.invoke({"input_text": text})
    
    try:
        import json
        return json.loads(output)
    except json.JSONDecodeError:
        print("[!] Failed to parse JSON from LLM output.")
        return {"raw_output": output}
