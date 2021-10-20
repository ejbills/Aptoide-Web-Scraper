import re
import validators

from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape(url) -> list:
    scraped_data = []

    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

    # Finds game title element by "name" attribute
    title = soup.find("meta", itemprop="name")
    # Finds version through "LatestVersion" attribute
    version = soup.find("div", {"class": re.compile('.*mini-versions__LatestVersion.*')})
    # Finds download number through "Info" attribute
    num_downloads = soup.find("span", {"class": re.compile('.*mini-stats__Info.*')})
    # Finds release date through "VersionDate" attribute
    release_date = soup.find("div", {"class": re.compile('.*mini-versions__VersionDate.*')})
    # Finds version through "DescBody" attribute
    description = soup.find("div", {"class": re.compile('.*description__DescBody.*')})

    # Returns data
    scraped_data.append(title['content'] if title else 'No data found')
    scraped_data.append(version.text if version else 'No data found')
    scraped_data.append(num_downloads.text if num_downloads else 'No data found')
    scraped_data.append(re.sub('[()]', '', release_date.text) if release_date else 'No data found')
    scraped_data.append(description if description else 'No data found')

    return scraped_data

def url_validation(url) -> bool:
    # Verifies input URL is valid and contains 'aptoide.com'
    return True if validators.url(url) and 'aptoide.com' in url else False
