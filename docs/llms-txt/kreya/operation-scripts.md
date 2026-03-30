# Source: https://kreya.app/docs/scripting-and-tests/operation-scripts.md

# Operation scripts [Pro / Enterprise](/pricing.md)

Operation scripts allow you to define JavaScript code that runs when an operation is invoked. Among other things, it allows you to create tests and view the results of them.

In contrast to other API clients, Kreya does not provide a way to control the execution flow in operation scripts (e.g. with `setNextRequest()` or similar methods). You can use [scripts](/docs/scripting-and-tests/invoker-scripts.md) to do this in Kreya.

Operation scripts can be defined in the Script tab of an operation. The script will run when the operation is sent. Note that the script editor supports autocompletion, simply press `Ctrl`+`Space` to bring it up.

Kreya offers a set of useful APIs. Checkout the [operation script API reference](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md) as well as the [general script API reference](/docs/scripting-and-tests/general.md). You can also [share code](/docs/scripting-and-tests/general.md#sharing-code) or [import external NPM modules](/docs/scripting-and-tests/general.md#importing-external-modules).

![Defining Kreya scripts](/assets/ideal-img/defining-scripts.aac6904.400.png)

As you can see in the screenshot, a global `kreya` object is provided. View all available properties and methods in the [API reference](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md).

## Hooks[​](#hooks "Direct link to Hooks")

Operation scripts use a hook-based execution model. Code written directly at the top level of the script runs *before* the operation is sent, while code inside hooks runs on a specific event.

### Running code before the operation is sent (pre-request script)[​](#running-code-before-the-operation-is-sent-pre-request-script "Direct link to Running code before the operation is sent (pre-request script)")

Any code placed at the top level of the script executes before the operation is sent. This is useful for setting up variables, reading data from files, or logging information:

```
// This runs before the request is sent
console.log('Preparing request...');
const startTime = Date.now();
```

### Running code after the response arrives (post-response script)[​](#running-code-after-the-response-arrives-post-response-script "Direct link to Running code after the response arrives (post-response script)")

To run code after the response arrives, register a callback using the appropriate hook for your protocol. The hook receives a context object with details about the response:

* REST
* gRPC
* GraphQL
* WebSocket

```
kreya.rest.onCallCompleted(ctx => {
  kreya.test('Status is 200', () => expect(ctx.status.code).to.equal(200));
});
```

```
kreya.grpc.onResponse(msg => {
  kreya.test('Response is valid', () => expect(msg.content.name).to.not.be.empty);
});
```

```
kreya.graphql.onQueryCompleted(ctx => {
  kreya.test('Has data', () => expect(ctx.response.content.data).to.not.be.null);
});
```

```
kreya.webSocket.onResponseMessage(msg => {
  kreya.test('Message received', () => expect(msg.content).to.not.be.empty);
});
```

### Available hooks per protocol[​](#available-hooks-per-protocol "Direct link to Available hooks per protocol")

Each protocol exposes its hooks on a dedicated namespace of the `kreya` object. For example, REST hooks are available on `kreya.rest`, gRPC hooks on `kreya.grpc`, and so on.

For the full callback context types and detailed signatures, see the protocol-specific API references:

## [📄️<!-- --> <!-- -->Operation script API reference](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md)

[The API reference for Kreya operation scripts.](/docs/scripting-and-tests/operation-scripts/operation-script-api-reference.md)

## [📄️<!-- --> <!-- -->gRPC script API reference](/docs/scripting-and-tests/operation-scripts/grpc-script-api-reference.md)

[The gRPC API reference for Kreya operation scripts.](/docs/scripting-and-tests/operation-scripts/grpc-script-api-reference.md)

## [📄️<!-- --> <!-- -->GraphQL script API reference](/docs/scripting-and-tests/operation-scripts/graphql-script-api-reference.md)

[The GraphQL API reference for Kreya operation scripts.](/docs/scripting-and-tests/operation-scripts/graphql-script-api-reference.md)

## [📄️<!-- --> <!-- -->REST script API reference](/docs/scripting-and-tests/operation-scripts/rest-script-api-reference.md)

[The REST API reference for Kreya operation scripts.](/docs/scripting-and-tests/operation-scripts/rest-script-api-reference.md)

## [📄️<!-- --> <!-- -->WebSocket script API reference](/docs/scripting-and-tests/operation-scripts/websocket-script-api-reference.md)

[The WebSocket API reference for Kreya operation scripts.](/docs/scripting-and-tests/operation-scripts/websocket-script-api-reference.md)
