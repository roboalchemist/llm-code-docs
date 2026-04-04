Source: https://docs.slack.dev/changelog/2019/09/01/what-they-see-is-what-you-get-and-more-and-less

# What you see is what you get and more and less

September 1, 2019

This autumn, Slack will make what-you-see-is-what-you-get (WYSIWYG) editing available to users.

Once we release WYSIWYG editing, the `text` field found in message objects your app encounters will become an _approximation_ of a user's more richly formatted message.

To capture a message's full nuance and vibrancy, your app may look to the new `blocks` attribute included with such messages.

## What's changing? {#what}

Users will compose and decorate their messages with a user interface that allows bolding, italics, and visual style only accomplishable with arcane symbols today.

Messages authored by users and sent to your app via APIs like [Events API](/apis/events-api/), [`chat.postMessage`](/reference/methods/chat.postMessage), and [`conversations.history`](/reference/methods/conversations.history) will expand to more fully capture user intent.

The `text` field will continue to contain a textual and markup-laden representation of the user's typed message.

For example, just as today you might find a message like: `This is a *rich text *message that uses _italics and _~strikethrough ~and looks :sparkles: _*fabulous*_ :sparkles:`. As before, the `text` field is not an exact representation of what a user typed... Slack will still process message markup and expand or contract aspects like "user mentions." This is going to be the most readable version of the user's message.

The `blocks` field will contain specific [Block Kit](/block-kit) "blocks" that make up the various kinds of markup available to users. Parsing these blocks will require some custom programming on your part — it's not possible for developers to _build_ messages using these rich text blocks.

### Example message object {#example-message-object}

This example demonstrates that same message, now verbosely containing WYSIWYG-authored content under the `blocks` attribute.

```json
{  "client_msg_id": "70c82df9-9db9-48b0-bf4e-9c43db3ed097",  "type": "message",  "text": "This is a *rich text *message that uses _italics and _~strikethrough ~and looks :sparkles: _*fabulous*_ :sparkles:",  "user": "U0JD3BPNC",  "ts": "1565629075.001000",  "team": "T0JD3BPMW",  "blocks": [    {      "type": "rich_text",      "block_id": "hUBz",      "elements": [        {          "type": "rich_text_section",          "elements": [            {              "type": "text",              "text": "This is a "            },            {              "type": "text",              "text": "rich text ",              "style": {                "bold": true              }            },            {              "type": "text",              "text": "message that uses "            },            {              "type": "text",              "text": "italics and ",              "style": {                "italic": true              }            },            {              "type": "text",              "text": "strikethrough ",              "style": {                "strike": true              }            },            {              "type": "text",              "text": "and looks "            },            {              "type": "emoji",              "name": "sparkles"            },            {              "type": "text",              "text": " "            },            {              "type": "text",              "text": "fabulous",              "style": {                "bold": true,                "italic": true              }            },            {              "type": "text",              "text": " "            },            {              "type": "emoji",              "name": "sparkles"            }          ]        }      ]    }  ]}
```text

### Rich elements {#the_riches}

Here are some elements you might find in the `rich_text_section` of a message sent to your app. Expect to encounter other (even undocumented) elements.

Each element is identified by a `type` described below:

* `text` - the words and punctuation a user typed. You'll frequently find `style` attributes paired with this element.
* `channel` - a message element for formatting channel mentions _just so_.
* `user` - a mention of a user, named by `user_id` and potentially with `style` and pizzazz.
* `emoji` - an emoji! will contain a `name` attribute naming the emoji, either from the Slack stock set or those custom and found in [`emoji.list`](/reference/methods/emoji.list).
* `link` - a link to a far off or inner place, with a `url` and sometimes `text` and/or `style`.
* `team` - a mention of a specific workspace/team; includes a `team_id` and can have `style`.
* `usergroup` - a mention of a [user group](/reference/objects/usergroup-object) by `usergroup_id`, like a macro to reach many users!
* `date` - date and time formatted logically and tidily for humans to read. We guarantee we'll include an epoch `timestamp` attribute.
* `broadcast` - used for "macro mentions" like `@channel`, `@everyone`, and `@here`

#### Elements with style {#elements-with-style}

Elements with `style` will contain an object with these named booleans. A `true` value indicates that the element is to be visually displayed in that style.

* `bold` - strong text, thicker fonts, with an intended heavy impact on the reader
* `italic` - the text has a decidedly angular emphasis, often used to express motion or a softness of voice
* `strike` - the text will have a line through it, typically used to express an idea that's no longer true but still relevant to the timeline
* `code` - a bit of programmer's magic or text presented in monospace font

## What isn't changing? {#not_changing}

Messages are still messages. These ones are still written by users. You'll still find the essence of their communication in the `text` field of message objects.

## How do I prepare? {#how}

If you don't consume the `text` field of messages, you don't need to do anything.

If you do use the `text` field, you can keep using it! You won't notice many differences in how typical Slack mark up is generated. Messages will still look like messages.

If your app is after the whole message in all its formal verbosity, you'll want to look to the `blocks` field to understand the many formatting choices chosen by workspace conversationalists.

## When is this happening? {#when}

This autumn, we plan to announce that we're gradually rolling WYSIWYG features out to workspaces. Once that happens, users will begin composing their messages and rich text `blocks` will tag along everywhere their message objects go.

## Tags:

* [New feature](/changelog/tags/new-feature)
