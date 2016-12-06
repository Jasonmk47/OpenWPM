from automation import TaskManager, CommandSequence

# Variables for what site
site = 'http://www.tbrandstudio.com/our-work/'

# Loads the manager preference and sthe default browser dictionaries
manager_params, browser_params = TaskManager.load_default_params(1)

# Update TaskManager configuration (use this for crawl-wide settings)
manager_params['data_directory'] = '~/Desktop/NYT'
manager_params['log_directory'] = '~/Desktop/NYT'

# Instantiates the measurement platform
# Commands time out by default after 60 seconds
manager = TaskManager.TaskManager(manager_params, browser_params)

command_sequence = CommandSequence.CommandSequence(site)

# Start by visiting the page
command_sequence.get(sleep=0, timeout=180)
#command_sequence.scroll_bottom(timeout=180)
command_sequence.dump_page_source("nyt_ads", 120)

manager.execute_command_sequence(command_sequence, index=None) 

# Shuts down the browsers and waits for the data to finish logging
manager.close()
