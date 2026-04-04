Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsItemsInfoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsInfoArguments

# Interface: SlackListsItemsInfoArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:479](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L479)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### id {#id}

```text
id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:488](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L488)

#### Description {#description}

ID of item to delete.

* * *

### include_is_subscribed? {#include_is_subscribed}

```text
optional include_is_subscribed: boolean;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:493](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L493)

#### Description {#description-1}

Set to true to include is\_subscribed data for the returned List row.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:483](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L483)

#### Description {#description-2}

Encoded ID of the List.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text
