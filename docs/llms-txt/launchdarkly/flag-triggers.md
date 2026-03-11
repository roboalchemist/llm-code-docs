# Source: https://launchdarkly.com/docs/api/flag-triggers.md

> ### Flag triggers is an Enterprise feature
>
> Flag triggers is available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).

Flag triggers let you initiate flag changes remotely using a unique webhook URL. For example, you can integrate triggers with your existing tools to enable or disable flags when you hit specific operational health thresholds or receive certain alerts. To learn more, read [Flag triggers](https://launchdarkly.com/docs/home/releases/triggers).

With the flag triggers API, you can create, delete, and manage triggers.

Several of the endpoints in the flag triggers API require a flag trigger ID. The flag trigger ID is returned as part of the [Create flag trigger](https://launchdarkly.com/docs/api/flag-triggers/create-trigger-workflow) and [List flag triggers](https://launchdarkly.com/docs/api/flag-triggers/get-trigger-workflows) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.
