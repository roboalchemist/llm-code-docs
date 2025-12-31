# Source: https://playwright.dev/docs/api/class-timeouterror

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [TimeoutError]

<div>

# TimeoutError

</div>

-   extends: [Error](https://nodejs.org/api/errors.html#errors_class_error "Error")

TimeoutError is emitted whenever certain operations are terminated due to timeout, e.g. [locator.waitFor()](/docs/api/class-locator#locator-wait-for) or [browserType.launch()](/docs/api/class-browsertype#browser-type-launch).

``` 
const playwright = require('playwright');

(async () => );
  } catch (error) 
  await browser.close();
})();
```