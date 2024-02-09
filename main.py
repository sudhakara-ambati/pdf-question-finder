import requests
import PyPDF2
from io import BytesIO
import fitz
from PIL import Image

def search_pdf_in_memory(pdf_content, search_words):
    found_pages = []
    reader = PyPDF2.PdfReader(BytesIO(pdf_content))
    num_pages = len(reader.pages)
    
    for page_num in range(num_pages):
        page_text = reader.pages[page_num].extract_text()
        for word in search_words:
            if word.lower() in page_text.lower():
                found_pages.append(page_num + 1)
                
    return found_pages

def capture_screenshot_from_page(pdf_content, page_num):
    doc = fitz.open(stream=BytesIO(pdf_content))
    page = doc.load_page(page_num - 1)  # Page numbers start from 0 in PyMuPDF
    pixmap = page.get_pixmap()
    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    return image

def create_pdf_with_images(images, output_pdf):
    images[0].save(output_pdf, save_all=True, append_images=images[1:])

url = "https://pmt.physicsandmathstutor.com/download/Maths/GCSE/Past-Papers/Edexcel/Paper-1H/MA/Nov%202021%20MA.pdf"
search_words = ["probability", "graph"]

pdf_response = requests.get(url)
if pdf_response.status_code == 200:
    pdf_content = pdf_response.content
    found_pages = search_pdf_in_memory(pdf_content, search_words)
    
    if found_pages:
        print(f"The word '{search_words[0]}' was found on pages: {', '.join(map(str, found_pages))}")
        images = []
        for page_num in found_pages:
            image = capture_screenshot_from_page(pdf_content, page_num)
            images.append(image)
        output_pdf = "output.pdf"
        create_pdf_with_images(images, output_pdf)
        print(f"PDF with screenshots saved as '{output_pdf}'")
    else:
        print("The word was not found in the PDF.")
else:
    print("Failed to download PDF.")
