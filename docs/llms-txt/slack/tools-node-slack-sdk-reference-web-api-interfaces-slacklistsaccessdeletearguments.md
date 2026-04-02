Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SlackListsAccessDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsAccessDeleteArguments

# Interface: SlackListsAccessDeleteArguments

Defined in: [packages/web-api/src/types/request/slackLists.ts:329](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L329)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### channel_ids? {#channel_ids}

```text
optional channel_ids: string[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:338](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L338)

#### Description {#description}

List of channels you wish to update access for. Can only be used if user\_ids is not provided.

* * *

### list_id {#list_id}

```text
list_id: string;
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:333](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L333)

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

* * *

### user_ids? {#user_ids}

```text
optional user_ids: string[];
```text

Defined in: [packages/web-api/src/types/request/slackLists.ts:343](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/slackLists.ts#L343)

#### Description {#description-3}

List of users you wish to update access for. Can only be used if channel\_ids is not provided.
