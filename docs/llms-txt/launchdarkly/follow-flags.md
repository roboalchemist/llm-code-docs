# Source: https://launchdarkly.com/docs/api/follow-flags.md

Follow flags to receive email updates about targeting changes to a flag in a project and environment.

Several of the endpoints in the follow flags API require a member ID. The member ID is returned as part of the [Invite new members](https://launchdarkly.com/docs/api/account-members/post-members) and [List account members](https://launchdarkly.com/docs/api/account-members/get-members) responses. It is the `_id` field of each element in the `items` array.
