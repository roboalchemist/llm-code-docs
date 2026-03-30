# Source: https://momentic.ai/docs/steps/key-down.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Key down

> Hold down a combination of keys on the keyboard

Hold down the specified keys using the keyboard. This is useful for testing
behaviors like Shift+Click.

For all available key combinations that can be used, see the
[Key values](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values)
guide.

## Inputs

<ResponseField name="Key" type="string" required>
  Use `+` to combine keys, e.g. `Control+Shift+T`. Here is a list of valid key
  values.
</ResponseField>

## Configs

<ResponseField name="Convert platform-specific keys" type="boolean" default={true}>
  Automatically convert known keyboard combinations based on the current
  operating system. For example, `Meta+V` is converted to `Ctrl+V` when the test
  is executed in a Linux environment.
</ResponseField>


Built with [Mintlify](https://mintlify.com).