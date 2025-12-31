# Source: https://playwright.dev/docs/codegen

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Test generator]

On this page

<div>

# Test generator

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright comes with the ability to generate tests for you as you perform actions in the browser and is a great way to quickly get started with testing. Playwright will look at your page and figure out the best locator, prioritizing [role, text and test id locators](/docs/locators). If the generator finds multiple elements matching the locator, it will improve the locator to make it resilient that uniquely identify the target element.

## Generate tests in VS Code[​](#generate-tests-in-vs-code "Direct link to Generate tests in VS Code") 

Install the VS Code extension and generate tests directly from VS Code. The extension is available on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-playwright.playwright). Check out our guide on [getting started with VS Code](/docs/getting-started-vscode).