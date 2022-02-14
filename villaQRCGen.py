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
from PIL import Image

"""
LAYOUT AND DIMENSIONS FOR VILLARIZA QR CODE PNG FILE.
"""
encode = qrcode.QRCode(
    # The general size of the QR Code.
    box_size = 10,
    # Alignment Pattern of the BCH Code.
    version = 1,
    # Distance from the QR Dataset Symbol Pattern
    border = 2,
    # Reed-Solomon Error Correction (H = High ) = 30% of data bytes can be stored.
    error_correction = qrcode.constants.ERROR_CORRECT_H 
)

"""
QR CODE GENERATOR LAYOUT
"""
# Data has been stored on the QR Code in an Alphanumeric Pattern.
details = """THE COVID-19 HEALTH MONITOR - CONTACT TRACING FORM
MANILA, PHILIPPINES

Personal Information
    Full Name       : Fritz Cedrick V. Villariza
    Sex / Gender    : Male (M)
    Age             : 22
    Birthdate       : January 1, 2000
    Home Address    : 310 San Rafael Street, San Miguel 1005, Manila City
    Phone Number    : 0912-345-6789
    Electronic Mail : fcv1995@yahoo.com

Medical Information
    Weight (in kgs) : 77
    Height (in cms) : 6'0
    Comorbidity     : Bronchial Asthma
    Allergy         : Nicotine
    Condition (Now) : None

Vaccination Report
    Fully Vaccinated? (Maximum of Two (2) Dose) If YES, select the brand you received and include the date and place; if NO, please specify.
        > June 6, 2021     : Sinovac-CoronaVac (Manila Sports Complex)
        > July 6, 2021     : Sinovac-CoronaVac (Manila Sports Complex)

    Already had a BOOSTER Vaccine? If YES, select the brand you received and include the date and place; if NO, please specify.
        > January 15, 2022 : BioNTech, Pfizer  (Manila Sports Complex)"""

encode.add_data(details)
# QR Code Presets and Illustrative Design for the making of PNG File.
encode.make(fit = True); icon = encode.make_image(back_color = 'white', fill_color = 'black').convert('RGB')
# The QR code will be saved from its Python Settings upon the dictation of the naming file.

"""
LOGO IMAGE HEADER FOR THE QR CODE PNG FILE (DESIGN PURPOSES)
"""
logo_display = Image.open('MARIN KITAGAWA.png') # PNG is imported through Image module.
logo_display.thumbnail((180, 180)) # Aspect Ratio of the imported PNG File.
logo_pos = ((icon.size[0] - logo_display.size[0]) // 2, (icon.size[1] - logo_display.size[1]) // 2) # Image Size Presets has been customized.
icon.paste(logo_display, logo_pos) # PNG is displayed through the "icon" global variable.

# The QR code will be saved from its Python Settings upon the dictation of the naming file.
icon.save('Villariza QR Code.png')