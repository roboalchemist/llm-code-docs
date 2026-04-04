Source: https://docs.slack.dev/changelog/2016/12/31/compilation

# 2016 shortform changelog entries

December 31, 2016

## December {#december}

* Now everyone's bot is present and accounted for. Events API-only bots can toggle online presence by visiting their app management command center. Details worth catching up on: bot user presence.
* We made it so Slack apps have a profile within Slack like humans do — Here's an [announcement tweet](https://twitter.com/SlackAPI/status/809823694683918337).

## November {#november}

* Let's extend a warm welcome to new `app_id` fields now appearing in our APIs. `app_id` is now found in `rtm.start` & `bots.info`. You'll also find `app_id` in the `bot_added` & `bot_changed` events. What's an `app_id`? It's the alphanumeric string found in the URL bar while managing your Slack apps.
* We've added a new OAuth permission scope called `users:read.email`. Apps created after **January 4th, 2017** will need to request this additional scope to gain access to team member `email` fields when using `users.list` and `users.info`. Existing Slack apps with `users:read` are automatically grandfathered to include these fields.
* Now you'll find links to practical tutorials and thoughtful articles displayed beside relevant documentation found here on api.slack.com. Discover new articles or browse them by topic in our new Tutorials hub. Written something great? Tell us about it!
* Our developer relations team has renewed Slack's adoption of key open source tooling: Slack Developer Kits. Discover our Python & node.js SDKs in their new home on our community index.

## October {#october}

* Your elaborate Slack apps are no longer shackled to but just one team member. Now you can invite other team members to be App Collaborators to share in the fun and responsibility. Here's what our web log has to say about it: [Build together with App Collaborators](https://medium.com/@SlackAPI/8162e31800f1)

## September {#september}

* We will soon add an additional `response_metadata` node to our JSON responses; we'll put warnings there first and other useful stuff later. More details are available.
* Newly issued OAuth token strings are longer than they were before, as we informed you about last month. Let us know if this vexes you.
* Now you can use the `users.profile:write` OAuth permission scope to reset and upload profile images using `users.deletePhoto` and `users.setPhoto`.
* We've dramatically improved the process of submitting a Slack App for inclusion in our Slack Marketplace. You'll find a helpful, interactive checklist when first submitting your app. When you're ready to iterate further, you can create a secondary beta application. If a core piece of your app's functionality changes (like requesting new OAuth permission scopes), we'll happily review your app again. [Read all about it](https://medium.com/@SlackAPI/c3234239731#.vwlgf4mwd) on the platform blog.

## August {#august}

* Ever needed to send a user to Slack directly from your app? Deep link and make native Slack clients part of your app's workflow: Open key teams, channels, and conversations. Or, defer to search results using the slack:// URI scheme.
* The character length of token strings is getting longer. Find out how long they'll get and how to future-proof yourself for changes in the future.
* You may encounter an occasional user ID beginning with the letter `W`. We've released a new version of [node-slack-sdk](https://github.com/slackhq/node-slack-sdk) to correct a related bug.
* Introducing the Events API, a new way for Slack apps to receive event types previously available only to the real time messaging API. Subscribe to the events your app needs and have them delivered right to your server as they happen. Build a bot or event-driven app without worrying about websockets, and scale it like a web app. [Read more](https://medium.com/@SlackAPI/d7120470983f) about the Events API in our blog post, [_Subscribe to the Events API_](https://medium.com/@SlackAPI/d7120470983f).

## July {#july}

* Until now, it's been easy to accidentally send messages flush with hundreds of message attachments. We've begun limiting the number of message attachments per message to 100. For approaches like `chat.postMessage`, incoming webhooks, and `chat.update`, and `response_urls` you will receive a `too_many_attachments` error. Unfortunately, we are unable to serve you an error when sending messages as part of a slash command or message buttons invocation response.
* If you're interested in listing your Slack app in the Slack Marketplace, you'll want to review our new Slack Marketplace Agreement and consider our Security Review Process. Find these and other policies in our new Slack App developer policy hub.
* We've corrected a bug where incoming webhooks could post messages in "#general" even 1. if that channel restricts posts and 2. the user owning the webhook was not allowed to post there. This new behavior will only prevent recently created webhooks from posting to restricted "#general" channels, so if your old webhooks are relying on this quirk, they'll be fine for now.

## June {#june}

* Now your applications can read and write defined team profile fields for individual team members. The `users.profile:write` scope allows you to edit fields with `users.profile.set`. The `users.profile:read` scope empowers you to discover available fields with `team.profile.get` and retrieve user profiles with `users.profile.get`.
* Slack apps can now add action-invoking interactive buttons to messages, allowing you to simplify workflows and encourage users to take decisive action from within Slack.
* For better readability, syntax highlighting has been added to code blocks throughout our documentation.
* We've corrected the behavior of `stars.list` so that it only returns stars belonging to the owner of the presented token. The `user` parameter may still be used if the provided user ID belongs to the user utilizing the token.
* Team administrators may now use tokens with the `admin` scope to request information about the billable status of team members using the team.billableInfo API method.
* Now that `bot_id` appears in the real-time messaging API and Web API, you need a better way to look up bot users. Use the new `bots.info` method to query bot/application information by ID. It requires the `users:read` scope.

## May {#may}

* Additional real time messaging API events will begin including the `event_ts` timestamp field later this summer. Find out what to expect.
* Now you can put down a footer on your message attachments. Use the `footer`, `footer_icon`, and `ts` fields to tie content across time and space.
* For the few of you out there using outdated tokens, we've made some changes to authorship behavior when using `chat.postMessage`.
* Error conditions in incoming webhooks are due for an improvement. Read all about how blanket HTTP 500s will become more fine-grained, purposeful error conditions. Shipped on **June 16, 2016**.
* Recently introduced bugs in our iOS & Android apps cause message attachment fields marked as "short" to wrongly render _long_ anyway. Our fixes may take a couple weeks to reach each platform.
* Sign team members into your website, service, or application with Sign in with Slack, based on the same OAuth 2.0 flow used by the Add to Slack button. Read more about it in this [announcement](https://medium.com/slack-developer-blog/introducing-sign-in-with-slack-290949e1c3f5#.hghansb1o).
* We've added two new API methods: `users.identity` works with Sign in with Slack and `auth.revoke` revokes hallway privileges for access tokens. Actually, it revokes the whole token.
* For those who don't know why they should build on Slack: [https://slack.com/developers](https://slack.com/developers)

## April {#april}

* Bot user tokens may now use `files.info` to look up information about files they have access to by virtue of their channel memberships. Also, very helpful for adapting to upcoming file events changes.
* Manage your Slack apps joyously with our updated app edit pages.
* File events are changing in the real time messaging API beginning **May 16th, 2016**. The `files.info` method is soon to be used by bot users.
* As [previously announced](https://medium.com/slack-developer-blog/api-update-new-field-in-api-responses-d23076ea2ef3), we've added a `bot_id` field to relevant API responses. Let us know if you run into any issues.
* We released a family of API methods to create and manage reminders. Meet reminders.list, reminders.info, reminders.add, reminders.delete, and reminders.complete.
* We fixed an unfortunate bug where a team member could inadvertently uninstall a whole Slack App from their team by removing a single incoming webhook associated with that instance of the app.
* Find out what we're building! [Announcing](https://medium.com/slack-developer-blog/the-slack-platform-roadmap-34067b054177) our Platform Roadmap.
* Another way to keep up with the Slack Platform: Install the API News App to receive occasional, important notifications about the platform.
* Your bot users author their own messages, now they can edit them too. Bot user tokens may now use `chat.update`, like humans do.

## March {#march}

* Now `chat.postMessage` will better intuit your intent when you don't explicitly specify the `as_user` parameter. Let us know if we're guessing wrong!
* One day soon our Web API will warn you when something is only slightly wrong with your requests. Read all about [API warnings](https://medium.com/slack-developer-blog/well-wishes-and-warnings-in-the-web-api-489456837220).
* _Be welcoming. Be kind. Look out for each other._ This is the Code of Conduct for the Slack Developer community.
* Now bot users can use methods requiring the `dnd:read` scope, like `dnd.info` and `dnd.teamInfo`. Your bots'll be more polite than a protocol droid!
* Craft your fancy messages in real time with the new Message Builder!
* Users can now rename Bot Users they've installed as Slack Apps. More naming, more claiming. No more terrible twos.
* We _finally_ updated the [slackhq/slack-api-docs](https://github.com/slackhq/slack-api-docs) repository, reflecting recently introduced and quite ancient documentation updates and new features.

## February {#february}

* `reaction_added` & `reaction_removed` events now include an `item_user` field indicating the user that created the original content everyone's raving about.
* Published this changelog you're reading right now. So that you can know about all this stuff. Tell your friends.
* New Web API methods: share files publicly with `files.sharedPublicURL` or make them private again with `files.revokePublicURL`.
* `files.comments.add`, `files.comments.edit`, and `files.comments.delete` are now available to bot users.
* Quickly find the right tools for your project with our new listing of often-used open source libraries.
* The handy test token generator previously found in the Web API documentation now stands proud with its very own page.
* Need help? We have some tips for you.
* api.slack.com's sidebar is now better organized by topic.

## January {#january}

* As of **January 4th, 2016**, authorization headers are now required for most Web API requests involving file URLs. See this doc and [blog post](https://medium.com/slack-developer-blog/important-changes-to-files-in-the-web-api-eb38f2a9c1e7) for more information.
* `url` and `url_download` are no longer part of file objects
* Enjoy our evolving collection of Frequently Asked Questions (and answers!)
* Responses to Incoming Webhook requests now include `channel_id`
* Make sure you're ready before submitting your Slack App for review by following this Slack app checklist.
* Incoming Webhooks documentation updated to better bait best practices and discourage fishy formatting behavior.
* The file object documentation now includes a list of possible file types.

**Tags:**

* [Compilation](/changelog/tags/compilation)
