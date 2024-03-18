import requests
import PyPDF2
from io import BytesIO
import fitz
from PIL import Image

def search_pdf_in_memory(pdf_content, search_words):
    found_pages = []
    reader = PyPDF2.PdfReader(BytesIO(pdf_content)) #PDF Content
    num_pages = len(reader.pages) #Number of pages
    
    for page_num in range(num_pages):
        page_text = reader.pages[page_num].extract_text()
        for word in search_words:
            if word.lower() in page_text.lower(): #Search for word in pages
                found_pages.append(page_num + 1) #Page numbers start at 0
                
    return found_pages

def capture_screenshot_from_page(pdf_content, page_num):
    doc = fitz.open(stream=BytesIO(pdf_content))
    page = doc.load_page(page_num - 1)
    pixmap = page.get_pixmap()
    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    return image #Taking screenshot of page

def create_pdf_with_images(images, output_pdf):
    images[0].save(output_pdf, save_all=True, append_images=images[1:]) #Append images into PDF

maths = [
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

biology = [
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84611H-QP-JUN22.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84612H-QP-JUN22.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-84611H-QP-NOV21.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-84612H-QP-NOV21.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2020/november/AQA-84611H-QP-NOV20.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2020/november/AQA-84612H-QP-NOV20.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2018/june/AQA-84611H-QP-JUN18.PDF",
    "https://filestore.aqa.org.uk/resources/biology/AQA-84611H-SQP.PDF",
    "https://filestore.aqa.org.uk/resources/biology/AQA-84612H-SQP.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL1HP-QP-JUN17.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL2HP-QP-JUN17.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL3HP-QP-JUN17.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL1HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL2HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL3HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL1HP-QP-JUN15.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL2HP-QP-JUN15.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-BL3HP-QP-JUN15.PDF"
]

chemistry = [
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84621H-QP-JUN22.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84622H-QP-JUN22.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-84621H-QP-NOV21.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-84622H-QP-NOV21.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2020/november/AQA-84621H-QP-NOV20.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2020/november/AQA-84622H-QP-NOV20.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2019/june/AQA-84621H-QP-JUN19.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2018/june/AQA-84621H-QP-JUN18.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2018/june/AQA-84622H-QP-JUN18.PDF",
    "https://filestore.aqa.org.uk/resources/chemistry/AQA-84621H-SQP.PDF",
    "https://filestore.aqa.org.uk/resources/chemistry/AQA-84622H-SQP.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH1HP-QP-JUN17.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH2HP-QP-JUN17.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH3HP-QP-JUN17.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH1HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH2HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH3HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH1HP-QP-JUN15.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH2HP-QP-JUN15.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-CH3HP-QP-JUN15.PDF"
]

physics = [
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84631H-QP-JUN22.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84632H-QP-JUN22.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-84631H-QP-NOV21.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-84632H-QP-NOV21.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2020/november/AQA-84631H-QP-NOV20.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2020/november/AQA-84632H-QP-NOV20.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2019/june/AQA-84632H-QP-JUN19.PDF",
    "https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2018/june/AQA-84632H-QP-JUN18.PDF",
    "https://filestore.aqa.org.uk/resources/physics/AQA-84631H-SQP.PDF",
    "https://filestore.aqa.org.uk/resources/physics/AQA-84632H-SQP.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH1HP-QP-JUN17.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH2HP-QP-JUN17.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH3HP-QP-JUN17.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH1HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH2HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH3HP-QP-JUN16.pdf",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH1HP-QP-JUN15.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH2HP-QP-JUN15.PDF",
    "https://revisionscience.com/sites/revisionscience.com/files/imce/AQA-PH3HP-QP-JUN15.PDF"
]

english = [
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1et0-01-que-20220526.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1et0-2n-que-20220609.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1et0-2p-que-20220609.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_01_que_20211117.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_2N_que_20211123.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_2P_que_20211123.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_01_que_20201106.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_02_que_20201113.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_01_que_20190516.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_02_que_20190524.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_01_que_20180523.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_02_que_20180526.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_01_que_20170522.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/1ET0_02_que_20170526.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/5ET1H_01_que_20160523.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/5ET2H_01_que_20160527.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/5ET1H_01_que_20150518.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/5ET2H_01_que_20150522.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/Question-paper-Unit-1H-June-2014.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/Question-paper-Unit-2H-June-2014.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/5ET1H_01_que_20130520.pdf",
    "https://revisionworld.com/sites/revisionworld.com/files/imce/5ET2H_01_que_20130523.pdf"

]

search_words = ["Question 3 − Dr Jekyll and Mr Hyde"]
all_images = []

for url in english:
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
