import sqlite3 as sql
import webbrowser
from automation import TaskManager, CommandSequence


def main():
	wpm_db = "/home/jason/Desktop/crawl-data.sqlite"
	conn = sql.connect(wpm_db)
	cur = conn.cursor()
	cur.execute("SELECT DISTINCT location AS link FROM links_found WHERE location LIKE '%eb2.%' ")
	native_ad_links = cur.fetchall()

	# Loads the manager preference and sthe default browser dictionaries
	manager_params, browser_params = TaskManager.load_default_params(1)

	# Update TaskManager configuration (use this for crawl-wide settings)
	manager_params['data_directory'] = '~/Desktop/analysis'
	manager_params['log_directory'] = '~/Desktop/analysis'
	manager = TaskManager.TaskManager(manager_params, browser_params)

	for idx, link in enumerate(native_ad_links):
		command_sequence = CommandSequence.CommandSequence(link[0])
		command_sequence.get(sleep=0, timeout=120)
		command_sequence.dump_page_source("ads" + str(idx), 120)
		manager.execute_command_sequence(command_sequence, index="**")

	manager.close()

if __name__ == "__main__":
	main()