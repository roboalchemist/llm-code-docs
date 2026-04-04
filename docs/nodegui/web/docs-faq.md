# Source: https://nodegui.org/docs/faq

Title: FAQ | NodeGui

URL Source: https://nodegui.org/docs/faq

Markdown Content:
Why does installation fail at "Minimal Qt setup"?[​](https://nodegui.org/docs/faq#why-does-installation-fail-at-minimal-qt-setup "Direct link to Why does installation fail at \"Minimal Qt setup\"?")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NodeGui currently relies on the [Qt framework](https://qt.io/) to acheive cross-platform native interfaces. The library uses a minimal configuration of specific open source Qt components which are downloaded upon installation.

If the server which hosts the component binaries is down or unavailable, the installation will fail and you might see something along the lines of:

`Minimal Qt 5.14.1 setup:FetchError: request to https://download.qt.io/online/qtsdkrepository/mac_x64/desktop/qt5_5141/qt.qt5.5141.clang_64/5.14.1-0-202001241000qttools-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z failed, reason: connect ETIMEDOUT 77.86.229.90:443    at ClientRequest.<anonymous> (.../nodegui/node_modules/node-fetch/lib/index.js:1461:11)    at ClientRequest.emit (events.js:315:20)    at TLSSocket.socketErrorListener (_http_client.js:426:9)    at TLSSocket.emit (events.js:315:20)    at emitErrorNT (internal/streams/destroy.js:92:8)    at emitErrorAndCloseNT (internal/streams/destroy.js:60:3)    at processTicksAndRejections (internal/process/task_queues.js:84:21) {  type: 'system',  errno: 'ETIMEDOUT',  code: 'ETIMEDOUT'}`

In this scenario, you would need to find a mirror (alternate domain) for the binaries which can then be substituted using the `QT_LINK_MIRROR` environment variable. Let's assume we've found an active mirror, for example, `https://qt-mirror.dannhauer.de`, we can then follow these steps to configure the installation:

#### **Unix / MacOS**[​](https://nodegui.org/docs/faq#unix--macos "Direct link to unix--macos")

`QT_LINK_MIRROR=https://qt-mirror.dannhauer.denpm install`

#### **Windows**[​](https://nodegui.org/docs/faq#windows "Direct link to windows")

`set QT_LINK_MIRROR=https://qt-mirror.dannhauer.denpm install`

Now, instead of requesting the resource from

`https://download.qt.io/online/...`

as in the example above, the script responsible for installing these components would use

`https://qt-mirror.dannhauer.de/online/...`

If this does not solve your problem, please make sure you have installed all the necessary [requirements](https://docs.nodegui.org/docs/guides/getting-started#developer-environment)

Why am I having trouble installing Qode?[​](https://nodegui.org/docs/faq#why-am-i-having-trouble-installing-qode "Direct link to Why am I having trouble installing Qode?")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When running `npm install @nodegui/qode`, some users occasionally encounter installation errors.

In almost all cases, these errors are the result of network problems and not actual issues with the `@nodegui/qode` npm package. Errors like `ELIFECYCLE`, `EAI_AGAIN`, `ECONNRESET`, and `ETIMEDOUT` are all indications of such network problems. The best resolution is to try switching networks, or wait a bit and try installing again.

You can also attempt to download Qode directly from [nodegui/qode/releases](https://github.com/nodegui/qode/releases) if installing via `npm` is failing.

As you would have noticed, the list of methods and properties are less compared to what is present in the Qt's corresponding widget class. This is because we havent written wrappers for them yet. You can help add more methods by following the development guide for contributors. Overtime this gap would reduce.

When will Qode upgrade to latest Node.js / Qt version?[​](https://nodegui.org/docs/faq#when-will-qode-upgrade-to-latest-nodejs--qt-version "Direct link to When will Qode upgrade to latest Node.js / Qt version?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When a new version of Node.js/Qt gets released, we usually wait for about a month before upgrading the one in Qode. So we can avoid getting affected by bugs introduced in new Node.js/Qt versions, which happens very often.

This happens when the variable which is used to store the window/tray gets garbage collected.

If you encounter this problem, the following articles may prove helpful:

*   [Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)
*   [Variable Scope](https://msdn.microsoft.com/library/bzt2dkta(v=vs.94).aspx)

If you want a quick fix, you can make the variables global by changing your code from this:

`const { QWidget } = require("@nodegui/nodegui");const view = new QWidget();view.setObjectName("container");view.setLayout(new FlexLayout());`

to this:

`const { QWidget } = require("@nodegui/nodegui");const view = new QWidget();view.setObjectName("container");view.setLayout(new FlexLayout());global.view = view; //prevent GC`
