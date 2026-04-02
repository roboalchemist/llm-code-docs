Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsItemsDeleteMultipleArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsDeleteMultipleArguments

# Interface: SlackListsItemsDeleteMultipleArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:466](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L466)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### ids {#ids}

```text
ids: string[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:475](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L475)

#### Description {#description}

IDs of the items to delete.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:470](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L470)

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
