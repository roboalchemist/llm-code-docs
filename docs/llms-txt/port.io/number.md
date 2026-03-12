# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/number.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/number.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/number.md

# Number

Number is a basic input for numeric data.

## ð¡ Common number usage[â](#-common-number-usage "Direct link to ð¡ Common number usage")

The number input type can be used to store any numeric data, for example:

* Memory/storage allocations
* Replica counts
* Number of days to retain data

In the [live demo](https://demo.port.io/self-serve) self-service hub page, we can see the **scaffold new service** action whose `K8s Replica Count` input is a number input. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Select (Enum)
* Array
* Enum Array

```
{
  "myNumberInput": {
    "title": "My number input",
    "icon": "My icon",
    "description": "My number input",
    "type": "number",
    "default": 7
  }
}
```

```
{
  "myNumberSelectInput": {
    "title": "My number select input",
    "icon": "My icon",
    "description": "My number select input",
    "type": "number",
    "enum": [1, 2, 3, 4]
  }
}
```

```
{
  "myNumberArrayInput": {
    "title": "My number array input",
    "icon": "My icon",
    "description": "My number array input",
    "type": "array",
    "items": {
      "type": "number"
    }
  }
}
```

```
{
  "myNumberArray": {
    "title": "My number-selection array input",
    "icon": "My icon",
    "description": "My number-selection array input",
    "type": "array",
    "items": {
      "type": "number",
      "enum": [1, 2, 3, 4],
      "enumColors": {
        "1": "red",
        "2": "green",
        "3": "blue"
      }
    }
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

* Basic
* Select (Enum)
* Array

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    number_props = {
      "myNumberInput" = {
        title       = "My number input"
        description = "My number input"
        default     = 7
      }
    }
  }
}
```

```

resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    number_props = {
      "myNumberInput" = {
        title       = "My number input"
        description = "My number input"
        enum        = [1, 2, 3, 4]
      }
    }
  }
}
```

```

resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    array_props = {
      "myNumberArrayInput" = {
        title       = "My number array input"
        description = "My number array input"
        number_items = {}
      }
    }
  }
}
```

## Validate number[â](#validate-number "Direct link to Validate number")

Number validations support the following operators:

* `range`

Ranges of numbers are specified using a combination of the `minimum` and `maximum` keywords, (or `exclusiveMinimum` and `exclusiveMaximum` for expressing exclusive range).

If *x* is the value being validated, the following must hold true:

* *x* â¥ `minimum`
* *x* > `exclusiveMinimum`
* *x* â¤ `maximum`
* *x* < `exclusiveMaximum`

- Basic
- Array
- Terraform

```
{
  "myNumberInput": {
    "title": "My number input",
    "icon": "My icon",
    "description": "My number input",
    "type": "number",
    "minimum": 0,
    "maximum": 50
  }
}
```

```
{
  "myNumberArrayInput": {
    "title": "My number array input",
    "icon": "My icon",
    "description": "My number array input",
    "type": "array",
    "items": {
      "type": "number",
      "exclusiveMinimum": 0,
      "exclusiveMaximum": 50
    }
  }
}
```

```

resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    number_props = {
      "myNumberInput" = {
        title       = "My number input"
        description = "My number input"
        minimum     = 0
        maximum     = 50
      }
    }
  }
}
```
