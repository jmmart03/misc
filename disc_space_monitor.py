#!/usr/bin/python3

#script to monitor disk usage

import shutil
import slack
import logging
import os

from logging.handles import RotatingFileHandler

#variables
alert_threshold = 0.9
alert_channel = ''
log_file = ''
slack_token = ''

#configure logger
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
handler = RotatingFileHandler(log_file, maxBytes=10000000, backupCount=10)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

x = shutil.disk_usage('/')
total_gb = round(x.total/(1024.0 ** 3),1)
free_gb = round(x.free/(1024.0 ** 3),1)
used_pct = round(x.used/x.total,4)

log.info(f"Total disk space: {total_gb}GB. Free disk space: {free_gb}GB. Used percent: {used_pct*100}%")

if used_pct > alert_threshold:
	#send slack alert
	client = slack.WebClient(token=slack_token)
	client.chat_postMessage(channel=alert_channel,text=f"Server disk space is low. {used_pct*100}% utilized!")
