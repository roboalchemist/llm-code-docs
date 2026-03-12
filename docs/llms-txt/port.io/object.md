# Source: https://docs.port.io/workflows/build-workflows/self-service-trigger/user-inputs/object.md

# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/object.md

# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/object.md

# Object

Object is a basic input for JSON data.

## ð¡ Common object usage[â](#-common-object-usage "Direct link to ð¡ Common object usage")

The object input type can be used to store any key/value based data, for example:

* Configurations
* Tags
* HTTP responses
* Dictionaries/Hash maps

In the [live demo](https://demo.port.io/self-serve) self-service hub page, we can see the **Open terraform PR to add S3 bucket** action whose `policy` input is an object input. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Select (Enum)
* Array

```
{
  "myObjectInput": {
    "title": "My object input",
    "icon": "My icon",
    "description": "My object input",
    "type": "object",
    "default": {
      "myKey": "myValue"
    }
  }
}
```

```
{
  "myObjectSelectInput": {
    "title": "My object select input",
    "icon": "My icon",
    "description": "My object select input",
    "type": "object",
    "enum": [
      {
        "myKey": 1
      },
      {
        "myKey": 2
      }
    ]
  }
}
```

```
{
  "myObjectArrayInput": {
    "title": "My object array input",
    "icon": "My icon",
    "description": "My object array input",
    "type": "array",
    "items": {
      "type": "object"
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
    object_props = {
      "myObjectInput" = {
        title       = "My object input"
        description = "My object input"
        default     = jsonencode({ "myKey" = "myValue" })
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
      "myObjectArrayInput" = {
        title       = "My object array input"
        description = "My object array input"
        object_items = {}
      }
    }
  }
}
```

## Validate object[â](#validate-object "Direct link to Validate object")

Object validations support the following operators:

* `properties` - defines the schema for object keys when present. Only the entire object can be marked as required via the action's top-level `required array`. A `required` array inside an object input is not supported.
* `additionalProperties` - whether keys not defined in `properties` are allowed (boolean) or what type they should be (type definition).
* `patternProperties` - which regex pattern should properties follow

Object validation limits

Port does not support making individual keys inside an object required. A `required` array defined inside an object-type input is not supported and will be rejected. You can only require the object input as a whole using the action's top-level required array.

Where supported, object validations follow the JSON schema model. See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/object.html) for available validations.

* Basic
* Array
* Terraform - coming soon

```
{
  "myObjectInput": {
    "title": "My object input",
    "icon": "My icon",
    "description": "My object input",
    "type": "object",
    "properties": {
      "myNumberProp": { "type": "number" }
    },
    "patternProperties": {
      "^S_": { "type": "string" },
      "^I_": { "type": "number" }
    },
    "additionalProperties": true
  }
}
```

```
{
  "myObjectArrayInput": {
    "title": "My object array input",
    "icon": "My icon",
    "description": "My object array input",
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "myNumberProp": { "type": "number" }
      },
      "patternProperties": {
        "^S_": { "type": "string" },
        "^I_": { "type": "number" }
      },
      "additionalProperties": true
    }
  }
}
```
