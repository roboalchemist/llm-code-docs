# Source: https://kreya.app/docs/scripting-and-tests/operation-scripts/websocket-script-api-reference.md

# WebSocket script API reference

In operation scripts for WebSocket operations, despite the [operation script API](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md), the definitions below are available through the `kreya.webSocket` namespace. For example:

```
import { expect } from 'chai';

let responseCount = 0;

kreya.webSocket.onResponseMessage(response => {
  responseCount++;
  kreya.test('Response content', () => expect(response.content).to.contain(`Message ${responseCount}`));
});

kreya.webSocket.onCallCompleted(call => {
  kreya.trace('The WebSocket call completed.');

  kreya.test('Status code', () => expect(call.status.code).to.equal(1000));
});
```

## Functions[​](#functions "Direct link to Functions")

### onCallCompleted()[​](#oncallcompleted "Direct link to onCallCompleted()")

```
function onCallCompleted(callback: (arg: WebSocketScriptCallCompletedContext) => void | Promise<void>): void;
```

Hook which is called when the web socket call completes.

#### Parameters[​](#parameters "Direct link to Parameters")

| Parameter  | Type                                                                                                                  | Description                 |
| ---------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `callback` | (`arg`: [`WebSocketScriptCallCompletedContext`](#websocketscriptcallcompletedcontext)) => `void` \| `Promise`<`void`> | The callback to be invoked. |

#### Returns[​](#returns "Direct link to Returns")

`void`

***

### onResponseMessage()[​](#onresponsemessage "Direct link to onResponseMessage()")

```
function onResponseMessage(callback: (arg: WebSocketScriptResponseMessageContext) => void | Promise<void>): void;
```

Hook which is called when a web socket response message arrives.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter  | Type                                                                                                                      | Description                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `callback` | (`arg`: [`WebSocketScriptResponseMessageContext`](#websocketscriptresponsemessagecontext)) => `void` \| `Promise`<`void`> | The callback to be invoked. |

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### WebSocketScriptCallCompletedContext[​](#websocketscriptcallcompletedcontext "Direct link to WebSocketScriptCallCompletedContext")

```
type WebSocketScriptCallCompletedContext = {
  durationMillis: number;
  responseMessageCount: number;
  status: WebSocketScriptStatus;
};
```

Callback context of gRPC completed call callback.

#### Properties[​](#properties "Direct link to Properties")

##### durationMillis[​](#durationmillis "Direct link to durationMillis")

```
readonly durationMillis: number;
```

Duration of the call in milliseconds.

##### responseMessageCount[​](#responsemessagecount "Direct link to responseMessageCount")

```
readonly responseMessageCount: number;
```

The number of received response messages.

##### status[​](#status "Direct link to status")

```
readonly status: WebSocketScriptStatus;
```

The status of the call.

***

### WebSocketScriptResponseMessageContext[​](#websocketscriptresponsemessagecontext "Direct link to WebSocketScriptResponseMessageContext")

```
type WebSocketScriptResponseMessageContext = {
  content: string;
  index: number;
  isBinary: boolean;
  size: number;
};
```

Callback context of the callback when a gRPC response message has arrived.

#### Properties[​](#properties-1 "Direct link to Properties")

##### content[​](#content "Direct link to content")

```
readonly content: string;
```

The content of the message.

##### index[​](#index "Direct link to index")

```
readonly index: number;
```

The index of the response.

##### isBinary[​](#isbinary "Direct link to isBinary")

```
readonly isBinary: boolean;
```

Whether the message is binary. If true, the content is encoded as Base64.

##### size[​](#size "Direct link to size")

```
readonly size: number;
```

The size of the message in bytes.

***

### WebSocketScriptStatus[​](#websocketscriptstatus "Direct link to WebSocketScriptStatus")

```
type WebSocketScriptStatus = {
  code: number;
  detail?: string;
};
```

Status of a web socket call.

#### Properties[​](#properties-2 "Direct link to Properties")

##### code[​](#code "Direct link to code")

```
readonly code: number;
```

The status code.

##### detail?[​](#detail "Direct link to detail?")

```
readonly optional detail: string;
```

The status detail.
