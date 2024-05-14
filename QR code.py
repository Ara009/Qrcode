import qrcode

img = qrcode.make("Hello world!, This is Aravind.")
img.save("mycode.png")

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)

qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
img.save("advantage.png")