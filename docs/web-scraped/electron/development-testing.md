# Source: https://www.electronjs.org/docs/latest/development/testing

On this page

# Testing

We aim to keep the code coverage of Electron high. We ask that all pull request not only pass all existing tests, but ideally also add new tests to cover changed code and new scenarios. Ensuring that we capture as many code paths and use cases of Electron as possible ensures that we all ship apps with fewer bugs.

This repository comes with linting rules for both JavaScript and C++ â€" as well as unit and integration tests. To learn more about Electron\'s coding style, please see the [coding-style](/docs/latest/development/coding-style) document.

## Linting[â€‹](#linting "Direct link to Linting") 

To ensure that your changes are in compliance with the Electron coding style, run `npm run lint`, which will run a variety of linting checks against your changes depending on which areas of the code they touch.

Many of these checks are included as precommit hooks, so it\'s likely you error would be caught at commit time.

## Unit Tests[â€‹](#unit-tests "Direct link to Unit Tests") 

If you are not using [build-tools](https://github.com/electron/build-tools), ensure that the name you have configured for your local build of Electron is one of `Testing`, `Release`, `Default`, or you have set `process.env.ELECTRON_OUT_DIR`. Without these set, Electron will fail to perform some pre-testing steps.

To run all unit tests, run `npm run test`. The unit tests are an Electron app (surprise!) that can be found in the `spec` folder. Note that it has its own `package.json` and that its dependencies are therefore not defined in the top-level `package.json`.

To run only specific tests matching a pattern, run `npm run test -- -g=PATTERN`, replacing the `PATTERN` with a regex that matches the tests you would like to run. As an example: If you want to run only IPC tests, you would run `npm run test -- -g ipc`.

## Node.js Smoke Tests[â€‹](#nodejs-smoke-tests "Direct link to Node.js Smoke Tests") 

If you\'ve made changes that might affect the way Node.js is embedded into Electron, we have a test runner that runs all of the tests from Node.js, using Electron\'s custom fork of Node.js.

To run all of the Node.js tests:

``` 
$ node script/node-spec-runner.js
```

To run a single Node.js test:

``` 
$ node script/node-spec-runner.js parallel/test-crypto-keygen
```

where the argument passed to the runner is the path to the test in the Node.js source tree.

### Testing on Windows 10 devices[â€‹](#testing-on-windows-10-devices "Direct link to Testing on Windows 10 devices") 

#### Extra steps to run the unit test:[â€‹](#extra-steps-to-run-the-unit-test "Direct link to Extra steps to run the unit test:") 

1.  Visual Studio 2019 must be installed.

2.  Node headers have to be compiled for your configuration.

    :::: 
    ::: codeBlockContent_QJqH
    ``` 
    ninja -C out\Testing electron:node_headers
    ```
    :::
    ::::

3.  The electron.lib has to be copied as node.lib.

    :::: 
    ::: codeBlockContent_QJqH
    ``` 
    cd out\Testing
    mkdir gen\node_headers\Release
    copy electron.lib gen\node_headers\Release\node.lib
    ```
    :::
    ::::

#### Missing fonts[â€‹](#missing-fonts "Direct link to Missing fonts") 

[Some Windows 10 devices](https://learn.microsoft.com/en-us/typography/fonts/windows_10_font_list) do not ship with the Meiryo font installed, which may cause a font fallback test to fail. To install Meiryo:

1.  Push the Windows key and search for *Manage optional features*.
2.  Click *Add a feature*.
3.  Select *Japanese Supplemental Fonts* and click *Install*.

#### Pixel measurements[â€‹](#pixel-measurements "Direct link to Pixel measurements") 

Some tests which rely on precise pixel measurements may not work correctly on devices with Hi-DPI screen settings due to floating point precision errors. To run these tests correctly, make sure the device is set to 100% scaling.

To configure display scaling:

1.  Push the Windows key and search for *Display settings*.
2.  Under *Scale and layout*, make sure that the device is set to 100%.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/testing.md)