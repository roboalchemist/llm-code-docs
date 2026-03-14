# Source: https://launchdarkly.com/docs/api/approvals.md

An account member can request approval on changes to a flag or AI Config's targeting or variations, or to a segment's targeting. Members may be required to request approval depending on the settings in their LaunchDarkly project. Members can optionally request an approval even if it is not required.

An approval request prevents a change from being applied without approval from another member. Select up to ten members as reviewers. Reviewers receive an email notification, but anyone with sufficient permissions can review a pending approval request. A change needs at least one approval before you can apply it. To learn more, read [Approvals](https://launchdarkly.com/docs/home/releases/approvals).

Changes that conflict will fail if approved and applied, and the flag or segment will not be updated.

Several of the endpoints in the approvals API require an approval request ID. The approval request ID is returned as part of the [Create approval request](https://launchdarkly.com/docs/api/approvals/post-approval-request) and [List approval requests for a flag](https://launchdarkly.com/docs/api/approvals/get-approvals-for-flag) responses. It is the `_id` field, or the `_id` field of each element in the `items` array. If you created the approval request as part of a [workflow](https://launchdarkly.com/docs/api/workflows), you can also use a workflow ID as the approval request ID. The workflow ID is returned as part of the [Create workflow](https://launchdarkly.com/docs/api/workflows/post-workflow) and [Get workflows](https://launchdarkly.com/docs/api/workflows/get-workflows) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.
