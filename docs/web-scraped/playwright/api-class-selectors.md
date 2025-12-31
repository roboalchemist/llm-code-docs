# Source: https://playwright.dev/docs/api/class-selectors

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [Selectors]

On this page

<div>

# Selectors

</div>

Selectors can be used to install custom selector engines. See [extensibility](/docs/extensibility) for more information.

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### register[​](#selectors-register "Direct link to register") 

Added before v1.9 selectors.register

Selectors must be registered before creating the page.

**Usage**

An example of registering selector engine that queries elements based on a tag name:

``` 
const  = require('@playwright/test');  // Or 'chromium' or 'webkit'.

(async () => ,

    // Returns all elements matching given selector in the root's subtree.
    queryAll(root, selector) 
  });

  // Register the engine. Selectors will be prefixed with "tag=".
  await selectors.register('tag', createTagNameEngine);

  const browser = await firefox.launch();
  const page = await browser.newPage();
  await page.setContent(`<div><button>Click me</button></div>`);

  // Use the selector prefixed with its name.
  const button = page.locator('tag=button');
  // We can combine it with built-in locators.
  await page.locator('tag=div').getByText('Click me').click();
  // Can use it in any methods supporting selectors.
  const buttonCount = await page.locator('tag=button').count();

  await browser.close();
})();
```

**Arguments**

-   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#selectors-register-option-name)

    Name that is used in selectors as a prefix, e.g. `` enables `foo=myselectorbody` selectors. May only contain `[a-zA-Z0-9_]` characters.

-   `script` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") \| [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") \| [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[][\#](#selectors-register-option-script)

    -   `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*

        Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working directory. Optional.

    -   `content` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*

        Raw script content. Optional.

    Script that evaluates to a selector engine instance. The script is evaluated in the page context.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `contentScript` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*[][\#](#selectors-register-option-content-script)

        Whether to run this selector engine in isolated JavaScript environment. This environment has access to the same DOM, but not any JavaScript objects from the frame\'s scripts. Defaults to `false`. Note that running as a content script is not guaranteed when this engine is used together with other registered engines.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#selectors-register-return)

------------------------------------------------------------------------

### setTestIdAttribute[​](#selectors-set-test-id-attribute "Direct link to setTestIdAttribute") 

Added in: v1.27 selectors.setTestIdAttribute

Defines custom attribute name to be used in [page.getByTestId()](/docs/api/class-page#page-get-by-test-id). `data-testid` is used by default.

**Usage**

``` 
selectors.setTestIdAttribute(attributeName);
```

**Arguments**

-   `attributeName` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#selectors-set-test-id-attribute-option-attribute-name)

    Test id attribute name.