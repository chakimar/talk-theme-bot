from slackbot.bot import listen_to
import json
import random

VERSION = '0.0.1'
talk_themes = []
now_talk_theme = ''
talk_theme_histories = []

@listen_to('./talk-theme help')
def show_talk_theme_usage(message):
    usage = ' ./talk-theme list\t一覧表示\n'\
           ' ./talk-theme now\t現在のトークテーマ\n'\
           ' ./talk-theme add トークテーマ\tトークテーマを追加\n'\
           ' ./talk-theme diceroll\t次のトークテーマを決める\n'\
           ' ./talk-theme history\t過去のトークテーマ一覧\n'\
           ' ./talk-theme version\tバージョン表示'
    attachments = [
    {
        'title': '使い方',
        'text': usage,
        'color': '#d3d3d3'
    }]
    message.send_webapi('', json.dumps(attachments))

@listen_to('./talk-theme version')
def show_bot_version(message):
    message.send(VERSION)

@listen_to('./talk-theme list')
def show_talk_theme_list(message):
    if talk_themes:
        text = ''
        for talk_theme in talk_themes:
                text = text + talk_theme + "\n"
        attachments = [
        {
                'title': 'トークテーマ一覧',
                'text': text,
                'color': '#59afe1'
        }]
        message.send_webapi('', json.dumps(attachments))
    else:
        message.send('トークテーマが登録されてません')

@listen_to('./talk-theme now')
def show_now_talk_theme(message):
    if now_talk_theme:
        text = now_talk_theme
        attachments = [
        {
                'title': '現在のトークテーマ',
                'text': text,
                'color': '#59afe1'
        }]
        message.send_webapi('', json.dumps(attachments))
    else:
        message.send('トークテーマが登録されてません')

@listen_to('./talk-theme add')
def add_talk_theme(message):
    text = message.body['text']
    command, option ,new_theme = text.split(None, 2)
    talk_themes.append(new_theme)
    message.send('トークテーマを追加しました！')

@listen_to('./talk-theme diceroll')
def diceroll_talk_theme(message):
    if talk_themes:
        global now_talk_theme
        talk_theme_histories.append(now_talk_theme)
        now_talk_theme = random.choice(talk_themes)
        talk_themes.remove(now_talk_theme)
        text = now_talk_theme
        attachments = [
        {
                'title': '次回のトークテーマ',
                'text': text,
                'color': '#59afe1'
        }]
        message.send_webapi('何が出るかな♪:dice-roll:', json.dumps(attachments))
    else:
        message.send('トークテーマが登録されてません')

@listen_to('./talk-theme history')
def show_talk_theme_history(message):
    if talk_theme_histories:
        text = ''
        for talk_theme in talk_theme_histories.reverse():
                text = text + talk_theme + "\n"
        attachments = [
        {
                'title': '過去のトークテーマ一覧',
                'text': text,
                'color': '#59afe1'
        }]
        message.send_webapi('', json.dumps(attachments))
    else:
        message.send('履歴はありません')
