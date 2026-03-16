# Source: https://kreya.app/docs/scripting-and-tests/operation-scripts/grpc-script-api-reference.md

# gRPC script API reference

In operation scripts for gRPC operations, despite the [operation script API](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md), the definitions below are available through the `kreya.grpc` namespace. For example:

```
import { expect } from 'chai';

let names = [];

kreya.grpc.onResponse(msg => {
  kreya.test('Size should be ok', () => expect(msg.size).to.be.gt(10));
  kreya.test('Greeting should start with Hello', () => expect(msg.content.greeting.startsWith('Hello')).to.be.true);

  // Store all received names to use them when the gRPC call completes
  names.push(msg.content.greeting.substr('Hello '.length));
});

kreya.grpc.onCallCompleted(call => {
  kreya.test('Status should be ok', () => expect(call.status.code).to.equal(0));

  kreya.trace(`Got ${call.responseCount} names: ${names.join(', ')}`);
});
```

info

The `msg.content` object from the `kreya.grpc.onResponse` callback will automatically be parsed to the defined response type. Kreya even provides auto completion for members of `msg.content`.

## Functions[​](#functions "Direct link to Functions")

### onCallCompleted()[​](#oncallcompleted "Direct link to onCallCompleted()")

```
function onCallCompleted(callback: (arg: GrpcScriptCallCompletedContext) => void | Promise<void>): void;
```

Hook which is called when a gRPC call completes.

#### Parameters[​](#parameters "Direct link to Parameters")

| Parameter  | Type                                                                                                        | Description                 |
| ---------- | ----------------------------------------------------------------------------------------------------------- | --------------------------- |
| `callback` | (`arg`: [`GrpcScriptCallCompletedContext`](#grpcscriptcallcompletedcontext)) => `void` \| `Promise`<`void`> | The callback to be invoked. |

#### Returns[​](#returns "Direct link to Returns")

`void`

***

### onResponse()[​](#onresponse "Direct link to onResponse()")

```
function onResponse(callback: (arg: GrpcScriptResponseMessageContext) => void | Promise<void>): void;
```

Hook which is called when a gRPC response message arrives.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter  | Type                                                                                                            | Description                 |
| ---------- | --------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `callback` | (`arg`: [`GrpcScriptResponseMessageContext`](#grpcscriptresponsemessagecontext)) => `void` \| `Promise`<`void`> | The callback to be invoked. |

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### GrpcScriptCallCompletedContext[​](#grpcscriptcallcompletedcontext "Direct link to GrpcScriptCallCompletedContext")

```
type GrpcScriptCallCompletedContext = {
  durationMillis: number;
  headers: Record<string, string>;
  responseCount: number;
  status: GrpcScriptStatus;
  trailers: Record<string, string>;
};
```

Callback context of gRPC completed call callback.

#### Properties[​](#properties "Direct link to Properties")

##### durationMillis[​](#durationmillis "Direct link to durationMillis")

```
readonly durationMillis: number;
```

Duration of the call in milliseconds.

##### headers[​](#headers "Direct link to headers")

```
readonly headers: Record<string, string>;
```

The received gRPC headers.

##### responseCount[​](#responsecount "Direct link to responseCount")

```
readonly responseCount: number;
```

The number of responses.

##### status[​](#status "Direct link to status")

```
readonly status: GrpcScriptStatus;
```

The status of the call.

##### trailers[​](#trailers "Direct link to trailers")

```
readonly trailers: Record<string, string>;
```

The received gRPC trailers.

***

### GrpcScriptResponseMessageContext[​](#grpcscriptresponsemessagecontext "Direct link to GrpcScriptResponseMessageContext")

```
type GrpcScriptResponseMessageContext = {
  content: any;
  index: number;
  size: number;
};
```

Callback context of the callback when a gRPC response message has arrived.

#### Properties[​](#properties-1 "Direct link to Properties")

##### content[​](#content "Direct link to content")

```
readonly content: any;
```

The content of the message.

##### index[​](#index "Direct link to index")

```
readonly index: number;
```

The index of the response.

##### size[​](#size "Direct link to size")

```
readonly size: number;
```

The size of the message in bytes.

***

### GrpcScriptStatus[​](#grpcscriptstatus "Direct link to GrpcScriptStatus")

```
type GrpcScriptStatus = {
  code: number;
  detail?: string;
};
```

Status of a gRPC call.

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
