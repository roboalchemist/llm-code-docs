# Source: https://checklyhq.com/docs/resolve/traces/export/honeycomb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Traces to Honeycomb

> Learn how to export traces from Checkly to Honeycomb.

1. Grab the relevant API endpoint from [the Honeycomb documentation](https://docs.honeycomb.io/send-data/opentelemetry/#using-the-honeycomb-opentelemetry-endpoint). It should look like `https://api.honeycomb.io/v1/traces`.
2. Grab your Honeycomb Ingest API key from the **Account** > **Team settings** > **Environments and API keys** section.
3. Add the endpoint the Checkly integration settings and provide the API key as an HTTP header `x-honeycomb-team` with
   the value of your API key.


Built with [Mintlify](https://mintlify.com).