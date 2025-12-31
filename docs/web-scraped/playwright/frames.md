# Source: https://playwright.dev/docs/frames

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Frames]

On this page

<div>

# Frames

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

A [Page](/docs/api/class-page "Page") can have one or more [Frame](/docs/api/class-frame "Frame") objects attached to it. Each page has a main frame and page-level interactions (like `click`) are assumed to operate in the main frame.

A page can have additional frames attached with the `iframe` HTML tag. These frames can be accessed for interactions inside the frame.

``` 
// Locate element inside frame
const username = await page.frameLocator('.frame-class').getByLabel('User Name');
await username.fill('John');
```

## Frame objects[​](#frame-objects "Direct link to Frame objects") 

One can access frame objects using the [page.frame()](/docs/api/class-page#page-frame) API:

``` 
// Get frame using the frame's name attribute
const frame = page.frame('frame-login');

// Get frame using frame's URL
const frame = page.frame();

// Interact with the frame
await frame.fill('#username-input', 'John');
```