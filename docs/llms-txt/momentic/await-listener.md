# Source: https://momentic.ai/docs/steps/await-listener.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Await listener

> Wait for an event listener to resolve

Wait for an event listener to resolve. This is useful when you have registered a
listener for a specific event (like a network request) and want to wait for that
event to complete before proceeding with the next steps. If the listener does
not resolve within the specified timeout, this step will fail.

## Inputs

<ResponseField name="Listener key" type="string" required>
  The unique key of the listener you want to wait for. This key should match the
  one used in the [register request
  listener](../steps/register-request-listener) step.
</ResponseField>

## Configs

<ResponseField name="Timeout" type="string">
  The maximum time to wait for the listener to resolve, in seconds. If the
  listener does not resolve within this time, the step will fail. Default is 10
  seconds.
</ResponseField>

<ResponseField name="Save to an environment variable" type="string">
  The name of the environment variable where the result of the listener will be
  saved. This is useful if you need to use a [javascript
  step](/steps/javascript) to validate the response.
</ResponseField>


Built with [Mintlify](https://mintlify.com).