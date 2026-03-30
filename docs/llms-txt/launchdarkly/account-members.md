# Source: https://launchdarkly.com/docs/api/account-members.md

The account members API allows you to invite new members to an account by making a `POST` request to `/api/v2/members`. When you invite a new member to an account, an invitation is sent to the email you provided. Members with Admin or Owner roles may create new members, as well as anyone with a `createMember` permission for "member/\*". To learn more, read [LaunchDarkly account members](https://launchdarkly.com/docs/home/account/members).

Any member may request the complete list of account members with a `GET` to `/api/v2/members`.

Several of the endpoints in the account members API require a member ID. The member ID is returned as part of the [Invite new members](https://launchdarkly.com/docs/api/account-members/post-members) and [List account members](https://launchdarkly.com/docs/api/account-members/get-members) responses. It is the `_id` field of each element in the `items` array.
