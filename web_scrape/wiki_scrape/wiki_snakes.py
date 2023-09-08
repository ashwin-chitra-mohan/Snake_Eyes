import wikipediaapi
import urllib.parse

wiki_wiki = wikipediaapi.Wikipedia('Ashwin (ashwin.vikaasa@gmail.com', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI)

file=open("snakes_list.txt","r")
count=0
for snake in file:
    print(snake)
    f1 = open("SNAKES/"+urllib.parse.unquote(str(snake).strip())+".txt", "w", encoding="utf-8")
    p_wiki = wiki_wiki.page(urllib.parse.unquote(str(snake).strip()))
    f1.write(str(p_wiki.text))
    f1.close()
    count = count+1

print(count)
#    print(p_wiki.text)
#     break

# a = 'Viperidae'
# p_wiki = wiki_wiki.page(a)
# print(p_wiki.text)

# page_py = wiki_wiki.page(a)
# print("Page - Title: %s" % page_py.title)
# # Page - Title: Python (programming language)s
# print("Page - Summary: %s" % page_py.summary[0:6000])
