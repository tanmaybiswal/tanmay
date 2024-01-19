import pyqrcode
import png
from pyqrcode import QRCode
T="https://www.google.com"
url=pyqrcode.create(T)
url.svg("myqr.svg",scale=8)
url.png("myqr.png",scale=6)