# Headless-RaspberryPi-Twitter-Controller-Bot
A simpe twitter bot that runs on raspberry pi and could return its IP address and more info.

# Why?
If you own a raspberrypi, it's quite normal to run it in headless mode, i.e. not having any keyboard, mouse or display connected to it. This means whatever you do is via your personal laptop/desktop with the help of ssh.

SSH requires you to know its IP Address, which can change depending upon which sort of network you are on. That should not stop you from being able to ssh into your raspberry pi. 

# How to use?
I DM a twitter bot that is running through this program. I could DM saying, "What is your IP address?" 
The program runs as cron on frequent interval on raspberrypi and checks if a new DM has come. 
If it detects a new DM that asks for IP address, it DMs back with its IP address.

Remember the IP address returned would be local IP address. So, in any case you need to be on same network to ssh to your raspberry pi. This is better in security terms.

# Requirements
Python v2.7 (I know, I know. It could be v3. But this is an old project)
twython (`pip install twython`)
configparser (`pip install configparser`)

# Future
The code is pretty straight forward. It executes the command asked for, and returns its output, but all using twitter. You could extend this to have any other commands which you want to have executed remotely. 
