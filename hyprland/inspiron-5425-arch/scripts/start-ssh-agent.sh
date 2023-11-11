#!/usr/bin/bash
if [[ -n "$SSH_AGENT_PID" ]];
then
   echo "ssh-agent is already running"
   # Do something knowing the pid exists, i.e. the process with $PID is running
else
eval `ssh-agent -s`
fi
