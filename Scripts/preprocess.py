"""Pull data from geth and parse it into mongo."""

import subprocess
import sys
sys.path.append("./../Preprocessing")
sys.path.append("./../Preprocessing/Crawler")
sys.path.append("./../Analysis")
import os
os.environ['ETH_BLOCKCHAIN_ANALYSIS_DIR'] = './../Preprocessing/'
from Crawler import Crawler
from ContractMap import ContractMap
import subprocess
import time
import argparse
import pdb

LOGDIR = "./../Preprocessing/logs"

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", type=str, help="Local MongoDB username")
parser.add_argument("-p", "--password", type=str, help="Local MongoDB password")
args = parser.parse_args()

print("Booting processes.")
# Catch up with the crawler
c = Crawler.Crawler(mongo_user=args.username, mongo_pass=args.password, mongo_host="localhost")

print("Updating contract hash map.")
# Update the contract addresses that have been interacted with
#ContractMap(c.mongo_client, last_block=c.max_block_mongo)

print("Update complete.")
