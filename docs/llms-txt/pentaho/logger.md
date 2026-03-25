# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/cdf/logger.md

# Logger

## cdf. Logger

Static

This is a static class used for logging messages in the console.

**AMD Module**

`require(["cdf/Logger"], function(Logger) { /* code goes here */ });`

\*\*Source:\*\*Logger.js, line 16

## Members

| Name                | Description            |
| ------------------- | ---------------------- |
| loglevel : `string` | The current log level. |

## Methods

| Name              | Description                          |
| ----------------- | ------------------------------------ |
| debug(m)          | Logs a message at `debug` level.     |
| error(m)          | Logs a message at `error` level.     |
| exception(m)      | Logs a message at `exception` level. |
| info(m)           | Logs a message at `info` level.      |
| log(m, type, css) | Logs a message to the console.       |
| warn(m)           | Logs a message at `warn` level.      |

## Members Details

| loglevel: `string`                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------ |
| <p>The current log level.</p><p>\*\*Source:\*\*Logger.js, line 44</p><p><strong>Default Value:</strong>"debug"</p> |

\## Methods Details

| **debug**(m)                                                                               |               |                 |
| ------------------------------------------------------------------------------------------ | ------------- | --------------- |
| <p>Logs a message at <code>debug</code> level.</p><p>\*\*Source:\*\*Logger.js, line 87</p> |               |                 |
| Name                                                                                       | Default Value | Summary         |
| m : `string`                                                                               |               | Message to log. |

| **error**(m)                                                                                |               |                 |
| ------------------------------------------------------------------------------------------- | ------------- | --------------- |
| <p>Logs a message at <code>error</code> level.</p><p>\*\*Source:\*\*Logger.js, line 117</p> |               |                 |
| Name                                                                                        | Default Value | Summary         |
| m : `string`                                                                                |               | Message to log. |

| **exception**(m)                                                                                |               |                                                                                  |
| ----------------------------------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------- |
| <p>Logs a message at <code>exception</code> level.</p><p>\*\*Source:\*\*Logger.js, line 127</p> |               |                                                                                  |
| Name                                                                                            | Default Value | Summary                                                                          |
| m : `string` \| `Object`                                                                        |               | Message to log or an `object` containing information about the exception to log. |

| **info**(m)                                                                               |               |                 |
| ----------------------------------------------------------------------------------------- | ------------- | --------------- |
| <p>Logs a message at <code>info</code> level.</p><p>\*\*Source:\*\*Logger.js, line 97</p> |               |                 |
| Name                                                                                      | Default Value | Summary         |
| m : `string`                                                                              |               | Message to log. |

| **log**(m, type, css)                                                                                                                                                   |               |                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------ |
| <p>Logs a message to the console using the specified <code>type</code> log level if it is allowed by the current log level.</p><p>\*\*Source:\*\*Logger.js, line 54</p> |               |                                                                          |
| Name                                                                                                                                                                    | Default Value | Summary                                                                  |
| m : `string` \| `Object`                                                                                                                                                |               | Message to log or an `object` containing information about an exception. |
| type : `string`Optional                                                                                                                                                 | "info"        | The log level, one of the registered log `levels`.                       |
| css : `string`Optional                                                                                                                                                  |               | CSS styling rules for the message.                                       |

| **warn**(m)                                                                                |               |                 |
| ------------------------------------------------------------------------------------------ | ------------- | --------------- |
| <p>Logs a message at <code>warn</code> level.</p><p>\*\*Source:\*\*Logger.js, line 107</p> |               |                 |
| Name                                                                                       | Default Value | Summary         |
| m : `string`                                                                               |               | Message to log. |
