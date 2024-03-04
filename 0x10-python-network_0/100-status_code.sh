#!/bin/bash
#sends a request to a URL passed as arg
curl -s -o /dev/null -w "%{http_code}" "$1"

