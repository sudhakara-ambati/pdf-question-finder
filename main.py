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
    page = doc.load_page(page_num - 1)
    pixmap = page.get_pixmap()
    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    return image

def create_pdf_with_images(images, output_pdf):
    images[0].save(output_pdf, save_all=True, append_images=images[1:])

urls = [
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_1H_que_20211103.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_2H_que_20211105.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_3H_que_20211109.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1ma1-1h-que-20220521.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1ma1-2h-que-20220608.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1ma1-3h-que-20220614.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_1H_que_20201104.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_2H_que_20201106.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_3H_que_20201110.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_1H_que_20190522.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_2H_que_20190607.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_3H_que_20190612.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/Questionpaper-Paper1H-November2018.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/Questionpaper-Paper2H-November2018.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/Questionpaper-Paper3H-November2018.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_1H_QP_0.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_2H_QP_0.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_3H_QP_0.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_1H_QP_1.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_2H_QP_1.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_3H_QP_1.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_1H_QP.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_2H_QP.pdf",
    "https://revisionmaths.com/sites/mathsrevision.net/files/imce/1MA1_3H_QP.pdf"
    ]

search_words = ["box plot", "probability"]
all_images = []

for url in urls:
    pdf_response = requests.get(url)
    if pdf_response.status_code == 200:
        pdf_content = pdf_response.content
        found_pages = search_pdf_in_memory(pdf_content, search_words)
        
        if found_pages:
            print(f"The words '{', '.join(search_words)}' were found on pages: {', '.join(map(str, found_pages))}")
            images = []
            for page_num in found_pages:
                image = capture_screenshot_from_page(pdf_content, page_num)
                images.append(image)
            all_images.extend(images)
            print(f"Images from {url} appended.")
        else:
            print(f"The word was not found in the PDF from {url}.")
    else:
        print(f"Failed to download PDF from {url}.")

output_pdf = "_".join(search_words) + ".pdf"
create_pdf_with_images(all_images, output_pdf)
print(f"PDF with screenshots saved as '{output_pdf}'")
