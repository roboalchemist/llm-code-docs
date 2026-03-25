# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/toggle.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/toggle.md

# Toggle (Boolean)

Toggle is a basic boolean input that has one of two possible values - `true` and `false`.<br /><!-- -->In Port, this input type is represented by a switch that can be toggled on or off.

## ð¡ Common toggle usage[â](#-common-toggle-usage "Direct link to ð¡ Common toggle usage")

This input type can be used to store any true/false gate, for example:

* Is environment locked for deployments
* Should environment perform nightly shutdown
* Does service handle PII
* Is environment public

In the [live demo](https://demo.port.io/self-serve) self-service hub page, we can see the **Delete Repo** action whose `Confirm` input is a toggle input. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic

```
{
  "myBooleanInput": {
    "title": "My boolean input",
    "icon": "My icon",
    "description": "My boolean input",
    "type": "boolean",
    "default": true
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

* Basic

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    boolean_props = {
      myBooleanInput = {
        title       = "My boolean input"
        description = "My boolean input"
        default     = true
      }
    }
  }
}
```
