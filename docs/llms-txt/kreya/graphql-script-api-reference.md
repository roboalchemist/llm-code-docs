# Source: https://kreya.app/docs/scripting-and-tests/operation-scripts/graphql-script-api-reference.md

# GraphQL script API reference

In operation scripts for GraphQL operations, despite the [operation script API](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md), the definitions below are available through the `kreya.graphql` namespace. For example:

```
import { expect } from 'chai';

kreya.graphql.OnQueryCompleted(call => {
  kreya.trace('The GraphQL query completed.');

  kreya.test('Status code', () => expect(call.status.code).to.equal(200));
  kreya.test('status is success', () => expect(call.status.isSuccess).to.be.true);

  // You can check for GraphQL errors
  if (call.response.content.errors) {
    kreya.trace('GraphQL errors occurred');
  }

  kreya.test('First user name', () => expect(call.response.content.data.users[0].name).to.eq('John'));
});
```

info

Accessing `call.response.content` will throw an exception if the response size is greater than 10 MiB.

Accessing `call.response.content` will throw if the response content is not valid JSON.

## Functions[​](#functions "Direct link to Functions")

### onMutationCompleted()[​](#onmutationcompleted "Direct link to onMutationCompleted()")

```
function onMutationCompleted(callback: (arg: GraphQlScriptQueryCompletedContext) => void | Promise<void>): void;
```

Hook which is called when a GraphQL mutation completes.

#### Parameters[​](#parameters "Direct link to Parameters")

| Parameter  | Type                                                                                                                | Description                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `callback` | (`arg`: [`GraphQlScriptQueryCompletedContext`](#graphqlscriptquerycompletedcontext)) => `void` \| `Promise`<`void`> | The callback to be invoked. |

#### Returns[​](#returns "Direct link to Returns")

`void`

***

### onQueryCompleted()[​](#onquerycompleted "Direct link to onQueryCompleted()")

```
function onQueryCompleted(callback: (arg: GraphQlScriptQueryCompletedContext) => void | Promise<void>): void;
```

Hook which is called when a GraphQL query completes.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter  | Type                                                                                                                | Description                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `callback` | (`arg`: [`GraphQlScriptQueryCompletedContext`](#graphqlscriptquerycompletedcontext)) => `void` \| `Promise`<`void`> | The callback to be invoked. |

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

***

### onSubscriptionCompleted()[​](#onsubscriptioncompleted "Direct link to onSubscriptionCompleted()")

```
function onSubscriptionCompleted(callback: (arg: GraphQlScriptSubscriptionCompletedContext) => void | Promise<void>): void;
```

Hook which is called when a subscription is completed.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Parameter  | Type                                                                                                                              | Description |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `callback` | (`arg`: [`GraphQlScriptSubscriptionCompletedContext`](#graphqlscriptsubscriptioncompletedcontext)) => `void` \| `Promise`<`void`> |             |

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

***

### onSubscriptionEventReceived()[​](#onsubscriptioneventreceived "Direct link to onSubscriptionEventReceived()")

```
function onSubscriptionEventReceived(callback: (arg: GraphQlScriptSubscriptionEventContext) => void | Promise<void>): void;
```

Hook which is called when a subscription event is received.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Parameter  | Type                                                                                                                      | Description |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `callback` | (`arg`: [`GraphQlScriptSubscriptionEventContext`](#graphqlscriptsubscriptioneventcontext)) => `void` \| `Promise`<`void`> |             |

#### Returns[​](#returns-3 "Direct link to Returns")

`void`

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### GraphQlScriptQueryCompletedContext[​](#graphqlscriptquerycompletedcontext "Direct link to GraphQlScriptQueryCompletedContext")

```
type GraphQlScriptQueryCompletedContext = {
  durationMillis: number;
  headers: Record<string, string>;
  response: GraphQlScriptQueryResponse;
  status: HttpScriptStatus;
  trailers: Record<string, string>;
};
```

Callback context of GraphQL completed call callback.

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

The received headers.

##### response[​](#response "Direct link to response")

```
readonly response: GraphQlScriptQueryResponse;
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

The received trailers.

***

### GraphQlScriptQueryResponse[​](#graphqlscriptqueryresponse "Direct link to GraphQlScriptQueryResponse")

```
type GraphQlScriptQueryResponse = {
  content: any;
  rawContentBytes: Uint8Array;
  rawContentText: string;
  size: number;
};
```

Response content of a GraphQL query.

#### Properties[​](#properties-1 "Direct link to Properties")

##### content[​](#content "Direct link to content")

```
readonly content: any;
```

The parsed and deserialized content.

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

### GraphQlScriptSubscriptionCompletedContext[​](#graphqlscriptsubscriptioncompletedcontext "Direct link to GraphQlScriptSubscriptionCompletedContext")

```
type GraphQlScriptSubscriptionCompletedContext = {
};
```

Callback context of GraphQL subscription completed callback.

***

### GraphQlScriptSubscriptionEventContext[​](#graphqlscriptsubscriptioneventcontext "Direct link to GraphQlScriptSubscriptionEventContext")

```
type GraphQlScriptSubscriptionEventContext = {
  durationMillis: number;
  response: GraphQlScriptQueryResponse;
};
```

Callback context of GraphQL subscription event callback.

#### Properties[​](#properties-2 "Direct link to Properties")

##### durationMillis[​](#durationmillis-1 "Direct link to durationMillis")

```
readonly durationMillis: number;
```

Duration of the call in milliseconds.

##### response[​](#response-1 "Direct link to response")

```
readonly response: GraphQlScriptQueryResponse;
```

The response.

***

### HttpScriptStatus[​](#httpscriptstatus "Direct link to HttpScriptStatus")

```
type HttpScriptStatus = {
  code: number;
  isSuccess: boolean;
  reasonPhrase?: string;
};
```

#### Properties[​](#properties-3 "Direct link to Properties")

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
