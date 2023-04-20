import logging
import os
import datetime

#create a logger

logger = logging.getLogger('Web_scrapping_Logpose')
logger.setLevel(logging.DEBUG)

#create file handler that logs messages to a file

logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)
current_date_str = datetime.datetime.now().strftime('%Y-%m-%d')
log_file_path = os.path.join(logs_dir, f'{current_date_str}.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

#create formatter

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %()')

#adding formatter to file handler
file_handler.setFormatter(formatter)

#add file handler to logger
logger.addHandler(file_handler)

#create filter to exclude messages from certain sources

class ExcludeSourceFilter(logging.Filter):
    def __init__(self, source_name):
        self.source_name = source_name

    def filter(self, record):
        return record.name not in self.source_name

#add filter to logger

excluded_sources = ['requests','urllib3']
exclude_filter = ExcludeSourceFilter(excluded_sources)
logger.addFilter(exclude_filter)