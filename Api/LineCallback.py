class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def Pinverified(self, pin):
        self.callback("Input pincode : " + pin)

    def QrUrl(self, url):
        self.callback("Access : " + url)
