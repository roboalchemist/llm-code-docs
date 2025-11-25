# Source: https://docs.hypermode.com/dgraph/graphql/lambda/query.md

# Source: https://docs.hypermode.com/dgraph/dql/query.md

# Source: https://docs.hypermode.com/dgraph/graphql/lambda/query.md

# Source: https://docs.hypermode.com/dgraph/dql/query.md

# Query Structure

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

Fetching data with Dgraph Query Language (DQL), is done through **DQL Queries**.
Adding, modifying or deleting data is done through [DQL Mutations](./mutation).

This overview explains the structure of DQL Queries and provides links to the
appropriate DQL reference documentation.

## DQL query structure

DQL is **declarative**, which means that queries return a response back in a
similar shape to the query. It gives the client app the control of what it gets:
the request return exactly what you ask for, nothing less and nothing more. In
this, DQL is similar to GraphQL from which it's inspired.

A DQL query finds nodes based on search criteria, matches patterns in the graph
and returns the node attributes, relationships specified in the query.

A DQL query has

* an optional parameterization, ie a name and a list of parameters
* an opening curly bracket
* at least one [query block](./#query-block), but can contain many blocks
* optional var blocks
* a closing curly bracket

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-1.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=82bfdaf6115cb039ad11dc63c69ef123" alt="DQL Query with parameterization" width="1962" height="722" data-path="images/dgraph/query-syntax-1.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-1.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=51a1b64f30a40654c1804c7db8ea12ec 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-1.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=d2f977ffadfa02718052b9efea5ad4f2 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-1.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=de4a2570d271e594d3d9f157c131f0a1 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-1.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=84f6a035b49be9d35e9e61e80837ce68 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-1.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9b2ff9783a636bc3e203b9e302aed8f2 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-1.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9612928145dd3a80cea05694065f01a0 2500w" data-optimize="true" data-opv="2" />

## Query parameterization

**Parameters**

* must have a name starting with a `$` symbol.
* must have a type `int`, `float`, `bool` or `string`.
* may have a default value. In the example below, `$age` has a default value of
  `95`
* may be mandatory by suffixing the type with a `!`. Mandatory parameters can't
  have a default value.

Variables can be used in the query where a string, float, int or bool value are
needed.

You can also use a variable holding `uids` by using a string variable and by
providing the value as a quoted list in square brackets:\
`query title($uidsParam: string = "[0x1, 0x2, 0x3]") { ... }`.

**Error handling** When submitting a query using parameters, Dgraph responds
with errors if

* A parameter value is not parsable to the given type.
* The query is using a parameter that is not declared.
* A mandatory parameter is not provided

The query parameterization is optional. If you don't use parameters you can omit
it and send only the query blocks.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-2.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4be5cb8a4c6694b23b930d509a367c29" alt="DQL Query without parameters" width="2086" height="594" data-path="images/dgraph/query-syntax-2.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-2.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=514c18e095fd1f194e2ca7467c29e859 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-2.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a6649c37a410fa438c6f9a046d600d08 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-2.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=c5bf3458cd1b6b42a07aa36d7ee50ffd 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-2.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=59e501f980ae603b54e387ecc943d7bb 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-2.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ca05fa046625b1aab41e0dbec6e3e56f 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/query-syntax-2.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=6b7a4dd066a3b4d660e12555c9fb83b6 2500w" data-optimize="true" data-opv="2" />

<Note>
  The current documentation is usually using example of queries without
  parameters.
</Note>

If you execute this query in our [Movies demo database](./schema#sample-schema)
you can see that Dgraph will return a JSON structure similar to the request :
<img src="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/query-syntax-3.png?fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=73ca6a86f4d839feef209af67bd66a15" alt="DQL response structure" width="1954" height="1014" data-path="images/dgraph/query-syntax-3.png" srcset="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/query-syntax-3.png?w=280&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=a01e03736a039926a531a84518e20b4e 280w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/query-syntax-3.png?w=560&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=67b84c1d491e9649fd4fa91d0450901f 560w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/query-syntax-3.png?w=840&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=7d591e596c858f40bdef3ca3ff81b949 840w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/query-syntax-3.png?w=1100&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=5219e09e40ce95571439ab98018cae76 1100w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/query-syntax-3.png?w=1650&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=1a17707bf171841828042bb37836f546 1650w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/query-syntax-3.png?w=2500&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=9d0886d57570dcb03d057bb3717e554c 2500w" data-optimize="true" data-opv="2" />

## Query block

A query block specifies information to retrieve from Dgraph.

A query block

* must have name
* must have a node criteria defined by the keyword `func:`
* may have ordering and pagination information
* may have a combination of filters (to apply to the root nodes)
* must provide the list of attributes and relationships to fetch for each node
  matching the root nodes.

Refer to [pagination](./pagination) and [ordering](./sorting) for more
information.

For each relationships to fetch, the query is using a nested block.

A nested block

* may specify filters to apply on the related nodes
* may specify criteria on the relationships attributes using
  [filtering on facets](./facets#filtering-on-facets))
* provides the list of relationship attributes ([facets](./facets))) to fetch.
* provides the list of attributes and relationships to fetch for the related
  nodes.

A nested block may contain another nested block, and such at any level.

## Multiple query blocks

Inside a single query, multiple query blocks are allowed, and each block can
have a name. Multiple query blocks are executed in parallel, and they don't need
to be related in any way.

Query Example: *"All of Angelina Jolie's films, with genres, and Peter Jackson's
films since 2008"*

```json
{
  AngelinaInfo(func: allofterms(name@en, "angelina jolie")) {
    name@en actor.film { performance.film { genre { name@en } } }
  }

  DirectorInfo(func: eq(name@en, "Peter Jackson")) {
    name@en director.film
    @filter(ge(initial_release_date, "2008")) { Release_date: initial_release_date
    Name: name@en }
  }
}
```

If queries contain some overlap in answers, the result sets are still
independent.

Query Example: *"The movies Mackenzie Crook has acted in and the movies Jack
Davenport has acted in"*

The results sets overlap because both have acted in the *Pirates of the
Caribbean* movies, but the results are independent and both contain the full
answers sets.

```json
{
  Mackenzie(func:allofterms(name@en, "Mackenzie Crook")) {
    name@en actor.film { performance.film { uid name@en } performance.character {
    name@en } }
  }

  Jack(func:allofterms(name@en, "Jack Davenport")) { name@en actor.film {
  performance.film { uid name@en } performance.character { name@en } } }
}
```

## Variable (`var`) blocks

Variable blocks (`var` blocks) start with the keyword `var` and are not returned
in the query results, but do affect the contents of query results.

Query Example: *"Angelina Jolie's movies ordered by genre"*

```json
{
  var(func:allofterms(name@en, "angelina jolie")) {
    name@en actor.film { A AS performance.film { B AS genre } }
  }

  films(func: uid(B), orderasc: name@en) { name@en ~genre @filter(uid(A)) {
  name@en }
  }
}
```

## Multiple `var` blocks

You can also use multiple `var` blocks within a single query operation. You can
use variables from one `var` block in any of the subsequent blocks, but not
within the same block.

Query Example: *"Movies containing both Angelina Jolie and Morgan Freeman sorted
by name"*

```json
{
  var(func:allofterms(name@en, "angelina jolie")) {
    name@en actor.film { A AS performance.film }
  }

  var(func:allofterms(name@en, "morgan freeman")) {
    name@en actor.film { B as performance.film @filter(uid(A)) }
  }

  films(func: uid(B), orderasc: name@en) {
    name@en
  }
}
```

### Combining multiple `var` blocks

You could get the same query results by logically combining both `var` blocks in
the films block, as follows:

```json
{
  var(func:allofterms(name@en, "angelina jolie")) {
    name@en actor.film { A AS performance.film }
  }

  var(func:allofterms(name@en, "morgan freeman")) {
    name@en actor.film { B as performance.film }
  }
  films(func: uid(A,B), orderasc: name@en) @filter(uid(A) AND uid(B)) { name@en }
}
```

The root `uid` function unions the `uid`s from `var` `A` and `B`, so you need a
filter to intersect the `uid`s from `var` `A` and `B`.

### Escape characters in predicate names

If your predicate has special characters, wrap it with angular brackets `< >` in
the query.

E.g. `<https://myschema.org#name>  `

### Formatting options

Dgraph returns the attributes and relationships that you specified in the query.
You can specify an alternate name for the result by using \[

You can flatten the response structure at any level using
[@normalize](./normalize) directive.

Entering the list of all the attributes you want to fetch could be fastidious
for large queries or repeating blocks : you may take advantage of
[fragments](./fragment) and the [expand function](./expand).

### Node criteria (used by root function or by filter)

Root criteria and filters are using [functions](./functions) applied to nodes
attributes or variables.

Dgraph offers functions for

* testing string attributes
  * term matching : [allofterms](./functions#allofterms),
    [anyofterms](./functions#anyofterms)
  * regular Expression : [regexp](./functions#regular-expressions)
  * fuzzy match : [match](./functions#fuzzy-matching)
  * full-text search : [alloftext](./functions#full-text-search)
* testing attribute value
  * equality : [eq](./functions#equal-to)
  * inequalities :
    [le,lt,ge,gt](./functions#less-than-less-than-or-equal-to-greater-than-and-greater-than-or-equal-to)
  * range : [between](./functions#between)
* testing if a node
  * has a particular predicate (an attribute or a relation) :
    [has](./functions#has)
  * has a given UID : `[uid]`(./functions#uid)
  * has a relationship to a given node : [uid\_in](./functions#uid_in)
  * is of a given type : type()
* testing the number of node relationships
  * equality : [eq](./functions#equal-to)
  * inequalities :
    [le,lt,ge,gt](./functions#less-than-less-than-or-equal-to-greater-than-and-greater-than-or-equal-to)
* testing geolocation attributes
  * if geo location is within distance : [near](./functions#near)
  * if geo location lies within a given area : [within](./functions#within)
  * if geo area contains a given location : [contains](./functions#contains)
  * if geo area intersects a given are : [intersects](./functions#intersects)

### Variable (`var`) block

Variable blocks (`var` blocks) start with the keyword `var` instead of a block
name.

var blocks are not reflected in the query result. They are used to compute
[query-variables](./variables#query-variables) which are lists of node UIDs, or
[value-variables](./variables#value-variables) which are maps from node UIDs to
the corresponding scalar values.

Note that query-variables and value-variables can also be computed in query
blocks. In that case, the query block is used to fetch and return data, and to
define some variables which must be used in other blocks of the same query.

Variables may be used as functions parameters in filters or root criteria in
other blocks.

### Summarizing functions

When dealing with array attributes or with relationships to many node, the query
may use summary functions [count](./count) , [min](./aggregation#min),
[max](./aggregation#max), [avg](./aggregation#sum-and-avg) or
[sum](./aggregation#sum-and-avg).

The query may also contain
[mathematical functions](./variables#math-on-value-variables) on value
variables.

Summary functions can be used in conjunction with [@grouby](./groupby) directive
to create aggregated value variables.

The query may contain **anonymous block** to return computed values. **Anonymous
block** don't have a root criteria as they are not used to search for nodes but
only to returned computed values.

### Graph traversal

When you specify nested blocks and filters you basically describe a way to
traverse the graph.

[@recurse](./recurse) and [@ignorereflex](./ignorereflex) are directives used to
optionally configure the graph traversal.

### Pattern matching

Queries with nested blocks with filters may be turned into pattern matching
using [@cascade](./cascade) directive : nodes that don’t have all attributes and
all relationships specified in the query at any sub level are not considered in
the result. So only nodes "matching" the complete query structure are returned.

### Graph algorithms

The query can ask for the shortest path between a source (from) node and
destination (to) node using the [shortest](./shortest) query block.

### Comments

Anything on a line following a `#` is a comment

```
```
