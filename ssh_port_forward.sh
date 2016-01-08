#!/bin/bash

USER="username"
MACHINE="machine-name"
#get ip from firebase
URL="https://firebase-app-name.firebaseio.com/$MACHINE/global_ip.json"
LOCAL_PORT=""
SERVER_PORT=""
echo "requesting $MACHINE ip from firebase"
IP=$(eval "curl $URL")
echo "$MACHINE ip: $IP"
tput setaf 1;tput smul;
echo "starting sync...password + yubikey OTP required"
tput setaf 7;tput rmul;
echo "forwarding server port $SERVER_PORT to local port $LOCAL_PORT"
eval "ssh -L $LOCAL_PORT:localhost:$SERVER_PORT $USER@$IP"