# Source: https://launchdarkly.com/docs/api/scheduled-changes.md

> ### Scheduled flag changes is an Enterprise feature
>
> Scheduled flag changes is available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).

You can schedule flag targeting rule changes to take place at a selected time. You may schedule multiple changes for a single flag with each change having a different `ExecutionDate`. To learn more, read [Scheduled flag changes](https://launchdarkly.com/docs/home/releases/scheduled-changes).

Several endpoints in the scheduled changes API require an existing scheduled change ID. This ID is returned in the `_id` field from the [Create scheduled changes workflow](https://launchdarkly.com/docs/api/scheduled-changes/post-flag-config-scheduled-changes) response, or in the `_id` field of each element in the `items` array from the [List scheduled changes](https://launchdarkly.com/docs/api/scheduled-changes/get-flag-config-scheduled-changes) response.
