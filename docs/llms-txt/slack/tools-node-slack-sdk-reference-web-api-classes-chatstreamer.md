Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/classes/ChatStreamer

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatStreamer

# Class: ChatStreamer

Defined in: [packages/web-api/src/chat-stream.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/chat-stream.ts#L15)

## Constructors {#constructors}

### Constructor {#constructor}

```
new ChatStreamer(   client,    logger,    args,    options): ChatStreamer;
```

Defined in: [packages/web-api/src/chat-stream.ts:47](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/chat-stream.ts#L47)

Instantiate a new chat streamer.

#### Parameters {#parameters}

##### client {#client}

[`WebClient`](/tools/node-slack-sdk/reference/web-api/classes/WebClient)

##### logger {#logger}

[`Logger`](/tools/node-slack-sdk/reference/web-api/interfaces/Logger)

##### args {#args}

[`ChatStartStreamArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/ChatStartStreamArguments)

##### options {#options}

[`ChatStreamerOptions`](/tools/node-slack-sdk/reference/web-api/interfaces/ChatStreamerOptions)

#### Returns {#returns}

`ChatStreamer`

#### Description {#description}

The "constructor" method creates a unique ChatStreamer instance that keeps track of one chat stream.

#### Example {#example}

```
const client = new WebClient(process.env.SLACK_BOT_TOKEN);const logger = new ConsoleLogger();const args = {  channel: "C0123456789",  thread_ts: "1700000001.123456",  recipient_team_id: "T0123456789",  recipient_user_id: "U0123456789",};const streamer = new ChatStreamer(client, logger, args, { buffer_size: 512 });await streamer.append({  markdown_text: "**hello world!**",});await streamer.stop();
```

#### See {#see}

* [https://docs.slack.dev/reference/methods/chat.startStream](https://docs.slack.dev/reference/methods/chat.startStream)
* [https://docs.slack.dev/reference/methods/chat.appendStream](https://docs.slack.dev/reference/methods/chat.appendStream)
* [https://docs.slack.dev/reference/methods/chat.stopStream](https://docs.slack.dev/reference/methods/chat.stopStream)

## Methods {#methods}

### append() {#append}

```
append(args): Promise<  | ChatAppendStreamResponse  | ChatStartStreamResponse| null>;
```

Defined in: [packages/web-api/src/chat-stream.ts:77](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/chat-stream.ts#L77)

Append to the stream.

#### Parameters {#parameters-1}

##### args {#args-1}

`Omit`<[`ChatAppendStreamArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/ChatAppendStreamArguments), `"channel"` | `"ts"`\>

#### Returns {#returns-1}

`Promise`< | [`ChatAppendStreamResponse`](/tools/node-slack-sdk/reference/web-api/type-aliases/ChatAppendStreamResponse) | [`ChatStartStreamResponse`](/tools/node-slack-sdk/reference/web-api/type-aliases/ChatStartStreamResponse) | `null`\>

#### Description {#description-1}

The "append" method appends to the chat stream being used. This method can be called multiple times. After the stream is stopped this method cannot be called.

#### Example {#example-1}

```
const streamer = client.chatStream({  channel: "C0123456789",  thread_ts: "1700000001.123456",  recipient_team_id: "T0123456789",  recipient_user_id: "U0123456789",});await streamer.append({  markdown_text: "**hello wo",});await streamer.append({  markdown_text: "rld!**",});await streamer.stop();
```

#### See {#see-1}

[https://docs.slack.dev/reference/methods/chat.appendStream](https://docs.slack.dev/reference/methods/chat.appendStream)

* * *

### stop() {#stop}

```
stop(args?): Promise<ChatStopStreamResponse>;
```

Defined in: [packages/web-api/src/chat-stream.ts:123](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/chat-stream.ts#L123)

Stop the stream and finalize the message.

#### Parameters {#parameters-2}

##### args? {#args-2}

`Omit`<[`ChatStopStreamArguments`](/tools/node-slack-sdk/reference/web-api/type-aliases/ChatStopStreamArguments), `"channel"` | `"ts"`\>

#### Returns {#returns-2}

`Promise`<[`ChatStopStreamResponse`](/tools/node-slack-sdk/reference/web-api/type-aliases/ChatStopStreamResponse)\>

#### Description {#description-2}

The "stop" method stops the chat stream being used. This method can be called once to end the stream. Additional "blocks" and "metadata" can be provided.

#### Example {#example-2}

```
const streamer = client.chatStream({  channel: "C0123456789",  thread_ts: "1700000001.123456",  recipient_team_id: "T0123456789",  recipient_user_id: "U0123456789",});await streamer.append({  markdown_text: "**hello world!**",});await streamer.stop();
```

#### See {#see-2}

[https://docs.slack.dev/reference/methods/chat.stopStream](https://docs.slack.dev/reference/methods/chat.stopStream)
