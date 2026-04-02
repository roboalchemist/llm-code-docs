Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsCreateArguments

# Interface: SlackListsCreateArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:370](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L370)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### copy_from_list_id? {#copy_from_list_id}

```text
optional copy_from_list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:390](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L390)

#### Description {#description}

ID of the List to copy.

* * *

### description_blocks? {#description_blocks}

```text
optional description_blocks: RichTextBlock[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:379](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L379)

#### Description {#description-1}

A rich text description of the List.

* * *

### include_copied_list_records? {#include_copied_list_records}

```text
optional include_copied_list_records: boolean;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:395](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L395)

#### Description {#description-2}

Boolean indicating whether to include records when a List is copied.

* * *

### name {#name}

```text
name: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:374](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L374)

#### Description {#description-3}

Name of the List.

* * *

### schema? {#schema}

```text
optional schema: SlackListsSchemaColumn[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:385](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L385)

#### Description {#description-4}

Column definition for the List.

#### See {#see}

[https://docs.slack.dev/reference/methods/slackLists.create#schema-definition](https://docs.slack.dev/reference/methods/slackLists.create#schema-definition)

* * *

### todo_mode? {#todo_mode}

```text
optional todo_mode: boolean;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:400](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L400)

#### Description {#description-5}

Boolean indicating whether the List should be used to track todo tasks.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-6}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text
