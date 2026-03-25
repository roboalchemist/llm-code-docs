# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/proto.md

# Proto

Proto is a data type used to save .proto definitions in Port

## Common proto usage[â](#common-proto-usage "Direct link to Common proto usage")

The proto property type can be used to store types defined in .proto files, for example:

* Messages between microservices;
* Microservices APIs;

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Array

```
{
  "myProtoProp": {
    "title": "My Proto",
    "icon": "My icon",
    "description": "My proto property",
    "type": "string",
    "format": "proto"
  }
}
```

```
{
  "myProtoArray": {
    "title": "My proto array",
    "icon": "My icon",
    "description": "My proto array",
    "type": "array",
    "items": {
      "type": "string",
      "format": "proto"
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
      "myProtoProp" = {
        title      = "My proto"
        required   = false
        format     = "proto"
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
      "myProtoArray" = {
        identifier = "myProtoArray"
        title      = "My proto array"
        required   = false
        string_items = {
          format = "proto"
        }
      }
    }
  }
}
```

## Pulumi definition[â](#pulumi-definition "Direct link to Pulumi definition")

* Basic

- Python
- TypeScript
- JavaScript
- GO

```
"""A Python Pulumi program"""

import pulumi
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintPropertyArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        string_props={
            "myProtoProp": BlueprintPropertyArgs(
                title="My proto",
                required=False,
                format="proto",
            )
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
      myProtoProp: {
        title: "My proto",
        required: false,
        format: "proto",
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
      myProtoProp: {
        title: "My proto",
        required: false,
        format: "proto",
      },
    },
  },
  relations: [],
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
				"myProtoProp": port.BlueprintPropertiesStringPropsArgs{
					Title:    pulumi.String("My proto"),
					Required: pulumi.Bool(false),
					Format:   pulumi.String("proto"),
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
