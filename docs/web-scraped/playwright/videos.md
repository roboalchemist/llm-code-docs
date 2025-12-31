# Source: https://playwright.dev/docs/videos

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Videos]

On this page

<div>

# Videos

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

With Playwright you can record videos for your tests.

## Record video[​](#record-video "Direct link to Record video") 

Playwright Test can record videos for your tests, controlled by the `video` option in your Playwright config. By default videos are off.

-   `'off'` - Do not record video.
-   `'on'` - Record video for each test.
-   `'retain-on-failure'` - Record video for each test, but remove all videos from successful test runs.
-   `'on-first-retry'` - Record video only when retrying a test for the first time.

Video files will appear in the test output directory, typically `test-results`. See [testOptions.video](/docs/api/class-testoptions#test-options-video) for advanced video configuration.

Videos are saved upon [browser context](/docs/browser-contexts) closure at the end of a test. If you create a browser context manually, make sure to await [browserContext.close()](/docs/api/class-browsercontext#browser-context-close).

-   Test
-   Library

playwright.config.ts

``` 
import  from '@playwright/test';
export default defineConfig(,
});
```

``` 
const context = await browser.newContext( });
// Make sure to await close, so that videos are saved.
await context.close();
```

You can also specify video size. The video size defaults to the viewport size scaled down to fit 800x800. The video of the viewport is placed in the top-left corner of the output video, scaled down to fit if necessary. You may need to set the viewport size to match your desired video size.

-   Test
-   Library

playwright.config.ts

``` 
import  from '@playwright/test';
export default defineConfig(
    }
  },
});
```

``` 
const context = await browser.newContext(,
  }
});
```

For multi-page scenarios, you can access the video file associated with the page via the [page.video()](/docs/api/class-page#page-video).

``` 
const path = await page.video().path();
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Note that the video is only available after the page or browser context is closed.