from requests import get

endpoint = "https://clck.ru/--"

def ru(url : str):
    try:
        response = get(
            endpoint,
            params = {"url" : url}
        )
        return response.text
    except:
        return None