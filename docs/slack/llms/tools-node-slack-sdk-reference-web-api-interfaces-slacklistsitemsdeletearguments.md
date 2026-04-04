Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsItemsDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsDeleteArguments

# Interface: SlackListsItemsDeleteArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:453](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L453)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### id {#id}

```text
id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:462](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L462)

#### Description {#description}

ID of item to delete.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:457](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L457)

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
