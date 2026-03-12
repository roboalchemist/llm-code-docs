# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/team.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/team.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/team.md

# Team

Team is an input used to reference teams that exist in Port.

## ð¡ Common team usage[â](#-common-team-usage "Direct link to ð¡ Common team usage")

The team input type can be used to reference any team that exists in Port, for example:

* The service owning team
* The current on-call
* The lead maintainers

In the [live demo](https://demo.port.io/self-serve) self-service hub page, we can see the **scaffold new service** action whose `Owning Team` input is a user input. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Array

```
{
  "myTeamInput": {
    "title": "My team input",
    "icon": "My icon",
    "description": "My team input",
    "type": "string",
    "format": "team",
    "default": "my-team"
  }
}
```

```
{
  "myTeamArrayInput": {
    "title": "My team array input",
    "icon": "My icon",
    "description": "My team array input",
    "type": "array",
    "items": {
      "type": "string",
      "format": "team"
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
      myTeamInput = {
        title       = "My team input"
        description = "My team input"
        format      = "team"
        default     = "my-team"
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
      myTeamArrayInput = {
        title       = "My team array input"
        description = "My team array input"
        format      = "team"
      }
    }
  }
}
```

```
```
