# Source: https://playwright.dev/docs/protractor

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Migration]
-   [Migrating from Protractor]

On this page

<div>

# Migrating from Protractor

</div>

## Migration Principles[​](#migration-principles "Direct link to Migration Principles") 

-   No need for \"webdriver-manager\" / Selenium.
-   Protractor's [ElementFinder](https://www.protractortest.org/#/api?view=ElementFinder) ⇄ [Playwright Test Locator](/docs/api/class-locator)
-   Protractor's [`waitForAngular`](https://www.protractortest.org/#/api?view=ProtractorBrowser.prototype.waitForAngular) ⇄ Playwright Test [auto-waiting](/docs/actionability)
-   Don't forget to await in Playwright Test

## Cheat Sheet[​](#cheat-sheet "Direct link to Cheat Sheet") 

Protractor

Playwright Test

`element(by.buttonText('...'))`

`page.locator('button, input[type="button"], input[type="submit"] >> text="..."')`

`element(by.css('...'))`

`page.locator('...')`

`element(by.cssContainingText('..1..', '..2..'))`

`page.locator('..1.. >> text=..2..')`

`element(by.id('...'))`

`page.locator('#...')`

`element(by.model('...'))`

`page.locator('[ng-model="..."]')`

`element(by.repeater('...'))`

`page.locator('[ng-repeat="..."]')`

`element(by.xpath('...'))`

`page.locator('xpath=...')`

`element.all`

`page.locator`

`browser.get(url)`

`await page.goto(url)`

`browser.getCurrentUrl()`

`page.url()`

## Example[​](#example "Direct link to Example") 

Protractor:

``` 
describe('angularjs homepage todo list', function() );
});
```

Line-by-line migration to Playwright Test:

``` 
const  = require('@playwright/test'); // 1

test.describe('angularjs homepage todo list', () => ) => );

    // You wrote your first test, cross it off the list
    await todoList.nth(2).getByRole('textbox').click();
    const completedAmount = page.locator('.done-true');
    await expect(completedAmount).toHaveCount(2);
  });
});
```

Migration highlights (see inline comments in the Playwright Test code snippet):

1.  Each Playwright Test file has explicit import of the `test` and `expect` functions
2.  Test function is marked with `async`
3.  Playwright Test is given a `page` as one of its parameters. This is one of the many [useful fixtures](/docs/api/class-fixtures) in Playwright Test.
4.  Almost all Playwright calls are prefixed with `await`
5.  Locator creation with [page.locator()](/docs/api/class-page#page-locator) is one of the few methods that is sync.

## Polyfilling `waitForAngular`[​](#polyfilling-waitforangular "Direct link to polyfilling-waitforangular") 

Playwright Test has built-in [auto-waiting](/docs/actionability) that makes protractor\'s [`waitForAngular`](https://www.protractortest.org/#/api?view=ProtractorBrowser.prototype.waitForAngular) unneeded in general case.

However, it might come handy in some edge cases. Here\'s how to polyfill `waitForAngular` function in Playwright Test:

1.  Make sure you have protractor installed in your package.json

2.  Polyfill function

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    async function waitForAngular(page) ;
            (function() }).apply(null, [...$, callback]);
          })
        `);
      }

      await executeScriptAsync(page, clientSideScripts.waitForAngular, '');
    }
    ```
    :::
    :::

    If you don\'t want to keep a version protractor around, you can also use this simpler approach using this function (only works for Angular 2+):

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    async function waitForAngular(page) 
        }
      });
    }
    ```
    :::
    :::

3.  Polyfill usage

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    const page = await context.newPage();
    await page.goto('https://example.org');
    await waitForAngular(page);
    ```
    :::
    :::

## Playwright Test Super Powers[​](#playwright-test-super-powers "Direct link to Playwright Test Super Powers") 

Once you\'re on Playwright Test, you get a lot!

-   Full zero-configuration TypeScript support
-   Run tests across **all web engines** (Chrome, Firefox, Safari) on **any popular operating system** (Windows, macOS, Ubuntu)
-   Full support for multiple origins, [(i)frames](/docs/api/class-frame), [tabs and contexts](/docs/pages)
-   Run tests in parallel across multiple browsers
-   Built-in test [artifact collection](/docs/test-use-options#recording-options)

You also get all these ✨ awesome tools ✨ that come bundled with Playwright Test:

-   [Playwright Inspector](/docs/debug)
-   [Playwright Test Code generation](/docs/codegen-intro)
-   [Playwright Tracing](/docs/trace-viewer) for post-mortem debugging

## Further Reading[​](#further-reading "Direct link to Further Reading") 

Learn more about Playwright Test runner:

-   [Getting Started](/docs/intro)
-   [Fixtures](/docs/test-fixtures)
-   [Locators](/docs/locators)
-   [Assertions](/docs/test-assertions)
-   [Auto-waiting](/docs/actionability)