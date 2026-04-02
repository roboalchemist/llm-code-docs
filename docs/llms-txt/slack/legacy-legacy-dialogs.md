Source: https://docs.slack.dev/legacy/legacy-dialogs

# Legacy dialogs

[Dialogs](/legacy/legacy-dialogs) are designed to help you gather multi-part input from end-users in a structured way; think, for example, of a helpdesk ticket that contains a freeform description of an issue, but also requires some category labels for triage.

They're best used for quick, contextual work: brief tasks that get some benefit from being completed in the context of a channel or conversation.

Users trigger your app's dialogs by clicking on [buttons](/legacy/legacy-messaging/legacy-message-buttons), selecting from [menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages), or invoking [slash commands](/interactivity/implementing-slash-commands). Dialogs contain a variety of guided input types.

### Anatomy of a dialog {#anatomy}

Dialogs appear as a modal window inside Slack. Within that modal, you can add one or many input fields in the form of single line text inputs, text areas, and dropdowns.

![Anatomy of a dialog](data:image/png;base64,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)

The dialog experience focuses squarely on the task at hand. User input is validated before being sent back to your app.

## Implementing dialogs in your app {#implementation}

Dialogs are part of the [interactive framework](/legacy/legacy-messaging/legacy-making-messages-interactive) already powering message menus and buttons.

While many aspects of dialog development are similar, the JSON used to compose a form differs significantly from interactive message components.

To continue interacting with a user after form submission, your app will need to create new messages or utilize the `response_url` associated with the interaction that originally spawned the dialog.

Apps can invoke dialogs when users interact with [slash commands](/interactivity/implementing-slash-commands), [message buttons](/legacy/legacy-messaging/legacy-message-buttons), or [message menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages). Each interaction will include a `trigger_id`, a kind of short-lived pointer to interaction's who, what, where, and when. Form submissions deliver to the Request URL associated with your Slack app.

Dialogs may contain a careful mixture of standard inputs: short text entry, long-form text areas, and drop-down menus. More are on the way.

### Implementation overview {#implementation-overview}

Most developers building and handling dialogs will follow steps similar to these:

1. Build an [interactive message](/legacy/legacy-messaging/legacy-making-messages-interactive), a [slash command](/interactivity/implementing-slash-commands), or both. Dialogs cannot open until users interact with buttons, menus, or slash commands.
2. As users interact or invoke commands, look for a `trigger_id` in the command invocation or interactive action payload.
3. Use [`dialog.open`](/reference/methods/dialog.open) to initiate a dialog in context with the user, providing a `trigger_id` and desired form elements.
4. Once completed, results are sent to your application's interactive Request URL.
5. Your app posts the results to a channel or provides some other submission confirmation message.

### Preparing apps for dialogs {#preparing-apps}

You'll need to create, configure, and install a **Slack app** before getting started with dialogs. Legacy custom integrations are not supported.

At minimum, you must configure the _Interactive Components_ section of [app management](https://api.slack.com/apps). Follow the UI's instructions to provide a Request URL to receive form submissions and other interactions.

If you will use a slash command to initiate dialogs, you will also need to configure your app's slash command.

It is necessary to reinstall your app after adding features and capabilities.

### Interactive triggers {#interactive-triggers}

A dialog cannot be invoked without first being initiated by a message interaction or a slash command. That means a user needs to interact with a message button, message menu, or slash command provided by your app before they can engage with any dialog experiences your app provides.

Slack attaches a `trigger_id` value as part of all interaction payloads you receive, which acts as a pointer to a specific moment in the space-Slack-time continuum where a user interacted with your app.

Here's an example of an [interactive message](/legacy/legacy-messaging/legacy-making-messages-interactive) action containing a `trigger_id`:

```json
{    "actions": [      {        "name": "channels_list",        "selected_options": [          {          "value": "C123ABC456"          }        ]      }    ],    "callback_id": "select_simple_1234",    "team": {      "id": "T0123ABC456",      "domain": "pocket-calculator"    },    "channel": {      "id": "C0123ABC456",      "name": "general"    },    "user": {      "id": "U123ABC456",      "name": "musik"    },    "action_ts": "1481579588.685999",    "message_ts": "1481579582.000003",    "attachment_id": "1",    "token": "iUeRJkkRC9RMMvSRTd8gdq2m",    "response_url": "https://hooks.slack.com/actions/T0123ABC456/123456789/JpmK0yzoZDeRiqfeduTBYXWQ",    "trigger_id": "13345224609.738474920.8088930838d88f008e0"}
```text

And here's an example of a [slash command](/interactivity/implementing-slash-commands) execution containing a `trigger_id`:

```text
token=gIkuvaNzQIHg97ATvDxqgjtOteam_id=T0001team_domain=exampleenterprise_id=E0001enterprise_name=Globular%20Construct%20Incchannel_id=C123ABC456channel_name=testuser_id=U123ABC456user_name=Stevecommand=/weathertext=94070response_url=https://hooks.slack.com/commands/1234/5678trigger_id=13345224609.738474920.8088930838d88f008e0
```text

These interactions are the inciting event to your app opening a dialog. The `trigger_id` is the key to unlock your app's momentary, focused dialog functionality. Because the `trigger_id` expires in 3 seconds, you must exchange the trigger to open a dialog in the given time interval. Using an expired trigger causes the `trigger_expired` error.

Use `dialog.open` soon after receiving a `trigger_id`. Triggers expire 3 seconds after being issued to your app.

## Opening a dialog {#dialog}

To begin a modal dialog, call the [`dialog.open`](/reference/methods/dialog.open) method.

As with all of our Web API methods, `dialog.open` typically takes URL-encoded parameters as arguments. We also support posting JSON.

#### Opening dialogs with JSON {#opening-dialogs-with-json}

The easiest way to open a dialog is to send a POST with a `Content-type` HTTP header set to `application/json` and a raw POST body containing your dialog's JSON presented as the `dialog` argument:

```json
{  "trigger_id": "13345224609.738474920.8088930838d88f008e0",  "dialog": {    "callback_id": "ryde-46e2b0",    "title": "Request a Ride",    "submit_label": "Request",    "notify_on_cancel": true,    "state": "Limo",    "elements": [        {            "type": "text",            "label": "Pickup Location",            "name": "loc_origin"        },        {            "type": "text",            "label": "Dropoff Location",            "name": "loc_destination"        }    ]  }}
```text

See [this section on HTTP POST bodies](/apis/web-api/#post_bodies) for any needed instruction.

#### Opening dialogs with URL-encoded JSON {#opening-dialogs-with-url-encoded-json}

A more complicated way to open dialogs is by sending your carefully crafted JSON as an `application/x-www-form-urlencoded` query parameter.

Similar to [`chat.postMessage`](/reference/methods/chat.postMessage), [`chat.unfurl`](/reference/methods/chat.unfurl), and [`chat.update`](/reference/methods/chat.update) this method also includes a parameter that expects a JSON object encoded with `application/x-www-form-urlencoded`.

A form you might create could be modeled in JSON as:

```json
{    "callback_id": "ryde-46e2b0",    "title": "Request a Ride",    "submit_label": "Request",    "notify_on_cancel": true,    "state": "Limo",    "elements": [        {            "type": "text",            "label": "Pickup Location",            "name": "loc_origin"        },        {            "type": "text",            "label": "Dropoff Location",            "name": "loc_destination"        }    ]}
```text

To prepare that as a HTTP POST to `dialog.open`, you'd optionally minify and then URL encode that JSON to a single string, displayed below as the value for the `dialog` POST body parameter.

```text
POST /api/dialog.openAuthorization: Bearer xoxb-such-and-suchContent-type: application/x-www-form-urlencodedtrigger_id=13345224609.738474920.8088930838d88f008e0&dialog=%7B%22callback_id%22%3A%22ryde-46e2b0%22%2C%22title%22%3A%22Request%20a%20Ride%22%2C%22submit_label%22%3A%22Request%22%2C%22notify_on_cancel%22%3Atrue%2C%22state%22%3A%22Limo%22%2C%22elements%22%3A%5B%7B%22type%22%3A%22text%22%2C%22label%22%3A%22Pickup%20Location%22%2C%22name%22%3A%22loc_origin%22%7D%2C%7B%22type%22%3A%22text%22%2C%22label%22%3A%22Dropoff%20Location%22%2C%22name%22%3A%22loc_destination%22%7D%5D%7D
```text

If all is well, you'll get a clean HTTP 200 OK response with an `application/json` body declaring:

```json
{  "ok": true}
```text

#### Error handling {#error-handling}

If your `dialog` parameter or other aspects of your dialog are invalid, detailed errors are provided to help aid you in correcting them. See [`dialog.open`](/reference/methods/dialog.open) for full detail on error conditions.

### Top-level dialog attributes {#top-level-dialog}

Your dialog is presented to users stylishly with your carefully chosen `title` and curated form `elements`.

By default, all form elements are required. Use the `optional` field to make an element non-mandatory.

Attribute

Type

Description

`title`

String

User-facing title of this entire dialog. 24 characters to work with and it's **required**.

`callback_id`

String

An identifier strictly for you to recognize submissions of this particular instance of a dialog. Use something meaningful to your app. 255 characters maximum. Don't use this ID to reference sensitive data; use the more expansive `state` parameter below for that. **Absolutely required.**

`elements`

Array

Up to **10** form elements are allowed per dialog. See [elements](#elements) below. **Required.**

`state`

String

An optional string that will be echoed back to your app when a user interacts with your dialog. Use it as a pointer to reference sensitive data stored elsewhere.

`submit_label`

String

User-facing string for whichever button-like thing submits the form, depending on form factor. Defaults to `Submit`, localized in whichever language the end user prefers. 48 characters maximum, and may contain only a single word.

`notify_on_cancel`

Boolean

Default is `false`. When set to `true`, we'll notify your request URL whenever there's a user-induced dialog cancellation.

## Dialog form elements {#elements}

The current list of supported form elements includes:

* [`text`](#text_elements) - **Text inputs** work well with concise free-form answers and inputs with unestablished bounds, such as names, email addresses, or ticket titles if your form is used for something like a bug tracker.
* [`textarea`](#textarea_elements) - **Text Areas** are best when the expected answer is long — over 150 characters or so —. It is best for open-ended and qualitative questions.
* [`select`](#select_elements) - **Select menus** are for multiple choice questions, and great for close-ended quantitative questions, such as office locations, priority level, meal preference, etc. The `select` elements may contain static menus or dynamically loaded menus specified with an optional `data_source`.

### Text elements {#text_elements}

Text elements are single-line plain text fields.

By default, all fields are _required_ for a user to fill. Otherwise, the client validation will give the user an error. You can also set each field optional (`"optional": true`) and in this case, empty fields will submit as `null`.

![Dialog text element](data:image/png;base64,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)

## Example:

```json
{  "label": "Email Address",  "name": "email",  "type": "text",  "subtype": "email",  "placeholder": "you@example.com"}
```text

There is an optional `subtype` for the `type: text`. The value of the `subtype` can be set to either `email`, `number`, `tel`, or `url`, where the default is a plain text. Slack will ignore `subtype`s that don't match one of those options.

Setting the `subtype` is useful for mobile Slack clients where it will trigger special keyboards. For example, when a form field expects a phone number, you should use `tel` as a `subtype` so it invokes the numeric keypad.

Adding a `subtype` _does not_ enforce any validation on the field it is added to.

![Dialog text element subtypes](/assets/images/dialog_text_subtypes-a1ba90b89154ef2063f80292c8716c33.png)

#### Text element attributes {#attributes_text_elements}

Element

Type

Description

`label`

String

Label displayed to user. Required. 48 character maximum.

`name`

String

Name of form element. Required. No more than 300 characters.

`type`

String

The type of form element. For a text input, the type is always `text`. Required.

`max_length`

Integer

Maximum input length allowed for element. Up to `150` characters. Defaults to `150`.

`min_length`

Integer

Minimum input length allowed for element. Up to `150` characters. Defaults to `0`.

`optional`

Boolean

Provide `true` when the form element is not required. By default, form elements are _required_.

`hint`

String

Helpful text provided to assist users in answering a question. Up to 150 characters.

`subtype`

String

A subtype for this text input. Accepts `email`, `number`, `tel`, or `url`. In some form factors, optimized input is provided for this subtype.

`value`

String

A default value for this field. Up to 150 characters.

`placeholder`

String

A string displayed as needed to help guide users in completing the element. 150 character maximum.

### Textarea elements {#textarea_elements}

A `textarea` is a multi-line plain text editing control. You've likely encountered these on the world wide web. Use this element if you want a relatively long answer from users. The element UI provides a remaining character count to the `max_length` you have set or the default, 3000.

![Dialog textarea element](data:image/png;base64,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)

Like text, this element supports subtype values of `email`, `number`, `url`, and `tel`.

## An example:

```json
{  "label": "Additional information",  "name": "comment",  "type": "textarea",  "hint": "Provide additional information if needed."}
```text

#### Textarea element attributes {#attributes_textarea_elements}

`Attribute`

Type

Description

`type`

String

For a text area, the `type` is always `textarea`. It's required.

`label`

String

Label displayed to user. Required. No more than 48 characters.

`name`

String

Name of form element. Required. No more than 300 characters.

`placeholder`

String

A string displayed as needed to help guide users in completing the element. 150 character maximum.

`max_length`

Integer

Maximum input length allowed for element. `0`\-`3000` characters. Defaults to 3000.

`min_length`

Integer

Minimum input length allowed for element. `1`\-`3000` characters. Defaults to 0.

`optional`

Boolean

Provide `true` when the form element is not required. By default, form elements are _required_.

`hint`

String

Helpful text provided to assist users in answering a question. Up to 150 characters.

`subtype`

String

A subtype for this text area, just in case you need a lot of space for them. `email`, `number`, `tel`, or `url`

`value`

String

A default value for this field. Up to 3000 characters.

### Select elements {#select_elements}

Use the `select` element for multiple choice selections allowing users to pick a single item from a list. True to web roots, this selection is displayed as a dropdown menu.

![Dialog select element](data:image/png;base64,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)

A `select` element may contain up to 100 selections, provided as an array of hashes ([see below](#option_element_attributes)) in the form element's `options` field, (or an `option_groups` array).

These `select` elements have a `data_source` attribute which specifies whether you want a static list (`static`, which is the default) or a dynamic list ([see below](#dynamic_select_elements)), but let's take a look at a `static` list first:

## Example `select` form element definition:

```json
{  "label": "Meal preferences",  "type": "select",  "name": "meal_preferences",  "options": [    {      "label": "Vegan",      "value": "vegan"    },    {      "label": "Kosher",      "value": "kosher"    },    {      "label": "Just put it in a burrito",      "value": "burrito"    }   ]}
```text

## Example `select` form element with `option_groups`:

```json
{  "label": "Choose a meme",  "name": "animal",  "type": "select",  "option_groups": [    {      "label": "Cats",      "options": [        {          "label": "Maru",          "value": "maru"        },        {          "label": "Lil Bub",          "value": "lilbub"        },        {          "label": "Hamilton the Hipster Cat",          "value": "hamilton"        }      ]    },    {      "label": "Dogs",      "options": [        {          "label": "Boo the Pomeranian",          "value": "boo"        }      ]    },  ]}
```text

![Dialog select element with option groups](data:image/png;base64,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)

#### Populate a select menu dynamically {#dynamic_select_elements}

In addition to the static select menu, you can also generate a data set for a menu on the fly. Make dialog select menus more dynamic by specifying one of these four `data_source` types:

Data source type

Description

`users`

The element will be populated with options corresponding to the users available to the current user.

`channels`

The element will be populated with options corresponding to the public channels available to the current user.

`conversations`

The element will be populated with options corresponding to the public channels, private channels, DMs, and MPIMs available to the current user.

`external`

The element will be populated with options or options groups return from an endpoint specified in your app configuration setting.

If no `data_source` is specified, it defaults to `static`.

##### 👤 Dynamic user list {#dynamic_select_elements_users}

Now you can easily populate a select menu with a list of users. For example, when you are creating a bug tracking app, you want to include a field for an assignee. Slack pre-populates the user list in client-side, so your app doesn't need access to a related OAuth scope.

## Example `select` element with `users` data source:

```json
{  "label": "Assignee",  "name": "bug_assignee",  "type": "select",  "data_source": "users"}
```text

![Dynamic select from user list](data:image/png;base64,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)

##### #️⃣Channels and conversations {#dynamic_select_elements_channels_conversations}

You can also provide a select menu with a list of channels. Specify your `data_source` as `channels` to limit only to public channels or use conversations to include private channels, direct messages, MPIMs, and whatever else we consider a conversation-like thing.

## Example `select` element with `conversations` data source:

```json
{  "label": "Post this message on",  "name": "channel_notify",  "type": "select",  "data_source": "conversations"}
```text

![Dynamic select from channels](data:image/png;base64,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)

##### 📄 Dynamic data from an external source {#dynamic_select_elements_external}

A list of options can be loaded from an external URL and used in your dialog menus.

First a little bit of setup is required to configure the URL that the options will be loaded from:

* Go to the [app settings page](https://api.slack.com/apps)
* Pick your app
* Navigate to the _Interactive Components_ section
* Insert the Options Load URL in the _Message Menus_ section

If you've already configured an Options Load URL for other uses, you'll be able to use the `type` and `callback_id` as below to determine which options data you want to return.

Now you can create a dialog with a `select` menu where the `data_source` is set to `external`:

```json
{  "label": "Bug ticket",  "name": "ticket_list",  "type": "select",  "data_source": "external"}
```text

As soon as a user clicks or taps the drop-down menu, a request like the following is sent to your specified URL:

```json
{  "type": "dialog_suggestion",  "token": "W3VDvuzi2nRLsiaDOsmJranO",  "action_ts": "1528203589.238335",  "team": {    "id": "T24BK35ML",    "domain": "hooli-hq"  },  "user": {    "id": "U900MV5U7",    "name": "gbelson"  },  "channel": {    "id": "C012AB3CD",    "name": "triage-platform"  },  "name": "external_data",  "value": "",  "callback_id": "bugs"}
```text

From the external URL, a list of `options` (or an `option_groups` array) should be returned as a HTTP `200` response:

## Example `options` from the external data source:

```json
{  "options": [    {      "label": "[UXD-342] The button color should be artichoke green, not jalapeño",      "value": "UXD-342"    },    {      "label": "[FE-459] Remove the marquee tag",      "value": "FE-459"    },    {      "label": "[FE-238] Too many shades of gray in master CSS",      "value": "FE-238"    }  ]}
```text

## Example `option_groups` from the external data source:

```json
{  "option_groups": [    {      "label": "Visual Design",      "options": [        {          "label": "[UXD-342] The button color should be artichoke green, not jalapeño",          "value": "UXD-342"        }      ]    },    {      "label": "Front-End Engineering",      "options": [        {          "label": "[FE-459] Remove the marquee tag",          "value": "FE-459"        },        {          "label": "[FE-238] Too many shades of gray in master CSS",          "value": "FE-238"        }      ]    }  ]}
```text

A maximum of 100 options may be included.

Dialog menus uses the more clearly labeled field `label` instead of `text` for menu option labels

##### Using Typeahead style select menus {#select_dynamic_typeahead}

When you're loading in external objects data for a menu, you can also adjust your code to provide a typeahead style experience where the user types the first few characters of a potential selection, and the app responds with a filtered list of results.

As users type into the select menu, Slack dispatches data to your app and by analyzing their text, you can return the most relevant, filtered options for them. Here's a data payload similar to the one that is sent to your app, showing a situation where the user has typed "des":

```json
{  "type": "dialog_suggestion",  "team": {    "id": "T123ABC456",    "domain": "hooli-hq"  },  "user": {    "id": "U123ABC456",    "name": "sbutterfield"  },  "channel": {    "id": "C123ABC456",    "name": "triage-platform"  },  "action_ts": "1520635427.671963",  "token": "W3VDvuzi2nRLsiaDOsmJranO",  "name": "external_data",  "value": "des",  "callback_id": "bugs"}
```text

When you're enabling this kind of interaction, it's recommended that you [set a `min_query_length` attribute](#attributes_select_elements) to a sane value (at least 2). Otherwise your app might end up searching a massive list of potential matches for a single character, and your DB admins will yell at you.

#### Setting default values for select menus {#select_default_values}

To set a default selection for a select menu with a `data_source` attribute of `static`, `users`, `channels`, or `conversations`, provide a `value` attribute containing one of the `value` attributes from the element's collection of `options`:

```json
{  "label": "Meal preferences",  "type": "select",  "name": "meal_preferences",  "value": "vegan",  "options": [    {      "label": "Vegan",      "value": "vegan"    },    {      "label": "Kosher",      "value": "kosher"    },    {      "label": "Just put it in a burrito",      "value": "burrito"    }   ]}
```text

To set a default selection for a select menu with the `data_source` type [set to `external`](#dynamic_select_elements_external), instead provide a `selected_options` attribute, which should be an array containing a single `label` and `value` object that you know is in the dynamic options list:

```json
{  "label": "Bug ticket",  "name": "ticket_list",  "type": "select",  "data_source": "external",  "min_query_length": 2,  "selected_options": [    {      "label": "[FE-459] Remove the marquee tag",      "value": "FE-459"    }  ]}
```text

#### Attributes for static and dynamic select elements {#attributes_select_elements}

Attribute

Type

Description

`label`

String

Label displayed to user. Required. No more than 48 characters.

`name`

String

Name of form element. Required. No more than 300 characters.

`type`

String

Set this to `select` for select elements.

`data_source`

String

Set this to either `users`, `channels`, `conversations`, or `external`. Default value is `static`.

`min_query_length`

Number

Specify the number of characters that must be typed by a user into a dynamic select menu before [dispatching to the app](#select_dynamic_typeahead).

`placeholder`

String

A string displayed as needed to help guide users in completing the element. 150 character maximum.

`optional`

Boolean

Provide `true` when the form element is not required. By default, form elements are _required_.

`value`

String

Provides a default selected value for select menus with a `data_source` of type `static`, `users`, `channels`, or `conversations` ([see above](#select_default_values)). **This option is invalid with `data_source` of type `external`, where you must use `selected_options` as below.**

`selected_options`

Array

Provides a default selected value for dynamic select menus with a `data_source` of type `external`. This should be an array containing a single object that specifies the default `label` and `value` ([see above](#select_default_values)).

`options`

Array

Provide up to 100 options. Either `options` or `option_groups` is required for the `static` and `external`.

`options[].label` is a user-facing string for this option. 75 characters maximum. Required. `options[].value` is a string value for your app. If an integer is used, it will be parsed as a string. 75 characters maximum. Required.| |`option_groups`|Array|An array of objects containing a `label` and a list of options. Provide up to 100 option groups. Either `options` or `option_groups` is required for the `static` and `external`.

`options_groups[].label` is a user-facing string for this option. 75 characters maximum. Required. `options_groups[].options` is an array that contains a list of options. It is formatted like the options array (see `options`).|

## Dialog submission sequence {#submit}

The typical submission workflow is:

1. When users submit a form, Slack will validate their responses against the dialog's configuration.
2. When the form is successfully submitted, Slack will send a request to your Request URL with the `callback_id` you set at dialog creation and the values submitted by the user.
3. Your app has the opportunity to validate the user's responses according to your own business logic and suggest additional corrections before final submission.
4. When the dialog is fully submitted, your app should display some kind of result or feedback to users.

Upon receiving this payload, your server must respond within **3 seconds**, whether the form is valid or not. Otherwise, [use the `response_url` to POST a delayed response.](/interactivity/handling-user-interaction#message_responses)

### Evaluating submission responses {#response}

Your "Request URL" (formerly known as an "Action URL"), configured in your application management settings under _Interactive Components_, will receive an interactive framework JSON structure in a URL-encoded `payload` POST parameter.

For example, consider this submission:

```text
POST https://example.com/your-request-urlpayload=%7B%22type%22%3A%22dialog_submission%22%2C%22submission%22%3A%7B%22name%22%3A%22Sigourney%20Dreamweaver%22%2C%22email%22%3A%22sigdre%40example.com%22%2C%22phone%22%3A%22%2B1%20800-555-1212%22%2C%22meal%22%3A%22burrito%22%2C%22comment%22%3A%22No%20sour%20cream%20please%22%2C%22team_channel%22%3A%22C0LFFBKPB%22%2C%22who_should_sing%22%3A%22U0MJRG1AL%22%7D%2C%22callback_id%22%3A%22employee_offsite_1138b%22%2C%22state%22%3A%22vegetarian%22%2C%22team%22%3A%7B%22id%22%3A%22T1ABCD2E12%22%2C%22domain%22%3A%22coverbands%22%7D%2C%22user%22%3A%7B%22id%22%3A%22W12A3BCDEF%22%2C%22name%22%3A%22dreamweaver%22%7D%2C%22channel%22%3A%7B%22id%22%3A%22C1AB2C3DE%22%2C%22name%22%3A%22coverthon-1999%22%7D%2C%22action_ts%22%3A%22936893340.702759%22%2C%22token%22%3A%22M1AqUUw3FqayAbqNtsGMch72%22%2C%22response_url%22%3A%22https%3A%2F%2Fhooks.slack.com%2Fapp%2FT012AB0A1%2F123456789%2FJpmK0yzoZDeRiqfeduTBYXWQ%22%7D
```text

Decode the `payload` parameter's JSON and you have a mapping with a few notable keys:

```json
{    "type": "dialog_submission",    "submission": {        "name": "Sigourney Dreamweaver",        "email": "sigdre@example.com",        "phone": "+1 800-555-1212",        "meal": "burrito",        "comment": "No sour cream please",        "team_channel": "C123ABC456",        "who_should_sing": "U123ABC456"    },    "callback_id": "employee_offsite_1138b",    "state": "vegetarian",    "team": {        "id": "T123ABC456",        "domain": "coverbands"    },    "user": {        "id": "W123ABC456",        "name": "dreamweaver"    },    "channel": {        "id": "C123ABC456",        "name": "coverthon-1999"    },    "action_ts": "936893340.702759",    "token": "M1AqUUw3FqayAbqNtsGMch72",    "response_url": "https://hooks.slack.com/app/T012AB0A1/123456789/JpmK0yzoZDeRiqfeduTBYXWQ"}
```text

Let's look deeper at those attributes, which you might recognize many of from [interactive messages](/legacy/legacy-messaging/legacy-making-messages-interactive).

* `type` - to differentiate from other interactive components, look for the string value `dialog_submission`.
* `submission` - a hash of key/value pairs representing the user's submission. Each key is a `name` field your app provided when composing the form. Each `value` is the user's submitted value, or in the case of a static select menu, the `value` you assigned to a specific response. The selection from a dynamic menu, the value can be a channel ID, user ID, etc.
* `callback_id` - this value is the unique `callback_id` identifier your app gave this instance of the dialog. Use the `callback_id` to keep track of which form submission is which, not to store state.
* `state` - this string echoes back what your app passed to `dialog.open`. Use it as a pointer that references sensitive data stored elsewhere.
* `team` - this hash contains the `id` and `name` of the workspace from which this interaction occurred
* `user` - this hash contains the `id` and `name` of the user who completed the form
* `channel` - this hash contains the `id` and `name` of the channel or conversation where this dialog was completed
* `action_ts` - this is a unique identifier for this specific action occurrence generated by Slack. It can be evaluated as a timestamp with milliseconds if that is helpful to you.
* `token` - this is a deprecated verification token shared between your app and Slack, used to check that an incoming request originates from Slack.
* `response_url` - the URL can be used to post responses to dialog submissions. [Read our guide to app interactivity](/interactivity/handling-user-interaction#message_responses) to learn more about how to respond using a `response_url`.

The `token` value, which represents a verification token, is _now deprecated_. The best way to verify the authenticity of a Slack request is to [use the signing secret provided to your app](/authentication/verifying-requests-from-slack).

### Using state to pass extra information through dialogs {#state}

When your app calls `dialog.open`, it may optionally pass additional data via the `state` parameter. The `state` string may be up to 3,000 characters long, and it isn't shown to users. During dialog submission and cancellation, the `state` string is echoed back to your app. Whatever stash of pointers you passed during `dialog.open` gets returned to you, unharmed and unchanged.

Note: don't store sensitive information in the `state` field. It's best to use `state` to reference sensitive data stored elsewhere. You may already be using the `callback_id` parameter for that, but we strongly recommend using the `state` field instead.

### Input validation {#input-validation}

While Slack will handle some client-side validation of user input upon submission, we encourage your app to do its own round of validation based on its own business logic.

As soon as your user hits the submit button, Slack client will validate the user's inputs against the validation parameters that you have passed to make sure that all the required fields are filled and the formats are correct. And the form won't submit until the user corrects all errors.

![Dialog client validation](data:image/png;base64,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)

You should validate the `submission` values you receive server-side against your own heuristics.

If your app finds any errors with the submission, respond with an `application/json` payload within the body of a `200 OK` response - the requests between your app and Slack are still `OK` after all, so don't use any kind of error response.

This payload should be an `errors` array containing 1 or more objects that include:

* `name` - a string which specifies the corresponding dialog element that is being rejected. This must match the `name` used to create that element.
* `error` - a string which describes _why_ that element is being rejected.

Here's an example of what that payload should look like:

```json
{  "errors": [    {      "name": "email_address",      "error": "Sorry, this email domain is not authorized!"    },    {      "name": "username",      "error": "Uh-oh. This username has been taken!"    }  ]}
```text

The API returns these errors to the user in-app, allowing the user to make corrections and submit again.

## When there are no exceptions within the dialog submission, your app must respond with `200 OK` with an _empty_ body. This will complete the dialog.

### Following up {#following_up}

After you've confirmed the submission is valid and sent a HTTP `200 OK` message, you'll want to let the user know everything is fine.

Use a method like `chat.postMessage` or `chat.postEphemeral`, depending on context and desired visibility, to create a message thanking the user and/or providing other feedback. You can also send a delayed response to the `response_url` if you need more than 3 seconds to respond. with the `response_url`, your app can continue interacting with users up to 5 times within 30 minutes of the action invocation.

For example, if you are building an app for survey, it is still a good idea to send a follow-up message to make sure your valuable user knows the form submission was successful!

[Read our guide to app interactivity](/interactivity/handling-user-interaction#message_responses) to learn more about [sending responses](/interactivity/handling-user-interaction#message_responses).

### Dialog cancellations {#dialog_cancellations}

When users dismiss a dialog by either clicking on the "Cancel" button, exit "x" on the top-right corner, or by clicking away from a dialog, we'll warn them that they'll lose any answers they've made to an unsubmitted dialog.

Once the dialog is canceled, Slack can send you a `dialog_cancellation` events to your Request URL, _if you wish_. To receive the notification, set the `notify_on_cancel` value `true`, when you [open the dialog](#opening_a_dialog).

If you wish to follow up with the user, use the cancellation's `response_url` to create a new message using response URL semantics.

```json
{  "type": "dialog_cancellation",  "token": "old-and-moldy-verification-token",  "action_ts": "1542993577.333025",  "team": {    "id": "T123ABC456",    "domain": "coverbands"  },  "user": {    "id": "U123ABC456",    "name": "leepresson"  },  "channel": {    "id": "C123ABC456",    "name": "graceland"  },  "callback_id": "best_elvis_impersonator_name",  "response_url": "https://hooks.slack.com/app/T123ABC456/486xxxxxx/jbF9HF",  "state": "final_round"}
```text

## Adapting existing workflows to dialogs {#adapting}

Existing workflows using only conversation, message buttons, or message menus can be enhanced with the focused concentration made possible with dialogs.

Imagine a `/helpdesk` slash command connected to a company's internal IT helpdesk. With very limited syntax enforcement and the wild possibilities inherent in free-form text, filing a ticket is imprecise and less instantly actionable.

```text
/helpdesk hardware "help my cat chewed on my mouse cable it doesn't work anymore"
```text

Commands like this are noble in purpose but could be made more precise in execution with dialogs.

Your software could easily interpret this as a ticket meant for a `hardware` category. With some heuristics and analysis, your app might derive that it's about a mouse.

Without asking a series of focused questions to illuminate the entire surface area of the user's inquiry, the user's submission is significantly less actionable than its potential.

By invoking a dialog, you may ask specific guided questions around urgency, platform, location, and other nuances made possible with multiple choice.

Another example, illustrated in the animation below, demonstrates a slash command execution leading to an optimized dialog and useful outcome.

* * *

## designing useful dialogs {#designing-useful-dialogs}

In general, the easier it is to enter information into a dialog, the more likely your users are to fill them out to completion. Wherever possible, favor structured inputs over freeform text, and work to keep the total length relatively short.

#### Modal {#modal}

In order to look best on mobile as well as desktop, we suggest that modal titles be short. Our tips on choosing words for messages generally apply: keep modal titles sentence-cased; pick action verbs for buttons that confirm what the user is doing.

Provide a `placeholder` value for all field elements to better communicate purpose independent of the user's interface.

#### Dropdown (select field) {#dropdown}

These are best used for concise answers with established bounds or options, e.g. office location, age range, or dietary preference. Keep dropdown options short, and remember to test how they render on mobile devices.

#### Text input {#text-input}

Text input fields are capped at 150 characters, and are best used for concise freeform answers, like name or ticket title.

If inputs are better served with pre-selected answers (e.g. age ranges, department), consider using a dropdown. If you expect input to be longer than 150 characters, consider using a text area.

#### Text area {#text}

Text areas are good for open-ended questions that need more room, like meeting notes or interview feedback. Most dialogs should not have more than one or two text areas; remember that keeping the input brief and contextual will help ensure that people complete the forms.

Like this:

![A well-formulated dialog](/assets/images/dialogs_do-a59815bf4cb20d4653d041b61a3bf42e.png)

Not like this:

![A ill-formulated dialog](/assets/images/dialogs_dont-4db31babe5e132aa6564b2098e1b91fe.png)

Your dialogs can be short and to the point, a focused way to collect a single piece of information. They can be long, asking questions requiring more thought, research, and careful response. Chain dialogs together with buttons or menus to serialize phased workflow execution.
