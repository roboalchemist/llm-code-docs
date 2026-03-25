# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/datetime.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/datetime.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/datetime.md

# Datetime

Datetime is an input used to reference a date and time.

## ð¡ Common datetime usage[â](#-common-datetime-usage "Direct link to ð¡ Common datetime usage")

The datetime input type can be used to store any date and time, for example:

* Deployment time
* Release time
* Creation timestamp

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Array

```
{
  "myDatetimeInput": {
    "title": "My datetime input",
    "icon": "My icon",
    "description": "My datetime input",
    "type": "string",
    "format": "date-time",
    "default": "2022-04-18T11:44:15.345Z"
  }
}
```

```
{
  "myDatetimeArrayInput": {
    "title": "My datetime array",
    "icon": "My icon",
    "description": "My datetime array",
    "type": "array",
    "items": {
      "type": "string",
      "format": "date-time"
    }
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

* Basic
* Array

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    string_props = {
      myDatetimeProp = {
        title    = "My datetime"
        format   = "date-time"
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
      myArrayDatetimeProp = {
        title    = "My array datetime"
        string_items = {
          format = "date-time"
        }
      }
    }
  }
}
```
