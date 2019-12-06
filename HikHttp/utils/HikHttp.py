import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin



class HikClient():
    def __init__(self, host, login=None, password=None, timeout=3):
        self.host = host
        self.login = login
        self.password = password
        self.timeout = timeout
        self.req = self._check_session()



    def _check_session(self):
        """Check the connection with device

         :return request.session() object
        """
        full_url = urljoin(self.host, 'ISAPI/System/status')
        session = requests.session()
        session.auth = HTTPBasicAuth(self.login, self.password)
        response = session.get(full_url)
        if response.status_code == 401:
            session.auth = HTTPDigestAuth(self.login, self.password)
        return session


    def get_frame(self):
        return self.req.get(url=urljoin(self.host, 'ISAPI/Streaming/channels/102/picture'),
                            timeout=self.timeout, stream=True)