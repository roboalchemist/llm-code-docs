# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/string.md

# String

String is a primitive data type used to save text data.

## Common string usage[â](#common-string-usage "Direct link to Common string usage")

The string property type can be used to store any text based data, for example:

* Image tags
* Variable keys
* Commit SHA
* File names

In this [live demo](https://demo.port.io/service_catalog) example, we can see the `Language` string property. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Enum
* Array
* Enum Array

```
{
  "myStringProp": {
    "title": "My string",
    "icon": "My icon",
    "description": "My string property",
    "type": "string",
    "default": "My default"
  }
}
```

```
{
  "myStringEnum": {
    "title": "My string enum",
    "icon": "My icon",
    "description": "My string enum",
    "type": "string",
    "enum": ["my-option-1", "my-option-2"],
    "enumColors": {
      "my-option-1": "red",
      "my-option-2": "green"
    }
  }
}
```

```
{
  "myStringArray": {
    "title": "My string array",
    "icon": "My icon",
    "description": "My string array",
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
    "title": "My string enum array",
    "icon": "My icon",
    "description": "My string enum array",
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
* Enum
* Array

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    string_props = {
      "myStringProp" = {
        title      = "My string"
        required   = false
      }
    }
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    string_props = {
      "myStringProp" = {
        title      = "My string"
        required   = false
        enum       = ["my-option-1", "my-option-2"]
        enum_colors = {
          "my-option-1" = "red"
          "my-option-2" = "green"
        }
      }
    }
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    array_props = {
      "myStringArray" = {
        title        = "My string array"
        string_items = {} # Pass an empty object only sets the type to string
      }
      "myStringArrayWithDefault" = {
        title = "My string array with default"
        string_items = {
          default = ["my-default-1", "my-default-2"]
        }
      }
    }
  }
}
```

## Pulumi definition[â](#pulumi-definition "Direct link to Pulumi definition")

* Basic
* Enum

- Python
- TypeScript
- JavaScript
- GO

```
"""A Python Pulumi program"""

import pulumi
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintPropertiesStringPropsArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        string_props={
            "myStringProp": BlueprintPropertiesStringPropsArgs(
                title="My string", required=False
            )
    ),
    relations={}
)
```

```
import * as pulumi from "@pulumi/pulumi";
import * as port from "@port-labs/port";

export const blueprint = new port.Blueprint("myBlueprint", {
  identifier: "myBlueprint",
  title: "My Blueprint",
  properties: {
    stringProps: {
      myStringProp: {
        title: "My string",
        required: true,
      },
    },
  },
});
```

```
"use strict";
const pulumi = require("@pulumi/pulumi");
const port = require("@port-labs/port");

const entity = new port.Blueprint("myBlueprint", {
  title: "My Blueprint",
  identifier: "myBlueprint",
  properties: {
    stringProps: {
      myStringProp: {
        title: "My string",
        required: true,
      },
    },
  },
  relations: {},
});

exports.title = entity.title;
```

```
package main

import (
	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		blueprint, err := port.NewBlueprint(ctx, "myBlueprint", &port.BlueprintArgs{
			Identifier: pulumi.String("myBlueprint"),
			Title:      pulumi.String("My Blueprint"),
			Properties: port.BlueprintPropertiesArgs{
				StringProps: port.BlueprintPropertiesStringPropsMap{
					"myStringProp": &port.BlueprintPropertiesStringPropsArgs{
                        Title:      pulumi.String("My String"),
                        Required:   pulumi.Bool(true),
                    },
                },
			},
		})
		ctx.Export("blueprint", blueprint.Title)
		if err != nil {
			return err
		}
		return nil
	})
}
```

* Python
* TypeScript
* JavaScript
* GO

```
"""A Python Pulumi program"""

import pulumi
from port_pulumi import Blueprint,BlueprintPropertiesArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        string_props={
            "myStringProp": {
                "title": "My String",
                "required": True,
                "enums": ["my-option-1", "my-option-2"],
                "enum_colors": {
                    "my-option-1": "red",
                    "my-option-2": "green"
                }
            }
        }
    ),
    relations={}
)
```

```
import * as pulumi from "@pulumi/pulumi";
import * as port from "@port-labs/port";

export const blueprint = new port.Blueprint("myBlueprint", {
  identifier: "myBlueprint",
  title: "My Blueprint",
  properties: {
    stringProps: {
      myStringProp: {
        title: "My String",
        required: true,
        enums: ["my-option-1", "my-option-2"],
        enumColors: {
          "my-option-1": "red",
          "my-option-2": "green",
        },
      },
    },
  },
});
```

```
"use strict";
const pulumi = require("@pulumi/pulumi");
const port = require("@port-labs/port");

const entity = new port.Blueprint("myBlueprint", {
  title: "My Blueprint",
  identifier: "myBlueprint",
  properties: {
    stringProps: {
      myStringProp: {
        title: "My String",
        required: true,
        enums: ["my-option-1", "my-option-2"],
        enumColors: {
          "my-option-1": "red",
          "my-option-2": "green",
        },
      },
    },
  },
  relations: {},
});

exports.title = entity.title;
```

```
package main

import (
	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		blueprint, err := port.NewBlueprint(ctx, "myBlueprint", &port.BlueprintArgs{
			Identifier: pulumi.String("myBlueprint"),
			Title:      pulumi.String("My Blueprint"),
			Properties: port.BlueprintPropertiesArgs{
				StringProps: port.BlueprintPropertiesStringPropsMap{
					"myStringProp": port.BlueprintPropertiesStringPropsArgs{
                        Title:      pulumi.String("My String"),
                        Required:   pulumi.Bool(false),
                        Type:       pulumi.String("string"),
                        Enums: pulumi.StringArray{
                            pulumi.String("my-option-1"),
                            pulumi.String("my-option-2"),
                        },
                        EnumColors: pulumi.StringMap{
                            "my-option-1": pulumi.String("red"),
                            "my-option-2": pulumi.String("green"),
                        },
                    },
                },
			},
		})
		ctx.Export("blueprint", blueprint.Title)
		if err != nil {
			return err
		}
		return nil
	})
}
```

## Validate string[â](#validate-string "Direct link to Validate string")

String validations support the following operators:

* `minLength` - enforce minimal string length.
* `maxLength` - enforce maximal string length.
* `pattern` - enforce Regex patterns.

- Basic
- Array
- Terraform
- Pulumi

```
{
  "myStringProp": {
    "title": "My string",
    "icon": "My icon",
    "description": "My string property",
    "type": "string",
    "minLength": 1,
    "maxLength": 32,
    "pattern": "^[a-zA-Z0-9-]*-service$"
  }
}
```

```
{
  "myStringArray": {
    "title": "My string array",
    "icon": "My icon",
    "description": "My string array",
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
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    string_props = {
      "myStringProp" = {
        title      = "My string"
        required   = false
        min_length = 1
        max_length = 32
        pattern    = "^[a-zA-Z0-9-]*-service$"
      }
    }
  }
}
```

```
export const blueprint = new port.Blueprint("myBlueprint", {
  // ...blueprint properties
  properties: {
    stringProps: {
      myStringProp: {
        maxLength: 32,
        minLength: 1,
        pattern: "^[a-zA-Z0-9-]*-service$"
      }
    }
  }
});
```

## Available enum colors[â](#available-enum-colors "Direct link to Available enum colors")

Properties defined using [enum](#api-definition) can also include specific colors for the different values available in the property definition, to see the available enum colors refer to the [enum page](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/enum.md#available-enum-colors).
