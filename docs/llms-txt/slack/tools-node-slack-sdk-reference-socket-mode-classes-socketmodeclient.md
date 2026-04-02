Source: https://docs.slack.dev/tools/node-slack-sdk/reference/socket-mode/classes/SocketModeClient

[@slack/socket-mode](/tools/node-slack-sdk/reference/socket-mode/) / SocketModeClient

# Class: SocketModeClient

Defined in: [packages/socket-mode/src/SocketModeClient.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/socket-mode/src/SocketModeClient.ts#L36)

A Socket Mode Client allows programs to communicate with the [Slack Platform's Events API](https://https://docs.slack.dev/apis/events-api) over WebSocket connections. This object uses the EventEmitter pattern to dispatch incoming events and has a built in send method to acknowledge incoming events over the WebSocket connection.

## Extends {#extends}

* `EventEmitter`

## Constructors {#constructors}

### Constructor {#constructor}

```text
new SocketModeClient(__namedParameters?): SocketModeClient;
```

Defined in: [packages/socket-mode/src/SocketModeClient.ts:96](https://github.com/slackapi/node-slack-sdk/blob/main/packages/socket-mode/src/SocketModeClient.ts#L96)

#### Parameters {#parameters}

##### __namedParameters? {#__namedparameters}

[`SocketModeOptions`](/tools/node-slack-sdk/reference/socket-mode/interfaces/SocketModeOptions) = `...`

#### Returns {#returns}

`SocketModeClient`

#### Overrides {#overrides}

```text
EventEmitter.constructor
```

## Properties {#properties}

### websocket? {#websocket}

```text
optional websocket: SlackWebSocket;
```

Defined in: [packages/socket-mode/src/SocketModeClient.ts:66](https://github.com/slackapi/node-slack-sdk/blob/main/packages/socket-mode/src/SocketModeClient.ts#L66)

The underlying WebSocket client instance

* * *

### prefixed {#prefixed}

```text
static prefixed: string | boolean;
```

Defined in: node\_modules/eventemitter3/index.d.ts:9

#### Inherited from {#inherited-from}

```text
EventEmitter.prefixed
```

## Methods {#methods}

### addListener() {#addlistener}

```text
addListener<T>(   event,    fn,    context?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:45

#### Type Parameters {#type-parameters}

##### T {#t}

`T` _extends_ `string` | `symbol`

#### Parameters {#parameters-1}

##### event {#event}

`T`

##### fn {#fn}

(...`args`) => `void`

##### context? {#context}

`any`

#### Returns {#returns-1}

`this`

#### Inherited from {#inherited-from-1}

```text
EventEmitter.addListener
```

* * *

### disconnect() {#disconnect}

```text
disconnect(): Promise<void>;
```

Defined in: [packages/socket-mode/src/SocketModeClient.ts:205](https://github.com/slackapi/node-slack-sdk/blob/main/packages/socket-mode/src/SocketModeClient.ts#L205)

End a Socket Mode session. After this method is called no messages will be sent or received unless you call start() again later.

#### Returns {#returns-2}

`Promise`<`void`\>

* * *

### emit() {#emit}

```text
emit<T>(event, ...args): boolean;
```

Defined in: node\_modules/eventemitter3/index.d.ts:32

Calls each of the listeners registered for a given event.

#### Type Parameters {#type-parameters-1}

##### T {#t-1}

`T` _extends_ `string` | `symbol`

#### Parameters {#parameters-2}

##### event {#event-1}

`T`

##### args {#args}

...`any`\[\]

#### Returns {#returns-3}

`boolean`

#### Inherited from {#inherited-from-2}

```text
EventEmitter.emit
```

* * *

### eventNames() {#eventnames}

```text
eventNames(): (string | symbol)[];
```

Defined in: node\_modules/eventemitter3/index.d.ts:15

Return an array listing the events for which the emitter has registered listeners.

#### Returns {#returns-4}

(`string` | `symbol`)\[\]

#### Inherited from {#inherited-from-3}

```text
EventEmitter.eventNames
```

* * *

### listenerCount() {#listenercount}

```text
listenerCount(event): number;
```

Defined in: node\_modules/eventemitter3/index.d.ts:27

Return the number of listeners listening to a given event.

#### Parameters {#parameters-3}

##### event {#event-2}

`string` | `symbol`

#### Returns {#returns-5}

`number`

#### Inherited from {#inherited-from-4}

```text
EventEmitter.listenerCount
```

* * *

### listeners() {#listeners}

```text
listeners<T>(event): (...args) => void[];
```

Defined in: node\_modules/eventemitter3/index.d.ts:20

Return the listeners registered for a given event.

#### Type Parameters {#type-parameters-2}

##### T {#t-2}

`T` _extends_ `string` | `symbol`

#### Parameters {#parameters-4}

##### event {#event-3}

`T`

#### Returns {#returns-6}

(...`args`) => `void`\[\]

#### Inherited from {#inherited-from-5}

```text
EventEmitter.listeners
```

* * *

### off() {#off}

```text
off<T>(   event,    fn?,    context?,    once?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:69

#### Type Parameters {#type-parameters-3}

##### T {#t-3}

`T` _extends_ `string` | `symbol`

#### Parameters {#parameters-5}

##### event {#event-4}

`T`

##### fn? {#fn-1}

(...`args`) => `void`

##### context? {#context-1}

`any`

##### once? {#once}

`boolean`

#### Returns {#returns-7}

`this`

#### Inherited from {#inherited-from-6}

```text
EventEmitter.off
```

* * *

### on() {#on}

```text
on<T>(   event,    fn,    context?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:40

Add a listener for a given event.

#### Type Parameters {#type-parameters-4}

##### T {#t-4}

`T` _extends_ `string` | `symbol`

#### Parameters {#parameters-6}

##### event {#event-5}

`T`

##### fn {#fn-2}

(...`args`) => `void`

##### context? {#context-2}

`any`

#### Returns {#returns-8}

`this`

#### Inherited from {#inherited-from-7}

```text
EventEmitter.on
```

* * *

### once() {#once-1}

```text
once<T>(   event,    fn,    context?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:54

Add a one-time listener for a given event.

#### Type Parameters {#type-parameters-5}

##### T {#t-5}

`T` _extends_ `string` | `symbol`

#### Parameters {#parameters-7}

##### event {#event-6}

`T`

##### fn {#fn-3}

(...`args`) => `void`

##### context? {#context-3}

`any`

#### Returns {#returns-9}

`this`

#### Inherited from {#inherited-from-8}

```text
EventEmitter.once
```

* * *

### removeAllListeners() {#removealllisteners}

```text
removeAllListeners(event?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:79

Remove all listeners, or those of the specified event.

#### Parameters {#parameters-8}

##### event? {#event-7}

`string` | `symbol`

#### Returns {#returns-10}

`this`

#### Inherited from {#inherited-from-9}

```text
EventEmitter.removeAllListeners
```

* * *

### removeListener() {#removelistener}

```text
removeListener<T>(   event,    fn?,    context?,    once?): this;
```

Defined in: node\_modules/eventemitter3/index.d.ts:63

Remove the listeners of a given event.

#### Type Parameters {#type-parameters-6}

##### T {#t-6}

`T` _extends_ `string` | `symbol`

#### Parameters {#parameters-9}

##### event {#event-8}

`T`

##### fn? {#fn-4}

(...`args`) => `void`

##### context? {#context-4}

`any`

##### once? {#once-2}

`boolean`

#### Returns {#returns-11}

`this`

#### Inherited from {#inherited-from-10}

```text
EventEmitter.removeListener
```

* * *

### start() {#start}

```text
start(): Promise<AppsConnectionsOpenResponse>;
```

Defined in: [packages/socket-mode/src/SocketModeClient.ts:162](https://github.com/slackapi/node-slack-sdk/blob/main/packages/socket-mode/src/SocketModeClient.ts#L162)

Start a Socket Mode session app. This method must be called before any messages can be sent or received, or to disconnect the client via the `disconnect` method.

#### Returns {#returns-12}

`Promise`<`AppsConnectionsOpenResponse`\>
