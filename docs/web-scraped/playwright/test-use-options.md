# Source: https://playwright.dev/docs/test-use-options

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Configuration (use)]

On this page

<div>

# Configuration (use)

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

In addition to configuring the test runner you can also configure [Emulation](#emulation-options), [Network](#network-options) and [Recording](#recording-options) for the [Browser](/docs/api/class-browser "Browser") or [BrowserContext](/docs/api/class-browsercontext "BrowserContext"). These options are passed to the `use: ` object in the Playwright config.

### Basic Options[​](#basic-options "Direct link to Basic Options") 

Set the base URL and storage state for all tests:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

Option

Description

[testOptions.baseURL](/docs/api/class-testoptions#test-options-base-url)

Base URL used for all pages in the context. Allows navigating by using just the path, for example `page.goto('/settings')`.

[testOptions.storageState](/docs/api/class-testoptions#test-options-storage-state)

Populates context with given storage state. Useful for easy authentication, [learn more](/docs/auth).

### Emulation Options[​](#emulation-options "Direct link to Emulation Options") 

With Playwright you can emulate a real device such as a mobile phone or tablet. See our [guide on projects](/docs/test-projects) for more info on emulating devices. You can also emulate the `"geolocation"`, `"locale"` and `"timezone"` for all tests or for a specific test as well as set the `"permissions"` to show notifications or change the `"colorScheme"`. See our [Emulation](/docs/emulation) guide to learn more.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,

    // Emulates the user locale.
    locale: 'en-GB',

    // Grants specified permissions to the browser context.
    permissions: ['geolocation'],

    // Emulates the user timezone.
    timezoneId: 'Europe/Paris',

    // Viewport used for all pages in the context.
    viewport: ,
  },
});
```

Option

Description

[testOptions.colorScheme](/docs/api/class-testoptions#test-options-color-scheme)

[Emulates](/docs/emulation#color-scheme-and-media) `'prefers-colors-scheme'` media feature, supported values are `'light'` and `'dark'`

[testOptions.geolocation](/docs/api/class-testoptions#test-options-geolocation)

Context [geolocation](/docs/emulation#geolocation).

[testOptions.locale](/docs/api/class-testoptions#test-options-locale)

[Emulates](/docs/emulation#locale--timezone) the user locale, for example `en-GB`, `de-DE`, etc.

[testOptions.permissions](/docs/api/class-testoptions#test-options-permissions)

A list of [permissions](/docs/emulation#permissions) to grant to all pages in the context.

[testOptions.timezoneId](/docs/api/class-testoptions#test-options-timezone-id)

Changes the [timezone](/docs/emulation#locale--timezone) of the context.

[testOptions.viewport](/docs/api/class-testoptions#test-options-viewport)

[Viewport](/docs/emulation#viewport) used for all pages in the context.

### Network Options[​](#network-options "Direct link to Network Options") 

Available options to configure networking:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,

    // Credentials for HTTP authentication.
    httpCredentials: ,

    // Whether to ignore HTTPS errors during navigation.
    ignoreHTTPSErrors: true,

    // Whether to emulate network being offline.
    offline: true,

    // Proxy settings used for all pages in the test.
    proxy: ,
  },
});
```

Option

Description

[testOptions.acceptDownloads](/docs/api/class-testoptions#test-options-accept-downloads)

Whether to automatically download all the attachments, defaults to `true`. [Learn more](/docs/downloads) about working with downloads.

[testOptions.extraHTTPHeaders](/docs/api/class-testoptions#test-options-extra-http-headers)

An object containing additional HTTP headers to be sent with every request. All header values must be strings.

[testOptions.httpCredentials](/docs/api/class-testoptions#test-options-http-credentials)

Credentials for [HTTP authentication](/docs/network#http-authentication).

[testOptions.ignoreHTTPSErrors](/docs/api/class-testoptions#test-options-ignore-https-errors)

Whether to ignore HTTPS errors during navigation.

[testOptions.offline](/docs/api/class-testoptions#test-options-offline)

Whether to emulate network being offline.

[testOptions.proxy](/docs/api/class-testoptions#test-options-proxy)

[Proxy settings](/docs/network#http-proxy) used for all pages in the test.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

You don\'t have to configure anything to mock network requests. Just define a custom [Route](/docs/api/class-route "Route") that mocks the network for a browser context. See our [network mocking guide](/docs/network) to learn more.

### Recording Options[​](#recording-options "Direct link to Recording Options") 

With Playwright you can capture screenshots, record videos as well as traces of your test. By default these are turned off but you can enable them by setting the `screenshot`, `video` and `trace` options in your `playwright.config.js` file.

Trace files, screenshots and videos will appear in the test output directory, typically `test-results`.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

Option

Description

[testOptions.screenshot](/docs/api/class-testoptions#test-options-screenshot)

Capture [screenshots](/docs/screenshots) of your test. Options include `'off'`, `'on'` and `'only-on-failure'`

[testOptions.trace](/docs/api/class-testoptions#test-options-trace)

Playwright can produce test traces while running the tests. Later on, you can view the trace and get detailed information about Playwright execution by opening [Trace Viewer](/docs/trace-viewer). Options include: `'off'`, `'on'`, `'retain-on-failure'` and `'on-first-retry'`

[testOptions.video](/docs/api/class-testoptions#test-options-video)

Playwright can record [videos](/docs/videos) for your tests. Options include: `'off'`, `'on'`, `'retain-on-failure'` and `'on-first-retry'`

### Other Options[​](#other-options "Direct link to Other Options") 

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

Option

Description

[testOptions.actionTimeout](/docs/api/class-testoptions#test-options-action-timeout)

Timeout for each Playwright action in milliseconds. Defaults to `0` (no timeout). Learn more about [timeouts](/docs/test-timeouts) and how to set them for a single test.

[testOptions.browserName](/docs/api/class-testoptions#test-options-browser-name)

Name of the browser that runs tests. Defaults to \'chromium\'. Options include `chromium`, `firefox`, or `webkit`.

[testOptions.bypassCSP](/docs/api/class-testoptions#test-options-bypass-csp)

Toggles bypassing Content-Security-Policy. Useful when CSP includes the production origin. Defaults to `false`.

[testOptions.channel](/docs/api/class-testoptions#test-options-channel)

Browser channel to use. [Learn more](/docs/browsers) about different browsers and channels.

[testOptions.headless](/docs/api/class-testoptions#test-options-headless)

Whether to run the browser in headless mode meaning no browser is shown when running tests. Defaults to `true`.

[testOptions.testIdAttribute](/docs/api/class-testoptions#test-options-test-id-attribute)

Changes the default [`data-testid` attribute](/docs/locators#locate-by-test-id) used by Playwright locators.

### More browser and context options[​](#more-browser-and-context-options "Direct link to More browser and context options") 

Any options accepted by [browserType.launch()](/docs/api/class-browsertype#browser-type-launch), [browser.newContext()](/docs/api/class-browser#browser-new-context) or [browserType.connect()](/docs/api/class-browsertype#browser-type-connect) can be put into `launchOptions`, `contextOptions` or `connectOptions` respectively in the `use` section.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
  },
});
```

However, most common ones like `headless` or `viewport` are available directly in the `use` section - see [basic options](#basic-options), [emulation](#emulation-options) or [network](#network-options).

### Explicit Context Creation and Option Inheritance[​](#explicit-context-creation-and-option-inheritance "Direct link to Explicit Context Creation and Option Inheritance") 

If using the built-in `browser` fixture, calling [browser.newContext()](/docs/api/class-browser#browser-new-context) will create a context with options inherited from the config:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
  },
});
```

An example test illustrating the initial context options are set:

``` 
test('should inherit use options on context when using built-in browser fixture', async () => );
```

### Configuration Scopes[​](#configuration-scopes "Direct link to Configuration Scopes") 

You can configure Playwright globally, per project, or per test. For example, you can set the locale to be used globally by adding `locale` to the `use` option of the Playwright config, and then override it for a specific project using the `project` option in the config. You can also override it for a specific test by adding `test.use()` in the test file and passing in the options.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

You can override options for a specific project using the `project` option in the Playwright config.

``` 
import  from '@playwright/test';

export default defineConfig(,
    },
  ],
});
```

You can override options for a specific test file by using the `test.use()` method and passing in the options. For example to run tests with the French locale for a specific test:

``` 
import  from '@playwright/test';

test.use();

test('example', async () => );
```

The same works inside a describe block. For example to run tests in a describe block with the French locale:

``` 
import  from '@playwright/test';

test.describe('french language block', () => );

  test('example', async () => );
});
```

### Reset an option[​](#reset-an-option "Direct link to Reset an option") 

You can reset an option to the value defined in the config file. Consider the following config that sets a `baseURL`:

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

You can now configure `baseURL` for a file, and also opt-out for a single test.

intro.spec.ts

``` 
import  from '@playwright/test';

// Configure baseURL for this file.
test.use();

test('check intro contents', async () => );

test.describe(() => );

  test('can navigate to intro from the home page', async () => );
});
```

If you would like to completely reset the value to `undefined`, use a long-form fixture notation.

intro.spec.ts

``` 
import  from '@playwright/test';

// Completely unset baseURL for this file.
test.use(, use) => use(undefined), ],
});

test('no base url', async () => );
```