# Assignment 10

# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger.

# QRCODE Library has been used due to the form request instructed from the Assignment on PLD.
import qrcode

"""
LAYOUT AND DIMENSIONS FOR VILLARIZA QR CODE PNG FILE.
"""
encode = qrcode.QRCode(
    # The general size of the QR Code.
    box_size = 10,
    # Alignment Pattern of the BCH Code.
    version = 5,
    # Distance from the QR Dataset Symbol Pattern
    border = 2,
    # Reed-Solomon Error Correction (H = High )= 30% of data bytes can be stored.
    error_correction = qrcode.constants.ERROR_CORRECT_H 
)

"""
QR CODE GENERATOR LAYOUT
"""
# Data has been stored on the QR Code in an Alphanumeric Pattern.
details = 'Test, Hello World!'; encode.add_data(details)
# QR Code Presets and Illustrative Design for the making of PNG File.
encode.make(fit = True); icon = encode.make_image(back_color = 'black', fill_color = 'cyan')
# The QR code will be saved from its Python Settings upon the dictation of the naming file.
icon.save('Villariza QR Code.png')