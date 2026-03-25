# Source: https://docs.rootly.com/liquid/alert-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Alert Variables

> Learn about alert variables available in Liquid templates for processing webhook data and alert information in workflows.

We are using [Liquid](https://shopify.github.io/liquid/) template language and available variables are:

```ruby Ruby theme={null}
{{ alert.id }} # returns string
{{ alert.source }} # returns string
{{ alert.summary }} # returns string
{{ alert.data }} # returns raw webhook data in json
```


Built with [Mintlify](https://mintlify.com).