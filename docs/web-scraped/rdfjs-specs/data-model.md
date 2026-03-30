# RDF/JS Data Model

**Source**: https://rdf.js.org/data-model-spec/

**Description**: Specification for the RDF/JS Data Model, defining interfaces for RDF terms, quads, and datasets in JavaScript.

---

RDF/JS: Data model specification

This document provides a specification of a low level interface definition representing RDF data
independent of a serialized format in a JavaScript environment. The task force which defines
this interface was formed by RDF JavaScript library developers with the wish to make existing
and future libraries interoperable. This definition strives to provide the minimal necessary
interface to enable interoperability of libraries such as serializers, parsers and higher level
accessors and manipulators.

## Design elements and principles

* We define data interfaces to represent **quads**,
  **named nodes**, **blank nodes**, **literals** and
  **variables**.
* Instances of the interfaces created with different libraries should be interoperable.
* Interfaces do *not* specify how instances are stored in memory.
* Interfaces mandate specific pre-defined methods such as `.equals()`.
* Interfaces are not expected to expose internal objects or return the same object from sucessive calls. Equivalence is tested with the `Term.equals()` function instead of `===` or `==`.
* Factory functions (e.g., `quad()`) or methods (e.g.,
  `store.createQuad()`) create instances.
* Interfaces may have additional implementation specific properties.
* We don't define any validation of given values (e.g. IRI, URI, CURIE).
  Implementations that apply validation should make this fact clear in their documentation.

A list of these properties maintained on the
[RDFJS Representation Task Force wiki](https://github.com/rdfjs/data-model-spec/wiki/Additional-properties).

## Data interfaces

![UML data interface diagram](img/data_diagram.svg)

### Term interface

```typescript
    [Exposed=(Window,Worker)]
    interface Term {
      attribute DOMString termType;
      attribute DOMString value;
      boolean equals(optional Term? other);
    };
```

Term is an abstract interface.

termType contains a value that identifies the concrete interface of the term, since
Term itself is not directly instantiated. Possible values include `"NamedNode"`,
`"BlankNode"`, `"Literal"`, `"Variable"`,
`"DefaultGraph"` and `"Quad"`.

value is refined by each interface which extends Term.

equals() returns `true`
when called with parameter `other`
on an object `term` if all of the conditions below hold:

* `other` is *neither* `null` nor `undefined`;
* `term.termType` is the same string as `other.termType`;
* `other` follows the additional constraints of the specific `Term` interface implemented by `term`
  (e.g., NamedNode, Literal, …);

otherwise, it returns `false`.

### NamedNode interface

```typescript
    [Exposed=(Window,Worker)]
    interface NamedNode : Term {
      attribute DOMString termType;
      attribute DOMString value;
      boolean equals(optional Term? other);
    };
```

termType contains the constant `"NamedNode"`.

value the IRI of the named node (example: `"http://example.org/resource"`).

equals() returns `true` if
all general Term.equals conditions hold
and `term.value` is the same string as `other.value`;
otherwise, it returns `false`.

### BlankNode interface

```typescript
    [Exposed=(Window,Worker)]
    interface BlankNode : Term {
      attribute DOMString termType;
      attribute DOMString value;
      boolean equals(optional Term? other);
    };
```

termType contains the constant `"BlankNode"`.

value blank node name as a string, without any serialization specific prefixes,
e.g. when parsing, if the data was sourced from Turtle, remove `"_:"`, if it was
sourced from RDF/XML, do not change the blank node name (example: `"blank3"`)

equals() returns `true` if
all general Term.equals conditions hold
and `term.value` is the same string as `other.value`;
otherwise, it returns `false`.

### Literal interface

```typescript
    [Exposed=(Window,Worker)]
    interface Literal : Term {
      attribute DOMString termType;
      attribute DOMString value;
      attribute DOMString language;
      attribute DOMString? direction;
      attribute NamedNode datatype;
      boolean equals(optional Term? other);
    };
```

termType contains the constant `"Literal"`.

value the text value, unescaped, without language or type (example:
`"Brad Pitt"`)

language the language as lowercase [[BCP47]] string (examples:
`"en"`, `"en-gb"`) or an empty string if the literal has no language.

direction is not falsy if the string is a directional language-tagged string.
In this case, the `direction` MUST be either be `"ltr"` or `"rtl"`.
Implementations supporting this feature should use an empty string when no direction is given.
`null` or `undefined` values are allowed to maintain compatibility with legacy
implementations.

datatype a `NamedNode` whose IRI represents the datatype of the literal.

If the literal has a language and a direction, its datatype has the IRI
`"http://www.w3.org/1999/02/22-rdf-syntax-ns#dirLangString"`.
If the literal has a language without direction, its datatype has the IRI
`"http://www.w3.org/1999/02/22-rdf-syntax-ns#langString"`. Otherwise, if no
datatype is explicitly specified, the datatype has the IRI
`"http://www.w3.org/2001/XMLSchema#string"`.

equals() returns `true` if
all general Term.equals conditions hold,
`term.value` is the same string as `other.value`,
`term.language` is the same string as `other.language`,
`term.direction` is the same string as `other.direction` or are both falsy, and
`term.datatype.equals(other.datatype)` evaluates to `true`;
otherwise, it returns `false`.

### Variable interface

```typescript
    [Exposed=(Window,Worker)]
    interface Variable : Term {
      attribute DOMString termType;
      attribute DOMString value;
      boolean equals(optional Term? other);
    };
```

termType contains the constant `"Variable"`.

value the name of the variable without leading `"?"` (example:
`"a"`).

equals() returns `true` if
all general Term.equals conditions hold
and `term.value` is the same string as `other.value`;
otherwise, it returns `false`.

### DefaultGraph interface

```typescript
    [Exposed=(Window,Worker)]
    interface DefaultGraph : Term {
      attribute DOMString termType;
      attribute DOMString value;
      boolean equals(optional Term? other);
    };
```

An instance of `DefaultGraph` represents the default graph. It's only allowed to
assign a `DefaultGraph` to the `graph` property of a `Quad`.

termType contains the constant `"DefaultGraph"`.

value contains an empty string as constant value.

equals() returns `true` if
all general Term.equals conditions hold;
otherwise, it returns `false`.

### Quad interface

```typescript
    [Exposed=(Window,Worker)]
    interface Quad : Term {
      attribute DOMString termType;
      attribute DOMString value;
      attribute Term subject;
      attribute Term predicate;
      attribute Term _object;
      attribute Term graph;
      boolean equals(optional Quad? other);
    };
```

termType contains the constant `"Quad"`.

value contains an empty string as constant value.

subject the subject, which is a `NamedNode`, `BlankNode`,
`Variable` or `Quad`.

predicate the predicate, which is a `NamedNode` or
`Variable`.

object the object, which is a `NamedNode`, `Literal`,
`BlankNode` or `Variable`.

graph the named graph, which is a `DefaultGraph`,
`NamedNode`, `BlankNode` or `Variable`.

`Triple` MUST be represented as `Quad` with `graph` set to a `DefaultGraph`

equals() returns `true`
when called with parameter `other`
on an object `quad` if
all of the conditions below hold:

* `other` is *neither* `null` nor `undefined`;
* `quad.subject.equals(other.subject)` evaluates to `true`;
* `quad.predicate.equals(other.predicate)` evaluates to `true`;
* `quad.object.equals(other.object)` evaluates to a `true`;
* `quad.graph.equals(other.graph)` evaluates to a `true`;

otherwise, it returns `false`.

### DataFactory interface

```typescript
    [Exposed=(Window,Worker)]
    interface DataFactory {
      NamedNode namedNode(DOMString value);
      BlankNode blankNode(optional DOMString value);
      Literal literal(DOMString value, optional (DOMString or NamedNode or DirectionalLanguage) languageOrDatatype);
      Variable variable(DOMString value);
      DefaultGraph defaultGraph();
      Quad quad(Term subject, Term predicate, Term _object, optional Term? graph);
      Term fromTerm(Term original);
      Quad fromQuad(Quad original);
    };

    [Exposed=(Window,Worker)]
    interface DirectionalLanguage {
      attribute DOMString language;
      attribute DOMString? direction;
    };
```

For default values of the instance properties and valid values requirements,
see the individual [interface definitions](#data-interfaces).

namedNode() returns a new instance of `NamedNode`.

blankNode() returns a new instance of `BlankNode`. If the value
parameter is undefined a new identifier for the blank node is generated for each call.

literal() returns a new instance of `Literal`.
If `languageOrDatatype` is a `NamedNode`,
then it is used for the value of `datatype`.
If `languageOrDatatype` is a `DirectionalLanguage`,
then its `language` and `direction` attributes
are respectively used for the literal's `language` and `direction`, where `direction` is optional or can be falsy.
Otherwise `languageOrDatatype` is used for the value of `language`.

variable() returns a new instance of `Variable`. This method is
optional.

defaultGraph() returns an instance of `DefaultGraph`.

quad()returns a new instance of `Quad`.
If `graph` is `undefined` or `null`
it MUST set `graph` to a `DefaultGraph`.

fromTerm() returns a new instance of the specific `Term` subclass given by `original.termType`
(e.g., `NamedNode`, `BlankNode`, `Literal`, etc.),
such that `newObject.equals(original)` returns `true`.

fromQuad() returns a new instance of `Quad`,
such that `newObject.equals(original)` returns `true`.
