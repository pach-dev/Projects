# import modules
import qrcode
from PIL import Image

# taking image which user wants 
# in the QR code center
Logo_link = 'D:/UBCD/Cyber sec_Python scripts/Rembo/rembotv.jpg'

logo = Image.open(Logo_link)

# taking base width
basewidth = 80

# adjust image size
wpercent = (basewidth/float(logo.size[0])) # resizes the width of the logo
hsize = int((float(logo.size[1])*float(wpercent))) # resizes the height of the logo
logo = logo.resize((basewidth, hsize), Image.LANCZOS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H #QR Code has error correction capability to restore data if the code is dirty or damaged
)

# taking url or text
url = 'https://www.instagram.com/strembotv/'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'Green'

# adding color to QR code
QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('STRemboTVQR.png')

print('QR code generated!')
