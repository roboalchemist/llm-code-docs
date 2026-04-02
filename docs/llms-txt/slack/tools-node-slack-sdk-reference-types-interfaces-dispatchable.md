Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Dispatchable

[@slack/types](/tools/node-slack-sdk/reference/types/) / Dispatchable

# Interface: Dispatchable

Defined in: [block-kit/extensions.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L28)

## Extended by {#extended-by}

* [`EmailInput`](/tools/node-slack-sdk/reference/types/interfaces/EmailInput)
* [`NumberInput`](/tools/node-slack-sdk/reference/types/interfaces/NumberInput)
* [`PlainTextInput`](/tools/node-slack-sdk/reference/types/interfaces/PlainTextInput)
* [`URLInput`](/tools/node-slack-sdk/reference/types/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/types/interfaces/RichTextInput)

## Properties {#properties}

### dispatch_action_config? {#dispatch_action_config}

```text
optional dispatch_action_config: DispatchActionConfig;
```

Defined in: [block-kit/extensions.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L33)

#### Description {#description}

A [DispatchActionConfig](/tools/node-slack-sdk/reference/types/interfaces/DispatchActionConfig) object that determines when during text input the element returns a [\`block\_actions\` payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload).
