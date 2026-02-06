# Source: https://docs.grit.io

# Pattern Modifiers

Various modifiers can be applied to patterns to transform how they are matched. All pattern modifiers yield a new pattern with the modified behavior. Importantly, none of these modifiers represent base patterns by themselves, but instead modify or combine other patterns.
`and` clause`and` clauses are used to combine one or more comma-separated patterns.
The `and` clause matches only if all of the patterns match.
In the example below, we combine [the `where` clause](/language/conditions#where-clause) with `and` to rewrite two types of React hooks in one pattern.
pattern arrow_function($body) where $body <: and {
  contains js"React.useState" => js"useState",
  contains js"React.useMemo" => js"useMemo",
}Before const someComponent = () => {
  const [count, setCount] = React.useState(0);
};

const anotherComponent = () => {
  const [count, setCount] = React.useState(0);
  const math = React.useMemo(() => count + 5, [count]);
};After const someComponent = () => {
  const [count, setCount] = React.useState(0);
};

const anotherComponent = () => {
  const [count, setCount] = useState(0);
  const math = useMemo(() => count + 5, [count]);
};`or` clause`or` clauses are used to match against multiple patterns. They are written using the `or` keyword, and their arguments are separated by a comma.
The `or` clause matches if any of the patterns match.
`or` is short-circuited, so the first pattern that matches will be the one that is used.
pattern arrow_function($body) where $body <: or {
  contains js"React.useState" => js"useState",
  contains js"React.useMemo" => js"useMemo",
}Before const someComponent = () => {
  const [count, setCount] = React.useState(0);
};

const anotherComponent = () => {
  const [count, setCount] = React.useState(0);
  const math = React.useMemo(() => count + 5, [count]);
};After const someComponent = () => {
  const [count, setCount] = useState(0);
};

const anotherComponent = () => {
  const [count, setCount] = useState(0);
  const math = React.useMemo(() => count + 5, [count]);
};`any` clauseThe `any` clause is a non-short-circuiting version of `or`. It will match if any of the provided patterns matches, but will continue to try to match all of the patterns and execute any applicable transformations:
pattern arrow_function($body) where $body <: any {
  contains js"React.useState" => js"useState",
  contains js"React.useMemo" => js"useMemo",
}Before const someComponent = () => {
  const [count, setCount] = React.useState(0);
};

const anotherComponent = () => {
  const [count, setCount] = React.useState(0);
  const math = React.useMemo(() => count + 5, [count]);
};After const someComponent = () => {
  const [count, setCount] = useState(0);
};

const anotherComponent = () => {
  const [count, setCount] = useState(0);
  const math = useMemo(() => count + 5, [count]);
};`not` clause`not` clauses are used to negate a pattern. They are written using the `not` keyword.
A `not` clause matches if the pattern it negates does not match.
pattern `$method($message)` => `console.warn($message)` where {
  $method <: not `console.error`
}Before console.log("Hello, world!");
console.error("Hello, world!");After console.warn("Hello, world!");
console.error("Hello, world!");`maybe` clause`maybe` clauses are used to optionally match against a pattern. If the pattern inside does not match, the `maybe` clause will still match as a whole.
pattern `throw new Error($err)` as $thrown => `throw new CustomError($err);` where {
  $err <: maybe string(fragment=$fun) => `{ message: $err }`
}Before if (Math.random() < 0.5) {
  throw new Error();
} else {
  throw new Error("nest the message in an object");
}After if (Math.random() < 0.5) {
  throw new CustomError();
} else {
  throw new CustomError({ message: "nest the message in an object" });
} **Warning**: In the pattern above, the metavariable `$fun` serves only an illustrative example and so isn&#x27;t actually used after it&#x27;s assigned. However, if we were to use it, we&#x27;d have to be careful: metavariables in `maybe` clauses are bound only if the `maybe` clause matches, and Grit will throw an error if you attempt to use one when the clause does not match.
`contains` operatorThe `contains` keyword is used to modify a pattern to match any node that contains a specific pattern by traversing downwards through the syntax tree.
grit `function ($args) { $body }` where {
  $args <: contains `x`
}In the example above, the pattern will only match functions where one of the arguments is `x`.
`until` modifierThe `until` modifier is appended to `contains` pattern is used to stop traversal within a `contains` clause.
The `contains` pattern will only traverse within the parts of the node that are not matched by the `until` pattern. When the `until` pattern is reached, traversal will not continue any deeper.
For example, the `until` here stops traversal inside `sanitized` calls:
grit `console.$_($content)` where {
  $content <: contains `secret` until `sanitized($_)`
}javascript console.log(secret);
console.log(sanitized(secret));
console.log(random(secret));
console.log(other + sanitized(secret));
console.log(random(secret) + sanitized(secret));`as` modifier`as` can be used to assign a matched snippet to a metavariable. This is often useful when you want to perform some change on a section of code as a whole while also making more granular changes within that section. For example:
pattern engine marzano(0.1)
language js

`function $name ($args) { $body }` as $func where {
  $func => `const $name = ($args) => { $body }`,
  $args <: contains `apple` => `mango`
}Before function fruits(apple, pear) {
  console.log("fruits");
}After const fruits = (mango, pear) => {
  console.log("fruits");
};`within` clause`within` restricts the pattern to only match if the target node appears within code matching another pattern.
For example, the pattern below only matches the second console.log, as it appears within the if block.
grit `console.log($arg)` where {
  $arg <: within `if (DEBUG) { $_ }`
}typescript console.log(&#x27;Hello, world!&#x27;);
if (DEBUG) {
  console.log(&#x27;Hello, world!&#x27;);
}`after` clause`after` clauses are used to restrict the pattern to only match if the target node is directly after a node matching a specific pattern. They are written using the `after` keyword.
grit `console.warn($_)` as $warn where {
  $warn <: after `console.log($_)`
}`after` can also be used to *retrieve* the node that comes after the target node.
pattern `const $x = 5` as $const where {
  $next = after $const
} += `// Next: $next`Before const x = 5;
const nine = 10;After const x = 5; // Next: const nine = 10;
const nine = 10;`before` clause`before` clauses are used to restrict the pattern to only match if the target node is directly before a node matching a specific pattern. They are written using the `before` keyword.
grit `console.warn($_)` as $warn where {
  $warn <: before `console.log($_)`
}`before` can also be used to *retrieve* the node that comes before the target node.
pattern `const $_ = 10` as $const where {
  $next = before $const,
  $next <: `const $name = $_`
} += `// Comes after $name`Before const x = 5;
const nine = 10;After const x = 5;
const nine = 10; // Comes after x`some` clauseThe `some` clause can be used to match a metavariable which represents a list against a pattern which represents some element of that list. The list can be any ordered set of syntax tree nodes, for example, a list of statements.
As long as one of the nodes matches the pattern, the `some` clause will match.
pattern `var $x = [$names]` => `var coolPeople = [$names]` where {
  $names <: some { `"andrew"` }
}Before var people = ["alex", "andrew", "susan"];
var peopleTwo = ["beth", "max", "right"];After var coolPeople = ["alex", "andrew", "susan"];
var peopleTwo = ["beth", "max", "right"]; - - **Tip**: If you would like the `some` clause to succeed even if no match is found, prefix it with `maybe`. Ex. `$names <: maybe some { `"andrew"` }`
`every` clauseThe `every` clause can be used to match a pattern against every element of a list. It matches only if all elements of the list match the pattern.
pattern `var $x = [$names]` => `var coolPeople = [$names]` where {
  $names <: every or {`"andrew"`, `"alex"`}
}Before var people = ["alex", "andrew", "alex"];
var peopleTwo = ["alex", "max", "right"];
var nobody = ["sam", "susan"];After var coolPeople = ["alex", "andrew", "susan"];
var peopleTwo = ["alex", "max", "right"];
var nobody = ["sam", "susan"]; - - **Tip**: `every` is short-circuited, so the first element that does not match will cause the `every` clause to fail.
[
## List patterns
](https://docs.grit.io/language/modifiers#list-patterns)List patterns are used to match against a list of terms. They are written using the `[]` syntax.
The list pattern matches if all of the terms in the list match in order.
pattern `var $x = [$numbers]` => `var firstPrimes = [$numbers]` where {
  $numbers <: [ `2`, `3`, `5` ]
}Before var someNumbers = [2, 3, 5];After var firstPrimes = [2, 3, 5];`...` clauseThe `...` clause is used to match against a sublist of a list, ignoring the `...` elements.
pattern `var $x = [$numbers]` => `var firstPrimes = [$numbers]` where {
  $numbers <: [ `2`, `3`, ..., `11` ]
}Before var someNumbers = [2, 3, 5, 7, 11];After var firstPrimes = [2, 3, 5, 7, 11];`limit` clauseThe `limit` clause can be added after any root pattern to limit the number of matches that are returned.
Limits can only be defined in the root query and are enforced globally across all files queried.
pattern `console.$method($message)` => `console.warn($message)` where {
  $method <: not `error`
} limit 2 // Only find 2 filesBefore // @filename: file.tsx
console.log("Hello, world!");
console.log("Hello, world 2!");

// @filename: file2
console.log("This is another file");

// @filename: file3
console.log("This is a third file");After // @filename: file.tsx
console.warn("Hello, world!");
console.warn("Hello, world 2!");

// @filename: file2
console.warn("This is another file");

// @filename: file3
console.log("This is a third file"); - - **Note**: The `limit` is moved to apply to the *file* as part of [pattern auto-wrapping](/language/bubble#pattern-auto-wrap). If you use `sequential` or `multifile` patterns, you will need to be careful to place the `limit` clause in the desired location.
When running a `limit` query through the studio, paid customers can configure Grit to [automatically generate a new PR](/workflows/sequence) whenever the previous PR is merged.