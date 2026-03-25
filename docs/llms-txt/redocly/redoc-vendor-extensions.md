# Source: https://redocly.com/docs/redoc/redoc-vendor-extensions.md

# Redoc CE vendor extensions

You can use the following [vendor extensions](https://redocly.com/docs/openapi-visual-reference/specification-extensions/) with Redoc CE.

## Swagger Object

Extends the OpenAPI root [OpenAPI Object](https://redocly.com/docs/openapi-visual-reference/openapi)

### x-servers

Backported from OpenAPI 3.0 [`servers`](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#server-object).
Currently doesn't support templates.

### x-tagGroups

| Field Name | Type | Description |
|  --- | --- | --- |
| x-tagGroups | [[Tag Group Object](#tag-group-object)] | A list of tag groups |


#### Use x-tagGroups with Redoc CE

`x-tagGroups` is used to group tags in the side menu.
Before you use `x-tagGroups`, make sure you **add all tags to a group**, since a tag that is not in a group, **is not displayed** at all!



#### Tag Group Object

Information about tags group

##### Fixed fields

| Field Name | Type | Description |
|  --- | --- | --- |
| name | string | The group name |
| tags | [string] | List of tags to include in this group |


#### x-tagGroups example


```json JSON
{
  "x-tagGroups": [
    {
      "name": "User Management",
      "tags": ["Users", "API keys", "Admin"]
    },
    {
      "name": "Statistics",
      "tags": ["Main Stats", "Secondary Stats"]
    }
  ]
}
```

yaml


```yaml
x-tagGroups:
  - name: User Management
    tags:
      - Users
      - API keys
      - Admin
  - name: Statistics
    tags:
      - Main Stats
      - Secondary Stats
```

## Info Object

Extends the OpenAPI [Info Object](https://redocly.com/docs/openapi-visual-reference/info/)

### x-logo

| Field Name | Type | Description |
|  --- | --- | --- |
| x-logo | [Logo Object](#logo-object) | The configuration for the logo that appears on the API's documentation pages. |


#### Use x-logo with Redoc CE

`x-logo` is used to specify API logo.
The corresponding image is displayed just above the side-menu.



#### Logo Object

The information about API logo

#### Fixed fields

| Field Name | Type | Description |
|  --- | --- | --- |
| url | string | The URL pointing to the logo image that appears on the API's documentation pages.
MUST be in the format of a URL.
To make the API description file usable from any location, use a an absolute URL. |
| backgroundColor | string | Background color for the image. MUST be an RGB color in [hexadecimal format](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) |
| altText | string | Text to use for the logo's `alt` tag.
Defaults to 'logo' if nothing is provided. |
| href | string | The URL pointing to the contact page. Default to 'info.contact.url' field of the OAS. |


#### x-logo example


```json JSON
{
  "info": {
    "version": "1.0.0",
    "title": "Swagger Petstore",
    "x-logo": {
      "url": "https://redocly.github.io/redoc/petstore-logo.png",
      "backgroundColor": "#FFFFFF",
      "altText": "Petstore logo"
    }
  }
}
```


```yaml YAML
info:
  version: "1.0.0"
  title: "Swagger Petstore"
  x-logo:
    url: "https://redocly.github.io/redoc/petstore-logo.png"
    backgroundColor: "#FFFFFF"
    altText: "Petstore logo"
```

## Tag Object

Extends the OpenAPI [Tag Object](https://redocly.com/docs/openapi-visual-reference/tags/)

### x-traitTag

| Field Name | Type | Description |
|  --- | --- | --- |
| x-traitTag | boolean | In Swagger two operations can have multiple tags.
This property distinguishes between tags that are used to group operations (default) from tags that are used to mark operation with certain trait (`true` value) |


#### Use x-traitTag with Redoc CE

Tags that have `x-traitTag` set to `true` are listed in the side-menu but don't have any subitems (operations).
It also renders the `description` tag.
This is useful for handling out common things like Pagination, Rate-Limits, etc.

#### x-traitTag example


```json JSON
{
    "name": "Pagination",
    "description": "Pagination description (can use markdown syntax)",
    "x-traitTag": true
}
```


```yaml YAML
name: Pagination
description: Pagination description (can use markdown syntax)
x-traitTag: true
```

### x-displayName

| Field Name | Type | Description |
|  --- | --- | --- |
| x-displayName | string | Defines the text that is used for this tag in the menu and in section headings |


## Operation Object vendor extensions

Extends the OpenAPI [Operation Object](https://redocly.com/docs/openapi-visual-reference/operation/)

### x-codeSamples

| Field Name | Type | Description |
|  --- | --- | --- |
| x-codeSamples | [[Code Sample Object](#code-sample-object)] | A list of code samples associated with operation |


#### Use x-codeSamples with Redoc CE

`x-codeSamples` are rendered on the right panel in Redoc CE.



### Code Sample Object

Operation code sample

#### Fixed fields

| Field Name | Type | Description |
|  --- | --- | --- |
| lang | string | Code sample language.
Value should be one of the following [list](https://github.com/github/linguist/blob/master/lib/linguist/popular.yml) |
| label | string? | Code sample label, for example `Node` or `Python2.7`, *optional*, `lang` is used by default |
| source | string | Code sample source code |


#### Code Sample Object example


```json JSON
{
  "lang": "JavaScript",
  "source": "console.log('Hello World');"
}
```


```yaml YAML
lang: JavaScript
source: console.log('Hello World');
```

### x-badges

| Field Name | Type | Description |
|  --- | --- | --- |
| x-badges | [[Badge Object](https://redocly.com/docs/realm/author/reference/openapi-extensions/x-badges#badge-object)] | A list of badges associated with the operation |


## Parameter Object

Extends the OpenAPI [Parameter Object](https://redocly.com/docs/openapi-visual-reference/parameter/)

### x-examples

| Field Name | Type | Description |
|  --- | --- | --- |
| x-examples | [Example Object](https://redocly.com/docs/openapi-visual-reference/example/) | Object that contains examples for the request. Applies when `in` is `body` and mime-type is `application/json` |


#### Use x-examples with Redoc CE

`x-examples` are rendered in the JSON tab on the right panel in Redoc CE.

## Response Object vendor extensions

Extends the OpenAPI [Response Object](https://redocly.com/docs/openapi-visual-reference/response/).

### x-summary

| Field Name | Type | Description |
|  --- | --- | --- |
| x-summary | string | a short summary of the response |


#### Use x-summary with Redoc CE

If specified, you can use `x-summary` as the response button text, with description rendered under the button.

## Schema Object

Extends the OpenAPI [Schema Object](https://redocly.com/docs/openapi-visual-reference/schemas/)

### x-nullable

| Field Name | Type | Description |
|  --- | --- | --- |
| x-nullable | boolean | marks schema as a nullable |


#### Use x-nullable with Redoc CE

Schemas marked as `x-nullable` are marked in Redoc CE with the label Nullable.

### x-additionalPropertiesName

`x-additionalPropertiesName` is a Redoc CE-specific vendor extension, and is not supported by other tools.

Extends the `additionalProperties` property of the schema object.

| Field Name | Type | Description |
|  --- | --- | --- |
| x-additionalPropertiesName | string | descriptive name of additional properties keys |


#### Use x-additionalPropertiesName with Redoc CE

Redoc CE uses this extension to display a more descriptive property name in objects with `additionalProperties` when viewing the property list with an `object`.

#### x-additionalPropertiesName example


```yaml
Player:
  required:
  - name

  properties:
    name:
      type: string

  additionalProperties:
    x-additionalPropertiesName: attribute-name
    type: string
```

### x-explicitMappingOnly

`x-explicitMappingOnly` is a Redoc CE-specific vendor extension, and is not supported by other tools.

Extends the `discriminator` property of the schema object.

| Field Name | Type | Description |
|  --- | --- | --- |
| x-explicitMappingOnly | boolean | limit the discriminator selectpicker to the explicit mappings only |


#### Use x-explicitMappingOnly with Redoc CE

Redoc CE uses this extension to filter the `discriminator` mappings shown in the selectpicker.
When set to `true`, the selectpicker lists only the explicitly defined mappings.
When `false`, the default behavior is kept, in other words, explicit and implicit mappings are shown.

#### x-explicitMappingOnly example


```yaml
Pet:
  type: object
  required:
    - name
    - photoUrls
  discriminator:
    propertyName: petType
    x-explicitMappingOnly: true
    mapping:
      cat: "#/components/schemas/Cat"
      bee: "#/components/schemas/HoneyBee"
```

Shows in the selectpicker only the items `cat` and `bee`, even though the `Dog` class inherits from the `Pet` class.

### x-enumDescriptions

| Field Name | Type | Description |
|  --- | --- | --- |
| x-enumDescriptions | [[Enum Description Object](https://redocly.com/docs/realm/author/reference/openapi-extensions/x-enum-descriptions#enum-description-object)] | A list of the enum values and descriptions to include in the documentation. |


#### Use x-enumDescriptions with Redoc CE

The enum (short for "enumeration") fields in OpenAPI allow you to restrict the value of a field to a list of allowed values.
These values need to be short and machine-readable, but that can make them harder for humans to parse and work with.

Add `x-enumDescriptions` to your OpenAPI description to show a helpful table of enum options and an explanation of what each one means.
This field supports Markdown.

#### x-enumDescriptions example

The following example shows a schema with two short-named options, and the `x-enumDescriptions` entry to list all enum entries and give additional context for each:


```yaml
components:
  schemas:
    TicketType:
      description: Type of ticket being purchased.
      Use `general` for regular museum entry and `event` for tickets to special events.
      type: string
      enum:
        - event
        - general
      x-enumDescriptions:
        event: Event Tickets _(timed entry)_
        general: General Admission
      example: event
```

## Resources

- **[Configure Redoc CE](/docs/redoc/config)** - Explore Redoc CE's configuration options