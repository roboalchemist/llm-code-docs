# Source: https://www.electronjs.org/docs/latest/tutorial/automated-testing

On this page

# Automated Testing

Test automation is an efficient way of validating that your application code works as intended. While Electron doesn\'t actively maintain its own testing solution, this guide will go over a couple ways you can run end-to-end automated tests on your Electron app.

## Using the WebDriver interface[â€‹](#using-the-webdriver-interface "Direct link to Using the WebDriver interface") 

From [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/):

> WebDriver is an open source tool for automated testing of web apps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more. ChromeDriver is a standalone server which implements WebDriver\'s wire protocol for Chromium. It is being developed by members of the Chromium and WebDriver teams.

There are a few ways that you can set up testing using WebDriver.

### With WebdriverIO[â€‹](#with-webdriverio "Direct link to With WebdriverIO") 

[WebdriverIO](https://webdriver.io/) (WDIO) is a test automation framework that provides a Node.js package for testing with WebDriver. Its ecosystem also includes various plugins (e.g. reporter and services) that can help you put together your test setup.

If you already have an existing WebdriverIO setup, it is recommended to update your dependencies and validate your existing configuration with how it is [outlined in the docs](https://webdriver.io/docs/desktop-testing/electron#configuration).

#### Install the test runner[â€‹](#install-the-test-runner "Direct link to Install the test runner") 

If you don\'t use WebdriverIO in your project yet, you can add it by running the starter toolkit in your project root directory:

- npm
- Yarn

``` 
npm init wdio@latest ./
```

``` 
yarn create wdio@latest ./
```

This starts a configuration wizard that helps you put together the right setup, installs all necessary packages, and generates a `wdio.conf.js` configuration file. Make sure to select *\"Desktop Testing - of Electron Applications\"* on one of the first questions asking *\"What type of testing would you like to do?\"*.

#### Connect WDIO to your Electron app[â€‹](#connect-wdio-to-your-electron-app "Direct link to Connect WDIO to your Electron app") 

After running the configuration wizard, your `wdio.conf.js` should include roughly the following content:

wdio.conf.js

``` 
export const config = 
  }]
  // ...
}
```

#### Write your tests[â€‹](#write-your-tests "Direct link to Write your tests") 

Use the [WebdriverIO API](https://webdriver.io/docs/api) to interact with elements on the screen. The framework provides custom \"matchers\" that make asserting the state of your application easy, e.g.:

``` 
import  from '@wdio/globals'

describe('keyboard input', () => )
})
```

Furthermore, WebdriverIO allows you to access Electron APIs to get static information about your application:

``` 
import  from '@wdio/globals'

describe('trigger message modal', async () =>  + $ + $ = $`
        })
      },
      1,
      2,
      3
    )
  })
})
```

#### Run your tests[â€‹](#run-your-tests "Direct link to Run your tests") 

To run your tests:

``` 
$ npx wdio run wdio.conf.js
```

WebdriverIO helps launch and shut down the application for you.

#### More documentation[â€‹](#more-documentation "Direct link to More documentation") 

Find more documentation on Mocking Electron APIs and other useful resources in the [official WebdriverIO documentation](https://webdriver.io/docs/desktop-testing/electron).

### With Selenium[â€‹](#with-selenium "Direct link to With Selenium") 

[Selenium](https://www.selenium.dev/) is a web automation framework that exposes bindings to WebDriver APIs in many languages. Their Node.js bindings are available under the `selenium-webdriver` package on NPM.

#### Run a ChromeDriver server[â€‹](#run-a-chromedriver-server "Direct link to Run a ChromeDriver server") 

In order to use Selenium with Electron, you need to download the `electron-chromedriver` binary, and run it:

- npm
- Yarn

``` 
npm install --save-dev electron-chromedriver
./node_modules/.bin/chromedriver
Starting ChromeDriver (v2.10.291558) on port 9515
Only local connections are allowed.
```

``` 
yarn add --dev electron-chromedriver
./node_modules/.bin/chromedriver
Starting ChromeDriver (v2.10.291558) on port 9515
Only local connections are allowed.
```

Remember the port number `9515`, which will be used later.

#### Connect Selenium to ChromeDriver[â€‹](#connect-selenium-to-chromedriver "Direct link to Connect Selenium to ChromeDriver") 

Next, install Selenium into your project:

- npm
- Yarn

``` 
npm install --save-dev selenium-webdriver
```

``` 
yarn add --dev selenium-webdriver
```

Usage of `selenium-webdriver` with Electron is the same as with normal websites, except that you have to manually specify how to connect ChromeDriver and where to find the binary of your Electron app:

test.js

``` 
const webdriver = require('selenium-webdriver')

const driver = new webdriver.Builder()
  // The "9515" is the port opened by ChromeDriver.
  .usingServer('http://localhost:9515')
  .withCapabilities(
  })
  .forBrowser('chrome') // note: use .forBrowser('electron') for selenium-webdriver <= 3.6.0
  .build()
driver.get('https://www.google.com')
driver.findElement(webdriver.By.name('q')).sendKeys('webdriver')
driver.findElement(webdriver.By.name('btnG')).click()
driver.wait(() => )
}, 1000)
driver.quit()
```

## Using Playwright[â€‹](#using-playwright "Direct link to Using Playwright") 

[Microsoft Playwright](https://playwright.dev) is an end-to-end testing framework built using browser-specific remote debugging protocols, similar to the [Puppeteer](https://github.com/puppeteer/puppeteer) headless Node.js API but geared towards end-to-end testing. Playwright has experimental Electron support via Electron\'s support for the [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) (CDP).

### Install dependencies[â€‹](#install-dependencies "Direct link to Install dependencies") 

You can install Playwright through your preferred Node.js package manager. It comes with its own [test runner](https://playwright.dev/docs/intro), which is built for end-to-end testing:

- npm
- Yarn

``` 
npm install --save-dev @playwright/test
```

``` 
yarn add --dev @playwright/test
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]Dependencies

This tutorial was written with `@playwright/test@1.52.0`. Check out [Playwright\'s releases](https://playwright.dev/docs/release-notes) page to learn about changes that might affect the code below.

### Write your tests[â€‹](#write-your-tests-1 "Direct link to Write your tests") 

Playwright launches your app in development mode through the `_electron.launch` API. To point this API to your Electron app, you can pass the path to your main process entry point (here, it is `main.js`).

``` 
import  from '@playwright/test'

test('launch app', async () => )
  // close app
  await electronApp.close()
})
```

After that, you will access to an instance of Playwright\'s `ElectronApp` class. This is a powerful class that has access to main process modules for example:

``` 
import  from '@playwright/test'

test('get isPackaged', async () => )
  const isPackaged = await electronApp.evaluate(async () => )
  console.log(isPackaged) // false (because we're in development mode)
  // close app
  await electronApp.close()
})
```

It can also create individual [Page](https://playwright.dev/docs/api/class-page) objects from Electron BrowserWindow instances. For example, to grab the first BrowserWindow and save a screenshot:

``` 
import  from '@playwright/test'

test('save screenshot', async () => )
  const window = await electronApp.firstWindow()
  await window.screenshot()
  // close app
  await electronApp.close()
})
```

Putting all this together using the Playwright test-runner, let\'s create a `example.spec.js` test file with a single test and assertion:

example.spec.js

``` 
import  from '@playwright/test'

test('example test', async () => )
  const isPackaged = await electronApp.evaluate(async () => )

  expect(isPackaged).toBe(false)

  // Wait for the first BrowserWindow to open
  // and return its Page object
  const window = await electronApp.firstWindow()
  await window.screenshot()

  // close app
  await electronApp.close()
})
```

Then, run Playwright Test using `npx playwright test`. You should see the test pass in your console, and have an `intro.png` screenshot on your filesystem.

``` 
â  $ npx playwright test

Running 1 test using 1 worker

  â  example.spec.js:4:1 âº example test (1s)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

Playwright Test will automatically run any files matching the `.*(test|spec)\.(js|ts|mjs)` regex. You can customize this match in the [Playwright Test configuration options](https://playwright.dev/docs/api/class-testconfig#test-config-test-match). It also works with TypeScript out of the box.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]Further reading

Check out Playwright\'s documentation for the full [Electron](https://playwright.dev/docs/api/class-electron/) and [ElectronApplication](https://playwright.dev/docs/api/class-electronapplication) class APIs.

## Using a custom test driver[â€‹](#using-a-custom-test-driver "Direct link to Using a custom test driver") 

It\'s also possible to write your own custom driver using Node.js\' built-in IPC-over-STDIO. Custom test drivers require you to write additional app code, but have lower overhead and let you expose custom methods to your test suite.

To create a custom driver, we\'ll use Node.js\' [`child_process`](https://nodejs.org/api/child_process.html) API. The test suite will spawn the Electron process, then establish a simple messaging protocol:

testDriver.js

``` 
const electronPath = require('electron')

const childProcess = require('node:child_process')

// spawn the process
const env = 
const stdio = ['inherit', 'inherit', 'inherit', 'ipc']
const appProcess = childProcess.spawn(electronPath, ['./app'], )

// listen for IPC messages from the app
appProcess.on('message', (msg) => )

// send an IPC message to the app
appProcess.send()
```

From within the Electron app, you can listen for messages and send replies using the Node.js [`process`](https://nodejs.org/api/process.html) API:

main.js

``` 
// listen for messages from the test suite
process.on('message', (msg) => )

// send a message to the test suite
process.send()
```

We can now communicate from the test suite to the Electron app using the `appProcess` object.

For convenience, you may want to wrap `appProcess` in a driver object that provides more high-level functions. Here is an example of how you can do this. Let\'s start by creating a `TestDriver` class:

testDriver.js

``` 
class TestDriver ) )

    // handle rpc responses
    this.process.on('message', (message) => )

    // wait for ready
    this.isReady = this.rpc('isReady').catch((err) => )
  }

  // simple RPC call
  // to use: driver.rpc('method', 1, 2, 3).then(...)
  async rpc (cmd, ...args) )
    return new Promise((resolve, reject) => this.rpcCalls.push())
  }

  stop () 
}

module.exports = 
```

In your app code, can then write a simple handler to receive RPC calls:

main.js

``` 
const METHODS = 
  // define your RPC-able methods here
}

const onMessage = async () => )
  } catch (err) 
    process.send()
  }
}

if (process.env.APP_TEST_DRIVER) 
```

Then, in your test suite, you can use your `TestDriver` class with the test automation framework of your choosing. The following example uses [`ava`](https://www.npmjs.com/package/ava), but other popular choices like Jest or Mocha would work as well:

test.js

``` 
const electronPath = require('electron')

const test = require('ava')

const  = require('./testDriver')

const app = new TestDriver(
})
test.before(async t => )
test.after.always('cleanup', async t => )
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/automated-testing.md)