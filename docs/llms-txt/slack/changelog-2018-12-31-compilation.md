Source: https://docs.slack.dev/changelog/2018/12/31/compilation

# 2018 shortform changelog entries

December 31, 2018

## December {#december}

* Post replies in a thread with incoming webhooks: the `thread_ts` parameter now puts your webhook reply in its proper place.
* The data structure of messages received from our APIs will change with the [launch of Block Kit](https://medium.com/slack-developer-blog/catching-up-on-all-things-spec-851f8c5136fb#df8b) early next year. In return you'll be able to add newer, clearer visual components to make your app's messages magnificent. Even if you aren't using it, your apps may be affected by the additions.

## November {#november}

* Apps may now restrict Web API requests to as many as _10_ IP address ranges.
* The developer preview for workspace apps has ended. We're taking the components of workspace apps and breaking them apart: applying them in phases to _existing_ as well as new apps. [Read more about the motivation behind ending the preview](https://medium.com/@SlackAPI/an-important-update-on-workspace-apps-aabc9e42a98b).

## September {#september}

* As public channels become private, they now retain their original channel ID. Legacy methods like `groups.*` and `channels.*` don't support these transitional channel types and Conversations API methods must be used instead.
* Whatever flavor of workspace token you're using, you can now expect the same `invalid_auth` error code when the token is invalid. You'll receive this error whether the token is expired, revoked, or just plain wrong. Use our OAuth 2.0-based token refresh system to refresh expired tokens safely.

## August {#august}

* Workspace apps may now continuously rotate shorter-lived tokens without downtime. Our OAuth 2.0-based token refresh system is strongly recommended for all workspace apps. Expiring and rotating tokens is required for all distributed workspace apps.
* Clear clever custom statuses like clockwork. Apps can add expiration dates when setting custom statuses for people.
* We're postponing planned changes around scope requirements for app and bot access to email addresses. The new date is in autumn, on **October 16th, 2018**.
* Dialogs now follow a separation of callback and state. Read more about the new `state` parameter and how it differs from `callback_id`.
* Verifying requests from Slack just got easier: [our Node Interactive Messages SDK](https://github.com/slackapi/node-slack-interactive-messages), [Node Events API SDK](https://github.com/slackapi/node-slack-events-api), and [Python Events API SDK](https://github.com/slackapi/python-slack-events-api) now verify request signatures automatically.
* _"40k ought to be enough characters for any message."_ - Slack Platform Gatekeepers. Messages are now limited to 40,000 characters.
* Your workspace app can use the new `apps.uninstall` method to uninstall itself from a single workspace, revoking all tokens associated with it. To revoke a workspace token _without_ uninstalling the app, use `auth.revoke`.
* It's official: workspace apps can reach out to and converse with anyone using the new `conversations.app_home:create` scope. No more fumbling with conversation IDs or different methods: just plug the user's ID into `chat.postMessage` and go.
* If your workspace app posts ghostly messages with `chat.postEphemeral`, you may have noticed a `no_permission` error thrown instead of `channel_not_found` when your app isn't a member of the target conversation. Turns out we actually _could_ find the channel after all.
* We updated our [Slack App Developer Policy and API Terms of Service](https://slack.com/terms-of-service/api-updated) to provide more detailed guidance, but we have not made material changes. The new policy is effective **August 31, 2018**. Together, we keep Slack a safe, private and secure platform for work.

## July {#july}

* Pagination rules the nation and the Slack API. These methods newly support cursors: `files.info`, `groups.list`, `im.list`, `mpim.list`, `reactions.list`, and `stars.list`. For apps created after **August 7, 2018**, results will be returned in perfect, piecemeal pages _by default_.
* With [Slack developer tools](https://sdt.builtbyslack.com) you can now quickly look up documentation, investigate the structure of messages, and more, all inside of Slack.
* Commenting on files is now just like replying to a message.
* HTTP requests originating from Slack now support Mutual TLS. Use Mutual TLS to attain the highest level of confidence that requests from Slack are, in fact, authentic. Read more.
* Get ready to lend users a hand and start working on their behalf. Now workspace apps can ask for permission to read & write personalized settings like reminders, custom status, and profile data.
* Our recently launched message actions are now available for use in all Enterprise organization workspaces and any Shared Channels within them.

## June {#june}

* Confidently verify a request originates from Slack by validating our new request signatures. The signing process replaces the use of verification tokens, now deprecated.
* We expect file threads to arrive after **July 19, 2018**. Do you manage a Slack app relying heavily on files or file comments? Join our _pilot program_ and prepare your app for file threads ahead of the transition.
* Learn when private channels are deleted with the new `group_deleted` event, now available for the Events and RTM APIs.
* The Conversations API now supports workspace apps, using three simplified scopes: `conversations:history`, `conversations:read`, and `conversations:write`. We recommend upgrading your apps in developer preview to the Conversations API as soon as possible.

## May {#may}

* Beginning **October 16, 2018** the `users:read.email` scope is _required_ to retrieve the `email` field from user profiles while using _user_ or _workspace_ tokens. Consult our previous announcements on this topic from 2016 and 2017 for migration tips and some historical perspective.
* Adding contextual actions lets users send specific messages to your app at will. [Here are some amazing things](https://medium.com/@SlackAPI/introducing-actions-a-simple-shortcut-attached-to-every-slack-message-e2404414ece) our partners do with actions. This blueprint demonstrates the ineffable _synergy_ of using actions and dialogs together.
* We're compiling a [humble library of JSON schema](https://github.com/slackapi/slack-api-specs/tree/master/events-api) about the Events API into a kind of [open specification](https://github.com/slackapi/slack-api-specs) called [AsyncAPI](https://www.asyncapi.com/).
* Newly-issued bot user token strings are a little longer than before. Building for the ages? Plan for token strings containing up to 255 characters.
* Apps participating in our developer preview using the Events API will need to subscribe to `message.app_home` events for a focused feed of messages between your app and the people who interface with them through the _app home_. These messages aren't delivered to `message.im` subscriptions now.
* File threads, a replacement for file comments, is on the way!

## April {#april}

* Measure drop off and send helpful follow ups when users cancel dialogs with these opt-in cancellation notifications.
* Have a bot user token you don't need or want to use anymore? Now you can use `xoxb-` tokens with `auth.revoke`.
* Your workspace token-based apps in _developer preview_ must now request the `files:write` scope to upload & manage files instead of `files:write:user`. Existing access grants are backfilled. Know your read & write rights.
* Working with workspace token-based apps as part of our preview? Please start using `oauth.access` instead of `oauth.token` during installation.
* Some bots are users too. Now you can find a bot user's `user_id` with `bots.info`.
* Enhance your dialogs with dynamic form elements "borrowed" from message menus.
* Rediscover the conversations you're party to with `users.conversations`.

## March {#march}

* We corrected and clarified the behavior of `users.profile.set` to only allow _admins_ of paid teams to update email address profile fields.
* We added a `type` field to the requests dispatched to your _Options Load URL_, used in message menus and— well, it doesn't work anywhere else _yet_ but we'll have a dialog about that one day...
* This significant upgrade to the [Slack SDK for Node.js](https://github.com/slackapi/node-slack-sdk/releases/tag/v4.0.0) modernizes one of the most widely-used JavaScript libraries on our platform with strong typing, more intuitive method signatures, and comfortingly predictable release cycles. It also sheds its aging DataStore, which has not evolved in tandem with the realities of building apps for today's workspaces. Learn more about upgrading in [our announcement](https://medium.com/slack-developer-blog/noteworthy-updates-to-the-slack-node-sdk-d3f77389d6c7).
* We are continuing to decrease the maximum number of results returned by `members` arrays returned in `channels.*` and `rtm.start`, with the limit currently set to 500 results. `conversations.members` provides paginated access instead. Read this announcement for detail.
* Web API methods will be enhanced with tiered rate limiting beginning **March 7, 2018**, with most methods gaining greater limits than ever before.
* Now you can follow up after users submit your dialogs. Use the new `response_url` attached to any `dialog_submission` to send messages after submission.

## February {#february}

* Now users can respond to dialog textarea elements with up to 3,000 riveting, carefully-chosen characters.
* Events API rate limiting has matured, now allowing apps up to 30,000 event deliveries per workspace per hour. Having trouble keeping up? Event deliveries will only be disabled when apps drop below a 5% successful response rate.
* The `users.setActive` method was recently rendered irrelevant by our efforts to modernize our message servers. Use `users.setPresence` and/or connect via RTM to proclaim a user's presence instead. We'll remove this no-op method entirely on **May 8, 2018**.

## January {#january}

* Catch up on recent changes to presence in the RTM and Web APIs and changes to come, including the deprecation of `users.list`'s `presence` parameter.
* Having trouble connecting to the RTM API lately? WebSocket URIs may contain querystring parameters & some libraries don't like that. Find out more.
* Workspace token apps in _developer preview_ now must request the `chat:write` scope to post messages. Existing access grants are backfilled.
* Active listening made easier: Subscribe to `app_mention` events to exclusively receive messages mentioning your app or bot.
* Now shared channels can be made private and the implications are well worth considering, especially if assuming channel IDs beginning with C are public.

**Tags:**

* [Compilation](/changelog/tags/compilation)
