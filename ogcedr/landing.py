from ogcedr.utils.urls import url
from ogcedr.utils.helper import get_data

landing_urls = url().landing_urls()

def metadata(f="json") -> dict:
    data = get_data(landing_urls["landing_url"],f)
    return data



