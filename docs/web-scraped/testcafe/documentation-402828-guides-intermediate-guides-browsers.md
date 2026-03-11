# Source: https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers

Title: Browsers | Intermediate Guides | Guides

URL Source: https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers

Markdown Content:
[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#browser-support)Browser support[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#browser-support)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe supports a wide array of modern browsers. The latest versions of the following browsers work without any extra configuration:

| Browser | Browser Alias |
| --- | --- |
| Chromium | `chromium` |
| Google Chrome | `chrome` |
| Google Chrome Canary | `chrome-canary` |
| Microsoft Edge (Chromium-based **only**) | `edge` |
| Mozilla Firefox | `firefox` |
| Opera | `opera` |
| Safari | `safari` |

Important

TestCafe 3.0 discontinued official support for Internet Explorer 11, several months after the browser’s official [retirement](https://techcommunity.microsoft.com/blog/windows-itpro-blog/internet-explorer-11-desktop-app-retirement-faq/2366549). TestCafe 3.0 does not support legacy versions of Microsoft Edge.

TestCafe also supports:

*   [Headless browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#test-in-headless-mode)
*   [Custom and portable browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#custom-browsers)
*   [Mobile browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#mobile-browsers-cloud-browsers-and-emulation)
*   [Remote browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#mobile-browsers-cloud-browsers-and-emulation)
*   [Cloud browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#mobile-browsers-cloud-browsers-and-emulation)
*   [Chromium-based browser emulation](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#mobile-browsers-cloud-browsers-and-emulation)

[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#specify-target-browsers)Specify target browsers[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#specify-target-browsers)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#cli)CLI[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#cli)

Specify the [browser alias](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#local-browsers) as the first command line argument.

```
testcafe chrome my-fixture.js
```

The command above launches tests in Google Chrome. If you want to launch tests in multiple browsers, separate the aliases with a comma:

```
testcafe chrome,edge my-fixture.js
```

Use the `all` alias to launch the test in all your local browsers.

### [](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#test-runner-api)Test Runner API[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#test-runner-api)

Use the [runner.browsers](https://testcafe.io/documentation/402661/reference/testcafe-api/runner/browsers) method to select the target browser:

```
await runner
    .browsers('chrome')
    .src('./tests/')
    .run();
```

Pass an array of browser aliases to select multiple browsers:

```
await runner
    .browsers(['safari', 'chrome'])
    .src('./tests/')
    .run();
```

Use the `all` alias to launch the test in all your local browsers.

[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#local-browsers)Local browsers[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#local-browsers)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe automatically detects local browsers. Run the following shell command to display a list of local browsers that work with TestCafe out of the box:

```
testcafe --list-browsers
```

### [](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#switch-between-chrome-channels)Switch between Chrome channels[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#switch-between-chrome-channels)

The `chrome` alias targets the stable channel of Google Chrome. To run tests in Chrome Beta or Chrome Dev, specify [the path to the browser executable](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#custom-browsers) instead of the alias.

### [](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#switch-between-versions-of-microsoft-edge)Switch between versions of Microsoft Edge[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#switch-between-versions-of-microsoft-edge)

Important

TestCafe 3.0 does not support legacy versions of Microsoft Edge

Windows users can run tests in [either](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-update-policies#allowsxs) the legacy or the Chromium version of Microsoft Edge. Open **Windows Settings**, navigate to **Default Apps** and select **Default Apps by Protocol**. Set the `MICROSOFT-EDGE:` protocol to whichever version of Edge you prefer. That version will open when you use the `edge` alias.

[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#custom-browsers)Custom browsers[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#custom-browsers)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run tests in a browser that TestCafe can’t automatically detect, such as a portable browser, specify the path to the browser’s executable. Use the `path:` prefix:

```
testcafe path:d:\firefoxportable\firefoxportable.exe ./tests/
```

```
await runner
    .browsers('path:d:\firefoxportable\firefoxportable.exe')
    .src('./tests/')
    .run();
```

Alternatively, specify target browsers in your [configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#browsers):

```
{
    "browsers": "path:`C:\\Program Files\\Google Chrome\\chrome.exe`"
}
```

[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#mobile-browsers-cloud-browsers-and-emulation)Mobile Browsers, Cloud Browsers and Emulation[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#mobile-browsers-cloud-browsers-and-emulation)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe makes it easy to maintain your website’s compatibility with a wide array of devices.

*   You can run TestCafe tests on remote devices such as smartphones and tablets.
*   You can run TestCafe tests on popular cloud testing services.
*   You can simulate mobile devices in Chromium-based browsers.

Read the [Mobile Devices, Cloud Browsers and Emulation Guide](https://testcafe.io/documentation/403584/guides/intermediate-guides/mobile-devices-cloud-browsers-and-emulation) for more information.

[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#test-in-headless-mode)Test in Headless Mode[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#test-in-headless-mode)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Chrome](https://developer.chrome.com/blog/headless-chrome/) and [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/) include **headless mode** — a less resource-intensive way to run TestCafe. Headless browsers don’t display their GUI, making it possible to run them without a GPU. Even then, you can still [take screenshots](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#take-screenshots) and [resize the browser window](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#resize-windows) in headless mode.

See also: [Headless browsers: limitations and quirks](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#headless-browsers-limitations-and-quirks)

Add `:headless` to browser alias to launch a browser in headless mode.

```
testcafe "chrome:headless" tests/sample-fixture.js
```

```
runner
    .src('tests/sample-fixture.js')
    .browsers('chrome:headless')
    .run();
```

To launch a custom headless browser, replace the `path:` prefix with that browser’s alias:

```
testcafe "firefox:d:\firefoxportable\firefoxportable.exe:headless" tests/sample-fixture.js
```

```
runner
    .src('tests/sample-fixture.js')
    .browsers('firefox:d:\firefoxportable\firefoxportable.exe:headless')
    .run();
```

### [](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#headless-browsers-limitations-and-quirks)Headless browsers: Limitations and quirks[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#headless-browsers-limitations-and-quirks)

*   When you run TestCafe tests in a headless browser, you cannot enable the `userProfile` option.
*   [Known Chromium bug](https://issues.chromium.org/issues/40256833) for [native automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) users: Chromium-based browsers do not honor the --window-size CLI flag.
*   When TestCafe uses [native automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode), browsers [upgrade insecure requests to HTTPS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Upgrade-Insecure-Requests).

[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#user-profiles-enable-extensions-and-custom-settings)User profiles: Enable extensions and custom settings[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#user-profiles-enable-extensions-and-custom-settings)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Important

You cannot enable the `userProfile` option in a headless browser.

Extensions and custom browser settings may interfere with your tests. That’s why TestCafe launches browsers with an _empty_ user profile. If you wish to use your browser’s default user profile, enable the `:userProfile` option.

```
testcafe firefox:userProfile tests/test.js
```

```
runner
    .src('tests/fixture1.js')
    .browsers('firefox:userProfile')
    .run();
```

To launch a custom browser with this option, replace the `path:` prefix with the browser alias:

```
testcafe chrome:d:\chrome_portable\chrome.exe:userProfile tests/test.js
```

[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#automation-port)Automation Port[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#automation-port)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe communicates with Chrome and Firefox though a remote control port. Usually, the framework scans for an available port, and assigns one automatically. You can specify a specific custom port with the `cdpPort` option (for Chrome) or the `marionettePort` option (for Firefox).

### [](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#chrome)Chrome[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#chrome)

```
testcafe "chrome:headless:cdpPort=9223" tests/sample-fixture.js
```

```
runner
    .src('tests/sample-fixture.js')
    .browsers('chrome:headless:cdpPort=9223')
    .run();
```

### [](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#firefox)Firefox[](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#firefox)

```
testcafe "firefox:headless:marionettePort=9223" tests/sample-fixture.js
```

```
runner
    .src('tests/sample-fixture.js')
    .browsers('firefox:headless:marionettePort=9223')
    .run();
```
