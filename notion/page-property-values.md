# Source: https://developers.notion.com/reference/page-property-values

## [](https://developers.notion.com/reference/page-property-values#overview)
A [page object](https://developers.notion.com/reference/page) is made up of page properties that contain data about the page.
When you send a request to [Create a page](https://developers.notion.com/reference/post-page), set the page properties in the `properties` object body parameter.
[Retrieve a page](https://developers.notion.com/reference/retrieve-a-page) surfaces the identifier, type, and value of a page’s properties.
[Retrieve a page property item](https://developers.notion.com/reference/retrieve-a-page-property) returns information about a single property ID. Especially for formulas, rollups, and relations, Notion recommends using this API to ensure you get an accurate, up-to-date property value that isn't truncating any results. Refer to [Page property items](https://developers.notion.com/reference/property-item-object) for specific API shape details when using this endpoint.
An [Update page](https://developers.notion.com/reference/patch-page) query modifies the page property values specified in the `properties` object body param. 
> ## 👍
> Pages that live in a data source are easier to query and manage
> **Page properties** are most useful when interacting with a page that is an entry in a data source, represented as a row in the Notion app UI.
> If a page is not part of a data source, then its only available property is its `title`.
## [](https://developers.notion.com/reference/page-property-values#attributes)
Each page property value object contains the following fields:
Field | Type | Description | Example value  
---|---|---|---  
`id` | `string` | An underlying identifier for the property. Historically, this may be a UUID, but newer IDs are a short ID that's always URL-encoded in the API and in [integration webhooks](https://developers.notion.com/reference/webhooks).  
  
`id` may be used in place of name when creating or updating pages.  
  
`id` remains constant when the property name changes. | `"f%5C%5C%3Ap"`  
`type` |  `string` (enum) | The type of the property in the page object. Possible type values are:  
  
- [`checkbox`](https://developers.notion.com/reference/page-property-values#checkbox)  
- [`created_by`](https://developers.notion.com/reference/page-property-values#created-by)  
- [`created_time`](https://developers.notion.com/reference/page-property-values#created-time)  
- [`date`](https://developers.notion.com/reference/page-property-values#date)  
- [`email`](https://developers.notion.com/reference/page-property-values#email)  
- [`files`](https://developers.notion.com/reference/page-property-values#files)  
- [`formula`](https://developers.notion.com/reference/page-property-values#formula)  
- [`last_edited_by`](https://developers.notion.com/reference/page-property-values#last-edited-by)  
- [`last_edited_time`](https://developers.notion.com/reference/page-property-values#last-edited-time)  
- [`multi_select`](https://developers.notion.com/reference/page-property-values#multi-select)  
- [`number`](https://developers.notion.com/reference/page-property-values#number)  
- [`people`](https://developers.notion.com/reference/page-property-values#people)  
- [`phone_number`](https://developers.notion.com/reference/page-property-values#phone-number)  
- [`relation`](https://developers.notion.com/reference/page-property-values#relation)  
- [`rollup`](https://developers.notion.com/reference/page-property-values#rollup)  
- [`rich_text`](https://developers.notion.com/reference/page-property-values#rich-text)  
- [`select`](https://developers.notion.com/reference/page-property-values#select)  
- [`status`](https://developers.notion.com/reference/page-property-values#status)  
- [`title`](https://developers.notion.com/reference/page-property-values#title)  
- [`url`](https://developers.notion.com/reference/page-property-values#url)  
- [`unique_id`](https://developers.notion.com/reference/page-property-values#unique-id)  
- [`verification`](https://developers.notion.com/reference/page-property-values#verification)Refer to specific type sections below for details on type-specific values. | `"rich_text"`  
[`checkbox`](https://developers.notion.com/reference/page-property-values#checkbox)  
[`created_by`](https://developers.notion.com/reference/page-property-values#created-by)  
[`created_time`](https://developers.notion.com/reference/page-property-values#created-time)  
[`date`](https://developers.notion.com/reference/page-property-values#date)  
[`email`](https://developers.notion.com/reference/page-property-values#email)  
[`files`](https://developers.notion.com/reference/page-property-values#files)  
[`formula`](https://developers.notion.com/reference/page-property-values#formula)  
[`last_edited_by`](https://developers.notion.com/reference/page-property-values#last-edited-by)  
[`last_edited_time`](https://developers.notion.com/reference/page-property-values#last-edited-time)  
[`multi_select`](https://developers.notion.com/reference/page-property-values#multi-select)  
[`number`](https://developers.notion.com/reference/page-property-values#number)  
[`people`](https://developers.notion.com/reference/page-property-values#people)  
[`phone_number`](https://developers.notion.com/reference/page-property-values#phone-number)  
[`relation`](https://developers.notion.com/reference/page-property-values#relation)  
[`rollup`](https://developers.notion.com/reference/page-property-values#rollup)  
[`rich_text`](https://developers.notion.com/reference/page-property-values#rich-text)  
[`select`](https://developers.notion.com/reference/page-property-values#select)  
[`status`](https://developers.notion.com/reference/page-property-values#status)  
[`title`](https://developers.notion.com/reference/page-property-values#title)  
[`url`](https://developers.notion.com/reference/page-property-values#url)  
[`unique_id`](https://developers.notion.com/reference/page-property-values#unique-id)  
[`verification`](https://developers.notion.com/reference/page-property-values#verification) | `object` | A type object that contains data specific to the page property type, including the page property value.  
  
Refer to the [type objects section](https://developers.notion.com/reference/page-property-values#type-objects) for descriptions and examples of each type. | `"checkbox": true`  
> ## 📘
> Size limits for page property values
> For information about size limitations for specific page property objects, refer to the [limits for property values documentation](https://developers.notion.com/reference/request-limits#limits-for-property-values).
When returned from the [Retrieve page property item](https://developers.notion.com/changelog/retrieve-page-property-values) API, there's an additional field, `object`, which is always the string `"property_item"`, as described in [Page property items](https://developers.notion.com/reference/property-item-object).
## [](https://developers.notion.com/reference/page-property-values#type-objects)
### [](https://developers.notion.com/reference/page-property-values#checkbox)
Field | Type | Description | Example value  
---|---|---|---  
`checkbox` | `boolean` | Whether the checkbox is checked (`true`) or unchecked (`false`). | `true`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `checkbox` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-checkbox-page-property-value)
JSON
```
{
  "properties": {
    "Task completed": {
      "checkbox": true
    }
  }
}

```

#### 
`checkbox` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-checkbox-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Task completed": {
    "id": "ZI%40W",
    "type": "checkbox",
    "checkbox": true
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#created-by)
Field | Type | Description | Example value  
---|---|---|---  
`created_by` | `object` | A [user object](https://developers.notion.com/reference/user) containing information about the user who created the page.  
  
`created_by` can’t be updated. | Refer to the example response objects below.  
#### 
`created_by` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-created_by-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "created_by": {
    "object": "user",
    "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#created-time)
Field | Type | Description | Example value  
---|---|---|---  
`created_time` |  `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time) | The date and time that the page was created.  
  
The `created_time` value can’t be updated. | `"2022-10-12T16:34:00.000Z"`  
#### 
`created_time` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-created_time-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Created time": {
    "id": "eB_%7D",
    "type": "created_time",
    "created_time": "2022-10-24T22:54:00.000Z"
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#date)
If the `type` of a page property value is `"date"`, then the property value contains a `"date"` object with the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`end` |  `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time) | (Optional) A string representing the end of a date range.  
  
If the value is `null`, then the date value is not a range. | `"2020-12-08T12:00:00Z"`  
`start` |  `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time) | A date, with an optional time.  
  
If the `date` value is a range, then `start` represents the start of the range. | `"2020-12-08T12:00:00Z”`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a date page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-date-page-property-value)
JSON
```
{
  "properties": {
    "Due date": {
      "date": {
        "start": "2023-02-23"
      }
    }
  }
}

```

#### 
`date` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-date-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Due date": {
    "id": "M%3BBw",
    "type": "date",
    "date": {
      "start": "2023-02-07",
      "end": null,
      "time_zone": null
    }
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#email)
Field | Type | Description | Example value  
---|---|---|---  
`email` | `string` | A string describing an email address. | `"ada@makenotion.com"`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates an `email` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-an-email-page-property-value)
JSON
```
{
  "properties": {
    "Email": {
      "email": "ada@makenotion.com"
    }
  }
}

```

#### 
`email` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-email-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Email": {
    "id": "y%5C%5E_",
    "type": "email",
    "email": "ada@makenotion.com"
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#files)
Field | Type | Description | Example value  
---|---|---|---  
`files` | array of [file objects](https://developers.notion.com/reference/file-object) | An array of objects containing information about the files. | Refer to the example response objects below.  
#### 
`files` property
[](https://developers.notion.com/reference/page-property-values#example-creation-or-update-of-files-property)
The following is an example `properties` body parameter for a `POST` or `PATCH` page request that creates or updates a `files` page property value.
When providing an `external` URL, the `name` parameter is required.
When providing a `file_upload`, the `name` is optional and defaults to the `filename` of the original [File Upload](https://developers.notion.com/reference/file-upload).
JSON
```
{
  "properties": {
    "Blueprint": {
      "files": [
        {
          "name": "Project Alpha blueprint",
          "external": {
            "url": "https://www.figma.com/file/g7eazMtXnqON4i280CcMhk/project-alpha-blueprint?node-id=0%3A1&t=nXseWIETQIgv31YH-1"
          }
        }
      ]
    }
  }
}

```

#### 
`files` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-files-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Blueprint": {
    "id": "tJPS",
    "type": "files",
    "files": [
      {
        "name": "Project blueprint",
        "type": "external",
        "external": {
          "url": "https://www.figma.com/file/g7eazMtXnqON4i280CcMhk/project-alpha-blueprint?node-id=0%3A1&t=nXseWIETQIgv31YH-1"
        }
      }
    ]
  }
}

```

> ## 📘
> Array parameter overwrites the entire existing value
> When updating a `files` page property value, the value is overwritten by the new array of `files` passed.
> If you pass a `file` object containing a file hosted by Notion, it remains one of the files. To remove any file, don't pass it in the update request.
### [](https://developers.notion.com/reference/page-property-values#formula)
Formula property value objects represent the result of evaluating a formula described in the  
[data source's properties](https://developers.notion.com/reference/data%20source). 
If the `type` of a page property value is `"formula"`, then the property value contains a `"formula"` object with the following fields:
Field | Type | Description | Example value  
---|---|---|---  
`boolean` || `date` || `number` || `string` |  `boolean` || `date` || `number` || `string` | The value of the result of the formula.  
  
The value can’t be updated directly via the API. | 42  
`type` |  `string` (enum) | A string indicating the data type of the result of the formula. Possible `type` values are:  
  
- `boolean`  
- `date`  
- `number`  
- `string` | `"number"`  
#### 
`formula` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-formula-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Days until launch": {
    "id": "CSoE",
    "type": "formula",
    "formula": {
      "type": "number",
      "number": 56
    }
  }
}

```

> ## 📘
> The [Retrieve a page endpoint](https://developers.notion.com/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `formula` property. If a `formula` property includes more than 25 references, then you can use the [Retrieve a page property item endpoint](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `formula` property to get its complete list of references.
### [](https://developers.notion.com/reference/page-property-values#icon)
> ## 📘
> Page icon and cover are not nested under `properties`
> The `icon` and `cover` parameters and fields in the [Create a page](https://developers.notion.com/reference/post-page) and [Update page properties](https://developers.notion.com/reference/patch-page) APIs are top-level are not nested under `properties`.
Field | Type | Description | Example value  
---|---|---|---  
`icon` | an object | Icon object | Refer to the example response objects below.  
#### 
`icon` property value as returned in GET page request
[](https://developers.notion.com/reference/page-property-values#example-emoji-icon-property-value-as-returned-in-get-page-request)
JSON
```
{
  "icon": {
    "type": "emoji",
    "emoji":"😀"
  }
}

```

#### 
`icon` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-uploaded-icon-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "icon": {
    "type":"file",
    "file": {
      "url": "https://local-files-secure.s3.us-west-2.amazonaws.com/13950b26-c203-4f3b-b97d-93ec06319565/a7084c4c-3e9a-4324-af99-34e0cb7f8fe7/notion.jpg?...",
      "expiry_time": "2024-12-03T19:44:56.932Z"
    }
  }
}

```

#### [](https://developers.notion.com/reference/page-property-values#example-updating-a-page-icon-to-an-uploaded-file)
After uploading an image using the [File Upload API](https://developers.notion.com/reference/file-upload#file-types-and-sizes), use the File Upload's ID in the [Create a page](https://developers.notion.com/reference/post-page) or [Update page properties](https://developers.notion.com/reference/patch-page) API to attach it as a page icon. For example:
JSON
```
{
  "icon": {
    "type": "file_upload",
    "file_upload": {
      "id": "43833259-72ae-404e-8441-b6577f3159b4"
    }
  }
}

```

To attach a file upload as a page cover rather than an icon, use the create or update page APIs with the `cover` parameter, nesting a `file_upload` parameter the same way as the `icon` example.
### [](https://developers.notion.com/reference/page-property-values#last-edited-by)
Field | Type | Description | Example value  
---|---|---|---  
`last_edited_by` | `object` | A [user object](https://developers.notion.com/reference/user) containing information about the user who last updated the page.  
  
`last_edited_by` can’t be updated. | Refer to the example response objects below.  
#### 
`last_edited_by` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-last_edited_by-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Last edited by column name": {
    "id": "uGNN",
    "type": "last_edited_by",
    "last_edited_by": {
      "object": "user",
      "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf",
      "name": "Test Integration",
      "avatar_url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/3db373fe-18f6-4a3c-a536-0f061cb9627f/leplane.jpeg",
      "type": "bot",
      "bot": {}
    }
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#last-edited-time)
Field | Type | Description | Example value  
---|---|---|---  
`last_edited_time` |  `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time) | The date and time that the page was last edited.  
  
The `last_edited_time` value can’t be updated. | `"2022-10-12T16:34:00.000Z"`  
#### 
`last_edited_time` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-last_edited_time-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Last edited time": {
    "id": "%3Defk",
    "type": "last_edited_time",
    "last_edited_time": "2023-02-24T21:06:00.000Z"
  } 
}

```

### [](https://developers.notion.com/reference/page-property-values#multi-select)
If the `type` of a page property value is `"multi_select"`, then the property value contains a `"multi_select"` array with the following fields:
Field | Type | Description | Example value  
---|---|---|---  
`color` |  `string` (enum) | Color of the option. Possible `"color"` values are:   
  
- `blue`  
- `brown`  
- `default`  
- `gray`  
- `green`  
- `orange`  
- `pink"`  
- `"purple`  
- `red`  
- `yellow`Defaults to `default`. The `color` value can’t be updated via the API. | `"red"`  
`id` | `string` | The ID of the option.  
  
You can use `id` or `name` to update a multi-select property. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"`  
`name` | `string` | The name of the option as it appears in Notion.  
  
If the multi-select [data source property](https://developers.notion.com/reference/property-object) does not yet have an option by that name, then the name will be added to the data source schema if the integration also has write access to the parent data source.  
  
Note: Commas (`","`) are not valid for select values. | `"JavaScript"`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `multi_select` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-multi_select-page-property-value)
JSON
```
{
  "properties": {
    "Programming language": {
      "multi_select": [
        {
          "name": "TypeScript"
        },
        {
          "name": "Python"
        }
      ]
    }
  }
}

```

#### 
`multi_select` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-multi_select-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Programming language": {
    "id": "QyRn",
    "name": "Programming language",
    "type": "multi_select",
    "multi_select": [
      {
        "id": "tC;=",
        "name": "TypeScript",
        "color": "purple"
      },
      {
        "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb",
        "name": "JavaScript",
        "color": "red"
      },
      {
        "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0",
        "name": "Python",
        "color": "gray"
      }
    ]
  }
}

```

> ## 📘
> If you want to add a new option to a multi-select property via the [Update page](https://developers.notion.com/reference/patch-page) or [Update data source](https://developers.notion.com/reference/update-a-data-source) endpoint, then your integration needs write access to the parent database.
### [](https://developers.notion.com/reference/page-property-values#number)
Field | Type | Description | Example value  
---|---|---|---  
`number` | `number` | A number representing some value. | `1234`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `number` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-number-page-property-value)
JSON
```
{
  "properties": {
    "Number of subscribers": {
      "number": 42
    }
  }
}

```

#### 
`number` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-number-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Number of subscribers": {
    "id": "WPj%5E",
    "name": "Number of subscribers",
    "type": "number",
    "number": {
      "format": "number"
    }
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#people)
Field | Type | Description | Example value  
---|---|---|---  
`people` | array of [user objects](https://developers.notion.com/reference/user) | An array of user objects. | Refer to the example response objects below.  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `people` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-people-page-property-value)
JSON
```
{
  "properties": {
    "Stakeholders": {
      "people": [{
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
      }]
    }
  }
}

```

#### 
`people` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-people-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Stakeholders": {
    "id": "%7BLUX",
    "type": "people",
    "people": [
      {
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e",
        "name": "Kimberlee Johnson",
        "avatar_url": null,
        "type": "person",
        "person": {
          "email": "hello@kimberlee.dev"
        }
      }
    ]
  }
}

```

> ## 📘
> Retrieve individual property items to avoid truncation
> The [Retrieve a page endpoint](https://developers.notion.com/reference/retrieve-a-page) can’t be guaranteed to return more than 25 people per `people` page property. If a `people` page property includes more than 25 people, then you can use the [Retrieve a page property item endpoint](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `people` property to get a complete list of people.
### [](https://developers.notion.com/reference/page-property-values#phone-number)
Field | Type | Description | Example value  
---|---|---|---  
`phone_number` | `string` | A string representing a phone number. No phone number format is enforced. | `"415-867-5309"`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `phone_number` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-phone_number-page-property-value)
JSON
```
{
  "properties": {
    "Contact phone number": {
      "phone_number": "415-202-4776"
    }
  }
}

```

#### 
`phone_number` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-phone_number-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Example phone number property": {
    "id": "%5DKhQ",
    "name": "Example phone number property",
    "type": "phone_number",
    "phone_number": {}
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#relation)
Field | Type | Description | Example value  
---|---|---|---  
`has_more` | `boolean` | If a `relation` has more than 25 references, then the `has_more` value for the relation in the response object is `true`. If a relation doesn’t exceed the limit, then `has_more` is `false`. | Refer to the example response objects below.  
`relation` | an array of page references | An array of related page references. A page reference is an object with an `id` key and a string value corresponding to a page ID in another data source. | Refer to the example response objects below.  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `relation` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-relation-page-property-value)
JSON
```
{
  "properties": {
    "Related tasks": {
      "relation": [
        {
          "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
        },
        {
          "id": "0c1f7cb2-8090-4f18-924e-d92965055e32"
        }
      ]
    }
  }
}

```

#### 
`relation` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-relation-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Related tasks": {
    "id": "hgMz",
    "type": "relation",
    "relation": [
      {
        "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
      },
      {
        "id": "0c1f7cb2-8090-4f18-924e-d92965055e32"
      }
    ],
    "has_more": false
  } 
}

```

> ## 📘
> To update a `relation` property value via the API, share the related parent database with the integration.
> If a `relation` property value is unexpectedly empty, then make sure that you have shared the original source database for the data source that the `relation` points to with the integration.
> Ensuring correct permissions is also important for complete results for `rollup` and `formula` properties.
### [](https://developers.notion.com/reference/page-property-values#rollup)
If the `type` of a page property value is `"rollup"`, then the property value contains a `"rollup"` object with the following fields: 
Field | Type | Description | Example value  
---|---|---|---  
`array` || `date` || `incomplete` || `number` || `unsupported` | Corresponds to the field.  
  
For example, if the field is `number`, then the type of the value is `number`. | The value of the calculated rollup.  
  
The value can't be directly updated via the API. | `1234`  
`function` |  `string` (enum) | The function that is evaluated for every page in the relation of the rollup. Possible `"function"` values are:  
  
- `average`  
- `checked`  
- `count`  
- `count_per_group`  
- `count_values`  
- `date_range`  
- `earliest_date`  
- `empty`  
- `latest_date`  
- `max`  
- `median`  
- `min`  
- `not_empty`  
- `percent_checked`  
- `percent_empty`  
- `percent_not_empty`  
- `percent_per_group`  
- `percent_unchecked`  
- `range`  
- `show_original`  
- `show_unique`  
- `sum`  
- `unchecked`  
- `unique` | `"sum"`  
`type` |  `array` || `date` || `incomplete` || `number` || `unsupported` | The value type of the calculated rollup. | `number`  
#### 
`rollup` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-rollup-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Number of units": {
    "id": "hgMz",
    "type": "rollup",
    "rollup": {
      "type": "number",
      "number": 2,
      "function": "count"
    }
  }
}

```

> ## 🚧
> For rollup properties with more than 25 references, use the Retrieve a page property endpoint
> Both the [Retrieve a page](https://developers.notion.com/reference/retrieve-a-page) and [Retrieve a page property](https://developers.notion.com/reference/retrieve-a-page-property) endpoints will return information related to the page properties. In cases where a rollup property has more than 25 references, the [Retrieve a page property](https://developers.notion.com/reference/retrieve-a-page-property) endpoint must but used.
> Learn more about rollup properties in Notion’s [Help Center](https://developers.notion.com/reference/page-property-values#rollup).
> ## 🚧
> The API does not support updating `rollup` page property values.
> To change a page's `rollup` property, use the Notion UI.
### [](https://developers.notion.com/reference/page-property-values#rich-text)
Field | Type | Description | Example value  
---|---|---|---  
`rich_text` | an array of [rich text objects](https://developers.notion.com/reference/rich-text) | An array of [rich text objects](https://developers.notion.com/reference/rich-text) | Refer to the example response objects below.  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `rich_text` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a--rich_text-page-property-value)
JSON
```
{
  "properties": {
    "Description": {
      "rich_text": [
        {
          "type": "text",
          "text": {
            "content": "There is some ",
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
          "plain_text": "There is some ",
          "href": null
        },
        {
          "type": "text",
          "text": {
            "content": "text",
            "link": null
          },
          "annotations": {
            "bold": true,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "text",
          "href": null
        },
        {
          "type": "text",
          "text": {
            "content": " in this property!",
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
          "plain_text": " in this property!",
          "href": null
        }
      ]
    }
  }
}

```

#### 
`rich_text` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-rich_text-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Description": {
    "id": "HbZT",
    "type": "rich_text",
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "There is some ",
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
        "plain_text": "There is some ",
        "href": null
      },
      {
        "type": "text",
        "text": {
          "content": "text",
          "link": null
        },
        "annotations": {
          "bold": true,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "text",
        "href": null
      },
      {
        "type": "text",
        "text": {
          "content": " in this property!",
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
        "plain_text": " in this property!",
        "href": null
      }
    ]
  } 
}

```

> ## 📘
> The [Retrieve a page endpoint](https://developers.notion.com/reference/retrieve-a-page) returns a maximum of 25 populated inline page or person references for a `rich_text` property. If a `rich_text` property includes more than 25 references, then you can use the [Retrieve a page property item endpoint](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `rich_text` property to get its complete list of references.
### [](https://developers.notion.com/reference/page-property-values#select)
If the type of a page property value is `select`, then the property value contains a `select` object with the following fields: 
Property | Type | Description | Example value  
---|---|---|---  
`color` |  `string` (enum) | The color of the option. Possible `"color"` values are:   
  
- `blue`  
- `brown`  
- `default`  
- `gray`  
- `green`  
- `orange`  
- `pink`  
- `purple`  
- `red`  
- yellow`Defaults to `default`. The `color` value can’t be updated via the API. | `red`  
`id` |  `string` | The ID of the option.  
  
You can use `id` or `name` to [update](https://developers.notion.com/reference/patch-page) a select property. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"`  
`name` | `string` | The name of the option as it appears in Notion.  
  
If the select [data source property](https://developers.notion.com/reference/property-object) doesn't have an option by that name yet, then the name is added to the data source schema if the integration also has write access to the parent data source.  
  
Note: Commas (`","`) are not valid for select values. | `"jQuery"`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `select` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a--select-page-property-value)
JSON
```
{
  "properties": {
    "Department": {
      "select": {
        "name": "Marketing"
      }
    }
  }
}

```

#### [](https://developers.notion.com/reference/page-property-values#example-select-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Department": {
    "id": "Yc%3FJ",
    "type": "select",
    "select": {
      "id": "ou@_",
      "name": "jQuery",
      "color": "purple"
    }
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#status)
If the type of a page property value is `status`, then the property value contains a `status` object with the following fields: 
Property | Type | Description | Example value  
---|---|---|---  
`color` |  `string` (enum) | The color of the option. Possible `"color"` values are:   
  
- `blue`  
- `brown`  
- `default`  
- `gray`  
- `green`  
- `orange`  
- `pink`  
- `purple`  
- `red`  
- `yellow`Defaults to `default`. The `color` value can’t be updated via the API. | `"red"`  
`id` |  `string` | `string` | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"`  
`name` | `string` | The name of the option as it appears in Notion. | `"In progress"`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `status` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-status-page-property-value)
JSON
```
{
  "properties": {
    "Status": {
      "status": {
        "name": "Not started"
      }
    }
  }
}

```

#### 
`status` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-status-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Status": {
    "id": "Z%3ClH",
    "type": "status",
    "status": {
      "id": "539f2705-6529-42d8-a215-61a7183a92c0",
      "name": "In progress",
      "color": "blue"
    }
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#title)
Field | Type | Description | Example value  
---|---|---|---  
`title` | an array of [rich text objects](https://developers.notion.com/reference/rich-text) | An array of [rich text objects](https://developers.notion.com/reference/rich-text). | Refer to the example response objects below.  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `title` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-title-page-property-value)
JSON
```
{
  "properties": {
    "Title": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "A better title for the page",
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
          "plain_text": "This is also not done",
          "href": null
        }
      ]
    }
  }
}

```

#### 
`title` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-title-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Title": {
    "id": "title",
    "type": "title",
    "title": [
      {
        "type": "text",
        "text": {
          "content": "A better title for the page",
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
        "plain_text": "This is also not done",
        "href": null
      }
    ]
  }
}

```

> ## 📘
> The [Retrieve a page endpoint](https://developers.notion.com/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `title` property. If a `title` property includes more than 25 references, then you can use the [Retrieve a page property item endpoint](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `title` property to get its complete list of references.
### [](https://developers.notion.com/reference/page-property-values#url)
Field | Type | Description | Example value  
---|---|---|---  
`url` | `string` | A string that describes a web address. | `"https://developers.notion.com/"`  
#### 
`properties` body param for a POST or PATCH page request that creates or updates a `url` page property value
[](https://developers.notion.com/reference/page-property-values#example-properties-body-param-for-a-post-or-patch-page-request-that-creates-or-updates-a-url-page-property-value)
JSON
```
{
  "properties": {
    "Website": {
      "url": "https://developers.notion.com/"
    }
  }
}

```

#### 
`url` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-url-page-property-value-as-returned-in-a-get-page-request)
JSON
```
{
  "Website": {
    "id": "bB%3D%5B",
    "type": "url",
    "url": "https://developers.notion.com/"
  }
}

```

### [](https://developers.notion.com/reference/page-property-values#unique-id)
Field | Type | Description | Example value  
---|---|---|---  
`number` | `number` | The ID count (auto-incrementing). | 3  
`prefix` |  `string` or `null` | An optional prefix to be applied to the unique ID. | "RL"  
> ## 👍
> Unique IDs can be read using the API with a [GET page](https://developers.notion.com/reference/retrieve-a-page) request, but they cannot be updated with the API, since they are auto-incrementing.
#### 
`url` page property value as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-url-page-property-value-as-returned-in-a-get-page-request-1)
JSON
```
{
  "test-ID": {
    "id": "tqqd",
    "type": "unique_id",
    "unique_id": {
      "number": 3,
      "prefix": "RL",
    },
  },
}

```

### [](https://developers.notion.com/reference/page-property-values#verification)
The verification status of a page in a wiki database. Pages can be verified or unverified, and verifications can have an optional expiration date set. 
The verification status cannot currently be set or updated via the public API. 
> ## 📘
> The `verification` property is only available for pages that are part of a [wiki database](https://developers.notion.com/docs/working-with-databases#wiki-databases). To learn more about wiki databases and verifying pages, see our [Help Center article](https://www.notion.so/help/wikis-and-verified-pages#verifying-pages).
Field | Type | Description | Example value  
---|---|---|---  
`state` | `string` | The verification state of the page. `"verified"` or `"unverified"`. | `"unverified"`  
`verified_by` |  [User](https://developers.notion.com/reference/user) object or `null` | If the page if verified, a [User](https://developers.notion.com/reference/user) object will be included to indicate the user who verified the page. | Refer to the example response objects below.  
`date` | Object or `null` | If the page is verified, the date object will include the date the verification started (`start`). If an expiration date is set for the verification, an end date (`end`) will be included. ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time.) | Refer to the example response objects below.  
#### 
`verification` page property values as returned in a GET page request
[](https://developers.notion.com/reference/page-property-values#example-verification-page-property-values-as-returned-in-a-get-page-request)
##### [](https://developers.notion.com/reference/page-property-values#unverified)
JSON
```
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: { state: "unverified", verified_by: null, date: null },
  },
}

```

##### [](https://developers.notion.com/reference/page-property-values#verified-with-no-expiration-date-set)
JSON
```
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: {
      state: "verified",
      verified_by: {
        object: "user",
        id: "01e46064-d5fb-4444-8ecc-ad47d076f804",
        name: "User Name",
        avatar_url: null,
        type: "person",
        person: {},
      },
      date: { start: "2023-08-01T04:00:00.000Z", end: null, time_zone: null },
    },
  },
}

```

##### [](https://developers.notion.com/reference/page-property-values#verified-with-90-day-expiration-date)
JSON
```
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: {...},
      date: {
        start: "2023-08-01T04:00:00.000Z",
        end: "2023-10-30T04:00:00.000Z",
        time_zone: null,
      },
    },
  },
}

```

## [](https://developers.notion.com/reference/page-property-values#paginated-page-properties)
The `title`, `rich_text`, `relation` and `people` page properties are returned as a paginated `list` object of individual `property_item` objects. 
An abridged set of the the properties found in the `list` object is below. Refer to the [pagination documentation](https://developers.notion.com/reference/intro#pagination) for additional information.
Field | Type | Description | Example value  
---|---|---|---  
`object` | `"list"` | Always `"list"`. | `"list"`  
`type` | `"property_item"` | Always `"property_item"`. | `"property_item"`  
`results` | `list` | List of `property_item` objects. | `[{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}... ]`  
`property_item` | `object` | A `property_item` object that describes the property. | `{"id": "title", "next_url": null, "type": "title", "title": {}}`  
`next_url` |  `string` or `null` | The URL the user can request to get the next page of results. | `"http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"`
