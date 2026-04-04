# Source: https://launchdarkly.com/docs/api/workflows.md

> ### Workflows are in maintenance mode
>
> The workflows feature is in maintenance mode, and is planned for future deprecation at a date not yet specified. We will work with existing customers using workflows to migrate to a replacement solution when deprecation occurs.

A workflow is a set of actions that you can schedule in advance to make changes to a feature flag at a future date and time. You can also include approval requests at different stages of a workflow. To learn more, read [Workflows](https://launchdarkly.com/docs/home/releases/workflows).

The actions supported are as follows:

- Turning targeting `ON` or `OFF`
- Setting the default variation
- Adding targets to a given variation
- Creating a rule to target by segment
- Modifying the rollout percentage for rules

You can create multiple stages of a flag release workflow. Unique stages are defined by their conditions: either approvals and/or scheduled changes.

Several of the endpoints in the workflows API require a workflow ID or one or more member IDs. The workflow ID is returned as part of the [Create workflow](https://launchdarkly.com/docs/api/workflows/post-workflow) and [Get workflows](https://launchdarkly.com/docs/api/workflows/get-workflows) responses. It is the `_id` field, or the `_id` field of each element in the `items` array. The member ID is returned as part of the [List account members](https://launchdarkly.com/docs/api/account-members/get-members) response. It is the `_id` field of each element in the `items` array.
