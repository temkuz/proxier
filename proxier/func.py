import requests


def __get_content(url):
    resp = requests.get(url)
    return resp.text


def save(name, url):
    with open(f'{name}.txt', 'w') as f:
        proxies = __get_content(url)
        f.writelines(proxies)
