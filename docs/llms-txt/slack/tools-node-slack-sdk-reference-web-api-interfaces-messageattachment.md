Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MessageAttachment

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MessageAttachment

# Interface: MessageAttachment

Defined in: packages/types/dist/message-attachments.d.ts:8

Add [secondary attachments](https://docs.slack.dev/messaging/formatting-message-text#attachments) to your messages in Slack. Message attachments are considered a legacy part of messaging functionality. They are not deprecated per se, but they may change in the future, in ways that reduce their visibility or utility. We recommend moving to Block Kit instead. Read more about [when to use message attachments](https://docs.slack.dev/messaging/formatting-message-text#attachments).

## See {#see}

[message attachments reference documentation](https://docs.slack.dev/messaging/formatting-message-text#attachmentsSecondary)

## Properties {#properties}

### actions? {#actions}

```text
optional actions: AttachmentAction[];
```text

Defined in: packages/types/dist/message-attachments.d.ts:97

* * *

### app_id? {#app_id}

```text
optional app_id: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:107

* * *

### app_unfurl_url? {#app_unfurl_url}

```text
optional app_unfurl_url: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:105

* * *

### author_icon? {#author_icon}

```text
optional author_icon: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:41

#### Description {#description}

A valid URL that displays a small 16px by 16px image to the left of the `author_name` text. Will only work if `author_name` is present.

* * *

### author_link? {#author_link}

```text
optional author_link: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:36

#### Description {#description-1}

A valid URL that will hyperlink the `author_name` text. Will only work if `author_name` is present.

* * *

### author_name? {#author_name}

```text
optional author_name: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:32

#### Description {#description-2}

Small text used to display the author's name.

* * *

### author_subname? {#author_subname}

```text
optional author_subname: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:42

* * *

### blocks? {#blocks}

```text
optional blocks: AnyBlock[];
```text

Defined in: packages/types/dist/message-attachments.d.ts:13

#### Description {#description-3}

An array of [layout blocks](/tools/node-slack-sdk/reference/web-api/type-aliases/KnownBlock) in the same format [as described in the building blocks guide](https://docs.slack.dev/block-kit/designing-with-block-kit).

* * *

### bot_id? {#bot_id}

```text
optional bot_id: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:108

* * *

### callback_id? {#callback_id}

```text
optional callback_id: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:98

* * *

### color? {#color}

```text
optional color: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:23

#### Description {#description-4}

Changes the color of the border on the left side of this attachment from the default gray. Can either be one of `good` (green), `warning` (yellow), `danger` (red), or any hex color code (eg. `#439FE0`)

* * *

### fallback? {#fallback}

```text
optional fallback: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:18

#### Description {#description-5}

A plain text summary of the attachment used in clients that don't show formatted text (e.g. mobile notifications).

* * *

### fields? {#fields}

```text
optional fields: MessageAttachmentField[];
```text

Defined in: packages/types/dist/message-attachments.d.ts:63

#### Description {#description-6}

An array of [MessageAttachmentField](/tools/node-slack-sdk/reference/web-api/interfaces/MessageAttachmentField) that get displayed in a table-like way (see [this example](https://docs.slack.dev/messaging/formatting-message-text#attachments)). For best results, include no more than 2-3 field objects.

* * *

### footer? {#footer}

```text
optional footer: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:83

#### Description {#description-7}

Some brief text to help contextualize and identify an attachment. Limited to 300 characters, and may be truncated further when displayed to users in environments with limited screen real estate.

* * *

### footer_icon? {#footer_icon}

```text
optional footer_icon: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:89

#### Description {#description-8}

A valid URL to an image file that will be displayed beside the `footer` text. Will only work if `footer` is present. We'll render what you provide at 16px by 16px. It's best to use an image that is similarly sized.

* * *

### image_url? {#image_url}

```text
optional image_url: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:70

#### Description {#description-9}

A valid URL to an image file that will be displayed at the bottom of the attachment. We support GIF, JPEG, PNG, and BMP formats. Large images will be resized to a maximum width of 360px or a maximum height of 500px, while still maintaining the original aspect ratio. Cannot be used with `thumb_url`.

* * *

### is_app_unfurl? {#is_app_unfurl}

```text
optional is_app_unfurl: boolean;
```text

Defined in: packages/types/dist/message-attachments.d.ts:106

* * *

### mrkdwn_in? {#mrkdwn_in}

```text
optional mrkdwn_in: ("text" | "pretext" | "fields")[];
```text

Defined in: packages/types/dist/message-attachments.d.ts:104

#### Description {#description-10}

Field names that should be [by \`mrkdwn\` syntax](https://docs.slack.dev/messaging/formatting-message-textformatted). The fields that can be formatted in this way include the names of the `fields` property, or the `text` or `pretext` properties.

* * *

### pretext? {#pretext}

```text
optional pretext: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:28

#### Description {#description-11}

Text that appears above the message attachment block. It can be formatted as plain text, or with [\`mrkdwn\`](https://docs.slack.dev/messaging/formatting-message-text#basic-formatting) by including it in the `mrkdwn_in` field.

* * *

### preview? {#preview}

```text
optional preview: MessageAttachmentPreview;
```text

Defined in: packages/types/dist/message-attachments.d.ts:109

* * *

### text? {#text}

```text
optional text: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:57

#### Description {#description-12}

The main body text of the attachment. It can be formatted as plain text, or with [\`mrkdwn\`](https://docs.slack.dev/messaging/formatting-message-text#basic-formatting) by including it in the `mrkdwn_in` field. The content will automatically collapse if it contains 700+ characters or 5+ line breaks, and will display a "Show more..." link to expand the content.

* * *

### thumb_url? {#thumb_url}

```text
optional thumb_url: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:78

#### Description {#description-13}

A valid URL to an image file that will be displayed as a thumbnail on the right side of a message attachment. We currently support the following formats: GIF, JPEG, PNG, and BMP. The thumbnail's longest dimension will be scaled down to 75px while maintaining the aspect ratio of the image. The file size of the image must also be less than 500 KB. For best results, please use images that are already 75px by 75px.

* * *

### title? {#title}

```text
optional title: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:46

#### Description {#description-14}

Large title text near the top of the attachment.

* * *

### title_link? {#title_link}

```text
optional title_link: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:50

#### Description {#description-15}

A valid URL that turns the `title` text into a hyperlink.

* * *

### ts? {#ts}

```text
optional ts: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:96

#### Description {#description-16}

A Unix timestamp that is used to relate your attachment to a specific time. The attachment will display the additional timestamp value as part of the attachment's footer. Your message's timestamp will be displayed in varying ways, depending on how far in the past or future it is, relative to the present. Form factors, like mobile versus desktop may also transform its rendered appearance.
