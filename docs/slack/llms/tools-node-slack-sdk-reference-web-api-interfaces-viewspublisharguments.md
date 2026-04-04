Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ViewsPublishArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ViewsPublishArguments

# Interface: ViewsPublishArguments

Defined in: [packages/web-api/src/types/request/views.ts:40](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/views.ts#L40)

## Extends {#extends}

* `BaseViewsArguments`.`TokenOverridable`.`ViewHash`

## Properties {#properties}

### hash? {#hash}

```text
optional hash: string;
```text

Defined in: [packages/web-api/src/types/request/views.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/views.ts#L36)

#### Description {#description}

A string that represents view state to protect against possible race conditions.

#### See {#see}

[Avoiding race conditions when using views](https://docs.slack.dev/surfaces/modals#handling_race_conditions).

#### Inherited from {#inherited-from}

```text
ViewHash.hash
```text

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```text

* * *

### user_id {#user_id}

```text
user_id: string;
```text

Defined in: [packages/web-api/src/types/request/views.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/views.ts#L42)

#### Description {#description-2}

ID of the user you want publish a view to.

* * *

### view {#view}

```text
view: View;
```text

Defined in: [packages/web-api/src/types/request/views.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/views.ts#L7)

#### Description {#description-3}

A [view payload](https://docs.slack.dev/surfaces/modals).

#### Inherited from {#inherited-from-2}

```text
BaseViewsArguments.view
```text
