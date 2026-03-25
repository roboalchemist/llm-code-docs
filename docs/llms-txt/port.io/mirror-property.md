# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/mirror-property.md

# Mirror Property

Mirror property allows you to map data from related entities to your entity. Mirror property can be used for blueprints that have [relations defined](/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints/.md).

When two blueprints are connected via a relation, a new set of properties becomes available to entities in the `source` blueprint.

Those new properties are called `mirrorProperties`.

Mirror properties will appear on the `source` blueprint as an additional key called `mirrorProperties`. It represents additional properties queried from the `target` blueprint (or from other entities further down the connection graph).

Mirror properties allow you to map property values from related entities, to `keys` in the `source` blueprint, thus giving you more context and data when viewing an Entity, while not cluttering the output with unnecessary fields.

Mirror properties support both [user-defined](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#available-properties) properties, and [meta-properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md) by using similar syntax.

## Common mirror usage[â](#common-mirror-usage "Direct link to Common mirror usage")

Mirror properties make it possible to enrich the data visible on an entity by mapping additional data and properties from other related entities in the catalog, for example:

* Show the chart version of a running service.
* Show the environment type of a running service.
* Show the cloud provider of a K8s cluster.

In this [live demo](https://demo.port.io/_teamEntity?identifier=guardians_of_the_galaxy) example, we can see the `Manager` property which is a mirror property of the related `User` blueprint. ð¬

## API definition[â](#api-definition "Direct link to API definition")

The `mirrorProperties` key is a top-level key in the JSON of an entity (similar to `identifier`, `title`, `properties`, etc..)

* Basic

```
{
  "mirrorProperties": {
    "myMirrorProp": {
      "title": "My mirror property",
      "path": "myRelation.myProperty"
    }
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

info

The `path` key receives a path of chained relations, which lead up to a blueprint property or [meta-property](#meta-property-as-a-mirror-property)

## Terraform definition[â](#terraform-definition "Direct link to Terraform definition")

* Basic

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  mirror_properties = {
    myMirrorProp = {
      title = "My mirror property"
      path  = "myRelation.myProperty"
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
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintMirrorPropertiesArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
        # blueprint properties
    ),
    mirror_properties={
        "myMirrorProp": BlueprintMirrorPropertiesArgs(
            title="My mirror property", path="myRelation.myStringProp"
        )
    },
)
```

```
import * as pulumi from "@pulumi/pulumi";
import * as port from "@port-labs/port";

export const blueprint = new port.Blueprint("myBlueprint", {
  identifier: "myBlueprint",
  title: "My Blueprint",
  properties: {
    // blueprint properties
  },
  mirrorProperties: {
    myMirrorProp: {
      title: "My mirror property",
      path: "myRelation.myProperty",
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
    // blueprint properties
  },
  mirrorProperties: {
    myMirrorProp: {
      title: "My mirror property",
      path: "myRelation.myProperty",
    },
  },
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
			// blueprint properties..
			MirrorProperties: port.BlueprintMirrorPropertiesMap{
              "myMirrorProp": port.BlueprintMirrorPropertiesArgs{
                    Title: pulumi.String("My mirror property"),
                    Path:  pulumi.String("myRelation.myProperty"),
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

## `Meta-property` as a mirror property[â](#meta-property-as-a-mirror-property "Direct link to meta-property-as-a-mirror-property")

This is a mirror property created from one of Port's [meta-properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md) on the `target` blueprint.

In the following example, we create a mirror property called `microserviceName` which is mapped to the `title` meta-property in the `target` blueprint (in this example the name of the relation is `deployment-to-microservice`). Note how the `title` field is referenced using `$title` because it is a meta-property:

```
"microserviceName": {
    "title": "Microservice Name",
    "path": "deployment-to-microservice.$title"
}
```

## Nested relation as a mirror property[â](#nested-relation-as-a-mirror-property "Direct link to Nested relation as a mirror property")

It is possible to use mirror properties to map properties from blueprints that are not direct descendants of our `source` blueprint.

For example, let's assume we have the following Relation chain: `Microservice -> System -> Domain`.

We want to map the members of the domain that owns the microservice directly to the `Microservice` entities.

The members of the domain are listed in an [array property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/array.md) under the user-defined property `domain_members`.

The names of the relations are:

* `Microservice -> System`: `system`
* `System -> Domain`: `domain`

Let's map the squad members using a mirror property called `owningDomainMembers`:

```
"owningDomainMembers": {
    "title": "Owning Domain Members",
    "path": "system.domain.domain_members"
}
```
