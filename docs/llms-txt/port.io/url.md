# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/url.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/url.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/url.md

# URL

URL is an input used to save links to websites.

## ð¡ Common url usage[â](#-common-url-usage "Direct link to ð¡ Common url usage")

The URL input type can be used to store a link to any web resource, for example:

* Link to Datadog dashboard
* Link to configuration file
* Link to pull request

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Select (Enum)
* Array

```
{
  "myUrlInput": {
    "title": "My url input",
    "icon": "My icon",
    "description": "My url input",
    "type": "string",
    "format": "url",
    "default": "https://example.com"
  }
}
```

```
{
  "myUrlSelectInput": {
    "title": "My url select input",
    "icon": "My icon",
    "description": "My url select input",
    "type": "string",
    "format": "url",
    "enum": ["https://example.com", "https://getport.io"]
  }
}
```

```
{
  "myUrlArrayInput": {
    "title": "My url array input",
    "icon": "My icon",
    "description": "My url array input",
    "type": "array",
    "items": {
      "type": "string",
      "format": "url"
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
      "myUrlInput" = {
        title       = "My url input"
        icon        = "My icon"
        description = "My url input"
        format      = "url"
        default     = "https://example.com"
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
      "myUrlSelectInput" = {
        title       = "My url select input"
        icon        = "My icon"
        description = "My url select input"
        format      = "url"
        enum        = ["https://example.com", "https://getport.io"]
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
      "myUrlArrayInput" = {
        title       = "My url array input"
        icon        = "My icon"
        description = "My url array input"
        format      = "url"
      }
    }
  }
}
```
