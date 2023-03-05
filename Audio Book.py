# Designed and Developed by Muhammad Umair Yaqub.
# Made in P A K I S T A N

# Import necessary modules
import pyttsx3
import PyPDF2

# Open the PDF file in read-binary mode
pdfFile = open('file.pdf', 'rb')

# Create a PdfFileReader object to read the PDF file
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# Initialize the pyttsx3 text-to-speech engine
speaker = pyttsx3.init()

# Loop through each page in the PDF file
for pageNum in range(pdfReader.numPages):

    # Extract the text from the current page
    text = pdfReader.getPage(pageNum).extractText()

    # Use the speaker to read the text out loud
    speaker.say(text)
    speaker.runAndWait()

# Stop the speaker from speaking
speaker.stop()
