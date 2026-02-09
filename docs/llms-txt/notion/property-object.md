# Source: https://developers.notion.com/reference/property-object.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data source properties

> Data source property objects are rendered in the Notion UI as data columns.

All [data source objects](/reference/data-source) include a child `properties` object. This `properties` object is composed of individual data source property objects. These property objects define the data source schema and are rendered in the Notion UI as data columns.

<Info>
  **Data source rows**

  If you’re looking for information about how to use the API to work with data source rows, then refer to the [page property values](/reference/property-value-object) documentation. The API treats data source rows as pages.
</Info>

Every data source property object contains the following keys:

| Field         | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Example value |
| :------------ | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------ |
| `id`          | `string`        | An identifier for the property, usually a short string of random letters and symbols. <br /><br /> Some automatically generated property types have special human-readable IDs. For example, all Title properties have an `id` of `"title"`.                                                                                                                                                                                                                                                                                          | `"fy:{"`      |
| `name`        | `string`        | The name of the property as it appears in Notion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |               |
| `description` | `string`        | The description of a property as it appear in Notion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |               |
| `type`        | `string` (enum) | The type that controls the behavior of the property. Possible values are:<br /><br /> - `"checkbox"`<br /> - `"created_by"`<br /> - `"created_time"`<br /> - `"date"`<br /> - `"email"`<br /> - `"files"`<br /> - `"formula"`<br /> - `"last_edited_by"`<br /> - `"last_edited_time"`<br /> - `"multi_select"`<br /> - `"number"`<br /> - `"people"`<br /> - `"phone_number"`<br /> - `"place"`<br /> - `"relation"`<br /> - `"rich_text"`<br /> - `"rollup"`<br /> - `"select"`<br /> - `"status"`<br /> - `"title"`<br /> - `"url"` | `"rich_text"` |

Each data source property object also contains a type object. The key of the object is the `type` of the object, and the value is an object containing type-specific configuration. The following sections detail these type-specific objects along with example property objects for each type.

## Checkbox

A checkbox data source property is rendered in the Notion UI as a column that contains checkboxes. The `checkbox` type object is empty; there is no additional property configuration.

<CodeGroup>
  ```json Example checkbox data source property object theme={null}
  "Task complete": {
    "id": "BBla",
    "name": "Task complete",
    "type": "checkbox",
    "checkbox": {}
  }
  ```
</CodeGroup>

## Created by

A created by data source property is rendered in the Notion UI as a column that contains people mentions of each row's author as values.

The `created_by` type object is empty. There is no additional property configuration.

<CodeGroup>
  ```json Example created by data source property object theme={null}
  "Created by": {
    "id": "%5BJCR",
    "name": "Created by",
    "type": "created_by",
    "created_by": {}
  }
  ```
</CodeGroup>

## Created time

A created time data source property is rendered in the Notion UI as a column that contains timestamps of when each row was created as values.

The `created_time` type object is empty. There is no additional property configuration.

<CodeGroup>
  ```json Example created time data source property object theme={null}
  "Created time": {
    "id": "XcAf",
    "name": "Created time",
    "type": "created_time",
    "created_time": {}
  }
  ```
</CodeGroup>

## Date

A date data source property is rendered in the Notion UI as a column that contains date values.

The `date` type object is empty; there is no additional configuration.

<CodeGroup>
  ```json Example date data source property object theme={null}
  "Task due date" {
    "id": "AJP%7D",
    "name": "Task due date",
    "type": "date",
    "date": {}
  }
  ```
</CodeGroup>

## Email

An email data source property is represented in the Notion UI as a column that contains email values.

The `email` type object is empty. There is no additional property configuration.

<CodeGroup>
  ```json Example email data source property object theme={null}
  "Contact email": {
    "id": "oZbC",
    "name": "Contact email",
    "type": "email",
    "email": {}
  }
  ```
</CodeGroup>

## Files

A files data source property is rendered in the Notion UI as a column that has values that are either files uploaded directly to Notion or external links to files. The `files` type object is empty; there is no additional configuration.

<CodeGroup>
  ```json Example files data source property object theme={null}
  "Product image": {
    "id": "pb%3E%5B",
    "name": "Product image",
    "type": "files",
    "files": {}
  }
  ```
</CodeGroup>

## Formula

A formula data source property is rendered in the Notion UI as a column that contains values derived from a provided expression.

The `formula` type object defines the expression in the following fields:

| Field        | Type     | Description                                                                                                                                                                                 | Example value                                                                                                |
| :----------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- |
| `expression` | `string` | The formula that is used to compute the values for this property. <br /><br /> Refer to the Notion help center for [information about formula syntax](https://www.notion.so/help/formulas). | `{{notion:block_property:BtVS:00000000-0000-0000-0000-000000000000:8994905a-074a-415f-9bcf-d1f8b4fa38e4}}/2` |

<CodeGroup>
  ```json Example formula data source property object theme={null}
  "Updated price": {
    "id": "YU%7C%40",
    "name": "Updated price",
    "type": "formula",
    "formula": {
      "expression": "{{notion:block_property:BtVS:00000000-0000-0000-0000-000000000000:8994905a-074a-415f-9bcf-d1f8b4fa38e4}}/2"
    }
  }
  ```
</CodeGroup>

## Last edited by

A last edited by data source property is rendered in the Notion UI as a column that contains people mentions of the person who last edited each row as values.

The `last_edited_by` type object is empty. There is no additional property configuration.

## Last edited time

A last edited time data source property is rendered in the Notion UI as a column that contains timestamps of when each row was last edited as values.

The `last_edited_time` type object is empty. There is no additional property configuration.

<CodeGroup>
  ```json Example last edited time data source property object theme={null}
  "Last edited time": {
    "id": "jGdo",
    "name": "Last edited time",
    "type": "last_edited_time",
    "last_edited_time": {}
  }
  ```
</CodeGroup>

## Multi-select

A multi-select data source property is rendered in the Notion UI as a column that contains values from a range of options. Each row can contain one or multiple options.

The `multi_select` type object includes an array of `options` objects. Each option object details settings for the option, indicating the following fields:

| Field   | Type            | Description                                                                                                                                                                                                                                                             | Example value                            |
| :------ | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
| `color` | `string` (enum) | The color of the option as rendered in the Notion UI. Possible values include:<br /><br /> - `blue`<br /> - `brown`<br /> - `default`<br /> - `gray`<br /> - `green`<br /> - `orange`<br /> - `pink`<br /> - `purple`<br /> - `red`<br /> - `yellow`                    | `"blue"`                                 |
| `id`    | `string`        | An identifier for the option, which does not change if the name is changed. An `id` is sometimes, but not *always*, a UUID.                                                                                                                                             | `"ff8e9269-9579-47f7-8f6e-83a84716863c"` |
| `name`  | `string`        | The name of the option as it appears in Notion. <br /><br /> **Notes**: Commas (",") are not valid for multi-select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"apple"` and `"APPLE"`. | `"Fruit"`                                |

<CodeGroup>
  ```json Example multi-select data source property expandable theme={null}
  "Store availability": {
    "id": "flsb",
    "name": "Store availability",
    "type": "multi_select",
    "multi_select": {
      "options": [
        {
          "id": "5de29601-9c24-4b04-8629-0bca891c5120",
          "name": "Duc Loi Market",
          "color": "blue"
        },
        {
          "id": "385890b8-fe15-421b-b214-b02959b0f8d9",
          "name": "Rainbow Grocery",
          "color": "gray"
        },
        {
          "id": "72ac0a6c-9e00-4e8c-80c5-720e4373e0b9",
          "name": "Nijiya Market",
          "color": "purple"
        },
        {
          "id": "9556a8f7-f4b0-4e11-b277-f0af1f8c9490",
          "name": "Gus's Community Market",
          "color": "yellow"
        }
      ]
    }
  }
  ```
</CodeGroup>

## Number

A number data source property is rendered in the Notion UI as a column that contains numeric values. The `number` type object contains the following fields:

| Field    | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Example value |
| :------- | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| `format` | `string` (enum) | The way that the number is displayed in Notion. Potential values include: <br /><br /> - `argentine_peso`<br /> - `baht`<br /> - `australian_dollar`<br /> - `canadian_dollar`<br /> - `chilean_peso`<br /> - `colombian_peso`<br /> - `danish_krone`<br /> - `dirham`<br /> - `dollar`<br /> - `euro`<br /> - `forint`<br /> - `franc`<br /> - `hong_kong_dollar`<br /> - `koruna`<br /> - `krona`<br /> - `leu`<br /> - `lira`<br /> - `mexican_peso`<br /> - `new_taiwan_dollar`<br /> - `new_zealand_dollar`<br /> - `norwegian_krone`<br /> - `number`<br /> - `number_with_commas`<br /> - `percent`<br /> - `philippine_peso`<br /> - `pound`<br /> - `peruvian_sol`<br /> - `rand`<br /> - `real`<br /> - `ringgit`<br /> - `riyal`<br /> - `ruble`<br /> - `rupee`<br /> - `rupiah`<br /> - `shekel`<br /> - `singapore_dollar`<br /> - `uruguayan_peso`<br /> - `yen`, - `yuan`<br /> - `won`<br /> - `zloty` | `"percent"`   |

<CodeGroup>
  ```json Example number data source property object theme={null}
  "Price"{
    "id": "%7B%5D_P",
    "name": "Price",
    "type": "number",
    "number": {
      "format": "dollar"
    }
  }
  ```
</CodeGroup>

## People

A people data source property is rendered in the Notion UI as a column that contains people mentions. The `people` type object is empty; there is no additional configuration.

<CodeGroup>
  ```json Example people data source property object theme={null}
  "Project owner": {
    "id": "FlgQ",
    "name": "Project owner",
    "type": "people",
    "people": {}
  }
  ```
</CodeGroup>

## Phone number

A phone number data source property is rendered in the Notion UI as a column that contains phone number values.

The `phone_number` type object is empty. There is no additional property configuration.

<CodeGroup>
  ```json Example phone number data source property object theme={null}
  "Contact phone number": {
    "id": "ULHa",
    "name": "Contact phone number",
    "type": "phone_number",
    "phone_number": {}
  }
  ```
</CodeGroup>

## Place

A place data source property is rendered in the Notion UI as a column that contains location values. It can be used in conjunction with the Map view for displaying locations.

| Field             | Type             | Description                                                                                                               | Example value |
| :---------------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------ | :------------ |
| `lat`             | `number`         | The latitude.                                                                                                             | `30.12`       |
| `lon`             | `number`         | The longitude.                                                                                                            | `-60.72`      |
| `name`            | `string \| null` | A name for the location.                                                                                                  | `"Notion HQ"` |
| `address`         | `string \| null` | An address for the location.                                                                                              | `""`          |
| `aws_place_id`    | `string \| null` | The corresponding ID value from a location provider. Only exposed for duplication or echoing responses; will not be read. | `"123"`       |
| `google_place_id` | `string \| null` | The corresponding ID value from a location provider. Only exposed for duplication or echoing responses; will not be read. | `"123"`       |

<CodeGroup>
  ```json Example place data source property object theme={null}
  "Place": {
    "id": "Xqz4",
    "name": "Place",
    "type": "place",
  	"place": {}
  }
  ```
</CodeGroup>

## Relation

A relation data source property is rendered in the Notion UI as column that contains [relations](https://www.notion.so/help/relations-and-rollups), references to pages in another data source, as values.

The `relation` type object contains the following fields:

| Field                  | Type            | Description                                                                                                                                     | Example value                            |
| :--------------------- | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
| `data_source_id`       | `string` (UUID) | The data source that the relation property refers to. The corresponding linked page values must belong to the data source in order to be valid. | `"668d797c-76fa-4934-9b05-ad288df2d136"` |
| `synced_property_id`   | `string`        | The `id` of the corresponding property that is updated in the related data source when this property is changed.                                | `"fy:{"`                                 |
| `synced_property_name` | `string`        | The `name` of the corresponding property that is updated in the related data source when this property is changed.                              | `"Ingredients"`                          |

<CodeGroup>
  ```json Example relation data source property object theme={null}
  "Projects": {
    "id": "~pex",
    "name": "Projects",
    "type": "relation",
    "relation": {
      "data_source_id": "6c4240a9-a3ce-413e-9fd0-8a51a4d0a49b",
      "dual_property": {
        "synced_property_name": "Tasks",
        "synced_property_id": "JU]K" 
      }
    }
  }
  ```
</CodeGroup>

<Info>
  **Database relations must be shared with your integration**

  To retrieve properties from data source [relations](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your integration in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.

  Similarly, to update a data source relation property via the API, share the related database with the integration.
</Info>

## Rich text

A rich text data source property is rendered in the Notion UI as a column that contains text values. The `rich_text` type object is empty; there is no additional configuration.

<CodeGroup>
  ```json Example rich text data source property object theme={null}
  "Project description": {
    "id": "NZZ%3B",
    "name": "Project description",
    "type": "rich_text",
    "rich_text": {}
  }
  ```
</CodeGroup>

## Rollup

A rollup data source property is rendered in the Notion UI as a column with values that are rollups, specific properties that are pulled from a related data source.

The `rollup` type object contains the following fields:

| Field                    | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Example value        |
| :----------------------- | :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- |
| `function`               | `string` (enum) | The function that computes the rollup value from the related pages. Possible values include:<br /><br /> - `average`<br /> - `checked`<br /> - `count_per_group`<br /> - `count`<br /> - `count_values`<br /> - `date_range`<br /> - `earliest_date`<br /> - `empty`<br /> - `latest_date`<br /> - `max`<br /> - `median`<br /> - `min`<br /> - `not_empty`<br /> - `percent_checked`<br /> - `percent_empty`<br /> - `percent_not_empty`<br /> - `percent_per_group`<br /> - `percent_unchecked`<br /> - `range`<br /> - `unchecked`<br /> - `unique`<br /> - `show_original`<br /> - `show_unique`<br /> - `sum` | `"sum"`              |
| `relation_property_id`   | `string`        | The `id` of the related data source property that is rolled up.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `"fy:{"`             |
| `relation_property_name` | `string`        | The `name` of the related data source property that is rolled up.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `Tasks"`             |
| `rollup_property_id`     | `string`        | The `id` of the rollup property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `"fy:{"`             |
| `rollup_property_name`   | `string`        | The `name` of the rollup property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `"Days to complete"` |

<CodeGroup>
  ```json Example rollup data source property object theme={null}
  "Estimated total project time": {
    "id": "%5E%7Cy%3C",
    "name": "Estimated total project time",
    "type": "rollup",
    "rollup": {
      "rollup_property_name": "Days to complete",
      "relation_property_name": "Tasks",
      "rollup_property_id": "\\nyY",
      "relation_property_id": "Y]<y",
      "function": "sum"
    }
  }
  ```
</CodeGroup>

## Select

A select data source property is rendered in the Notion UI as a column that contains values from a selection of options. Only one option is allowed per row.

The `select` type object contains an array of objects representing the available options. Each option object includes the following fields:

| Field   | Type            | Description                                                                                                                                                                                                                                                 | Example value                            |
| :------ | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
| `color` | `string` (enum) | The color of the option as rendered in the Notion UI. Possible values include:<br /><br /> - `blue`<br /> - `brown`<br /> - `default`<br /> - `gray`<br /> - `green`<br /> - `orange`<br /> - `pink`<br /> - `purple`<br /> - `red`<br /> - `yellow`        | - `"red"`                                |
| `id`    | `string`        | An identifier for the option. It doesn't change if the name is changed. These are sometimes, but not *always*, UUIDs.                                                                                                                                       | `"ff8e9269-9579-47f7-8f6e-83a84716863c"` |
| `name`  | `string`        | The name of the option as it appears in the Notion UI. **Notes**: Commas (",") are not valid for select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"apple"` and `"APPLE"`. | `"Fruit"`                                |

<CodeGroup>
  ```json Example select data source property object expandable theme={null}
  "Food group": {
    "id": "%40Q%5BM",
    "name": "Food group",
    "type": "select",
    "select": {
      "options": [
        {
          "id": "e28f74fc-83a7-4469-8435-27eb18f9f9de",
          "name": "🥦Vegetable",
          "color": "purple"
        },
        {
          "id": "6132d771-b283-4cd9-ba44-b1ed30477c7f",
          "name": "🍎Fruit",
          "color": "red"
        },
        {
          "id": "fc9ea861-820b-4f2b-bc32-44ed9eca873c",
          "name": "💪Protein",
          "color": "yellow"
        }
      ]
    }
  }
  ```
</CodeGroup>

## Status

A status data source property is rendered in the Notion UI as a column that contains values from a list of status options. The `status` type object includes an array of `options` objects and an array of `groups` objects.

The `options` array is a sorted list of list of the available status options for the property. Each option object in the array has the following fields:

| Field   | Type            | Description                                                                                                                                                                                                                                                                          | Example value                            |
| :------ | :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
| `color` | `string` (enum) | The color of the option as rendered in the Notion UI. Possible values include:<br /><br /> - `blue`<br /> - `brown`<br /> - `default`<br /> - `gray`<br /> - `green`<br /> - `orange`<br /> - `pink`<br /> - `purple`<br /> - `red`<br /> - `yellow`                                 | `"green"`                                |
| `id`    | `string`        | An identifier for the option. The `id` does not change if the `name` is changed. It is sometimes, but not *always*, a UUID.                                                                                                                                                          | `"ff8e9269-9579-47f7-8f6e-83a84716863c"` |
| `name`  | `string`        | The name of the option as it appears in the Notion UI. <br /><br /> **Notes**: Commas (",") are not valid for select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"In progress"` and `"IN PROGRESS"`. | `"In progress"`                          |

A group is a collection of options. The `groups` array is a sorted list of the available groups for the property. Each group object in the array has the following fields:

| Field        | Type                         | Description                                                                                                                                                                                                                                          | Example value                               |
| :----------- | :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
| `color`      | `string` (enum)              | The color of the option as rendered in the Notion UI. Possible values include:<br /><br /> - `blue`<br /> - `brown`<br /> - `default`<br /> - `gray`<br /> - `green`<br /> - `orange`<br /> - `pink`<br /> - `purple`<br /> - `red`<br /> - `yellow` | `"purple"`                                  |
| `id`         | `string`                     | An identifier for the option. The `id` does not change if the `name` is changed. It is sometimes, but not *always*, a UUID.                                                                                                                          | `"ff8e9269-9579-47f7-8f6e-83a84716863c"`    |
| `name`       | `string`                     | The name of the option as it appears in the Notion UI. <br /><br /> **Note**: Commas (",") are not valid for status values.                                                                                                                          | `"To do"`                                   |
| `option_ids` | an array of `string`s (UUID) | A sorted list of `id`s of all of the options that belong to a group.                                                                                                                                                                                 | Refer to the example `status` object below. |

<CodeGroup>
  ```json Example status data source property object expandable theme={null}
  "Status": {
    "id": "biOx",
    "name": "Status",
    "type": "status",
    "status": {
      "options": [
        {
          "id": "034ece9a-384d-4d1f-97f7-7f685b29ae9b",
          "name": "Not started",
          "color": "default"
        },
        {
          "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
          "name": "In progress",
          "color": "blue"
        },
        {
          "id": "497e64fb-01e2-41ef-ae2d-8a87a3bb51da",
          "name": "Done",
          "color": "green"
        }
      ],
      "groups": [
        {
          "id": "b9d42483-e576-4858-a26f-ed940a5f678f",
          "name": "To-do",
          "color": "gray",
          "option_ids": [
            "034ece9a-384d-4d1f-97f7-7f685b29ae9b"
          ]
        },
        {
          "id": "cf4952eb-1265-46ec-86ab-4bded4fa2e3b",
          "name": "In progress",
          "color": "blue",
          "option_ids": [
            "330aeafb-598c-4e1c-bc13-1148aa5963d3"
          ]
        },
        {
          "id": "4fa7348e-ae74-46d9-9585-e773caca6f40",
          "name": "Complete",
          "color": "green",
          "option_ids": [
            "497e64fb-01e2-41ef-ae2d-8a87a3bb51da"
          ]
        }
      ]
    }
  }
  ```
</CodeGroup>

<Warning>
  **It is not possible to update a status data source property's `name` or `options` values via the API.**

  Update these values from the Notion UI, instead.
</Warning>

## Title

A title data source property controls the title that appears at the top of a page when a data source row is opened. The `title` type object itself is empty; there is no additional configuration.

<CodeGroup>
  ```json Example title data source property object theme={null}
  "Project name": {
    "id": "title",
    "name": "Project name",
    "type": "title",
    "title": {}
  }
  ```
</CodeGroup>

<Warning>
  **All data sources require one, and only one, `title` property.**
  The API throws errors if you send a request to [Create a data source](/reference/create-a-data-source) or [Create a database](/reference/database-create) without a `title` property, or if you attempt to [Update a data source](/reference/update-a-data-source) to add or remove a `title` property.
</Warning>

<Info>
  **Title data source property vs. data source title**

  A `title` data source property is a type of column in a data source.

  A data source `title` defines the title of the data source and is found on the [data source object](/reference/data-source).

  Every data source requires both a data source `title` and a `title` data source property. This ensures that we have both:

  * An overall title to display when viewing the database or data source in the Notion app
  * A title property for each page under the data source, so page titles can be displayed in the Notion app
</Info>

## URL

A URL data source property is represented in the Notion UI as a column that contains URL values.

The `url` type object is empty. There is no additional property configuration.

<CodeGroup>
  ```json Example URL data source property object theme={null}
  "Project URL": {
    "id": "BZKU",
    "name": "Project URL",
    "type": "url",
    "url": {}
  }
  ```
</CodeGroup>

## Unique ID

A unique ID data source property records values that are automatically incremented, and enforced to be unique across all pages in a data source. This can be useful for task or bug report IDs (e.g. TASK-1234), or other similar types of identifiers that must be unique.

The `unique_id` type object can contain an optional `prefix` attribute, which is a common prefix assigned to pages in the data source. When a `prefix` is set, a special URL (for example, `notion.so/TASK-1234`) is generated to be able to look up a page easily by the ID. Learn more in our [help center documentation](https://www.notion.com/help/unique-id) or [Notion Academy lesson](https://www.notion.com/help/notion-academy/lesson/unique-id-property).

<CodeGroup>
  ```json Example unique ID data source property object theme={null}
  "Task ID": {
    "prefix": "TASK"
  }
  ```
</CodeGroup>
