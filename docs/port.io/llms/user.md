# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/user.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/user.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/user.md

# User

User is an input used to reference users that exist in Port.

## ð¡ Common user usage[â](#-common-user-usage "Direct link to ð¡ Common user usage")

The user input type can be used to reference any user that exists in Port, for example:

* The code owners
* The current on-call
* The lead maintainer

In the [live demo](https://demo.port.io/self-serve) self-service hub page, we can see the **change on-call** action whose `On-Call` input is a user input. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Array

```
{
  "myUserInput": {
    "title": "My user input",
    "icon": "My icon",
    "description": "My user input",
    "type": "string",
    "format": "user",
    "default": "me@example.com"
  }
}
```

```
{
  "myUserArrayInput": {
    "title": "My user array input",
    "icon": "My icon",
    "description": "My user array input",
    "type": "array",
    "items": {
      "type": "string",
      "format": "user"
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
      "myUserInput" = {
        title       = "My user input"
        description = "My user input"
        format      = "user"
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
    array_props = {
      "myUserArrayInput" = {
        title       = "My user array input"
        description = "My user array input"
        format      = "user"
      }
    }
  }
}
```
