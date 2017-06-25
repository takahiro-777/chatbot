# chatbot

## リポジトリ概要
```
chatbotの開発をしていくためのリポジトリ
実装内容は現段階では未定だが、
https://github.com/takahiro-777/nlp_tutorial/tree/master/chat/slackbot
上記で入門者用の簡単なchatbotまでは作成できているので、それをベースに
実際にアプリとしてリリースできるレベルの完成度を目指す。
```

## インストール
```
# mecabのインストール
$ brew install mecab
$ brew install mecab-ipadic
$ brew install git curl xz
$ git clone --depth 1 git@github.com:neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd -n
$ pip install mecab-python3

# cabochaのインストール(参考: http://www.maytry.net/how-to-use-cabocha-mecab-with-python/)
https://drive.google.com/folderview?id=0B4y35FiV1wh7cGRCUUJHVTNJRnM&usp=sharing#list　より、cabocha-0.69.tar.bz2をダウンロードする。
$ brew install crf++
$ tar jxf cabocha-0.69.tar.bz2
$ cd cabocha-0.69
$ ./configure --with-mecab-config=`which mecab-config` --with-charset=utf8 # これでエンコードのエラーが出ないはず
$ make
$ sudo make install

$ cd python
$ sudo python setup.py install

#slackbotのインストール
$ pip install slackbot
```

# 参考資料
```
http://qiita.com/taroc/items/b9afd914432da08dafc8
```
