from urllib2 import urlopen
from bs4 import BeautifulSoup, SoupStrainer

url = "http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=2005,2014"
source = urlopen(url).read()

