Source: https://docs.slack.dev/tools/bolt-js/concepts/deferring-initialization

# Deferring app initialization

Bolt offers a way to defer full initialization via the `deferInitialization` option and to call the equivalent `App#init()` in your code, putting more control over asynchronous execution required for initialization into your hands as the developer.

info

If you call `start()` before `init()`, Bolt will raise an exception.

## Example {#example}

```text
const { App } = require('@slack/bolt');// deferInitialization is one of the options you can set in the constructorconst app = new App({  token,  signingSecret,  deferInitialization: true,});(async () => {  try {    // Must call init() before start() within an async function    await app.init();    // Now safe to call start()    await app.start(process.env.PORT || 3000);  } catch (e) {    app.logger.error(e);    process.exit(1);  }})()
```text
