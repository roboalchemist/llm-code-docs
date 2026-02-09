# Source: https://rspack.dev/config/infrastructure-logging.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/configuration/infrastructureLogging/](https://webpack.js.org/configuration/infrastructureLogging/)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# InfrastructureLogging

Options for infrastructure level logging. Generally used for logs unrelated to the Compilation.

## infrastructureLogging.appendOnly

- **Type:** `boolean`

Append lines to the output instead of updating existing output, useful for status messages. This option is used only when no custom [console](#infrastructureloggingconsole) is provided.

```js title="rspack.config.mjs"
export default {
  //...
  infrastructureLogging: {
    appendOnly: true,
    level: 'verbose',
  },
  plugins: [
    (compiler) => {
      const logger = compiler.getInfrastructureLogger('MyPlugin');
      logger.status('first output'); // this line won't be overridden with `appendOnly` enabled
      logger.status('second output');
    },
  ],
};
```

## infrastructureLogging.colors

- **Type:** `boolean`

Enable colorful output for infrastructure level logging. This option is used only when no custom [console](#infrastructureloggingconsole) is provided.

```js title="rspack.config.mjs"
export default {
  //...
  infrastructureLogging: {
    colors: true,
    level: 'verbose',
  },
  plugins: [
    (compiler) => {
      const logger = compiler.getInfrastructureLogger('MyPlugin');
      logger.log('this output will be colorful');
    },
  ],
};
```

## infrastructureLogging.console

- **Type:** `Console`
- **Default:** `Console`

Customize the console used for infrastructure level logging.

```js title="rspack.config.mjs"
export default {
  //...
  infrastructureLogging: {
    console: yourCustomConsole(),
  },
};
```

## infrastructureLogging.debug

- **Type:** `boolean | RegExp | function(name) => boolean | [string, RegExp, function(name) => boolean]`
- **Default:** `'false'`

Enable debug information of specified loggers such as plugins or loaders. Similar to [stats.loggingDebug](/config/stats.md#statsloggingdebug) option but for infrastructure. Defaults to `false`.

```js title="rspack.config.mjs"
export default {
  //...
  infrastructureLogging: {
    level: 'info',
    debug: ['MyPlugin', /MyPlugin/, (name) => name.contains('MyPlugin')],
  },
};
```

## infrastructureLogging.level

- **Type:** `'none' | 'error' | 'warn' | 'info' | 'log' | 'verbose'`
- **Default:** `'info'`

Enable infrastructure logging output. Similar to [stats.logging](/config/stats.md#statslogging) option but for infrastructure. Defaults to `'info'`.

Possible values:

- `'none'` - disable logging
- `'error'` - errors only
- `'warn'` - errors and warnings only
- `'info'` - errors, warnings, and info messages
- `'log'` - errors, warnings, info messages, log messages, groups, clears. Collapsed groups are displayed in a collapsed state.
- `'verbose'` - log everything except debug and trace. Collapsed groups are displayed in expanded state.

```js title="rspack.config.mjs"
export default {
  //...
  infrastructureLogging: {
    level: 'info',
  },
};
```

## infrastructureLogging.stream

- **Type:** `NodeJS.WritableStream`
- **Default:** `process.stderr`

Stream used for logging output. Defaults to `process.stderr`. This option is used only when no custom [console](#infrastructureloggingconsole) is provided.

```js title="rspack.config.mjs"
export default {
  //...
  infrastructureLogging: {
    stream: process.stderr,
  },
};
```
