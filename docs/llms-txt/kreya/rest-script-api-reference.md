# Source: https://kreya.app/docs/scripting-and-tests/operation-scripts/rest-script-api-reference.md

# REST script API reference

In operation scripts for REST operations, despite the [operation script API](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md), the definitions below are available through the `kreya.rest` namespace. For example:

```
import { expect } from 'chai';

kreya.rest.onCallCompleted(call => {
  kreya.trace('The REST call completed.');

  kreya.test('Status code', () => expect(call.status.code).to.equal(200));
  kreya.test('status is success', () => expect(call.status.isSuccess).to.be.true);

  kreya.test('Content type', () => expect(call.response.contentType).to.eq('application/json'));

  const curlyBraceCharCode = '{'.charCodeAt(0);
  kreya.test('Byte content first entry should be a curly brace', () => expect(call.response.rawContentBytes[0]).to.eq(curlyBraceCharCode));
  kreya.test('Text content first char should be a curly brace', () => expect(call.response.rawContentText[0]).to.eq('{'));

  kreya.test('Deserialized number should equal', () => expect(call.response.content.myInt).to.eq(26));
});
```

info

Accessing `call.response.content`, `call.response.rawContentText` or `rcall.response.awContentBytes` will throw an exception if the response size is greater than 10 MiB.

Accessing `call.response.content` will throw if the response content is not valid JSON or YAML.

## Functions[​](#functions "Direct link to Functions")

### onCallCompleted()[​](#oncallcompleted "Direct link to onCallCompleted()")

```
function onCallCompleted(callback: (arg: RestScriptCallCompletedContext) => void | Promise<void>): void;
```

Hook which is called when a REST call completes.

#### Parameters[​](#parameters "Direct link to Parameters")

| Parameter  | Type                                                                                                        | Description                 |
| ---------- | ----------------------------------------------------------------------------------------------------------- | --------------------------- |
| `callback` | (`arg`: [`RestScriptCallCompletedContext`](#restscriptcallcompletedcontext)) => `void` \| `Promise`<`void`> | The callback to be invoked. |

#### Returns[​](#returns "Direct link to Returns")

`void`

***

### onStreamEventReceived()[​](#onstreameventreceived "Direct link to onStreamEventReceived()")

```
function onStreamEventReceived(callback: (arg: RestScriptStreamEventReceivedContext) => void | Promise<void>): void;
```

Hook which is called when a streamed event is received.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter  | Type                                                                                                                    | Description |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| `callback` | (`arg`: [`RestScriptStreamEventReceivedContext`](#restscriptstreameventreceivedcontext)) => `void` \| `Promise`<`void`> |             |

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### HttpScriptStatus[​](#httpscriptstatus "Direct link to HttpScriptStatus")

```
type HttpScriptStatus = {
  code: number;
  isSuccess: boolean;
  reasonPhrase?: string;
};
```

#### Properties[​](#properties "Direct link to Properties")

##### code[​](#code "Direct link to code")

```
readonly code: number;
```

##### isSuccess[​](#issuccess "Direct link to isSuccess")

```
readonly isSuccess: boolean;
```

##### reasonPhrase?[​](#reasonphrase "Direct link to reasonPhrase?")

```
readonly optional reasonPhrase: string;
```

***

### RestScriptCallCompletedContext[​](#restscriptcallcompletedcontext "Direct link to RestScriptCallCompletedContext")

```
type RestScriptCallCompletedContext = {
  durationMillis: number;
  headers: Record<string, string>;
  response: RestScriptResponse;
  status: HttpScriptStatus;
  trailers: Record<string, string>;
};
```

Callback context of REST completed call callback.

#### Properties[​](#properties-1 "Direct link to Properties")

##### durationMillis[​](#durationmillis "Direct link to durationMillis")

```
readonly durationMillis: number;
```

Duration of the call in milliseconds.

##### headers[​](#headers "Direct link to headers")

```
readonly headers: Record<string, string>;
```

The received REST headers.

##### response[​](#response "Direct link to response")

```
readonly response: RestScriptResponse;
```

The response.

##### status[​](#status "Direct link to status")

```
readonly status: HttpScriptStatus;
```

The status of the call.

##### trailers[​](#trailers "Direct link to trailers")

```
readonly trailers: Record<string, string>;
```

The received REST trailers.

***

### RestScriptResponse[​](#restscriptresponse "Direct link to RestScriptResponse")

```
type RestScriptResponse = {
  content: any;
  contentType: string;
  rawContentBytes: Uint8Array;
  rawContentText: string;
  size: number;
};
```

Response of a REST call.

#### Properties[​](#properties-2 "Direct link to Properties")

##### content[​](#content "Direct link to content")

```
readonly content: any;
```

The parsed and deserialized content, if available. Only available for JSON and YAML content types.

##### contentType[​](#contenttype "Direct link to contentType")

```
readonly contentType: string;
```

The content type.

##### rawContentBytes[​](#rawcontentbytes "Direct link to rawContentBytes")

```
readonly rawContentBytes: Uint8Array;
```

##### rawContentText[​](#rawcontenttext "Direct link to rawContentText")

```
readonly rawContentText: string;
```

##### size[​](#size "Direct link to size")

```
readonly size: number;
```

***

### RestScriptStreamEventReceivedContext[​](#restscriptstreameventreceivedcontext "Direct link to RestScriptStreamEventReceivedContext")

```
type RestScriptStreamEventReceivedContext = {
  data?: string;
  event?: string;
  id?: string;
};
```

Callback context of server sent event received context.

#### Properties[​](#properties-3 "Direct link to Properties")

##### data?[​](#data "Direct link to data?")

```
readonly optional data: string;
```

The data of the event.

##### event?[​](#event "Direct link to event?")

```
readonly optional event: string;
```

The event of the event (if a server sent event and the event field is set).

##### id?[​](#id "Direct link to id?")

```
readonly optional id: string;
```

The id of the event (if a server sent event and the id field is set).
