# Notion API

## Objects

### Block
- [Rich text](/reference/rich-text)

### Page
- [Page properties](/reference/page-property-values)
  - [Page property items](/reference/property-item-object)

### Database
- [Database](/reference/database)

### Data source
- [Data source properties](/reference/data-source)

### Comment
- [Comment attachment](/reference/comment-attachment)
- [Comment display name](/reference/comment-display-name)

### File
- [File Upload](/reference/file-upload)

### User
- [User](/reference/user)

### Parent
- [Parent](/reference/parent-object)

### Emoji
- [Emoji](/reference/emoji-object)

### Unfurl attribute (Link Previews)
- [Unfurl attribute (Link Previews)](/reference/unfurl-attribute-object)

## Endpoints

### Authentication
- [Create a token](/reference/create-a-token) (post)
- [Introspect token](/reference/introspect-token) (post)
- [Revoke token](/reference/revoke-token) (post)
- [Refresh a token](/reference/refresh-a-token) (post)

### Blocks
- [Append block children](/reference/append-block-children) (patch)
- [Retrieve a block](/reference/retrieve-a-block) (get)
- [Retrieve block children](/reference/retrieve-block-children) (get)
- [Update a block](/reference/update-a-block) (patch)
- [Delete a block](/reference/delete-a-block) (del)

### Pages
- [Create a page](/reference/create-a-page) (post)
- [Retrieve a page](/reference/retrieve-a-page) (get)
- [Retrieve a page property item](/reference/retrieve-a-page-property) (get)
- [Update page](/reference/update-page)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (post)
- [List databases](/reference/list-databases) (get)
- [Delete a database](/reference/delete-database) (del)
```

# API Reference

## Database Operations

- [Create a database](https://docs.nestbase.com/reference/database-create)
- [Update a database](https://docs.nestbase.com/reference/database-update)
- [Retrieve a database](https://docs.nestbase.com/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.nestbase.com/reference/create-a-data-source)
- [Update a data source](https://docs.nestbase.com/reference/update-a-data-source)
  - [Update data source properties](https://docs.nestbase.com/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.nestbase.com/reference/retrieve-a-data-source)
- [Query a data source](https://docs.nestbase.com/reference/query-a-data-source)
  - [Filter data source entries](https://docs.nestbase.com/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.nestbase.com/reference/sort-data-source-entries)
- [List data source templates](https://docs.nestbase.com/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.nestbase.com/reference/create-a-database)
- [Query a database](https://docs.nestbase.com/reference/post-database-query)
  - [Filter database entries](https://docs.nestbase.com/reference/post-database-query-filter)
  - [Sort database entries](https://docs.nestbase.com/reference/post-database-query-sort)
- [Retrieve a database](https://docs.nestbase.com/reference/retrieve-a-database)
- [Update a database](https://docs.nestbase.com/reference/update-a-database)
  - [Update database properties](https://docs.nestbase.com/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.nestbase.com/reference/get-databases)

### Comments

- [Create comment](https://docs.nestbase.com/reference/create-a-comment)
- [Retrieve a comment](https://docs.nestbase.com/reference/retrieve-comment)
- [List comments](https://docs.nestbase.com/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.nestbase.com/reference/create-a-file-upload)
- [Send a file upload](https://docs.nestbase.com/reference/send-a-file-upload)
- [Complete a file upload](https://docs.nestbase.com/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.nestbase.com/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.nestbase.com/reference/list-file-uploads)

### Search

- [Search](https://docs.nestbase.com/reference/post-search)
```

# Rich text

Notion uses rich text to allow users to customize their content. Rich text refers to a type of document where content can be styled and formatted in a variety of customizable ways. This includes styling decisions, such as the use of italics, font size, and font color, as well as formatting, such as the use of hyperlinks or code blocks.

Notion includes rich text objects in [block objects](/reference/block) to indicate how blocks in a page are represented. [Blocks](/reference/block) that support rich text will include a rich text object; however, not all block types offer rich text.

When blocks are retrieved from a page using the [Retrieve a block](/reference/retrieve-a-block) or [Retrieve block children](/reference/get-block-children) endpoints, an array of rich text objects will be included in the block object (when available). Developers can use this array to retrieve the plain text (`plain_text`) for the block or get all the rich text styling and formatting options applied to the block.

```json
{
  "type": "text",
  "text": {
    "content": "Some words ",
    "link": null
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "Some words ",
  "href": null
}
```

> Many [block types](/reference/block#block-type-objects) support rich text. In cases where it is supported, a `rich_text` object will be included in the block `type` object. All `rich_text` objects will include a `plain_text` property, which provides a convenient way for developers to access unformatted text from the Notion block.

Each rich text object contains the following fields.

| Field            | Type               | Description                                                                 | Example value |
| ---------------- | ------------------ | --------------------------------------------------------------------------- | ------------- |
| `type`           | `string` (enum)     | The type of this rich text object. Possible type values are: `"text"`, `"mention"`, `"equation"`. | `"text"`      |
| `text` | `object` | An object containing type-specific configuration.<br/>Refer to the rich text type objects section below for details on type-specific values. | Refer to the rich text type objects section below for examples. |
| `annotations`   | `object`          | The information used to style the rich text object. Refer to the annotation object section below for details. | Refer to the annotation object section below for examples. |
| `plain_text`    | `string`          | The plain text without annotations.                                           | `"Some words "` |
| `href`           | `string` (optional) | The URL of any link or Notion mention in this text, if any.                | `"https://www.notion.so/Avocado-d093f1d200464ce78b36e58a3f0d8043"` |

## The annotation object

All rich text objects contain an `annotations` object that sets the styling for the rich text. `annotations` includes the following fields:

| Property              | Type               | Description                                                                 | Example value |
|-----------------------|--------------------|-----------------------------------------------------------------------------|---------------|
| `bold`               | `boolean`         | Whether the text is **bolded**.                                               | `true`        |
| `italic`             | `boolean`         | Whether the text is _italicized_.                                             | `true`        |
| `strikethrough`       | `boolean`         | Whether the text is struck through.                                            | `false`       |
| `underline`           | `boolean`         | Whether the text is underlined.                                                | `false`       |
| `code`               | `boolean`         | Whether the text is `code style`.                                               | `true`        |
| `color`              | `string` (enum)     | Color of the text. Possible values include: - `"blue"` - `"blue_background"` - `"brown"` - `"brown_background"` - `"default"` - `"gray"` - `"gray_background"` - `"green"` - `"green_background"` - `"orange"` - `"orange_background"` - `"pink"` - `"pink_background"` - `"purple"` - `"purple_background"` - `"red"` - `"red_background"` - `"yellow"` - `"yellow_background"` | `"green"`      |

## Rich text type objects

### Equation

Notion supports inline LaTeX equations as rich text object’s with a type value of `"equation"`. The corresponding equation type object contains the following:

| Field            | Type               | Description                                                                 | Example value                    |
| ---------------- | ------------------ | --------------------------------------------------------------------------- | -------------------------------- |
| `expression`     | `string`           | The LaTeX string representing the inline equation.                            | `"\frac{{ - b \pm \sqrt {b^2 - 4ac} }}{{2a}}"` |

#### Example rich text equation object

```json
{
  "type": "equation",
  "expression": "\\frac{{ - b \\pm \\sqrt {b^2 - 4ac} }}{2a}"
}
``` 
```

# Example rich text

## JSON

```json
{
  "type": "equation",
  "equation": {
    "expression": "E = mc^2"
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "E = mc^2",
  "href": null
}
```

## Mention

Mention objects represent an inline mention of a database, date, link preview mention, page, template mention, or user. A mention is created in the Notion UI when a user types `@` followed by the name of the reference.

If a rich text object’s `type` value is `"mention"`, then the corresponding `mention` object contains the following:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `type` | `string` (enum) | The type of the inline mention. Possible values include: <br/> - `"database"` <br/> - `"date"` <br/> - `"link_preview"` <br/> - `"page"` <br/> - `"template_mention"` <br/> - `"user"` | `"user"` |
| `database` | `object` | An object containing type-specific configuration. Refer to the mention type object sections below for details. | Refer to the mention type object sections below for example values. |

### Database mention type object

Database mentions contain a database reference within the corresponding `database` field. A database reference is an object with an `id` key and a string value (UUIDv4) corresponding to a database ID.

If an integration doesn’t have [access](/reference/capabilities) to the mentioned database, then the mention is returned with just the ID. The `plain_text` value that would be a title appears as `"Untitled"` and the annotation object’s values are defaults.

_Example rich text `mention` object for a `database` mention_

```json
{
  "type": "mention",
  "mention": {
    "type": "database",
    "database": {
      "id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "Database with test things",
  "href": "https://www.notion.so/a1d8501e1ac143e9a6bdea9fe6c8822b"
}
```

### Date mention type object

Date mentions contain a [date property value object](/reference/property-value-object#date-property-values) within the corresponding `date` field.

_Example rich text `mention` object for a `date` mention_

```json
{
  "type": "mention",
  "mention": {
    "type": "date",
    "date": {
      "start": "2022-12-16",
      "end": null
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "2022-12-16",
  "href": null
}
```

### Link Preview mention type object

If a user opts to share a [Link Preview](/docs/link-previews) as a mention, then the API handles the Link Preview mention as a rich text object with a `type` value of `link_preview`. Link preview rich text mentions contain a corresponding `link_preview` object that includes the `url` that is used to create the Link Preview mention.

_Example rich text `mention` object for a `link_preview` mention_

```json
{
  "type": "mention",
  "mention": {
    "type": "link_preview",
    "link_preview": {
      "url": "https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD",
  "href": "https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD"
}
```

### Page mention type object

Page mentions contain a page reference within the corresponding `page` field. A page reference is an object with an `id` property and a string value (UUIDv4) corresponding to a page ID.

If an integration doesn’t have [access](/reference/capabilities) to the mentioned page, then the mention is returned with just the ID. The `plain_text` value that would be a title appears as `"Untitled"` and the annotation object’s values are defaults.

_Example rich text `mention` object for a `page` mention_

```json
{
  "type": "mention",
  "mention": {
    "type": "page",
    "page": {
      "id": "3c612f56-fdd0-4a30-a4d6-bda7d7426309"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "This is a test page",
  "href": "https://www.notion.so/3c612f56fdd04a30a4d6bda7d7426309"
}
```

### Template mention type object

The content inside a [template button](https://www.notion.so/help/template-buttons) in the Notion UI can include placeholder date and user mentions that populate when a template is duplicated. Template mention type objects contain these populated values.

Template mention rich text objects contain a `template_mention` object with a nested `type` key that is either `"template_mention_date"` or `"template_mention_user"`.

If the `type` key is `"template_mention_date"`, then the rich text object contains the following `template_mention_date` field:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `template_mention_date` | `string` (enum) | The type of the date mention. Possible values include: <br/> - `"today"` <br/> - `"now"` | `"today"` |

_Example rich text `mention` object for a `template_mention_date` mention_

```json
{
  "type": "mention",
  "mention": {
    "type": "template_mention",
    "template_mention": {
      "type": "template_mention_date",
      "template_mention_date": "today"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "@Today",
  "href": null
}
```

If the `type` key is `"template_mention_user"`, then the rich text object contains the following `template_mention_user` field:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `template_mention_user` | `string` (enum) | The type of the user mention. The only possible value is `"me"`. | `"me"` |

_Example rich text `mention` object for a `template_mention_user` mention_

```json
{
  "type": "mention",
  "mention": {
    "type": "template_mention",
    "template_mention": {
      "type": "template_mention_user",
      "template_mention_user": "me"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "@Me",
  "href": null
}
```

### User mention type object

If a rich text object’s `type` value is `"user"`, then the corresponding user field contains a [user mention](/reference/user).

_Example rich text `mention` object for a `user` mention_

```json
{
  "type": "mention",
  "mention": {
    "type": "user",
    "user": {
      "name": "John Doe",
      "profile_image_url": "https://example.com/profile.jpg"
    }
  },
  "annotations": {
    "bold": true,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "blue"
  },
  "plain_text": "Hello, John! How are you?",
  "href": "https://example.com/profile.jpg"
}
```

# The Annotation Object

A rich text object includes an object called `annotation` which can contain annotations like bold, italic, underline, color, and more.

## The Annotation Object

A rich text object includes an object called `annotation` which can contain annotations like bold, italic, underline, color, and more.

### Rich Text Type Objects

#### Equation

An equation is created using mathematical notation. An equation can be created using one or more terms, each of which can be a number, letter, or variable.

**Example:**
```json
{
  "type": "equation",
  "equation": [
    {
      "term": "x"
    },
    {
      "term": "y"
    },
    {
      "term": "z"
    }
  ]
}
```

#### Mention

A mention is created when you want to reference another user's profile. You can do this by specifying the username of the person you want to mention.

**Example:**
```json
{
  "type": "mention",
  "mention": {
    "type": "user",
    "user": {
      "object": "user",
      "id": "b2e19928-b427-4aad-9a9d-fde65479b1d9"
    }
  }
}
```

#### Text

Text is the most common type of content in Notion. It can be used to describe anything from simple paragraphs to complex documents.

**Example:**
```json
{
  "type": "text",
  "text": "This is a sample text."
}
```

### Text

If a rich text object’s `type` value is `"text"`, then the corresponding `text` field contains an object including the following:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `content` | `string` | The actual text content of the text. | `"Some words "` |
| `link` | `object` (optional) | An object with information about any inline link in this text, if included.<br>If the text contains an inline link, then the object key is `url` and the value is the URL’s string web address.<br>If the text doesn’t have any inline links, then the value is `null`. | `{ "url": "https://developers.notion.com/" }` |

#### Example rich text `text` object without link

```json
{
  "type": "text",
  "text": {
    "content": "This is an ",
    "link": null
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "This is an ",
  "href": null
}
```

#### Example rich `text` text object with link

```json
{
  "type": "text",
  "text": {
    "content": "inline link",
    "link": {
      "url": "https://developers.notion.com/"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "inline link",
  "href": "https://developers.notion.com/"
}
```