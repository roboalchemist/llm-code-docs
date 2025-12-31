# Source: https://playwright.dev/docs/api/class-logger

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [Logger]

On this page

<div>

# Logger

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]Deprecated

This class is deprecated. The logs pumped through this class are incomplete. Please use tracing instead.

Playwright generates a lot of logs and they are accessible via the pluggable logger sink.

``` 
const  = require('playwright');  // Or 'firefox' or 'webkit'.

(async () =>  $`)
    }
  });
  // ...
})();
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### isEnabled[​](#logger-is-enabled "Direct link to isEnabled") 

Added before v1.9 logger.isEnabled

Determines whether sink is interested in the logger with the given name and severity.

**Usage**

``` 
logger.isEnabled(name, severity);
```

**Arguments**

-   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#logger-is-enabled-option-name)

    logger name

-   `severity` \"verbose\" \| \"info\" \| \"warning\" \| \"error\"[][\#](#logger-is-enabled-option-severity)

**Returns**

-   [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[][\#](#logger-is-enabled-return)

------------------------------------------------------------------------

### log[​](#logger-log "Direct link to log") 

Added before v1.9 logger.log

**Usage**

``` 
logger.log(name, severity, message, args, hints);
```

**Arguments**

-   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#logger-log-option-name)

    logger name

-   `severity` \"verbose\" \| \"info\" \| \"warning\" \| \"error\"[][\#](#logger-log-option-severity)

-   `message` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") \| [Error](https://nodejs.org/api/errors.html#errors_class_error "Error")[][\#](#logger-log-option-message)

    log message format

-   `args` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")\<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")\>[][\#](#logger-log-option-args)

    message arguments

-   `hints` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[][\#](#logger-log-option-hints)

    -   `color` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*

        Optional preferred logger color.

    optional formatting hints