#!/bin/bash
# File Name: docker-entrypoint.sh
# Author: JackeyGao
# mail: junqi.gao@shuyun.com
# Created Time: 五  9/25 10:31:45 2015

/code/manage.py syncdb --noinput
/usr/local/bin/gunicorn bubu.wsgi:application -w 2 -b :8000
