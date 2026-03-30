# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/enum.md

# Enum

Enum is a data type used to define a named set of constant values.

## ð¡ Common enum usage[â](#-common-enum-usage "Direct link to ð¡ Common enum usage")

The enum property type can be used to define a set of constant values, for example:

* Deployment status: pending, in progress, success, failed.
* Environments: production, staging, development.
* Service health status: healthy, degraded, unhealthy, unkown, maintenance, etc.

## API definition[â](#api-definition "Direct link to API definition")

### Limit field[â](#limit-field "Direct link to Limit field")

When creating a blueprint property of type <!-- -->Enum<!-- --> in the UI, use the **limit** field to define how many values users can select for that property.

In the property creation form, the limit field dropdown provides two options:

* **1 value**: Only one value can be selected.
* **List of values**: Multiple values can be selected.

Selecting the **list of values** option will set the property's `type` to `array` in the JSON definition.

Limit field restriction

The limit field setting, whether it's **1 value** or a **list of values**, is permanent and cannot be changed after the property is created. If you create a property with a single value limit, you wonât be able to change it later to allow multiple values.

To change the limit configuration after creation:

1. Create a new property with the **limit** field set to a **list of values**.
2. Use the [migrate blueprint data](/build-your-software-catalog/customize-integrations/configure-data-model/migrate-data/.md) feature to insert the data to the new property.
3. Delete the old property.
4. Rename the new property to the old property name (optional).

* Basic
* Array

```
{
  "myStringEnum": {
    "title": "My enum",
    "icon": "My icon",
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
    "title": "My enum array",
    "icon": "My icon",
    "description": "My enum array",
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
* Array

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    string_props = {
      "myEnumProp" = {
        title       = "My Enum"
        required    = false
        enum        = ["my-option-1", "my-option-2"]   
        enum_colors = {
            "my-option-1" = "green"
            "my-option-2" = "blue"
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
    my_enum_array_prop = {
        title = "myEnumArrayProp"
        string_items = {
            type = "string"
            enum = [ "my-option-1", "my-option-2", "my-option-3"]
            enum_colors = {
                "my-option-1" = "gold"
                "my-option-2" = "bronze"
                "my-option-3" = "lightGray"
                }
            }
       }
   }
}
```

## Pulumi definition[â](#pulumi-definition "Direct link to Pulumi definition")

* Basic
* Array

- Python
- TypeScript
- JavaScript
- GO

```
"""A Python Pulumi program"""

import pulumi
from port_pulumi import Blueprint

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties={
        "string_props": {
            "myEnumProp": {
                "title": "My Enum",
                "required": True,
                "enum_colors": {
                    "my-option-1": "red",
                    "my-option-2": "green",
                },
                "enums": ["my-option-1", "my-option-2"]
            }
        }
    },
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
      myEnumProp: {
        title: "My Enum",
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
      myEnumProp: {
        title: "My Enum",
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
					"myEnumProp": port.BlueprintPropertiesStringPropsArgs{
                        Title:      pulumi.String("My Enum"),
                        Required:   pulumi.Bool(false),
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

* Python
* TypeScript
* JavaScript
* GO

```
"""A Python Pulumi program"""

import pulumi
from port_pulumi import Blueprint

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="myBlueprint",
    properties={
        "array_props": {
            "myEnumProp": {
                "title":"My Enum Array",
                "required":True,
                "string_items": {
                    "enums" : ["my-option-1", "my-option-2"],
                    "enum_colors" : {
                        "my-option-1": "red",
                        "my-option-2": "green",
                    }
                }
            } 
        }
    },
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
    arrayProps: {
        myEnum: {
            title: "My enum",
            required: true,
            stringItems: {
                enumColors: {
                "my-option-1": "red",
                "my-option-2": "green",
                },
                enums: ["my-option-1", "my-option-2"],
            },
        }
    }
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
    arrayProps: { 
        myEnumProp: {
            title: "My Enum",
            required: true,
            stringItems: {
            enums: ["my-option-1", "my-option-2"],
            enumColors: {
            "my-option-1": "red",
            "my-option-2": "green",
                },
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
			Title:      pulumi.String("myBlueprint"),
			Properties: &port.BlueprintPropertiesArgs{
				ArrayProps: port.BlueprintPropertiesArrayPropsMap{
					"myEnumProp": &port.BlueprintPropertiesArrayPropsArgs{
						Title:    pulumi.String("My Enum"),
						Required: pulumi.Bool(false),
						StringItems: &port.BlueprintPropertiesArrayPropsStringItemsArgs{
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

## Available enum colors[â](#available-enum-colors "Direct link to Available enum colors")

Properties defined using [enum](#api-definition) can also include specific colors for the different values available in the property definition, the available enum colors are:

```
blue
turquoise
orange
purple
pink
yellow
green
red
darkGray
lightGray
bronze
```
