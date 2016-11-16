import sqlite3 as sql
import webbrowser
import re
from automation import TaskManager, CommandSequence


SQL_Query = '''SELECT DISTINCT * FROM links_found
WHERE location NOT LIKE "https://www.facebook%"
AND location NOT LIKE "https://www.pinterest%"
AND location NOT LIKE "https://www.twitter%"
AND location NOT LIKE "https://itunes%"
AND location NOT LIKE "http://wda.biz/mrmxub"
AND location NOT LIKE "http://theatlantic.tumblr.com/"
AND location NOT LIKE "https://twitter%"
AND location NOT LIKE "https://www.linkedin%"
AND location NOT LIKE "%.pdf%"
AND location NOT LIKE "https://www.theatlantic.com/author%"
AND location NOT LIKE "https://www.theatlantic.com/category/%"
AND location NOT LIKE "http://www.theatlantic.com/category/%"
AND location NOT LIKE "https://www.theatlantic.com/projects/%"
AND location NOT LIKE "https://www.theatlantic.com/subscribe/%"
AND location NOT LIKE "http://www.theatlantic.com/follow-the-atlantic/#follow-rssfeeds"
AND location NOT LIKE "https://www.theatlantic.com/newsletters/sign-up/"
AND location NOT LIKE "https://www.theatlantic.com/terms-and-conditions/"
AND location NOT LIKE "https://www.theatlantic.com/locator/subscribe-magazine/"
AND location NOT LIKE "http://www.theatlantic.com/"
AND location NOT LIKE "https://www.theatlantic.com/"
AND location NOT LIKE "https://www.theatlantic.com/#"
AND location NOT LIKE "https://accounts%"'''


def main():
	pattern = re.compile("https?://www.theatlantic.com/[A-Za-z0-9-]*/$");

	wpm_db = "/home/jason/Desktop/crawl-data.sqlite"
	conn = sql.connect(wpm_db)
	cur = conn.cursor()
	cur.execute(SQL_Query)
	native_ad_links = cur.fetchall()

	# Loads the manager preference and sthe default browser dictionaries
	manager_params, browser_params = TaskManager.load_default_params(1)

	# Update TaskManager configuration (use this for crawl-wide settings)
	manager_params['data_directory'] = '~/Desktop/analysis'
	manager_params['log_directory'] = '~/Desktop/analysis'
	manager = TaskManager.TaskManager(manager_params, browser_params)

	for idx, link in enumerate(native_ad_links):
		if not pattern.match(link[1]):
			print idx
			print link
			command_sequence = CommandSequence.CommandSequence(link[1])
			command_sequence.get(sleep=0, timeout=180)
			command_sequence.dump_page_source("ads" + str(idx), 120)
			manager.execute_command_sequence(command_sequence, index="**")

	manager.close()

if __name__ == "__main__":
	main()