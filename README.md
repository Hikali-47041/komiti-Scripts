# Scripts

[komiti](https://komiti.github.io/) をビルドするためのスクリプトです。  
komitiは[koruri](https://koruri.github.io/) のforkです。

## 使い方

```
git clone https://github.com/Koruri/Scripts.git make_komiti
```

```
cd make_komiti
```

Titillium Web と Roboto は `setup.sh` の中でGoogle Fontsからダウンロード、展開されます。

```
./setup.sh
```

あとは

* [ここ](https://osdn.jp/projects/mplus-fonts/releases/62344) から最新の `M+ OUTLINE FONTS TESTFLIGHT` をダウンロード
* M+ 1p を `mplus` に展開
* [FontForge](https://fontforge.org/) をインストールしておく

```
fontforge -lang=py -script komiti.py
```
