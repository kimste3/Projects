import qrcode as q


class Qr_Generator:

    def __init__(self, url, save_directory, filename):
        self.url = url
        self.filename = filename
        self.save_directory = save_directory
        self.save_location_path = self.save_directory + "\\" + self.filename + ".png"
    
    def make_qr(self):
        
        img = q.make(self.url)
        img.save(self.save_location)

    def get_url(self):
        return self.url
    
    def get_save_location_path(self):
        return self.save_location_path
    
    def get_filename(self):
        return self.filename

    def get_save_diractory(self):
        return self.save_directory    