import logging
import sys

log = logging.getLogger(__name__)

out_handler = logging.StreamHandler(sys.stdout)
out_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_handler.setLevel(logging.INFO)

log.addHandler(out_handler)
log.setLevel(logging.INFO)

def endpoint():
    log.info("running")
