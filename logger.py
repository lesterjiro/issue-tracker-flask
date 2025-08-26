import logging
	
LOG_FILE = "/home/ubuntu/issue-tracker/app.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s : %(message)s"
)

logger = logging.getLogger("issue-tracker")
