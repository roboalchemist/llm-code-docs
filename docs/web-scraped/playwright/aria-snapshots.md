# Source: https://playwright.dev/docs/aria-snapshots

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Snapshot testing]

On this page

<div>

# Snapshot testing

</div>

## Overview[​](#overview "Direct link to Overview") 

With Playwright\'s Snapshot testing you can assert the accessibility tree of a page against a predefined snapshot template.

``` 
await page.goto('https://playwright.dev/');
await expect(page.getByRole('banner')).toMatchAriaSnapshot(`
  - banner:
    - heading /Playwright enables reliable end-to-end/ [level=1]
    - link "Get started"
    - link "Star microsoft/playwright on GitHub"
    - link /[\\d]+k\\+ stargazers on GitHub/
`);
```