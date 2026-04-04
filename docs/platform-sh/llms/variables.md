# Source: https://docs.upsun.com/development/variables.md

# Source: https://docs.upsun.com/create-apps/image-properties/variables.md

# variables


A variables dictionary that defines variables to control the environment.

Optional in [single-runtime](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) and [composable](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties) images.

Upsun provides a number of ways to set [variables](https://docs.upsun.com/development/variables.md).
Variables set in your app configuration have the lowest precedence,
meaning they're overridden by any conflicting values provided elsewhere.

All variables set in your app configuration must have a prefix.
Some [prefixes have specific meanings](https://docs.upsun.com/development/variables.md#variable-prefixes).

Variables with the prefix `env` are available as a separate environment variable.
All other variables are available in
the [`PLATFORM_VARIABLES` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

The following example sets two variables:

- A variable named `env:AUTHOR` with the value `Juan` that's available in the environment as `AUTHOR`
- A variable named `d8config:system.site:name` with the value `My site rocks`
  that's available in the `PLATFORM_VARIABLES` environment variable

```yaml {}
applications:
  myapp:
    type: 'python:3.14'
    source:
      root: "/"
    variables:
      env:
        AUTHOR: 'Juan'
      d8config:
        "system.site:name": 'My site rocks'
```

    .upsun/config.yaml

```yaml {}
applications:
  myapp:
    type: "composable:25.11"
    source:
      root: "/"
    stack: 
      runtimes: [ "python@3.14" ]
    variables:
      env:
        AUTHOR: 'Juan'
      d8config:
        "system.site:name": 'My site rocks'
```

You can also define and access more [complex values](https://docs.upsun.com/development/variables/use-variables.md#access-complex-values).


