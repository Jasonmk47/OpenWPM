from bs4 import BeautifulSoup
import webbrowser
from automation import TaskManager, CommandSequence

def main():
	with open('/home/jason/Desktop/NYT/sources/html.html', 'r') as myfile:
		soup = BeautifulSoup(myfile.read(), 'lxml')
		links = []
		with open('/home/jason/Desktop/NYT/sources/links.txt', 'w') as outfile:
			for item in soup.find_all('a', attrs={'data-link' : True}):
				if "data-link" in item.attrs:
					if ".html" in item['data-link']:
						outfile.write(item['data-link'])
						outfile.write("\n")
						links.append(item['data-link'])


	# Go and dump the source for each
	manager_params, browser_params = TaskManager.load_default_params(1)

	# Update TaskManager configuration (use this for crawl-wide settings)
	manager_params['data_directory'] = '~/Desktop/NYT/analysis'
	manager_params['log_directory'] = '~/Desktop/NYT/analysis'
	manager = TaskManager.TaskManager(manager_params, browser_params)

	for idx, link in enumerate(links):
		command_sequence = CommandSequence.CommandSequence(link)
		command_sequence.get(sleep=0, timeout=180)
		command_sequence.dump_page_source("nyt_ad_" + str(idx), 120)
		manager.execute_command_sequence(command_sequence, index="**")

	manager.close()


	

if __name__ == '__main__':
	main()