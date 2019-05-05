from lxml import html
import requests

urls = open("urls.txt", "r")
results_file = open("results.txt", "w")

for item in urls:
    url = item.rstrip("\n")
    page = requests.get(url)
    tree = html.fromstring(page.content)
    text = tree.xpath('//h3[@class="r"]/a/@href')
    results_file.write("%s,%s\n" % (url, text))
    print ("SCRAPING " + url)
    print (text, "\n")

results_file.close()
