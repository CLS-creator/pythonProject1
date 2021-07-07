
# Generate
import pyqrcode

url = pyqrcode.create("developer-factory.de", error= 'H')


url.png("data/qrcode.png", module_color=(0,255,0,255), background=(0,0,0,255), scale=5)
