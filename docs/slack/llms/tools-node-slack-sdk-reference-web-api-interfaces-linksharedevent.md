Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/LinkSharedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / LinkSharedEvent

# Interface: LinkSharedEvent

Defined in: packages/types/dist/events/link-shared.d.ts:1

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:3

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:14

* * *

### is_bot_user_member {#is_bot_user_member}

```text
is_bot_user_member: boolean;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:4

* * *

### links {#links}

```text
links: object[];
```text

Defined in: packages/types/dist/events/link-shared.d.ts:8

#### domain {#domain}

```text
domain: string;
```text

#### url {#url}

```text
url: string;
```text

* * *

### message_ts {#message_ts}

```text
message_ts: string;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:6

* * *

### source? {#source}

```text
optional source: string;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:13

* * *

### thread_ts? {#thread_ts}

```text
optional thread_ts: string;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:7

* * *

### type {#type}

```text
type: "link_shared";
```text

Defined in: packages/types/dist/events/link-shared.d.ts:2

* * *

### unfurl_id? {#unfurl_id}

```text
optional unfurl_id: string;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:12

* * *

### user {#user}

```text
user: string;
```text

Defined in: packages/types/dist/events/link-shared.d.ts:5
