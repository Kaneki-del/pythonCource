import requests
from bs4 import BeautifulSoup



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
    url = 'https://news.ycombinator.com/'
    current_page_relative_path = 'news'
    for page in range(3):
        full_url = url + current_page_relative_path
        res = requests.get(full_url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            links =   soup.select('.titleline')
            subtext =  soup.select('.subtext')
            print(f'_____________________result from page: {page}_____________________')
            print(get_info(links, subtext))
            more_links_tag = soup.find('a', class_= 'morelink')
            if more_links_tag and more_links_tag.get('href'):
                current_page_relative_path = more_links_tag.get('href')
            else:
                print(f"No 'More' link found on page {page}. End of pages.")
                break 
        else: 
            print('somting went wrong')
            break


main()
