# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_base.ipynb.

# %% auto 0
__all__ = ['ISTAT', 'CustomHttpAdapter', 'get_custom_ssl_session']

# %% ../nbs/00_base.ipynb 1
import requests
import urllib3
import ssl
import warnings
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# %% ../nbs/00_base.ipynb 4
class ISTAT:
    """Base class that provides useful functions to communicate with ISTAT API"""
    def __init__(self):
        self.base_url = "http://sdmx.istat.it/SDMXWS/rest"
        self.agencyID = "IT1"

    def _request(self, path, **kwargs):
        """Make a request to ISTAT API given a 'path'"""
        if "headers" in kwargs.keys():
            headers = kwargs["headers"]
        else:
            headers = {}
        url = "/".join([self.base_url, path])
        warnings.filterwarnings('ignore', message='Unverified HTTPS request')        
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        # response = requests.get(url, headers=headers, verify = False)
        session = get_custom_ssl_session()
        # response = session.get(url, headers=headers, verify=False)
        # session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        response = session.get(url, headers=headers, verify = False)
        return response

class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    '''Transport adapter" that allows us to use custom ssl_context.'''

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)
        
def get_custom_ssl_session():
    '''Get a session with a custom ssl context'''
    session = requests.session()        
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4
    session.mount('https://', CustomHttpAdapter(ctx))
    return session
