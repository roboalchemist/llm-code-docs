# Source: https://launchdarkly.com/docs/api/segments.md


> ### Synced segments and larger list-based segments are an Enterprise feature
>
> This section documents endpoints for rule-based, list-based, and synced segments.
>
> A "big segment" is a segment that is either a synced segment, or a list-based segment with more than 15,000 entries that includes only one targeted context kind. LaunchDarkly uses different implementations for different types of segments so that all of your segments have good performance.
>
> In the segments API, a big segment is indicated by the `unbounded` field being set to `true`.
>
> These segments are available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).

Segments are groups of contexts that you can use to manage flag targeting behavior in bulk. LaunchDarkly supports:

* rule-based segments, which let you target groups of contexts individually or by attribute,
* list-based segments, which let you target individual contexts or uploaded lists of contexts, and
* synced segments, which let you target groups of contexts backed by an external data store.

To learn more, read [Segments](https://launchdarkly.com/docs/home/flags/segments).

The segments API allows you to list, create, modify, and delete segments programmatically.

You can find other APIs for working with big segments under [Persistent store integrations (beta)](https://launchdarkly.com/docs/api/persistent-store-integrations-beta).
