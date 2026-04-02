Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsUpdateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsUpdateArguments

# Interface: SlackListsUpdateArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:533](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L533)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### description_blocks? {#description_blocks}

```text
optional description_blocks: RichTextBlock[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:547](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L547)

#### Description {#description}

A rich text description of the List.

* * *

### id {#id}

```text
id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:537](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L537)

#### Description {#description-1}

Encoded ID of the List.

* * *

### name? {#name}

```text
optional name: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:542](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L542)

#### Description {#description-2}

Name of the List.

* * *

### todo_mode? {#todo_mode}

```text
optional todo_mode: boolean;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:552](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L552)

#### Description {#description-3}

Boolean indicating whether the List should be used to track todo tasks.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text
