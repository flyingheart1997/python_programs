# Create Simple QrCode

# import qrcode as qr
# qrCode = qr.make("https://koushik.vercel.app/")
# qrCode.save("koushik_qrCode.png")


# Modify QrCode
import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
url = input("Enter URL : ")
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="gray")
img.save("koushik_qr.png")
