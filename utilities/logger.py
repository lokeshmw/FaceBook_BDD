import logging
import json
import os

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     filename='FB_Login.log')
#
# logger = logging.getLogger(__name__)
# print(logger)


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='FB_logs.json',
    filemode='w'
)

logger = logging.getLogger(__name__)














#
# def log_as_json(to_file, content):
#     to_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + to_file
#     folder = os.path.dirname(to_file)
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#     filename = os.path.basename(to_file)
#     file_path = os.path.join(folder, filename)
#     with open(file_path, "w") as jsf:
#         json.dump(content, jsf, indent=4)
#         print(os.path.abspath(file_path))

# def write_log_to_json(filename, log_data):
#     """
#     Writes a dictionary containing log data to a JSON file.
#
#     Args:
#         filename (str): Name of the JSON file to write to.
#         log_data (dict): Dictionary containing log message and other relevant data.
#     """
#     with open(filename, 'a') as f:
#         json.dump(log_data, f, indent=4)


# import logging
# import json
#
#
# # Custom formatter to format log records as JSON
# class JSONFormatter(logging.Formatter):
#     def format(self, record):
#         log_record = {
#             'timestamp': self.formatTime(record),
#             'level': record.levelname,
#             'message': record.getMessage(),
#             'logger_name': record.name
#         }
#         return json.dumps(log_record)
#
#
# # Configure logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# # Create file handler and set formatter
# file_handler = logging.FileHandler('FB_Login.json')
# formatter = JSONFormatter()
# file_handler.setFormatter(formatter)
#
# # Add file handler to logger
# logger.addHandler(file_handler)
#
# # Your step implementations...
