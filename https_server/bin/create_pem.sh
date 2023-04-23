#!/bin/bash

cd $(dirname $0)

openssl req -x509 -new -days 365 -nodes \
  -keyout localhost.pem \
  -out ../dist/localhost.pem \
  -subj "/CN=localhost"

