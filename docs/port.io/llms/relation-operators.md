# Source: https://docs.port.io/search-and-query/operators/relation-operators.md

# Relation operators

This page details the available relation operators when writing [rules](/search-and-query/structure-and-syntax.md#rules) as part of the search route.

## RelatedTo[â](#relatedto "Direct link to RelatedTo")

The `relatedTo` operator will return all entities that have a relationship with the specified entity:

### Structure[â](#structure "Direct link to Structure")

| Field       | Description                                                                                |
| ----------- | ------------------------------------------------------------------------------------------ |
| `operator`  | Search operator to use when evaluating this rule, see a list of available operators below. |
| `blueprint` | Blueprint of the entity identifier specified in the `value` field.                         |
| `value`     | Value to filter by.                                                                        |

```
{
  "operator": "relatedTo",
  "blueprint": "myBlueprint",
  "value": "myEntity"
}
```

The operator also supports multiple related entities as the searched value:

```
{
  "operator": "relatedTo",
  "blueprint": "myBlueprint",
  "value": ["myFirstEntity", "mySecondEntity"]
}
```

This query will return all of the entities that are related to one or more of the identifiers in the value array.

### Required[â](#required "Direct link to Required")

The `relatedTo` operator also supports the `required` property - which allows you to search for:

* Related entities from all relations (relations with either required `true` or `false`).
* Related entities only from required relations (relations with required `true`).
* Related entities only from non-required relations (relations with required `false`).

For example, to search only for related entities that *require* the `myEntity` entity from the `myBlueprint` blueprint, use the following search rule:

```
{
  "operator": "relatedTo",
  "required": true,
  "value": "myEntity",
  "blueprint": "myBlueprint"
}
```

### Direction[â](#direction "Direct link to Direction")

The `relatedTo` operator also supports the `direction` property - which allows you to search for dependent entities in a specific direction on the dependency graph. To better understand the functionality of this property, let's take a look at the example below:

Let's assume that we have the blueprints `deploymentConfig` and `microservice` with the following relation definition (declared on the `deploymentConfig` blueprint):

```
"relations": {
  "microservice": {
    "description": "The service this Deployment Config belongs to",
    "many": false,
    "required": false,
    "target": "microservice",
    "title": "Microservice"
  }
}
```

In addition, we have the following entities:

```
Deployment Configs:
- Order-Service-Production
- Cart-Service-Production

Microservices:
- Order Service
- Cart Service

Environments:
- Production
```

And the following relations:

```
Order-Service-Production -> Order-Service
Order-Service-Production -> Production

Cart-Service-Production -> Cart-Service
Cart-Service-Production -> Production
```

By looking at the resulting graph layout, we can also map the directions:

![Dependency graph upstream downstream diagram](/assets/images/search-direction-diagram-faab8361638f4c4f6c67294958fe94bb.png)

* To search for entities which the source depends on - use `"direction": "upstream"`.
* To search for entities which depend on the source - use `"direction": "downstream"`.

In the example shown above, if we want to get the `Microservice` and `Environment` that *Order-Service-Production* depends on, the search rule would be:

```
{
  "operator": "relatedTo",
  "blueprint": "deploymentConfig",
  "value": "Order-Service-Production",
  "direction": "upstream"
}
```

And the result shall be:

**Order-Service-Production upstream related entities (click to expand)**

```
{
  "ok": true,
  "matchingBlueprints": ["microservice", "environment"],
  "entities": [
    {
      "identifier": "Order-Service",
      "title": "Order-Service",
      "blueprint": "microservice",
      "properties": {
        "on-call": "mor@getport.io",
        "language": "Python",
        "slack-notifications": "https://slack.com/Order-Service",
        "launch-darkly": "https://launchdarkly.com/Order-Service"
      },
      "relations": {},
      "createdAt": "2022-11-17T15:54:20.432Z",
      "createdBy": "auth0|62ab380295b34240aa511cdb",
      "updatedAt": "2022-11-17T15:54:20.432Z",
      "updatedBy": "auth0|62ab380295b34240aa511cdb"
    },
    {
      "identifier": "Production",
      "title": "Production",
      "blueprint": "environment",
      "properties": {
        "awsRegion": "eu-west-1",
        "configUrl": "https://github.com/config-labs/kube/config.yml",
        "slackChannel": "https://yourslack.slack.com/archives/CHANNEL-ID",
        "onCall": "Mor P",
        "namespace": "Production"
      },
      "relations": {},
      "createdAt": "2022-09-19T08:54:23.025Z",
      "createdBy": "Cnc3SiO7T0Ld1y1u0BsBZFJn0SCiPeLS",
      "updatedAt": "2022-10-16T09:28:32.960Z",
      "updatedBy": "auth0|62ab380295b34240aa511cdb"
    }
  ]
}
```

If we want to get all of the `deploymentConfigs` that are deployed in the *Production* `Environment`, the search rule would be:

```
{
  "operator": "relatedTo",
  "blueprint": "environment",
  "value": "Production",
  "direction": "downstream"
}
```

And the result shall be:

**Production downstream related entities (click to expand)**

```
{
  "ok": true,
  "matchingBlueprints": ["deploymentConfig"],
  "entities": [
    {
      "identifier": "Order-Service-Production",
      "title": "Order-Service-Production",
      "blueprint": "deploymentConfig",
      "properties": {
        "url": "https://github.com/port-labs/order-service",
        "config": {
          "encryption": "SHA256"
        },
        "monitor-links": [
          "https://grafana.com",
          "https://prometheus.com",
          "https://datadog.com"
        ]
      },
      "relations": {
        "microservice": "Order-Service",
        "environment": "Production"
      },
      "createdAt": "2022-11-17T15:55:55.591Z",
      "createdBy": "auth0|62ab380295b34240aa511cdb",
      "updatedAt": "2022-11-17T15:55:55.591Z",
      "updatedBy": "auth0|62ab380295b34240aa511cdb"
    },
    {
      "identifier": "Cart-Service-Production",
      "title": "Cart-Service-Production",
      "blueprint": "deploymentConfig",
      "properties": {
        "url": "https://github.com/port-labs/cart-service",
        "config": {
          "foo": "bar"
        },
        "monitor-links": [
          "https://grafana.com",
          "https://prometheus.com",
          "https://datadog.com"
        ]
      },
      "relations": {
        "microservice": "Cart-Service",
        "environment": "Production"
      },
      "createdAt": "2022-11-17T15:55:10.714Z",
      "createdBy": "auth0|62ab380295b34240aa511cdb",
      "updatedAt": "2022-11-17T15:55:20.253Z",
      "updatedBy": "auth0|62ab380295b34240aa511cdb"
    }
  ]
}
```

## MatchAny[â](#matchany "Direct link to MatchAny")

The `matchAny` operator will match entities based on your input:

* If you specify a single value, it will find all entities with the same identifier.
* If you provide a list of values, it will match any entity whose identifier is in the list.

### Related to by specific path[â](#related-to-by-specific-path "Direct link to Related to by specific path")

You can search for entities that are related through a specific path of relations. This is useful when you want to find entities that are connected through a specific chain of relationships.

### Structure[â](#structure-1 "Direct link to Structure")

| Field                    | Description                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| `property.path`          | An array containing the full path of relation identifiers to traverse.                                               |
| `property.fromBlueprint` | *(Optional)* The blueprint to start the path traversal from. If omitted, traversal starts from the target blueprint. |
| `operator`               | The search operator to use. For this feature, use `"matchAny"`.                                                      |
| `value`                  | The value or list of values to match against the target entity identifiers at the end of the path.                   |

#### For upstream paths[â](#for-upstream-paths "Direct link to For upstream paths")

```
{
  "property": {
    "path": ["relation1", "relation2", "relation3"]
  },
  "operator": "matchAny",
  "value": "targetEntity"
}
```

#### For downstream paths[â](#for-downstream-paths "Direct link to For downstream paths")

```
{
  "property": {
    "path": ["relation1", "relation2", "relation3"],
    "fromBlueprint": "sourceBlueprint"
  },
  "operator": "matchAny",
  "value": "targetEntity"
}
```

When using downstream paths, the `fromBlueprint` parameter specifies the source blueprint from which to start the path traversal.

Instead of thinking about the path as downstream from the target, we treat it as upstream from the specified blueprint to the target blueprint. This means that the path will be traversed starting from entities of the specified `fromBlueprint`.

### Examples[â](#examples "Direct link to Examples")

Suppose you have the following data model:

![](/img/software-catalog/search-in-port/specific-path-diagram-example.png)

#### Find all services related to a cluster (upstream)

To find all services that are related to a specific cluster (e.g., "production-cluster"):

```
{
  "combinator": "and",
  "rules": [
    {
      "property": "$blueprint",
      "operator": "=",
      "value": "service"
    },
    {
      "property": {
        "path": ["deployedOn"]
      },
      "operator": "matchAny",
      "value": "production-cluster"
    }
  ]
}
```

This will return all **services** that have a deployment in the "production-cluster".

***

#### Example 2: Find all deployments related to a specific service (downstream)

To find all deployments related to a specific service (e.g., "production-service"):

```
{
  "combinator": "and",
  "rules": [
    {
      "property": "$blueprint",
      "operator": "=",
      "value": "deployment"
    },
    {
      "property": {
        "path": ["deployedOn", "deployments"],
        "fromBlueprint": "service"
      },
      "operator": "matchAny",
      "value": "production-service"
    }
  ]
}
```

This will return all **deployments** that are related to the "production-service".

***

#### Contextual values[â](#contextual-values "Direct link to Contextual values")

You can combine relation-path filters with [contextual query rules](/search-and-query/structure-and-syntax.md#contextual-query-rules) to dynamically filter entities based on the current user. This is useful when you need to filter entities based on ownership derived from related entities.

The following rule filters entities where the owner is derived from a **directly related entity**:

```
{
  "combinator": "and",
  "rules": [
    {
      "operator": "matchAny",
      "property": {
        "path": ["relationID_1"]
      },
      "value": {
        "context": "user",
        "property": "$identifier"
      }
    }
  ]
}
```

This will return all entities where the related entity (via `relationID_1`) matches the current user's identifier.

You can also traverse **multiple relations** to find ownership. The following rule filters entities where the owner is derived by traversing through two related entities:

```
{
  "combinator": "and",
  "rules": [
    {
      "operator": "matchAny",
      "property": {
        "path": ["relationID_1", "relationID_2"]
      },
      "value": {
        "context": "user",
        "property": "$identifier"
      }
    }
  ]
}
```

This will return all entities where the entity at the end of the relation chain (traversing `relationID_1` â `relationID_2`) matches the current user's identifier.

In the above examples:

* `property.path` specifies the chain of relations to traverse (replace the relation names with your actual relation identifiers).
* The contextual `value` dynamically resolves to the current user's identifier.
* The `matchAny` operator matches entities where the value at the end of the relation path equals the contextual value.

## Self-relation[â](#self-relation "Direct link to Self-relation")

Self-relations allow a blueprint to reference itself, so entities of the same type can be connected.

![](/img/guides/hierarchyTiers/hierarchyTiers.png)

<br />

<br />

In this example, a **group** is comprised of one or more **domains**, which are comprised of one or more **tribes**, and so on.<br /><!-- -->The diagram illustrates the hierarchy, where different entities are linked by the same self-relation (parent) within the `Team` blueprint.

You can use the `matchAny` operator to search through self-relations, allowing you to find entities at various levels of the hierarchy.

### Examples[â](#examples-1 "Direct link to Examples")

**Example 1: basic self-relation with fixed hops count**

If you want **exactly 2 hops**, specify the self-relation twice:

```
{
  "combinator": "and",
  "rules": [
    {
      "property": {
        "path": [
          "parent",
          "parent"
        ],
        "fromBlueprint" : "Team"
      },
      "operator": "matchAny",
      "value": "targetEntity"
    }
  ]
}
```

For example, if the `value` is `Squad`:

* First hop: `Squad` â `Tribe`.
* Second hop: `Tribe` â `Domain`.

Result: `Domain` (only the final destination after exactly 2 hops).

***

**Example 2: self-relation with maxHops for variable hops**

If you want a variable number of hops (between 1 and 15), use `maxHops`.<br />`maxHops` specifies the maximum number of hops to traverse through the self-relation.

```
{
  "combinator": "and",
  "rules": [
    {
      "property": {
        "path": [
          {
            "relation": "parent",
            "maxHops": 3
          }
        ],
        "fromBlueprint": "Team"
      },
      "operator": "matchAny",
      "value": "targetEntity"
    }
  ]
}
```

For example, if the `value` is `Squad`:

* First hop: `Squad` â `Tribe`.
* Second hop: `Tribe` â `Domain`.
* Third hop: `Domain` â `Group`.

Result: `Tribe`, `Domain` and `Group` (all entities found along the path up to 3 hops).

maxHops limitation

The `maxHops` parameter can only be applied **once** per path, and it accepts values from **1 to 15**.

***

**Example 3: mixed approach**

You can also mix fixed hops with variable hops. For example, if you specify the self-relation twice followed by a `maxHops` object, the system will start traversing from the 2 hops already made and continue with the additional hops specified in `maxHops`.

```
{
  "combinator": "and",
  "rules": [
    {
      "property": {
        "path": [
          "parent",
          "parent",
          {
            "relation": "parent",
            "maxHops": 3
          }
          ],
          "fromBlueprint": "Team"
        },
      "operator": "matchAny",
      "value": "targetEntity"  
    }
  ]
}
```

For example, if the `value` is `Squad`:

* First hop: `Squad` â `Tribe`.
* Second hop: `Tribe` â `Domain`.
* Third hop: `Domain` â `Group`.

Result: `Domain` (from fixed hops) and `Group` (from variable hops, up to 3 additional hops).
