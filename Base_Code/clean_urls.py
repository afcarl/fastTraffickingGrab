urls = open("urls_to_scrape.txt","r")
urls_to_scrape = []
for i in urls:
    if ".html" in i:
        urls_to_scrape.append(i)
urls.close()
urls = open("urls_to_scrape.txt","w")
for i in urls_to_scrape:
    urls.write(i)
urls.close()
