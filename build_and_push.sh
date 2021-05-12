#!/bin/zsh

echo "building"
docker build -t fthievent/emoba:latest .

echo "pushing"
docker push fthievent/emoba:latest

echo "finito"