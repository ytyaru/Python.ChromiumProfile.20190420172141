# このソフトウェアについて

　Chromiumのプロファイル情報を取得する。

* Python製CLI

# インストールと実行

```sh
git clone https://github.com/ytyaru/Python.ChromiumProfile.20190420172141
cd Python.ChromiumProfile.20190420172141/src
```
```sh
python3 ChromiumProfileCommand.py tsv
```

# コマンド概要

## メインコマンド引数

引数|意味
----|----
`-f`|設定ファイルパスが` ~/.config/chromium/Local State`以外なら指定する

## サブコマンドと引数

サブコマンド|引数|意味
------------|----|----
`tsv`| |TSV形式で出力する
`list`|`-d`|ディレクトリ名一覧（改行区切り）
`list`|`-u`|ユーザ名一覧（改行区切り）
`get`|`-d ユーザ名`|対応するディレクトリ名
`get`|`-u ディレクトリ名`|対応するユーザ名
`get`|`-l`|最後に使用したディレクトリ名

# 使用例

　プロファイルは以下とする。

ディレクトリ名|ユーザ名
----|----
`Default`|`default`
`Profile 1`|`work`
`Profile 2`|`life`

　TSV形式。

```sh
python3 ChromiumProfileCommand.py tsv
```
```tsv
Default	default
Profile 1	work
Profile 2	life
```

　ディレクトリ名一覧。（辞書順）

```sh
python3 ChromiumProfileCommand.py list -d
```
```
Default
Profile 1
Profile 2
```

　ユーザ名一覧。（ディレクトリ名の辞書順）

```sh
python3 ChromiumProfileCommand.py list -u
```
```
default
work
life
```

　ディレクトリ名からユーザ名を取得する。

```sh
python3 ChromiumProfileCommand.py get -u 'Profile 2'
```
```
life
```

　ユーザ名からディレクトリ名を取得する。

```sh
python3 ChromiumProfileCommand.py get -d 'life'
```
```
Profile 2
```

　最後に使用したユーザ名を取得する。

```sh
python3 ChromiumProfileCommand.py get -l
```
```
（最後に終了したプロファイルのディレクトリ名））
```

　設定ファイルパスが` ~/.config/chromium/Local State`以外の場所なら`-f`で指定する。（サブコマンドの前）

```sh
python3 ChromiumProfileCommand.py -f /tmp/LocalState.json get -d 'life'
```


# 開発環境

* 2019-04-20
* [Raspbierry pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B+
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) 9.0 stretch 2018-11-13 Desktop
        * Python 3.5.3

```sh
$ uname -a
Linux raspberrypi 4.14.98-v7+ #1200 SMP Tue Feb 12 20:27:48 GMT 2019 armv7l GNU/Linux
```

# ライセンス

　このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

