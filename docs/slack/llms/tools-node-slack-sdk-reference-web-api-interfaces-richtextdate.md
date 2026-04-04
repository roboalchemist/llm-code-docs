Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextDate

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextDate

# Interface: RichTextDate

Defined in: packages/types/dist/block-kit/block-elements.d.ts:738

## Description {#description}

A date element for use in a rich text message.

## Extends {#extends}

* [`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable)

## Properties {#properties}

### fallback? {#fallback}

```text
optional fallback: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:778

#### Description {#description-1}

Text to display in place of the date should parsing, formatting or displaying fails.

* * *

### format {#format}

```text
format: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:770

#### Description {#description-2}

A template string containing curly-brace-enclosed tokens to substitute your provided `timestamp` in a particularly-formatted way. For example: `Posted at {date_long}`. The available date formatting tokens are:

* `{day_divider_pretty}`: Shows `today`, `yesterday` or `tomorrow` if applicable. Otherwise, if the date is in current year, uses the `{date_long}` format without the year. Otherwise, falls back to using the `{date_long}` format.
* `{date_num}`: Shows date as YYYY-MM-DD.
* `{date_slash}`: Shows date as DD/MM/YYYY (subject to locale preferences).
* `{date_long}`: Shows date as a long-form sentence including day-of-week, e.g. `Monday, December 23rd, 2013`.
* `{date_long_full}`: Shows date as a long-form sentence without day-of-week, e.g. `August 9, 2020`.
* `{date_long_pretty}`: Shows `yesterday`, `today` or `tomorrow`, otherwise uses the `{date_long}` format.
* `{date}`: Same as `{date_long_full}` but without the year.
* `{date_pretty}`: Shows `today`, `yesterday` or `tomorrow` if applicable, otherwise uses the `{date}` format.
* `{date_short}`: Shows date using short month names without day-of-week, e.g. `Aug 9, 2020`.
* `{date_short_pretty}`: Shows `today`, `yesterday` or `tomorrow` if applicable, otherwise uses the `{date_short}` format.
* `{time}`: Depending on user preferences, shows just the time-of-day portion of the timestamp using either 12 or 24 hour clock formats, e.g. `2:34 PM` or `14:34`.
* `{time_secs}`: Depending on user preferences, shows just the time-of-day portion of the timestamp using either 12 or 24 hour clock formats, including seconds, e.g. `2:34:56 PM` or `14:34:56`.
* `{ago}`: A human-readable period of time, e.g. `3 minutes ago`, `4 hours ago`, `2 days ago`. TODO: test/document `{member_local_time}`, `{status_expiration}` and `{calendar_header}`

* * *

### style? {#style}

```text
optional style: object;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:75

#### bold? {#bold}

```text
optional bold: boolean;
```text

##### Description {#description-3}

When `true`, boldens the text in this element. Defaults to `false`.

#### code? {#code}

```text
optional code: boolean;
```text

##### Description {#description-4}

When `true`, the text is preformatted in an inline code style. Defaults to \`false.

#### italic? {#italic}

```text
optional italic: boolean;
```text

##### Description {#description-5}

When `true`, italicizes the text in this element. Defaults to `false`.

#### strike? {#strike}

```text
optional strike: boolean;
```text

##### Description {#description-6}

When `true`, strikes through the text in this element. Defaults to `false`.

#### underline? {#underline}

```text
optional underline: boolean;
```text

##### Description {#description-7}

When `true`, underlines the text in this element. Defaults to `false`.

#### Description {#description-8}

A limited style object for styling rich text `text` elements.

#### Inherited from {#inherited-from}

[`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable).[`style`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable#style)

* * *

### timestamp {#timestamp}

```text
timestamp: number;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:746

#### Description {#description-9}

A UNIX timestamp for the date to be displayed in seconds.

* * *

### type {#type}

```text
type: "date";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:742

#### Description {#description-10}

The type of element. In this case `type` is always `date`.

* * *

### url? {#url}

```text
optional url: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:774

#### Description {#description-11}

URL to link the entire `format` string to.
