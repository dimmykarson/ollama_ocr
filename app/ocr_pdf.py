from ollama_ocr import OCRProcessor
from dotenv import load_dotenv
import os
load_dotenv()

host      = os.getenv("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
base_url  = f"{host}/api/generate" 

class OCRParser:
    def __init__(self, model_name="llama3.2-vision"):
        self.ocr = OCRProcessor(
            model_name=model_name,
            base_url=base_url
        )
        self.model_name = model_name

    def parse(self, pdf_path):
        result = self.ocr.process_image(
            image_path=pdf_path,
            format_type="text",
            language="pt"
        )
        return result

