# talk-theme-bot
Talk theme slackbot

## Features
* CRUD talk theme
* Dice roll talk theme

## Bot Commands
`./talk-theme list` - show talk theme list  
`./talk-theme now` - show now talk theme  
`./talk-theme add <talk-theme>` - add talk theme  
`./talk-theme diceroll` - dice roll talk theme  
`./talk-theme history` - show talk theme history  
`./talk-theme version` - show bot version  

## Getting Started

### Prerequisites
* Docker


## Development

### Get API Token

Get API Token from slack bot page.


### Configure the bot

Set your API Token to environment value at runtime.(See below `Run` section)

### Build
```
docker build . -t mybot
```


### Run
```
docker run -e API_TOKEN=xxx-xxx-xxx -it mybot
```

### Volume
`/slackbot/data`  
Persistent data directory.


##  Debug
Insert your api token to slackbot_settings.py
```python:slackbot_settings.py
API_TOKEN = "<your-api-token>"
```

and run below

```
python3 run.py
```

## Vagrant

### Installing
```
vagrant plugin install vagrant-docker-compose
vagrant up
```

## Acknowledements
* [Python slackbot library](https://github.com/lins05/slackbot)
