#!/bin/bash
gunicorn --bind=0.0.0.0:8000 --chdir=/VulnerableWebApp/ VulnerableWebApp.wsgi  --user root --workers 3 & nginx -g "daemon off;"
