Source: https://docs.slack.dev/changelog/2017-09-the-one-about-usernames

# The one about usernames

September 1, 2017

Slack is phasing out the `@username` artifact in favor of the more expressive and flexible concept of _display names_.

Handles, aliases, call-signs, and usernames — in chat, they all represent the same concept: a way for an individual or entity to indicate a preferred identification noun, in whichever way is appropriate to the apparatus at work.

Users will be even better equipped to present their preferred nomenclature while giving organizations the option to work primarily with so-called _real_ names as suits "the suits."

The transition should be technically "backwards compatible" to you, the developer. But the social ramifications, changes in user behavior, and treatments given in Slack clients will inevitably alter the way your apps approach interpreting, storing, and utilizing the now _deprecated_ `name` field.

As fellow developers, we know you'll have some feelings about the sunset of `@username` considering its historical significance in computing, networking, and digital identity. From mainframes to UNIX to BBSes to IRC, maybe you've used the same name for what seems like centuries.

Fly your freak, geek, or mild-mannered flag proudly by just setting your _display name_ to your preferred `@username`.

## What's changing? {#changing}

It may seem like both everything and nothing is changing.

We've worked to make this transition as seamless and non-breaking as possible, though some unanticipated bugs have turned up here and there.

There are many things we _want_ you to do, but in the short term there is likely _nothing_ you _must_ do.

One [undocumented form](#undocumented_mentions) of user mentioning was temporarily broken but is now repaired. You'll still want to adjust your mentions to the new syntax described below.

Here's a complete accounting of what technically changed in the API. User experience changes are not addressed in this article.

### User objects {#user-objects}

User objects encountered throughout the platform will continue having a `name` (AKA `@username` and sometimes even `user_name` or `username`) field _but_:

* Users will be less likely to manually set their `@username` as it will rarely surface in any part of the Slack product.
* Users created after September 11, 2017 will have their `@username` set for them.
* User objects' `profile` will contain the `display_name` and `display_name_normalized` fields, indicating the user's preferred name.
* `display_name` is _not_ unique and may contain a relatively full gamut of UTF-8 characters. Emoji and a limited range of characters are not allowed.
* Existing users created before September 11, 2017 will have their `display_name` set to their current `name` value.
* Users will begin setting their display names now.

### Mentioning users in messages {#mentioning-users-in-messages}

We're preserving the old ways of mentioning users programmatically for the next year. You may need to adapt your approach if you're using an outdated syntax.

* The user mentioning syntax `<@W123|bronte>` is now deprecated and will eventually be removed. Slack will use the "display name" when rendering all mentions.
* Use the user ID-only form `<@W123>` instead.
* Using `link_names` when posting messages is also deprecated. We'll continue matching `@mentions` with usernames, but for now please mention users with the `<@W123>` user ID format instead.
* When evaluating messages to determine if your user or bot user is mentioned, look for a user ID, not a `username`.
* Bots still have a `username` but we advise you to start thinking of your app's name as your app's _display name_.
* The undocumented approach to mentioning users via the API — `<@username>` — will no longer function after September 12, 2018. Please reference with the user ID format (`<@U123>`) instead.
* Undecorated `@username` mentions posted directly to [RTM API](/legacy/legacy-rtm-api) websockets are no longer interpreted and matched to users — only User ID-based `<@U0123ABC>` mentioning will work. Use `chat.postMessage` or incoming webhooks to post messages with usernames during the deprecation period instead.

Mentioning users in the Slack product itself has also evolved and is more UI-driven than before. See [this Slack help center article](https://slack.com/help/articles/205240127-Mention-a-member) to learn how the Slack product has changed.

### Authoring messages {#authoring-messages}

Authoring messages with [`chat.postMessage`](/reference/methods/chat.postMessage), [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks), and other means is largely unchanged. However:

* Don't provide a `username` in the `channel` field when trying to direct a message to a specific user. Use [`conversations.open`](/reference/methods/conversations.open) to create a direct message and then specify the direct message "channel" ID instead.
* Slack apps and their bot users should not use the `username` field when authoring a message. The username is part of your app's configuration and will not always be settable at runtime.

### Slash commands {#slash-commands}

Slash commands often utilize a `@username` mention provided in free form text by an invoking user. If you pay attention to mentioned usernames, know that:

* You should be using the [_Escape channels, users, and links_](/interactivity/implementing-slash-commands#creating_commands) slash command feature. It will provide you with a response that includes user IDs. You need that to free yourself of the `username` habit.
* We'll send that in the `<@W123|username_like_string>` format when we can, but really you should focus on just the ID portion of the string. `@W123`.

### Channel topics, purposes, and other undocumented tricks {#channel-topics-purposes-and-other-undocumented-tricks}

Slack has been pretty liberal in how it will linkify the strings it encounters in more than just messages. The transition to display names means that:

* A naked `@username` mention in a channel topic, purpose, or custom status will not automatically linkify to the corresponding user and `<@W123>` syntax is not supported.

### Enterprise organizations and Shared Channels {#enterprise-organizations-and-shared-channels}

Any "shared channels" between workspaces, whether in an [Enterprise organization](/enterprise) or using the new [Shared Channels](/apis/slack-connect/) feature set may have multiple users with the same `name`. Use user IDs to more reliably identify and separate user identity across teams.

### Slack user experience {#slack-user-experience}

Much will change in the Slack user experience to accommodate these changes. User behavior may change enough that your application's behavior becomes irrelevant, incongruent, or outdated. Users will begin to expect to see their names rendered as anticipated.

Read this [help center article](https://slack.com/help/articles/205240127-Mention-a-team-member) for the full user experience story.

* Teams still have a setting to favor real names over display names.
* Users may choose whether to favor display names instead.
* The user mentioning experience while composing a message is more interactive.
* Slack will attempt to map a copy and pasted username whenever possible.

## What isn't changing? {#not_changing}

While looking through that laundry list of things that _are_ changing and seeing how short the list of what's _not_ changing is, you may wonder how we claim this change is _mostly_ backwards compatible.

The fundamentals remain:

* The `name` field isn't disappearing yet. It's just becoming less significant and we'll eventually phase it out in a year or so.
* Teams can still indicate whether they are real name-focused or display name-focused.
* Users can still personalize their name's display by setting a display name. It can be decidedly `name`\-like if desired.
* We'll still helpfully translate naked `@username` mentions when we can match them to a specific `name` we have on file, though we can't translate the undocumented `<@username>` convention.
* Users still type `@` to start mentioning another user but user interface hints guide them to select the proper user.
* Your bot and app still have a referenced user identity.

## What happens if I do nothing? {#happens}

In the immediate future, _nothing_ we hope. Your slash commands keep chugging along, your `@mentions` match a corresponding user, and life for you remains just as it was before we announced these changes.

But longer term — within a year — you may notice an eventual decrepitude in how your app addresses users or watches for user mentions.

* A `display_name` and `name` may drift and if you continue addressing a user by `name` eventually that name may fall out of fashion.
* You'll miss out on new features directed toward display names.
* Your app may exhibit unexpected behavior when anticipating uniqueness of username values.

## How do I prepare? {#prepare}

Your apps should really no longer be concerned with usernames or the `name` field. Don't bother storing it. Don't bother using it conversation. Don't introspect on it. Don't use it in a `channel` field.

## Pretend as if the `name` field doesn't exist.

* You should never use `name` as any kind of primary key for a user. It's always been mutable, and we cannot guarantee uniqueness, especially when multiple workspaces collaborate together. Reference user IDs instead, which are unique to specific workspaces.
* When mentioning users, use the user ID `<@W123>` format instead.
* Look for mentions in messages of users or bots in the user ID `<@W123>` format instead of scanning for a `@username`.

### Mapping usernames to user IDs {#mapping}

#### Copy and paste from Slack {#copy-and-paste-from-slack}

We now display user IDs when viewing user profiles within the Slack product. Browse a user's profile and use the control to display and quickly copy and paste a specific user's ID.

#### Using the Web API {#using-the-web-api}

Use the [`users.list`](/reference/methods/users.list) Web API method to map any usernames you may have to user IDs. You'll want to consume the entire user list. When working with large teams, you'll definitely want to use [pagination](/apis/web-api/pagination).

The best way to access `users.list` for your own workspace is by creating a Slack app and request the [`users:read`](/reference/scopes/users.read) permission scope. After installing your app to you workspace, use the OAuth access token to work with `users.list`.

If you had only the usernames `janice`, `teeth`, and `zoot` and wanted their user IDs, you would examine the `users.list` response for matching `name` fields.

Once a match is found, find the `id` field and record it. User IDs commonly begin with `W` or `U`. If you want to maintain a mapping of display names and user IDs, look for the `display_name` listed under `profile` and note the `updated` timestamp indicating the last time the user record was updated.

Here's an example `users.list` response, condensed for brevity.

```json
{    "ok": true,    "members": [        {            "id": "W012A3CDA",            "team_id": "T012AB3C4",            "name": "janice",            "real_name": "Janice",            "profile": {                "real_name": "Egon Spengler",                "display_name": "spengler",                "real_name_normalized": "Egon Spengler",                "display_name_normalized": "spengler",                "team": "T012AB3C4"            },            "updated": 1502138686,        },        {            "id": "W012A3CDB",            "team_id": "T012AB3C4",            "name": "teeth",            "real_name": "Dr. Teeth",            "profile": {                "real_name": "Dr. Teeth",                "display_name": "Dr. Teeth",                "real_name_normalized": "Dr. Teeth",                "display_name_normalized": "Dr. Teeth",                "team": "T012AB3C4"            },            "updated": 1502138686,        },        {            "id": "W012A3CDC",            "team_id": "T012AB3C4",            "name": "zoot",            "real_name": "Zoot",            "profile": {                "real_name": "Zoot",                "display_name": "zoot",                "real_name_normalized": "zoot",                "display_name_normalized": "zoot",                "team": "T012AB3C4"            },            "updated": 1502138686,        }    ],    "cache_ts": 1498777272,    "response_metadata": {        "next_cursor": "dXNlcjpVMEc5V0ZYTlo="    }}
```text

In the `next_cursor`, you're likely to find `animal` and `floyd` too.

### Just one more thing: channels {#just_one_more_thing}

Consider a future where mentioning channels required using only its ID and channel names were not necessarily unique or following the same structure as `#channel` names today

That future will one day arrive. Get ahead of the curve and use channel IDs for all indexing and storage organization.

## When is this happening? {#when}

This all started happening on September 11, 2017. We're gradually untangling legacy support for the `username` field, and expect developers to adopt a pure user ID and `display_name` model going forward.

More detailed plans to follow.

## Tags:

* [Breaking change](/changelog/tags/breaking-change)
* [Announcement](/changelog/tags/announcement)
