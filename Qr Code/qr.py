import qrcode as q


## url: url you want people to click on on
## save_directory location on computer where you want to save the PNG file
## name of QR code you want 

def make_qr(url, save_directory, filename):
    location = save_directory + "\\" + filename + ".png"
    img = q.make(url)
    img.save(location)
