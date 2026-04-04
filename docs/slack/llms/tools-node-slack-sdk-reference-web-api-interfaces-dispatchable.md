Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Dispatchable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Dispatchable

# Interface: Dispatchable

Defined in: packages/types/dist/block-kit/extensions.d.ts:23

## Extended by {#extended-by}

* [`EmailInput`](/tools/node-slack-sdk/reference/web-api/interfaces/EmailInput)
* [`NumberInput`](/tools/node-slack-sdk/reference/web-api/interfaces/NumberInput)
* [`PlainTextInput`](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextInput)
* [`URLInput`](/tools/node-slack-sdk/reference/web-api/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextInput)

## Properties {#properties}

### dispatch_action_config? {#dispatch_action_config}

```text
optional dispatch_action_config: DispatchActionConfig;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:28

#### Description {#description}

A [DispatchActionConfig](/tools/node-slack-sdk/reference/web-api/interfaces/DispatchActionConfig) object that determines when during text input the element returns a [\`block\_actions\` payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload).
