# Source: https://www.apollographql.com/docs/graphos/connectors/mapping/literals.md

# Using Literal Values

Use literal values to enhance your graph with data that doesn't come directly from your REST API responses.
Using literal values, you can add constants and create new data structures to complement the data from your APIs.

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.

## Common use cases for literal values

Literal values serve several important purposes in GraphQL schema mapping:

* **Adding metadata**: Append version numbers, timestamps, or source information to your GraphQL responses
* **Standardizing formats**: Transform inconsistent response formats into a consistent structure

## Using literal values

You can use literal values with `$()` like so:

```connectorsExample title=Literal values
body: """
  hello: $("world")
  theAnswer: $(42)
  isTrue: $(true)
  anObject: $({ key: "value" })
  aList: $([1, 2, 3])
"""
```

To avoid using the `$()` wrapper repeatedly, you can wrap an entire object with `$()`:

```connectorsExample title=Literal values, again
body: """
  $({
    hello: "world",
    theAnswer: 42,
    isTrue: true,
    anObject: { key: "value" },
    aList: [1, 2, 3],
  })
"""
```

Inside the `$()`expression, you can use any JSON literal: numbers, strings, booleans, arrays, objects, and `null`.

Commas are required between the properties of the object literal.

## Combining literal values with API data

You can seamlessly combine literal values with data from your API response:

```connectorsExample
selection: """
  id
  name
  metadata: $({
    source: "product-api",
    version: "1.0",
    features: ["search", "filter", "sort"]
  })
"""
```

This creates a response with both API-sourced data (`id` and `name`) and literal values (`metadata`).

## Variables in literals

You can use [variables](https://www.apollographql.com/docs/graphos/connectors/reference/mapping/variables), like `$args` and `$this`, in literal values.

```connectorsExample title=Expressions in literals
selection: """
  names: $([             # a list field like `names: [String]`
    $args.input.name,    # a variable
    results->first.name  # a selection
  ])
"""
```

Given the following inputs for the example above:

```json title=Variables
{
  "$args": {
    "input": {
      "name": "Alice"
    }
  }
}
```

```json title=Response
{
  "results": [
    { "name": "Bob" }
    { "name": "Charlie" }
  ]
}
```

The selection mapping results in:

```json title=Result
{ "names": ["Alice", "Bob"] }
```

## Using literals with `@connect`

The following rules apply when using literal values with the `@connect` directive:

1. All literal values in the `body` argument are always allowed.
2. Scalar literal values (strings, numbers, booleans) and lists of scalars are allowed in the `selection` argument.
3. Literal values can't be mapped to a field that returns a nested object or list of nested objects.
4. Literal objects and lists and lists of objects are allowed only if they're mapped to a custom scalar field.

See corresponding examples of these rules below. The number in parentheses, for example, `(1)` on line 6 shows an example of rule 1.

```graphql
type Mutation {
  createPost(input: CreatePostInput!): PostPayload
    @connect(
      http: {
        POST: "https://api.example.com/posts"
        body: "$({ id: 1, title: "Hello, world!" })" # ✅ (1)
      }
      selection: """
      success: $(true) # ✅ (2)
      post: $({ id: 1, title: "Hello, world!" }) # ❌ (3)
      metadata: $({ key: "value" }) # ✅ (4)
      """
    )

type PostPayload {
  success: Boolean
  post: Post # ⚠️ Object type
  metadata: JSON
}

scalar JSON
```

## Differentiating between `null` and a missing value (`None`)

Because the connectors mapping language assumes JSON-compatible data, and `null`
is a JSON value, you often encounter `null` when building connectors, and you
can obtain a `null` literal value using `$(null)`.

Many APIs use `null` to indicate the absence of a value, or perhaps a value that
encountered an error during computation, but `null` can also be used as
meaningful data in other contexts, and it's not always safe to provide `null`
where a value or property was expected to be missing, because `null` is not
synonymous with absence.

To address this distinction, the connectors mapping language has a `None`
"value" (representing the absence of a value) that can be generated when a value
might be missing, or fails to evaluate, accompanied by a runtime error
explaining the failure.

Whenever a `None` value is generated during execution, the current path
immediately stops executing and evaluates to `None`. If the `None` was
unexpected, a runtime error should have been reported. If the `None` was
expected or tolerable, you can use the `?` notation to silence errors related to
a particular `None` value.

The `?` operator interprets both `null` and `None`/missing values as if they
were `None`, so both `null` and `None` can short-circuit path evaluation early
if `?` is applied to them, instead of propagating the `null` as data to the rest
of the path.

Whenever any `->` method receives an input value of `None` or any argument
evaluates to `None`, the entire method evaluates to `None`, terminating further
path execution. By comparison, `null` is a valid input/argument for methods and
does not prevent their execution.

When an object property value computes to `None`, the property is omitted from
the object. Due to limitations of JSON arrays, array elements cannot be
omitted/missing, so when the `@.key` in `array->map(@.key)` evaluates to `None`,
that array element becomes `null` to avoid shifting the indices of the array by
skipping elements. This is the only case where `null` is implied to be a
substitute for `None`.

## Defaulting values with `$(... ?? default)` and `$(... ?! default)`

The `?` optional chaining operator provides a mechanism for tolerating the
absence of certain JSON properties or values, controlling what happens when
values are present or not. This is a useful capability, but it does not cover
all scenarios involving missing and nullable values.

When a property is missing, as `hobbies` might be in `id name hobbies? { kind }`,
it is currently omitted from the output. However, depending on your needs,
you might want to provide a default value, instead of omitting the property. The
new `??` and `?!` operators let you specify default values for missing or `null`
values, as in the following examples:

```connectors
id
name
hobbies: $(hobbies ?? []) { kind frequency }
hobbyKinds: $(hobbies ?! [{ kind: "other" }]).kind
personOrNull: $(person ?! null)
a_b_c_or_null: $(a ?? b ?? c ?? null)
safeSlice: $args.input->slice($args.offset ?? 0, $args.maxLength ?? 100)
```

The `??` operator is inspired by the [Nullish Coalescing
Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator)
in ECMAScript/TS/JS, and the `?!` is a slightly stricter version that isn't
found in those languages but serves a similar purpose.

The `$(hobbies ?? [])` expression provides a default empty array for a field
(`hobbies`) that might be missing or `null`. Note also that `$(hobbies ?? [])`
works the same as `$(hobbies? ?? [])`, so you don’t need the single `?` in
`hobbies?` when you’re using `??`.

The `??` and `?!` operators often require the `$(...)` wrapper to enable
expression parsing (when in selection parsing mode), but `$(...)` can be omitted
when the expression is passed as an argument to a `->` method, like
`$args.offset ?? 0` in the `safeSlice: $args.input->slice($args.offset ?? 0,
...)` example, because method arguments are always parsed as expressions.

The difference between `??` and `?!` is that `??` rejects both missing and
`null` inputs on its left-hand side, whereas `?!` only rejects missing inputs,
letting `null` through as a valid input. When working with nullable values in
GraphQL, `??` is the operator you'll use most often, but `?!` can be useful in
cases where `null` represents data rather than its absence.

As you can see from the `$(hobbies ?! [{ kind: "other" }]).kind` example, the
default expression can be anything, and is lazily evaluated only when needed.

### Chaining multiple (>2) operands

You can also chain multiple expressions together, as in `$(a ?? b ?? null)`. If
both the `a` and `b` expressions fail to evaluate (are missing or produce
`None`), then the `$(... ?? null)` expression falls back to the infallible
`null`. If that final expression fails too (impossible here), then the whole
`$(...)` expression behaves like the final failed expression.

The parser currently forbids mixing `??` and `?!` in the same chain,
but you can break them up with `$(...)` grouping:

```connectors
$(a ?? b ?! c) # error
$(a ?? $(b ?! c)) # ok
$($(a ?? b) ?! c) # ok
```

Many languages require you to learn fixed precedence rules for parsing mixed
infix operators like `??` and `?!`, but the connectors mapping language hasn't
made any commitments regarding operator precedence so far. For now, you can
achieve any grouping you want, but you must control the grouping explicitly with
`$(...)` when you’re mixing different operators.

## Additional resources

* Refer to the [mapping language reference](https://www.apollographql.com/docs/graphos/connectors/mapping) for a complete overview of mapping syntax and usage
* See the [variables reference](https://www.apollographql.com/docs/graphos/connectors/reference/mapping/variables) to see which variables you can use with literals
* See [methods reference](https://www.apollographql.com/docs/graphos/connectors/reference/mapping/methods) for examples of more complex data manipulation
