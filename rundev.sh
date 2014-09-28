#!/bin/bash                                                                                                                                                                  
set -e
LOGFILE=/webapp/tbio/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as                                                                                                                                                       
cd /webapp/dashboard/
. ../bin/activate
exec ./manage.py runserver 0.0.0.0:8000