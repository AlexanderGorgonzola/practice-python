import logging
import logging.config

#logging.config.fileConfig("logging.conf") <-- specific file configurations

#Check the documentation for more info

#logging.basicConfig() <-- basic configurations
logger = logging.getLogger(__name__)
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

#levels and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error("This is an error")

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)