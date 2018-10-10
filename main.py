import requests
import re

def getHtmlContent(url):
    page = requests.get(url)
    return page.text

def getJPGs(html):
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)')
    	
    jpgs = re.findall(jpgReg, html)
    return jpgs


def downloadJPG(imgUrl, fileName):
    from contextlib import closing
    with closing(requests.get(imgUrl,stream = True)) as resp:
        with open(fileName,'wb') as f:
            for chunk in resp.iter_content(128):
                f.write(chunk)

def batchDownloadJPGs(imgUrls, path = './'):
    count = 1
    for url in imgUrls:
        downloadJPG("https://www.visvim.tv" + url,''.join([path,'{0}.jpg'.format(count)]))
        print("Downloading Image Number", count)
        count += 1

def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)
    
def main():
    url = "https://www.visvim.tv/lookbook/fw18-19/visvim/"
    download(url)

main()
