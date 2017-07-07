# coding: utf-8

# requestを追加する
import numpy as np
from janome.tokenizer import Tokenizer
import datetime
import yaml
import ast
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#ルールの読み込み
f = open("api_config/word2intent.yml", "r+")
correspondence = yaml.load(f)
f = open("api_config/date_info.yml", "r+")
date_info = yaml.load(f)
f = open("api_config/gourmet_genre.yml", "r+")
gourmet_genre = yaml.load(f)


def word2intent(tokens):
    intentions = []
    for token in tokens:
        word = token.surface
        #品詞を取得
        pos = token.part_of_speech.split(',')[0]
        if word in correspondence:
            intentions.append(correspondence[word])

    return intentions

def get_date(tokens):
    today = datetime.date.today()
    date = today
    for token in tokens:
        word = token.surface
        pos = token.part_of_speech.split(',')[0]
        if word in date_info:
            date = today + datetime.timedelta(days=date_info[word])
            break
    return date.isoformat()

def get_genre(tokens):
    genre = []
    for token in tokens:
        word = token.surface
        #品詞を取得
        pos = token.part_of_speech.split(',')[0]
        if word in gourmet_genre:
            genre.append(gourmet_genre[word])

    return genre

@app.route('/test')
def test():
    # request.argsにクエリパラメータが含まれている
    text = request.args.get("msg", "Not defined")
    #res = "your input text is "+val
    intentions = word2intent(text)
    #res = "your input text is "+text+". Your intention is "+','.join(intentions)
    res = {}
    res['text'] = text
    res['intentions'] = ','.join(intentions)
    res_json = jsonify(res)
    return res_json

@app.route('/post_req', methods=['POST'])
def post_req():
    data = ast.literal_eval(request.data.decode())
    text = data["msg"]
    t = Tokenizer()
    tokens = t.tokenize(text)
    intentions = word2intent(tokens)
    date = get_date(tokens)

    #返り値となるJSONの設定
    res = {}
    res['text'] = text
    res['intentions'] = ','.join(intentions)
    res['date'] = date
    if 'グルメ' in intentions:
        genre = get_genre(tokens)
        res['genre'] = ','.join(genre)
    res_json = jsonify(res)

    return res_json

if __name__ == "__main__":
    print('start bot_API')
    app.run()
