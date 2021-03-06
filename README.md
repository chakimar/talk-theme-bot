# talk-theme-bot
Talk theme slackbot

## Features
* Management talk theme
* Dice roll talk theme

## Bot Commands
`./talk-theme list` - show talk theme list  
`./talk-theme now` - show now talk theme  
`./talk-theme add <talk-theme>` - add talk theme  
`./talk-theme set <talk-theme>` - set talk theme  
`./talk-theme remove <talk-theme>` - remove talk theme  
`./talk-theme diceroll` - dice roll talk theme  
`./talk-theme history` - show talk theme history  
`./talk-theme version` - show bot version  

`./talk-theme` commands can be changed to mention.

## Getting Started

### Prerequisites
* Docker

### Get API Token

Get API Token from slack bot page.


### Configure the bot

Set your API Token to environment value at runtime.(See below `Run` section)

### Run
```
docker run -e SLACKBOT_API_TOKEN=xxx-xxx-xxx -it chakimar/talk-theme-bot
```

### Volume
`/app/data`  
Persistent data directory.



## Development

##  Debug
Insert your api token to slackbot_settings.py
```python:slackbot_settings.py
API_TOKEN = "<your-api-token>"
```

and run below

```
python3 run.py
```

### Docker Build & Run
```
docker build . -t mybot
docker run -e SLACKBOT_API_TOKEN=xxx-xxx-xxx -it mybot
```


## Vagrant

### Provisioning
```
vagrant plugin install vagrant-docker-compose
vagrant up
```

## Acknowledements
* [Python slackbot library](https://github.com/lins05/slackbot)
