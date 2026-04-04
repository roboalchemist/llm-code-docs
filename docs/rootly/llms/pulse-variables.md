# Source: https://docs.rootly.com/liquid/pulse-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pulse Variables

> Reference for pulse variables available in Liquid templates for processing health check and monitoring data in workflows.

We are using [Liquid](https://shopify.github.io/liquid/) template language and available variables are:

```ruby Ruby theme={null}
{{ pulse.id }} # returns string
{{ pulse.source }} # returns string
{{ pulse.summary }} # returns string
{{ pulse.data }} # returns object
```


Built with [Mintlify](https://mintlify.com).