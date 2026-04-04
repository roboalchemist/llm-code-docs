# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/boolean.md

# Boolean

Boolean is a primitive data type that has one of two possible values - `true` and `false`.

## Common boolean usage[â](#common-boolean-usage "Direct link to Common boolean usage")

The boolean property type can be used to store any true/false gate, for example:

* Is environment locked for deployments
* Should environment perform nightly shutdown
* Does service handle PII
* Is environment public

## API definition[â](#api-definition "Direct link to API definition")

```
{
  "myBooleanProp": {
    "title": "My boolean",
    "icon": "My icon",
    "description": "My boolean property",
    "type": "boolean",
    "default": true
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    boolean_props = {
      "myBooleanProp" = {
        title      = "My boolean"
        required   = true
      }
    }
  }
}
```

## Pulumi definition[â](#pulumi-definition "Direct link to Pulumi definition")

* Python
* TypeScript
* JavaScript
* GO

```
"""A Python Pulumi program"""

import pulumi
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintPropertiesBooleanPropsArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        boolean_props={
            "myBooleanProp": BlueprintPropertiesBooleanPropsArgs(
                title="My boolean",
                required=True,
            )
        }
    ),
    relations={},
)
```

```
import * as pulumi from "@pulumi/pulumi";
import * as port from "@port-labs/port";

export const blueprint = new port.Blueprint("myBlueprint", {
  identifier: "myBlueprint",
  title: "My Blueprint",
  properties: {
    booleanProps: {
      myBooleanProp: {
        title: "My boolean",
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
    booleanProps: {
      myBooleanProp: {
        title: "My boolean",
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
				BooleanProps: port.BlueprintPropertiesBooleanPropsMap{
					"myBooleanProp": port.BlueprintPropertiesBooleanPropsArgs{
						Title:    pulumi.String("My boolean"),
						Required: pulumi.Bool(false),
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
