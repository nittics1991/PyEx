#!/bin/bash

ps

SOFFICE_PID=$( \
    ps |grep soffice \
        |sed -n -e '/soffice/p' -e 'q' \
        |tr -s " " "\t" \
        |cut -f 2 \
)

echo "${SOFFICE_PID}"

sudo kill -9 "${SOFFICE_PID}"

ps

