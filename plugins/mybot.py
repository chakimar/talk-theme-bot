from slackbot.bot import respond_to
from slackbot.bot import listen_to
import json
import random
import os

VERSION = '0.0.2'
TALK_THEME_PATH = 'data/talk_theme.lst'
TALK_THEME_HISTORY_PATH = 'data/talk_theme_history.lst'
NOW_TALK_THEME_PATH = 'data/now_talk_theme'

talk_themes = []
now_talk_theme = ''
talk_theme_histories = []

talk_theme_list_loaded_flag = False
talk_theme_history_list_loaded_flag = False


def _load_talk_theme():
    if os.path.exists(TALK_THEME_PATH):
        global talk_themes
        with open(TALK_THEME_PATH) as f:
            talk_themes = [s.strip() for s in f.readlines()]

def _load_talk_theme_history():
    if os.path.exists(TALK_THEME_HISTORY_PATH):
        global talk_theme_histories
        with open(TALK_THEME_HISTORY_PATH) as f:
            talk_theme_histories = [s.strip() for s in f.readlines()]

def _load_now_talk_theme():
    if os.path.exists(NOW_TALK_THEME_PATH):
        global now_talk_theme
        with open(NOW_TALK_THEME_PATH) as f:
            now_talk_theme = f.read()


_load_talk_theme()
_load_talk_theme_history()
_load_now_talk_theme()


@respond_to('help')
@listen_to('./talk-theme help')
def show_talk_theme_usage(message):
    usage = ' `./talk-theme list`\t一覧表示\n'\
           ' `./talk-theme now`\t現在のトークテーマ\n'\
           ' `./talk-theme add <トークテーマ>`\tトークテーマを追加\n'\
           ' `./talk-theme diceroll`\t次のトークテーマを決める\n'\
           ' `./talk-theme history`\t過去のトークテーマ一覧\n'\
           ' `./talk-theme version`\tバージョン表示\n'\
           '上記コマンドは `./takl-theme`をbotへのメンションに変えても反応します。\n'\
           'また、botへのダイレクトメッセージであれば `./talk-theme`を省略可能です。'
    attachments = [
    {
        'title': '使い方',
        'text': usage,
        'color': '#d3d3d3'
    }]
    message.send_webapi('', json.dumps(attachments))

@respond_to('version')
@listen_to('./talk-theme version')
def show_bot_version(message):
    message.send(VERSION)

@respond_to('list')
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

@respond_to('now')
@listen_to('./talk-theme now')
def show_now_talk_theme(message):
    if now_talk_theme:
        text = now_talk_theme
        attachments = [
        {
                'title': '現在のトークテーマ',
                'text': text,
                'color': '#008000'
        }]
        message.send_webapi('', json.dumps(attachments))
    else:
        message.send('トークテーマが登録されてません')

@respond_to('add')
@listen_to('./talk-theme add')
def add_talk_theme(message):
    text = message.body['text']
    tmp, new_theme = text.rsplit(None, 1)
    talk_themes.append(new_theme)
    _save_talk_theme()
    message.send('トークテーマを追加しました！')

@respond_to('diceroll')
@listen_to('./talk-theme diceroll')
def diceroll_talk_theme(message):
    if talk_themes:
        if now_talk_theme:
            _save_talk_theme_history(now_talk_theme)
        _save_now_talk_theme(random.choice(talk_themes))
        talk_themes.remove(now_talk_theme)
        _save_talk_theme()
        text = now_talk_theme
        attachments = [
        {
                'title': '次回のトークテーマ',
                'text': text,
                'color': '#ff0000'
        }]
        message.send_webapi('何が出るかな♪:dice-roll:', json.dumps(attachments))
    else:
        message.send('トークテーマが登録されてません')

@respond_to('history')
@listen_to('./talk-theme history')
def show_talk_theme_history(message):
    if talk_theme_histories:
        text = ''
        for talk_theme in (reversed(talk_theme_histories)):
            text = text + talk_theme + "\n"
        attachments = [
        {
                'title': '過去のトークテーマ一覧',
                'text': text,
                'color': '#ffa500'
        }]
        message.send_webapi('', json.dumps(attachments))
    else:
        message.send('履歴はありません')

@respond_to('set')
def set_talk_theme(message):
    if now_talk_theme:
        _save_talk_theme_history(now_talk_theme)
    text = message.body['text']
    tmp, new_theme = text.rsplit(None, 1)
    _save_now_talk_theme(new_theme)
    message.send('トークテーマを設定しました！')

def _save_talk_theme():
    with open(TALK_THEME_PATH, mode='w') as f:
        for talk_theme in talk_themes:
            f.write(talk_theme + '\n')
        
def _save_talk_theme_history(old_talk_theme):
    talk_theme_histories.append(old_talk_theme)
    with open(TALK_THEME_HISTORY_PATH, mode='a') as f:
        f.write(old_talk_theme + '\n')

def _save_now_talk_theme(talk_theme):
    global now_talk_theme
    now_talk_theme = talk_theme
    with open(NOW_TALK_THEME_PATH, mode='w') as f:
        f.write(talk_theme)
    