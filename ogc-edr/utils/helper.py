import requests

def get_data(endpoint,response_format) -> dict:
    if response_format == "json":
        data = requests.get(
            endpoint,
            headers = {
                "accept": f"application/{response_format}"
            }
        )
        return data.json()
    elif response_format == "html":
        html_data = (
            endpoint + "&f=html" if ("?" in endpoint) else endpoint + "?f=html"
        )
        raw_data = requests.get(html_data)
        return raw_data.text
