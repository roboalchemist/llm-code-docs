# Source: https://checklyhq.com/docs/resolve/traces/export/dash0.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Traces to Dash0

> Learn how to export traces from Checkly to Dash0.

1. Create an API key in the **Settings** > **Auth Tokens** section.
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/dash0-token.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=2f6518e3ea6f20755faed20d089eae14" alt="Generate an auth token" width="1244" height="392" data-path="images/docs/images/otel/export-traces/dash0-token.png" />
2. Grab the right endpoint URL for your Dash0 organization from the **Settings** > **Endpoints** section. It should look like `https://ingress.eu-west-1.aws.dash0.com/v1/traces`.
   Make sure it ends with `/v1/traces/`
3. Add the endpoint and the auth token to the Checkly integration settings. The auth token is added as an HTTP header named
   `Authorization` with the value of `Bearer ` and your auth token.
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/dash0-checkly.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=0fecfe46bcab51c185dcd402f71d9c21" alt="Fill in the values into Checkly" width="1017" height="473" data-path="images/docs/images/otel/export-traces/dash0-checkly.png" />
4. Observe Spans appearing in Dash0 on the `Tracing` tab.
   <img src="https://mintcdn.com/checkly-422f444a/WJFfxOuqqqZjE4cw/images/docs/images/otel/export-traces/dash0-traces.png?fit=max&auto=format&n=WJFfxOuqqqZjE4cw&q=85&s=4e57ce24a318c5eea6de5a54ed800cff" alt="Traces displayed in Dash0" width="1485" height="902" data-path="images/docs/images/otel/export-traces/dash0-traces.png" />

Find all the details in the [Dash0 documentation](https://www.dash0.com/documentation).


Built with [Mintlify](https://mintlify.com).