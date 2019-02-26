import json
import requests


class url(object):
    HOST = "http://gd2u.line.naver.jp"

    LONG_POLLING = "/P4"
    NORMAL_POLLING = "/NP4"
    NORMAL = "/S4"
    COMPACT_MESSAGE = "/C5"
    REGISTRATION = "/api/v4/TalkService.do"
    SESSION_KEY = "/authct/v1/keys/line"
    CERTIFICATE = "/Q"

    USER_AGENT = "DESKTOP:MAC:10.10.2-YOSEMITE-x64(4.1.2)"
    LINE_APPLICATION = "DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.1.2"

    _session = requests.session()
    Headers = {}
    _pincode = None

    @classmethod
    def parseUrl(self, path):
        return self.HOST + path

    @classmethod
    def get_json(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    @classmethod
    def set_Headers(self, argument, value):
        self.Headers[argument] = value