Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsItemsUpdateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsUpdateArguments

# Interface: SlackListsItemsUpdateArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:520](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L520)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### cells {#cells}

```text
cells: SlackListsItemCellUpdate[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:529](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L529)

#### Description {#description}

Cells to update. Each cell includes the row\_id, column\_id, and field value.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:524](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L524)

#### Description {#description-1}

Encoded ID of the List.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text
