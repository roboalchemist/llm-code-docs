Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsItemsListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsListArguments

# Interface: SlackListsItemsListArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:497](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L497)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### archived? {#archived}

```text
optional archived: boolean;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:516](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L516)

#### Description {#description}

Boolean indicating whether archived items or normal items should be returned.

* * *

### cursor? {#cursor}

```text
optional cursor: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:511](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L511)

#### Description {#description-1}

Next cursor for pagination.

* * *

### limit? {#limit}

```text
optional limit: number;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:506](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L506)

#### Description {#description-2}

The maximum number of records to return.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:501](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L501)

#### Description {#description-3}

Encoded ID of the List.

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
