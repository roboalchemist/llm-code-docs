Source: https://docs.slack.dev/changelog/2019/12/31/compilation

# 2019 shortform changelog entries

December 31, 2019

## December {#december}

* We didn't set out to produce almost 700 pages of documentation but you can search it all now on api.slack.com/search.
* Slack apps may now be submitted to the Slack Marketplace.
* Place useful limits on multi-select menus using the new `max_selected_items` parameter.

## November {#november}

* Your App home is going mobile — you can now interact with an app's Home tab from iOS and Android clients. We recently published a new App home tutorial to help you build, or you can read the Home tab docs.
* Help users make informed decisions when considering your app by listing the languages it's fluent in and any pricing model that applies to it. You can provide this info as part of the Slack Marketplace submission process.
* You can now use Block Kit radio buttons in modals, in addition to Home tabs.
* We're removing the misleading and undocumented `guest_channels` field from user profile objects belonging to guest users. The `users.conversations` method is an accurate way to query the channels a guest user belongs to.
* Slack has but one REST API, the SCIM API, and it's now fully standards-compliant with SCIM 1.1 when using the HTTP PATCH method to update user records.

## October {#october}

* Your apps have always needed a better home, right in Slack. Now apps with bot users can use Block Kit with a new surface called the _Home tab_. Learn how to use this new space to provide users with a persistent place for dynamic experiences.
* Radio is alive and well in Block Kit. Obtain a singular choice from users using our new radio button elements.
* Craft a workspace faster than a cup of coffee and fill it with users, admins, and owners. Check out the APIs for creating workspaces and managing users, now available for Enterprise organizations.
* Slack apps can act independently of a user token. Build a bot user powered by only the specific permissions it needs. Check out our open beta for newly created Slack apps.

## September {#september}

* Announcing new pastures for Block Kit beyond messaging: trigger dynamic modal interfaces to provide linked user experiences invoked from messages, actions, or slash commands.
* Embrace procrastination — allow users choose from multiple options in interactive workflows. Use new multi-select menus in all your Block Kit surfaces.
* This autumn or soon thereafter, users will begin editing messages using a WYSIWYG (_what you see is what you get_) interface. When they do, their posted messages will appear slightly different throughout our APIs.

## August {#august}

* Two new events, `channel_shared` and `channel_unshared`, now notify your app when a channel is shared or unshared.
* A single admin app can now approve or restrict other app installs across an entire Enterprise org. Get a little meta, and a lot more time-efficient, with the APIs for app management.
* As previously announced, `pins.add` will stop accepting file and file comment IDs beginning **August 22, 2019**. Similarly, `reactions.add` will no longer allow file and file comment parameters. Nowadays, apps and users pin & react to messages _about_ files instead.
* On **March 4, 2020**, we'll require all apps, custom integrations, bots, and users communicating with Slack to use TLS version `1.2` or higher. There will be a 24 hour test deprecation on **February 19th, 2020**. Read more details on why and how to upgrade.
* Channel names have grown up: instead of a maximum length of 21 characters, channel names may now feature a full 80 character label.

## July {#july}

* Host files wherever you please, while you add, update, remove, share, and unfurl them in Slack. Read up on the new Remote Files API.
* Enterprise org admins may now use the `admin.users.session.reset` method to wipe a user session, logging out a user whose device may have been stolen or compromised.about the new method, as well as the new scope required to use it.

## June {#june}

* Your app may now encounter channels shared between workspaces in an Enterprise org. As a result, it's even more important to use the Conversations API methods to safely handle channels both shared and unshared.
* Using the SCIM API's `GET /Users` or `/Groups` methods? Their `count` parameters will no longer accept values above `1000` beginning **August 30, 2019**.
* As announced previously, the `dnd.teamInfo` method now _requires_ the `users` parameter. An explicit list of `users` helps you, and us, avoid slow API calls.

## May {#may}

* As previously announced, the `files.comments.add` and `files.comments.edit` methods are retiring today. Also, files may no longer be pinned to channels. The `pins.add` method will no longer accept files or file comments beginning **August 22, 2019**.
* Better built-ins. Nifty type hints. Easier RTM event handling. Build for the future with the [new Python SDK V2.0.0](https://github.com/slackapi/python-slackclient), lovingly crafted with Python 3.
* Want to build a Slack app with JavaScript? Use the [Bolt](https://github.com/slackapi/bolt) framework. Effortlessly _bolt_ listeners onto events. Minimize boilerplate to post messages, forming a beautiful _bolt_ of conversational cloth. Leverage TypeScript to autocomplete code faster than a lighting _bolt_. Go ahead, bolt toward [Bolt](https://github.com/slackapi/bolt).

## April {#april}

* Parent messages in a thread will no longer explicitly list their replies. Instead of a large `replies` array containing threaded message replies, we'll provide a lighter-weight list of `reply_users`, plus a `reply_users_count` and the `latest_reply` message. These new fields are already available. We'll remove the `replies` array on **March 31st, 2020**.
* Make your app a better listener with the `app_home_opened` event. When a user enters a conversation with your app, you can trigger a friendly onboarding flow, a whimsical welcome message, or a deep-dive into dialog.
* Retrieve all active incidents, rather than just the most recent one, using version 2.0.0 of the Slack Status API.
* Buttons in message blocks have gained some color. Use the new `style` field to visually compel and alert users.
* We're returning a more descriptive `limit_required` error when you call `users.list` or `channels.list` for teams containing tens of thousands of responses. To avoid the peril of errors entirely, use pagination.

## March {#march}

* Taking a novel approach to pagination, the v5 release of our [Slack SDK for Node.js](https://github.com/slackapi/node-slack-sdk/releases) supports Node v8 LTS and above. It also splits the client into three separately installable packages optimized for speed and bundle size. Work with other languages or frameworks? Browse other tools built for you.
* When querying `dnd.teamInfo`, the `users` argument is required beginning **June 3, 2019**. Future-proof your app by explicitly listing which `users` you wish to see _Do Not Disturb_ settings for.
* Harness a hint of time travel for your app. Schedule messages for delivery at the time of your choosing.
* We're starting to enforce (more firmly) the 5GB file upload limit for workspaces on a Free plan. Some API endpoints will yield tombstoned files with the content redacted.

## February {#february}

* We're retiring the `files.comments.add` and `files.comments.edit` methods on **May 22nd, 2019**.
* We're loosening up limits on dialogs. You can use five extra elements (ten total) and lovingly label them with longer lengths of letters.
* When your exacting maths require the precise number of members party to a particular conversation, use the new `include_num_members` parameter with `conversations.info`.
* Build better messages with Block Kit, a set of building blocks for messages and vast, interactive workflows. And, build messages better with Block Kit Builder.
* We're limiting legacy tester tokens by revoking them when they're left unused for several months. As a pleasant counterpoint, our method testers let you bring your own token now.

## January {#january}

* Apps endure, even when their installing user leaves the team—_as long as_ the app doesn't perform actions on behalf of the installing user. This new behavior rolls out to free, paid, and Enterprise org teams over the next week.
* Conversation objects associated with shared channels now feature a `conversation_host_id` field, indicating the workspace or Enterprise organization that "hosts" the shared channel.
* We're erasing the `shares` attribute from "shared channel" conversation objects. In methods like `conversations.history` and the Events and RTM APIs, enjoy a lighter-weight list of the `shared_team_ids` representing the teams across which the conversation is shared.

**Tags:**

* [Compilation](/changelog/tags/compilation)
