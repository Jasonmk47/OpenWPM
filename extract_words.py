from bs4 import BeautifulSoup
import re
import sys

def main():
	with open(sys.argv[1], 'r') as myfile:
		data = myfile.read()

	data = re.subn(r'<(script).*?</\1>(?s)', '', data)[0]
	data = re.subn(r'<(noscript).*?</\1>(?s)', '', data)[0]
	data = re.subn(r'<(style).*?</\1>(?s)', '', data)[0]
	data = re.subn(r'\n+', '\n', data)[0]
	soup = BeautifulSoup(data, 'html.parser')

	print(soup.get_text().encode('utf-8'))

if __name__ == '__main__':
	main()