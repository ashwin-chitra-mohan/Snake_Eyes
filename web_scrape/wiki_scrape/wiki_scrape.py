import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/List_of_snakes_by_common_name'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
count = 0
for link in soup.find_all('a'):
    if (str(link.get('href')).startswith('/wiki/')):
        print(str(link.get('href')))
        count = count+1
        if str(link.get('href')) == '/wiki/List_of_snakes':
            break

        
print(count)

f = open("test1.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
    if (str(link.get('href')).startswith('/wiki/')):
        data = link.get('href')
        f.write(data)
        f.write("\n")
        if str(link.get('href')) == '/wiki/List_of_snakes':
            break

f.close()
