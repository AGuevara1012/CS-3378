# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

#professor sites
url_1 = 'https://cs.txstate.edu/accounts/profiles/jg66/' #Dr. Byron Gao
url_2 = 'https://cs.txstate.edu/accounts/profiles/xc10/' #Dr. Xiao Chen
url_3 = 'https://cs.txstate.edu/accounts/profiles/qg11/' #Dr. Qijun Gu


def extract(url):

    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    name = ''
    education = ''
    research = ''
    email = ''
    webpage = ''

    #get name of professor
    name = getName(url, name, soup)
        
    #get education info for professor
    education = getEducation(url, education, soup)

    #get research info for professor
    research = getResearch(url, research, soup)

    #get email address for professor
    email = getEmail(url, email, soup)

    #get webpage info for professor
    webpage = getWebpage(url, webpage, soup)

    #write information to file
    writeFile(name, education, research, email, webpage)

def getName(url, name, soup):
    main_content = soup.find('div', attrs = {'class': 'page-heading clearfix'})
    name = main_content.find('h1').text
    name = " ".join(name.split())        
    return name

def getEducation(url, education, soup):
    main_content = soup.find_all('div', attrs = {'class': 'panel-body'}, limit = 2)
    main_content = main_content[1]
    education = main_content.find('p').text
    education = " ".join(education.split())
    return education

def getResearch(url, research, soup):
    main_content = soup.find_all('div', attrs = {'class': 'panel-body'}, limit = 2)
    main_content = main_content[0]
    research = main_content.find('p').text
    research = " ".join(research.split())
    return research

def getEmail(url, email, soup):
    main_content = soup.find('img', attrs = {'class': 'email-image'})
    email = str(main_content)
    email = re.findall(r'(?<=email )[a-zA-Z0-9]*@[a-zA-Z]*\.edu', email)
    for var in email:
        email = var
    return email

def getWebpage(url, email, soup):
    for link in soup.find('h3'):
        webpage = link.get('href')
    return webpage

def writeFile(name, education, research, email, webpage):
    file = open(name + ".txt", 'w')
    file.write("Name: " + name + "\n")
    file.write("Education: " + education + "\n")
    file.write("Research interests: " + research + "\n")
    file.write("Email: " + email + "\n")
    file.write("Webpage: " + webpage + "\n")
    file.close()
    return

    
    
   
def main():
    
    extract(url_1)
    extract(url_2)
    extract(url_3)

if __name__ == "__main__":
    main()



 
        




        




