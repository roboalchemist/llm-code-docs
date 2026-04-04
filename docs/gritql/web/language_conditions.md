# Source: https://docs.grit.io

## Conditional Operators

`where` clauseThe `where` clause introduces one or more conditions that must be true for the pattern preceding it to execute.

pattern `console.log($message)` => . where $message <: js"&#x27;Hello, world!&#x27;"

Before console.log(&#x27;Hi&#x27;);
console.log(&#x27;Hello, world!&#x27;);

After console.log(&#x27;Hi&#x27;);

The `where` clause can be followed by either a single condition or a list of conditions, wrapped in braces and separated by commas (`{ cond1, cond2 }`). If a `where` clause contains multiple conditions, all must be true for the pattern to match.

Match (`<:`) conditionGrit&#x27;s most common condition, the match operator `<:` specifies what part of the codebase you want to target. It does this by matching a [metavariable](/language/patterns#metavariables) to its left against a pattern to its right.

grit `console.log(&#x27;$message&#x27;)` where $message <: `Hello, world!`

`!` condition

The `!` operator is used to negate a condition.

pattern `console.log(&#x27;$message&#x27;);` => `console.warn(&#x27;$message&#x27;);` where {
  ! $message <: "Hello, world!"
}

Before console.log(&#x27;Hello, world!&#x27;);
console.log(&#x27;Hello, people!&#x27;);

After console.log(&#x27;Hello, world!&#x27;);
console.warn(&#x27;Hello, people!&#x27;);

`!` is similar to [the `not` modifier](/language/modifiers#not-clause), except it applies to the entire condition, rather than the pattern within the condition. For example, `! $message <: "Hello, world!"` is equivalent to `$message <: not "Hello, world!"`.

`and` condition

The `and` operator is true if all of the conditions are true. Note that the `and` in the following example is redundant, as the `where` clause already requires all conditions to be true.

pattern `console.$method(&#x27;$message&#x27;);` => `console.warn(&#x27;$message&#x27;);` where {
  and {
    $message <: r"Hello, .*!",
    $method <: `log`
  }
}

Before console.log(&#x27;Hello, world!&#x27;);
console.error(&#x27;Hello, world!&#x27;);

After console.warn(&#x27;Hello, world!&#x27;);
console.error(&#x27;Hello, world!&#x27;);

`or` condition

The `or` operator is true if any of the conditions are true.

pattern `console.$method(&#x27;$message&#x27;);` => `console.warn(&#x27;$message&#x27;);` where {
  or {
    $message <: "Hello, world!",
    $method <: `error`
  }
}

Before console.log(&#x27;Hello, world!&#x27;);
console.error(&#x27;Hello, people!&#x27;);
console.info(&#x27;Hello, people!&#x27;);

After console.warn(&#x27;Hello, world!&#x27;);
console.warn(&#x27;Hello, people!&#x27;);
console.info(&#x27;Hello, people!&#x27;);

`if` as a condition

The `if` clause can be used to add a condition only if another condition is true.

pattern `$method(&#x27;$message&#x27;)` where {
  if ($message <: r"Hello, .*!") {
    $method => `console.info`
  } else {
    $method => `console.warn`
  }
}

Before console.log(&#x27;Hello, world!&#x27;);
console.log(&#x27;Hello, people!&#x27;);
console.log(&#x27;Hi!&#x27;);

After console.info(&#x27;Hello, world!&#x27;);
console.info(&#x27;Hello, people!&#x27;);
console.warn(&#x27;Hi!&#x27;);

Rewrite (`=>`) as conditionRewrites can also be used within conditions. The syntax is the same as for rewrites, but the left-hand side of the rewrite **must** be a metavariable.

The rewrite will be applied to the code locations referenced by the metavariable, and the condition will match if the rewrite succeeds for all locations.

pattern `console.log(&#x27;$message&#x27;)` where $message => `Hello, world!`

Before console.log(&#x27;Hello?&#x27;);

After console.log(&#x27;Hello, world!&#x27;);

Assignment `=`

The assignment operator `=` is used to assign a value to a metavariable, much in the same way as you would assign to a variable in other programming languages.

The value can be anything that can appear on the right-hand side of a rewrite.

An assignment can appear inside a where clause, and always succeeds.

grit `console.log($message)` as $log where {
  $new_log_call = `logger.log($message)`,
  $log => $new_log_call
}
