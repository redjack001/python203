# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:48:10 2020

@author: redjack
"""


import cv2 
import pytesseract
import time

start_time = time.process_time()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = cv2.imread('the_guardian_extract.jpg')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

#print(text)

updated_text = text.replace("\n"," ")
updated_text = updated_text.replace("- ","")

print(updated_text)


print (time.process_time() - start_time, "seconds")
