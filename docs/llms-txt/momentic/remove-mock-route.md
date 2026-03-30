# Source: https://momentic.ai/docs/steps/remove-mock-route.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove mock route

> Stop mocking network requests to a given route

After this step is run, subsequent requests will be routed to their original
destination.

For more information about using this step, see our guide on
[request mocking](../request-mocking).

## Inputs

<ResponseField name="Key" type="string">
  The key that was defined when mocking the route. If not specified, this step
  will remove all mocks.
</ResponseField>


Built with [Mintlify](https://mintlify.com).