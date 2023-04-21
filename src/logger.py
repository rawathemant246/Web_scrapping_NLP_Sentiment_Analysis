import logging
import os
from datetime import datetime

from logging import getLogger, DEBUG, FileHandler, Formatter, Filter

#create a logger
logger = getLogger('Project_log')
logger.setLevel(DEBUG)

#create file handler that logs messages to a file
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)
current_date_str = datetime.datetime.now().strftime('%Y-%m-%d')
log_file_path = os.path.join(logs_dir, f'{current_date_str}.log')
file_handler = FileHandler(log_file_path)
file_handler.setLevel(DEBUG)

#create formatter
formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s - %()')

#adding formatter to file handler
file_handler.setFormatter(formatter)

#add file handler to logger
logger.addHandler(file_handler)

#create filter to exclude messages from certain sources
class ExcludeSourceFilter(Filter):
    def __init__(self, source_name):
        self.source_name = source_name

    def filter(self, record):
        return record.name not in self.source_name

#add filter to logger
excluded_sources = ['requests','urllib3']
exclude_filter = ExcludeSourceFilter(excluded_sources)
logger.addFilter(exclude_filter)


