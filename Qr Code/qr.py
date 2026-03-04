import qrcode as q

def make_qr(url, filename):
    img = q.make(url)
    img.save(filename)
