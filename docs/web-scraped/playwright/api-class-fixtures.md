# Source: https://playwright.dev/docs/api/class-fixtures

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Test Runner]
-   [Fixtures]

On this page

<div>

# Fixtures

</div>

Playwright Test is based on the concept of the [test fixtures](/docs/test-fixtures). Test fixtures are used to establish environment for each test, giving the test everything it needs and nothing else.

Playwright Test looks at each test declaration, analyses the set of fixtures the test needs and prepares those fixtures specifically for the test. Values prepared by the fixtures are merged into a single object that is available to the `test`, hooks, annotations and other fixtures as a first parameter.

``` 
import  from '@playwright/test';

test('basic test', async () => );
```

Given the test above, Playwright Test will set up the `page` fixture before running the test, and tear it down after the test has finished. `page` fixture provides a [Page](/docs/api/class-page "Page") object that is available to the test.

Playwright Test comes with builtin fixtures listed below, and you can add your own fixtures as well. Playwright Test also [provides options](/docs/api/class-testoptions "TestOptions") to configure [fixtures.browser](/docs/api/class-fixtures#fixtures-browser), [fixtures.context](/docs/api/class-fixtures#fixtures-context) and [fixtures.page](/docs/api/class-fixtures#fixtures-page).

------------------------------------------------------------------------

## Properties[​](#properties "Direct link to Properties") 

### browser[​](#fixtures-browser "Direct link to browser") 

Added in: v1.10 fixtures.browser

[Browser](/docs/api/class-browser "Browser") instance is shared between all tests in the [same worker](/docs/test-parallel) - this makes testing efficient. However, each test runs in an isolated [BrowserContext](/docs/api/class-browsercontext "BrowserContext") and gets a fresh environment.

Learn how to [configure browser](/docs/test-configuration) and see [available options](/docs/api/class-testoptions "TestOptions").

**Usage**

``` 
test.beforeAll(async () => );
```

**Type**

-   [Browser](/docs/api/class-browser "Browser")

------------------------------------------------------------------------

### browserName[​](#fixtures-browser-name "Direct link to browserName") 

Added in: v1.10 fixtures.browserName

Name of the browser that runs tests. Defaults to `'chromium'`. Useful to [annotate tests](/docs/test-annotations) based on the browser.

**Usage**

``` 
test('skip this test in Firefox', async () => );
```

**Type**

-   \"chromium\" \| \"firefox\" \| \"webkit\"

------------------------------------------------------------------------

### context[​](#fixtures-context "Direct link to context") 

Added in: v1.10 fixtures.context

Isolated [BrowserContext](/docs/api/class-browsercontext "BrowserContext") instance, created for each test. Since contexts are isolated between each other, every test gets a fresh environment, even when multiple tests run in a single [Browser](/docs/api/class-browser "Browser") for maximum efficiency.

Learn how to [configure context](/docs/test-configuration) and see [available options](/docs/api/class-testoptions "TestOptions").

Default [fixtures.page](/docs/api/class-fixtures#fixtures-page) belongs to this context.

**Usage**

``` 
test('example test', async () => );
```

**Type**

-   [BrowserContext](/docs/api/class-browsercontext "BrowserContext")

------------------------------------------------------------------------

### page[​](#fixtures-page "Direct link to page") 

Added in: v1.10 fixtures.page

Isolated [Page](/docs/api/class-page "Page") instance, created for each test. Pages are isolated between tests due to [fixtures.context](/docs/api/class-fixtures#fixtures-context) isolation.

This is the most common fixture used in a test.

**Usage**

``` 
import  from '@playwright/test';

test('basic test', async () => );
```

**Type**

-   [Page](/docs/api/class-page "Page")

------------------------------------------------------------------------

### request[​](#fixtures-request "Direct link to request") 

Added in: v1.10 fixtures.request

Isolated [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext") instance for each test.

**Usage**

``` 
import  from '@playwright/test';

test('basic test', async () => 
  });
  // ...
});
```

**Type**

-   [APIRequestContext](/docs/api/class-apirequestcontext "APIRequestContext")