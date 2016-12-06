import sqlite3 as sql
import webbrowser
import re
from automation import TaskManager, CommandSequence


SQL_Query = '''SELECT DISTINCT * FROM links_found
WHERE location LIKE "http://www.nytimes.com/20%"
AND location NOT LIKE "%index.html%"'''

def main():

	wpm_db = "/home/jason/Desktop/NYT/crawl-data.sqlite"
	conn = sql.connect(wpm_db)
	cur = conn.cursor()
	cur.execute(SQL_Query)
	article_links = cur.fetchall()

	# Loads the manager preference and sthe default browser dictionaries
	manager_params, browser_params = TaskManager.load_default_params(1)

	# Update TaskManager configuration (use this for crawl-wide settings)
	manager_params['data_directory'] = '~/Desktop/NYT/analysis'
	manager_params['log_directory'] = '~/Desktop/NYT/analysis'
	manager = TaskManager.TaskManager(manager_params, browser_params)

	for idx, link in enumerate(article_links):
		print idx
		print link
		command_sequence = CommandSequence.CommandSequence(link[1])
		command_sequence.get(sleep=0, timeout=180)
		command_sequence.dump_page_source("nyt_articles_" + str(idx), 120)
		manager.execute_command_sequence(command_sequence, index="**")

	manager.close()

if __name__ == "__main__":
	main()