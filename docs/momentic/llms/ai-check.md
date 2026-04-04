# Source: https://momentic.ai/docs/steps/ai-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI check

> Use AI to check if a condition is true

AI checks are assertions on steroids. You can specify a condition in natural
language that can be as specific as "the button on the top left corner of the
page is blue" or as broad as "there is no error page".

## Inputs

<ResponseField name="Assertion" type="string" required>
  The condition you want to assert. The assertion should be written in plain
  English and can be as specific or as broad as you like.
</ResponseField>

## Configs

<ResponseField name="AI context mode" type="string" default="HTML & screenshot">
  Choose between a general-purpose AI model that can understand both HTML &
  screenshots, or an advanced vision-only model optimized for visual attributes.
</ResponseField>

<ResponseField name="Timeout" type="number">
  The maximum number of seconds to wait for the assertion to be true. If it
  becomes true at any point during that window, the step passes. The step may
  continue running for a bit longer due to the latency of the final check, which
  starts when the timeout is reached. If unset, defaults to the smart waiting
  timeout, which is usually 5s.
</ResponseField>


Built with [Mintlify](https://mintlify.com).