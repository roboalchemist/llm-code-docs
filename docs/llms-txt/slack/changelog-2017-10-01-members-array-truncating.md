Source: https://docs.slack.dev/changelog/2017/10/01/members-array-truncating

# The members array is being truncated

October 1, 2017

Arrays of `members` found in API methods will become truncated beginning December 1, 2017.

The maximum number of results found in `members` continues to decrease regularly

As of March 2018, the limit is set to 500 results. Use [`conversations.members`](/reference/methods/conversations.members) for channels with large memberships.

Initially, Slack will limit `members` to the first 1,500 users and then gradually lower the number of users returned. You should expect API methods will cease returning `members` entirely at some point in the future. If you rely on the `members` array, you should instead begin using [`conversations.members`](/reference/methods/conversations.members) for a full list of members.

As Slack teams continue to grow in size, returning the full `members` array in these methods is no longer practical or performant, for the Slack APIs or developers. The `conversations.members` method will allow you to request a list of members at a time that makes sense for your app and should keep these method calls nice and zippy.

## What's changing? {#whats-changing}

Previously, calling a method such as `rtm.start` would include a `members` array that listed all of the members of a workspace or channel. But some Slack workspaces and channels now have tens of thousands of team members, which means these methods can be slow to be delivered and difficult for developers to manage.

Starting December 1, 2017, we will begin truncating the `members` array to 1,500 members. This number will then be lowered over time until, eventually, the `members` array will cease to be returned in these methods.

At the time of the last update in March 2018, `members` results are capped at 500.

If any `members` array is truncated, you'll receive a `member_list_truncated` warning in the response's `response_metadata`:

```json
{    // all other parts of the response    "response_metadata": {        "warnings": [            "member_list_truncated"        ]    }}
```text

If you need a list of team members in a channel, please begin using the recently introduced [`conversations.members`](/reference/methods/conversations.members) method, which includes a pagination cursor. See [pagination](/apis/web-api/pagination) for more detail.

## What happens if I do nothing? {#what-happens-if-i-do-nothing}

If your app isn't using the `members` array returned by any of the above methods, you don't need to change a thing!

If your app relies on the `members` array returned by these methods, it will no longer reliably return a full list of team members starting December 1, 2017. You should begin using the [conversations.members](/reference/methods/conversations.members) method to get a complete list of team members.

## When is this happening? {#when-is-this-happening}

The `members` array will be truncated starting **December 1, 2017**.

As of March, 2018 the `members` array is capped at 500 and will continue to decline.

## Tags:

* [Breaking change](/changelog/tags/breaking-change)
* [Announcement](/changelog/tags/announcement)
