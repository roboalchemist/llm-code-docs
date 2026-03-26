# Source: https://momentic.ai/docs/steps/press.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Press

> Press a combination of keys on the keyboard

Press the specified keys using the keyboard.

For all available key combinations that can be used, see the
[Key values](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values)
guide.

## Inputs

<ResponseField name="Value" type="string" required>
  Use `+` to combine keys, e.g. `Control+Shift+T`. Here is a list of valid key
  values.
</ResponseField>

## Configs

<ResponseField name="Convert platform-specific keys" type="boolean" default={true}>
  Automatically convert known keyboard combinations based on the current
  operating system. For example, `Meta+V` is converted to `Ctrl+V` when the test
  is executed in a Linux environment.
</ResponseField>

<ResponseField name="Repeat" type="number" default={1}>
  Number of times to issue the key sequence.
</ResponseField>

<ResponseField name="Delay ms" type="number" default={25}>
  Milliseconds to wait after each key sequence. This is only applicable if the
  `repeat` config is set to a value greater than 1.
</ResponseField>


Built with [Mintlify](https://mintlify.com).