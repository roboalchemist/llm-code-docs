# Source: https://playwright.dev/docs/test-snapshots

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Visual comparisons]

On this page

<div>

# Visual comparisons

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright Test includes the ability to produce and visually compare screenshots using `await expect(page).toHaveScreenshot()`. On first execution, Playwright test will generate reference screenshots. Subsequent runs will compare against the reference.

example.spec.ts

``` 
import  from '@playwright/test';

test('example test', async () => );
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

Browser rendering can vary based on the host OS, version, settings, hardware, power source (battery vs. power adapter), headless mode, and other factors. For consistent screenshots, run tests in the same environment where the baseline screenshots were generated.

## Generating screenshots[​](#generating-screenshots "Direct link to Generating screenshots") 

When you run above for the first time, test runner will say:

``` 
Error: A snapshot doesn't exist at example.spec.ts-snapshots/example-test-1-chromium-darwin.png, writing actual.
```

That\'s because there was no golden file yet. This method took a bunch of screenshots until two consecutive screenshots matched, and saved the last screenshot to file system. It is now ready to be added to the repository.

The name of the folder with the golden expectations starts with the name of your test file:

``` 
drwxr-xr-x  5 user  group  160 Jun  4 11:46 .
drwxr-xr-x  6 user  group  192 Jun  4 11:45 ..
-rw-r--r--  1 user  group  231 Jun  4 11:16 example.spec.ts
drwxr-xr-x  3 user  group   96 Jun  4 11:46 example.spec.ts-snapshots
```

The snapshot name `example-test-1-chromium-darwin.png` consists of a few parts:

-   `example-test-1.png` - an auto-generated name of the snapshot. Alternatively you can specify snapshot name as the first argument of the `toHaveScreenshot()` method:

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    await expect(page).toHaveScreenshot('landing.png');
    ```
    :::
    :::

-   `chromium-darwin` - the browser name and the platform. Screenshots differ between browsers and platforms due to different rendering, fonts and more, so you will need different snapshots for them. If you use multiple projects in your [configuration file](/docs/test-configuration), project name will be used instead of `chromium`.

The snapshot name and path can be configured with [testConfig.snapshotPathTemplate](/docs/api/class-testconfig#test-config-snapshot-path-template) in the playwright config.

> Note that `toHaveScreenshot()` also accepts an array of path segments to the snapshot file such as `expect().toHaveScreenshot(['relative', 'path', 'to', 'snapshot.png'])`. However, this path must stay within the snapshots directory for each test file (i.e. `a.spec.js-snapshots`), otherwise it will throw.

## Updating screenshots[​](#updating-screenshots "Direct link to Updating screenshots") 

Sometimes you need to update the reference screenshot, for example when the page has changed. Do this with the `--update-snapshots` flag.

``` 
npx playwright test --update-snapshots
```

## Options[​](#options "Direct link to Options") 

### maxDiffPixels[​](#maxdiffpixels "Direct link to maxDiffPixels") 

Playwright Test uses the [pixelmatch](https://github.com/mapbox/pixelmatch) library. You can [pass various options](/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1) to modify its behavior:

example.spec.ts

``` 
import  from '@playwright/test';

test('example test', async () => );
});
```

If you\'d like to share the default value among all the tests in the project, you can specify it in the playwright config, either globally or per project:

playwright.config.ts

``` 
import  from '@playwright/test';
export default defineConfig(,
  },
});
```

### stylePath[​](#stylepath "Direct link to stylePath") 

You can apply a custom stylesheet to your page while taking screenshot. This allows filtering out dynamic or volatile elements, hence improving the screenshot determinism.

screenshot.css

``` 
iframe 
```

example.spec.ts

``` 
import  from '@playwright/test';

test('example test', async () => );
});
```

If you\'d like to share the default value among all the tests in the project, you can specify it in the playwright config, either globally or per project:

playwright.config.ts

``` 
import  from '@playwright/test';
export default defineConfig(,
  },
});
```

## Non-image snapshots[​](#non-image-snapshots "Direct link to Non-image snapshots") 

Apart from screenshots, you can use `expect(value).toMatchSnapshot(snapshotName)` to compare text or arbitrary binary data. Playwright Test auto-detects the content type and uses the appropriate comparison algorithm.

Here we compare text content against the reference.

example.spec.ts

``` 
import  from '@playwright/test';

test('example test', async () => );
```

Snapshots are stored next to the test file, in a separate directory. For example, `my.spec.ts` file will produce and store snapshots in the `my.spec.ts-snapshots` directory. You should commit this directory to your version control (e.g. `git`), and review any changes to it.