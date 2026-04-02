Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsDownloadStartArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsDownloadStartArguments

# Interface: SlackListsDownloadStartArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:417](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L417)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### include_archived? {#include_archived}

```text
optional include_archived: boolean;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:426](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L426)

#### Description {#description}

Boolean indicating whether to include archived items.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:421](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L421)

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
