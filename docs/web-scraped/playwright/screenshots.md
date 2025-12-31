# Source: https://playwright.dev/docs/screenshots

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Screenshots]

On this page

<div>

# Screenshots

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Here is a quick way to capture a screenshot and save it into a file:

``` 
await page.screenshot();
```

[Screenshots API](/docs/api/class-page#page-screenshot) accepts many parameters for image format, clip area, quality, etc. Make sure to check them out.

## Full page screenshots[​](#full-page-screenshots "Direct link to Full page screenshots") 

Full page screenshot is a screenshot of a full scrollable page, as if you had a very tall screen and the page could fit it entirely.

``` 
await page.screenshot();
```

## Capture into buffer[​](#capture-into-buffer "Direct link to Capture into buffer") 

Rather than writing into a file, you can get a buffer with the image and post-process it or pass it to a third party pixel diff facility.

``` 
const buffer = await page.screenshot();
console.log(buffer.toString('base64'));
```

## Element screenshot[​](#element-screenshot "Direct link to Element screenshot") 

Sometimes it is useful to take a screenshot of a single element.

``` 
await page.locator('.header').screenshot();
```