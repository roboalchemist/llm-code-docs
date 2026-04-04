Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/URLRespondable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / URLRespondable

# Interface: URLRespondable

Defined in: packages/types/dist/block-kit/extensions.d.ts:51

## Extended by {#extended-by}

* [`ConversationsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsSelect)
* [`ChannelsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/ChannelsSelect)

## Properties {#properties}

### response_url_enabled? {#response_url_enabled}

```text
optional response_url_enabled: boolean;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:58

#### Description {#description}

When set to `true`, the [\`view\_submission\` payload](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) from the menu's parent view will contain a `response_url`. This `response_url` can be used for [message responses](https://docs.slack.dev/interactivity/handling-user-interaction#message_responses). The target conversation for the message will be determined by the value of this select menu.
