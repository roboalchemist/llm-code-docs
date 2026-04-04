---
---
title: Integrations
description: "Sentry provides additional integrations designed to change configuration or add instrumentation to your application."
---

The Sentry SDK uses integrations to hook into the functionality of popular libraries to automatically instrument your application and give you the best data out of the box.

## Available Integrations

### Web Frameworks

|                                                                                                                       | **Auto-enabled** |
| --------------------------------------------------------------------------------------------------------------------- | :--------------: |
|     |        ✓         |
|      |        ✓         |
|    |        ✓         |
|    |        ✓         |
|     |        ✓         |
|     |        ✓         |
|    |        ✓         |
|      |        ✓         |
|      |        ✓         |
|  |        ✓         |
|   |        ✓         |
|   |                  |
|    |        ✓         |

### Databases

|                                                                                                                                        | **Auto-enabled** |
| -------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
|            |        ✓         |
|  |        ✓         |
|            |        ✓         |
|              |        ✓         |
|         |        ✓         |

### AI

|                                                                                                                                   | **Auto-enabled** |
| --------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
|               |        ✓         |
|        |                  |
|  |        ✓         |
|                     |        ✓         |
|   |                  |
|               |        ✓         |
|               |        ✓         |
|                   |                  |
|           |                  |
|  |                  |

### Data Processing

|                                                                                                                          | **Auto-enabled** |
| ------------------------------------------------------------------------------------------------------------------------ | :--------------: |
|   |                  |
|      |                  |
|     |                  |
|       |        ✓         |
|    |        ✓         |
|  |                  |
|      |        ✓         |
|        |        ✓         |
|       |                  |

### Feature Flags

|                                                                                                                    | **Auto-enabled** |
| ------------------------------------------------------------------------------------------------------------------ | :--------------: |
|  |                  |
|   |                  |
|       |                  |
|       |                  |

### Cloud Computing

|                                                                                                                                                          | **Auto-enabled** |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
|            |                  |
|                 |        ✓         |
|               |        ✓         |
|  |                  |
|         |                  |
|            |                  |

### HTTP Clients

|                                                                                                                                | **Auto-enabled** |
| ------------------------------------------------------------------------------------------------------------------------------ | :--------------: |
|  |        ✓         |
|                   |        ✓         |
| Python standard HTTP client (in the [Default Integrations](default-integrations/#stdlib))                                      |        ✓         |
| `Requests` HTTP instrumentation is done via the [Default Integrations](default-integrations/#stdlib).                          |        ✓         |

### GraphQL

|                                                                                                                           | **Auto-enabled** |
| ------------------------------------------------------------------------------------------------------------------------- | :--------------: |
|      |        ✓         |
|          |        ✓         |
|     |        ✓         |
|  |        ✓         |

### RPC

|                                                                                                        | **Auto-enabled** |
| ------------------------------------------------------------------------------------------------------ | :--------------: |
|  |        ✓         |

### Logging

|                                                                                                                 | **Auto-enabled** |
| --------------------------------------------------------------------------------------------------------------- | :--------------: |
|  |        ✓         |
|   |        ✓         |

### Miscellaneous

|                                                                                                                                     | **Auto-enabled** |
| ----------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
|           |                  |
|        |                  |
|      |                  |
|      |                  |
|  |                  |
|   |                  |
|         |                  |
|       |                  |
|         |                  |
|          |                  |
|           |                  |

### Default Integrations

| Integration                                          |
| ---------------------------------------------------- |
| [Argv](default-integrations/#argv)                   |
| [Atexit](default-integrations/#atexit)               |
| [Excepthook](default-integrations/#excepthook)       |
| [Deduplication](default-integrations/#deduplication) |
| [Stdlib](default-integrations/#stdlib)               |
| [Modules](default-integrations/#modules)             |
| [Logging](default-integrations/#logging)             |
| [Threading](default-integrations/#threading)         |

## Configuration

### Enabling Integrations

Integrations can be added using the [`integrations`](/platforms/python/configuration/options/#integrations) config option.

Integrations marked as "auto-enabled" in the above table will be turned on automatically, unless you set [`auto_enabling_integrations`](/platforms/python/configuration/options/#auto-enabling-integrations) to `False`. If you want to configure a specific integration's settings (for instance, change Flask's default `transaction_style`), add it to your `integrations` list as you would a non-auto-enabling integration and pass in the desired options.

```python
import sentry_sdk
from sentry_sdk.integrations.asyncio import AsyncioIntegration
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    integrations=[
        # The Flask integration is auto-enabling, but we want to change
        # transaction_style from the default "endpoint" to "url"
        FlaskIntegration(transaction_style="url"),
        # The asyncio integration is not enabled automatically
        # and needs to be added manually.
        AsyncioIntegration(),
    ],
)
```

### Disabling Integrations

To disable an integration, use the [`disabled_integrations`](/platforms/python/configuration/options/#disabled-integrations) config option:

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    # Do not use the Flask integration even if Flask is installed.
    disabled_integrations=[
        FlaskIntegration(),
    ],
)
```

It's also possible to disable all automatically-added integrations. There are two types:

- **Auto-enabled integrations** like `FlaskIntegration` are automatically added
  if the SDK detects that you have a corresponding package (like Flask) installed.
  This happens when the [`auto_enabling_integrations`](/platforms/python/configuration/options/#auto-enabling-integrations) option is set to
  `True` (default).
- **Default integrations** like `logging` or `excepthook` are always enabled,
  regardless of what packages you have installed, as long as the
  [`default_integrations`](/platforms/python/configuration/options/#default-integrations) option is `True` (default). They provide essential
  SDK functionality like error deduplication or event flushing at interpreter
  shutdown.

To disable all auto-enabling integrations, you can use the [`auto_enabling_integrations`](/platforms/python/configuration/options/#auto-enabling-integrations) option:

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    # Turn off all auto-enabling integrations except for Flask
    auto_enabling_integrations=False,
    integrations=[
        FlaskIntegration(),
    ],
)
```

To disable all [default integrations](default-integrations/),
set [`default_integrations`](/platforms/python/configuration/options/#default-integrations) to `False`. Note that this disables _all_ automatically
added integrations, both default and auto-enabling. Any integrations you want to use
then have to be manually specified via the [`integrations`](/platforms/python/configuration/options/#integrations) config option.

```python
import sentry_sdk
from sentry_sdk.integrations.atexit import AtexitIntegration
from sentry_sdk.integrations.argv import ArgvIntegration
from sentry_sdk.integrations.dedupe import DedupeIntegration
from sentry_sdk.integrations.excepthook import ExcepthookIntegration
from sentry_sdk.integrations.stdlib import StdlibIntegration
from sentry_sdk.integrations.modules import ModulesIntegration
from sentry_sdk.integrations.threading import ThreadingIntegration

sentry_sdk.init(
    # Turn off the default logging integration, but keep the rest.
    default_integrations=False,
    integrations=[
        AtexitIntegration(),
        ArgvIntegration(),
        DedupeIntegration(),
        ExcepthookIntegration(),
        StdlibIntegration(),
        ModulesIntegration(),
        ThreadingIntegration(),
    ],
)
```
