# ut-listening-combiner

青本や実戦模試の東大英語のリスニング音源を本番と同じ形式の
1つのファイルに結合できるプログラムです。
Pythonで動作します。

## セットアップ
### 1. ダウンロード
    git clone https://github.com/hiro2620/ut-listening-combiner
    cd ut-listening-combiner

### 2. ffmpegをインストールして、使えることを確認
    ffmpeg -version

### 3-1. (必要なら)仮想環境を作成
    python -m venv env
    . ./env/bin/activate

### 3-2. 依存ライブラリをインストール
    pip install -r requirements.txt


## 使い方
### 1. 音源のファイルを準備

`/mp3`配下に1回分の音源のmp3ファイルを配置して下さい。

ファイル名には再生する順番を表す数字が含まれている必要
があります。


```bash
.
├── mp3
│   ├── Track8.mp3
│   ├── Track9.mp3
│   ├── Track10.mp3
│   ├── Track11.mp3
│   ├── Track12.mp3
│   ├── Track13.mp3
│   └── Track14.mp3
└── src
    └── main.py
```

デフォルトでは
- リスニング試験の冒頭
- ABCの説明
- ABCの本体

の計7ファイルを使い、セクション内の繰り返しの間には30秒、
セクション間には60秒の無音部分が挿入されます。

これらは`config/audio-config.json`を編集することで
変更できます。

### 2. 実行
    python3 ./src/main.py
ファイルは`./out.mp3`に保存されます。


## 動作確認環境
- Ubuntu 20.04 LTS x64
- Python 3.9.6
