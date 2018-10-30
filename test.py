from pytesseract import image_to_string
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img='bill8.png'
text=image_to_string(img,lang='eng',config=pytesseract.pytesseract.tesseract_cmd)
print(text)

