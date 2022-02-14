from pyzbar import pyzbar; from datetime import *
import cv2

details = "Contact Tracing Information.txt"

"""
DEF FUNCTION FOR THE CALENDAR OF UPDATED REGISTRY - TO BE IMPORTED ON THE CONTACT TRACING INFORMATION TEXT FILE
"""
def time_registry(icon):
    BCHScan = pyzbar.decode(icon)
    for info in BCHScan:
        a, b, c, d = info.rect # Settling up global parameters for the Font Layout on the Live Webcam.
        TxtBCHFile = info.data.decode('utf-8') # ASCII Standard Unicode Character
        cv2.rectangle(icon, (a, b),(a+c, b+d), (0, 0, 255), 3) # ASCII Font Density
        TxtFont = cv2.FONT_HERSHEY_COMPLEX_SMALL # Modifying Font Type
        cv2.putText(icon, TxtBCHFile, (a + 10, b - 10), TxtFont, 1.0, (255, 255, 255), 2) # Layout and Text Color for the Font Presets.
        local_time = datetime.now() # REAL-TIME GMT+8 / UTC+9 PHILIPPINES
        datezone = local_time.strftime("%B %d, %Y") # MONTH, DAY, AND YEAR (e.g. January 1, 2022)
        timezone = local_time.strftime("%H:%M") # HOURS AND MINUTES (e.g. 09:45)
        """
        TEXT FILE WITHIN THE SAME FOLDER HAS THE AUTHORIZATION TO GET OVERWRITTEN.
        """
        with open(details, "w") as update:
            update.write(TxtBCHFile + (f"\n\n>>> REAL-TIME MANAGEMENT SYSTEM <<< \nDate Tracking Record: {datezone}\nTime Tracking Record: {timezone}"))
    return icon; # Brings back the variable upon the Font Layout - illustration on the Live Webcam.

"""
DEF FUNCTION FOR A LIVE QR CODE SCANNER THROUGH INTEGRATED/OUTPUT DEVICE WEBCAM
"""
def webcamExtract():
    aperture = cv2.VideoCapture(0) # Acts as an Intermediary Between the Python Progam and the Operating System.
    link, icon = aperture.read() # Reads a specific context of data patterns alongside of its pixels.
    while link: # Loop is used to prevent the unnecesarry closing of Webcam before QR Code is detected and decoded.
        link, icon = aperture.read() # Loop is iterated to refresh the command system.
        icon = time_registry(cv2.resize(icon, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR_EXACT)) # Programmed Font will be displayed between the Live Webcam.
        cv2.imshow("VILLARIZA QR CODE SCANNER", icon) # The Live Webcam Shall Run Together with a Detected QR Code Scanner with its Presented Font Layout alongside of the Stored Input Data.
        if cv2.waitKey(1) & 0xFF == 43: # 43 Characters are Present within the first code-block of dictionary line: THE COVID-19 HEALTH MONITOR - CONTACT TRACING FORM
            break # Break is used to shut down the endless looping after the QR Code has been detected-decoded.
    aperture.release() # Operating System will then be informed - Allocated Memory shall despise at any moment.
    cv2.destroyAllWindows() # A Shut Down Command for the Webcam Program.

webcamExtract() # Initializing the overall Python Program.