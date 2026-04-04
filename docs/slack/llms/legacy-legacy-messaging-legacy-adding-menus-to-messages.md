Source: https://docs.slack.dev/legacy/legacy-messaging/legacy-adding-menus-to-messages

# Legacy adding menus to messages

Help users make clear, concise decisions by providing a menu of options within messages.

Message menus build on our interactive message framework allowing your Slack app to provide more expansive and evolutionary selections than previously possible.

![Triforce Project PM](data:image/png;base64,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)

[Message buttons](/legacy/legacy-messaging/legacy-message-buttons) empower limited and precise workflows within Slack conversations. Every one wants to click those tender buttons.

There's a new way to promote more nuanced decision-making.

Instead of buttons, users encounter drop downs, each containing a series of options: perhaps a list of fellow members, a list of Slack channels, or a list of actions you provide while creating the message. Message menus can even be dynamically populated with options based on your server's response.

## Prerequisite knowledge and experience required {#prerequisites}

To create messages with message menus and respond to user selections, you'll need a Slack app set up with a functional interactive message Request URL.

This guide assumes that you're already familiar with posting messages to Slack, whether via [`chat.postMessage`](/reference/methods/chat.postMessage), [`chat.postEphemeral`](/reference/methods/chat.postEphemeral), [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks), or in response to [slash command invocations](/interactivity/implementing-slash-commands).

We also assume you're already familiar with adding [message formatting](/messaging/formatting-message-text) and [message attachments](/messaging/formatting-message-text#attachments) to your messages.

Building message menus and responding to user interaction builds on patterns already established with [interactive messages](/legacy/legacy-messaging/legacy-making-messages-interactive) and [message buttons](/legacy/legacy-messaging/legacy-message-buttons). These three documents form a voltronic gestalt.

## Interactive message invocation pattern {#review}

There's more to it than this, but here's a recap of how [interactive messages](/legacy/legacy-messaging/legacy-making-messages-interactive) work.

1. Post a message containing one or more `attachments` containing one or more interactive elements
2. Users click a button or select an option from a menu
3. A request is sent to your registered Request URL containing all the context you need to understand: who clicked it, which option they clicked, which message `callback_id` was associated with the message, and the original message inciting the selection
4. You respond to your Request URL's invocation with a message to replace the original, and/or a new ephemeral message, and/or you utilize the invocation's `response_url` to update the original message out of band for a limited time.

This pattern doesn't occur in a vacuum — often you will coalesce the simultaneous option selection of multiple members interacting with one or (possibly many) more messages.

Interactive messages are an evolving narrative, where one message may be all it takes to complete a workflow. Or that one message may become a chain of many messages, progressively evolving to suit the goal. Or that one message may be continuously destroyed and rebuilt again anew, with new options, new goals, new ways to discover the self.

## Building basic menus {#simple_menu}

The most basic kind of message menu is one where your app provides a static set of options to select from.

For a comprehensive accounting of all the fields related to interactive messages, please consult the dedicated [field guide](/legacy/legacy-messaging/legacy-interactive-message-field-guide).

### Attach a drop down of predetermined actions {#attach-simple-menu}

![A short list of selectable options&quot; style=&quot;max-width: 400px;](data:image/png;base64,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)

If providing three or more pre-determined options, this is the best approach to making your message interactive.

For example, this message presents users with a menu of possible (but increasingly dangerous) games to play:

```json
{    "text": "Would you like to play a game?",    "response_type": "in_channel",    "attachments": [        {            "text": "Choose a game to play",            "fallback": "If you could read this message, you'd be choosing something fun to do right now.",            "color": "#3AA3E3",            "attachment_type": "default",            "callback_id": "game_selection",            "actions": [                {                    "name": "games_list",                    "text": "Pick a game...",                    "type": "select",                    "options": [                        {                            "text": "Hearts",                            "value": "hearts"                        },                        {                            "text": "Bridge",                            "value": "bridge"                        },                        {                            "text": "Checkers",                            "value": "checkers"                        },                        {                            "text": "Chess",                            "value": "chess"                        },                        {                            "text": "Poker",                            "value": "poker"                        },                        {                            "text": "Falken's Maze",                            "value": "maze"                        },                        {                            "text": "Global Thermonuclear War",                            "value": "war"                        }                    ]                }            ]        }    ]}
```text

This message structure is very similar to those used in [message buttons](/legacy/legacy-messaging/legacy-message-buttons).

They key difference is that instead of each button being a distinct _action_, a message menu is represented as a single action with multiple _options_.

#### Request URL response {#request-url-response}

As users select options from the provided drop down, your Request URL will receive invocations similar to those found in message buttons. You'll receive a HTTP POST with a `payload` body parameter containing a string-encoded JSON object. Decode the JSON to your programming language's native hash/object data structure to evaluate the action.

Continuing with the above example, if a user had selected the `Falken's Maze` menu option, Slack would issue a request to your configured Request URL indicating that the `games_list` select dialog was used to choose the `maze` option.

Here's example JSON sent in this scenario, already decoded from the `payload` parameter:

```json
{    "type": "interactive_message",    "actions": [        {            "name": "games_list",            "selected_options": [                {                    "value": "maze"                }            ]        }    ],    "callback_id": "game_selection",    "team": {        "id": "T012AB0A1",        "domain": "pocket-calculator"    },    "channel": {        "id": "C012AB3CD",        "name": "general"    },    "user": {        "id": "U012A1BCD",        "name": "muzik"    },    "action_ts": "1481579588.685999",    "message_ts": "1481579582.000003",    "attachment_id": "1",    "token": "verification_token_string",    "original_message": {        "text": "Pick a game...",        "bot_id": "B08BCU62D",        "attachments": [            {                "callback_id": "game_selection",                "fallback": "Upgrade your Slack client to use messages like these.",                "id": 1,                "color": "3AA3E3",                "actions": [                    {                        "name": "games_list",                        "text": "Pick a game...",                        "type": "select",                        "options": [                            {                                "text": "Chess",                                "value": "chess"                            },                            {                                "text": "Falken's Maze",                                "value": "maze"                            },                            {                                "text": "Global Thermonuclear War",                                "value": "war"                            }                        ]                    }                ]            }        ],        "type": "message",        "subtype": "bot_message",        "ts": "1481579582.000003"    },    "response_url": "https://hooks.slack.com/actions/T012AB0A1/1234567890/JpmK0yzoZ5eRiqfeduTBYXWQ",    "trigger_id": "13345224609.738474920.8088930838d88f008e0"}
```text

We have exhaustive detail on these fields in the [field guide](/legacy/legacy-messaging/legacy-interactive-message-field-guide#action_payload), but here are some highlights:

You'll find an `original_message` attached for those of you that like to re-use message bodies and don't keep them in memory. `original_message` is not included when referring to an ephemeral message, and only contains attachment data when working with a [link unfurl](/messaging/unfurling-links-in-messages) interactive message.

There's also the `callback_id`, helping identify this specific instance of interaction, along with context around the `team` and `channel` this happened in and the `user` invoking this action. You know to use the `token` value to [validate this inbound request](/legacy/legacy-messaging/legacy-making-messages-interactive#validating_tokens) comes from Slack.

So let's focus on what's new and relevant in the top-level `actions` array.

##### Invoked message menu actions {#invoked-message-menu-actions}

* `name` - the string you provided as the name of this message menu. Like `games_list` used above.
* `selected_options` - an array of option value hashes selected by the user from this message menu. The example above shows a single select option `value` set to `maze`, but it could have been `war` or `chess`. At this time only a single option can be selected by the user or delivered to your app.

After receiving a Request URL invocation, your response pattern remains the same as message buttons: respond directly to the message with another (adding a new message, replacing the original, or delivering something more ephemeral) and/or use the `response_url` and perhaps [`chat.update`](/reference/methods/chat.update) to deliver further interactions.

### Allow users to select from a list of members {#menu_team_members}

![A list of members to select from](/assets/images/message_menus_users-6a168ef5b8467eafb2d612b0beb476d5.png)

It's easy to populate a message menu with a list of a members to select from. Slack will even populate the user list client-side, so your app doesn't even need access to a related OAuth scope.

When users make selections, your Request URL receives any selected user's User ID.

The magic begins by specifying `users` as your action's `data_source`:

Here's a demonstrative example:

```json
{    "text": "I hope the tour went well, Mr. Wonka.",    "response_type": "in_channel",    "attachments": [        {            "text": "Who wins the lifetime supply of chocolate?",            "fallback": "You could be telling the computer exactly what it can do with a lifetime supply of chocolate.",            "color": "#3AA3E3",            "attachment_type": "default",            "callback_id": "select_simple_1234",            "actions": [                {                    "name": "winners_list",                    "text": "Who should win?",                    "type": "select",                    "data_source": "users"                }            ]        }    ]}
```text

### Let users choose one of their workspace's channels {#menu_channels}

![A list of channels](/assets/images/message_menus_channels-3cebe86437dbd860e8a9f2ee53536347.png)

You can also provide a message menu of channels. You don't need the associated scopes to use this approach. Your Request URL will receive only the selected channel's ID.

Users will only be able to select from public channels on their workspace.

Specify `channels` as your action's `data_source` like so:

```json
{    "text": "It's time to nominate the channel of the week",    "response_type": "in_channel",    "attachments": [        {            "fallback": "Upgrade your Slack client to use messages like these.",            "color": "#3AA3E3",            "attachment_type": "default",            "callback_id": "select_simple_1234",            "actions": [                {                    "name": "channels_list",                    "text": "Which channel changed your life this week?",                    "type": "select",                    "data_source": "channels"                }            ]        }    ]}
```text

### Let users choose one of their conversations {#menu_conversations}

Chatter occurs in more that just channels. A user might want to choose from the full breadth of their productive conversations

Show a list of conversations, tailored to each user seeing it by providing `conversations` as your action's `data_source`:

```json
{    "text": "Let's get a productive conversation going",    "response_type": "in_channel",    "attachments": [        {            "fallback": "Upgrade your Slack client to use messages like these.",            "color": "#3AA3E3",            "attachment_type": "default",            "callback_id": "conversations_123",            "actions": [                {                    "name": "conversations_list",                    "text": "Who did you talk to last?",                    "type": "select",                    "data_source": "conversations"                }            ]        }    ]}
```text

### Conversation, channel, and user Request URL invocations {#conversation-invocations}

When a workspace member selects an option from the `conversations`, `channels`, or `users` dropdown, your Request URL will receive the familiar Request URL invocation. Populated once more with `selected_options` field, containing an array of selected values.

In the example below, the user selected a specific workspace's `#general` channel. But you won't know that just from the action response. You'll only have the channel's ID — if you need more info about it, use [`conversations.info`](/reference/methods/conversations.info) if you have the proper permissions.

```json
{        "type": "interactive_message",        "actions": [            {                "name": "channels_list",                "selected_options": [                    {                    "value": "C012AB3CD"                    }                ]            }        ],        "callback_id": "select_simple_1234",        "team": {            "id": "T012AB0A1",            "domain": "pocket-calculator"        },        "channel": {            "id": "C012AB3CD",            "name": "general"        },        "user": {            "id": "U012A1BCD",            "name": "musik"        },        "action_ts": "1481579588.685999",        "message_ts": "1481579582.000003",        "attachment_id": "1",        "token": "iUeRJkkRC9RMMvSRTd8gdq2m",        "original_message": {                "text": "It's time to nominate the channel of the week",                "bot_id": "B08BCU62D",                "attachments": [                    {                       "callback_id": "select_simple_1234",                       "fallback": "Upgrade your Slack client to use messages like these.",                       "id": 1,                       "color": "3AA3E3",                       "actions": [                           {                               "id": "1",                               "name": "channels_list",                               "text": "Which channel changed your life this week?",                               "type": "select",                               "data_source": "channels"                           }                        ]                    }                ],                "type": "message",                "subtype": "bot_message",                "ts": "1481579582.000003"        },        "response_url": "https://hooks.slack.com/actions/T012AB0A1/123456789/JpmK0yzoZDeRiqfeduTBYXWQ",        "trigger_id": "13345224609.738474920.8088930838d88f008e0"}
```text

As with predetermined option selection, look to the `actions` array for a single named selection. Inside its `selected_options` array you'll find the `value` field containing the relevant conversation, channel, or user.

## Populate message menus dynamically {#menu_dynamic}

Sometimes you don't want to provide a list of static options but want them to change dynamically based on the user, channel, or a previous interaction. Perhaps you want to offer the latest possible values, or personalize every little option for the engaging user. You can do all these things with dynamic message menus.

Once you've configured your External Suggestions URL in your app's interactive message settings, create a message with an attachment action set with a `data_source` set to `external`.

When the posted message's drop down is opened, we'll send a request to your specified URL, expecting a HTTP 200 OK response back along with an `application/json` post body.

When users enter a externally-loaded menu's typeahead mode, requests will be sent to your External Suggestions URL for each character or change. If you prefer fewer requests or more fully ideated queries, use the `min_query_length` attribute to tell Slack the fewest number of typed characters required before dispatch. Yes, this is one way to provide guided text-entry — you'll receive a `value` field with the user's current query.

Include an `options` or `option_groups` array attribute as described in the [field guide](/legacy/legacy-messaging/legacy-interactive-message-field-guide#option_fields). These can be formatted and configured just like pre-populated options in the static example above.

A maximum of 100 options may be included.

Here's a menu to help you find some bugs.

```json
{    "text": "What's bugging you?",    "response_type": "in_channel",    "attachments": [        {            "fallback": "Upgrade your Slack client to use messages like these.",            "color": "3AA3E3",            "attachment_type": "default",            "callback_id": "select_remote_1234",            "actions": [                {                    "name": "bugs_list",                    "text": "Which random bug do you want to resolve?",                    "type": "select",                    "data_source": "external",                    "min_query_length": 3,                }            ]        }    ]}
```text

We've set up our external URL to return a list of options containing a few bugs to choose from. Options returned here will be passed to the user, so you can do some intelligent filtering and ordering on your side.

```json
{    "options": [        {            "text": "Unexpected sentience",            "value": "AI-2323"        },        {            "text": "Bot biased toward other bots",            "value": "SUPPORT-42"        },        {            "text": "Bot broke my toaster",            "value": "IOT-75"        }    ]}
```text

Send that `applications/json` response when your External Suggestions URL receives a request similar to this one, giving you needed context to customize your response:

Your list of options may also include the `selected_options` structure [detailed above](#preselect_option). Selected options do not automatically persist, so if your receive another options load request, you'll want to include `selected_options` each time.

#### Options Load URL {#options-load-url}

When Slack sends requests to your Options Load URL, it sends you context about the workspace, channel, and user. Use this data to customize the response directly for the user interacting with the menu. If the workspace member uses typeahead, you'll also receive a `value` attribute with the current query.

```json
{    "name": "bugs_list",    "value": "bot",    "callback_id": "select_remote_1234",    "type": "interactive_message",    "team": {        "id": "T012AB0A1",        "domain": "pocket-calculator"    },    "channel": {        "id": "C012AB3CD",        "name": "general"    },    "user": {        "id": "U012A1BCJ",        "name": "bugcatcher"    },    "action_ts": "1481670445.010908",    "message_ts": "1481670439.000007",    "attachment_id": "1",    "token": "verification_token_string"}
```text

For a comprehensive accounting of all the fields related to interactive messages, please consult the dedicated [field guide](/legacy/legacy-messaging/legacy-interactive-message-field-guide#options_load_url).

As with all of these interactions, your server's response time is important. With dynamically loaded menus, this is even more true — you don't want to make users wait to order from your message menu and there's no chance to use `response_url`.

### Grouping options {#grouping-options}

Whether you're pre-populating options or loading them remotely, you can nestle them categorically to make navigation easier and typeahead more expressive. Instead of providing an `options` field, provide `option_groups`.

You'll find [option groups](/legacy/legacy-messaging/legacy-interactive-message-field-guide#option_groups) in the field guide but really there are only two attributes:

* `text` - the words used to identify the "category". Can even include
* `options` - an array of [option objects](/legacy/legacy-messaging/legacy-interactive-message-field-guide#option_fields)

In the example below, we nest bugs by category.

```json
{    "option_groups": [        {            "text": "Doggone bot antics",            "options": [                    {                        "text": "Unexpected sentience",                        "value": "AI-2323"                    },                    {                        "text": "Bot biased toward other bots",                        "value": "SUPPORT-42"                    },                    {                        "text": "Bot broke my toaster",                        "value": "IOT-75"                    }            ]        },        {            "text": "Human error",            "options": [                {                    "text": "Not Penny's boat",                    "value": "LOST-7172"                },                {                    "text": "We built our own CMS",                    "value": "OOPS-1"                }            ]        }    ]}
```text

Nested options are still limited to a total of 100 options.

## Preselecting menu options {#preselect_option}

If you have a suggested choice for your particular user, make use of the `selected_options` field to pre-populate the dropdown with what you have in mind while still allowing them to peruse the full menu. This is available for all `data_source` types. At this time, only one selection may be made.

In this example, we preselect `maze` for the `games_list`.

```json
{    "attachments": [        {            "callback_id": "select_simple_1234",            "actions": [                {                    "name": "games_list",                    "text": "Pick a game...",                    "type": "select",                    "options": [                        {                            "text": "Chess",                            "value": "chess"                        },                        {                            "text": "Falken's Maze",                            "value": "maze"                        },                        {                            "text": "Thermonuclear War",                            "value": "war"                        }                    ],                    "selected_options": [                        {                            "text": "Falken's Maze",                            "value": "maze"                        }                    ]                }            ]        }    ]}
```text

The provided `value` must correspond to a value contained within the menu options itself. Here's how that plays out with each menu type:

### Static and dynamic menus {#static-dynamic-menus}

Just make sure the `value` and `text` match an actual option you've provided.

```text
"selected_options": [    {        "text": "Yes! I am a long way from home",        "value": "mogwai"    }]
```text

### Channels and conversations {#channels-conversations}

The provided `value` should be the channel, MPIM, or direct message's ID. Don't worry about providing `text` but if you do make it sensible.

```text
"selected_options": [    {        "text": "#melding",        "value": "C123456"    }]
```text

### Users {#users}

Provide a user's ID as the `value` — they begin with `U` or `W`. We take both. You don't need to provide a `text` value.

```text
"selected_options": [    {        "text": "Mr. Book",        "value": "W123456"    }]
```text

## Best practices are on the menu {#best_practices}

These message menu best practices should be considered with our [message guidelines](/surfaces/app-design#messaging).

* If your message only needs to provide one or two interaction options, use [message buttons](/legacy/legacy-messaging/legacy-message-buttons) to make those choices distinct and encourage decisiveness.
* You can mix message buttons and message menus within the same message by including multiple attachments. Wow your friends and colleagues with ancient inputs made new again.
* Respond quickly! We'll timeout a request to your Request URL or Option Load URL after 3 seconds. If it takes you longer to build a response or decide what to do, send a HTTP 200 OK and use other means to progress the interaction.
