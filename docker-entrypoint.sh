#!/bin/bash
set -e

if [ "$API_TOKEN" ]; then
	sed -i -e "s/^API_TOKEN = .*/API_TOKEN = \"$API_TOKEN\"/g" slackbot_settings.py
fi

exec "$@"