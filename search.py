#!bin/usr/python

"""
*type url from which data to be extracted
*type html tag 
"""

import urllib 
from bs4  import BeautifulSoup


class HtmlPage(object):
	
	def __init__(self, url):
		self.url = url
		self.data = None

	def load(self):
		html = urllib.urlopen(self.url).read()
		self.data = BeautifulSoup(html, 'lxml')
		return self.data

	def parse(self, tag):
		if self.data.find(tag) != None:
			for item in self.data.findAll(tag):
				print item.get_text()
		else:
			print "no data found"



def main():
	URLlast = raw_input("enter url: ")	
	URLfirst = "http://"
	URL = URLfirst + URLlast
	TAG = raw_input("enter tag type(h1,h2,a,..): ")
	currentData = HtmlPage(URL)
	currentData.load()
	currentData.parse(TAG)
	
if __name__ == "__main__":
	main()	
