# Source: https://launchdarkly.com/docs/api/persistent-store-integrations-beta.md

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

### Persistent store integrations

Persistent store integrations, also called "big segment" store integrations, are required when you use a server-side SDK and big segments. You can use the persistent store integrations API endpoints to manage these integrations.

> ### Synced segments and larger list-based segments are an Enterprise feature
>
> Segments synced from external tools and larger list-based segments with more than 15,000 entries are the two kinds of "big segment." LaunchDarkly uses different implementations for different types of segments so that all of your segments have good performance.
>
> These segments are available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).

[Segments synced from external tools](https://launchdarkly.com/docs/home/flags/synced-segments) and [larger list-based segments](https://launchdarkly.com/docs/home/flags/list-based-segments) are the two kinds of big segment. If you are using server-side SDKs, these segments require a persistent store within your infrastructure. LaunchDarkly keeps the persistent store up to date and consults it during flag evaluation.

You need either a persistent store integration or a [Relay Proxy](https://launchdarkly.com/docs/sdk/relay-proxy) to support these segments. The persistent store integrations API lets you manage the persistent store integrations.

To learn more about segments, read [Segments](https://launchdarkly.com/docs/home/flags/segments) and [Segment configuration](https://launchdarkly.com/docs/home/flags/segment-config).

Several of the endpoints in the persistent store integrations API require an integration ID. The integration ID is returned as part of the [Create big segment store integration](https://launchdarkly.com/docs/api/persistent-store-integrations-beta/create-big-segment-store-integration) response, in the `_id` field. It is also returned as part of the [List all big segment store integrations](https://launchdarkly.com/docs/api/persistent-store-integrations-beta/get-big-segment-store-integrations) response, in the `_id` field of each element in the `items` array.

You can find other APIs for working with big segments under [Segments](https://launchdarkly.com/docs/api/segments).
