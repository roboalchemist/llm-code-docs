Source: https://docs.slack.dev/tools/bolt-js/ja-jp/concepts/deferring-initialization

# アプリの初期化の遅延

Bolt は `deferInitialization` というオプションを使うことで、アプリの初期化処理の完了を遅延させることができます。このオプションを使う場合、あなたのコードの中で遅延された初期化処理部分に対応する `App#init()` メソッドを呼び出す必要がありますが、こうすることで初期化に必要となる非同期処理の実行をよりコントロールすることが可能となります。

## 注意: `init()` メソッドを呼び出す前に `start()` メソッドを呼び出した場合、 Bolt は例外を発生させます。

```text
const { App } = require('@slack/bolt');// deferInitialization はコンストラクターで指定できるオプションconst app = new App({  token,  signingSecret,  deferInitialization: true,});(async () => {  try {    // 非同期関数の中で start() メソッドを呼び出す前に init() メソッドを呼び出すこと    await app.init();    // init() メソッドを呼び出したので、`start()` メソッドを安全に呼び出すことができる    await app.start(process.env.PORT || 3000);  } catch (e) {    app.logger.error(e);    process.exit(1);  }})()
```text
