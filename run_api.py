# coding: utf-8

# requestを追加する
import numpy as np
from janome.tokenizer import Tokenizer
import yaml
import ast
from flask import Flask, jsonify
from flask import request

#極性データの読み込み
f = open("plugins_word2intent/word2intent.yml", "r+")
correspondence = yaml.load(f)

def word2intent(text):
    t = Tokenizer()
    #m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tokens = t.tokenize(text)
    #msg = 'あなたの送ったメッセージをmecabで解析します。\n```' + m.parse(text) + '```'
    intentions = []
    for token in tokens:
        word = token.surface
        #品詞を取得
        pos = token.part_of_speech.split(',')[0]
        if word in correspondence:
            intentions.append(correspondence[word])

    return intentions

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
    # request.argsにクエリパラメータが含まれている
    data = ast.literal_eval(request.data.decode())
    text = data["msg"]
    intentions = word2intent(text)
    #res = "your input text is "+text+". Your intention is "+','.join(intentions)
    res = {}
    res['text'] = text
    res['intentions'] = ','.join(intentions)
    res_json = jsonify(res)
    return res_json

if __name__ == "__main__":
    print('start bot_API')
    app.run()
