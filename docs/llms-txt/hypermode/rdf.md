# Source: https://docs.hypermode.com/dgraph/dql/rdf.md

# RDF Data Format

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

Dgraph natively supports Resource Description Framework (RDF) when creating,
importing and exporting data. Dgraph Client libraries can be used to query RDF
as well.

[RDF 1.1](https://www.w3.org/RDF/) is a Semantic Web Standard for data
interchange defined by the W3C. It expresses statements about resources. The
format of these statements is simple and in the form of triples.

A triple has the form

```dql
<subject> <predicate> <object> .
```

In RDF terminology, each triple represents one fact about a node.

In Dgraph, the `<subject>` of a triple is always a node, and must be a numeric
UID. The `<object>` of a triple may be another node or a literal value:

```dql
<0x01> <name> "Alice" .
<0x01> <knows> <0x02> .
```

The first triple specifies that a node has a name property of “Alice”. The
subject is the UID of the first node, the predicate is `name`, and the object is
the literal value string: `"Alice"`. The second triple specifies that Alice
knows Bob. The subject is again the UID of a node (the "alice" node), the
predicate is `knows`, and the object of this triple is the UID of the other node
(the "bob" node). When the object is a UID, the triple represents a relationship
in Dgraph.

Each triple representation in RDF ends with a period.

### Blank nodes in mutations

When creating nodes in Dgraph, you often let Dgraph assign the node
[UID](/dgraph/glossary#uid) by specifying a blank node starting with `_:`. All
references to the same blank node, such as `_:identifier123`, identify the same
node within a mutation. Dgraph creates a UID identifying each blank node.

### Language for string values

Languages are written using `@lang`. For example

```dql
<0x01> <name> "Adelaide"@en .
<0x01> <name> "Аделаида"@ru .
<0x01> <name> "Adélaïde"@fr .
<0x01> <dgraph.type> "Person" .
```

See also
[how language strings are handled in queries](/dgraph/dql/language-support#language-support).

### Types

Dgraph understands standard RDF types specified in RDF using the `^^` separator.
For example

```dql
<0x01> <age> "32"^^<xs:int> .
<0x01> <birthdate> "1985-06-08"^^<xs:dateTime> .
```

The supported
[RDF data types](https://www.w3.org/TR/rdf11-concepts/#section-Datatypes) and
the corresponding internal Dgraph type are as follows.

| Storage Type                                                                                            | Dgraph type |
| ------------------------------------------------------------------------------------------------------- | :---------: |
| \<xs:string>                                                                                            |   `string`  |
| \<xs:dateTime>                                                                                          |  `dateTime` |
| \<xs:date>                                                                                              |  `datetime` |
| \<xs:int>                                                                                               |    `int`    |
| \<xs:integer>                                                                                           |    `int`    |
| \<xs:boolean>                                                                                           |    `bool`   |
| \<xs:double>                                                                                            |   `float`   |
| \<xs:float>                                                                                             |   `float`   |
| \<geo:geojson>                                                                                          |    `geo`    |
| \<xs:password>                                                                                          |  `password` |
| \<[http://www.w3.org/2001/XMLSchema#string](http://www.w3.org/2001/XMLSchema#string)>                   |   `string`  |
| \<[http://www.w3.org/2001/XMLSchema#dateTime](http://www.w3.org/2001/XMLSchema#dateTime)>               |  `dateTime` |
| \<[http://www.w3.org/2001/XMLSchema#date](http://www.w3.org/2001/XMLSchema#date)>                       |  `dateTime` |
| \<[http://www.w3.org/2001/XMLSchema#int](http://www.w3.org/2001/XMLSchema#int)>                         |    `int`    |
| \<[http://www.w3.org/2001/XMLSchema#positiveInteger](http://www.w3.org/2001/XMLSchema#positiveInteger)> |    `int`    |
| \<[http://www.w3.org/2001/XMLSchema#integer](http://www.w3.org/2001/XMLSchema#integer)>                 |    `int`    |
| \<[http://www.w3.org/2001/XMLSchema#boolean](http://www.w3.org/2001/XMLSchema#boolean)>                 |    `bool`   |
| \<[http://www.w3.org/2001/XMLSchema#double](http://www.w3.org/2001/XMLSchema#double)>                   |   `float`   |
| \<[http://www.w3.org/2001/XMLSchema#float](http://www.w3.org/2001/XMLSchema#float)>                     |   `float`   |

### Facets

Dgraph is more expressive than RDF in that it allows properties to be stored on
every relation. These properties are called Facets in Dgraph, and dgraph allows
an extension to RDF where facet values are included in any triple.

#### Creating a list with facets

The following set operation uses a sequence of RDF statements with additional
facet information:

```sh
{
  set {
    _:Julian <name> "Julian" .
    _:Julian <nickname> "Jay-Jay" (kind="first") .
    _:Julian <nickname> "Jules" (kind="official") .
    _:Julian <nickname> "JB" (kind="CS-GO") .
  }
}
```

```graphql
{
  q(func: eq(name,"Julian")){
    name
    nickname @facets
  }
}
```

Result:

```JSON
{
  "data": {
    "q": [
      {
        "name": "Julian",
        "nickname|kind": {
          "0": "first",
          "1": "official",
          "2": "CS-GO"
        },
        "nickname": [
          "Jay-Jay",
          "Jules",
          "JB"
        ]
      }
    ]
  }
}
```

<Tip>
  Dgraph can automatically generate a reverse relation. If the user wants to run
  queries in that direction, they would define the [reverse
  relationship](./schema#reverse-edges)
</Tip>

## N-quads format

While most RDF data uses only triples (with three parts) an optional fourth part
is allowed. This fourth component in RDF is called a graph label, and in Dgraph
it must be the UID of the namespace that the data should go into as described in
[Multi-tenancy](/dgraph/enterprise/multitenancy).

## Processing RDF to comply with Dgraph syntax for subjects

While it's valid RDF to specify subjects that are IRI strings, Dgraph requires a
numeric UID or a blank node as the subject. If a string IRI is required, Dgraph
support them via [xid properties](./upsert#external-ids-and-upsert-block). When
importing RDF from another source that does not use numeric UID subjects, it
will be required to replace arbitrary subject IRIs with blank node IRIs.

Typically this is done simply by prepending "\_:" to the start of the original
IRI. So a triple such as:

`<http://abc.org/schema/foo#item1> <http://abc.org/hasRelation> "somevalue"^^xs:string`

may be rewritten as

`<_:http://abc.org/schema/foo#item1> <http://abc.org/hasRelation> "somevalue"^^xs:string`

Dgraph will create a consistent UID for all references to the uniquely-named
blank node. To maintain this uniqueness over multiple data loads, use the
[dgraph live](/dgraph/glossary#uid) utility with the xid option, or use specific
UIDs such as the hash of the IRI in the source RDF directly.
