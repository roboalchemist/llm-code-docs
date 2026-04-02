Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Action

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Action

# Interface: Action

Defined in: packages/types/dist/block-kit/extensions.d.ts:5

## Deprecated {#deprecated}

Action aliased to [Actionable](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable) in order to name the mixins in this file consistently.

## Extended by {#extended-by}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable)

## Properties {#properties}

### action_id? {#action_id}

```
optional action_id: string;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:12

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

* * *

### type {#type}

```
type: string;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:6
