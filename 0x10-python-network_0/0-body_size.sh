#!/bin/bash
#take in a URL send a request to that URLand display the size of the body of the response
curl -s "$1" | wc -c
