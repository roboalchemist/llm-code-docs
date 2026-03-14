# Source: https://launchdarkly.com/docs/api/teams.md

> ### Teams is an Enterprise feature
>
> Teams is available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).

A team is a group of members in your LaunchDarkly account. Members of the team have access to various resources in LaunchDarkly, such as projects or flags, based on the role or roles you assign to the team. To learn more, read [Teams](https://launchdarkly.com/docs/home/account/teams).

The Teams API allows you to create, read, update, and delete a team.

Several of the endpoints in the Teams API require one or more member IDs. The member ID is returned as part of the [List account members](https://launchdarkly.com/docs/api/account-members/get-members) response. It is the `_id` field of each element in the `items` array.
