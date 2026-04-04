Source: https://docs.slack.dev/changelog/2020/12/31/compilation

# 2020 shortform changelog entries

December 31, 2020

## December {#december}

* Submissions to the Slack Marketplace now require Security & Compliance information.
* Reach a whole new world of workspaces: build an app that can be deployed across an entire Enterprise org.

## November {#november}

* Apps created after **February 24, 2021** will no longer be able to send `token` as a query parameter. All existing apps require no changes.
* Apps will now be able to unfurl links anywhere in Slack.

## October {#october}

* The admin.analytics.getFile method returns compressed JSON files with workspace member analytics for the day of your choice—now available for Enterprise.
* App [modals](/surfaces/modals) can now be 'popped out' by users, giving them their own resizable, movable window. No app changes are needed, we just wanted to pop in with an update.
* To simplify time input for users, we added a new time picker element to Block Kit.
* Block Kit checkboxes and radio buttons are now available to use in messages. Quickly and conversationally collect information from users by including them inline.
* Gather data from users directly from your App Home—input blocks can now be added to Home tabs. Additionally, input blocks can now dispatch `block_actions` payloads when someone interacts with them. Read about the new `dispatch_actions` flag.
* We refreshed the look of your app's listing in the Slack Marketplace. Among the changes: a _Features_ tab shows your app's entry points—like shortcuts and slash commands.

## September {#september}

* We updated our [developer policy and API terms of service](https://slack.com/terms-of-service/api-updated) to clarify language around export controls and international data transfers.
* Alongside upcoming changes to the Events API, you'll find numerous new features: a new `authorizations` field delivered with events, a new method for listing installations, a new scope—even a new token type for working across an entire organization.
* Starting **February 24, 2021**, event payloads will no longer contain full lists of `authed_users` or `authed_teams`. Instead, you can call a separate method if you need a full list of parties an event is visible to.
* On **September 29, 2020**, `view_submission` and `block_actions` payloads will begin including full `state` for messages, modal, and App Home views.
* On **September 15, 2020**, you'll no longer need to worry about different _global_ and _local_ IDs for Enterprise users. Users will have a single, global ID across an Enterprise org, which may begin with _either_ `U` or `W`.
* In responses from the `search.messages` method, four fields—`next`, `next_2`, `previous`, and `previous_2`—that sometimes appeared are now deprecated and will no longer appear in responses, beginning **December 3, 2020**.
* Get a handle on creating channels, setting preferences, and connecting new workspaces—all with a single app. Use the APIs for channel management, available to Enterprise organizations.
* We _slightly_ changed your App Home's appearance by refreshing the default text style and how hint text is displayed. We hope you'll enjoy it.

## August {#august}

* Users may now mute and unmute their conversations with apps [like they can with other channel types](https://slack.com/help/articles/204411433-Mute-channels-and-direct-messages). When a user mutes a conversation with your app, the messages you send are still delivered and a colorful badge will continue to surface in their channel list. However, users will not receive a direct operating system or browser notification on delivery.
* Slash command invocations will now include an `api_app_id` parameter with your Slack app's ID. This parameter will better assist you in handling commands from multiple applications or environments.

## July {#july}

* New header blocks let you provide stronger delineation between groups of content in your app surfaces. Stay a_head_ of the game by learning how they work.
* Expand Workflow Builder's capabilities by creating reusable, custom steps that any builder can add to their workflows. Workflow Steps from Apps is now in open beta. What’s your app’s next step?
* Previously, when a user mentioned an app that wasn't party to the conversation, the user could `Invite` the app to the conversation, `Let Them Know`, or `Do Nothing`. The `Let Them Know` button didn't work. We've fixed that mistake by removing the button, and updated our documentation on the `app_mention` event as well.
* Mark messages unread for users with `conversations.mark`. Bespoke clients and personal utilities should use this method sparingly.
* The URL where users manage existing installations of Slack apps is changing to [`https://app.slack.com/apps-manage/`](https://app.slack.com/apps-manage/). You might not even notice the difference, but we’re letting you know just in case.

## June {#june}

* You can now present your app's pricing information in your listing in the Slack Marketplace.
* With Slack Connect, channels connect multiple workspaces and organizations with ease.
* A change to `user_change` events: we've fixed a bug where these events dispatched to subscriptions from all workspaces in externally-shared channels. Now, `user_change` events are dispatched only to the home workspace of an externally-shared channel.
* If you create a _new_ Slack app and use deprecated methods like `channels.*`, `im.*`, `mpim.*`, or `groups.*`, you'll now receive a `method_deprecated` error. _Existing_ apps will receive _warnings_ but still have until **February 24th, 2021** to migrate to the Conversations API.
* Maintain a membership allowlist for private channels using `admin.conversations.restrictAccess.addGroup`, `admin.conversations.restrictAccess.removeGroup`, & `admin.conversations.restrictAccess.listGroups` methods, now available for Enterprise organizations. _Update_: These methods were renamed but the old names will continue to work.
* We recently updated [Block Kit Builder](https://app.slack.com/block-kit-builder) with additional preview options and more convenient ways to copy, paste, and dispatch payloads. There's more beauty to it too.

## May {#may}

* The deadline for all Slack apps to use the Conversations API—instead of its antecedents—has moved from this November to **February 24th, 2021**. Newly created Slack apps won't be able to use `channels.*`, `im.*`, `mpim.*`, or `groups.*` methods beginning **June 10th, 2020**. Warnings will soon be included as part of deprecated responses.
* Use the Calls API to hook your calls natively into Slack. Catch up on Calls.
* Legacy tester tokens may no longer be created. Existing tokens may continue to be used, regenerated, or revoked. Tokens left unused for three months or more will be regularly revoked.from our previous announcement.
* [Complete your IDP groups](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-organization) with custom default channels, courtesy of the `admin.usergroups.*` API methods.
* Starting **July 1st, 2020**, rate limits will apply to all SCIM methods. Please make sure any apps using the SCIM APIs remain within these limits and humbly handle HTTP 429 responses.

## April {#april}

* A more direct route to messaging in response to modals: the new `default_to_current_conversation` field allows your `conversation_select` and `multi_conversation_select` menus to be pre-populate the currently open conversation.
* The shortcuts button is now available for all Slack workspaces, so we're taking global shortcuts out of beta.
* Previously, OAuth Redirect URLs could contain anchors (`#`). We've fixed that mistake, and anchors are no longer allowed.
* Beginning **June 10th, 2020**, all newly created Slack apps will be unable to use the deprecated methods in `channels.*`, `im.*`, `mpim.*`, and `groups.*`. Existing apps have until **February 24th, 2021** to migrate to the Conversations API.
* Visually highlight destructive actions by using the new `style` parameter in confirmation objects.
* Give app installers good reason to trust your app: submit security and compliance information to the Slack Marketplace today.
* SCIM API endpoints now have clear, explicit rate limits.

## March {#march}

* Tune out the noise—you can now use filters with conversation lists in select and multi-select menus.and start filtering.
* Give users clear entry points to your Slack app with Shortcuts. App Actions are now called message shortcuts. They're joined by new global shortcuts that allow users to initiate interactivity from anywhere in Slack.
* The IDs returned by our APIs have grown longer. They are now up to 11 characters long, and could grow longer in future. Please audit your Slack apps, and verify any assumptions about the length of IDs for users, channels, and other objects.
* We didn't turn off the `replies` array field found in threaded parent messages on **October 18th, 2019** like we said we would. The new date is **March 31st, 2020**. Please use the `reply_users`, `reply_users_count`, and `latest_reply` fields instead.
* Fair is fair: radio buttons now support `mrkdwn` formatting, just like checkboxes.

## February {#february}

* New guidelines for Slack Marketplace submissions have arrived to help ready your app for the world.
* Using two new scopes, your Slack app can adjust its message authorship and post in any public channel.
* The creation of legacy test tokens is now deprecated and will permanently retire on **May 5th, 2020**.about using Slack apps to build firmly scoped integrations.
* Starting **February 18, 2020**, unexpected results using the SCIM API when rapidly updating data on the same user or group will become a thing of the past.
* It's a win for webhooks: you can skip the small stuff and [trigger a workflow with a web request](https://slack.com/help/articles/360041352714).
* Check another item off your Block Kit wishlist - we've added a checkbox group element to modals and Home tabs for your multiple choice input needs.
* You can submit information to the Slack Marketplace on your app's privacy policy, data retention, security tests, and compliance with major laws. [Read our blog post on the new Security & Compliance feature, now in open beta](https://medium.com/slack-developer-blog/building-trust-with-security-conscious-customers-1e85ee856045).

## January {#january}

* Our new emoji APIs allow Enterprise organization Admins and Owners to add, remove, list, rename, and alias custom emoji across the entire Enterprise organization. 🎉!
* Slack apps, with subtler permissions and more intuitive behavior, are now the default when you create an app. Get started by building or migrating.
* Your app's new Home tab is out of beta. Design a comfortable place for users to get work done using Block Kit Builder and publish them for users using `views.publish`. Get started by diving into the Home tab docs.
* Give users a key to directly open your Home tab. Read our updated deep-linking guide to see how you can create links to specific tabs in your App Home.
* We are deprecating all `channels.*`, `groups.*`, `im.*`, and `mpim.*` Web API methods in favor of their Conversations API replacements. Migrate to `conversations.*` as soon as possible, as these deprecated methods will retire on **February 24, 2021**.

**Tags:**

* [Compilation](/changelog/tags/compilation)
