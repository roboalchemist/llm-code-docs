# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/text.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/text.md

# Text

Text is a basic input for textual information.

## ð¡ Common text usage[â](#-common-text-usage "Direct link to ð¡ Common text usage")

The text input type can be used to store any text based data, for example:

* Image tags
* Variable keys
* Commit SHA
* File names

In the [live demo](https://demo.port.io/self-serve) self-service hub page, we can see the **scaffold new service** action whose `Service Name` input is a text input. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Select (Enum)
* Array
* Enum Array

```
{
  "myTextInput": {
    "title": "My text input",
    "icon": "My icon",
    "description": "My text input",
    "type": "string",
    "default": "My default"
  }
}
```

```
{
  "myTextSelectInput": {
    "title": "My text select input",
    "icon": "My icon",
    "description": "My text select input",
    "type": "string",
    "enum": ["my-option-1", "my-option-2"]
  }
}
```

```
{
  "myTextArrayInput": {
    "title": "My text array input",
    "icon": "My icon",
    "description": "My text array input",
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

```
{
  "myStringArray": {
    "title": "My text-selection array input",
    "icon": "My icon",
    "description": "My text-selection array input",
    "type": "array",
    "items": {
      "type": "string",
      "enum": ["my-option-1", "my-option-2"],
      "enumColors": {
        "my-option-1": "red",
        "my-option-2": "green"
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
    string_props = {
      myTextInput = {
        title       = "My text input"
        description = "My text input"
        default     = "My default"
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
      myTextSelectInput = {
        title       = "My text select input"
        description = "My text select input"
        enum        = ["my-option-1", "my-option-2"]
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
      myTextArrayInput = {
        title       = "My text array input"
        description = "My text array input"
        string_items = {}
      }
    }
  }
}
```

## Validate text[â](#validate-text "Direct link to Validate text")

Text validations support the following operators:

* `minLength` - enforce minimal string length.
* `maxLength` - enforce maximal string length.
* `pattern` - enforce Regex patterns.

- Basic
- Array
- Terraform

```
{
  "myTextInput": {
    "title": "My text input",
    "icon": "My icon",
    "description": "My text input",
    "type": "string",
    "minLength": 1,
    "maxLength": 32,
    "pattern": "^[a-zA-Z0-9-]*-service$"
  }
}
```

```
{
  "myTextArrayInput": {
    "title": "My text array input",
    "icon": "My icon",
    "description": "My text array input",
    "type": "array",
    "items": {
      "type": "string",
      "minLength": 1,
      "maxLength": 32,
      "pattern": "^[a-zA-Z0-9-]*-service$"
    }
  }
}
```

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    string_props = {
      myTextInput = {
        title       = "My text input"
        description = "My text input"
        default     = "My default"
        minLength   = 1
        maxLength   = 32
        pattern     = "^[a-zA-Z0-9-]*-service$"
      }
    }
  }
}
```

## Multi-line text[â](#multi-line-text "Direct link to Multi-line text")

In some cases, you might want to allow users to input long text.<br /><!-- -->You can do so by toggling the `multi-line input` option when creating the input.

This is beneficial for use-cases such as surveys, where the person executing the action might want to provide a relatively long answer to a question.

```
{
  "myTextInput": {
    "title": "My text input",
    "icon": "My icon",
    "description": "My text input",
    "type": "string",
    "format": "multi-line"
  }
}
```
