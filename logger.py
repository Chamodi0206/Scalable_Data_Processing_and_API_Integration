import logging

# Create logger
logger = logging.getLogger("my_project_logger")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add handler to logger
if not logger.handlers:
    logger.addHandler(console_handler)
