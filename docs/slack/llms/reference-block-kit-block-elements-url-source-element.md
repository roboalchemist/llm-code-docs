Source: https://docs.slack.dev/reference/block-kit/block-elements/url-source-element

# URL source element

## Fields {#fields}

Field

Type

Description

Required?

`type`

String

The type of element. In this case `type` is always `url`.

Required

`url`

String

The URL type source.

Required

`text`

String

Display text for the URL.

Required

## Usage info {#usage-info}

The URL source element is used to display clickable URL references within a [task card block](/reference/block-kit/blocks/task-card-block). It cannot be used within other blocks.

## Examples {#examples}

A URL source element:

```json
{  "type": "url",  "url": "https://docs.slack.dev/",  "text": "Slack API docs"}
```text

Example within a task card block:

```json
{  "type": "task_card",  "task_id": "task_1",  "title": "Scientific findings",  "status": "complete",  "sources": [    {      "type": "url",      "url": "https://docs.example.com/",      "text": "Tracy's delightful docs"    },    {      "type": "url",      "url": "https://research.example.com/",      "text": "Haley's resourceful research"    }  ]}
```text
