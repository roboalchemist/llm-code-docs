# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/yaml.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/yaml.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/yaml.md

# Yaml

Yaml is an input used to save object definitions in YAML.

## ð¡ Common yaml usage[â](#-common-yaml-usage "Direct link to ð¡ Common yaml usage")

The yaml input type can be used to store any key/value based data, for example:

* Configurations
* Helm charts
* Dictionaries/Hash maps
* Manifests
* `values.yml`

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Array

```
{
  "myYamlInput": {
    "title": "My yaml input",
    "icon": "My icon",
    "description": "My yaml input",
    "type": "string",
    "format": "yaml"
  }
}
```

```
{
  "myYamlArrayInput": {
    "title": "My yaml array input",
    "icon": "My icon",
    "description": "My yaml array input",
    "type": "array",
    "items": {
      "type": "string",
      "format": "yaml"
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
      "myYamlInput" = {
        title       = "My yaml input"
        description = "My yaml input"
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
      "myYamlArrayInput" = {
        title       = "My yaml array input"
        description = "My yaml array input"
        string_items = {
          format = "yaml"
        }
      }
    }
  }
}
```
