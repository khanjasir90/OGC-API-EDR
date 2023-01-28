import requests

def get_data(endpoint,response_format) -> dict:
    print(endpoint)
    if response_format == "json":
        data = requests.get(
            endpoint,
            headers = {
                "accept": f"application/{response_format}"
            }
        )
        return data.json()