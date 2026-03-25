# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/array.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/array.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/array.md

# Array

Array is an input for lists of data.

## ð¡ Common array usage[â](#-common-array-usage "Direct link to ð¡ Common array usage")

The array input type can be used to store any list of data, for example:

* Configuration parameters
* Ordered values

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Select (Enum)

```
{
  "myArrayInput": {
    "title": "My array input",
    "icon": "My icon",
    "description": "My array input",
    "type": "array",
    "default": [1, 2, 3]
  }
}
```

```
{
  "myArraySelectInput": {
    "title": "My array select input",
    "icon": "My icon",
    "description": "My array select input",
    "type": "array",
    "enum": [
      [1, 2, 3],
      [1, 2]
    ]
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

* Basic
* Select (Enum) - coming soon

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties {
    identifier  = "myArrayInput"
    title       = "My array input"
    description = "My array input"
    type        = "array"
  }
}
```

## Validate array[â](#validate-array "Direct link to Validate array")

Array validations support the following operators:

* `minItems`
* `maxItems`
* `uniqueItems`

tip

Array validations follow the JSON schema model, refer to the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/array.html) to learn about all of the available validations

* Basic
* Terraform

```
{
  "myArrayInput": {
    "title": "My array input",
    "icon": "My icon",
    "description": "My array input ",
    "type": "array",
    "minItems": 0,
    "maxItems": 5,
    "uniqueItems": false
  }
}
```

```

resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    array_props = {
      "myArrayInput" = {
        title       = "My array input"
        description = "My array input"
        min_items   = 0
        max_items   = 5
        unique_items = false
      }
    }
  }
}
```
