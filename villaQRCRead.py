from pyzbar import pyzbar; from datetime import *
import cv2

details = "Contact Tracing Information.txt"

def time_registry(icon):
    BCHScan = pyzbar.decode(icon)
    for info in BCHScan:
        a, b, c, d = info.rect
        TxtBCHFile = info.data.decode('utf-8')
        cv2.rectangle(icon, (a, b),(a+c, b+d), (0, 0, 255), 3)
        TxtFont = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(icon, TxtBCHFile, (a + 10, b - 10), TxtFont, 1.0, (255, 255, 255), 2)
        local_time = datetime.now()
        datezone = local_time.strftime("%H:%M")
        timezone = local_time.strftime("%B %d, %Y")
        with open(details, "w") as update:
            update.write(TxtBCHFile + (f"\n>>> REAL-TIME MANAGEMENT SYSTEM <<< \nDate Tracking Record: {datezone}\nTime Tracking Record: {timezone}"))
    return icon

def webcamExtract():
    aperture = cv2.VideoCapture(0)
    link, icon = aperture.read()
    while link:
        link, icon = aperture.read()
        icon = time_registry(cv2.resize(icon, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR_EXACT))
        cv2.imshow("VILLARIZA QR CODE SCANNER", icon)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    aperture.release()
    cv2.destoryAllWindows()

webcamExtract()