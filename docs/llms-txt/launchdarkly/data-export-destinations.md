# Source: https://launchdarkly.com/docs/api/data-export-destinations.md

> ### Data Export is an add-on feature
>
> Data Export is available as an add-on for customers on a Foundation or Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).

Data Export provides a real-time export of raw analytics data, including feature flag requests, analytics events, custom events, and more.

Data Export destinations are locations that receive exported data. The Data Export destinations API allows you to configure destinations so that your data can be exported.

Several of the endpoints in the Data Export destinations API require a Data Export destination ID. The Data Export destination ID is returned as part of the [Create a Data Export destination](https://launchdarkly.com/docs/api/data-export-destinations/post-destination) and [List destinations](https://launchdarkly.com/docs/api/data-export-destinations/get-destinations) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.

To learn more, read [Data Export](https://launchdarkly.com/docs/integrations/data-export).
