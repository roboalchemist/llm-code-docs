# Source: https://developers.notion.com/reference/unfurl-attribute-object.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unfurl attribute (Link Previews)

> A Link Preview is created from an array of unfurl attribute objects.

A [Link Preview](/guides/link-previews/link-previews) is a real-time excerpt of authenticated content that unfurls in Notion when an authenticated user shares an enabled link. Developers can build Link Preview integrations to customize how links for domains they own look when the links unfurl in a Notion workspace. The display of the Link Preview is customizable in terms of content and layout.

<Check>
  **Learn how to build your own Link Preview integration**

  * [Introduction to Link Preview integrations](/guides/link-previews/link-previews) guide
  * [Build a Link Preview integration](/guides/link-previews/build-a-link-preview-integration) guide
  * [Help Centre](https://www.notion.so/help/guides/notion-api-link-previews-feature) guide
</Check>

Link Previews can be displayed in their full format, or they can be shown as a "Mention".

Let's first look at an example of a full-format Link Preview:

<Frame caption="Example Link Preview in a Notion workspace">
  <img src="https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/a034247-link_preview.png?fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=ce1abef0ec570f35bd482fdd8c6dc552" width="1242" height="246" data-path="images/reference/a034247-link_preview.png" />
</Frame>

Here is the same link again but now as a Mention — a miniature version of a Link Preview that uses the same data.

<Frame caption="Example Mention in a Notion workspace">
  <img src="https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/f588a6f-mention.png?fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=8fb360ddae135021a789f072cc2ba88d" width="1060" height="108" data-path="images/reference/f588a6f-mention.png" />
</Frame>

A Link Preview or Mention displays data that is sent to Notion as an array of unfurl attribute objects. There are a number of optional attributes developers cannot. However, **every array must contain a `title` attribute and a `dev` attribute.**

Using the same Link Preview and Mention we saw above, let's look at the array of unfurl attribute objects that would render these previews. The following payload creates the example Link Preview and Mention above:

<CodeGroup>
  ```json JSON expandable theme={null}
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
          "value": "Would love to be able to preview some Acme resources in Notion!\n Maybe an open item?",
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
</CodeGroup>

Each unfurl attribute object in this array maps to a different customizable section of a Link Preview. (To learn more about each section, jump to [The `section` value](/reference/unfurl-attribute-object#the-section-value).

<Frame caption="Anatomy of a Link Preview in Notion">
  <img src="https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/3d6f5ec-Untitled_1.png?fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=4c9dc387fecc9d2d606377e68d06d9b3" width="1378" height="818" data-path="images/reference/3d6f5ec-Untitled_1.png" />
</Frame>

First, let's let at the properties in each individual unfurl attribute object.

## The unfurl attribute object

<CodeGroup>
  ```json Example unfurl attribute object theme={null}
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
    }
  ```
</CodeGroup>

Each unfurl attribute object contains the following values:

| Field                 | Type                  | Description                                                                                                                                                    | Example value                                                                    |
| :-------------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| `id`                  | `string`              | A unique identifier for the attribute. If more than one attribute with the same `id` is provided, then the latter attribute overrides the value of the first.  | `"title"`                                                                        |
| `name`                | `string`              | A human readable name describing the attribute.                                                                                                                | `"Title"`                                                                        |
| `type`                | `inline` \|\| `embed` | The type of attribute. Most attributes are `inline`. Use `embed` for rich media sub-types like `image`, `video`, or `audio`.                                   | `"inline"`                                                                       |
| `inline` \|\| `embed` | `object`              | An object whose key is a sub-type. The child sub-type object includes the `value` to display and the `section` of the Link Preview where the data is rendered. | `{ "title": { "value": "Feature Request: Link Previews", "section": "title" } }` |

### Inline sub-type objects

The key of inline sub-type objects represents the kind of sub-type. The values of the key are the `value` to display and the `section` of the Link Preview where the value is rendered.

| Sub-type     | Description                                                                                                                          | Example value                                                                                                             |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| `color`      | A color with r, b, g values.                                                                                                         | `{ "value": { "r": 247, "g": 247, "b": 42 }, "section": "entity" }`                                                       |
| `date`       | A date.                                                                                                                              | `{ "value": "2022-01-11", "section": "secondary" }`                                                                       |
| `datetime`   | A datetime.                                                                                                                          | `{ "value": "2022-01-11T19:53:18.829Z", "section": "secondary" }`                                                         |
| `enum`       | A string value and optional color object.                                                                                            | `{ "value": "🔨 Ready to Build", "color": { "r": 100, "g": 100, "b": 100 }, "section": "primary" }`                       |
| `plain_text` | Any plain text content.                                                                                                              | `{ "value": "Would love to be able to preview some Acme resources in Notion!\n Maybe an open item?", "section": "body" }` |
| `title`\*    | The title of the Link Preview. \*An unfurl attribute object of this type must be included in every payload to create a Link Preview. | `{ "value": "Feature Request: Link Previews", "section": "title" }`                                                       |

#### The `dev` attribute

Every array of attribute objects that is sent to Notion to create a Link Preview must also include a `dev` attribute. The attribute indicates the developer or company who created the Link Preview. It takes the following format:

<CodeGroup>
  ```json Example dev attribute theme={null}
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
</CodeGroup>

### Embed sub-type child objects

You can use the `embed` sub-type object to add rich content like JPGs, GIFs, or iFrames to your Link Preview.

<Frame caption="An example Link Preview that embeds an image of Kermit the Frog">
  <img src="https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/d482801-embed.png?fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=23c25fb4d7c3eb461655767f2dffb63a" width="1228" height="806" data-path="images/reference/d482801-embed.png" />
</Frame>

All embed sub-type objects contain: a `src_url` field that is a link to the embed, and an object whose key is the sub-type of the embed and whose value is an object indicating the `section` of the Link Preview where the value is rendered.

| Sub-type | Description                                           | Example value                                                                                     |
| -------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `audio`  | Audio from a source URL.                              | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "audio": { "section": "embed" } }`  |
| `html`   | HTML from a source URL that is rendered in an iFrame. | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.html", "html": { "section": "embed" } }`  |
| `image`  | Image from a source URL.                              | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.png", "image": { "section": "avatar" } }` |
| `video`  | Video from a source URL.                              | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "video": { "section": "embed" } }`  |

<Note>
  There’s no need to ask a user to log in to your service in an iFrame embed. If they’re using a Link Preview, then they’ve already authenticated.
</Note>

### The `section` value

The `section` value of an unfurl attribute object defines where an attribute is rendered in the Link Preview or Mention.

<Frame caption="The sections of a Link Preview">
  <img src="https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/121dcba-sections_lp.png?fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=3aeb3186980cfe813930568826de3adf" width="1378" height="818" data-path="images/reference/121dcba-sections_lp.png" />
</Frame>

<br />

<Frame caption="The sections of a Mention">
  <img src="https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/1de6886-sections_mention.png?fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=103ce514aa4462c145d50c0ac95653d7" width="926" height="172" data-path="images/reference/1de6886-sections_mention.png" />
</Frame>

A `section` is specified in the sub-type object for the attribute. Refer to the table below for details about each `section` and its valid parent sub-types.

| Section    | Description                                                                                    | Valid parent sub-types                   |
| :--------- | :--------------------------------------------------------------------------------------------- | :--------------------------------------- |
| avatar     | The picture found on the bottom left of a Link Preview.                                        | `image`, `plain_text`                    |
| background | A background color for the Link Preview.                                                       | `color`                                  |
| body       | The main string content of a Link Preview.                                                     | `plain_text`                             |
| embed      | The large space where the content of an `embed` attribute type is displayed in a Link Preview. | `audio`, `html`, `image`, `pdf`, `video` |
| entity     | The small picture found in the subheading of a Link Preview and in a Mention.                  | `color`, `image`                         |
| identifier | The subheading found on the bottom of a Link Preview and on the left side of a Mention.        | `image`, `plain_text`                    |
| primary    | The first subheading section.                                                                  | `enum`, `date`, `datetime`, `plain_text` |
| secondary  | The second subheading section.                                                                 | `date`, `datetime`, `plain_text`         |
| title\*    | The main heading in a Link Preview or Mention. \*Required.                                     | `title`                                  |


Built with [Mintlify](https://mintlify.com).