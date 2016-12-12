from bs4 import BeautifulSoup
import re
import sys

def main():
	with open(sys.argv[1], 'r') as myfile:
		data = myfile.read()

	data = re.sub(r'<(script).*?</\1>(?s)', '', data)
	data = re.sub(r'<(noscript).*?</\1>(?s)', '', data)
	data = re.sub(r'<(style).*?</\1>(?s)', '', data)

	soup = BeautifulSoup(data, 'html.parser')
	data = soup.get_text().encode('utf-8')

	data = re.sub('skip ad', '', data)
	data = re.sub('PAID FOR AND POSTED BY', '', data)
	data = re.sub("The news and editorial staffs of The New York Times had no role in this post's preparation.", '', data)


	data = re.sub('Continue reading the main story', '', data)
	data = re.sub('Share this comment on Facebook', '', data)
	data = re.sub('Share this comment on Twitter', '', data)
	data = re.sub('Sign up with Facebook', '', data)
	data = re.sub('Sign up with Twitter', '', data)
	data = re.sub('Log in with Facebook', '', data)
	data = re.sub('Log in with Google', '', data)
	data = re.sub('A Type size small', '', data)
	data = re.sub('A Type size medium', '', data)
	data = re.sub('Subscribe to continue reading', '', data)
	data = re.sub('A Type size large', '', data)
	data = re.sub('Close this modal window', '', data)
	data = re.sub('Forgot password?', '', data)
	data = re.sub('Clear this text input', '',data)
	data = re.sub('NYTimes.com no longer supports Internet Explorer 9 or earlier. Please upgrade your browser.', '', data)

	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+$', '', data)
	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+$', '', data)
	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+ [A-Za-z0-9\.\:\'\-]+$', '', data)

	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+ [A-Za-z0-9\.\:\'\-]+ [A-Za-z0-9\.\:\'\-]+$', '', data)
	data = re.sub('(?m)^[A-Za-z0-9\.\:\'\-]+ & [A-Za-z0-9\.\:\'\-]+$', '', data)

	data = re.sub('\n+' , '\n', data)

	data = data.split('\xa9 2016 The New York Times Company')[0]
	data = re.sub('\C2' , '', data)


	print(data)


if __name__ == '__main__':
	main()