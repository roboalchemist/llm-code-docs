# Source: https://momentic.ai/docs/steps/page-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Page check

> Assert on page content

Assert on the active page using HTML content substring.

<ResponseField name="Timeout" type="number">
  The maximum number of seconds to wait for the assertion to be true. If it
  becomes true at any point during that window, the step passes. The step may
  continue running for a bit longer due to the latency of the final check, which
  starts when the timeout is reached.
</ResponseField>


Built with [Mintlify](https://mintlify.com).