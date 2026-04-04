Source: https://docs.slack.dev/tools/bolt-python/ja-jp/concepts/socket-mode

# ソケットモードの利用

[ソケットモード](/apis/events-api/using-socket-mode)は、アプリに WebSocket での接続と、そのコネクション経由でのデータ受信を可能とします。Bolt for Python は、バージョン 1.2.0 からこれに対応しています。

ソケットモードでは、Slack からのペイロード送信を受け付けるエンドポイントをホストする HTTP サーバーを起動する代わりに WebSocket で Slack に接続し、そのコネクション経由でデータを受信します。ソケットモードを使う前に、アプリの管理画面でソケットモードの機能が有効になっていることを確認しておいてください。

ソケットモードを使用するには、環境変数に `SLACK_APP_TOKEN` を追加します。アプリのトークン（App-Level Token）は、アプリの設定の「**Basic Information**」セクションで確認できます。

[組み込みのソケットモードアダプター](https://github.com/slackapi/bolt-python/tree/main/slack_bolt/adapter/socket_mode/builtin)を使用するのがおすすめですが、サードパーティ製ライブラリを使ったアダプターの実装もいくつか存在しています。利用可能なアダプターの一覧です。

内部的に利用する PyPI プロジェクト名

Bolt アダプター

[slack\_sdk](https://pypi.org/project/slack-sdk/)

[slack\_bolt.adapter.socket\_mode](https://github.com/slackapi/bolt-python/tree/main/slack_bolt/adapter/socket_mode/builtin)

[websocket\_client](https://pypi.org/project/websocket_client/)

[slack\_bolt.adapter.socket\_mode.websocket\_client](https://github.com/slackapi/bolt-python/tree/main/slack_bolt/adapter/socket_mode/websocket_client)

[aiohttp](https://pypi.org/project/aiohttp/) (asyncio-based)

[slack\_bolt.adapter.socket\_mode.aiohttp](https://github.com/slackapi/bolt-python/tree/main/slack_bolt/adapter/socket_mode/aiohttp)

[websockets](https://pypi.org/project/websockets/) (asyncio-based)

[slack\_bolt.adapter.socket\_mode.websockets](https://github.com/slackapi/bolt-python/tree/main/slack_bolt/adapter/socket_mode/websockets)

```python
import osfrom slack_bolt import Appfrom slack_bolt.adapter.socket_mode import SocketModeHandler# 事前に Slack アプリをインストールし 'xoxb-' で始まるトークンを入手app = App(token=os.environ["SLACK_BOT_TOKEN"])# ここでミドルウェアとリスナーの追加を行いますif __name__ == "__main__":    # export SLACK_APP_TOKEN=xapp-***    # export SLACK_BOT_TOKEN=xoxb-***    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])    handler.start()
```

## Async (asyncio) の利用 {#async-asyncio-の利用}

aiohttp のような asyncio をベースとしたアダプターを使う場合、アプリケーション全体が asyncio の async/await プログラミングモデルで実装されている必要があります。`AsyncApp` を動作させるためには `AsyncSocketModeHandler` とその async なミドルウェアやリスナーを利用します。

`AsyncApp` の使い方についての詳細は、[Async (asyncio) の利用](/tools/bolt-python/concepts/async)や、関連する[サンプルコード例](https://github.com/slackapi/bolt-python/tree/main/examples)を参考にしてください。

```python
from slack_bolt.app.async_app import AsyncApp# デフォルトは aiohttp を使った実装from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandlerapp = AsyncApp(token=os.environ["SLACK_BOT_TOKEN"])# ここでミドルウェアとリスナーの追加を行いますasync def main():    handler = AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])    await handler.start_async()if __name__ == "__main__":    import asyncio    asyncio.run(main())
```
