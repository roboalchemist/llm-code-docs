Source: https://docs.slack.dev/changelog/2022/12/31/output

# 2022 changelog entries

December 31, 2022

## November {#november}

* We released version `v1.16.4` of the developer tools for our Slack platform beta. We fixed some pipes behind the scenes to prevent future leaks; check out how we are improving the beta platform experience for our community.
* Three new endpoints for admins to manage role assignments are now available: `admin.roles.listAssignments`, `admin.roles.addAssignments`, and `admin.roles.removeAssignments`. Explore other useful methods for managing your users and workspaces here.
* We released version `v1.15.0` of the developer tools for our Slack platform beta. It also introduces a breaking change (arriving **January 26th, 2023**) for those making API calls to outgoing domains in their functions.

## October {#october}

* A bevy of new Block Kit input elements await developers soliciting input from users including the often requested combined date and time picker. Collect links with the URL input element or email addresses, numbers, too.
* We released version `v1.14.0` of the developer tools for our Slack platform beta.
* We updated the fine print and added default `placeholder` text for the following Block Kit elements: `channels_select`, `conversations_select`, `multi_channels_select`, `multi_users_select`, and `users_select`.
* At last, member\_joined\_channel now works as you'd expect for multi-party direct messages (MPIM). Be sure to add the mpim:read scope to receive these events!
* We're cleaning up some lingering behavior in our legacy Real Time Messaging API. In message events streamed over the RTM API, channel and usergroup mentions will no longer include entity names. Still need entity names? Access them using Web API methods such as `conversation.info` and `usergroups.list`. Alternatively, consider using the Events API, which also supports WebSockets, to receive `message` events.

## September {#september}

* Today we permanently alter the behavior of the retired Web API method `rtm.start`: those still using this method will receive the more reliable but brief response of the `rtm.connect` method.
* To better accommodate customers at Dreamforce next week, we've moved `rtm.start`'s final retirement date to **September 27th, 2022**. Learn more about the future of `rtm.start` and how it may impact your app.
* Several new tools for app developers are now available as part of our Slack platform open beta. Developers can ship higher-quality apps and workflows quickly with a streamlined development lifecycle, including secure hosting and data storage in Slack.

## August {#august}

* Keep track of who gets added to DM conversations. You can now monitor the `dm_user_added` audit event with the Audit Logs API.
* On **September 13th, 2022**, we will provide a preview of the `rtm.start` future behavior. If you still use `rtm.start` to connect to Slack, learn more about when this preview will be happening in your time zone and how it may impact your app.

## July {#july}

* Slack is used by public sector teams and their partners for being faster, better organized, and more secure than email. If you're a government agency, contractor, or just intrigued by how Slack supports government communication, our GovSlack documentation is the place to be!
* Bring users information and delight in your Slack apps with the video block now available in Block Kit. Read on to learn more on how to embed videos in your app.

## May {#may}

* Be informed about specific changes to users' data. One of three events will now be dispatched alongside the `user_change` event: `user_huddle_changed`, `user_profile_changed`, or `user_status_changed`.
* The file may be deleted, but the record of the event won't be. You can now monitor `file_deleted` audit events with the Audit Logs API.

## April {#april}

* Messages are how people communicate in Slack, message metadata is how apps communicate with apps! Read on to learn about how to spark more automation with your app throughout Slack.
* The `team.info` parameter `domain` is now public. Query for your team's information by `domain` only when `team` is null.

## March {#march}

* Mentioning a private channel in a slash command when your app manifest flag `should_escape` is `false` now correctly formats the channel identifier. Previously, the API would return HTML entities (`&lt;` and `&gt;`) that had to be manually converted into their character counterparts.

## February {#february}

* Help users find links, messages, and files germane to a channel's distinctive purpose with the Bookmarks API.
* The `admin.users.unsupportedVersions.export` API allows you to export users using unsupported software within your workspace. Read on to learn more.

## January {#january}

* Block Kit button elements can now utilize the optional `accessibility_label` field, which allows you to write longer descriptive text for a button. Learn more.
* The `admin.apps.requests.cancel` method allows admins to cancel app approval requests within a workspace or Enterprise org. Learn more.

**Tags:**

* [Compilation](/changelog/tags/compilation)
