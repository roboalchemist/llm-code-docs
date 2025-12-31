# Source: https://playwright.dev/docs/api/class-snapshotassertions

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Assertions]
-   [SnapshotAssertions]

On this page

<div>

# SnapshotAssertions

</div>

Playwright provides methods for comparing page and element screenshots with expected values stored in files.

``` 
expect(screenshot).toMatchSnapshot('landing-page.png');
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### toMatchSnapshot(name)[​](#snapshot-assertions-to-match-snapshot-1 "Direct link to toMatchSnapshot(name)") 

Added in: v1.22 snapshotAssertions.toMatchSnapshot(name)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

To compare screenshots, use [expect(page).toHaveScreenshot()](/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1) instead.

Ensures that passed value, either a [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") or a [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer"), matches the expected snapshot stored in the test snapshots directory.

**Usage**

``` 
// Basic usage.
expect(await page.screenshot()).toMatchSnapshot('landing-page.png');

// Pass options to customize the snapshot comparison and have a generated name.
expect(await page.screenshot()).toMatchSnapshot('landing-page.png', );

// Configure image matching threshold.
expect(await page.screenshot()).toMatchSnapshot('landing-page.png', );

// Bring some structure to your snapshot files by passing file path segments.
expect(await page.screenshot()).toMatchSnapshot(['landing', 'step2.png']);
expect(await page.screenshot()).toMatchSnapshot(['landing', 'step3.png']);
```

Learn more about [visual comparisons](/docs/test-snapshots).

Note that matching snapshots only work with Playwright test runner.

**Arguments**

-   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") \| [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")\<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\>[][\#](#snapshot-assertions-to-match-snapshot-1-option-name)

    Snapshot name.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `maxDiffPixelRatio` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#snapshot-assertions-to-match-snapshot-1-option-max-diff-pixel-ratio)

        An acceptable ratio of pixels that are different to the total amount of pixels, between `0` and `1`. Default is configurable with `TestConfig.expect`. Unset by default.

    -   `maxDiffPixels` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#snapshot-assertions-to-match-snapshot-1-option-max-diff-pixels)

        An acceptable amount of pixels that could be different. Default is configurable with `TestConfig.expect`. Unset by default.

    -   `threshold` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#snapshot-assertions-to-match-snapshot-1-option-threshold)

        An acceptable perceived color difference in the [YIQ color space](https://en.wikipedia.org/wiki/YIQ) between the same pixel in compared images, between zero (strict) and one (lax), default is configurable with `TestConfig.expect`. Defaults to `0.2`.

------------------------------------------------------------------------

### toMatchSnapshot(options)[​](#snapshot-assertions-to-match-snapshot-2 "Direct link to toMatchSnapshot(options)") 

Added in: v1.22 snapshotAssertions.toMatchSnapshot(options)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

To compare screenshots, use [expect(page).toHaveScreenshot()](/docs/api/class-pageassertions#page-assertions-to-have-screenshot-2) instead.

Ensures that passed value, either a [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") or a [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer"), matches the expected snapshot stored in the test snapshots directory.

**Usage**

``` 
// Basic usage and the file name is derived from the test name.
expect(await page.screenshot()).toMatchSnapshot();

// Pass options to customize the snapshot comparison and have a generated name.
expect(await page.screenshot()).toMatchSnapshot();

// Configure image matching threshold and snapshot name.
expect(await page.screenshot()).toMatchSnapshot();
```

Learn more about [visual comparisons](/docs/test-snapshots).

Note that matching snapshots only work with Playwright test runner.

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `maxDiffPixelRatio` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#snapshot-assertions-to-match-snapshot-2-option-max-diff-pixel-ratio)

        An acceptable ratio of pixels that are different to the total amount of pixels, between `0` and `1`. Default is configurable with `TestConfig.expect`. Unset by default.

    -   `maxDiffPixels` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#snapshot-assertions-to-match-snapshot-2-option-max-diff-pixels)

        An acceptable amount of pixels that could be different. Default is configurable with `TestConfig.expect`. Unset by default.

    -   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") \| [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")\<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\> *(optional)*[][\#](#snapshot-assertions-to-match-snapshot-2-option-name)

        Snapshot name. If not passed, the test name and ordinals are used when called multiple times.

    -   `threshold` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#snapshot-assertions-to-match-snapshot-2-option-threshold)

        An acceptable perceived color difference in the [YIQ color space](https://en.wikipedia.org/wiki/YIQ) between the same pixel in compared images, between zero (strict) and one (lax), default is configurable with `TestConfig.expect`. Defaults to `0.2`.