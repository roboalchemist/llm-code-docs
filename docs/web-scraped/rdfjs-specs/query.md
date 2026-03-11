# RDF/JS Query

**Source**: https://rdf.js.org/query-spec/

**Description**: Specification for RDF/JS Query interfaces for querying RDF graphs in JavaScript.

---

RDF/JS: Query specification


Abstract
--------

The scope of this specification is to provide a way to query over RDF quads in JavaScript, as defined in the [RDF/JS: Data model specification](http://rdf.js.org/data-model-spec/#quad-interface).
It contains high-level interfaces for libraries that want to expose querying capabilities,
and low-level interfaces for working across query engine components.

This document provides a specification of an interface for RDF query engines in a JavaScript environment.
The task force which defines this interface was formed by RDF JavaScript library developers with the wish to make existing
and future libraries interoperable. This definition strives to provide the minimal necessary
interface to enable interoperability of RDF querying libraries.

**Currently, this specification provides high-level interfaces such as `Queryable` for exposing querying capabilities,
and low-level interfaces such as `FilterableSource` for interoperability across query engines.**

Design elements and principles
------------------------------

* *All [design elements and principles from the RDF/JS data model specification](http://rdf.js.org/data-model-spec/#design-elements-and-principles) apply here as well.*
* Interfaces do not conflict with other RDF/JS interfaces, and users and implementers of purely other RDF/JS interfaces should not be aware of the interfaces in this specification if they are not needed.
* Data interfaces should not contain methods, as to enable straightforward transmission over low-level communication protocols such as Web Assembly.
* To enable querying over large graphs, interfaces should handle quads in a streaming manner, such as the [RDF/JS stream interfaces](https://rdf.js.org/stream-spec/).

SPARQL Queryable interfaces
---------------------------

This section introduces queryable interfaces that can be implemented by SPARQL-constrained query engines.
These interfaces guarantees that result objects are of the expected type as defined by the SPARQL spec,
and is often more convenient to use compared to the general queryable interfaces.

### StringSparqlQueryable interface

```
    interface StringSparqlQueryable {
      optional Promise<Stream<Bindings>> queryBindings(String query, QueryStringContext? context);
      optional Promise<Stream<Quad>> queryQuads(String query, QueryStringContext? context);
      optional Promise<boolean> queryBoolean(String query, QueryStringContext? context);
      optional Promise<void> queryVoid(String query, QueryStringContext? context);
    };
```

A `StringSparqlQueryable` can be implemented by objects that want to expose a SPARQL-constrained query execution interface
that accepts queries as a string.

queryBindings() is an optional method that asynchronously returns a [Stream](https://rdf.js.org/stream-spec/#stream-interface) of Bindings objects.
query is a query string that SHOULD be a SPARQL `SELECT` query.
context is an optional context in which query execution options can be passed.

queryQuads() is an optional method that asynchronously returns a [Stream](https://rdf.js.org/stream-spec/#stream-interface) of [Quad](http://rdf.js.org/data-model-spec/#quad-interface) objects.
query is a query string that SHOULD be a SPARQL `CONSTRUCT` or `DESCRIBE` query.
context is an optional context in which query execution options can be passed.

queryBoolean() is an optional method that asynchronously returns a `boolean`.
query is a query string that SHOULD be a SPARQL `ASK` query.
context is an optional context in which query execution options can be passed.

queryVoid() is an optional method that asynchronously returns a `void`.
query is a query string that SHOULD be a SPARQL update query.
context is an optional context in which query execution options can be passed.

### AlgebraSparqlQueryable interface

```
    interface AlgebraSparqlQueryable {
      optional Promise<Stream<Bindings>> queryBindings(Algebra query, QueryStringContext? context);
      optional Promise<Stream<Quad>> queryQuads(Algebra query, QueryStringContext? context);
      optional Promise<boolean> queryBoolean(Algebra query, QueryStringContext? context);
      optional Promise<void> queryVoid(Algebra query, QueryStringContext? context);
    };
```

An `AlgebraSparqlQueryable` can be implemented by objects that want to expose a query execution interface that accepts queries as an `Algebra` object.

queryBindings() is an optional method that asynchronously returns a [Stream](https://rdf.js.org/stream-spec/#stream-interface) of Bindings objects.
query is a query `Algebra` object that SHOULD be a SPARQL `SELECT` query.
context is an optional context in which query execution options can be passed.

queryQuads() is an optional method that asynchronously returns a [Stream](https://rdf.js.org/stream-spec/#stream-interface) of [Quad](http://rdf.js.org/data-model-spec/#quad-interface) objects.
query is a query `Algebra` object that SHOULD be a SPARQL `CONSTRUCT` or `DESCRIBE` query.
context is an optional context in which query execution options can be passed.

queryBoolean() is an optional method that asynchronously returns a `boolean`.
query is a query `Algebra` object that SHOULD be a SPARQL `ASK` query.
context is an optional context in which query execution options can be passed.

queryVoid() is an optional method that asynchronously returns a `void`.
query is a query `Algebra` object that SHOULD be a SPARQL update query.
context is an optional context in which query execution options can be passed.

Queryable interfaces
--------------------

This section introduces interfaces that can be implemented by query engines to make them expose a query execution interface.

### StringQueryable interface

```
    interface StringQueryable {
      Promise<Query> query(String query, QueryStringContext? context);
    };
```

A `StringQueryable` can be implemented by objects that want to expose a query execution interface that accepts queries as a string.

query() asynchronously returns a new Query object that can be executed later.
query is a query string.
context is an optional context in which query execution options can be passed.

### AlgebraQueryable interface

```
    interface AlgebraQueryable {
      Promise<Query> query(Algebra query, QueryAlgebraContext? context);
    };
```

An `AlgebraQueryable` can be implemented by objects that want to expose a query execution interface that accepts queries as an `Algebra` object.

query() asynchronously returns a new Query object that can be executed later.
query is a query `Algebra` object.
context is an optional context in which query execution options can be passed.

Query interfaces
----------------

This section introduces query interfaces that act as intermediary objects that represent queries that can be executed.

### Query interface

```
    interface Query {
      readonly attribute string resultType;
      Promise<any> execute(any options);
    };
```

`Query` is an abstract interface that represents a query that can be executed.

resultType represents the type of query results that will be obtained for a query's execution.
Possible values include `"bindings"`, `"quads"`, `"boolean"`, and `"void"`.

execute() asynchronously returns the query result, where the signature depends on the `resultType`.

### QueryBindings interface

```
    interface QueryBindings {
      readonly attribute string resultType;
      Promise<Stream<Bindings>> execute(QueryExecuteOptions<Variable>? options);
      Promise<QueryMetadata<Bindings>> metadata(QueryMetadataOptions? options);
    };
```

`QueryBindings` represents a query that returns a stream of Bindings, such as a SPARQL `SELECT` query.

resultType contains the constant `"bindings"`.

execute() asynchronously returns a stream of Bindings.
options is an optional argument in which execution options can be passed.

metadata() asynchronously returns a QueryMetadata object.
options is an optional argument in which desired metadata options can be passed.

### QueryQuads interface

```
    interface QueryQuads {
      readonly attribute string resultType;
      Promise<Stream<Quad>> execute(QueryExecuteOptions<("subject" or "predicate" or "object" or "graph")>? options);
      Promise<QueryMetadata<Quad>> metadata(QueryMetadataOptions? options);
    };
```

`QueryQuads` represents a query that returns a stream of [Quad](http://rdf.js.org/data-model-spec/#quad-interface)s, such as a SPARQL `CONSTRUCT` or `DESCRIBE` query.

resultType contains the constant `"quads"`.

execute() asynchronously returns a stream of [Quad](http://rdf.js.org/data-model-spec/#quad-interface)s.
options is an optional argument in which execution options can be passed.

metadata() asynchronously returns a QueryMetadata object.
options is an optional argument in which desired metadata options can be passed.

### QueryBoolean interface

```
    interface QueryBoolean {
      readonly attribute string resultType;
      Promise<boolean> execute();
    };
```

`QueryBoolean` represents a query that returns a `boolean`, such as a SPARQL `ASK` query.

resultType contains the constant `"boolean"`.

execute() asynchronously returns a `boolean`.

### QueryVoid interface

```
    interface QueryVoid {
      readonly attribute string resultType;
      Promise<void> execute();
    };
```

`QueryVoid` represents a query that returns nothing, such as a SPARQL update query.

resultType contains the constant `"void"`.

execute() asynchronously returns nothing.

### QueryExecuteOptions interface

```
    interface QueryExecuteOptions<OrderType> {
      readonly attribute Array<QueryOperationOrderTerm<OrderType>> order;
    };
```

`QueryExecuteOptions` represents the options for executing a query.

order contains the desired order of query results.

### QueryMetadataOptions interface

```
    interface QueryMetadataOptions {
      attribute ("estimate" or "exact")? cardinality;
      attribute boolean order;
      attribute boolean availableOrders;
    };
```

`QueryMetadataOptions` represents the options for requesting the metadata of a query.

cardinality indicates if an exact or estimated value for the `cardinality` metadata field should be returned.

order indicates if the `order` metadata field should be returned.

availableOrders indicates if the `availableOrders` metadata field should be returned.

Metadata interfaces
-------------------

This section introduces metadata interfaces that can contain additional information about the query execution process.

### QueryMetadata interface

```
    interface QueryMetadata<OrderType> {
      readonly attribute QueryResultCardinality? cardinality;
      readonly attribute Array<QueryOperationOrderTerm<OrderType>>? order;
      readonly attribute Array<QueryResultOrderCost<OrderType>>? availableOrders;
    };
```

`QueryMetadata` is an interface that contains side information about the query execution process.

cardinality represents the number of results of a query.

order represents the order of results in the query result.

availableOrders is an array of alternative orders that may be requested when executing a query.

### QueryResultCardinality interface

```
    interface QueryResultCardinality {
      attribute ("estimate" or "exact") type;
      attribute unsigned long value;
    };
```

`QueryResultCardinality` represents the number of results of a query, which can either be an estimated value or exact.

type contains the value `"estimate"` or `"exact"`,
which respectively refer to an exact or estimate value.

value contains the cardinality value.

### QueryOperationOrderTerm interface

```
    interface QueryOperationOrderTerm<OrderType> {
      attribute OrderType term;
      attribute ("asc" or "desc") direction;
    };
```

`QueryOperationOrderTerm` represents the ordering of a term of a given generic type.

term contains the term over which the order is applied.

direction contains the value `"asc"` or `"desc"`,
which respectively refer to an ascending or descending order.

### QueryResultOrderCost interface

```
    interface QueryResultOrderCost<OrderType> {
      attribute QueryOperationCost cost;
      attribute Array<QueryOperationOrderTerm<OrderType>> terms;
    };
```

`QueryResultOrderCost` represents the cost of a specific ordering of query results.

cost represents the cost of executing this ordering.

terms represents the order of terms in an ordering.

### QueryOperationCost interface

```
    interface QueryOperationCost {
      attribute unsigned long iterations;
      attribute unsigned long persistedItems;
      attribute unsigned long blockingItems;
      attribute unsigned long requestTime;
    };
```

`QueryOperationCost` represents the cost of a certain query operation.

iterations is estimation of how many iterations over items are executed. This can be used to determine the CPU cost.

persistedItems is estimation of how many items are stored in memory. This is used to determine the memory cost.

blockingItems is estimation of how many items block the stream. This is used to determine the time the stream is not progressing anymore.

requestTime is estimation of the time to request items from sources. This is used to determine the I/O cost.

Query context interfaces
------------------------

This section introduces interfaces related to query contexts,
which are an optional argument to queryable interfaces for passing additional in information to query engines.

### QueryContext interface

```
    interface QueryContext {
      attribute Date? queryTimestamp;
    };
```

`QueryContext` is a base context interface.

queryTimestamp The date that should be used by SPARQL operations such as `NOW()`.

### QueryStringContext interface

```
    interface QueryStringContext : QueryContext {
      attribute QueryFormat? queryFormat;
      attribute string? baseIRI;
    };
```

A `QueryStringContext` is a context that can be passed together with a query string.

queryFormat The format in which the query string is defined.

baseIRI The base IRI for parsing the query.

### QueryAlgebraContext interface

```
    interface QueryAlgebraContext : QueryContext {};
```

A `QueryAlgebraContext` is a context that can be passed together with a query `Algebra` object.

### QuerySourceContext interface

```
    interface QuerySourceContext : QueryContext {
      attribute Array? sources;
    };
```

A `QuerySourceContext` can be used by query engines that accept custom data sources during query execution.

sources An array of data sources the query engine must use.

### QueryFormat interface

```
    interface QueryFormat {
      attribute string language;
      attribute string version;
      attribute Array<string>? extensions;
    };
```

A `QueryFormat` represents the format of a string query, and may influence parsing or execution behaviour.

language The query language, e.g. `"sparql"`.

version The version of the query language, e.g. `"1.1"`.

language An optional array of extensions on the query language. The representation of these extensions is undefined.

Bindings interfaces
-------------------

This section introduces interfaces related to query result bindings.
In SPARQL SELECT queries, these bindings correspond to [solution mappings](https://www.w3.org/TR/sparql11-query/#sparqlSolutions).

Goals
-----

* Query engines should be able to interact with bindings created by different libraries.
* Bindings are immutable
* Interfaces do no specify how bindings are stored in memory

### Bindings interface

```
    interface Bindings {
      iterable<(Variable, Term)>;

      readonly attribute string type;
      readonly attribute unsigned long size;

      boolean has((Variable or string) key);
      Term? get((Variable or string) key);
      Bindings set((Variable or string) key, Term value);
      Bindings delete((Variable or string) key);
      iterable<Variable> keys();
      iterable<Term> values();
      boolean equals(optional Bindings? other);
      void forEach(BindingsEntryCallback callback);
      Bindings filter(BindingsFilterCallback callback);
      Bindings map(BindingsMapCallback callback);
      Bindings merge(Bindings other);
      Bindings mergeWith(BindingsMergeCallback callback, Bindings other);
    };
    
    callback BindingsEntryCallback = undefined (Term value, Variable key);
    callback BindingsFilterCallback = boolean (Term value, Variable key);
    callback BindingsMapCallback = Term (Term value, Variable key);
    callback BindingsMergeCallback = Term (Term self, Term other, Variable key);
```

A Bindings is an object that represents the mapping of variables to RDF values using an immutable Map-like representation.
This means that methods such as `set` and `delete` do not modify this instance,
but they return a new Bindings instance that contains the modification.

Every Bindings object is an iterable over its entries, where each entry is a tuple of `Variable` key and `Term` value.

### Attributes

type contains the constant `"bindings"`.

size is a field that contains the number of entries in this Bindings object.

### Methods

has checks if a binding exist for the given variable.
key can be a [Variable](http://rdf.js.org/data-model-spec/#variable-interface) or string. If it is a string, no `?` prefix must be given.

get returns the [Term](http://rdf.js.org/data-model-spec/#term-interface) value bound to the given variable, or `undefined` if no binding exists.
key can be a [Variable](http://rdf.js.org/data-model-spec/#variable-interface) or string. If it is a string, no `?` prefix must be given.

set returns a new Bindings object by adding the given variable and value mapping.
If the variable already exists in the binding, then the existing mapping is overwritten.
key can be a [Variable](http://rdf.js.org/data-model-spec/#variable-interface) or string. If it is a string, no `?` prefix must be given.
value is the [Term](http://rdf.js.org/data-model-spec/#term-interface) value that must be bound.

delete returns a new Bindings object by removing the given variable.
If the variable does not exist in the binding, a copy of the Bindings object is returned.
key can be a [Variable](http://rdf.js.org/data-model-spec/#variable-interface) or string. If it is a string, no `?` prefix must be given.

keys returns an iterable of [Variable](http://rdf.js.org/data-model-spec/#variable-interface) instances for which mappings exist.

values returns an iterable of [Term](http://rdf.js.org/data-model-spec/#term-interface) values for which mappings exist.

equals returns `true`
when called with parameter `other`
on an object Bindings if
all of the conditions below hold:

* `other` is *neither* `null` nor `undefined`;
* The keys in the this and the other Bindings object are equal (following the semantics of `Variable.equals`);
* For each key, the values within each Bindings object are equal (following the semantics of `Term.equals`);

forEach invokes the `callback` for all entries in this Bindings object,
with the entry value [Term](http://rdf.js.org/data-model-spec/#term-interface) as first argument, and the entry key [Variable](http://rdf.js.org/data-model-spec/#variable-interface) as second argument.

filter returns a new Bindings object by filtering entries using `callback`,
with the entry value [Term](http://rdf.js.org/data-model-spec/#term-interface) as first argument, and the entry key [Variable](http://rdf.js.org/data-model-spec/#variable-interface) as second argument.
Returning `true` indicates that this entry must be contained in the resulting Bindings object.

map returns a new Bindings object by mapping entries using `callback`,
with the entry value `Term` as first argument, and the entry key [Variable](http://rdf.js.org/data-model-spec/#variable-interface) as second argument.
The original `Term` value is replaced by the returned [Term](http://rdf.js.org/data-model-spec/#term-interface) value in the resulting Bindings object.

merge merges this Bindings object with another Bindings object.
If a merge conflict occurs (this and other have an equal variable with unequal value), then `undefined` is returned.

mergeWith merges this Bindings object with another Bindings object,
where merge conflicts can be resolved using `callback`.
`callback` is invoked with the value [Term](http://rdf.js.org/data-model-spec/#term-interface) of the first Bindings object as first argument,
the value [Term](http://rdf.js.org/data-model-spec/#term-interface) of the second Bindings object as second argument,
and the key [Variable](http://rdf.js.org/data-model-spec/#variable-interface) as third argument,
where the returned [Term](http://rdf.js.org/data-model-spec/#term-interface) is considered the merged value.

### BindingsFactory interface

```
    interface BindingsFactory {
      Bindings bindings(Array<(Variable, Term)>? entries);
      Bindings fromBindings(Bindings bindings);
    };
```

bindings() returns a new Bindings using the given entries,
where the entries are represented as an array of key-value pairs.

fromBindings() returns a copy of the given Bindings using this factory.

The following interfaces are experimental and will change in future versions of this document:

`FilterableSource`, `FilterResult`, `QueryResultMetadata`, `QueryResultMetadataCount`, `QueryResultMetadataOptions`, `Expression`, `OperatorExpression`, `TermExpression`, `ExpressionFactory`

Filter expression interfaces
----------------------------

This section introduces interfaces that enable quad sources to be filtered based on a declarative expression.

Goals
-----

* Query engines MUST be able to push down filters into sources.
* Query engines MUST be able to detect what expressions are supported by sources.
* Query engines MUST be able to obtain the estimated cardinality of any supported expression.

### FilterableSource interface

```
    interface FilterableSource {
      FilterResult matchExpression (
        optional Term? subject,
        optional Term? predicate,
        optional Term? obj,
        optional Term? graph,
        optional Expression? expression
      );
    };
```

A `FilterableSource` is an object that produces a `FilterableSourceResult` that can emit quads.
The emitted quads can be directly contained in this `FilterableSource` object, or they can be generated on the fly.

`FilterableSource` is not necessarily an extension of the [RDF/JS Source interface](https://rdf.js.org/stream-spec/#source-interface), but implementers MAY decide to implement both at the same time.

matchExpression() Returns a `FilterableSourceResult` that contains a quad stream that processes all quads matching the quad pattern and the expression.

When a `Term` parameter is defined, and is a `NamedNode`, `Literal` or `BlankNode`,
it must match each produced quad, according to the [`Quad.equals`](http://rdf.js.org/data-model-spec/#quad-interface) semantics.
When a `Term` parameter is a `Variable`,
or it is undefined, it acts as a wildcard, and can match with any `Term`.

When matching with `graph` set to `undefined` or `null`
it MUST match all the graphs (sometimes called *the union graph*). To match only *the default graph*
set `graph` to a `DefaultGraph`

When an `Expression` parameter is defined, the complete quad stream is filtered according to this expression.
When it is undefined, no filter is applied.

If parameters of type `Variable` with an equal variable name are in place,
then the corresponding quad components in the resulting quad stream MUST be equal.

`Expression`'s MAY contain `Variable` `Term`'s.
If their variable names are equal to `Variable`'s in the given quad pattern,
then the `Expression` MUST be instantiated for each variable's binding in the resulting quad stream when applying the `Expression` filter.

### FilterResult interface

```
    interface FilterResult {
      Stream quads();
      Promise<QueryResultMetadata> metadata(optional QueryResultMetadataOptions? options);
      Promise<boolean> isSupported();
    };
```

A `FilterResult` is an object that represents the result of a filter expression of `FilterableSource` for a given quad pattern and expression.
It MAY create results lazily after one of its methods is invoked.

quads() Returns a [`Stream`](https://rdf.js.org/stream-spec/#stream-interface) containing all the quads that matched the given quad pattern and expression.

metadata() Asynchronously returns a `QueryResultMetadata`, that contains the metadata of the current result.

isSupported() Asynchronously returns a boolean indicating if the requested expression is supported by the `FilterableSource`.
If it returns `true`, `quads()` and `metadata()` MAY produce a valid result.
If it returns `false`, `quads()` MUST return a stream emitting an error, and `metadata()` MUST reject.

### QueryResultMetadata interface

```
    interface QueryResultMetadata {
      attribute QueryResultMetadataCount? count;
    };
```

A `QueryResultMetadata` is an object that represents contains metadata bout a certain query result,
such as invoking `FilterableSource.matchExpression`.

count is an optional field that contains metadata about the number of quads in the result stream.

### QueryResultMetadataCount interface

```
    interface QueryResultMetadataCount {
      attribute string type;
      attribute number value;
    };
```

`QueryResultMetadataCount` is part of the `QueryResultMetadata` interface
to represent metadata about the number of quads in the result stream.

type indicates the type of counting that was done, and MUST either be `"estimate"` or `"exact"`.

value indicates an estimate of the number of quads in the stream if `type = "estimate"`,
or the exact number of quads in the stream if `type = "exact"`.

### QueryResultMetadataOptions interface

```
    interface QueryResultMetadataOptions {
      attribute string? count;
    };
```

A `QueryResultMetadataOptions` is an object that gives suggestions on what type of metadata is desired,
such as when invoking `FilterResult.metadata`.

count is an optional field that MAY either contain `"estimate"` or `"exact"`.
If defined, this type MUST correspond to the type in `QueryResultMetadataCount`.

### Expression interface

```
    interface Expression {
      attribute string expressionType;
    };
```

`QueryResultMetadataOptions` is an abstract interface that represents a generic expression over a stream of quads.

expressionType contains a value that identifies the concrete interface of the expression, since the Expression itself is not directly instantiated.
Possible values include `"operator"` and `"term"`.

### OperatorExpression interface

```
    interface OperatorExpression {
      attribute string expressionType;
      attribute string operator;
      attribute FrozenArray<Expression> args;
    };
```

An `OperatorExpression` is represents an expression that applies a given operator on given sub-expressions.

expressionType contains the constant `"operator"`.

operator contains a value that identifies an operator.
Possible values can be found in [the list of operators](#expression-operators).

args contains an array of `Expression`'s on to which the given operator applies.
The length of this array depends on the operator.

### TermExpression interface

```
    interface TermExpression {
      attribute string expressionType;
      attribute Term term;
    };
```

A `TermExpression` is an expression that contains a [`Term`](http://rdf.js.org/data-model-spec/#term-interface).

expressionType contains the constant `"term"`.

term contains a [`Term`](http://rdf.js.org/data-model-spec/#term-interface).

### ExpressionFactory interface

```
    interface ExpressionFactory {
      OperatorExpression operatorExpression(string operator, sequence<Expression> args);
      TermExpression termExpression(Term term);
    };
```

`ExpressionFactory` enables expressions to be created in an idiomatic manner.

operatorExpression creates a new `OperatorExpression` instance for the given operator and array of arguments.

termExpression creates a new `TermExpression` instance for the given term.

Expression operators
--------------------

This section introduces a non-exhaustive list of operators that MAY be used in `OperatorExpression`.

Implementers MAY decide to support only a subset of these operators.

We omit any formal semantics behind these operators in this specification, and refer to their [SPARQL 1.1. semantics](https://www.w3.org/TR/sparql11-query/).

Relational operators
--------------------

This section introduces [relational operators](https://www.w3.org/TR/sparql11-query/#OperatorMapping).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| `!` | 1. `Literal (xsd:boolean)` | `Literal (xsd:boolean)` | The inverse of the given boolean value. |
| `uplus` | 1. `Literal (numeric)` | `Literal (numeric)` | The positive value of the given numeric value. |
| `uminus` | 1. `Literal (numeric)` | `Literal (numeric)` | The negative value of the given numeric value. |
| `*` | 1. `Literal (numeric)` 2. `Literal (numeric)` | `Literal (numeric)` | The multiplication of the given values. |
| `/` | 1. `Literal (numeric)` 2. `Literal (numeric)` | `Literal (numeric)` | The division of the given values. |
| `+` | 1. `Literal (numeric)` 2. `Literal (numeric)` | `Literal (numeric)` | The addition of the given values. |
| `-` | 1. `Literal (numeric)` 2. `Literal (numeric)` | `Literal (numeric)` | The subtraction of the given values. |
| `=` | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | If the given values are equal. If the terms are `Literal`s, their lexical value is compared |
| `!=` | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | If the given values are not equal. If the terms are `Literal`s, their lexical value is compared |
| `<` | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | If the first value is lesser than the second value. If the terms are `Literal`s, their lexical value is compared |
| `>` | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | If the first value is greater than the second value. If the terms are `Literal`s, their lexical value is compared |
| `≤` | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | If the first value is lesser than or equal to the second value. If the terms are `Literal`s, their lexical value is compared |
| `≥` | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | If the first value is greater than or equal to the second value. If the terms are `Literal`s, their lexical value is compared |

Term functions
--------------

This section introduces [functions on RDF terms](https://www.w3.org/TR/sparql11-query/#func-rdfTerms).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| [`isiri`](https://www.w3.org/TR/sparql11-query/#func-isIRI) | 1. `Term` | `Literal (xsd:boolean)` | Returns true if term is a `NamedNode`. Returns false otherwise. |
| [`isblank`](https://www.w3.org/TR/sparql11-query/#func-isBlank) | 1. `Term` | `Literal (xsd:boolean)` | Returns true if term is a `BlankNode`. Returns false otherwise. |
| [`isliteral`](https://www.w3.org/TR/sparql11-query/#func-isLiteral) | 1. `Term` | `Literal (xsd:boolean)` | Returns true if term is a `Literal`. Returns false otherwise. |
| [`isnumeric`](https://www.w3.org/TR/sparql11-query/#func-isNumeric) | 1. `Term` | `Literal (xsd:boolean)` | Returns true if term is a `Literal` with a numeric datatype. Returns false otherwise. |
| [`str`](https://www.w3.org/TR/sparql11-query/#func-str) | 1. `Term` | `Literal (xsd:string)` | Returns the (lexical) string representation of the given term. |
| [`lang`](https://www.w3.org/TR/sparql11-query/#func-lang) | 1. `Literal` | `Literal (xsd:string)` | Returns the language tag of the given `Literal`, or the empty string if the `Literal` has no language tag. |
| [`datatype`](https://www.w3.org/TR/sparql11-query/#func-datatype) | 1. `Literal` | `NamedNode` | Returns the datatype of the given `Literal`. |
| [`iri`](https://www.w3.org/TR/sparql11-query/#func-iri) | 1. `Literal` (xsd:string), `NamedNode` | `NamedNode` | Resolve the given IRI against the base IRI of the current context. |
| [`bnode`](https://www.w3.org/TR/sparql11-query/#func-bnode) | 1. `Literal` (xsd:string), *empty* | `BlankNode` | Create a new blank node with the given label if provided. |
| [`strdt`](https://www.w3.org/TR/sparql11-query/#func-strdt) | 1. `Literal` (xsd:string) 2. `NamedNode` | `Literal` | Returns a new `Literal` with the given datatype. |
| [`strlang`](https://www.w3.org/TR/sparql11-query/#func-strlang) | 1. `Literal` (xsd:string) 2. `Literal` (xsd:string) | `Literal` | Returns a new `Literal` with the given language tag. |
| [`uuid`](https://www.w3.org/TR/sparql11-query/#func-uuid) | / | `NamedNode` | Returns a new `NamedNode` following the [UUID URN scheme](https://www.ietf.org/rfc/rfc4122.txt). |
| [`struuid`](https://www.w3.org/TR/sparql11-query/#func-struuid) | / | `Literal` (xsd:string) | Returns a new `Literal` following the [UUID URN scheme](https://www.ietf.org/rfc/rfc4122.txt). |

String functions
----------------

This section introduces [string functions](https://www.w3.org/TR/sparql11-query/#func-strings).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| [`strlen`](https://www.w3.org/TR/sparql11-query/#func-strlen) | 1. `Literal (xsd:string)` | `Literal (xsd:integer)` | Returns the number of characters of the given string. |
| [`substr`](https://www.w3.org/TR/sparql11-query/#func-substr) | 1. `Literal (xsd:string)` 2. `Literal (xsd:integer)` 3. `Literal (xsd:integer)` (optional) | `Literal (xsd:string)` | Returns the substring of the given string starting from the given position (second parameter) with the given length (third parameter). If no third parameter is provided, then the maximum length is taken. |
| [`ucase`](https://www.w3.org/TR/sparql11-query/#func-ucase) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Transform each character in the given string to upper case. |
| [`lcase`](https://www.w3.org/TR/sparql11-query/#func-lcase) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Transform each character in the given string to lower case. |
| [`strstarts`](https://www.w3.org/TR/sparql11-query/#func-strstarts) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` | `Literal (xsd:boolean)` | Check if the given string starts with the given second string. |
| [`strends`](https://www.w3.org/TR/sparql11-query/#func-strends) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` | `Literal (xsd:boolean)` | Check if the given string ends with the given second string. |
| [`strcontains`](https://www.w3.org/TR/sparql11-query/#func-strcontains) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` | `Literal (xsd:boolean)` | Check if the given string contains the given second string. |
| [`strbefore`](https://www.w3.org/TR/sparql11-query/#func-strbefore) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` | `Literal (xsd:string)` | From the given first string, find the full string that occurs before the given second string. |
| [`strafter`](https://www.w3.org/TR/sparql11-query/#func-strafter) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` | `Literal (xsd:string)` | From the given first string, find the full string that occurs after the given second string. |
| [`encode_for_uri`](https://www.w3.org/TR/sparql11-query/#func-encode) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Apply URI encoding on the given string. |
| [`concat`](https://www.w3.org/TR/sparql11-query/#func-concat) | 1. `Literal (xsd:string)` (variable number of arguments) | `Literal (xsd:string)` | Concatenation of all the given strings. |
| [`langmatches`](https://www.w3.org/TR/sparql11-query/#func-langMatches) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` | `Literal (xsd:boolean)` | If the language tag of the first literal matches the second string. |
| [`regex`](https://www.w3.org/TR/sparql11-query/#func-regex) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` 3. `Literal (xsd:string)` (optional) | `Literal (xsd:boolean)` | Check if on the given first string, the given second regular expression matches. The third parameter indicates optional regex flags. |
| [`replace`](https://www.w3.org/TR/sparql11-query/#func-replace) | 1. `Literal (xsd:string)` 2. `Literal (xsd:string)` 3. `Literal (xsd:string)` 4. `Literal (xsd:string)` (optional) | `Literal (xsd:boolean)` | In the given first string, match the given second regular expression, and replace it with the given third string. The fourth parameter indicates optional regex flags. |

Numerical functions
-------------------

This section introduces [numerical functions](https://www.w3.org/TR/sparql11-query/#func-numerics).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| [`abs`](https://www.w3.org/TR/sparql11-query/#func-abs) | 1. `Literal (numeric)` | `Literal (numeric)` | Returns the absolute value of the given numerical term. |
| [`round`](https://www.w3.org/TR/sparql11-query/#func-round) | 1. `Literal (numeric)` | `Literal (numeric)` | Returns the number with no fractional part that is closest to the argument, with preference for rounding up. |
| [`ceil`](https://www.w3.org/TR/sparql11-query/#func-ceil) | 1. `Literal (numeric)` | `Literal (numeric)` | Returns the smallest (closest to negative infinity) number with no fractional part that is not less than the value of arg. |
| [`floor`](https://www.w3.org/TR/sparql11-query/#func-floor) | 1. `Literal (numeric)` | `Literal (numeric)` | Returns the largest (closest to positive infinity) number with no fractional part that is not greater than the value of arg. |
| [`rand`](https://www.w3.org/TR/sparql11-query/#func-rand) | / | `Literal (xsd:double)` | Returns a pseudo-random, number between 0 (inclusive) and 1.0e0 (exclusive). Different numbers can be produced every time this function is invoked. Numbers should be produced with approximately equal probability. |

Date and time functions
-----------------------

This section introduces [date and time functions](https://www.w3.org/TR/sparql11-query/#func-date-time).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| [`now`](https://www.w3.org/TR/sparql11-query/#func-now) | / | `Literal (xsd:dateTime)` | Returns an XSD dateTime value for the current query execution. All calls to this function in any one query execution must return the same value. |
| [`year`](https://www.w3.org/TR/sparql11-query/#func-year) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:integer)` | Returns the year of the given date. |
| [`month`](https://www.w3.org/TR/sparql11-query/#func-month) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:integer)` | Returns the month of the given date. |
| [`day`](https://www.w3.org/TR/sparql11-query/#func-day) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:integer)` | Returns the day of the given date. |
| [`hours`](https://www.w3.org/TR/sparql11-query/#func-hours) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:integer)` | Returns the hours of the given date. |
| [`minutes`](https://www.w3.org/TR/sparql11-query/#func-minutes) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:integer)` | Returns the minutes of the given date. |
| [`seconds`](https://www.w3.org/TR/sparql11-query/#func-seconds) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:integer)` | Returns the seconds of the given date. |
| [`timezone`](https://www.w3.org/TR/sparql11-query/#func-timezone) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:dayTimeDuration)` | Returns the timezone part of the given date. |
| [`tz`](https://www.w3.org/TR/sparql11-query/#func-tz) | 1. `Literal (xsd:dateTime)` | `Literal (xsd:string)` | Returns the timezone part of the given date. |

Hash functions
--------------

This section introduces [hash functions](https://www.w3.org/TR/sparql11-query/#func-hash).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| [`md5`](https://www.w3.org/TR/sparql11-query/#func-md5) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Returns the MD5 checksum of the given string. |
| [`sha1`](https://www.w3.org/TR/sparql11-query/#func-sha1) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Returns the SHA1 checksum of the given string. |
| [`sha256`](https://www.w3.org/TR/sparql11-query/#func-sha256) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Returns the SHA256 checksum of the given string. |
| [`sha384`](https://www.w3.org/TR/sparql11-query/#func-sha384) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Returns the SHA384 checksum of the given string. |
| [`sha512`](https://www.w3.org/TR/sparql11-query/#func-sha512) | 1. `Literal (xsd:string)` | `Literal (xsd:string)` | Returns the SHA512 checksum of the given string. |

XPath constructor functions
---------------------------

This section introduces [XPath constructor functions](https://www.w3.org/TR/sparql11-query/#FunctionMapping).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| `http://www.w3.org/2001/XMLSchema#string` | 1. `Term` | `Literal (xsd:string)` | Cast the given term to `xsd:string` |
| `http://www.w3.org/2001/XMLSchema#float` | 1. `Term` | `Literal (xsd:float)` | Cast the given term to `xsd:float` |
| `http://www.w3.org/2001/XMLSchema#double` | 1. `Term` | `Literal (xsd:double)` | Cast the given term to `xsd:double` |
| `http://www.w3.org/2001/XMLSchema#decimal` | 1. `Term` | `Literal (xsd:decimal)` | Cast the given term to `xsd:decimal` |
| `http://www.w3.org/2001/XMLSchema#integer` | 1. `Term` | `Literal (xsd:integer)` | Cast the given term to `xsd:integer` |
| `http://www.w3.org/2001/XMLSchema#dateTime` | 1. `Term` | `Literal (xsd:dateTime)` | Cast the given term to `xsd:dateTime` |
| `http://www.w3.org/2001/XMLSchema#date` | 1. `Term` | `Literal (xsd:date)` | Cast the given term to `xsd:date` |
| `http://www.w3.org/2001/XMLSchema#boolean` | 1. `Term` | `Literal (xsd:boolean)` | Cast the given term to `xsd:boolean` |

Functional forms
----------------

This section introduces [functional operators](https://www.w3.org/TR/sparql11-query/#func-forms).

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| [`bound`](https://www.w3.org/TR/sparql11-query/#func-bound) | 1. `Variable` | `Literal (xsd:boolean)` | Returns true if the given variable is bound to a value. Returns false otherwise. |
| [`if`](https://www.w3.org/TR/sparql11-query/#func-if) | 1. `Expression` 2. `Term` 3. `Term` | `Term` | Evaluates the expression as [effective boolean value](https://www.w3.org/TR/sparql11-query/#ebv). Returns the second argument if true, otherwise the third argument. |
| [`coalesce`](https://www.w3.org/TR/sparql11-query/#func-coalesce) | 1. `Expression` (variable number of arguments) | `Term` | Returns the first expression result that evaluates without an error. |
| [`||`](https://www.w3.org/TR/sparql11-query/#func-logical-or) | 1. `Literal (xsd:boolean)` 2. `Literal (xsd:boolean)` | `Literal (xsd:boolean)` | Returns a logical OR of left and right. Note that logical-or operates on the [effective boolean value](https://www.w3.org/TR/sparql11-query/#ebv) of its arguments. |
| [`&&`](https://www.w3.org/TR/sparql11-query/#func-logical-and) | 1. `Literal (xsd:boolean)` 2. `Literal (xsd:boolean)` | `Literal (xsd:boolean)` | Returns a logical AND of left and right. Note that logical-or operates on the [effective boolean value](https://www.w3.org/TR/sparql11-query/#ebv) of its arguments. |
| [`=`](https://www.w3.org/TR/sparql11-query/#func-RDFterm-equal) | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | Returns true if both terms are the same follow these [rules](https://www.w3.org/TR/sparql11-query/#func-RDFterm-equal). A type error is produced if both arguments are literals but not the same. |
| [`sameterm`](https://www.w3.org/TR/sparql11-query/#func-sameTerm) | 1. `Term` 2. `Term` | `Literal (xsd:boolean)` | Returns true if both terms are the same follow these [rules](https://www.w3.org/TR/sparql11-query/#func-RDFterm-equal). False is returned instead of type errors. |
| [`in`](https://www.w3.org/TR/sparql11-query/#func-in) | 1. `Term` 2. `Expression` (variable number of arguments) | `Literal (xsd:boolean)` | Tests whether the RDF term on the left-hand side is found in the values of list of expressions on the right-hand side. |
| [`notin`](https://www.w3.org/TR/sparql11-query/#func-not-in) | 1. `Term` 2. `Expression` (variable number of arguments) | `Literal (xsd:boolean)` | Tests whether the RDF term on the left-hand side is not found in the values of list of expressions on the right-hand side. |
