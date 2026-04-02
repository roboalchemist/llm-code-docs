Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/URLRespondable

[@slack/types](/tools/node-slack-sdk/reference/types/) / URLRespondable

# Interface: URLRespondable

Defined in: [block-kit/extensions.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L60)

## Extended by {#extended-by}

* [`ConversationsSelect`](/tools/node-slack-sdk/reference/types/interfaces/ConversationsSelect)
* [`ChannelsSelect`](/tools/node-slack-sdk/reference/types/interfaces/ChannelsSelect)

## Properties {#properties}

### response_url_enabled? {#response_url_enabled}

```
optional response_url_enabled: boolean;
```

Defined in: [block-kit/extensions.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L67)

#### Description {#description}

When set to `true`, the [\`view\_submission\` payload](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) from the menu's parent view will contain a `response_url`. This `response_url` can be used for [message responses](https://docs.slack.dev/interactivity/handling-user-interaction#message_responses). The target conversation for the message will be determined by the value of this select menu.
