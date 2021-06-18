import requests, datetime

now = datetime.datetime.now()
current_date = now.date()


# downloading the web page on our device
def url_to_txt(url, filename='world.html', save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f'world_{current_date}.html', 'w') as f:
                f.write(html_text)
        return html_text
    return ""

url = 'https://www.boxofficemojo.com/year/world/'

url_to_txt(url, save=True)




