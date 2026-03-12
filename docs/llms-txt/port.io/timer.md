# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/timer.md

# Timer

Timer is a data type used to define an expiration date/lifespan of a specific entity.

## Common timer usage[â](#common-timer-usage "Direct link to Common timer usage")

The timer property type can be used to store the future expiration date of catalog entities and properties, for example:

* Temporary development environment.
* Countdown to next healthcheck.
* Temporary cloud resources.
* Add temporary permissions to resource.

In this [live demo](https://demo.port.io/developer_envs) example, we can see the `TTL` timer property. ð¬

## API definition[â](#api-definition "Direct link to API definition")

* Basic

```
{
  "myTimerProp": {
    "title": "My timer",
    "icon": "My icon",
    "description": "My timer property",
    "type": "string",
    "format": "timer",
    "default": "2022-04-18T11:44:15.345Z"
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

* Basic

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    string_props = {
      "myTimerProp" = {
        title       = "My timer"
        icon        = "My icon"
        description = "My timer property"
        format      = "timer"
        default     = "2022-04-18T11:44:15.345Z"
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
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintPropertiesStringPropsArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        string_props={
            "myTimerProp": BlueprintPropertiesStringPropsArgs(
                title="My timer",
                format="timer",
                required=True,
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
      myTimerProp: {
        title: "My timer",
        format: "timer",
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
      myTimerProp: {
        title: "My timer",
        format: "timer",
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
					"myTimerProp": &port.BlueprintPropertiesStringPropsArgs{
                        Title:    pulumi.String("My timer"),
                        Format:   pulumi.String("timer"),
                        Required: pulumi.Bool(true),
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

## Example[â](#example "Direct link to Example")

Here is an entity for a `timerExample` blueprint which has a timer property with the identifier `timer`.

In the example entity, an expiration datetime is specified:

```
  "identifier": "entityIdentifier",
  "title": "Timer Example",
  "icon": "Microservice",
  "blueprint": "timerExample",
  "properties": {
    "timer": "2022-12-01T16:50:00+02:00"
  },
  "relations": {}
```

Looking at Port's UI, we can see that the timer we created expires in 2 hours:

![Timer entity](/assets/images/TTLCreateEntity-ae9c958c4f096781583e5cca37a15c5f.png)

After 2 hours pass, the property status will change to `Expired`, and an event of `Timer Expired` will be sent to the ChangeLog:

![Timer entity expired](/assets/images/TTLExpiredEntity-ca9d715031012b3fb1fd3a77850037cf.png)

The timer expiration event will also appear in Port's audit log:

![Timer Audit log](/assets/images/AuditLogTTL-7897536b6e810c4120671829320d92d9.png)

In order to notify about the timer expiration, the following notification body will be sent to the Webhook/Kafka topic configured in the blueprint's `changelogDestination`:

```
{
  "context": {
    "blueprint": "timerExample",
    "entity": "entityIdentifier"
  },
  "action": "TIMER_EXPIRED",
  "trigger": {
    "at": "2022-12-01T16:50:00+02:00",
    "by": {
      "byPort": true,
      "orgId": "org_example"
    },
    "origin": "API"
  },
  "resourceType": "entity",
  "status": "SUCCESS"
}
```
