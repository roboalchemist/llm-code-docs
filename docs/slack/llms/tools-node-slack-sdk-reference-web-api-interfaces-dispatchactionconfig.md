Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/DispatchActionConfig

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DispatchActionConfig

# Interface: DispatchActionConfig

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:52

## Description {#description}

Defines when a [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) will return a [\`block\_actions\` interaction payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload).

## See {#see}

[\`block\_actions\` interaction payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload).

## Properties {#properties}

### trigger_actions_on? {#trigger_actions_on}

```text
optional trigger_actions_on: ("on_enter_pressed" | "on_character_entered")[];
```

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:61

#### Description {#description-1}

An array of interaction types that you would like to receive a [\`block\_actions\` payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload) for. Should be one or both of: `on_enter_pressed` — payload is dispatched when user presses the enter key while the input is in focus. Hint text will appear underneath the input explaining to the user to press enter to submit. `on_character_entered` — payload is dispatched when a character is entered (or removed) in the input.
