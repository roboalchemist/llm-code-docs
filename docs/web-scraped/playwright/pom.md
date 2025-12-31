# Source: https://playwright.dev/docs/pom

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Page object models]

On this page

<div>

# Page object models

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Large test suites can be structured to optimize ease of authoring and maintenance. Page object models are one such approach to structure your test suite.

A page object represents a part of your web application. An e-commerce web application might have a home page, a listings page and a checkout page. Each of them can be represented by page object models.

Page objects **simplify authoring** by creating a higher-level API which suits your application and **simplify maintenance** by capturing element selectors in one place and create reusable code to avoid repetition.

## Implementation[​](#implementation "Direct link to Implementation") 

We will create a `PlaywrightDevPage` helper class to encapsulate common operations on the `playwright.dev` page. Internally, it will use the `page` object.

-   Test
-   Library

playwright-dev-page.ts

``` 
import  from '@playwright/test';

export class PlaywrightDevPage );
    this.gettingStartedHeader = page.locator('h1', );
    this.pomLink = page.locator('li', ).locator('a', );
    this.tocList = page.locator('article div.markdown ul > li > a');
  }

  async goto() 

  async getStarted() 

  async pageObjectModel() 
}
```

models/PlaywrightDevPage.js

``` 
class PlaywrightDevPage  page
   */
  constructor(page) );
    this.gettingStartedHeader = page.locator('h1', );
    this.pomLink = page.locator('li', ).locator('a', );
    this.tocList = page.locator('article div.markdown ul > li > a');
  }
  async getStarted() 

  async pageObjectModel() 
}
module.exports = ;
```

Now we can use the `PlaywrightDevPage` class in our tests.

-   Test
-   Library

example.spec.ts

``` 
import  from '@playwright/test';
import  from './playwright-dev-page';

test('getting started should contain table of contents', async () => );

test('should show Page Object Model article', async () => );
```

example.spec.js

``` 
const  = require('./playwright-dev-page');

// In the test
const page = await browser.newPage();
await playwrightDev.goto();
await playwrightDev.getStarted();
await expect(playwrightDev.tocList).toHaveText([
  `How to install Playwright`,
  `What's Installed`,
  `How to run the example test`,
  `How to open the HTML test report`,
  `Write tests using web first assertions, page fixtures and locators`,
  `Run single test, multiple tests, headed mode`,
  `Generate tests with Codegen`,
  `See a trace of your tests`
]);
```