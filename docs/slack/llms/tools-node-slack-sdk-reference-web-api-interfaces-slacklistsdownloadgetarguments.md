Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsDownloadGetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsDownloadGetArguments

# Interface: SlackListsDownloadGetArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:404](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L404)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### job_id {#job_id}

```text
job_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:413](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L413)

#### Description {#description}

The ID of the recently started job to export the List.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:408](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L408)

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
