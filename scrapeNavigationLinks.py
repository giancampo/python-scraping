# written in Python 3: this could cause issues with earlier versions of Python

from lxml import html
import requests

urls = open("urls.txt", "r")
results_file = open("results.txt", "a+")

for item in urls:
    url = item.rstrip("\n")
    page = requests.get(url)
    tree = html.fromstring(page.content)
    text = tree.xpath('//ul[@id="menu-primary-items"]/li/a/text()')
    results_file.write("%s,%s\n" % (url, text))
    print ("SCRAPING " + url)
    print (text, "\n")

results_file.close()
