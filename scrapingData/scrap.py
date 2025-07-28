import requests
from bs4 import BeautifulSoup
url = 'https://news.ycombinator.com/news'
res = requests.get(url)


# def get_value(dic):
#     return dic['point']

def get_info(links, subtext):
    hr = []
    for index, it in enumerate(links):
        title = it.getText()
        herf = it.find('a').get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace("points", ""))
            if (points > 99):
                hr.append({'title': title, 'link': herf, 'point':points})
    hr.sort(reverse=True, key = lambda dic: dic['point'])
    return hr
def main():
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        links =   soup.select('.titleline')
        subtext =  soup.select('.subtext')
        print(get_info(links, subtext))
    else: 
        print('somting went wrong')


main()
