# Source: https://docs.grit.io

- - **Note**: You do not need to learn GritQL to use Grit. New users should start with one of our many [built-in migrations](https://docs.grit.io/patterns).

GritQL is a query language designed for searching and modifying *source code*, with semantics similar to SQL or other declarative query languages.
[

## Patterns

](https://docs.grit.io/tutorials/gritql#patterns)The root of every GritQL query is a *pattern* to search for in a codebase. If you know JavaScript, you already know GritQL: any valid JavaScript code snippet is a valid GritQL pattern if you surround it with backticks.
For example, this query will find everywhere we log "Hello world!" in our codebase:
 `console.log("Hello world!")`Click the "Run Pattern" button to run the query on a sample file. Notice how it is able to find the cases where the call is split across multiple lines or uses single quotes instead of double quotes, but it ignores the comment.
This is because GritQL is designed to do *structural* matching, not just string matching. Every code snippet is automatically converted into a [syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) before it is matched against the codebase.
 **Warning**: The downside of structural matching is that each code snippet must be valid JavaScript. If you want to match arbitrary strings, you can use quotes instead: `"console.log("`
[

## Metavariables

](https://docs.grit.io/tutorials/gritql#metavariables)In many cases, you will want to match a pattern that is *similar* to a specific code snippet, but not exactly the same. To do this, just replace the parts you want to match with a *metavariable*: any identifier that starts with a dollar sign (`$`).
For example, this query will find all console.log calls regardless of what message they are logging:
 `console.log($my_message)`You can name metavariables anything you want, but we recommend using descriptive names that make it easy to understand what the metavariable represents.
[

## Rewrites

](https://docs.grit.io/tutorials/gritql#rewrites)GritQL is useful for searching, but the real power comes from its ability to rewrite code. To convert a query into a rewrite, just add a `=>` followed by a code snippet you want to replace it with.
For example: this query will find all console.log calls and replace them with the [Winston logging](https://github.com/winstonjs/winston) library:
 `console.log($my_message)` => `winston.info($my_message)`Notice how you can use metavariables in the replacement code snippet to refer to the parts of the original code snippet you want to keep.
[

## Conditions

](https://docs.grit.io/tutorials/gritql#conditions)Simple queries are often enough to get the job done, but you can add a `where` clause to filter the results. The `where` clause is similar to the `where` clause in SQL and introduces a set of side conditions that must **all** be true for the query to match.
The most common condition uses the `<:` match operator to check if a given metavariable matches another pattern.
For example, we could use a side query to turn our user-facing console.log call into an `alert` instead:
 `console.log($my_message)` => `alert($my_message)` where {
  $my_message <: `"This is a user-facing message"`
}Conditions in GritQL support all the normal [boolean operators](https://docs.grit.io/language/conditions) like `and`, `or`, or negation.
For example, you can use negation to exclude console.log calls that are user-facing from the Winston rewrite.
 `console.log($my_message)` => `winston.info($my_message)` where {
  !$my_message <: r".+user-facing.+"
}[

## Alternative patterns

](https://docs.grit.io/tutorials/gritql#alternative-patterns)Notice how in the last example we used a regular expression to match the message instead of a code snippet.
You can also use regular expressions, string literals, and [AST nodes](/language/patterns#syntax-tree-nodes) as patterns in GritQL.
For example, you can exclude `console.log` calls that are not strings by referencing the `string()` AST node:
 `console.log($my_message)` => `winston.info($my_message)` where {
  $my_message <: string()
}[

## Compound patterns

](https://docs.grit.io/tutorials/gritql#compound-patterns)Boolean clauses can also be used to combine multiple patterns into a single pattern.
For example, `or` can be used to match either a `console.log` or `console.error` call:
 or {
  `console.log($my_message)`,
  `console.error($my_message)`
} => `winston.info($my_message)`Note that rewrites are *also* patterns, so you can use them in conditional clauses as well. This allows you to construct nested rewrites.
For example, this compound query rewrites all `console.log` calls to `winston.debug` and all `console.error` calls to `winston.warn`:
 `console.$method($my_message)` => `winston.$method($my_message)` where {
  $method <: or {
    `log` => `debug`,
    `error` => `warn`
  }
}[

## Pattern modifiers

](https://docs.grit.io/tutorials/gritql#pattern-modifiers)In clauses, you often want to match based on the *context* of a pattern, not just the pattern itself. You can use [pattern modifier keywords](https://docs.grit.io/language/modifiers) to adjust the behavior of a pattern.
For example, you can use the `within` modifier to traverse upwards through the syntax tree and match `console.log` statements only if they are inside a `try/catch` block:
 `console.log($my_message)` => `winston.error($my_message)` where {
  $my_message <: within `try { $_ } catch($_) { $_ }`
}You might have noticed the `$_` metavariable in the `within` clause. This is an anonymous metavariable that matches any pattern. It is useful when you want to include a placeholder without binding the value to a metavariable.
[

## Pattern calls

](https://docs.grit.io/tutorials/gritql#pattern-calls)When refactoring code, you often want to reuse common patterns. You can "call" a pre-defined pattern by surrounding it with parentheses. This is similar to calling a function in a programming language, and pattern calls can also take named arguments.
Grit includes a robust standard library of [built-in patterns](https://docs.grit.io/patterns) that you can use in your queries.
For example, if you want to match all JavaScript literals with a value of "42" you can call the [literal pattern](https://github.com/getgrit/stdlib/blob/main/.grit/patterns/js/util_literal.md) from the Grit standard library:
 `console.log($my_message)` => `winston.info($my_message)` where {
  $my_message <: literal(value="42")
}[

## Next steps

](https://docs.grit.io/tutorials/gritql#next-steps)This tutorial only covers the basics of GritQL. For more information, try:

- Reading the [GritQL reference](/language/overview) documentation.
- Writing your own patterns in the [GritQL studio](https://app.grit.io/studio).
- Exploring the [standard library](https://github.com/getgrit/stdlib/tree/main/.grit/patterns) to see what patterns are available.
