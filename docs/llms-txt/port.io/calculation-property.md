# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property.md

# â Calculation Property

Calculation properties allow you to use existing properties defined on blueprints, either directly or by using relations and mirror properties, in order to create new properties by using the [`jq`](https://github.com/stedolan/jq) processor for `JSON`.

* Filter/Select/Slice/Concatenate data from an existing property;
* Create math equations or modifications. For example, calculate required disk storage by specifying page size, and number of pages needed.
* Merge complex properties, including deep-merge and overriding.

## Common calculation usage[â](#common-calculation-usage "Direct link to Common calculation usage")

Calculation properties make it easier to define properties that are based on values from other properties, with the added ability to transform the data, for example:

* Construct custom URLs based on templates - for example:

  <!-- -->

  * `https://slack.com/ + {my_parameter}`;
  * `https://datadog.com/ + {my_parameter}`;
  * `https://launchdarkly.com/ + {my_parameter}`;

* Merge service configurations templates to create a real service config;

* Calculate the number of code owners;

* etc.

Performance impact of calculation properties

Calculation properties are evaluated dynamically for each entity. Defining complex or numerous calculation properties (especially on blueprints with a large number of entities) can impact page load performance.

It is recommended to use calculation properties only when necessary and prefer simple calculations over complex ones.

In this [live demo](https://demo.port.io/service_catalog) example, we can see the `Slack Notifications` calculation property. ð¬

## Definition[â](#definition "Direct link to Definition")

* API
* Terraform
* Pulumi

The `calculationProperties` key is a top-level key in the JSON of an entity (similar to `identifier`, `title`, `properties`, etc..)

You can access properties as part of the calculation by using `.properties`

```
{
  "calculationProperties": {
    "myCalculationProp": {
      "title": "My calculation property",
      "type": "string",
      "calculation": ".properties.myStringProp + .properties.myStringProp"
    }
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  calculation_properties {
    identifier  = "myCalculationProp"
    title       = "My calculation property"
    type        = "string"
    calculation = ".properties.myStringProp + .properties.myStringProp"
  }
}
```

* Python
* TypeScript
* JavaScript
* GO

```
"""A Python Pulumi program"""

import pulumi
from port_pulumi import Blueprint,BlueprintPropertiesArgs,BlueprintCalculationPropertiesArgs

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    properties=BlueprintPropertiesArgs(
    # blueprint properties
    ),
    calculation_properties={
      "myCalculation": BlueprintCalculationPropertiesArgs(
        title="My calculation property", calculation=".properties.myStringProp + .properties.myStringProp", type="string",
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
  calculationProperties: {
    myCalculation: {
      title: "My calculation property",
      calculation: ".properties.myStringProp + .properties.myStringProp",
      type: "string",
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
  calculationProperties: {
    myCalculation: {
      title: "My calculation property",
      calculation: ".properties.myStringProp + .properties.myStringProp",
      type: "string",
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
            CalculationProperties: port.BlueprintCalculationPropertiesMap{
              "myCalculation": port.BlueprintCalculationPropertiesArgs{
                  Title:       pulumi.String("My calculation property"),
                  Calculation: pulumi.String(".properties.myStringProp + .properties.myStringProp"),
                  Type:        pulumi.String("string"),
              }
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

## Supported Types[â](#supported-types "Direct link to Supported Types")

* Basic
* Format
* Spec

Calculation properties support the following output types: `string`, `number`, `object`, `array`, and `boolean`. For example:

```
{
  "calculationProperties": {
    "myCalculationProp": {
      "title": "My calculation property",
      "type": "my_output_type",
      "calculation": ".properties.myStringProp + .properties.myStringProp"
    }
  }
}
```

Calculation properties support the following output formats: `yaml`, `team`, `user`, `ipv6`, and `url`. For example:

```
{
  "calculationProperties": {
    "myCalculationProp": {
      "title": "My calculation property",
      "type": "string",
      "format": "user",
      "calculation": ".properties.user"
    }
  }
}
```

Calculation properties support the following output specs: `markdown`, `open-api` and `async-api`. For example:

```
{
  "calculationProperties": {
    "myCalculationProp": {
      "title": "My calculation property",
      "type": "string",
      "format": "url",
      "spec": "embedded-url"
      "calculation": ".properties.text"
    }
  }
}
```

## Using `meta properties` in calculation properties[â](#using-meta-properties-in-calculation-properties "Direct link to using-meta-properties-in-calculation-properties")

It is possible to use [meta properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md) as template values for calculation properties.

For example, if you want to concatenate a template URL (for example `https://datadog.com`) with the `identifier` meta property:

Given the following `notification-service` entity:

```
{
  "identifier": "notification-service",
   "title": "Notification Service",
  "properties": {
   ...
  },
}
```

And the following calculation property definition for the blueprint:

```
{
  "calculationProperties": {
    "monitorUrl": {
      "title": "Monitor url",
      "type": "string",
      "format": "url",
      "calculation": "'https://datadog.com/' + .identifier"
    }
  }
}
```

The value of the property `monitorUrl` will be `https://datadog.com/notification-service`

## Using `mirror properties` in calculation properties[â](#using-mirror-properties-in-calculation-properties "Direct link to using-mirror-properties-in-calculation-properties")

It is possible to use [mirror properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/mirror-property.md) as template values for calculation properties.

For example, if an entity has a mirror property called `owningSquad`:

```
"mirrorProperties": {
    "owningSquad": {
        "path": "microservice-to-squad.$title"
    }
}
```

A calculation property that links to the slack channel of the squad can be:

```
"owning_squad_slack": {
    "title": "Owning Squad Channel",
    "calculation": "'https://slack.com/' + .properties.owningSquad",
}
```

Calculation on calculation is not supported

Calculation properties **cannot** be used as template values for other calculation properties.

## Colorized calculation properties[â](#colorized-calculation-properties "Direct link to Colorized calculation properties")

You can colorize calculation properties according to their value, by adding a `colorized` key with the value `true` to the calculation property object. You can also add a `colors` key to specify the colors of the different values, otherwise, the colors will be chosen automatically for you.

For example, if you want to colorize a calculation property called `status-calculation` with the values `OK`, `WARNING`, and `CRITICAL`:

```
"properties":{
    "status":{
        "type": "string"
    },
},
"calculationProperties": {
    "status-calculation": {
        "title": "Status",
        "type": "string",
        "calculation": ".properties.status",
        "colorized": true,
        "colors": {
            "OK": "green",
            "WARNING": "yellow",
            "CRITICAL": "red"
        }
    }
}
```

***

Parameters with special characters

Parameter contains special characters (for example: `-`) or starts with a digit (for example: `@/#/$/1/2/3`), should be surrounded with single quotes.

```

"properties":{
    "prop-with-special-char":{
        "type": "string"
    },
},
"calculationProperties": {
    "myCalculatedProp": {
        "title": "My Calculated Property",
        "type": "string",
        "calculation": ".properties.'prop-with-special-char'",
    }
}
```

## Performance impact[â](#performance-impact "Direct link to Performance impact")

When defined on blueprints with many entities, calculation properties might have negative performance impact, causing long entities table loading time.

If you are facing long loading time for entities table of a blueprint with calculation properties, we recommend replacing the calculation property with a regular property by calculating the needed value on the entity creation itself if possible.

### Replacing calculation property[â](#replacing-calculation-property "Direct link to Replacing calculation property")

Let's demonstrate this with an example:

Suppose we have a `Deployment` blueprint with a string property called `name` and a calculation property called `URL` that is based on the name property.

```
{
  "identifier": "deployment",
  "title": "Deployment",
  "properties":{
      "name":{
          "type": "string"
      },
  },
  "calculationProperties": {
      "URL": {
          "type": "string",
          "calculation": "'https://' + .properties.name + '.port.io'",
      }
  }
}
```

We can avoid this calculation property by create a new string property called `url_temp` (This name is temporary and will be updated once we confirm it has successfully replaced the calculation property). Then we can take the calculation property jq expression and put it directly in the [mapping](/build-your-software-catalog/customize-integrations/configure-mapping.md) section when we map our entities on creation.

```
resources:
  - kind: repository
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: ".name"
          title: ".name"
          blueprint: '"deployment"'
          properties:
            name: ".name"
            url_temp: "'https://' + .name + '.port.io'"
```

Once done, `url_temp` will match the `URL` calculation property when the entity is created.

### Handling existing entities[â](#handling-existing-entities "Direct link to Handling existing entities")

While the new property works for newly created entities, existing entities still rely on the calculation property for their URL value.

You can handle this in two ways:

1. **Resync all entities** so the mapping change we applied also affects existing entities.
2. **Create a** [**Port migration**](/build-your-software-catalog/customize-integrations/configure-data-model/migrate-data/.md) on the blueprint, to populate the new property with URL values for existing entities.

After completing these steps and verifying that the calculation property has been successfully replaced, we can remove the old `URL` property and rename the identifier of the `url_temp` to be `URL`.

If you prefer not to delete the old property right away, you can first exclude it from the entities table using the [excluded properties](/customize-pages-dashboards-and-plugins/page/catalog-page.md#excluded-properties) and see if there is any performance improvement.

## Examples[â](#examples "Direct link to Examples")

Refer to the calculation property [examples](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/examples.md) page.
