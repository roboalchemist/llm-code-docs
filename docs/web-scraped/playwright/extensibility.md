# Source: https://playwright.dev/docs/extensibility

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Extensibility]

On this page

<div>

# Extensibility

</div>

## Custom selector engines[​](#custom-selector-engines "Direct link to Custom selector engines") 

Playwright supports custom selector engines, registered with [selectors.register()](/docs/api/class-selectors#selectors-register).

Selector engine should have the following properties:

-   `query` function to query first element matching `selector` relative to the `root`.
-   `queryAll` function to query all elements matching `selector` relative to the `root`.

By default the engine is run directly in the frame\'s JavaScript context and, for example, can call an application-defined function. To isolate the engine from any JavaScript in the frame, but leave access to the DOM, register the engine with `` option. Content script engine is safer because it is protected from any tampering with the global objects, for example altering `Node.prototype` methods. All built-in selector engines run as content scripts. Note that running as a content script is not guaranteed when the engine is used together with other custom engines.

Selectors must be registered before creating the page.

An example of registering selector engine that queries elements based on a tag name:

baseTest.ts

``` 
import  from '@playwright/test';

export  from '@playwright/test';

// Must be a function that evaluates to a selector engine instance.
const createTagNameEngine = () => (,

  // Returns all elements matching given selector in the root's subtree.
  queryAll(root, selector) 
});

export const test = base.extend<, >(, use) => , ],
});
```

example.spec.ts

``` 
import  from './baseTest';

test('selector engine test', async () => );
```