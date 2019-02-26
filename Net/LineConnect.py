# -*- coding: utf-8 -*-
import json
import rsa

from ..Gen import TalkService
from ..Gen.ttypes import *

from .LineServer import url

from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol

from .LineTransport import LineTransport
from ..Api.LineCallback import LineCallback


class LineConnect(object):
    _thriftTransport = None
    _thriftProtocol = None
    onLogin = False
    authToken = ""
    certificate = ""

    def __init__(self):
        self._transportOpen(url.HOST)
        self.callback = LineCallback(self.defaultCall)

    def _transportOpen(self, host, path=None):
        if path is not None:
            self._thriftTransport = LineTransport(host + path)
        else:
            self._thriftTransport = LineTransport(host)

        self._thriftProtocol = TCompactProtocol.TCompactProtocol(
            self._thriftTransport)

        self._client = TalkService.Client(self._thriftProtocol)

    def _login(self, email, passwordd, certificate=None, loginName='kaopy'):
        self._thriftTransport.targetPath(url.REGISTRATION)

        session_json = url.get_json(url.parseUrl(url.SESSION_KEY))

        self.certificate = certificate

        session_key = session_json['session_key']
        message = (chr(len(session_key)) + session_key +
                   chr(len(email)) + email +
                   chr(len(passwordd)) + passwordd).encode('utf-8')

        keyname, n, e = session_json['rsa_key'].split(",")
        pub_key = rsa.PublicKey(int(n, 16), int(e, 16))
        crypto = rsa.encrypt(message, pub_key).encode('hex')

        self._thriftTransport.targetPath(url.REGISTRATION)

        result = self._client.loginWithIdentityCredentialForCertificate(
            IdentityProvider.LINE, keyname, crypto, True, '127.0.0.1', loginName, certificate)

        if result.type == 3:
            # required pin verification
            url._pincode = result.pinCode

            self.callback.Pinverified(url._pincode)

            url.set_Headers('X-Line-Access', result.verifier)
            getAccessKey = url.get_json(
                url.parseUrl(url.CERTIFICATE), allowHeader=True)

            self.verifier = getAccessKey['result']['verifier']

            result = self._client.loginWithVerifierForCerificate(self.verifier)

            self.certificate = result.certificate
            self.authToken = result.authToken

            self._thriftTransport.setAccesskey(self.authToken)
            self.onLogin = True
            self._thriftTransport.targetPath(url.NORMAL)

        elif result.type == 2:
            pass

        elif result.type == 1:
            self.authToken = result.authToken

            self._thriftTransport.setAccesskey(self.authToken)
            self.onLogin = True
            self._thriftTransport.targetPath(url.NORMAL)

    def _tokenLogin(self, authToken):
        self._thriftTransport.targetPath(url.REGISTRATION)

        self._thriftTransport.setAccesskey(authToken)
        self.authToken = authToken
        self.onLogin = True
        self._thriftTransport.targetPath(url.NORMAL)

    def _qrLogin(self, keepLoggedIn=True, systemName="kaopy"):
        self._thriftTransport.targetPath(url.REGISTRATION)
        qr = self._client.getAuthQrcode(keepLoggedIn, systemName)

        self.callback.QrUrl("line://au/q/" + qr.verifier)

        url.set_Headers('X-Line-Application', url.LINE_APPLICATION)
        url.set_Headers('X-Line-Access', qr.verifier)

        verified = url.get_json(
            url.parseUrl(url.CERTIFICATE), allowHeader=True)
        vr = verified['result']['verifier']
        lr = self._client.loginWithVerifierForCertificate(vr)
        self._thriftTransport.setAccesskey(lr.authToken)
        self.authToken = lr.authToken
        self.onLogin = True

        self._thriftTransport.targetPath(url.NORMAL)

    def setCallback(self, callback):
        self.callback = LineCallback(callback)

    def defaultCall(self, str):
        print str

    def _logout(self):
        self._client.logoutSession(self.authToken)

        self._thriftTransport.setAccesskey("")