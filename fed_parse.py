import re
from BeautifulSoup import BeautifulSoup
from starflow import utils

def hasDataDownloadProgram(li):
    x = re.compile('.*\.aspx.*')
    return li.findAll('a',{'href':x}) != []

def extractRel(urlString):
    regex = re.compile('.*\.aspx\?rel=(.*)')
    return regex.match(urlString).groups()[0]

def getDataCodes(string):
    pattern = '([A-Z](\.[0-9]+)+)+'
    all = re.findall(pattern,string)
    return [match[0] for match in all]

def childrenContent(li):
    contents = [utils.Contents(child) for child in li.children()]

file = open('statisticsdata.htm')
linkTable =  BeautifulSoup(file,convertEntities='html').find('table',{'class':'stats'})
headers = linkTable.findAll('h2')
links = [header.findNext().findAll('li') for header in headers]

res = [[(utils.Contents(h), utils.Contents(l.findAll('a')[0]), getDataCodes(utils.Contents(l.findAll('a')[0]))) for l in L] for (L,h) in zip(links,headers)]

