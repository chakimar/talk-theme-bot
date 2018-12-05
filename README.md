# python-slackbot-devkit
Python slackbot development kit

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
