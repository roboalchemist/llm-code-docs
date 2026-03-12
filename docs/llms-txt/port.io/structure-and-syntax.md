# Source: https://docs.port.io/search-and-query/structure-and-syntax.md

# Structure & syntax

This page details the structure and syntax used to build search queries in Port, including how to construct search requests, define rules, use combinators, and apply operators to filter entities.

## Search request[â](#search-request "Direct link to Search request")

A search request contains filters and rules to find matching [entities]() in your software catalog.<br /><!-- -->To search for entities using the API, see the [search](/api-reference/search-a-blueprints-entities.md) route.

A search request is comprised of the following elements:

| Field        | Description                                                |
| ------------ | ---------------------------------------------------------- |
| `combinator` | Defines the logical operation to apply to the query rules. |
| `rules`      | An array of search rules to filter results with.           |

For example:

```
{
  "combinator": "and",
  "rules": [
    {
      "property": "$blueprint",
      "operator": "=",
      "value": "myBlueprint"
    },
    {
      "property": "$identifier",
      "operator": "contains",
      "value": "myIdentifierPart"
    }
  ]
}
```

The query above searches for all entities based on the `myBlueprint` blueprint whose `identifier` contains the string `myIdentifierPart`.

## Combinator[â](#combinator "Direct link to Combinator")

There are two available combinators:

* `and` - will apply a logical AND operation between all rules, requiring all of them to satisfy for a given asset in order to return it.
* `or` - will apply a logical OR operation between all rules, requiring at least one of them to satisfy for a given asset in order to return it.

single rule queries

If you only have a single rule in your query, the combinator has no effect. But keep in mind that it still needs to be included to adhere to the query structure.

**Single rule query example (click to expand)**

In the following example, only a single rule appears in the `rules` array, so the `combinator` field has no effect:

```
{
  "combinator": "and",
  "rules": [
    {
      "property": "$blueprint",
      "operator": "=",
      "value": "myBlueprint"
    }
  ]
}
```

* And
* Or

```
{
  "combinator": "and",
  "rules": [
    {
      "property": "$blueprint",
      "operator": "=",
      "value": "myBlueprint"
    },
    {
      "property": "$identifier",
      "operator": "contains",
      "value": "myIdentifierPart"
    }
  ]
}
```

```
{
  "combinator": "or",
  "rules": [
    {
      "property": "$blueprint",
      "operator": "=",
      "value": "myBlueprint"
    },
    {
      "property": "$identifier",
      "operator": "contains",
      "value": "myIdentifierPart"
    }
  ]
}
```

## Rules[â](#rules "Direct link to Rules")

A search rule is a small filtering unit, used to control the search output.

Here is an example search rule:

```
{
  "property": "$blueprint",
  "operator": "=",
  "value": "microservice"
}
```

Port has 2 types of search rule operators:

1. Comparison (e.g. `=`, `>`).
2. Relation (e.g. `relatedTo`).

### Comparison operators[â](#comparison-operators "Direct link to Comparison operators")

#### Structure[â](#structure "Direct link to Structure")

| Field      | Description                                                                                                                                                                                                                                                                                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `operator` | Search operator to use when evaluating this rule, see a list of available operators below                                                                                                                                                                                                                                                                                                  |
| `property` | Property to filter by according to its value. It can be a [meta-property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md) such as `$identifier`, or one of the [standard properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#available-properties) |
| `value`    | The value to filter by                                                                                                                                                                                                                                                                                                                                                                     |

#### Operators[â](#operators "Direct link to Operators")

A wide variety of operators are available, see them [here](/search-and-query/operators/comparison-operators.md).

***

### Relation operators[â](#relation-operators "Direct link to Relation operators")

Several relation-based operators are available, see them [here](/search-and-query/operators/relation-operators.md).

### Contextual query rules[â](#contextual-query-rules "Direct link to Contextual query rules")

To implement specific and/or complex queries, you can add the context of the triggering user to a query rule, allowing you to access that user's properties and/or owning teams.<br /><!-- -->You can mix contextual query rules freely with other rules as part of your queries. This can be used in either the `property` or `value` key in a query rule:

* Property
* Value

```
{
   ...other rule keys
   "property": {
      "context": "user" | "userTeams",
      "property": "prop"
  }
}
```

```
{
  ...other rule keys
   "value": {
      "context": "user" | "userTeams",
      "property": "prop"
  }
}
```

#### Available contexts[â](#available-contexts "Direct link to Available contexts")

| Context     | Description                                                       |
| ----------- | ----------------------------------------------------------------- |
| `user`      | The entity of the user triggering the query                       |
| `userTeams` | The entities of the owning teams of the user triggering the query |

#### Usage examples[â](#usage-examples "Direct link to Usage examples")

![](/img/entities-search/contextual-search-rules.png)

The following rule will result in the entities owned by any one of the user's teams:

```
[ 
  ...other rules
  { 
    "property": "$team",
    "operator": "containsAny",
    "value": {
      "context": "userTeams",
      "property": "$identifier"
    }
  }
]
```

The following rule will result in entities with the same department as the user's:

```
[ 
  ...other rules
  { 
    "property": "department",
    "operator": "=",
    "value": {
      "context": "user",
      "property": "department"
    }
  }
]
```

The following rule asserts that only users with `manager` role will get the resulting entities:

```
[ 
  ...other rules
  { 
    "property": {
      "context": "user",
      "property": "company_role"
    },
    "operator": "=",
    "value": "manager"
  }
]
```

The following rule asserts that only users in the user's team/s will get the resulting entities:

```
[
  ...other rules
  { 
    "property": {
      "context": "userTeams",
      "property": "$identifier"
    },
    "operator": "containsAny",
    "value": ["Spider Team", "Builder Team"]
  }
]
```

For examples of using contextual values with relation path filters, see [filter with contextual values](/search-and-query/operators/relation-operators.md#filter-with-contextual-values).

### Filter by relations/scorecards[â](#filter-by-relationsscorecards "Direct link to Filter by relations/scorecards")

When using the [search a blueprint's entities](/api-reference/search-a-blueprints-entities.md) API route, you can also filter results by [relations]() or [scorecards]().

See the following examples for each filter type:

* Relation
* Scorecard
* Scorecard rule

```
{
  "relation": "relationId",
  "operator": "=",
  "value": "value"
}
```

```
{
  "scorecard": "scorecardId",
  "operator": "=",
  "value": "Bronze"
}
```

```
{
  "scorecard": "scorecardId",
  "scorecardRule": "scorecardRuleId",
  "operator": "=",
  "value": "Bronze"
}
```

### Dynamic properties[â](#dynamic-properties "Direct link to Dynamic properties")

Deprecation Notice

Dynamic properties are deprecated and will be discontinued soon, please use [contextual query rules](#contextual-query-rules) instead.

When using Port's UI, you can use properties of the logged-in user when writing rules by using the following functions:

* `getUserTeams` - a list of the teams the user belongs to.
* `getUserEmail` - the user's email.
* `getUserFullName` - the user's full name.
* `blueprint` - the blueprint identifier of the current page.

UI only

Since we don't have context of the logged-in user when using the API, these functions are only available when using the UI. This is useful when creating [chart/table widgets](/customize-pages-dashboards-and-plugins/dashboards/custom-widgets.md#chart-filters) and [catalog pages](/customize-pages-dashboards-and-plugins/page/catalog-page.md#page-creation).

Several relation-based operators are available, see them [here](/search-and-query/operators/relation-operators.md).

#### Usage examples[â](#usage-examples-1 "Direct link to Usage examples")

```
[
  {
    "property": "$team",
    "operator": "containsAny",
    "value": ["{{getUserTeams()}}"]
  }
]
```

```
[
  {
    "property": "emails",
    "operator": "contains",
    "value": "{{getUserEmail()}}"
  }
]
```

```
[
  {
    "property": "name",
    "operator": "=",
    "value": "{{getUserFullName()}}"
  }
]
```

```
[
  {
    "property": "$blueprint",
    "operator": "=",
    "value": "{{blueprint}}"
  }
]
```
