# Source: https://www.apollographql.com/docs/graphos/connectors/mapping/enums.md

# Mapping Enums

When working with REST APIs, you often encounter string values representing states, statuses, or categories that should be represented as enums in your GraphQL schema. Apollo Connectors provides tools for normalizing these values to match your GraphQL enum types, ensuring consistency and type safety.

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.

## Common use cases

Enum mapping is particularly valuable in these scenarios:

* Converting lowercase or mixed-case status values (for example, `"active"` and `"Active"`) to uppercase GraphQL enums (for example, `ACTIVE`)
* Standardizing variations of the same value (for example, `"in_progress"`, `"in progress"`, and `"inProgress"`) to a single enum value
* Transforming numeric codes (for example, `1`, `2`, `3`) into semantic enum values (for example, `PENDING`, `APPROVED`, `REJECTED`)
* Handling internationalized or legacy values by mapping them to a consistent set of enums

## Matching enum values

The example below uses the `->match` method to transform `status` values from `active` to `ACTIVE` and `not active` to `INACTIVE`.

```connectors title=Selection mapping snippet
status: status->match(
  ["active", "ACTIVE"],
  ["not active", "INACTIVE"],
  [@, "UNKNOWN"] # fallback — the value always matches `@`
)
```

The `->match` method evaluates patterns sequentially and returns the first matching value.
Order matters; place more specific patterns before general ones, and use the catch-all pattern (`@`) last.

Using the above transformation on the following response data yields the following results:

```json title=Response data
{
  "status": "active"
}
```

```json title=Result
{
  "status": "ACTIVE"
}
```

```json title=Response data
{
  "status": "none of the above"
}
```

```json title=Result
{
  "status": "UNKNOWN"
}
```

If a match isn't found, the result will be omitted and the field will be `null` if nullable or result in a validation error if non-nullable. If you want to avoid this, you can use the [`@` variable](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#-1) to provide a fallback, as shown in the example above.

## Mapping arrays of string values

When mapping arrays of strings to lists of enum values, you can use the `->map()` method combined with `->match()`:

```connectors
categories: categories->map({
  @->match(
    ["fashion", "FASHION"],
    ["electronics", "ELECTRONICS"],
    ["home", "HOME"],
    [@, "OTHER"]
  )
})
```

This transforms an array like `["fashion", "home", "unknown"]` into `["FASHION", "HOME", "OTHER"]`.

## Additional resources

* Learn more about GraphQL enum types in the [official GraphQL documentation](https://graphql.org/learn/schema/#enumeration-types)
* Explore other transformation methods in the [methods reference](https://www.apollographql.com/docs/graphos/connectors/reference/mapping/methods)
