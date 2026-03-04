import qrcode as q

def make_qr(url):
    img = q.make(url)
    img.save("C:\\Users\\kimst\\Downloads\\qr.png")
