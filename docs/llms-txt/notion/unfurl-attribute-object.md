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
- [Data source properties](/reference/property-object)

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

# Unfurl attribute (Link Previews)

A Link Preview is created from an array of unfurl attribute objects.

A [Link Preview](/docs/link-previews) is a real-time excerpt of authenticated content that unfurls in Notion when an authenticated user shares an enabled link. Developers can build Link Preview integrations to customize how links for domains they own look when the links unfurl in a Notion workspace. The display of the Link Preview is customizable in terms of content and layout.

> **👍 Learn how to build your own Link Preview integration**
> 
> - [Introduction to Link Preview integrations](/docs/link-previews) guide
> - [Build a Link Preview integration](/docs/build-a-link-preview-integration) guide
> - [Help Centre](https://www.notion.so/help/guides/notion-api-link-previews-feature) guide

Link Previews can be displayed in their full format, or they can be shown as a "Mention".

Let's first look at an example of a full-format Link Preview:

![1242](https://files.readme.io/a034247-link_preview.png)
*Example Link Preview in a Notion workspace*

Here is the same link again but now as a Mention — a miniature version of a Link Preview that uses the same data.

![1060](https://files.readme.io/f588a6f-mention.png)
*Example Mention in a Notion workspace*

A Link Preview or Mention displays data that is sent to Notion as an array of unfurl attribute objects. There are a number of optional attributes developers cannot. However, **every array must contain a** `title` attribute and a `dev` attribute.

Using the same Link Preview and Mention we saw above, let's look at the array of unfurl attribute objects that would render these previews. The following payload creates the example Link Preview and Mention above:

```json
[
  {
    "id": "title",
    "name": "Title",
    "type": "inline",
    "inline": {
      "title": {
        "value": "Feature Request: Link Previews",
        "section": "title"
      }
    }
  },
  {
    "id": "dev",
    "name": "Developer Name",
    "type": "inline",
    "inline": {
      "plain_text": {
        "value": "Acme Inc",
        "section": "secondary"
      }
    }
  },
  {
    "id": "state",
    "name": "State",
    "type": "relation",
    "relation": {
      "uri": "acme:item_state/open",
      "mention": {
        "section": "primary"
      }
    }
  },
  {
    "id": "itemId",
    "name": "Item Id",
    "type": "inline",
    "inline": {
      "plain_text": {
        "value": "#23487",
        "section": "identifier"
      }
    }
  },
  {
    "id": "itemIcon",
    "name": "Item Icon",
    "type": "inline",
    "inline": {
      "color": {
        "value": {
          "r": 247,
          "g": 247,
          "b": 42
        },
        "section": "entity"
      }
    }
  },
  {
    "id": "description",
    "name": "Description",
    "type": "inline",
    "inline": {
      "plain_text": {
        "value": "Would love to be able to preview some Acme resources in Notion!\nMaybe an open item?",
        "section": "body"
      }
    }
  },
  {
    "id": "updated_at",
    "name": "Updated At",
    "type": "inline",
    "inline": {
      "datetime": {
        "value": "2022-01-11T19:53:18.829Z",
        "section": "secondary"
      }
    }
  },
  {
    "id": "label",
    "name": "Label",
    "type": "inline",
    "inline": {
      "enum": {
        "value": "🔨 Ready to Build",
        "color": {
          "r": 100,
          "g": 100,
          "b": 100
        },
        "section": "primary"
      }
    }
  },
  {
    "id": "media",
    "name": "Embed",
    "embed": {
      "src_url": "https://c.tenor.com/XgaU95K_XiwAAAAC/kermit-typing.gif",
      "image": {
        "section": "embed"
      }
    }
  }
]
```

Each unfurl attribute object in this array maps to a different customizable section of a Link Preview. (To learn more about each section, jump to [The `section` value](/reference/unfurl-attribute-object#the-section-value).

![Anatomy of a Link Preview in Notion](https://files.readme.io/3d6f5ec-Untitled_1.png)
*Anatomy of a Link Preview in Notion*

First, let's let at the properties in each individual unfurl attribute object.

## The unfurl attribute object

### Inline sub-type objects

The key of inline sub-type objects represents the kind of sub-type. The values of the key are the `value` to display and the `section` of the Link Preview where the value is rendered.

| Sub-type | Description | Example value |
| --- | --- | --- |
| `color` | A color with r, b, g values. | `{ "value": { "r": 247, "g": 247, "b": 42 }, "section": "entity" }` |
| `date` | A date. | `{ "value": "2022-01-11", "section": "secondary" }` |
| `datetime` | A datetime. | `{ "value": "2022-01-11T19:53:18.829Z", "section": "secondary" }` |
| `enum` | A string value and optional color object. | `{ "value": "🔨 Ready to Build", "color": { "r": 100, "g": 100, "b": 100 }, "section": "primary" }` |
| `plain_text` | Any plain text content. | `{ "value": "Would love to be able to preview some Acme resources in Notion!\nMaybe an open item?", "section": "body" }` |
| `title`\* | The title of the Link Preview. *An unfurl attribute object of this type must be included in every payload to create a Link Preview.* | `{ "value": "Feature Request: Link Previews", "section": "title" }` |

#### The `dev` attribute

Every array of attribute objects that is sent to Notion to create a Link Preview must also include a `dev` attribute. The attribute indicates the developer or company who created the Link Preview. It takes the following format:

```json
{
    "id": "dev",
    "name": "Developer Name",
    "type": "inline",
    "inline": {
      "plain_text": {
        "value": "Acme Inc",
        "section": "secondary"
     }
 }
}
```
```

# Embed sub-type child objects

You can use the `embed` sub-type object to add rich content like JPGs, GIFs, or iFrames to your Link Preview.

![An example Link Preview that embeds an image of Kermit the Frog](https://files.readme.io/d482801-embed.png)

All embed sub-type objects contain: a `src_url` field that is a link to the embed, and an object whose key is the sub-type of the embed and whose value is an object indicating the `section` of the Link Preview where the value is rendered.

| Sub-type | Description | Example value |
| --- | --- | --- |
| `audio` | Audio from a source URL. | ```{   "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4",   "audio": {   "section": "embed"   } } ``` |
| `html` | HTML from a source URL that is rendered in an iFrame. | ```{   "src_url": "https://s3.us-east-3.amazonaws.com/12345.html",   "html": {   "section": "embed"   } } ``` |
| `image` | Image from a source URL. | ```{   "src_url": "https://s3.us-east-3.amazonaws.com/12345.png",   "image": {   "section": "avatar"   } } ``` |
| `video` | Video from a source URL. | ```{   "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4",   "video": {   "section": "embed"   } } ``` |

> There’s no need to ask a user to log in to your service in an iFrame embed. If they’re using a Link Preview, then they’ve already authenticated.

## The `section` value

The `section` value of an unfurl attribute object defines where an attribute is rendered in the Link Preview or Mention.

![The sections of a Link Preview](https://files.readme.io/121dcba-sections_lp.png)

![The sections of a Mention](https://files.readme.io/1de6886-sections_mention.png)

A `section` is specified in the sub-type object for the attribute. Refer to the table below for details about each `section` and its valid parent sub-types.

| Section | Description | Valid parent sub-types |
| --- | --- | --- |
| avatar | The picture found on the bottom left of a Link Preview. | `image`, `plain_text` |
| background | A background color for the Link Preview. | `color` |
| body | The main string content of a Link Preview. | `plain_text` |
| embed | The large space where the content of an `embed` attribute type is displayed in a Link Preview. | `audio`, `html`, `image`, `pdf`, `video` |
| entity | The small picture found in the subheading of a Link Preview and in a Mention. | `color`, `image` |
| identifier | The subheading found on the bottom of a Link Preview and on the left side of a Mention. | `image`, `plain_text` |
| primary | The first subheading section. | `enum`, `date`, `datetime`, `plain_text` |
| secondary | The second subheading section. | `date`, `datetime`, `plain_text` |
| title\* | The main heading in a Link Preview or Mention. *Required.* | `title` |

\*Required.
```