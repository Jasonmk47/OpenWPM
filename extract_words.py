from bs4 import BeautifulSoup
import re
import sys

def main():
	with open(sys.argv[1], 'r') as myfile:
		data = myfile.read().replace('\n', '')

	data = re.subn(r'<(script).*?</\1>(?s)', '', data)[0]
	data = re.subn(r'<(noscript).*?</\1>(?s)', '', data)[0]
	data = re.subn(r'<(style).*?</\1>(?s)', '', data)[0]
	soup = BeautifulSoup(data, 'html.parser')

	print(soup.get_text())

if __name__ == '__main__':
	main()