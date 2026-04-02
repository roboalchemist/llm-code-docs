Source: https://docs.slack.dev/tools/node-slack-sdk/reference/rtm-api/classes/RTMClient

[@slack/rtm-api](/tools/node-slack-sdk/reference/rtm-api/) / RTMClient

# Class: RTMClient

Defined in: [packages/rtm-api/src/RTMClient.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L63)

An RTMClient allows programs to communicate with the [Platform's RTM API](https://docs.slack.dev/legacy/legacy-rtm-api%7CSlack). This object uses the EventEmitter pattern to dispatch incoming events and has several methods for sending outgoing messages.

## Extends {#extends}

* `EventEmitter`

## Constructors {#constructors}

### Constructor {#constructor}

```text
new RTMClient(token, __namedParameters?): RTMClient;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:367](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L367)

#### Parameters {#parameters}

##### token {#token}

`string`

##### __namedParameters? {#__namedparameters}

[`RTMClientOptions`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMClientOptions) = `{}`

#### Returns {#returns}

`RTMClient`

#### Overrides {#overrides}

```text
EventEmitter.constructor
```

## Properties {#properties}

### activeTeamId? {#activeteamid}

```text
optional activeTeamId: string;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:83](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L83)

The team ID for the workspace the client is connected to.

* * *

### activeUserId? {#activeuserid}

```text
optional activeUserId: string;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:78](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L78)

The user ID for the connected client.

* * *

### authenticated {#authenticated}

```text
authenticated: boolean = false;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:73](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L73)

Whether or not the client has authenticated to the RTM API. This occurs when the connect method completes, and a WebSocket URL is available for the client's connection.

* * *

### connected {#connected}

```text
connected: boolean = false;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L67)

Whether or not the client is currently connected to the RTM API

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

### addOutgoingEvent() {#addoutgoingevent}

#### Call Signature {#call-signature}

```text
addOutgoingEvent(   awaitReply,    type, body?): Promise<RTMCallResult>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:525](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L525)

Generic method for sending an outgoing message of an arbitrary type. This method guards the higher-level methods from concern of which state the client is in, because it places all messages into a queue. The tasks on the queue will buffer until the client is in a state where they can be sent.

If the awaitReply parameter is set to true, then the returned Promise is resolved with the platform's acknowledgement response. Not all message types will result in an acknowledgement response, so use this carefully. This promise may be rejected with an error containing code=RTMNoReplyReceivedError if the client disconnects or reconnects before receiving the acknowledgement response.

If the awaitReply parameter is set to false, then the returned Promise is resolved as soon as the message is sent from the websocket.

##### Parameters {#parameters-2}

###### awaitReply {#awaitreply}

`true`

whether to wait for an acknowledgement response from the platform before resolving the returned Promise.

###### type {#type}

`string`

the message type

###### body? {#body}

`Record`<`string`, `unknown`\>

the message body

##### Returns {#returns-2}

`Promise`<[`RTMCallResult`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMCallResult)\>

#### Call Signature {#call-signature-1}

```text
addOutgoingEvent(   awaitReply,    type, body?): Promise<undefined>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:526](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L526)

Generic method for sending an outgoing message of an arbitrary type. This method guards the higher-level methods from concern of which state the client is in, because it places all messages into a queue. The tasks on the queue will buffer until the client is in a state where they can be sent.

If the awaitReply parameter is set to true, then the returned Promise is resolved with the platform's acknowledgement response. Not all message types will result in an acknowledgement response, so use this carefully. This promise may be rejected with an error containing code=RTMNoReplyReceivedError if the client disconnects or reconnects before receiving the acknowledgement response.

If the awaitReply parameter is set to false, then the returned Promise is resolved as soon as the message is sent from the websocket.

##### Parameters {#parameters-3}

###### awaitReply {#awaitreply-1}

`false`

whether to wait for an acknowledgement response from the platform before resolving the returned Promise.

###### type {#type-1}

`string`

the message type

###### body? {#body-1}

`Record`<`string`, `unknown`\>

the message body

##### Returns {#returns-3}

`Promise`<`undefined`\>

* * *

### disconnect() {#disconnect}

```text
disconnect(): Promise<void>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:464](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L464)

End an RTM session. After this method is called no messages will be sent or received unless you call start() again later.

#### Returns {#returns-4}

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

#### Parameters {#parameters-4}

##### event {#event-1}

`T`

##### args {#args}

...`any`\[\]

#### Returns {#returns-5}

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

#### Returns {#returns-6}

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

#### Parameters {#parameters-5}

##### event {#event-2}

`string` | `symbol`

#### Returns {#returns-7}

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

#### Parameters {#parameters-6}

##### event {#event-3}

`T`

#### Returns {#returns-8}

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

#### Parameters {#parameters-7}

##### event {#event-4}

`T`

##### fn? {#fn-1}

(...`args`) => `void`

##### context? {#context-1}

`any`

##### once? {#once}

`boolean`

#### Returns {#returns-9}

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

#### Parameters {#parameters-8}

##### event {#event-5}

`T`

##### fn {#fn-2}

(...`args`) => `void`

##### context? {#context-2}

`any`

#### Returns {#returns-10}

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

#### Parameters {#parameters-9}

##### event {#event-6}

`T`

##### fn {#fn-3}

(...`args`) => `void`

##### context? {#context-3}

`any`

#### Returns {#returns-11}

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

#### Parameters {#parameters-10}

##### event? {#event-7}

`string` | `symbol`

#### Returns {#returns-12}

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

#### Parameters {#parameters-11}

##### event {#event-8}

`T`

##### fn? {#fn-4}

(...`args`) => `void`

##### context? {#context-4}

`any`

##### once? {#once-2}

`boolean`

#### Returns {#returns-13}

`this`

#### Inherited from {#inherited-from-10}

```text
EventEmitter.removeListener
```

* * *

### send() {#send}

```text
send(type, body?): Promise<number>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:578](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L578)

Generic method for sending an outgoing message of an arbitrary type. The main difference between this method and addOutgoingEvent() is that this method does not use a queue so it can only be used while the client is ready to send messages (in the 'ready' substate of the 'connected' state). It returns a Promise for the message ID of the sent message. This is an internal ID and generally shouldn't be used as an identifier for messages (for that, there is `ts` on messages once the server acknowledges it).

#### Parameters {#parameters-12}

##### type {#type-2}

`string`

the message type

##### body? {#body-2}

the message body

#### Returns {#returns-14}

`Promise`<`number`\>

* * *

### sendMessage() {#sendmessage}

```text
sendMessage(text, conversationId): Promise<RTMCallResult>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:487](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L487)

Send a simple message to a public channel, private channel, DM, or MPDM.

#### Parameters {#parameters-13}

##### text {#text}

`string`

The message text.

##### conversationId {#conversationid}

`string`

A conversation ID for the destination of this message.

#### Returns {#returns-15}

`Promise`<[`RTMCallResult`](/tools/node-slack-sdk/reference/rtm-api/interfaces/RTMCallResult)\>

* * *

### sendTyping() {#sendtyping}

```text
sendTyping(conversationId): Promise<void>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:495](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L495)

Sends a typing indicator to indicate that the user with `activeUserId` is typing.

#### Parameters {#parameters-14}

##### conversationId {#conversationid-1}

`string`

The destination for where the typing indicator should be shown.

#### Returns {#returns-16}

`Promise`<`void`\>

* * *

### start() {#start}

```text
start(options?): Promise<WebAPICallResult>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:438](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L438)

Begin an RTM session using the provided options. This method must be called before any messages can be sent or received.

#### Parameters {#parameters-15}

##### options? {#options}

[`RTMStartOptions`](/tools/node-slack-sdk/reference/rtm-api/type-aliases/RTMStartOptions)

#### Returns {#returns-17}

`Promise`<`WebAPICallResult`\>

* * *

### subscribePresence() {#subscribepresence}

```text
subscribePresence(userIds): Promise<void>;
```

Defined in: [packages/rtm-api/src/RTMClient.ts:504](https://github.com/slackapi/node-slack-sdk/blob/main/packages/rtm-api/src/RTMClient.ts#L504)

Subscribes this client to presence changes for only the given `userIds`.

#### Parameters {#parameters-16}

##### userIds {#userids}

`string`\[\]

An array of user IDs whose presence you are interested in. This list will replace the list from any previous calls to this method.

#### Returns {#returns-18}

`Promise`<`void`\>
