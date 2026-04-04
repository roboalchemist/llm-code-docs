# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/email.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/email.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/email.md

# Email

Email is an input used to save Email addresses.

## ð¡ Common email usage[â](#-common-email-usage "Direct link to ð¡ Common email usage")

The Email input type can be used to store any legal email address.

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Select (Enum)
* Array

```
{
  "myEmailInput": {
    "title": "My email input",
    "icon": "My icon",
    "description": "My email input",
    "type": "string",
    "format": "email",
    "default": "me@example.com"
  }
}
```

```
{
  "myEmailSelectInput": {
    "title": "My email select input",
    "icon": "My icon",
    "description": "My email select input",
    "type": "string",
    "format": "email",
    "enum": ["me@example.com", "example@example.com"]
  }
}
```

```
{
  "myEmailArrayInput": {
    "title": "My email array input",
    "icon": "My icon",
    "description": "My email array input",
    "type": "array",
    "items": {
      "type": "string",
      "format": "email"
    }
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

* Basic
* Select (Enum)
* Array - coming soon

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    string_props = {
      "myEmailInput" = {
        title       = "My email input"
        description = "My email input"
        format      = "email"
        default     = "me@example.com"
      }
    }
  }
}
```

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    string_props = {
      "myEmailInput" = {
        title       = "My email input"
        description = "My email input"
        format      = "email"
        default     = "me@example.com"
        enum = ["me@example.com", "example@example.com"]
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
      "myEmailInput" = {
        title       = "My email input"
        description = "My email input"
        default     = "me@example.com"
        string_items = {
          format = "email"
        }
      }
    }
  }
}
```
