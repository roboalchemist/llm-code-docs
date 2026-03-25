# Source: https://wafris.org/docs/concepts/headless/

Title: Headless and Datastoreless

URL Source: https://wafris.org/docs/concepts/headless/

Markdown Content:
[](https://wafris.org/docs/concepts/headless/#context) Context
--------------------------------------------------------------

Early versions of the Wafris clients relied upon having provisioned a separate Redis instance to store rules and request data.

This unfortunately induced a lot of friction in the setup process and worked against our goals of helping developers secure every app.

[](https://wafris.org/docs/concepts/headless/#headless-storageless) Headless (Storageless)
------------------------------------------------------------------------------------------

From Wafris clients v2 and above, the Wafris clients are now “headless” and do not require a separate Redis instance or any user provided data store of any kind.

Under the hood the Wafris clients use synced and distributed SQLite DBs to store rules. Asynchronous communications to Wafris Hub replaced central storage of request data.

[](https://wafris.org/docs/concepts/headless/#how-it-works) How it works
------------------------------------------------------------------------

In standalone mode, the Wafris client rules are distributed as a SQLite DB file deployed alongside your application.

In managed mode, the Wafris client rules are automatically distributed from Wafris Hub to the Wafris client. At startup and periodically, the Wafris client will pull the latest rules from Wafris Hub to the local clients.

* * *
