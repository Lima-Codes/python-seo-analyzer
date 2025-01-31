import certifi
import urllib3


class Http():
    def __init__(self):
        user_agent = {'User-Agent': 'Mozilla/5.0'}
        self.http = urllib3.PoolManager(
            timeout=urllib3.Timeout(connect=1.0, read=2.0),
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where(),
            headers=user_agent
        )

    def get(self, url):
        sanitized_url = self.sanitize_url(url)
        return self.http.request('GET', sanitized_url)

    @staticmethod
    def sanitize_url(url):
        scheme, netloc, path, query, fragment = parse.urlsplit(url)
        path = parse.quote(path)
        sanitized_url = parse.urlunsplit((scheme, netloc, path, query, fragment))
        return sanitized_url

http = Http()
        
