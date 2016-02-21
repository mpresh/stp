from pprint import pprint
import requests
from bs4 import BeautifulSoup


URL = "http://insidertrading.org/"

def get_page():
    html = requests.get(URL).text
    return html


def get_records():
    data = []
    html = get_page()
    soup = BeautifulSoup(html, 'html.parser')
    
    table = soup.find('table', attrs={'id':'tracker'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
                
    return data
    
if __name__ == "__main__":
    pprint(get_records())
