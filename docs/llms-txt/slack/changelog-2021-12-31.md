Source: https://docs.slack.dev/changelog/2021/12/31

# 2021 shortform changelog entries

December 31, 2021

## November {#november}

* If you still use `rtm.connect` or `rtm.start` to connect to Slack, you'll notice that all WebSocket URLs now begin with `wss://wss-primary.slack.com`.
* As previously announced, apps & integrations created after today, **November 30, 2021**, must use `rtm.connect` instead of the deprecated `rtm.start` when connecting to the RTM API.
* Block elements can now utilize the `focus_on_load` field within Block kit messages, which allows you to pick one specific Block element to auto focus on.
* The default Slack Connect invitation type when using `conversations.inviteShared` has changed. Invites are now sent to limit the recipient's actions to only sending messages. The new `external_limited` argument can be used to control which invitation type is sent.

## October {#october}

* We're starting to roll out a new, opt-in beta UI that lets you configure and reconfigure apps using manifests. We're also launching new App Manifest APIs to let you create and manage all your apps programmatically.
* One of our earliest API methods is taking a well-deserved retirement on **September 27, 2022**. For existing apps, `rtm.start` will instead return an equivalent response to `rtm.connect`. Beginning **November 30, 2021**, _newly_ created apps and integrations will only be able to use `rtm.connect`.
* Introducing two API methods that return information about workspaces previously only available in `rtm.start`: `team.billing.info` and `team.preferences.list`.

## September {#september}

* [Slack Developer Tools](https://sdt.builtbyslack.com) now offers the _Platform Guide_, an interactive and introductory education experience for developers interested in learning the basics of building a Slack app _within_ a Slack app.
* Pick a time, any time. The `timepicker` block element is released out of `beta` and available to use in your spiffy apps.
* The `link_shared` event is changing, bringing unfurls—allowing users to see what's in a link—into the message composer.
* In the app approval APIs, you may now distinguish the apps built within your organization from those developed externally—or by Slack—with the `developer_type` field.

## August {#august}

* Legacy workspace apps are now completely retired. They won't function anymore and eventually will be completely removed from our databases. If you run into trouble, [please reach out](https://my.slack.com/help/requests/new).
* The `link_shared` event is changing to bring a little more magic to app unfurls. Read up on the changes, which roll out to free teams on **September 1, 2021**.

## July {#july}

* Modern Sign in with Slack uses the [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) protocol to make signing in with Slack faster and more flexible. Try it today.
* Refresh your access tokens regularly with token rotation, available for opt-in now.
* You can now manage Slack Connect directly for your organization using an app. Read up on the Slack Connect APIs.

## June {#june}

* We gave this dusty place a new coat of paint. Enjoy our updates to api.slack.com to help you navigate, discover, and absorb content more easily. Almost everything should be where you’d expect it.

## May {#may}

* Use manifests to create and manage apps from saveable, shareable, and relatable YAML and JSON. Try out some sample manifests in our new guided tutorials.

## April {#april}

* Apps using classic message attachments have an updated look. Attachment images now have a hover menu and will mostly appear to the right of text. Consider using Block Kit to have more control over how images render.
* We're teaching old blocks new tricks. Starting **April 20, 2021** `input` blocks are now able to exist within messages, allowing you to gather information more swiftly within conversation.

## March {#march}

* Apps may now broadcast messages to users via direct message without handling unnecessary or unsupported conversation and slash commands. Starting **March 29, 2021**, this feature will be _default_ for all _newly-created_ Slack apps. Get started by visiting the App Home tab of your existing Slack apps.
* Newly created private channel IDs now always begin with the letter `C`, just like public channel IDs already do. The Conversations API will tell you whether a conversation is private or not with the `is_private` boolean field.
* Legacy workspace apps, deprecated since October 2018, will officially retire on **August 24, 2021**.

## February {#february}

* The `admin.analytics.getFile` method now returns daily data about conversations in public channels. Members analytics remain available. Explore what's happening on your Enterprise org workspaces.
* Three deprecations take effect today, **February 24,2021**. First, new apps may no longer pass tokens as query parameters. Second, Conversations API methods are now required over their typed counterparts: `channel.*`, `group.*`, `im.*`, and `mpim.*`. Third, event payloads no longer contain full lists of `authed_users` or `authed_teams`—instead, use a new method to learn the full list of authorizations an event is visible to. We know keeping up with best practices for Slack apps is a lot to handle—thank you for allowing us to make the platform better. Keep reading.
* If your app makes use of user emails, be on the lookout for _relay email addresses_. When users sign into Slack via Apple, their emails may appear as anonymized relay addresses. Relatedly, Sign in with Slack won't work with these users.
* Now you can decorate your ephemeral messages requesting authorization with Block Kit using `chat.unfurl`.
* When a user initiates a private channel share via Slack Connect, the channel's ID _changes_. Subscribe to `channel_id_changed` to learn the new IDs for the private channels visible to your app.

## January {#january}

* Updated: Beginning mid-March, links appearing in Block Kit messages shared by apps will unfurl just like other links found in that message.
* Your app can now count its workflow steps with the help of four new events: `workflow_published`, `workflow_unpublished`, `workflow_deleted`, and `workflow_step_deleted`. Use these events to stay informed on workflows—from unpublished to published and back again—that make use of steps powered by your app.
* Socket Mode supplies your app with events and interactive feature payloads over a dynamic WebSocket URL.

**Tags:**

* [Compilation](/changelog/tags/compilation)
