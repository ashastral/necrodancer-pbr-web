#!/bin/sh
gunicorn -b 0.0.0.0:8000 -k eventlet necrodancer_pbr_web.wsgi
