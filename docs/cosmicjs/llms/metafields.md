# Source: https://www.cosmicjs.com/docs/api/metafields.md

# Metafields

Learn about Metafields; the way you compose, extend, and connect the Object content model in Cosmic.

**What are Metafields?** Metafields are the way to add custom fields to your Objects. They are stored in the Object type and are not stored in the Object. They contain the data model, validation, etc.

**What is Metadata?** Metadata is the data you add to your Objects using the Metafields model. They contain the data values.

## Data model

| Parameter               |                         Required                         |       Type       | Description                                                                                                                                                                                      |
| :---------------------- | :------------------------------------------------------: | :--------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                  |                         required                         |       Enum       | text, textarea, html-textarea, select-dropdown, object, objects, file, files, date, radio-buttons, check-boxes, repeater, parent, markdown, json, switch, number, color, emoji                   |
| `title`                 |                         required                         |      String      | Your Metafield title                                                                                                                                                                             |
| `key`                   |                         required                         |      String      | Unique identifier for your Metafield                                                                                                                                                             |
| `value`                 |                          varies                          | Varies by `type` | Metafield value. Property required to be present (empty string ok) except for `repeater` and `parent` (should not be present). See example model below for various value types and requirements. |
| `required`              |                                                          |       Bool       | A value is required                                                                                                                                                                              |
| `regex`                 |                                                          |      String      | Restrict the value to match a regular expresssion                                                                                                                                                |
| `regex_message`         |                                                          |      String      | The message displayed when the value fails the regex                                                                                                                                             |
| `minlength`             |                                                          |      Number      | Add minlength to text or textarea Metafields                                                                                                                                                     |
| `maxlength`             |                                                          |      Number      | Add maxlength to text or textarea Metafields                                                                                                                                                     |
| `options`               | Required for `options`, `radio`, `checkbox` and `switch` | Varies by `type` | Array of options for select, radio, and checkbox Metafields and string for switch Metafield with possible values `true,false` and `yes,no`                                                       |
| `children`              |                                                          |      Array       | Array of nested Metafields                                                                                                                                                                       |
| `object_type`           |                                                          |      String      | Valid Object type slug. Applies only to `object` and `objects` Metafield                                                                                                                         |
| `repeater_fields`       |                                                          |      Array       | Array of nested Metafields. Applies only to `repeater` Metafield                                                                                                                                 |
| `media_validation_type` |                                                          |      String      | image, video, audio, application. Applies only to `file` and `files` Metafield                                                                                                                   |

## Adding and editing Metafields

When adding / editing Metafields to Object types using the API, use the following model for each Metafields type. Any value added to the `value` property is treated as a default value on each newly created Object.
```json
{
  "metafields": [
    {
      "type": "text",
      "title": "Headline",
      "key": "headline",
      "value": "3030 Palo Alto Blvd.",
      "required": true
    },
    {
      "type": "textarea",
      "title": "Basic Text",
      "key": "basic_text",
      "value": "This home is a must see!",
      "required": true
    },
    {
      "type": "html-textarea",
      "title": "Extended Text",
      "key": "extended_text",
      "value": "<p>Some <strong>HTML content</strong> for <em>dramatic</em> effect!</p>"
    },
    {
      "type": "markdown",
      "title": "Markdown Text",
      "key": "markdown_text",
      "value": "# Hello World!"
    },
    {
      "type": "select-dropdown",
      "title": "State",
      "key": "state",
      "value": "California",
      "options": [
        {
          "key": "CA",
          "value": "California"
        },
        {
          "key": "TX",
          "value": "Texas"
        }
      ]
    },
    {
      "type": "object",
      "title": "Author",
      "key": "author",
      "object_type": "authors",
      "value": "5a4806974fa85fc8a7000002" // Object ID
    },
    {
      "type": "objects",
      "title": "Categories",
      "key": "categories",
      "object_type": "categories",
      "value": ["5a4806974fa85fc8a7000007,5a4806974fa85fc8a7000008"] // Object IDs
    },
    {
      "type": "file",
      "title": "Hero",
      "key": "hero",
      "value": "media-name-property-in-bucket.jpg", // This is the name of your media.
      "media_validation_type": "image"
    },
    {
      "type": "files",
      "title": "Gallery",
      "key": "gallery",
      "value": [
        "gallery-image-1.jpg",
        "gallery-image-2.jpg",
        "gallery-image-3.jpg"
      ] // These are the names of your media.
    },
    {
      "type": "date",
      "title": "Listing Start Date",
      "key": "listing_start_date",
      "value": "2020-10-15"
    },
    {
      "type": "json",
      "title": "JSON Data",
      "key": "json_data",
      "value": {
        "strings": "cheese",
        "arrays": ["Bradbury", "Charles", "Ramono", "the last Jedi", "Liotta"],
        "objects": {
          "bools": true,
          "nestable": true
        }
      }
    },
    {
      "type": "radio-buttons",
      "title": "Deposit Required",
      "key": "deposit_required",
      "value": "The Other",
      "options": [
        {
          "value": "This"
        },
        {
          "value": "That"
        },
        {
          "value": "The Other"
        }
      ]
    },
    {
      "type": "check-boxes",
      "title": "Amenities",
      "key": "amenities",
      "value": ["Pool", "Gym"],
      "options": [
        {
          "value": "Pool"
        },
        {
          "value": "Gym"
        },
        {
          "value": "Landscaping"
        }
      ]
    },
    {
      "type": "switch",
      "title": "This is great",
      "key": "this_is_great",
      "value": true,
      "options": "true,false"
    },
    {
      "type": "color",
      "title": "Color",
      "key": "color",
      "value": "#29abe2"
    },
    {
      "type": "parent", // ! Value is not allowed for parent Metafield !
      "title": "Call Out Section",
      "key": "call_out_section",
      "children": [
        {
          "type": "text",
          "title": "Headline",
          "key": "headline",
          "value": "You're Going to Love it Here!"
        },
        {
          "type": "html-textarea",
          "title": "Section Content",
          "key": "section_content",
          "value": "<p>You are going to <strong>love</strong> it in Cosmic Village. The best place to raise a team!</p>"
        },
        {
          "type": "file",
          "title": "Hero",
          "key": "hero",
          "value": "big-beautiful-image.jpg",
          "media_validation_type": "image"
        }
      ]
    },
    {
      "type": "repeater", // ! Value is not allowed for repeater Metafield !
      "title": "Testimonials",
      "key": "testimonials",
      // Available repeaters
      "repeater_fields": [
        {
          "title": "Name",
          "key": "name",
          "value": "",
          "type": "text",
          "required": false
        },
        {
          "title": "Quote",
          "key": "quote",
          "value": "",
          "type": "text",
          "required": false
        }
      ]
    }
  ]
}

```
### Metafield Validation

You can use optional validation parameters to make sure editors using the web dashboard enter the correct values.

Reference the [Metafield model](/docs/api/metafields#data-model) to learn more.

| Parameter       | Required | Type   | Description                                          |
| --------------- | -------- | ------ | ---------------------------------------------------- |
| `required`      |          | Bool   | A value is required                                  |
| `regex`         |          | String | Restrict the value to match a regular expresssion    |
| `regex_message` |          | String | The message displayed when the value fails the regex |
| `minlength`     |          | Number | Add minlength to text or textarea Metafields         |
| `maxlength`     |          | Number | Add maxlength to text or textarea Metafields         |

### Example Metafields with validation
```json
{
  "title": "Users",
  "singular": "User",
  "slug": "users",
  "metafields": [
    {
      "key": "first_name",
      "title": "First Name",
      "type": "text",
      "required": true,
      "minlength": 2
    },
    {
      "key": "last_name",
      "title": "Last Name",
      "type": "text",
      "required": true,
      "minlength": 2
    },
    {
      "key": "email",
      "title": "Email",
      "type": "text",
      "regex": "/^([a-z0-9_.-]+)@([da-z.-]+).([a-z.]{2,6})$/",
      "regex_message": "You must enter a valid email."
    },
    {
      "key": "avatar",
      "title": "Avatar",
      "type": "file",
      "media_validation_type": "image"
    },
    {
      "key": "tagline",
      "title": "Tagline",
      "type": "text",
      "maxlength": 50
    }
  ]
}

```
## Fetching Metadata

When fetching Objects from the API, Metafields get converted into `key: value` pairs on the Object `metadata` property. See the [Objects model](/docs/api/objects) for more information.
```json
{
  "metadata": {
    "headline": "3030 Palo Alto Blvd.",
    "basic_text": "This home is a must see!",
    "extended_text": "<p>Some <strong>HTML content</strong> for <em>dramatic</em> effect!</p>",
    "markdown_text": "# Hello World!",
    "state": "California",
    "author": {
      "title": "Author Name",
      "metadata": {
        "image": {
          "url": "https://cdn.cosmicjs.com/author-headshot.jpg",
          "imgix_url": "https://imgix.cosmicjs.com/author-headshot.jpg"
        }
      }
      // May include more nested data
    },
    "categories": [
      {
        "title": "Category 1"
        // May include more nested data
      },
      {
        "title": "Category 2"
        // May include more nested data
      },
    ],
  "hero": "https://cdn.cosmicjs.com/media-name-property-in-bucket.jpg",
  "gallery": [
    {
      "url": "https://cdn.cosmicjs.com/gallery-image-1.jpg",
      "imgix_url": "https://imgix.cosmicjs.com/gallery-image-1.jpg"
    },
    {
      "url": "https://cdn.cosmicjs.com/gallery-image-2.jpg",
      "imgix_url": "https://imgix.cosmicjs.com/gallery-image-2.jpg"
    },
    {
      "url": "https://cdn.cosmicjs.com/gallery-image-3.jpg",
      "imgix_url": "https://imgix.cosmicjs.com/gallery-image-3.jpg"
    },
  ],
  "listing_start_date": "2020-10-15",
  "json_data": {
    "strings": "cheese",
    "arrays": ["Bradbury", "Charles", "Ramono", "the last Jedi", "Liotta"],
    "objects": {
      "bools": true,
      "nestable": true
    }
  },
  "deposit_required": "The Other",
  "amenities": ["Pool", "Gym"],
  "this_is_great": true,
  "call_out_section": {
    "headline": "You're Going to Love it Here!",
    "section_content": "<p>You are going to <strong>love</strong> it in Cosmic Village. The best place to raise a team!</p>",
    "hero": {
      "url": "https://cdn.cosmicjs.com/big-beautiful-image.jpg",
      "imgix_url": "https://imgix.cosmicjs.com/big-beautiful-image.jpg"
    }
  },
  "testimonials": [
    {
      "name": "Fiona Apple",
      "quote": "This is the best place in the LA area!"
    },
    {
      "name": "Jon Brion",
      "quote": "I came for the great music, I stayed for the good vibes."
    }
  ]
}

```