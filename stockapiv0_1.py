from bs4 import BeautifulSoup
import requests
import time
import re
getSymbol = raw_input("Enter symbol: ")
r = requests.get('http://www.nasdaq.com/symbol/%s'%getSymbol)
soup = BeautifulSoup(r.content, 'html.parser')

while True:
	time.sleep(1)
	getLine = re.findall(r'id="qwidget_lastsale.............', str(soup))
	print soup.title.string
	get_num = re.search(r'[0-9.]+', str(getLine))
	if get_num:
		print 'Stock Price --> ', get_num.group()