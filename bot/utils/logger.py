import sys
from loguru import logger


logger.remove()
logger.add(sink=sys.stdout, format="<r>[Paws]</r> | <white>{time:YYYY-MM-DD HH:mm:ss}</white>"
                                   " | <level>{level: <7}</level>"
                                   " | <cyan><b>{line: <3}</b></cyan>"
                                   " | <white><b>{message}</b></white>")
logger = logger.opt(colors=True)
