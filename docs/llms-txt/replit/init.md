# Source: https://docs.replit.com/extensions/api/init.md

# init API

> Learn how to initialize a Replit extension, establish a handshake with the Replit App, and manage event listeners using the init() method.

The `init()` method initializes the Extension, establishes a handshake with the Replit App, and adds an event listener to the window object. It takes as an argument an object containing optional parameters for the initialization process. It returns a function that removes the event listener added to the window object.

## Usage

```ts  theme={null}
import { init } from '@replit/extensions';
```

## Signature

```ts  theme={null}
init(args: ReplitInitArgs): Promise<ReplitInitOutput>
```

## Types

### HandshakeStatus

An enumerated set of values for the Handshake between the workspace and an extension

| Property | Type |
| -------- | ---- |

### ReplitInitArgs

The Replit init() function arguments

| Property | Type     |
| -------- | -------- |
| timeout? | `number` |

### ReplitInitOutput

The output of the Replit init() function

| Property | Type                                  |
| -------- | ------------------------------------- |
| dispose  | `Function`                            |
| status   | [`HandshakeStatus`](#handshakestatus) |

### HandshakeStatus

An enumerated set of values for the Handshake between the workspace and an extension

```ts  theme={null}
Error = 'error'
Loading = 'loading'
Ready = 'ready'
```
