Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/GenericMessageEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / GenericMessageEvent

# Interface: GenericMessageEvent

Defined in: packages/types/dist/events/message.d.ts:7

## Properties {#properties}

### assistant_thread? {#assistant_thread}

```text
optional assistant_thread: Record<string, unknown>;
```text

Defined in: packages/types/dist/events/message.d.ts:36

* * *

### attachments? {#attachments}

```text
optional attachments: MessageAttachment[];
```text

Defined in: packages/types/dist/events/message.d.ts:20

* * *

### blocks? {#blocks}

```text
optional blocks: (Block | KnownBlock)[];
```text

Defined in: packages/types/dist/events/message.d.ts:21

* * *

### bot_id? {#bot_id}

```text
optional bot_id: string;
```text

Defined in: packages/types/dist/events/message.d.ts:14

* * *

### bot_profile? {#bot_profile}

```text
optional bot_profile: BotProfile;
```text

Defined in: packages/types/dist/events/message.d.ts:15

* * *

### channel {#channel}

```text
channel: string;
```text

Defined in: packages/types/dist/events/message.d.ts:12

* * *

### channel_type {#channel_type}

```text
channel_type: ChannelTypes;
```text

Defined in: packages/types/dist/events/message.d.ts:19

* * *

### client_msg_id? {#client_msg_id}

```text
optional client_msg_id: string;
```text

Defined in: packages/types/dist/events/message.d.ts:27

* * *

### edited? {#edited}

```text
optional edited: object;
```text

Defined in: packages/types/dist/events/message.d.ts:23

#### ts {#ts}

```text
ts: string;
```text

#### user {#user}

```text
user: string;
```text

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:10

* * *

### files? {#files}

```text
optional files: File[];
```text

Defined in: packages/types/dist/events/message.d.ts:22

* * *

### is_starred? {#is_starred}

```text
optional is_starred: boolean;
```text

Defined in: packages/types/dist/events/message.d.ts:29

* * *

### parent_user_id? {#parent_user_id}

```text
optional parent_user_id: string;
```text

Defined in: packages/types/dist/events/message.d.ts:28

* * *

### pinned_to? {#pinned_to}

```text
optional pinned_to: string[];
```text

Defined in: packages/types/dist/events/message.d.ts:30

* * *

### reactions? {#reactions}

```text
optional reactions: object[];
```text

Defined in: packages/types/dist/events/message.d.ts:31

#### count {#count}

```text
count: number;
```text

#### name {#name}

```text
name: string;
```text

#### users {#users}

```text
users: string[];
```text

* * *

### subtype {#subtype}

```text
subtype: undefined;
```text

Defined in: packages/types/dist/events/message.d.ts:9

* * *

### team? {#team}

```text
optional team: string;
```text

Defined in: packages/types/dist/events/message.d.ts:11

* * *

### text? {#text}

```text
optional text: string;
```text

Defined in: packages/types/dist/events/message.d.ts:16

* * *

### thread_ts? {#thread_ts}

```text
optional thread_ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:18

* * *

### ts {#ts-1}

```text
ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:17

* * *

### type {#type}

```text
type: "message";
```text

Defined in: packages/types/dist/events/message.d.ts:8

* * *

### user {#user-1}

```text
user: string;
```text

Defined in: packages/types/dist/events/message.d.ts:13
