# Source: https://docs.replit.com/extensions/api/debug.md

# debug API

> Learn how to use the debug API module to log data, warnings, and errors to the Extension Devtools in Replit extensions.

The `debug` api module allows you to log data to the Extension Devtools

## Usage

```ts  theme={null}
import { debug } from '@replit/extensions';
```

## Methods

### `debug.info`

Logs information to the Extension Devtools

```ts  theme={null}
info(message: string, data: Data): Promise<void>
```

### `debug.warn`

Logs a warning to the extension devtools

```ts  theme={null}
warn(message: string, data: Data): Promise<void>
```

### `debug.error`

Logs an error message to the extension devtools

```ts  theme={null}
error(message: string, data: Data): Promise<void>
```

### `debug.log`

Logs information to the Extension Devtools

```ts  theme={null}
log(message: string, data: Data): Promise<void>
```
