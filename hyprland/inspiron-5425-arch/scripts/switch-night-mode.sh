#!/bin/bash

if $(killall wlsunset); then
	exit 0;
else
	wlsunset -t 3000 & disown
fi
