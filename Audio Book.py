# A python script that can be used to convert a pdf into an audiobook

import pyttsx3, PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
    speaker.runAndWait()
speaker.stop()