Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsItemsCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsCreateArguments

# Interface: SlackListsItemsCreateArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:430](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L430)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### duplicated_item_id? {#duplicated_item_id}

```text
optional duplicated_item_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:439](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L439)

#### Description {#description}

ID of the record to make a copy of.

* * *

### initial_fields? {#initial_fields}

```text
optional initial_fields: SlackListsItemField[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:449](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L449)

#### Description {#description-1}

Initial item data.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:434](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L434)

#### Description {#description-2}

Encoded ID of the List.

* * *

### parent_item_id? {#parent_item_id}

```text
optional parent_item_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:444](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L444)

#### Description {#description-3}

ID of the parent record for this subtask.

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
