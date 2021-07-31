# ut-listening-combiner

青本や実戦模試の東大英語のリスニング音源を本番と同じ形式の
1つのファイルに結合できるプログラムです。
ローカルのPythonまたはdocker-composeで実行できます。

## セットアップ
### 共通
#### 0. ダウンロード
    git clone https://github.com/hiro2620/ut-listening-combiner
    cd ut-listening-combiner

### docker-composeを使う場合
#### 1. ダウンロード
    git clone https://github.com/hiro2620/ut-listening-combiner
    cd ut-listening-combiner

#### 2. ビルド
    docker-compose build

### Dockerを使わない場合
#### 1. ffmpegをインストール
インストール方法はOSにより異なります。

    ffmpeg -version
    # ffmpeg version 4.1.6-1~deb10u1 Copyright (c) 2000-2020 the FFmpeg developers
    # built with gcc 8 (Debian 8.3.0-6)

#### 2-1. (必要なら)仮想環境を作成
    python -m venv env
    . ./env/bin/activate

#### 2-2. 依存ライブラリをインストール
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
#### Dockerを使う場合
    docker-compose up

#### Dockerを使わない場合
    cd src
    python3 main.py
ファイルは`./out.mp3`に保存されます。


## 動作確認環境
- Ubuntu 20.04.2 LTS x86_64
- Python 3.9.6
- ffmpeg 4.1.6-1
- Docker 20.10.7, build f0df350
- docker-compose 1.25.5, build 8a1c60f6
