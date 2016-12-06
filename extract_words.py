from bs4 import BeautifulSoup
import re
import sys

def main():
	with open(sys.argv[1], 'r') as myfile:
		data = myfile.read()

<<<<<<< HEAD
	data = re.sub(r'<(script).*?</\1>(?s)', '', data)
	data = re.sub(r'<(noscript).*?</\1>(?s)', '', data)
	data = re.sub(r'<(style).*?</\1>(?s)', '', data)

	soup = BeautifulSoup(data, 'html.parser')
	data = soup.get_text().encode('utf-8')

	data = re.sub('skip ad', '', data)
	data = re.sub('PAID FOR AND POSTED BY', '', data)
	data = re.sub('Continue reading the main story', '', data)
	
	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+$', '', data)
	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+$', '', data)
	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+ [A-Za-z0-9\.\:\'\-]+$', '', data)

	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+ [A-Za-z0-9\.\:\'\-]+ [A-Za-z0-9\.\:\'\-]+$', '', data)
	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+ & [A-Za-z0-9\.\:\'\-]+$', '', data)

	print(data)

if __name__ == '__main__':
	main()