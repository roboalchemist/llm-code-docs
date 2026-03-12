# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/structure-and-fields.md

# Structure and fields

Each self-service workflow trigger has a `userInputs` section in its configuration. In this section, you can define all of the user inputs you want your developers and users to fill when executing the workflow.

## Input structure[â](#input-structure "Direct link to Input structure")

```
{
  "userInputs": {
    "properties": {
      "myInput": {
        "title": "My Input",
        "icon": "DefaultProperty",
        "description": "Description of the input",
        "type": "string"
      }
    },
    "required": ["myInput"],
    "order": ["myInput"]
  }
}
```

## Common fields[â](#common-fields "Direct link to Common fields")

All input types share these common fields:

| Field         | Description                                                                                                                                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`       | The display name of the input (max 140 characters)                                                                                                                                                                            |
| `description` | A description to help users understand the input (max 1000 characters)                                                                                                                                                        |
| `icon`        | An icon to display next to the input                                                                                                                                                                                          |
| `type`        | **Required.** The data type of the input                                                                                                                                                                                      |
| `default`     | A default value for the input                                                                                                                                                                                                 |
| `dependsOn`   | An array of input names that this input depends on                                                                                                                                                                            |
| `readOnly`    | Whether the input is read-only                                                                                                                                                                                                |
| `visible`     | Whether the input is visible (can be a boolean or JQ expression). See [advanced input configurations](/workflows/build-workflows/self-service-trigger/advanced-input-configurations.md#visibility-controls) for more details. |

Property structure

The name of the input is the key of the input object. For example, in the code block above, the name of the input is `myInput`.

Note that all of the [properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#supported-properties) available for Port blueprints can also be used as user inputs, which is why they follow the same structure.

## Dynamic defaults with JQ[â](#dynamic-defaults-with-jq "Direct link to Dynamic defaults with JQ")

You can use JQ expressions to set dynamic default values based on other inputs or context:

```
{
  "environment": {
    "type": "string",
    "title": "Environment",
    "enum": ["dev", "staging", "prod"]
  },
  "replicas": {
    "type": "number",
    "title": "Replicas",
    "default": {
      "jqQuery": "if .form.environment == \"prod\" then 3 else 1 end"
    }
  }
}
```

## Ordering inputs[â](#ordering-inputs "Direct link to Ordering inputs")

Use the `order` field to control the display order of inputs:

```
{
  "properties": {
    "input1": { "type": "string", "title": "First" },
    "input2": { "type": "string", "title": "Second" },
    "input3": { "type": "string", "title": "Third" }
  },
  "order": ["input3", "input1", "input2"]
}
```

## Required inputs[â](#required-inputs "Direct link to Required inputs")

Specify which inputs are required using the `required` array:

```
{
  "properties": {
    "name": { "type": "string", "title": "Name" },
    "description": { "type": "string", "title": "Description" }
  },
  "required": ["name"]
}
```

## Read-only inputs[â](#read-only-inputs "Direct link to Read-only inputs")

Specify which inputs are read-only using the `readOnly` key:

```
{
  "properties": {
    "name": {
      "type": "string",
      "title": "Name"
      "readOnly": true
    },
    "title": {
      "type": "string",
      "title": "Title"
      "readOnly": {
        "jqQuery": ".form.name != \"\""
      }
    },
  },
}
```

## Hidden inputs[â](#hidden-inputs "Direct link to Hidden inputs")

Specify which inputs are hidden using the `visible` key:

```
{
  "properties": {
    "name": {
      "type": "string",
      "title": "Name"
      "visible": false
    },
    "title": {
      "type": "string",
      "title": "Title"
      "visible": {
        "jqQuery": ".form.name != \"\""
      }
    },
  },
}
```
