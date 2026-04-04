# Source: https://docs.grit.io

## Variable Scoping

Within a pattern, all metavariables share a common scope. Once a metavariable is bound to a value, it retains this value throughout the target code. Therefore, the scope of the metavariable spans the entire target file. For instance, if your pattern matches the snippet `console.log($x)`, then according to the standard Grit scoping rules, it would only match the first occurrence of `$x` in the target file.

## Defined patterns

When you [define a pattern](/guides/patterns#pattern-definitions), it establishes a new variable scope. However, pattern parameters bridge this scope. In the following pattern, `$method` will cross the scope boundary while `$message` remains local:

grit pattern console_method_to_info($method) {
  `console.$method($message)` => `console.info($message)`
}

## bubble clause

The `bubble` clause introduces a new scope without the necessity of defining a separate pattern. Like with separate patterns, variables inside the `bubble` clause are isolated from the surrounding code.
This is particularly useful when you want to match a pattern in multiple places without requiring metavariables to hold the same value in each location.

pattern `function() { $body }` where {
  $body <: contains bubble `console.log($message)`=> `console.warn($message)`
}

Before function() {
  console.log(&#x27;Hello, world!&#x27;);
  console.log(&#x27;How are you?&#x27;);
}

After function() {
  console.warn(&#x27;Hello, world!&#x27;);
  console.warn(&#x27;How are you?&#x27;);
}

In the above pattern, the `bubble` clause ensures the metavariable `$message` is not bound to the same value in both `console.log` calls.
Absent the `bubble`, only the first `console.log` call would be rewritten. After it was rewritten, `$message` would be bound to the value `&#x27;Hello, world!&#x27;`. When attempting to match the second `console.log`, `$message` would try to bind to `&#x27;How are you?&#x27;` and fail.

### Arguments for the `bubble` clause

Like pattern definitions, the `bubble` clause can accept arguments. Such arguments are used to "pierce" the bubble by allowing metavariables to preserve the values they had outside the bubble scope. For example:

pattern `function $name() { $body }` where {
  $body <: contains bubble($name) `console.log($message)` => `console.warn($message, $name)`
}

Before function logger() {
  console.log(&#x27;Hello, world!&#x27;);
  console.log(&#x27;How are you?&#x27;);
}

After function logger() {
  console.warn(&#x27;Hello, world!&#x27;, logger);
  console.warn(&#x27;How are you?&#x27;, logger);
}

If `$name` weren&#x27;t specified as an argument for `bubble`, the metavariable `$name` would be undefined inside the bubble, leading to an error during rewriting.

## Pattern auto-wrap

Unless a root pattern targets either `file` or `body`, it is automatically wrapped to become `file(body = contains bubble $root_pattern)`. The main effect of auto-wrap is that patterns can match multiple times within a file without needing to manually specify `bubble`.

grit file(body=contains bubble $THE_PATTERN)

This default behavior often proves beneficial as it facilitates matching multiple sections within a file independently. To override this, encapsulate the pattern within `file`.
For example, if you want to transform `console.$method` calls but only for one method at a time, you can use a pattern like this:

pattern file(body = contains `console.$method` => `println`)

Before console.info(&#x27;Hello, world!&#x27;);
console.info(&#x27;How are you?&#x27;);
console.error(&#x27;Hello?&#x27;);

After println(&#x27;Hello, world!&#x27;);
println(&#x27;How are you?&#x27;);
console.error(&#x27;Hello?&#x27;);

In the pattern shown above, the metavariable `$method` consistently binds to a singular value, `info`, throughout the pattern&#x27;s application.

## Global metavariables

While these scoping rules suffice in most scenarios, there are times when you might want to share scope across a file within a defined pattern. This can be achieved using global metavariables, denoted with a `$GLOBAL_` prefix and written in uppercase.
For example, the default [import utilities](https://github.com/getgrit/stdlib/blob/main/.grit/patterns/js/imports.grit) use global metavariables to keep a running list of all imports in a file.
