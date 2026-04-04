Source: https://docs.slack.dev/changelog/2017/12/31/compilation

# 2017 shortform changelog entries

December 31, 2017

## December {#december}

* For those moments when your app knows a user's email address but hasn't met them on Slack yet: now apps with `users:read.email` can use `users.lookupByEmail` and skip wading through `users.list`.
* Turn your links into buttons by adding link buttons to your messages.
* Storyboard, mock, and play make believe with these useful design templates starring your favorite platform features.

## November {#november}

* Use `chat.getPermalink` to easily exchange a message `ts` for a permalink URL.
* Why couldn't bot users use `bots.info`? We don't know but now they can too.
* Help people get back to work by deep linking to your Slack app or directly to a channel.
* When a workspace migrates to an Enterprise organization, existing users are given a second _global_ user ID. Now you can bulk convert those with `migration.exchange` and turn off your app's translation layer, living the dream of one user ID per user.
* Do what you like with this OpenAPI 2.0 specification of our Web API. Most methods now contain more helpful response examples. More specs and coverage on the way. [Read on](https://medium.com/slack-developer-blog/standard-practice-slack-web-openapi-spec-daaad18c7f8) about our API spec.

## October {#october}

* Send JSON when posting to Web API write methods. Gone are the days of perfunctory errors when sending lovingly crafted JSON to `chat.postMessage` and other methods.
* We broadened support for presenting your tokens as a "bearer token" in `Authorization` HTTP headers with the Web API.
* We removed the `latest`, `unread_count`, and `unread_count_display` fields from limited contexts of the new Conversations API. They weren't really supposed to be there. You won't find them spuriously lurking in the shadows again. We don't anticipate any issues but let us know if you find any.
* The `members` array found in many API methods is now truncated. We continue to lower the maximum results returned. Please use `conversations.members` to manage memberships instead.
* Scheduled changes and feature retirements to the Slack platform are now easier to find in our forward-looking calendar of upcoming changes.
* The RTM API's `presence_change` event requires `presence_sub` subscriptions beginning **November 15, 2017**.

## September {#september}

* Ask users for more structured form-based information with Dialogs.
* Now you can customize your app's experience by the locale and language preferred by users, channels, and other conversational constructs. Start practicing your Klingon. 🖖
* Shared Channels let Slack apps collaborate with users across different organizations.
* The Conversations API is a collection of more than 15 Web API methods normalizing the way apps deal with channels, direct messages, and more. Never rely on the first character of a channel ID again.
* The role of `@username` is changing on the platform but we're making the transition as backwards-compatible as possible.
* We are clarifying two terms encountered throughout Slack, _"team"_ (the people you _talk_ to in Slack) and _"workspace"_ (the place you do work). You'll find many _team_ references updated to _workspace_ across Slack and API documentation. With artifacts like the `team` object, field, and parameters scattered through the platform, you'll often still encounter `team` while reading and programming.
* No more sad panda 🐼 because we fixed it — Now the outgoing webhook response payload includes a `thread_ts` attribute so you know if the message is triggered in a thread!

## August {#august}

* Batten down the hatches! Further secure your internal integrations by restricting token use of Web API methods to specific IP addresses you trust: IP allowlisting is here.
* Improve your custom unfurling flows with enhancements to authenticated unfurls and `chat.unfurl`.
* No longer the sole domain of slash commands and interactive messages, now apps can emit their own ghostly ephemeral messages with `chat.postEphemeral`.
* _Temporary rollback_: We've reinstated access to the `email` attribute for bot and user tokens. On **August 1, 2017** we proceeded with limiting email access to user tokens with `users:read.email`.
* Our developer preview for a new kind of Slack app based on workspace tokens is _open_. Learn how to work with workspace tokens and about our new Permissions API. Our [announcement](https://medium.com/slack-developer-blog/looking-to-the-future-of-apps-in-slack-c2633df0bcb7) covers the story behind the token.
* With so many token types decorating our platform, this guide to token types has become a necessity.
* Now we allow you to learn more about OAuth permission scopes and methods, events, and token types each supports with this helpful OAuth scope library.

## July {#july}

* Shuttle Slack app installers to the installation flow more swiftly from the Slack Marketplace with a Direct Install URL.
* Our little changelog has its own RSS feed now.
* Buried somewhere in this RTM announcement, we told you about the `latest` field departing from channel objects returned in the long `rtm.start` preamble. Those fields are gone. Turns out we also removed `unread_count_display` and `unread_count` too. If you're suffering from a sense of loss over these unread count fields, please drop us a line. You can still find them in `conversations.info`.
* Your app has a home in Slack. [Read all about it](https://medium.com/slack-developer-blog/giving-apps-a-new-home-in-slack-daa2ba3a75ed)!
* Teams now have the option to limit Slack app installation _only_ to apps listed in the Slack Marketplace.
* We're introducing a unified cursor-based pagination model to many of our Web API methods beginning with but one: now you can drink from `users.list` one delicious sip at a time.

## June {#june}

* Get an event when more members join your User Group or when — uh-oh, it loses members with `subteam_members_changed`.
* Do you work with `presence_change` events in the RTM API? Learn about new ways to subscribe and consolidate presence events here.
* We've compiled a collection of Best Practices around building fantastic Slack app user experiences. Your users will be stoked!
* We've turned a light on for you and your development team: App Blueprints are like recipes for building the internal integrations your team needs to succeed.
* We've corrected a long-standing bug where user or `@channel`\-type mentions in back-tick fenced code blocks would trigger notifications. They won't now.
* We've made very minor improvements to our OAuth-based installation process. You may notice a shifted pixel here and there but no app-facing functionality has changed.
* Just like subscribing to your app's own newsletter: App Events tell the story of your app's lifecycle. Learn when your app is uninstalled with `app_uninstalled`, or when user and bot tokens are revoked with `tokens_revoked`. Pause and resume activity when teams migrate to an Enterprise organization with `grid_migration_started` and `grid_migration_finished`.

## May {#may}

* We _undocumented_ the mysterious `user_id_mapping_old_to_new` field described in the Enterprise organization documentation. It doesn't actually exist and never has, oops!
* Slackbot wants to help spread the word about your cool Slack app. Add a little HTML to your site and we'll suggest your app when your links are mentioned.
* You'll soon see fewer `message.channel_join` and `message.channel_leave` message subtype events in the Events API and RTM API. Instead, you'll find these new refreshingly direct and informative events: `member_joined_channel` and `member_left_channel`.

## April {#april}

* The old `channels.list` API method has a new parameter: `exclude_members`. Some teams are so big and some channels have so many members that listing them all in a single API response along with every other channel is just outright impractical. Cull unneeded data easily accessed with `conversations.info` by excluding `members` fields.
* We'd like you to stop using `rtm.start` and start using `rtm.connect` instead. `rtm.connect` boots quickly and works well with the most gigantic teams and enterprises of the galaxy.
* It's spring cleaning time for email. We're winding down the grandfathering introduced for apps using `users:read` created before **January 4th, 2017**. After **August 1st, 2017** your apps must request `users:read.email` to gain that access. See this post for more detail. This retirement has been delayed with no date yet rescheduled.
* Observe the custom status of team members with `users.profile.get`. Update a user's custom status with `users.profile.set`.
* More ways to make messages interactive than before: introducing message menus. Define your options statically, dynamically, even _personally_ — or use our handy conversation, channel, and user pickers. Don't forget your field guide.

## March {#march}

* As with the humans operating them, user objects change over time. With the new `updated` field, decisively learn last time a user object transformed. Look for it in methods including (but not limited to) `users.list` and `users.info`. It's an integer value depicting [seconds since the epoch](https://en.wikipedia.org/wiki/Unix_time).
* We're introducing new, multimedia ways for bots and apps to express themselves in the Slack Marketplace. Follow our new guidelines to make a great impression with potential installers.
* Provide users posting links with all the context and interactivity they need, right in Slack. Introducing Slack app unfurling. Here's the [announcement](https://medium.com/@SlackAPI/ebcad7c531f0#.dp0ehltqg)!
* Beginning **March 9, 2017**, events transmitted via the Events API will include `event_id` and `event_time` fields. `event_id` is globally unique across all teams while the `event_time` is when the event dispatched, in integer-based epoch time. Use these fields as you like, but there's nothing you need to do to prepare for this eventuality.
* We made it easier to create and manage your Slack apps. And if you're building internal integrations for your own team, there's a better way to install your app without worrying about the OAuths. Check it out.
* Looking for custom integrations? They're documented as legacy now. They still work like you're used to but we'd prefer you built your internal integrations as part of a Slack app instead.

## February {#february}

* Minor field changes coming to `channels.history` file messages and `skype` user profile fields.

## January {#january}

* You have the tools and the talent — now you have the opportunity: develop for Slack Enterprise orgs. Here's [the announcement](https://medium.com/@SlackAPI/148185a609f2) for the suits.
* Now your app can read, write, and party with message threads. Rolling out to teams over the next few days, message threads are a perfect place to tuck your wonderful workflows. Here's [our announcement](https://medium.com/@SlackAPI/cd272a42924f#.tn0geq5bf).
* This new year's resolution is a minor slash command revolution: a backwards-compatible, familiar, and decisive means to resolve user IDs, channel IDs, and links from references in slash command invocations.

**Tags:**

* [Compilation](/changelog/tags/compilation)
