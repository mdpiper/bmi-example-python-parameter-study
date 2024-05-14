#!/bin/bash


printf "Start time: "; /bin/date -Iminutes
printf "Job running on node: "; /bin/hostname
printf "OSG site: $OSG_SITE_NAME"
printf "Job running as user: "; /usr/bin/id
printf "Current working directory: "; /usr/bin/pwd
printf "contents of /srv: "; /usr/bin/ls -al /srv
echo "Command line args: $@"

bmiheat-parameter-study run heat-config-${1}.yaml > output-${1}.txt 2>&1
