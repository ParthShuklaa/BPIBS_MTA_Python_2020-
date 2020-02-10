import pyqrcode

RegisterationLink = "https://www.linkedin.com/in/parth-shukla-09205239"
MyQRCODE = pyqrcode.create(RegisterationLink)
MyQRCODE.svg("MyLinkedLink.svg")