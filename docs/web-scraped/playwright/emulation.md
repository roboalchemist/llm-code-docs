# Source: https://playwright.dev/docs/emulation

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Emulation]

On this page

<div>

# Emulation

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

With Playwright you can test your app on any browser as well as emulate a real device such as a mobile phone or tablet. Simply configure the devices you would like to emulate and Playwright will simulate the browser behavior such as `"userAgent"`, `"screenSize"`, `"viewport"` and if it `"hasTouch"` enabled. You can also emulate the `"geolocation"`, `"locale"` and `"timezone"` for all tests or for a specific test as well as set the `"permissions"` to show notifications or change the `"colorScheme"`.

## Devices[​](#devices "Direct link to Devices") 

Playwright comes with a [registry of device parameters](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json) using [playwright.devices](/docs/api/class-playwright#playwright-devices) for selected desktop, tablet and mobile devices. It can be used to simulate browser behavior for a specific device such as user agent, screen size, viewport and if it has touch enabled. All tests will run with the specified device parameters.

-   Test
-   Library

playwright.config.ts

``` 
import  from '@playwright/test'; // import devices

export default defineConfig(,
    },
    ,
    },
  ],
});
```

``` 
const  = require('playwright');
const browser = await chromium.launch();

const iphone13 = devices['iPhone 13'];
const context = await browser.newContext();
```

![playwright.dev website emulated for iPhone 13](https://user-images.githubusercontent.com/13063165/220411073-76fe59f9-9a2d-463d-8e30-c19a7deca133.png)

## Viewport[​](#viewport "Direct link to Viewport") 

The viewport is included in the device but you can override it for some tests with [page.setViewportSize()](/docs/api/class-page#page-set-viewport-size).

-   Test
-   Library

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
      },
    },
  ]
});
```

``` 
// Create context with given viewport
const context = await browser.newContext(
});
```

Test file:

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use(,
});

test('my test', async () => );
```

``` 
// Create context with given viewport
const context = await browser.newContext(
});

// Resize viewport for individual page
await page.setViewportSize();

// Emulate high-DPI
const context = await browser.newContext(,
  deviceScaleFactor: 2,
});
```

The same works inside a test file.

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.describe('specific viewport block', () =>  });

  test('my test', async () => );
});
```

``` 
// Create context with given viewport
const context = await browser.newContext(
});
const page = await context.newPage();
```

## isMobile[​](#ismobile "Direct link to isMobile") 

Whether the meta viewport tag is taken into account and touch events are enabled.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
    },
  ]
});
```

## Locale & Timezone[​](#locale--timezone "Direct link to Locale & Timezone") 

Emulate the browser Locale and Timezone which can be set globally for all tests in the config and then overridden for particular tests.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use();

test('my test for de lang in Berlin timezone', async () => );
```

``` 
const context = await browser.newContext();
```

![Bing in german lang and timezone](https://user-images.githubusercontent.com/13063165/220416571-ccc96ab1-44bb-4579-8430-64502fc24a15.png)

###### 

Note that this only affects the browser timezone and locale, not the test runner timezone. To set the test runner timezone, you can use the [`TZ` environment variable](https://nodejs.org/api/cli.html#tz).

## Permissions[​](#permissions "Direct link to Permissions") 

Allow app to show system notifications.

-   Test
-   Library

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

``` 
const context = await browser.newContext();
```

Allow notifications for a specific domain.

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.beforeEach(async () => );
});

test('first', async () => );
```

``` 
await context.grantPermissions(['notifications'], );
```

Revoke all permissions with [browserContext.clearPermissions()](/docs/api/class-browsercontext#browser-context-clear-permissions).

``` 
// Library
await context.clearPermissions();
```

## Geolocation[​](#geolocation "Direct link to Geolocation") 

Grant `"geolocation"` permissions and set geolocation to a specific area.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
    permissions: ['geolocation'],
  },
});
```

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use(,
  permissions: ['geolocation'],
});

test('my test with geolocation', async () => );
```

``` 
const context = await browser.newContext(,
  permissions: ['geolocation']
});
```

![geolocation for italy on bing maps](https://user-images.githubusercontent.com/13063165/220417670-bb22d815-f5cd-47c4-8562-0b88165eac27.png)

Change the location later:

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use(,
  permissions: ['geolocation'],
});

test('my test with geolocation', async () => );
});
```

``` 
await context.setGeolocation();
```

**Note** you can only change geolocation for all pages in the context.

## Color Scheme and Media[​](#color-scheme-and-media "Direct link to Color Scheme and Media") 

Emulate the users `"colorScheme"`. Supported values are \'light\' and \'dark\'. You can also emulate the media type with [page.emulateMedia()](/docs/api/class-page#page-emulate-media).

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use();

test('my test with dark mode', async () => );
```

``` 
// Create context with dark mode
const context = await browser.newContext();

// Create page with dark mode
const page = await browser.newPage();

// Change color scheme for the page
await page.emulateMedia();

// Change media for page
await page.emulateMedia();
```

![playwright web in dark mode](https://user-images.githubusercontent.com/13063165/220411638-55d2b051-4678-4da7-9f0b-ed22f5a3c47c.png)

## User Agent[​](#user-agent "Direct link to User Agent") 

The User Agent is included in the device and therefore you will rarely need to change it however if you do need to test a different user agent you can override it with the `userAgent` property.

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use();

test('my user agent test', async () => );
```

``` 
const context = await browser.newContext();
```

## Offline[​](#offline "Direct link to Offline") 

Emulate the network being offline.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

## JavaScript Enabled[​](#javascript-enabled "Direct link to JavaScript Enabled") 

Emulate a user scenario where JavaScript is disabled.

-   Test
-   Library

tests/example.spec.ts

``` 
import  from '@playwright/test';

test.use();

test('test with no JavaScript', async () => );
```

``` 
const context = await browser.newContext();
```