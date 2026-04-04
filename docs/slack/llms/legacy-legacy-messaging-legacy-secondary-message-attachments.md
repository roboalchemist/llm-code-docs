Source: https://docs.slack.dev/legacy/legacy-messaging/legacy-secondary-message-attachments

# Legacy secondary message attachments

This feature is a legacy part of messaging functionality for Slack apps.

We recommend you stick with [layout blocks](/reference/block-kit/blocks), but if you still want to use attachments, [read our caveats.](/messaging/formatting-message-text#when-to-use-attachments)

Secondary content can be attached to messages to include lower priority content - content that doesn't necessarily need to be seen to appreciate the intent of the message, but perhaps adds further context or additional information.

* * *

## An example message attachment {#example}

Here's what a message looks like with a secondary attachment:

![Example message with attachment showing full range of fields](/assets/images/message_example_with_attachments-ceabc178c2b2668b1b9f16a16eb30cbe.png)

And here's the example code used to create a message with this attachment in it:

```json
{    "channel": "ABCDEBF1",    "attachments":     [        {            "mrkdwn_in": ["text"],            "color": "#36a64f",            "pretext": "Optional pre-text that appears above the attachment block",            "author_name": "author_name",            "author_link": "http://flickr.com/bobby/",            "author_icon": "https://placeimg.com/16/16/people",            "title": "title",            "title_link": "https://docs.slack.dev/",            "text": "Optional `text` that appears within the attachment",            "fields":             [                {                    "title": "A field's title",                    "value": "This field's value",                    "short": false                },                {                    "title": "A short field's title",                    "value": "A short field's value",                    "short": true                },                {                    "title": "A second short field's title",                    "value": "A second short field's value",                    "short": true                }            ],            "thumb_url": "http://placekitten.com/g/200/200",            "footer": "footer",            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",            "ts": 123456789        }    ]}
```text

Read on to find out what each of these fields and values do.

* * *

## Field reference {#fields}

Apps can use the following fields and values to generate each JSON object within the `attachments` array of a message:

Field

Type

Description

Required?

`blocks`

Array

An array of [layout blocks](/reference/block-kit/blocks) in the same format [as described in the building blocks guide](/block-kit).

No

`color`

String

Changes the color of the border on the left side of this attachment from the default gray. Can either be one of `good` (green), `warning` (yellow), `danger` (red), or any hex color code (eg. `#439FE0`)

No

In addition to these fields, there are a number of legacy fields that can included that are [explained below](#legacy_fields).

### Legacy fields {#legacy_fields}

If you are using attachments, we still recommend that you use the `blocks` field above to structure and layout the content within them [using Block Kit](/messaging/formatting-message-text#rich-layouts).

Legacy options shown below should be avoided in nearly every case - [blocks](/reference/block-kit/blocks) offer the same visual capabilities, and add many more. Meanwhile, these legacy options may be subject to reductions in visibility or functionality.

All of these fields are optional if you're including `blocks` as [above](#fields). If you aren't, one of either `fallback` or `text` are required:

Field

Description

Block alternatives

`author_icon`

A valid URL that displays a small 16px by 16px image to the left of the `author_name` text. Will only work if `author_name` is present.

An [image element](/reference/block-kit/block-elements/image-element) in a [context block](/reference/block-kit/blocks/context-block).

`author_link`

A valid URL that will hyperlink the `author_name` text. Will only work if `author_name` is present.

A [text object](/reference/block-kit/composition-objects/text-object) in a [context block](/reference/block-kit/blocks/context-block).

`author_name`

Small text used to display the author's name.

A [text object](/reference/block-kit/composition-objects/text-object) in a [context block](/reference/block-kit/blocks/context-block).

`fallback`

A plain text summary of the attachment used in clients that don't show formatted text (eg. IRC, mobile notifications).

The top-level `text` field from the [message payload](/messaging#payloads).

`fields`

An array of [field objects](#field_objects) that get displayed in a table-like way (See the [example above](#example)). For best results, include no more than 2-3 field objects.

`fields` in a [section block](/reference/block-kit/blocks/section-block).

`footer`

Some brief text to help contextualize and identify an attachment. Limited to 300 characters, and may be truncated further when displayed to users in environments with limited screen real estate.

A [text object](/reference/block-kit/composition-objects/text-object) in a [context block](/reference/block-kit/blocks/context-block).

`footer_icon`

A valid URL to an image file that will be displayed beside the `footer` text. Will only work if `footer` is present. We'll render what you provide at 16px by 16px. It's best to use an image that is similarly sized.

An [image element](/reference/block-kit/block-elements/image-element) in a [context block](/reference/block-kit/blocks/context-block).

`image_url`

A valid URL to an image file that will be displayed at the bottom of the attachment. We support GIF, JPEG, PNG, and BMP formats.Large images will be resized to a maximum width of 360px or a maximum height of 500px, while still maintaining the original aspect ratio. Cannot be used with `thumb_url`.

An [image block](/reference/block-kit/blocks/image-block).

`mrkdwn_in`

An array of field names that should be [formatted by `mrkdwn` syntax](/messaging/formatting-message-text#basics).

Format [text objects](/reference/block-kit/composition-objects/text-object) with [`mrkdwn`](/messaging/formatting-message-text#basics).

`pretext`

Text that appears above the message attachment block. It can be formatted as plain text, or with [`mrkdwn`](/messaging/formatting-message-text#basics) by including it in the `mrkdwn_in` field.

A [section block](/reference/block-kit/blocks/section-block).

`text`

The main body text of the attachment. It can be formatted as plain text, or with [`mrkdwn`](/messaging/formatting-message-text#basics) by including it in the `mrkdwn_in` field. The content will automatically collapse if it contains 700+ characters or 5+ line breaks, and will display a "Show more..." link to expand the content.

A [section block](/reference/block-kit/blocks/section-block) using [text formatting](/messaging/formatting-message-text).

`thumb_url`

A valid URL to an image file that will be displayed as a thumbnail on the right side of a message attachment. We currently support the following formats: GIF, JPEG, PNG, and BMP.The thumbnail's longest dimension will be scaled down to 75px while maintaining the aspect ratio of the image. The file size of the image must also be less than 500 KB.For best results, please use images that are already 75px by 75px.

A [section block](/reference/block-kit/blocks/section-block) with an [image element](/reference/block-kit/block-elements/image-element).

`title`

Large title text near the top of the attachment.

A [section block](/reference/block-kit/blocks/section-block).

`title_link`

A valid URL that turns the `title` text into a hyperlink.

A [section block](/reference/block-kit/blocks/section-block) using [`mrkdwn` links](/messaging/formatting-message-text#linking-urls).

`ts`

An integer [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time) that is used to relate your attachment to a specific time. The attachment will display the additional timestamp value as part of the attachment's footer.Your message's timestamp will be displayed in varying ways, depending on how far in the past or future it is, relative to the present. Form factors, like mobile versus desktop may also transform its rendered appearance.

A [context block](/reference/block-kit/blocks/context-block) using [date formatting](/messaging/formatting-message-text#date-formatting).

### Field objects {#field_objects}

Field

Type

Description

Required?

`title`

String

Shown as a bold heading displayed in the field object. It cannot contain markup and will be escaped for you.

No

`value`

String

The text value displayed in the field object. It can be formatted as plain text, or with [`mrkdwn`](/messaging/formatting-message-text#basics) by using the [`mrkdwn_in` option above](#legacy_fields).

No

`short`

Boolean

Indicates whether the field object is short enough to be displayed side-by-side with other field objects. Defaults to `false`.

No

* * *

## Message attachment guidelines {#guidelines}

Message attachments allow you to add richer formatting to messages, as well as interactive buttons and menus. Try to use the least amount of formatting needed, and remember that messages will look slightly different on mobile devices than they do on a computer screen.

### Basic message attachment {#basic-message-attachment}

![How message formatting appears](/assets/images/Formatting_1-d67624f2ac49123895e2dc9431dd6920.png)

![Message formatting on mobile](/assets/images/Formatting_Mobile_1-707a6d67d74fc7b3ecad6d3f4a76bff0.png)

### Message with thumbnail attachment {#message-with-thumbnail-attachment}

![Message with thumbnail](data:image/png;base64,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)

![Message formatting with thumbnail on mobile](/assets/images/Formatting_Mobile_2-0391dedbe0f612521b47ed56b20c9044.png)

### Message with image attachment {#message-with-image-attachment}

![Message with image](/assets/images/Formatting_3-65df45c2b1640dd426bd9cb01e3cf216.png)

![Message formatting with image on mobile](/assets/images/Formatting_Mobile_3-a337cd57f656a27dd6fbf83b2bf39e37.png)

### Don't get too attached {#dont-get-too-attached}

Don't use an attachment when regular message text will suffice, and don't send multiple attachments when a single attachment will do.

And never ever (ever!) send more than 20 attachments.

#### Like this {#like-this}

![Good: Keep it simple](/assets/images/Example_2_Good-d71a27168d6fe41bc6ad0642c98d7f53.png)

#### Not like that {#not-like-that}

![Bad: Uh-oh, this is unnecessary](/assets/images/Example_2_Bad-dc474e5dfe078ba80cd863f102d56863.png)

#### Great: This is one attachment {#great-this-is-one-attachment}

![Good: Limited button selections](/assets/images/Example_3_Good-18731d15539b33b549310ae282baad05.png)

#### Uh-oh: This is three {#uh-oh-this-is-three}

![Bad: Uh-oh too many pieces of flair](/assets/images/Example_3_Bad-2711409ade470d3dde298f1d93bdd3a3.png)

The difference is small, yes, but Slack prefers consolidated messages.

### Message attachments as objects {#message-attachments-as-objects}

Each attachment should represent an object so if there's a title for it, it should be _inside_ the attachment.

#### Good idea {#good-idea}

![Good: Title in attachment](/assets/images/Example_4_Good-b5fdd85c95fca24c92f61ce615fbce44.png)

#### Bad idea {#bad-idea}

![Bad: Unattached title](/assets/images/Example_4_Bad-b806476a49ea3986027f0005de9e863f.png)

### Showing a large number of items {#showing-a-large-number-of-items}

Please don't display a long list of items. Try to show the most likely options first and, if you _must_, use buttons to paginate items. Try to replace the list instead of adding new messages.

Avoid cluttering up the conversation for everyone by using ephemeral messages in conversations when displaying items as an intermediary step of an action.
