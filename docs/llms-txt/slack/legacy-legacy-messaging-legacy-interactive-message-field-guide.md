Source: https://docs.slack.dev/legacy/legacy-messaging/legacy-interactive-message-field-guide

# Legacy interactive message field guide

The [interactive message framework](/legacy/legacy-messaging/legacy-making-messages-interactive) layers atop typical Slack [messages](/messaging) and makes heavy use of [message formatting](/messaging/formatting-message-text) and [attachments](/messaging/formatting-message-text#attachments).

The fields and values and patterns used in the call and response sequence of an evolving workflow are particularly specialized when working with [message menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages) and [message buttons](/legacy/legacy-messaging/legacy-message-buttons).

This guide will help you sort through the various fields encountered and utilized with [interactive messages](/legacy/legacy-messaging/legacy-making-messages-interactive).

Some of these attributes must be adapted to POST parameters when using [`chat.postMessage`](/reference/methods/chat.postMessage).

## Top-level message fields {#message}

Messages act as delivery vehicle for all interactive message experiences. Use them not only when initiating messages, but also when updating or creating evolving workflows.

See the [formatting guide](/messaging/formatting-message-text) for text markup tips.

Field

Type

Description

Required?

`text`

string

The basic text of the message. Only required if the message contains zero attachments.

No

`attachments`

[attachments array](#attachment_fields)

Provide a JSON array of [attachment objects](#attachment_fields). Adds additional components to the message. Messages should contain no more than 20 attachments.

No

`thread_ts`

string

When replying to a parent message, this value is the `ts` value of the parent message to the thread. See [message threading](/messaging#threading) for more context.

`response_type`

string

Expects one of two values: `in_channel` — display the message to all users in the channel where a message button was clicked. Messages sent in response to invoked button actions are set to `in_channel` by default. Or `ephemeral` — display the message only to the user who clicked a message button. Messages sent in response to Slash commands are set to `ephemeral` by default. This field cannot be specified for a brand new message and must be used only in response to the execution of message button action or a slash command response. Once a `response_type` is set, it cannot be changed when updating the message.

No

`replace_original`

boolean

Used only when creating messages in response to a button action invocation. When set to `true`, the inciting message will be replaced by this message you're providing. When `false`, the message you're providing is considered a brand new message.

No

`delete_original`

boolean

Used only when creating messages in response to a button action invocation. When set to `true`, the inciting message will be deleted and if a message is provided, it will be posted as a brand new message.

No

### Attachment fields {#attachment_fields}

Consult the guide to [attaching content to messages](/messaging/formatting-message-text#attachments) for more flavor on working with attachments. Attachments house [message buttons](/legacy/legacy-messaging/legacy-message-buttons).

These fields should be presented as a hash within an array presented in the message's `attachments` field.

Field

Type

Description

Required?

`title`

string

Provide this attachment with a visual header by providing a short string here.

No

`fallback`

string

A plaintext message displayed to users using an interface that does not support attachments or interactive messages. Consider leaving a URL pointing to your service if the potential message actions are representable outside of Slack. Otherwise, let folks know what they are missing.

Yes

`callback_id`

string

The provided string will act as a unique identifier for the collection of buttons within the attachment. It will be sent back to your message button action URL with each invoked action. This field is required when the attachment contains message buttons. It is key to identifying the interaction you're working with.

Yes

`color`

string

Used to visually distinguish an attachment from other messages. Accepts hex values and a few named colors as documented in [attaching content to messages](/messaging/formatting-message-text#attachments). Use sparingly and according to [best practices](/surfaces/app-design#messaging).

No

`actions`

[action array](#action_fields)

A collection of [actions](#action_fields) (buttons or menus) to include in the attachment. Required when using message buttons or message menus. A maximum of 5 actions per attachment may be provided.

Yes

`attachment_type`

string

Even for message menus, remains the default value of `default`.

No

### Message action fields {#action_fields}

The actions you provide will be rendered as message buttons or menus to users.

Be sure and consult our [best practices](/surfaces/app-design#messaging) and storyboard your button interactions.

These fields should be provided as a JSON hash within an array as part of an `attachment` definition defined in the `attachments` field of a message ([see above](#attachment_fields)).

Field

Type

Description

Required?

`name`

string

Provide a string to give this specific action a name. The name will be returned to your Action URL along with the message's `callback_id` when this action is invoked. Use it to identify this particular response path. **If multiple actions share the same name, only one of them can be in a triggered state.**

Yes

`text`

string

The user-facing label for the message button or menu representing this action. Cannot contain markup. Best to keep these short and decisive. Use a maximum of 30 characters or so for best results across form factors.

Yes

`type`

string

Provide `button` when this action is a message button or provide `select` when the action is a message menu.

Yes

`value`

string

Provide a string identifying this specific action. It will be sent to your action URL along with the `name` and attachment's `callback_id`. If providing multiple actions with the same name, `value` can be strategically used to differentiate intent. Your value may contain up to 2000 characters.

No

`confirm`

[confirmation hash](#confirmation_fields)

If you provide a JSON hash of [confirmation fields](#confirmation_fields), your button or menu will pop up a dialog with your indicated text and choices, giving them one last chance to avoid a destructive action or other undesired outcome.

No

`style`

string

Used only with message buttons, this decorates buttons with extra visual importance, which is especially useful when providing logical default action or highlighting a destructive activity.`default`—Yes, it's the default.`primary`—Use this sparingly, when the button represents a key action to accomplish. You should probably only ever have one primary button within a set.`danger`—Use this when the consequence of the button click will result in the destruction of something, like a piece of data stored on your servers. Use even more sparingly than `primary`.

No

`options`

array

Used only with message menus. The individual options to appear in this menu, provided as an array of [option fields](#option_fields). Required when `data_source` is `static` or otherwise unspecified. A maximum of 100 options can be provided in each menu.`[{"text":"<#C9A145GH3>", "value":"C9A145GH3"}]`

No

`option_groups`

array

Used only with message menus. An alternate, semi-hierarchal way to list available options. Provide an array of [option group definitions](#option_groups). This replaces and supersedes the `options` array.

No

`data_source`

string

Accepts `static`, `users`, `channels`, `conversations`, or `external`. Our clever default behavior is `default`, which means the menu's options are provided directly in the posted message under `options`. Defaults to `static`. Example: "channels"

No

`selected_options`

[array of option\_fields](#option_fields)

If provided, the first element of this array will be set as the pre-selected option for this menu. Any additional elements will be ignored. Example: `[{"text":"<#C9A145GH3>", "value":"C9A145GH3"}]` The selected option's `value` field is contextual based on menu type and is always required:For menus of type `static` (the default) this should be in the list of options included in the action.For menus of type `users`, `channels`, or `conversations`, this should be a valid ID of the corresponding type.For menus of type `external` this can be any value, up to a couple thousand characters.

No

`min_query_length`

integer

Only applies when `data_source` is set to `external`. If present, Slack will wait till the specified number of characters are entered before sending a request to your app's external suggestions API endpoint. Defaults to `1`.

No

### Confirmation fields {#confirmation_fields}

Protect users from destructive actions or particularly distinguished decisions by asking them to confirm their button click one more time. Use confirmation dialogs with care.

These fields should be presented as a JSON hash buried deep within the `confirm` field of an `action` within the `actions` array that's also part of an attachment that's inside the `attachments` array field of a message.

Example:

```text
"confirm": {    "title": "Are you sure?",    "text": "Wouldn't you prefer a good game of chess?",    "ok_text": "Yes",    "dismiss_text": "No"}
```text

Field

Type

Description

Required?

`title`

string

Title the pop up window. Please be brief.

No

`text`

string

Describe in detail the consequences of the action and contextualize your button text choices. Use a maximum of 30 characters or so for best results across form factors.

Yes

`ok_text`

string

The text label for the button to continue with an action. Keep it short. Defaults to `Okay`.

No

`dismiss_text`

string

The text label for the button to cancel the action. Keep it short. Defaults to `Cancel`.

No

### Option fields to place within message menu actions {#option_fields}

A collection of option fields. Used in `static` and `external` [message menu](/legacy/legacy-messaging/legacy-adding-menus-to-messages) data types.

The `value` is especially important when used in `selected_options` and must match one of the previously provided `options`.

Example in context:

```json
{    "options": [        {            "text": "Barren Realms Elite",            "value": "barren_realms_elite"        },        {            "text": "Legend of the Red Dragon",            "value": "legend_of_the_red_dragon"        },        {            "text": "Solar Realms Elite",            "value": "solar_realms_elite"        },        {            "text": "Tradewars 2002",            "value": "tradewars_2002"        }    ]}
```text

Field

Type

Description

Required?

`text`

string

A short, user-facing string to label this option to users. Use a maximum of 30 characters or so for best results across, you guessed it, form factors.

Yes

`value`

string

A short string that identifies this particular option to your application. It will be sent to your Action URL when this option is selected. While there's no limit to the value of your Slack app, this `value` may contain up to only 2000 characters.

Yes

`description`

string

A user-facing string that provides more details about this option. Also should contain up to 30 characters.

No

### Option groups to place within message menu actions {#option_groups}

Options groups are a set of 100 options divided into groups. They can be used with `static` or `external` [message menu](/legacy/legacy-messaging/legacy-adding-menus-to-messages) data types.

Example in context:

```json
{    "option_groups": [        {            "text": "Doggone bot antics",            "options": [                    {                        "text": "Unexpected sentience",                        "value": "AI-2323"                    },                    {                        "text": "Bot biased toward other bots",                        "value": "SUPPORT-42"                    },                    {                        "text": "Bot broke my toaster",                        "value": "IOT-75"                    }            ]        },        {            "text": "Human error",            "options": [                {                    "text": "Not Penny's boat",                    "value": "LOST-7172"                },                {                    "text": "We built our own CMS",                    "value": "OOPS-1"                }            ]        }    ]}
```text

Field

Type

Description

Required?

`text`

string

A short, user-facing string to label this option to users

Yes

`options`

string

The individual options to appear in this message menu, provided as an array of [option fields](#option_field). Required when `data_source` is default or otherwise unspecified.

Yes

## Action URL invocation payload {#action_payload}

The key to interactive messages is the noble [message](#message) and its [attachments](#attachment_fields), but the fields delivered to your action URL whenever a button is pressed or a menu option is selected yields all the context your app needs to determine the next step.

Example:

```json
{        "type": "interactive_message",        "actions": [            {                "name": "channels_list",                "selected_options": [                    {                    "value": "C012AB3CD"                    }                ]            }        ],        "callback_id": "select_simple_1234",        "team": {            "id": "T012AB0A1",            "domain": "pocket-calculator"        },        "channel": {            "id": "C012AB3CD",            "name": "general"        },        "user": {            "id": "U012A1BCD",            "name": "musik"        },        "action_ts": "1481579588.685999",        "message_ts": "1481579582.000003",        "attachment_id": "1",        "token": "iUeRJkkRC9RMMvSRTd8gdq2m",        "original_message": {                "text": "It's time to nominate the channel of the week",                "bot_id": "B08BCU62D",                "attachments": [                    {                       "callback_id": "select_simple_1234",                       "fallback": "Upgrade your Slack client to use messages like these.",                       "id": 1,                       "color": "3AA3E3",                       "actions": [                           {                               "id": "1",                               "name": "channels_list",                               "text": "Which channel changed your life this week?",                               "type": "select",                               "data_source": "channels"                           }                        ]                    }                ],                "type": "message",                "subtype": "bot_message",                "ts": "1481579582.000003"        },        "response_url": "https://hooks.slack.com/actions/T012AB0A1/123456789/JpmK0yzoZDeRiqfeduTBYXWQ"}
```text

Field

Type

Description

`type`

string

Use this string to determine where the invoked action originates from, like an `interactive_message` or a `dialog_submission`.

`actions`

action array

An array of actions that were clicked, including the name and value of the actions, as you prepared when creating your message buttons. Though presented as an array, at this time you'll only receive a single action per incoming invocation.`name`—the string correlating to the `name` attribute set in the originating action`value`—the string correlating to the `value` attribute set in the originating action`type`—the string correlating to the `type` attribute set in the originating action

`callback_id`

string

The string you provided in the original message attachment as the `callback_id`. Use this to identify the specific set of actions/buttons originally posed. If the `value` of an action is the answer, `callback_id` is the specific question that was asked. No more than 200 or so characters please.

`team`

team hash

A small set of string attributes about the workspace/team where this action occurred.`id`—A unique identifier for the Slack workspace where the originating message appeared`domain`—The slack.com subdomain of that same Slack workspace, like `watermelonsugar`

`channel`

channel hash

Where it all happened — the user inciting this action clicked a button on a message contained within a channel, and this hash presents attributed about that channel.`id`—A string identifier for the channel housing the originating message. Channel IDs are unique to the workspace they appear within.`name`—The name of the channel the message appeared in, without the leading `#` character.

`user`

user hash

The clicker! The action-invoker! The button-presser! These attributes tell you all about the user who decided to interact your message.`id`—A string identifier for the user invoking the action. Users IDs are unique to the workspace they appear within.`name`—The name of that very same user.

`action_ts`

string

The time when the action occurred, expressed in decimal epoch time, wrapped in a string. Like `"1458170917.164398"`

`message_ts`

string

The time when the message containing the action was posted, expressed in decimal epoch time, wrapped in a string. Like `"1458170917.164398"`

`attachment_id`

string

A 1-indexed identifier for the specific attachment within a message that contained this action. In case you were curious or building messages containing buttons within many attachments.

`token`

string

This is the same string you received when configuring your application for interactive message support, presented to you on an [app details page](https://api.slack.com/apps). Validate this to ensure the request is coming to you from Slack. [See below](#validating_action_url_tokens).

`original_message`

object

A object hash containing JSON expressing the original message that triggered this action. This is especially useful if you don't retain state or need to know the message's `message_ts` for use with [`chat.update`](/reference/methods/chat.update) This value is not provided for ephemeral messages.

`response_url`

string

A string containing a URL, used to respond to this invocation independently from the triggering of your action URL.

## Options Load URL payload {#options_load_url}

When using external menus, Slack will send your Options Load URL a request to retrieve dynamic options for the interfacing user.

The invocation's payload includes important context on the user, workspace, and message you can use to determine which options to provide in response.

Its structure is similar to an Action URL invocation.

Example:

```json
{    "name": "bugs_list",    "value": "bot",    "callback_id": "select_remote_1234",    "type": "interactive_message",    "team": {        "id": "T012AB0A1",        "domain": "pocket-calculator"    },    "channel": {        "id": "C012AB3CD",        "name": "general"    },    "user": {        "id": "U012A1BCJ",        "name": "bugcatcher"    },    "action_ts": "1481670445.010908",    "message_ts": "1481670439.000007",    "attachment_id": "1",    "token": "verification_token_string"}
```text

Field

Type

Description

`name`

string

The name of the message menu being invoked. You named it this for a reason, right?

`value`

string

When users utilize typeahead, their query will be presented here. Use `min_query_length` to customize the minimum amount of typing needed before dispatching an options loading request.

`callback_id`

string

The string you provided in the original message attachment as the `callback_id`. Use this to identify the specific set of actions/buttons originally posed. If the `value` of an action is the answer, `callback_id` is the specific question that was asked. No more than 200 or so characters please.

`type`

string

Indicates the type of interaction inspiring this Options Load request. Only `interactive_message` is currently in use and indicates the request comes from a message menu.

`team`

team hash

A small set of string attributes about the workspace/team where this action occurred.`id`—A unique identifier for the Slack workspace where the originating message appeared`domain`—The slack.com subdomain of that same Slack workspace, like `watermelonsugar`

`channel`

channel hash

Where it all happened — the user inciting this action clicked a button on a message contained within a channel, and this hash presents attributed about that channel.`id`—A string identifier for the channel housing the originating message. Channel IDs are unique to the workspace they appear within.`name`—The name of the channel the message appeared in, without the leading `#` character.

`user`

user hash

The clicker! The action-invoker! The button-presser! These attributes tell you all about the user who decided to interact your message.`id`—A string identifier for the user invoking the action. Users IDs are unique to the workspace they appear within.`name`—The name of that very same user.

`action_ts`

string

The time when the action occurred, expressed in decimal epoch time, wrapped in a string. Like `"1458170917.164398"`

`message_ts`

string

The time when the message containing the action was posted, expressed in decimal epoch time, wrapped in a string. Like `"1458170917.164398"`

`attachment_id`

string

A 1-indexed identifier for the specific attachment within a message that contained this action. In case you were curious or building messages containing buttons within many attachments.

`token`

string

This is the same string you received when configuring your application for interactive message support, presented to you on an [app details page](https://api.slack.com/apps). Validate this to ensure the request is coming to you from Slack. See [below](#validating_action_url_tokens).

* * *

Good luck out in "the field."
