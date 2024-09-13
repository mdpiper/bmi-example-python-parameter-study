#!/bin/bash


printf "Start time: "; /bin/date -Iminutes
printf "Job running on node: "; /bin/hostname
printf "OSG site: $OSG_SITE_NAME"
printf "Job running as user: "; /usr/bin/id
printf "Current working directory: "; /usr/bin/pwd
printf "contents of /srv and /code: "; /usr/bin/ls -al /srv /code
echo "Command line args: $@"

mkdir -p /srv/results
cd /code && bmiheat-parameter-study run heat-config-${1}.yaml > /srv/results/output-${1}.txt 2>&1
