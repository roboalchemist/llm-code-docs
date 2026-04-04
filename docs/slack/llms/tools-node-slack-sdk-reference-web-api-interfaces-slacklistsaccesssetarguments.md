Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsAccessSetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsAccessSetArguments

# Interface: SlackListsAccessSetArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:347](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L347)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### access_level {#access_level}

```text
access_level: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:356](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L356)

#### Description {#description}

Desired level of access.

* * *

### channel_ids? {#channel_ids}

```text
optional channel_ids: string[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:361](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L361)

#### Description {#description-1}

List of channels you wish to update access for. Can only be used if user\_ids is not provided.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:351](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L351)

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

* * *

### user_ids? {#user_ids}

```text
optional user_ids: string[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:366](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L366)

#### Description {#description-4}

List of users you wish to update access for. Can only be used if channel\_ids is not provided.
