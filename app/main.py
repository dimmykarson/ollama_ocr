
from ocr_pdf import OCRParser


if __name__ == "__main__":
    ocr_parser = OCRParser()
    text = ocr_parser.parse("data/example.pdf")
    print(text)