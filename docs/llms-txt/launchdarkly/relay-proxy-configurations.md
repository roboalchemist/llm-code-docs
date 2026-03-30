# Source: https://launchdarkly.com/docs/api/relay-proxy-configurations.md


> ### Relay Proxy automatic configuration is an Enterprise feature
>
> Relay Proxy automatic configuration is available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).

The Relay Proxy automatic configuration API provides access to all resources related to relay tokens. To learn more, read [Automatic configuration](https://launchdarkly.com/docs/sdk/relay-proxy/automatic-configuration).

Several of the endpoints in the Relay Proxy automatic configuration API require a configuration ID. The Relay Proxy configuration ID is returned as part of the [Create a new Relay Proxy config](https://launchdarkly.com/docs/api/relay-proxy-configurations/post-relay-auto-config) and [List Relay Proxy configs](https://launchdarkly.com/docs/api/relay-proxy-configurations/get-relay-proxy-configs) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.
