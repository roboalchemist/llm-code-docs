# Source: https://playwright.dev/docs/api/class-weberror

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [WebError]

On this page

<div>

# WebError

</div>

[WebError](/docs/api/class-weberror "WebError") class represents an unhandled exception thrown in the page. It is dispatched via the [browserContext.on(\'weberror\')](/docs/api/class-browsercontext#browser-context-event-web-error) event.

``` 
// Log all uncaught errors to the terminal
context.on('weberror', webError => "`);
});

// Navigate to a page with an exception.
await page.goto('data:text/html,<script>throw new Error("Test")</script>');
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### error[​](#web-error-error "Direct link to error") 

Added in: v1.38 webError.error

Unhandled error that was thrown.

**Usage**

``` 
webError.error();
```

**Returns**

-   [Error](https://nodejs.org/api/errors.html#errors_class_error "Error")[][\#](#web-error-error-return)

------------------------------------------------------------------------

### page[​](#web-error-page "Direct link to page") 

Added in: v1.38 webError.page

The page that produced this unhandled exception, if any.

**Usage**

``` 
webError.page();
```

**Returns**

-   [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") \| [Page](/docs/api/class-page "Page")[][\#](#web-error-page-return)