Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Action

[@slack/types](/tools/node-slack-sdk/reference/types/) / Action

# Interface: Action

Defined in: [block-kit/extensions.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L8)

## Deprecated {#deprecated}

Action aliased to [Actionable](/tools/node-slack-sdk/reference/types/interfaces/Actionable) in order to name the mixins in this file consistently.

## Extended by {#extended-by}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable)

## Properties {#properties}

### action_id? {#action_id}

```text
optional action_id: string;
```

Defined in: [block-kit/extensions.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L15)

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

* * *

### type {#type}

```text
type: string;
```

Defined in: [block-kit/extensions.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L9)
