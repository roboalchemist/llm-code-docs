# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/labeled-url-object.md

# Labeled URL

Labeled URL is an object type used to store URLs with custom display labels. This property allows you to associate a human-readable label with a URL, making it easier to display meaningful link text in the UI instead of showing icons only.

Creating via UI

When creating a [URL property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/url.md) in the UI, enabling the **Custom display text** toggle creates a labeled URL property. Note that this toggle cannot be changed after the property is saved.

## Common labeled URL usage[â](#common-labeled-url-usage "Direct link to Common labeled URL usage")

The labeled URL property type can be used to store links with descriptive labels, for example:

* Documentation links with descriptive titles.
* External service dashboards with custom names.
* Related resources with meaningful descriptions.
* Pull request links with PR titles.
* Monitoring dashboards with environment names.

## Schema structure[â](#schema-structure "Direct link to Schema structure")

A labeled URL object contains two fields:

| Field         | Type   | Required | Description                                |
| ------------- | ------ | -------- | ------------------------------------------ |
| `url`         | string | Yes      | The URL to link to (internal or external). |
| `displayText` | string | No       | The display text to show for the link.     |

### Example value[â](#example-value "Direct link to Example value")

```
{
  "url": "https://app.datadoghq.com/dashboard/abc123",
  "displayText": "Production Metrics Dashboard"
}
```

## Display behavior[â](#display-behavior "Direct link to Display behavior")

Labeled URLs are rendered intelligently based on the URL type:

* **Internal links**: Displayed as navigable links within Port.
* **External links**: Displayed as buttons that open in a new tab.

## API definition[â](#api-definition "Direct link to API definition")

* Basic
* Array

```
{
  "myLabeledUrlProp": {
    "title": "My labeled URL",
    "icon": "Link",
    "description": "My labeled URL property",
    "type": "object",
    "format": "labeled-url"
  }
}
```

```
{
  "myLabeledUrlArray": {
    "title": "My labeled URL array",
    "icon": "Link",
    "description": "My labeled URL array",
    "type": "array",
    "items": {
      "type": "object",
      "format": "labeled-url"
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
    object_props = {
      "myLabeledUrlProp" = {
        title       = "My labeled URL"
        description = "My labeled URL property"
        format      = "labeled-url"
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
      "myLabeledUrlArray" = {
        title       = "My labeled URL array"
        description = "My labeled URL array"
        object_items = {
          format = "labeled-url"
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
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintPropertiesObjectPropsArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        object_props={
            "myLabeledUrlProp": BlueprintPropertiesStringPropsArgs(
                title="My labeled URL",
                required=False,
                format="labeled-url",
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
    objectProps: {
      myLabeledUrlProp: {
        title: "My labeled URL",
        required: false,
        format: "labeled-url",
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
    objectProps: {
      myLabeledUrlProp: {
        title: "My labeled URL",
        required: false,
        format: "labeled-url",
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
			Identifier: pulumi.Object("myBlueprint"),
			Title:      pulumi.Object("My Blueprint"),
			Properties: port.BlueprintPropertiesArgs{
				objectProps: port.BlueprintPropertieObjectPropsMap{
					"myLabeledUrlProp": port.BlueprintPropertiesObjectPropsArgs{
						Title:    pulumi.Object("My labeled URL"),
						Required: pulumi.Bool(false),
						Format:   pulumi.Object("labeled-url"),
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
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintPropertiesArrayPropsArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        array_props={
            "myLabeledUrlArray": BlueprintPropertiesArrayPropsArgs(
                title="My labeled URL array",
                required=False,
                object_items={
                    "format": "labeled-url"
                }
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
    arrayProps: {
      myLabeledUrlArray: {
        title: "My labeled URL array",
        required: false,
        objectItems: {
          format: "labeled-url",
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
    arrayProps: {
      myLabeledUrlArray: {
        title: "My labeled URL array",
        required: false,
        objectItems: {
          format: "labeled-url",
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
			Identifier: pulumi.Object("myBlueprint"),
			Title:      pulumi.Object("My Blueprint"),
			Properties: port.BlueprintPropertiesArgs{
				ArrayProps: port.BlueprintPropertiesArrayPropsMap{
					"myLabeledUrlArray": port.BlueprintPropertiesArrayPropsArgs{
						Title:    pulumi.Object("My labeled URL array"),
						Required: pulumi.Bool(false),
						ObjectItems: port.BlueprintPropertiesArrayPropsObjectItemsArgs{
							Format: pulumi.Object("labeled-url"),
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

## Using labeled URLs in self-service actions[â](#using-labeled-urls-in-self-service-actions "Direct link to Using labeled URLs in self-service actions")

You can use labeled URL properties as user inputs in self-service actions and automations. The input form provides a JSON editor with schema validation to ensure proper structure.

### Example action input[â](#example-action-input "Direct link to Example action input")

```
{
  "documentationLink": {
    "title": "Documentation Link",
    "description": "Link to the service documentation",
    "type": "object",
    "format": "labeled-url"
  }
}
```

### Example entity data[â](#example-entity-data "Direct link to Example entity data")

When populating an entity with labeled URL data:

```
{
  "identifier": "my-service",
  "title": "My Service",
  "properties": {
    "documentationLink": {
      "url": "https://docs.example.com/my-service",
      "label": "Service Documentation"
    },
    "relatedLinks": [
      {
        "url": "https://github.com/org/my-service",
        "label": "GitHub Repository"
      },
      {
        "url": "https://app.datadoghq.com/dashboard/xyz",
        "label": "Monitoring Dashboard"
      }
    ]
  }
}
```
