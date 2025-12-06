# Source: https://docs.vespa.ai/en/basics/schemas.html.md

# Source: https://docs.vespa.ai/en/reference/schemas/schemas.html.md

# Schema reference

 

This reference documents the syntax and content of schemas, document types, and fields. This is a reference, see [schemas](../../basics/schemas.html) for an overview and examples.

## Syntax

Throughout this document, a string in square brackets represents some argument. The whole string, including the brackets, is replaced by a concrete string in a schema.

Constructs in schemas have a regular syntax. Each element starts with the element _identifier_, possibly followed by the _name_ of this particular occurrence of the element, possibly followed by a space-separated list of interleaved _attribute names_and _attribute values_, possibly followed by the _element body_. Thus, one will find elements of these varieties:

`[element-identifier] : [element-body]`  
`[element-identifier] [element-name] : [element-body]`  
`[element-identifier] [element-name] [attribute-name] [attribute-value]`  
`[element-identifier] [element-name] [attribute-name] [attribute-value] {
    [element-body]
}`

One-line element values start with a colon and end with a newline.

Multiline values (for fields supporting them) are any block of text enclosed in curly brackets.

Comments may be inserted anywhere and start with a hash (#).

Names are _identifiers_, they must match `["a"-"z","A"-"Z", "_"]["a"-"z","A"-"Z","0"-"9","_"]*`.

A schema file is not sensitive to indentation.

## Elements

Elements and structure of a schema file:

```
[schema](#schema)[document](#document)[struct](#struct)[field](#field)[match](#match)[field](#field) [array\<type\>](#array)[bool](#bool)[byte](#byte)[double](#double)[float](#float)[int](#int)[long](#long)[map\<key-type,value-type\>](#map)[position](#position)[predicate](#predicate)[raw](#raw)[reference\<document-type\>](#reference)[string](#string)[struct-name](#struct-name)[tensor(dimension-1,...,dimension-N)](#tensor)[uri](#uri)[weightedset\<element-type\>](#weightedset)[weightedset](#weightedset-properties)[alias](#alias)[attribute](#attribute)[distance-metric](#distance-metric)[bolding](#bolding)[dictionary](#dictionary)[id](#id)[index](#index)[hnsw](#index-hnsw)[indexing](#indexing)[match](#match)[normalizing](#normalizing)[query-command](#query-command)[rank](#rank)[rank-type](#rank-type)[sorting](#sorting)[stemming](#stemming)[struct-field](#struct-field)[indexing](#indexing)[match](#match)[query-command](#query-command)[struct-field](#struct-field)…[summary](#summary)[summary-to **DEPRECATED**](#summary-to)[summary](#summary)[summary-to **DEPRECATED**](#summary-to)[weight](#weight)[compression](#compression)[index](#index)[field](#field)[fieldset](#fieldset)[rank-profile](#rank-profile)[diversity](#diversity)[attribute](#diversity-attribute)[min-groups](#diversity-min-groups)[match-phase](#match-phase)[attribute](#match-phase-attribute)[order](#match-phase-order)[max-hits](#match-phase-max-hits)[first-phase](#firstphase-rank)[keep-rank-count](#keep-rank-count)[rank-score-drop-limit](#rank-score-drop-limit)[expression](#expression)[second-phase](#secondphase-rank)[expression](#expression)[rank-score-drop-limit](#secondphase-rank-score-drop-limit)[rerank-count](#secondphase-rerank-count)[global-phase](#globalphase-rank)[expression](#expression)[rerank-count](#globalphase-rerank-count)[rank-score-drop-limit](#globalphase-rank-score-drop-limit)[function [name] ](#function-rank)[inputs](#inputs)[constants](#constants)[onnx-model](#onnx-model)[significance](#significance)[rank-properties](#rank-properties)[match-features](#match-features)[mutate](#mutate)[on-match](#on-match)[on-first-phase](#on-first-phase)[on-second-phase](#on-second-phase)[on-summary](#on-summary)[summary-features](#summary-features)[rank-features](#rank-features)[ignore-default-rank-features](#ignore-default-rank-features)[num-threads-per-search](#num-threads-per-search)[num-search-partitions](#num-search-partitions)[min-hits-per-thread](#min-hits-per-thread)[termwise-limit](#termwise-limit)[post-filter-threshold](#post-filter-threshold)[approximate-threshold](#approximate-threshold)[filter-first-threshold](#filter-first-threshold)[filter-first-exploration](#filter-first-exploration)[exploration-slack](#exploration-slack)[target-hits-max-adjustment-factor](#target-hits-max-adjustment-factor)[filter-threshold](#filter-threshold)[rank](#rank)[filter-threshold](#rank-filter-threshold)[element-gap](#rank-element-gap)[rank-type](#rank-type)[weakand](#weakand)[stopword-limit](#weakand-stopword-limit)[adjust-target](#weakand-adjust-target)[allow-drop-all](#weakand-allow-drop-all)[rank-profile (inner)](#rank-profile)[constant](#constant)[onnx-model](#onnx-model)[stemming](#stemming)[document-summary](#document-summary)[summary](#summary)[import field](#import-field)[raw-as-base64-in-summary](#raw-as-base64-in-summary)
```

## schema

The root element of schemas. A schema describes a type of data and what we should compute over it. A schema must be defined in a file named `[schema-name].sd`.

```
schema [name] inherits [name] {
    [body]
}
```

The `inherits` attribute is optional. If a schema is inherited, this schema will include all the constructs of it as if they were defined in this schema (except the parent document type). The document type in this must declare that it inherits the document type of the parent schema.

The body is mandatory and may contain:

| Name | Occurrence | Description |
| --- | --- | --- |
| [document](#document) | One | A document type defined in this schema |
| [field](#field) | Zero to many | A field not contained in the document. Use _synthetic fields_ (outside [document](#document)) to derive new field values to be placed in the indexing structure from document fields. Find examples in [reindexing](../../operations/reindexing.html#use-cases). |
| [fieldset](#fieldset) | Zero to many | Group document fields together for searching |
| [rank-profile](#rank-profile) | Zero to many | A bundle of ranking functions and settings, selectable in a query. |
| [constant](#constant) | Zero to many | A constant tensor located in a file used for ranking |
| [onnx-model](#onnx-model) | Zero to many | An ONNX model located in the application package used for ranking |
| [stemming](#stemming) | Zero or one | The default stemming setting. |
| [raw-as-base64-in-summary](#raw-as-base64-in-summary) | Zero or one | Base64 encode raw fields in summary rather than using an escaped string. The default is true. |
| [document-summary](#document-summary) | Zero to many | An explicitly defined document summary |
| [import field](#import-field) | Zero to many | Import a field value from a global document |

## document

Contained in [schema](#schema) and describes a document type. This can also be the root of the schema, if the document is not to be queried directly.

```
document [name] inherits [name-list] {
    [body]
}
```

The document name is optional; it defaults to the containing `schema` element's name. If there is no containing `schema` element, the document name is required. If the document with a name is defined inside a schema, the document name must match the `schema` element's name. The reference to _document type_ in the documentation refers to the document name defined here.

The `inherits` attribute is optional and has as value a comma-separated list of names of other document types. A document type may inherit the fields of one or more other document types, see [document inheritance](/en/schemas/inheritance-in-schemas.html) for examples. If no document types are explicitly inherited, the document inherits the generic `document` type.

The body of a document type is optional and may contain:

| Name | Occurrence | Description |
| --- | --- | --- |
| [struct](#struct) | Zero to many | A struct type definition for this document. |
| [field](#field) | Zero to many | A field of this document. |
| [compression](#compression) | Zero to one | Specifies compression options for documents of this document type in storage. |

## struct

Contained in [document](#document). Defines a composite type. A struct consists of zero or more fields that the user can access together as one. The struct has to be defined before it is used as a type in a field specification.

```
struct [name] {
    [body]
}
```

The body of a struct is optional and may contain:

| Name | Occurrence | Description |
| --- | --- | --- |
| [field](#field) | Zero to many | A field of this struct. |

## field

Contained in[schema](#schema),[document](#document), or[struct](#struct). Defines a named value with a type and (optionally) how this field should be stored, indexed, searched, presented, and how it should influence ranking.

```
field [name] type [type-name] {
    [body]
}
```
Do not use names that are used for other purposes in the indexing language or other places in the schema file. Reserved names are:
- attribute
- body
- case
- context
- documentid
- else
- header
- hit
- host
- if
- index
- position
- reference
- relevancy
- sddocname
- summary
- switch
- tokenize

Other names not to use include any words that start with a number or include special characters.

The _type_ attribute is mandatory - supported types:

| Field type | Description |
| --- | --- |
| array\<type\> | 

For single-value (primitive) types, use array\<type\> to create an array field of the element type:

| Index | Each element is indexed separately |
| Attribute | Added as an array attribute |
| Summary | Added as an array summary field |

Also used to create an array field of the given [struct type](#struct). The struct type must be defined separately. Example:

```
struct person {
    field first_name type string {}
    field last_name type string {}
}

field people type array<person> {
    indexing: summary
    summary: matched-elements-only
    struct-field first_name {
        indexing: attribute
        attribute: fast-search
    }
}
```

The entire _people_ field is part of the document summary. The [struct field](#struct-field) _first\_name_ is defined as an _attribute_ for searching, with [fast-search](../../content/attributes.html#fast-search). A subset, or all, of the struct fields can be defined as attributes.

Use the [sameElement](../querying/yql.html#sameelement) operator to ensure matches in the same struct field instance.

Use [matched-elements-only](#matched-elements-only) to reduce the amount of data that is returned in the document summary.

 **Important:**`key` and `value` are reserved words in an array\<struct\>, as these are used to implement [map](#map). Do not use these as struct-field names.

Restrictions:

- Array of struct types does not support [ranking features](../../basics/ranking.html) and can only be used for matching and filtering.
- All struct arrays can be fed, retrieved, and used in document summaries.
- Some parts of struct arrays can be searched in [indexed search mode](../applications/services/content.html#document), while all parts of struct arrays can be searched in [streaming search](../../performance/streaming-search.html). See below for supported cases.

| Index | Only supported in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search). Set this on the top-level struct array field to make all parts searchable. |
| Attribute | Only supported for [struct fields](#struct-field) that have primitive types (string, int, long, byte, float, double). Any struct field must be defined as an attribute to be used for searching. The struct type can still contain fields of non-primitive types, as long as these are not defined as attributes. |
| Summary | Added as an array summary field |

 |
| bool | 

Use for boolean values.

```
field alive type bool {
    indexing: summary | attribute
}
```

| Index | Not supported |
| Attribute | Added as a boolean |
| Summary | Added as a boolean value (`true` or `false`) |

 **Important:** Defaults to `false` if not specified. 
 |
| byte | 

Use for single 8-bit numbers.

```
field smallnumber type byte {
    indexing: summary | attribute
}
```

| Index | Not supported. An attribute will automatically be used instead |
| Attribute | Added as a byte which supports range searches |
| Summary | Added as a byte |

 |
| double | 

Use for high precision floating point numbers (64-bit IEEE 754 double).

```
field mydouble type double {
    indexing: summary | attribute
}
```

| Index | Not supported. An attribute will automatically be used instead |
| Attribute | Added as a 64-bit IEEE 754 double which supports range searches |
| Summary | Added as a 64-bit IEEE 754 double |

 |
| float | 

Use for floating point numbers (32-bit IEEE 754 float).

```
field myfloat type float {
    indexing: summary | attribute
}
```

| Index | Not supported. An attribute will automatically be used instead |
| Attribute | Added as a 32-bit IEEE 754 float which supports range searches |
| Summary | Added as a 32-bit IEEE 754 float |

 |
| int | 

Use for single 32-bit integers.

```
field release_year type int {
    indexing: summary | attribute
}
```

| Index | Not supported. An attribute will automatically be used instead |
| Attribute | Becomes integer attributes, which supports range grouping and range searches |
| Summary | Added as a 32-bit integer |

 |
| long | 

Use for single 64-bit integers.

```
field bignumber type long {
    indexing: summary | attribute
}
```

| Index | Not supported. An attribute will automatically be used instead |
| Attribute | Becomes a 64-bit integer attribute, which supports range grouping and range searches |
| Summary | Added as a 64-bit integer |

 |
| map\<key-type,value-type\> | 

Use to create a map where each unique key is mapped to a single value. Any primitive type can be used as _key-type_ and any primitive type or Vespa struct type as _value-type_. Example of a map of primitive types, where the _key_ and _value_ fields are specified as _attributes_:

```
field my_map type map<string, int> {
    indexing: summary
    struct-field key { indexing: attribute }
    struct-field value { indexing: attribute }
}
```

Note that a Vespa map entry is handled as a _struct_ with a _key_ and _value_ field with _key-type_ and _value-type_ as types. This explains the _struct-field_ syntax above. The full _my\_map_ field is configured into the document summary.

A more complex example is a map of struct:

```
struct person {
    field first_name type string {}
    field last_name type string {}
    field age type int {}
}

field identities type map<string, person> {
    indexing: summary
    summary: matched-elements-only
    struct-field key {
        indexing: attribute
        attribute: fast-search
    }
    struct-field value.first_name {
        indexing: attribute
        attribute: fast-search
    }
    struct-field value.last_name {
        indexing: attribute
        attribute: fast-search
    }
}
```

This example illustrates that the struct elements are configured individually - there is no field configuration for _age_ - one can define a subset of the struct fields as attributes.

Here, _key_, _value.first\_name_ and _value.last\_name_ are defined as attributes. This makes them available for searching and [grouping](/en/querying/grouping.html#grouping-over-a-map-field). A common use case is requiring matches in the same map entry (e.g., match both first and last name for the same person), see the [sameElement](/en/reference/querying/yql.html#sameelement) operator for how to implement this. Use [matched-elements-only](#matched-elements-only) to reduce the amount of data in the document summary.

[fast-search](/en/performance/feature-tuning.html#when-to-use-fast-search-for-attribute-fields) is used to make query access faster by creating an index structure for lookups.

As an alternative to a map, an [array\<struct\>](#array) can contain the same element multiple times and maintains order.

Restrictions:

- Map of struct or primitive types do not support [ranking features](../../basics/ranking.html) and can only be used for matching and filtering.
- All map types can be fed, retrieved, and used in document summaries.
- Some map types can be searched in [indexed search mode](../applications/services/content.html#document), while all map types can be searched in [streaming search](../../performance/streaming-search.html). See below for supported cases:

| Index | Only supported in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search). Set this on the top-level map field to make all struct fields in the map field searchable. |
| Attribute | Only supported for [struct fields](#struct-field) where _value-type_ is either a primitive type (string, int, long, byte, float, double) or a [struct type](#struct) with fields of primitive types. Any struct field must be defined as an attribute to be used for searching. The _value-type_ struct can still contain fields of non-primitive types, as long as these are not defined as attributes. |
| Summary | Added as a map. |

 |
| position | 

Used to filter and/or rank documents by distance to a position in the query, see [Geo search](../../querying/geo-search.html).

```
field location type position {
    indexing: attribute
}
```

| Index | Not supported |
| Attribute | Added as an interleaved 64-bit integer (see [Z-order curve](https://en.wikipedia.org/wiki/Z-order_curve)) - queries are implemented by doing a set of range searches in the attribute. This attribute has [fast-search](../../content/attributes.html#fast-search) set implicitly |
| Summary | Refer to the [reference](document-json-format.html#position) |

 |
| predicate | 

Use to match queries to a set of boolean constraints. See [querying predicate fields.](../../schemas/predicate-fields.html#queries) Predicate fields are not supported in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

```
field predicate_field type predicate {
    indexing: attribute
    index {
        arity: 2 # mandatory
        lower-bound: 3
        upper-bound: 200
        dense-posting-list-threshold: 0.25
    }
}
```

| Index | Not supported |
| Attribute | Indexed in-memory in a variable-size binary format that is optimized for application during query evaluation |
| Summary | Added as-is |

 |
| raw | 

Use for binary data

```
field rawfield type raw {
    indexing: summary | attribute
}
```

| Index | Not supported |
| Attribute | Added as raw data. Not searchable. |
| Summary | Added as raw data. Outputted as a base64-encoded string. See [JSON feed format](document-json-format.html#raw) for details. |

 |
| reference\<document-type\> | 

A _reference\<document-type\>_ field is a reference to an instance of a document-type - i.e., a foreign key. Reference fields are not supported in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

```
field artist_ref type reference<artist> {
    indexing: attribute
}
```
 The reference is the [document id](../../schemas/documents.html) of the document-type instance. References are used to join documents in a [parent-child relationship](../../schemas/parent-child.html). A reference can only be made to [global](../applications/services/content.html#document) documents. The following types of references are not supported: 
- Self-reference
- Cyclic reference: If document type _foo_ has a reference to _bar_, then _bar_ cannot have a reference to _foo_

 A reference attribute field can be searched using the document id of the parent document-type instance as query term. Note that this will be a linear scan as [fast-search](#attribute) is not supported. 

| Index | Invalid - deployment will fail |
| Attribute | As [string](#string) - a reference must be an attribute. Can be an empty string or point to a non-existent document. Memory usage is about 33 bytes per parent document. This is composed of 24 bytes used in a reference store, with a btree structure on top of that which requires 5 bytes on average (depends on lid compaction). In addition 4 bytes on average for a reference from child document to the parent document (depends on lid compaction). In total about 33 bytes. |
| Summary | As [string](#string) |

 |
| string | 

Use for a text field of any length. String fields may only contain _text characters_, as defined by `isTextCharacter` in [com.yahoo.text.Text](https://github.com/vespa-engine/vespa/blob/master/vespajlib/src/main/java/com/yahoo/text/Text.java)

```
field surname type string {
    indexing: summary | index
}
```

| Index | Refer to [linguistics](../../linguistics/linguistics.html) for details on normalization, tokenization and stemming. |
| Attribute | Added as-is. [match](#match) exact or prefix is supported types of searches in string attributes. Searches are however case-insensitive. A query for `BritneY.spears` will match a document containing `BrItNeY.SpEars` |
| Summary | Added as-is |

 |
| struct | 

Use to define a field with a struct datatype. Create a [struct type](#struct) inside the document definition and declare the struct field in a document or struct using the struct type name as the field type:

```
struct person {
    field first_name type string {}
    field last_name type string {}
}
field my_person type person {
    indexing: summary
}
```
 Restrictions: 
- Struct fields can **not** be searched in indexed search mode (but [array of struct](#array) and [map type](#map) are searchable, with some restrictions).
- Struct fields can be fed, retrieved, and used in document summaries.

| Index | Only supported in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search). Set this on the top-level field to make all parts searchable. |
| Attribute | Not supported. |
| Summary | Added as a struct. |

 |
| tensor(dimension-1,...,dimension-N) | 

Use to create a tensor field with the given [tensor type spec](../ranking/tensor.html#tensor-type-spec) that can be used for [ranking](../../basics/ranking.html) and [nearest neighbor search](../../querying/nearest-neighbor-search). A tensor field is otherwise not searchable.

See [tensor evaluation reference](../ranking/tensor.html) for definition, the [tensor user guide](../../ranking/tensor-user-guide.html) and the [JSON feed format](document-json-format.html#tensor).

```
field tensorfield type tensor<float>(x{},y{}) {
    indexing: attribute | summary
}

field tensorfield type tensor<float>(x[2],y[2]) {
    indexing: attribute | summary
}
```

| Index | Supported for tensor types with: 
- One indexed dimension - single vector per document
- One or more mapped dimensions and one indexed dimension - multiple vectors per document

 See [approximate nearest neighbor search](../../querying/approximate-nn-hnsw). |
| Attribute | Added as-is in an attribute to be used for ranking and nearest neighbor search. |
| Summary | Added as-is. |

 |
| uri | 

Use for URL type matching. URI fields are not supported in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

| Index | 

The URL is split into its different components, which are indexed separately. Note that only URLs can be indexed this way, not other URIs. The different components are as defined by the HTTP standard: Scheme, hostname, port, path, query, and fragment. Example:

```
http://mysite.mydomain.com:8080/path/shop?d=hab&id=1804905709&cat=100#frag1
```

| scheme | http |
| hostname | mysite.mydomain.com (indexed as "mysite", "mydomain" and "com") |
| port | 8080 (note that port numbers 80 and 443 are not indexed, as they are the normal port numbers) |
| path | /path/shop (indexed as "path" and "shop") |
| query | d=hab&id=1804905709&cat=100 (indexed as "d", "hab", "id", "1804905709", "cat" and "100") |
| fragment | frag1 |

 The syntax for searching these different components is: 
```
[field-name].[component-name]:term
```
 Example: In a URI field `sourceurl`, search for documents from slashdot: 
```
query=sourceurl.hostname:slashdot
```

URL hostnames also support _anchored searching_, see [search in URL fields](../querying/yql.html#uri).

It is not possible to index uri-typed fields into a common index, i.e., it has to be indexed separately from other fields. If you need to combine URLs with other fields, you could store it in a string-field instead, but then you can not search in the different parts of the URL (scheme, hostname, port, path, query, and fragment).

**Aliasing** also works differently for URL fields - you are allowed to create aliases both to the index (as usual) and to the components of it. Use

```
alias [component]: [alias]
```
 to create an alias for a component. For example, given this field: 
```
field surl type uri {
    indexing: summary | index
    alias: url
    alias hostname: site
}
```

a search in "surl" and "url" will search in the entire url, while "surl.hostname" or "site" will search the hostname.

 |
| Attribute | Not allowed |
| Summary | Added as-is as a string |

 |
| weightedset\<element-type\> | 

Use to create a multivalue field of the element type, where each element is assigned a signed 32-bit integer weight.

```
field tag type weightedset<string> {
    indexing: attribute | summary
}
```
 The element type can be any single value type. Prefer not to use floating-point number types like _float_ or _double_. 

To access a weighted set in ranking when using `attribute`, see [attribute the match features](../ranking/rank-features.html#attribute-match-features-not-normalized), or convert the weighted set to a tensor using the tensorFromWeightedSet(field, dimensionName) feature.

To access a weighted set in ranking when using `index`, see [ranking features for indexed multivalued fields](../ranking/rank-features.html#features-for-indexed-multivalue-string-fields). Note that when using `index` with weightedset, queries are matching across elements in the set.

It is possible to specify that a new key should be created if it does not exist before the update, and that it should be removed if the weight is set to zero - see the [reference](#weightedset-properties).

The weightedset field does not support filtering on weight. If you need that use the [map](#map) type and [sameElement](../querying/yql.html#sameelement) query operator - see [this example](../../querying/query-language.html#map).

| Index | Each token present in the field is indexed separately. Information indexed includes element number, element weight, and a list of token occurrence positions for each element in which the token is present |
| Attribute | Added as a multivalue weighted attribute |
| Summary | Added as a multivalue summary field if this is an attribute |

 |

The body of a field is optional for [schema](#schema),[document](#document) and[struct](#struct). It may contain the following elements:

| Name | Occurrence | Description |
| --- | --- | --- |
| alias | Zero to many | 

Make an index or attribute available in queries under an additional name. This has minimal performance impact and can safely be added to running applications. Example:

```
field artist type string {
    alias: artist_name
}
```
 |
| [attribute](#attribute) | Zero to many | 

Specify an attribute setting.

 |
| [bolding](#bolding) | Zero to one | 

Specifies whether the content of this field should be bolded. Only supported for [index](#indexing-index) fields of type string or array\<string\>.

 |
| [id](#id) | Zero to one | 

Explicitly decide the numerical id of this field. Is normally not necessary, but can be used to save some disk space.

 |
| [index](#index) | Zero to many | 

Specify a parameter of an index.

 |
| [indexing](#indexing) | Zero to one | 

The indexing statements used to create index structure additions from this field.

 |
| [match](#match) | Zero to one | 

Set the matching type to use for this field.

 |
| [normalizing](#normalizing) | Zero or one | 

Specifies the kind of text normalizing to do on a string field.

 |
| [query-command](#query-command) | Zero to many | 

Specifies a command which can be received by a plugin searcher in the Search Container.

 |
| [rank](#rank) | Zero or one | 

Specify if the field is used for ranking.

 |
| [rank-type](#rank-type) | Zero to one | 

Selects the set of low-level rank settings to be used for this field when using default `nativeRank`.

 |
| [sorting](#sorting) | Zero or one | 

The sort specification for this field.

 |
| [stemming](#stemming) | Zero or one | 

Specifies stemming options to use for this field.

 |
| [struct-field](#struct-field) | Zero to many | 

A subfield of a field of type struct. The struct must have been defined to contain this subfield in the struct definition. If you want the subfield to be handled differently from the rest of the struct, you may specify it within the body of the struct-field.

 |
| [summary](#summary) | Zero to many | 

Sets a summary setting of this field, set to `dynamic` to make a dynamic summary.

 |
| [summary-to](#summary-to) | Zero to one | 

 **Deprecated:** Use [document-summary](#document-summary) instead.
 The list of document summary names this should be included in. |
| [weight](#weight) | Zero to one | 

The importance of a field when searching multiple fields and using `nativeRank`.

 |
| [weightedset](#weightedset-properties) | Zero to one | 

Properties of a weightedset [weightedset\<element-type\>](#weightedset)

 |

Fields can not have default values. See the [document guide](../../schemas/documents.html#fields) for how to auto-set field values.

It is not possible to query for fields without value (i.e. query for NULL) - see the [query language reference](../querying/yql.html). Fields without value are not returned in [query results](../querying/default-result-format.html).

Fields can be declared outside the document block in the schema. These fields are not part of the document type but behave like regular fields for queries. Since they are not part of the document, they cannot be written directly, but instead take their values from document fields, using the `input` expression:`indexing: input my_document_field | embed | summary | index`

This is useful e.g., to index a field in multiple ways, or to change the field value, something which is not allowed with document fields. When the document field(s) used as input are updated, these fields are updated with them.

## struct-field

Contained in [field](#field) or[struct-field](#struct-field). Defines how this struct field (a subfield of a struct) should be stored, indexed, searched, presented, and how it should influence ranking. The field in which this struct field is contained must be of type struct or a collection of type struct:

```
struct-field [name] {
    [body]
}
```

The body of a struct field is optional and may contain the following elements:

| Name | Occurrence | Description |
| --- | --- | --- |
| [indexing](#indexing) | Zero to one | The indexing statements used to create index structure additions from this field. For indexed search only `attribute` is supported, which makes the struct field a searchable in-memory attribute that can also be used for e.g. grouping and ranking. For [streaming search](../../performance/streaming-search.html)`index` and `summary` are supported in addition. |
| [attribute](#attribute) | Zero to many | Specifies an attribute setting. For example `attribute:fast-search`. |
| [rank](#rank) | Zero to one | Specifies [rank](#rank) settings |
| [match](#match) | Zero to one | Specifies [match](#match) settings |

If this struct field is of type struct (i.e., a nested struct), only [indexing:summary](#indexing) may be specified. See [array\<type\>](#array) for example use.

## fieldset

Contained in [schema](#schema).

 **Note:** this is not related to the [Document fieldset](../../schemas/documents.html#fieldsets). Also see the [FAQ](../../learn/faq#must-all-fields-in-a-fieldset-have-compatible-type-and-matching-settings) for a discussion of what happens when using different types/match settings.

A fieldset groups fields together for searching:

```
fieldset myfieldset {
    fields: a,b,c
}
```

Create a fieldset named `default` to be used as the default (i.e., when not specified in the query):

```
fieldset default {
    fields: a,b,c
}
```

See [example queries using fieldset](../../querying/query-api.html#using-a-fieldset).

The fields in the fieldset should be as similar as possible in terms of indexing clause and [match mode](#match). If they are not, test the application thoroughly. Having different match modes for the fields in the fieldset generates a warning during application deployment. If specific match settings for the fieldset are needed, such as _exact_, specify it using _match_:

```
fieldset myfieldset {
    fields: a,b,c
    match {
        exact
    }
}
```

Use [query-commands](#query-command) in the field set to set search settings. Example:

```
fieldset myfieldset {
    fields: a,b,c
    query-command:"exact @@"
}
```

Adding a fieldset will not create extra index structures in memory / on disk; it is just a mapping.

## compression

 **Deprecated:** see [deprecations](../release-notes/vespa8.html#compression).

Contained in [document](#document). If a compression level is set within this element,**lz4** compression is enabled for whole documents.

```
compression {
    [body]
}
```
The body of a compression specification is optional and may contain:

| Name | Occurrence | Description |
| --- | --- | --- |
| type | Zero to one | 

**LZ4** is the only valid compression method.

 |
| level | Zero to one | 

Enable compression. LZ4 is linear and 9 means HC(high compression)

 |
| threshold | Zero to one | 

A percentage (multiplied by 100) giving the maximum size that compressed data can have to keep the compressed value. If the resulting compressed data is higher than this, the document will be stored uncompressed. The default value is 95.

 |

## rank-profile

Contained in [schema](#schema) or equivalently in separate files in the[application package](../applications/application-packages.html), named`[profile-name].profile` in any directory below `schemas/[schema-name]/`. A [rank profile](../../basics/ranking.html#rank-profiles) is a named set of ranking expression functions and settings which can be[selected in the query](../api/query.html#ranking.profile)).

Whether defined inline in the schema or in a separate .profile file, the syntax of a rank profile is

```
rank-profile [name] inherits [rank-profile1], [rank-profile2], ... {
    [body]
}
```

The `inherits` list is optional and may contain the name of other rank profiles in this schema or one it inherits. Elements not defined in this rank profile will then be inherited from those profiles. Inheriting multiple profiles that define the same elements leads to an error at deployment.

The body of a rank-profile may contain:

| Name | Occurrence | Description |
| --- | --- | --- |
| [diversity](#diversity) | Zero or one | Specification of required diversity between the different phases. |
| [strict](#strict) | Zero or one | true/false: Whether to use strict or loose type checking. |
| [match-phase](#match-phase) | Zero or one | Ranking configuration to be used for hit limitation during matching. |
| [first-phase](#firstphase-rank) | Zero or one | The ranking config to be used for first-phase ranking. |
| [second-phase](#secondphase-rank) | Zero or one | The ranking config to be used for second-phase ranking. |
| [global-phase](#globalphase-rank) | Zero or one | The ranking config to be used for global-phase ranking. |
| [function [name] ](#function-rank) | Zero or more | Defines a named function that can be referenced during ranking phase(s) and (if without arguments) as part of match-and summary-features. |
| [inputs](#inputs) | Zero or many | List of query features used in ranking expressions. |
| [constants](#constants) | Zero or many | List of constant features available in ranking expressions. |
| [mutate](#mutate) | Zero or many | Specification of mutations you can apply after different phases of a query. |
| [onnx-model](#onnx-model) | Zero or many | An onnx model to make available in this profile. |
| [significance](#significance) | Zero or one | To enable the use of significance models defined in the service.xml config. |
| [rank-properties](#rank-properties) | Zero or one | List of any rank property key-values to be used by rank features. |
| [match-features](#match-features) | Zero or more | The [rank features](../ranking/rank-features.html) to be returned with each hit, computed in the _match_ phase. |
| [summary-features](#summary-features) | Zero or more | The [rank features](../ranking/rank-features.html) to be returned with each hit, computed in the _fill_ phase. |
| [rank-features](#rank-features) | Zero or more | The [rank features](../ranking/rank-features.html) to be dumped when using the query-argument [rankfeatures](../api/query.html#ranking.listfeatures). |
| ignore-default-rank-features | Zero or one | 

Do not dump the default set of rank features, only those explicitly specified with the [rank-features](#rank-features) command.

 |
| num-threads-per-search | Zero or one | 

Overrides the global [persearch](../applications/services/content.html#requestthreads-persearch) threads to a **lower** value.

 |
| min-hits-per-thread | Zero or one | 

After estimating the number of hits for a query prior to query evaluation, this number is used to decide how many threads to use for the query.

`num_treads = min(num-threads-per-search,
      estimated_hits / min-hits-per-thread)`

The current default is 1. If you suspect the fixed cost per thread is too high, increasing this number might be a good idea. Especially if most of your queries are cheap, but you have increased the [num-threads-per-search](#num-threads-per-search) in order to reduce latency for your costly queries covering a lot of documents. The default might change, or the optimal value might be adaptive rendering overrides ignored or counterproductive.

 |
| num-search-partitions | Zero or one | 

The number of logical partitions in which the corpus is divided on a search node. By default, this is the same as [num-threads-per-search](#num-threads-per-search). A partition is the smallest unit a search thread will handle. If you have a locality in time when searching and feeding documents, you might want to split it into more, smaller partitions. That way, you avoid that one costly partition leaves some threads idle while others are working hard.

If you have 8 threads per search, you might have 10x as many partitions at 80 reducing max skew with a similar factor. Note that a value of zero turns on adaptive partitioning which tries to solve this optimally.

 **Note:** If `num-search-partitions` is set to 0 (work sharing is enabled), make sure `termwise-limit` is set to 1.0 (termwise evaluation is disabled). This is to avoid redoing termwise evaluation when work is passed from one thread to another.
 |
| termwise-limit | Zero or one | 

If estimated number of hits \> corpus \* termwise-limit, it will prune candidates with a CPU cache-friendly [TAAT](../../performance/feature-tuning.html#hybrid-taat-daat) with the terms not needed for ranking, prior to doing [DAAT](../../performance/feature-tuning.html#hybrid-taat-daat). Current default is 1.0 which turns it off. A value between 0.05 and 0.20 can be a good starting point. This is particularly useful if you have many weak filters. Note that this is a manual override. The default might change, or the optimal value might be adaptive rendering overrides ignored or counterproductive.

 |
| post-filter-threshold | Zero or one | 

Threshold value (in the range [0.0, 1.0]) deciding if a query with an approximate [nearestNeighbor](../querying/yql.html#nearestneighbor) operator combined with filters is evaluated using post-filtering instead of the default filtering. Post-filtering is chosen when the estimated filter hit ratio of the query is _larger_ than this threshold. The default value is 1.0, which disables post-filtering. See [Controlling the filtering behavior with approximate nearest neighbor search](https://blog.vespa.ai/constrained-approximate-nearest-neighbor-search/#controlling-the-filtering-behavior-with-approximate-nearest-neighbor-search) for more details.

With post-filtering the [targetHits](../querying/yql.html#targethits) value used when searching the HNSW index is auto-adjusted in an effort to expose _targetHits_ hits to first-phase ranking after post-filtering has been applied. The following formula is used:

```
adjustedTargetHits = min(targetHits / estimatedFilterHitRatio, targetHits * targetHitsMaxAdjustmentFactor).
```

Use [target-hits-max-adjustment-factor](#target-hits-max-adjustment-factor) to control the upper bound of the adjusted _targetHits_.

This parameter has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

 |
| approximate-threshold | Zero or one | 

Threshold value (in the range [0.0, 1.0]) deciding if a query with an approximate [nearestNeighbor](../querying/yql.html#nearestneighbor) operator combined with filters is evaluated by searching the [HNSW](schemas.html#index-hnsw) graph for approximate neighbors with filtering, or performing an [exact nearest neighbor search](../../querying/nearest-neighbor-search) with pre-filtering. The fallback to exact search is chosen when the estimated filter hit ratio of the query is _less_ than this threshold. The default value is 0.05. See [Controlling the filtering behavior with approximate nearest neighbor search](https://blog.vespa.ai/constrained-approximate-nearest-neighbor-search/#controlling-the-filtering-behavior-with-approximate-nearest-neighbor-search) for more details.

This parameter has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

 |
| filter-first-threshold | Zero or one | 

Threshold value (in the range [0.0, 1.0]) deciding if the filter is checked before computing a distance (_filter-first heuristic_) while searching the [HNSW](schemas.html#index-hnsw) graph for approximate neighbors with filtering. This improves the response time at low hit ratios but causes a dip in recall. The heuristic is used when the estimated filter hit ratio of the query is _less_ than this threshold. The default value is 0.0.

This parameter has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

 |
| filter-first-exploration | Zero or one | 

Value (in the range [0.0, 1.0]) specifying how aggressively the filter-first heuristic explores the graph when searching the [HNSW](schemas.html#index-hnsw) graph for approximate neighbors with filtering. A higher value means that the graph is explored more aggressively and improves the recall at the cost of the response time. The default value is 0.3.

This parameter has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

 |
| exploration-slack | Zero or one | 

Value (in the range [0.0, 1.0]) specifying slack to delay the termination of the search of the [HNSW](schemas.html#index-hnsw) graph for approximate neighbors with or without filtering. A higher value means that more of the graph is explored and improves the recall at the cost of the response time. The default value is 0.0.

This parameter has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

 |
| target-hits-max-adjustment-factor | Zero or one | 

Value (in the range [1.0, inf]) used to control the auto-adjustment of [targetHits](../querying/yql.html#targethits) used when evaluating an approximate [nearestNeighbor](../querying/yql.html#nearestneighbor) operator with post-filtering. The default value is 20.0.

Setting this value to 1.0 disables auto-adjustment of _targetHits_. See [post-filter-threshold](#post-filter-threshold) for more details.

This parameter has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

 |
| filter-threshold | Zero or one | 

The threshold value (in the range [0.0, 1.0]) deciding when matching in _index_ fields should be treated as filters. This happens for query terms with [estimated hit ratios](../../learn/glossary.html#estimated-hit-ratio) (in the range [0.0, 1.0]) that are above the _filter-threshold_. Use this to optimize query performance when searching large text [index](../../basics/schemas.html#document-fields) fields, by allowing a per query combination of [rank: filter](#filter) and [rank: normal](#normal) behavior. This parameter can be overridden per _index_ field, see [field-level filter-threshold](#rank-filter-threshold) for a more detailed description with tradeoffs.

In testing with various text datasets (e.g., Wikipedia), a _filter-threshold_ setting of 0.05 has been shown to be a good starting point. See [Tuning query performance for lexical search](../../performance/feature-tuning.html#tuning-query-performance-for-lexical-search) for more details.

This parameter has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

Use the [ranking.matching.filterThreshold](/en/reference/api/query.html#ranking.matching.filterThreshold) query parameter to override this value.

 |
| [rank](#rank) | Zero or more | Specify rank settings of a field in this profile. |
| [rank-type](#rank-type) | Zero or more | The rank-type of a field in this profile. |
| [weakand](#weakand) | Zero or one | 

Tunes the [weakAnd](../../ranking/wand.html#weakand) algorithm to automatically exclude terms and documents with expected low query significance based on [document frequency](../../learn/glossary.html#document-frequency-normalized) statistics present in the document corpus. This makes matching faster at the cost of potentially reduced recall.

 |
| [rank-profile (inner)](#rank-profile) | Zero or more | 

An inner rank profile, useful for grouping related profiles, especially when defined in separate .profile files. This behaves just like a top level rank profile, except that:

- The full name of the profile to use in queries will be `containing-profile-name.inner-profile-name`.
- The profile must explicitly inherit the containing profile.

 |

## match-phase

Contained in [rank-profile](#rank-profile). The match-phase feature lets you increase performance by limiting hits exposed to first-phase ranking to the highest (lowest) values of some attribute. The performance gain may be substantial, especially with an expensive first-phase function. The quality loss depends on how well the chosen attribute correlates with the first-phase score.

Documents that have no value of the chosen attribute will be taken as having the value 0.

See also [graceful degradation](../../performance/graceful-degradation.html#match-phase-degradation) and [result diversity](../../querying/result-diversity#match-phase-diversity).

```
match-phase {
    attribute: [numeric single value attribute]
    order: [ascending | descending]
    max-hits: [integer]
}
```

| Name | Description |
| --- | --- |
| attribute | 

The quality attribute that decides which documents are a match if the match phase estimates that there will be more than [max-hits](#match-phase-max-hits) hits. The attribute must be single-value numeric with [fast-search](#attribute) enabled. It should correlate with the order which would be produced by a full query evaluation. No default.

 |
| order | 

Whether the attribute should be used in `descending` order (prefer documents with a high value) or `ascending` order (prefer documents with a low value). Usually, it is not necessary to specify this, as the default value `descending` is by far the most common.

 |
| max-hits | 

The max hits each content node should attempt to produce in the match phase. Usually, a number like 10000 works well here.

 |

## strict

Contained in [rank-profile](#rank-profile). True or false. By default, Vespa uses loose type checking, where any query feature used but not defined in a query profile type is assumed to be a float. Set true to cause a deploy failure on missing query property type definitions instead.

```
strict: true
```

## diversity

Contained in [rank-profile](#rank-profile). Diversity is used to guarantee diversity in the different query phases. If you have [match-phase](#match-phase), it will provide diverse results from match-phase to first-phase. If you have [second-phase](#secondphase-rank), it will provide diverse results from first-phase to second-phase.

Read more about this in [result diversity](../../querying/result-diversity).

Specify the name of an attribute that will be used to provide diversity. Result sets are guaranteed to get at least [min-groups](#diversity-min-groups)unique values from the [diversity attribute](#diversity-min-groups) from this phase, but no more than max-hits. For [match-phase](#match-phase) max-hits = [match-phase max-hits](#match-phase-max-hits). For [second-phase](#secondphase-rank) max-hits = [rerank-count](#secondphase-rerank-count)A document is considered a candidate if:

- The query has not yet reached the _max-hits_ number produced from this phase.
- The query has not yet reached the max number of candidates in one group. This is computed by the _max-hits_ of the phase divided by [min-groups](#diversity-min-groups)

```
diversity {
    attribute: [attribute name]
    min-groups: [integer]
}
```

| Name | Description |
| --- | --- |
| attribute | 

Which attribute to use when deciding diversity. The attribute must be a single-valued numeric, string or [reference](#reference) type.

 |
| min-groups | 

Specifies the minimum number of groups returned from the phase. Using this with [match-phase](#match-phase) often means one can reduce [max-hits](#match-phase-max-hits). In [second-phase](#secondphase-rank) you might reduce [rerank-count](#secondphase-rerank-count) and still good and diverse results.

 |

## first-phase

Contained in [rank-profile](#rank-profile). The config specifying the first phase of ranking. See [phased ranking with Vespa](../../ranking/phased-ranking.html). This is the initial ranking performed on all matching documents; you should therefore avoid doing computationally expensive relevancy calculations here. By default, this will use the ranking feature `nativeRank`.

```
first-phase {
    [body]
}
```
The body of a first-phase ranking statement consists of:

| Name | Description |
| --- | --- |
| [expression](#expression) | 

Specify the ranking expression to be used for the first phase of ranking - see [ranking expressions](../ranking/ranking-expressions.html).

 |
| keep-rank-count | 

How many documents to keep the first phase top rank values for. The default value is 10000.

 |
| rank-score-drop-limit | 

Drop all hits with a first-phase rank score less than or equal to this floating-point number. Use this to implement a rank cutoff. Default is `-Double.MAX_VALUE`

 |

## expression

Contained in [first-phase](#firstphase-rank) or[second-phase](#secondphase-rank) or[global-phase](#globalphase-rank). Specify a [ranking expression](../ranking/ranking-expressions.html). The expression can either be written directly or loaded from a file. When writing it directly, the syntax is:

```
expression: [ranking expression]
```
or
```
expression {
    [ranking expression]
    [ranking expression]
    [ranking expression]
}
```

The second format is primarily a convenience feature when using long expressions, enabling them to be split over multiple lines.

Expressions can also be loaded from a separate file. This is useful when dealing with the long expressions generated by e.g. MLR. The syntax is:

```
expression: file:[path-to-expressionfile]
```

The path is relative to the location of the schema definition file. The file itself must end with `.expression`. This suffix is optional in the schema. Therefore `expression: file:mlrranking.expression` and`expression: file:mlrranking` are identical. Both refer to a file called `mlrranking.expression` in the _schemas_ directory.

 **Note:** Directories are not allowed in the path.

## rank-features

Contained in [rank-profile](#rank-profile). List of extra [rank features](../ranking/rank-features.html) to be dumped when using the query-argument [rankfeatures](../api/query.html#ranking.listfeatures).

```
rank-features: [feature] [feature]
```
or
```
rank-features {
    [feature]
    [feature]
}
```

Any number of ranking features can be listed on each line, separated by space.

## inputs

Contained in [rank-profile](#rank-profile). List of inputs: Query features consumed by ranking expressions in this profile.

Query features are set either as a [request property](../api/query.html#ranking.features), or equivalently from a [Searcher](../../applications/searchers.html), by calling`query.getRanking().getFeatures().put("query(myInput)", myValue)`.

Query feature types can also be declared in[query profile types](../../querying/query-profiles.html#query-profile-types), but declaring inputs in the profile needing them is usually preferable.

Inputs are inherited from inherited profiles.

```
inputs {
    name [type]? (: value)?
}
```

| Name | Description |
| --- | --- |
| name | The name of the inputs, written either the full feature name `query(myName)`, or just as `name`. |
| type | The type of the constant, either `double` or a [tensor type](../ranking/tensor.html#tensor-type-spec). If omitted, the type is double. |
| value | An optional default module, used if this input is not set in the query. A number, or a [tensor on literal form](../ranking/tensor.html#tensor-literal-form). |

Input examples:

```
inputs {
    myDouble: 0.5
    query(myOtherDouble) double
    query(myArray) tensor(x[3])
    query(myMap) tensor(key{}):{key1: 1.0, key2: 2.0}
}
```

## constants

Contained in [rank-profile](#rank-profile). List of constants available in ranking expressions, resolved and optimized at configuration time.

Constants are inherited from inherited profiles, and from the schema itself.

```
constants {
    name [type]?: value|file:[path]
}
```

| Name | Description |
| --- | --- |
| name | The name of the constant, written either the full feature name `constant(myName)`, or just as `name`. |
| type | The type of the constant, either `double` or a [tensor type](../ranking/tensor.html#tensor-type-spec). If omitted, the type is double. |
| value | A number, a [tensor on literal form](../ranking/tensor.html#tensor-literal-form), or `file:` followed by a path from the application package root to a file containing the constant. The file must be stored in a valid [tensor JSON Format](../ranking/constant-tensor-json-format.html)and end with `.json`. The file may be lz4 compressed, in which case the ending must be`.json.lz4`. |

Constant examples:

```
constants {
    myDouble: 0.5
    constant(myOtherDouble) double: 0.6
    constant(myArray) tensor(x[3]):[1, 2, 3]
    constant(myMap) tensor(key{}]):{key1: 1.0, key2: 2.0}
    constant(myLargeTensor) tensor(x[10000]): file:constants/myTensor.json.lz4
}
```

## rank-properties

Contained in [rank-profile](#rank-profile). List of generic properties, in the form of key/value pairs to be used by ranking features.[Examples](../ranking/rank-feature-configuration.html).

```
rank-properties {
    key: value
}
```

| Name | Description |
| --- | --- |
| key | Name of the property. |
| value | A number or any string. Must be quoted if it contains spacing. |

## function (inline)? [name]

Contained in [rank-profile](#rank-profile). Define a named function that can be referenced as a part of the ranking expression, or (if having no arguments) as a feature. A function accepts any number of arguments.

```
function [name]([arg1], [arg2], [arg3]) {
    expression: …
}
```
or
```
function [name] ([arg1], [arg2], [arg3]) {
    expression {
        [ranking expression]
        [ranking expression]
        …
}
```
Note that the parenthesis is required after the name. A rank-profile example is shown below:
```
rank-profile default inherits default {
    function myfeature() {
        expression: fieldMatch(title) + freshness(timestamp)
    }
    function otherfeature(foo) {
        expression{ nativeRank(foo, body) }
    }

    first-phase {
        expression: myfeature * 10
    }
    second-phase {
        expression: otherfeature(title) * myfeature
    }
    summary-features: myfeature
}
```

You can not include functions that accept arguments in summary features.

Adding the `inline` modifier will inline this function in the calling expression if it also has no arguments. This is faster for small and cheap functions (and more expensive for others).

## second-phase

Contained in [rank-profile](#rank-profile). The config specifying the second phase of ranking. See [phased ranking with Vespa](../../ranking/phased-ranking.html). This is the optional re-ranking phase performed on the top-ranking hits from the`first-phase`, and where you should put any advanced relevancy calculations. For example Machine Learned Ranking (MLR) models. By default, no second-phase ranking is performed.

```
second-phase {
    [body]
}
```
The body of a secondphase-ranking statement consists of:

| Name | Description |
| --- | --- |
| [expression](#expression) | 

Specify the ranking expression to be used for the second phase of ranking. (for a description, see the [ranking expression](../ranking/ranking-expressions.html) documentation.

Hits not reranked might be re-scored using a linear function to avoid a greater rank score than the worst reranked hit. This linear function will normally attempt to map the first phase rank score range of reranked hits to the reranked rank score range

 |
| rank-score-drop-limit | 

When set, drop all hits with a second phase rank score (possibly a [re-scored](#secondphase-rescoring) rank score) less than or equal to this floating point number. Use this to implement a second-phase rank cutoff. By default, this value is not set. This can also be [set in the query](../api/query.html#ranking.secondphase.rankscoredroplimit).

 |
| rerank-count | 

Optional argument. Specifies the number of hits to be re-ranked in the second phase. The default value is 100. This can also be [set in the query](../api/query.html#ranking.rerankcount). Note that this value is local to each node involved in a query. Hits not reranked might be [re-scored](#secondphase-rescoring).

 |

## global-phase

Contained in [rank-profile](#rank-profile). The config specifying the global phase of ranking. See [phased ranking with Vespa](../../ranking/phased-ranking.html). This is an optional re-ranking phase performed on the top-ranking hits in the stateless container after merging hits from all the content nodes. The "top ranking" here means as scored by the first-phase ranking expression or (if specified) second-phase ranking expression. Typically used for computing large ONNX models, which would be expensive to compute on all content nodes. By default, no global-phase ranking is performed.

```
global-phase {
    [body]
}
```
The body of a global-phase ranking statement consists of:

| Name | Description |
| --- | --- |
| [expression](#expression) | Specify the ranking expression to be used for the global phase of ranking. (for a description, see the [ranking expression](../ranking/ranking-expressions.html) documentation. |
| rerank-count | 

Optional argument. Specifies the number of hits to be re-ranked in the global phase. The default value is 100. Note for complex setups: Applied to hits from one schema at a time, so if a query searches in multiple schemas simultaneously, global-phase may run for 100 hits per schema as default.

 |
| rank-score-drop-limit | 

When set, drop all hits with a global phase rank score (possibly a [re-scored](#globalphase-rank) rank score) less than or equal to this floating point number. Use this to implement a global phase rank cutoff. By default, this value is not set. This can also be [set in the query](../api/query.html#ranking.globalphase.rankscoredroplimit).

 |

## summary-features

Contained in [rank-profile](#rank-profile). List of [rank features](../ranking/rank-features.html) to be included with each result hit, in the [summaryfeatures](../querying/default-result-format.html#summaryfeatures) field. Also see [feature values in results](../../ranking/ranking-expressions-features.html#accessing-feature-function-values-in-results).

If not specified, the features are as specified in the parent profile (if any). To inherit the features from the parent profile _and_ specify additional features, specify explicitly that the features should be inherited from the parent, as shown below. Refer to [schema inheritance](/en/schemas/inheritance-in-schemas.html) for examples.

The rank features specified here are computed in the [fill phase](../../applications/searchers.html#multiphase-searching) of multiphased queries.

 **Note:** Rank-features references in _summary-features_are **re-calculated** during the _fill protocol phase_for the hits which made it into the global top ranking hits (from all nodes). See [match-features](#match-features) for an alternative.

```
summary-features: [feature] [feature]…
```

or

```
summary-features [inherits parent-profile (, other-parent-profile)*]? {
    [feature]
    [feature]
}
```

Any number of rank features separated by space can be listed on each line.

 **Note:** Note that compound expressions must be wrapped in a [function](https://docs.vespa.ai/en/ranking-expressions-features.html#accessing-feature-function-values-in-results) to be accessible by match/summary-features. 

## match-features

Contained in [rank-profile](#rank-profile). List of [rank features](../ranking/rank-features.html) to be included with each result hit, in the [matchfeatures](../querying/default-result-format.html#matchfeatures) field. Also see [feature values in results](../../ranking/ranking-expressions-features.html#accessing-feature-function-values-in-results).

If not specified, the features are as specified in the parent profile (if any). To inherit the features from the parent profile _and_ specify additional features, specify explicitly that the features should be inherited from the parent as shown below, also see [schema inheritance](/en/schemas/inheritance-in-schemas.html).

To disable match-features from parent rank profiles, use `match-features {}`.

_match-features_ is similar to [summary-features](#summary-features), but the rank features specified here are computed in the _first protocol phase_ of [multiprotocol query execution](../../applications/searchers.html#multiphase-searching), also called the _match_ protocol phase. This gives a different performance trade-off, for details, see [feature values in results](../../ranking/ranking-expressions-features.html#accessing-feature-function-values-in-results).

```
match-features: [feature] [feature]…
```

or

```
match-features [inherits parent-profile (, other-parent-profile)*]? {
    [feature]
    [feature]
}
```

Any number of ranking features separated by space can be listed on each line.

 **Note:** Note that compound expressions must be wrapped in a [function](https://docs.vespa.ai/en/ranking-expressions-features.html#accessing-feature-function-values-in-results) to be accessible by match/summary-features. 

## mutate

Contained in [rank-profile](#rank-profile). Specifies mutating operations you can do to each of the documents that make it through the 4 query phases,_on-match_, _on-first-phase_, _on-second-phase_ and _on-summary_.

```
mutate {
    [phase name] { [attribute name] [operation] [numeric_value] }
}
```
The phases are:

| Name | Description |
| --- | --- |
| on-match | 

All documents that satisfy the query.

 |
| on-first-phase | 

All documents from [on-match](#on-match), and is not dropped due the optional [rank-score-drop-limit](#rank-score-drop-limit)

 |
| on-second-phase | 

All documents from [on-first-phase](#on-first-phase) that makes it onto the [second-phase](#secondphase-rank) heap.

 |
| on-summary | 

All documents where are a summary is requested.

 |

The attribute must be a single value numeric attribute, enabled as [mutable](#mutable). It must also be defined outside the [document](#document) clause.

| Operation | Description |
| --- | --- |
| = | 

Set the value of the attribute to the given value.

 |
| += | 

Add the given value to the attribute

 |
| -= | 

Subtract the given value from the attribute

 |

Find examples and use cases in [rank phase statistics](../../ranking/phased-ranking.html#rank-phase-statistics).

## constant

_Prefer to define constants in the rank profiles that need them, with rank profile inheritance to avoid repetition. See [constants](#constants)._

Contained in [schema](#schema). This defines a named constant tensor located in a file with a given type that can be used in ranking expressions using the rank feature[constant(name)](../ranking/rank-features.html#constant(name)):

```
constant [name] {
    [body]
}
```
The body of a constant must contain:

| Name | Description | Occurrence |
| --- | --- | --- |
| file | Path to the file containing this constant, relative to the application package root. The file must be stored in a valid [tensor JSON Format](../ranking/constant-tensor-json-format.html) and end with `.json`. The file may be lz4 compressed, in which case the ending must be `.json.lz4`. | One |
| type | The type of the constant tensor, refer to [tensor-type-spec](../ranking/tensor.html#tensor-type-spec) for reference. | One |

Constant tensor example:
```
constant my_constant_tensor {
    file: constants/my_constant_tensor_file.json
    type: tensor<float>(x{},y{})
}
```
This example has a constant tensor with two mapped dimensions, `x` and `y`:
```
{
    "cells": [
        { "address": { "x": "a", "y": "b"}, "value": 2.0 },
        { "address": { "x": "c", "y": "d"}, "value": 3.0 }
    ]
}
```

When an application with tensor constants is deployed, the files are distributed to the content nodes before the new configuration is used by the search nodes. Incremental changes to constant tensors are not supported. When changed, replace the old file with a new one and redeploy the application, or create a new constant with a new name in a new file.

## raw-as-base64-in-summary

Contained in [schema](#schema). Whether raw fields should be rendered as a base64 encoded string in summary, the same way as in [json feed format](document-json-format.html#raw), rather than an escaped string. This is by default true.

## onnx-model

Contained in [rank-profile](#rank-profile) or [schema](#schema). This defines a named ONNX model located in a file that can be used in ranking expressions using the "onnx" rank feature.

Prefer to define onnx models in the rank profiles using them. Onnx models are inherited from parent profiles and from the schema.

```
onnx-model [name] {
    [body]
}
```

The body of an ONNX model must contain:

| Name | Occurrence | Description |
| --- | --- | --- |
| file | One | Path to the location of the file containing the ONNX model. The path is relative to the root of the application package containing this schema. |
| input | Zero to many | An input to the ONNX model. The ONNX name, as given in the model, as well as the source for the input, is specified. |
| output | Zero to many | An output of the ONNX model. The ONNX name, as given in the model, as well as the name for use in Vespa, is specified. If no output is defined and is not referred to from the rank feature, the first output defined in the model is used. |
| gpu-device | Zero or one | Set the GPU device number to use for computation, starting at 0, i.e. if your GPU is `/dev/nvidia0` set this to 0. This must be an Nvidia CUDA-enabled GPU. Currently only models used in [global-phase](#globalphase-rank) can make use of GPU-acceleration. |
| intraop-threads | Zero or one | The number of threads available for running operations with multithreaded implementations. |
| interop-threads | Zero or one | The number of threads available for running multiple operations in parallel. This is only applicable for `parallel` execution mode. |
| execution-mode | Zero or one | Controls how the operators of a graph are executed, either `sequential` or `parallel`. |

For more details including examples, see [ranking with ONNX models.](../../ranking/onnx)

## significance

Contained in [rank-profile](#rank-profile). Configures a [significance model](../../ranking/significance).

```
significance {
    use-model: true
}
```

The body must contain:

| name | occurrence | description |
| --- | --- | --- |
| use-model | One | Enable or disable the use of significance models specified in [service.xml](../applications/services/search.html#significance). |

For more details see [Significance Model.](../../ranking/significance)

## document-summary

Contained in [schema](#schema). An explicitly defined document summary. By default, a document summary named `default` is created. Using this element, other document summaries containing a different set of fields can be created.

```
document-summary [name] inherits [document-summary1], [document-summary2], ... {
    [body]
}
```

The `inherits` attribute is optional. If defined, it contains the name of other document summaries in the same schema (or a parent) which this summary should inherit the fields of. Refer to [schema inheritance](../../schemas/inheritance-in-schemas.html) for examples.

The body of a document summary consists of:

| Name | Occurrence | Description |
| --- | --- | --- |
| from-disk | Zero or one | Mark this summary as accessing fields on disk. This will silence the warnings that this summary reads from disk; in the console for prod deployments, on the command line for manual deployments. Read more in [Document Summaries](/en/querying/document-summaries.html#performance) on how to avoid disk access to speed up queries. |
| [summary](#summary) | Zero to many | A summary field in this document summary. |
| omit-summary-features | Zero or one | Specifies that [summary-features](#summary-features) should be omitted from this document summary. Use this to reduce CPU cost in [multiphase searching](../../applications/searchers.html#multiphase-searching) when using multiple document summaries to fill hits, and only some of them need the summary features that are specified in the [rank-profile](#rank-profile). |

Use the [summary](../api/query.html#presentation.summary) query parameter to choose a document summary in searches or in [grouping](/en/reference/querying/grouping-language.html#summary). See also [document summaries](../../querying/document-summaries.html).

## stemming

Contained in [field](#field),[schema](#schema) or[index](#index). Sets how to stem a field or an index, or how to stem by default. Read more on [stemming](../../linguistics/linguistics.html#stemming).

```
stemming: [stemming-type]
```
The stemming types are:

| Type | Description |
| --- | --- |
| none | No stemming: Keep words unchanged |
| best | Use the 'best' stem of each word according to some heuristic scoring. This is the default setting |
| shortest | Use the shortest stem of each word |
| multiple | Use multiple stems. Retains all stems returned from the linguistics library |

 **Note:** When combining multiple fields in a [fieldset](#fieldset), all fields should use the same stemming type.

## normalizing

Contained in [field](#field). Sets [normalizing](../../linguistics/linguistics.html#normalization) to be done on this field. The default is to normalize.

```
normalizing: [normalizing-type]
```

| Type | Description |
| --- | --- |
| none | No normalizing. |

## dictionary

Contained in [field](#field), and specifies details of the dictionary used in the inverted index of the field. Applies only to [attributes](#attribute) annotated with `fast-search`. You can specify either `btree` or `hash`, or both.

### Dictionary Types

**btree** (Default): Provides good performance for exact, prefix, and range lookups. Recommended for most use cases. Find more details in [attribute index structures](../../content/attributes.html#index-structures).

**hash**: Optimized for fields with high cardinality (many unique values), such as unique ID fields where each posting list contains only one item.

 **Note:** When using `hash`, prefix searches for strings and range searches for numeric fields will fall back to a full scan. This is primarily beneficial when you have many unique terms with few occurrences each, where dictionary lookup costs would otherwise be significant. 

### Case Handling for String Fields

For string attributes, you can specify how character case is handled:

- **uncased** (Default): Case-insensitive - 'bear', 'Bear', and 'BEAR' are treated as identical
- **cased**: Case-sensitive - 'bear', 'Bear', and 'BEAR' are treated as different terms

This setting is automatically checked against the field's [match:casing](#match) setting.

### Important Rules for String Fields with Dictionaries

**For `btree` dictionaries**: Both `cased` and `uncased` options are supported.

**For `hash` dictionaries**: Only `cased` is supported for string fields. When using `hash` dictionaries:

- You **must** set `match: cased` on the field
- You **must** include `cased` in the dictionary block

```
dictionary {
  hashcased}
```

### Example: Case-Sensitive Hash Dictionary

```
field id_str type string {
      indexing: summary | attribute
      attribute: fast-searchmatch: casedrank: filter
      dictionary {
        hashcased}
}
```

## attribute

Contained in [field](#field) or[struct-field](#struct-field). Specifies a property of an index structure attribute:

```
attribute [attribute-name]: [property]
```
or
```
attribute [attribute-name] {
    [property]
    [property]
    …
}
```
Read the [introduction to attributes](../../content/attributes.html). If the attribute name is specified, it will be used instead of the field name as the name of the attribute.
 **Deprecated:** Deprecated, use a field with the wanted name outside the document instead.
Actions required when [adding or modifying attributes](#modifying-schemas). Properties:

| Property | Description |
| --- | --- |
| fast-search | Create a dictionary/index structure to speed up search in the attribute. [Read more](../../content/attributes.html#index-structures). |
| fast-access | If [searchable-copies](../applications/services/content.html#searchable-copies) \< [redundancy](../applications/services/content.html#redundancy), use _fast-access_ to load the attribute in memory on all nodes with a document replica. Use this for fast access when doing [partial updates](../../writing/reads-and-writes.html) and when used in a [selection expression](../applications/services/content.html#documents) for garbage collection. If [searchable-copies](../applications/services/content.html#searchable-copies) == [redundancy](../applications/services/content.html#redundancy) (default), this property is a no-op. [Read more](../../performance/sizing-feeding.html#redundancy-settings). |
| fast-rank | Only supported for [tensor](../../ranking/tensor-user-guide.html) field types with at least one mapped dimension. Ensures that the per-document tensors are stored in-memory using a format that is more optimal for [ranking expression](../ranking/ranking-expressions.html) evaluation. This comes at the cost of using more memory. Without this setting, these tensors are serialized in-memory, which requires deserialization as part of ranking expression evaluation. See [tensor performance](../../performance/feature-tuning.html#tensor-ranking). |
| paged | This can reduce the memory footprint by allowing paging the attribute data out of memory to disk. Not supported for [tensor](#tensor) with fast-rank and [predicate](#predicate) types. See [paged attributes](../../content/attributes.html#paged-attributes) for details. Do not enable _paged_ before fully understanding the consequences. |
| [sorting](#sorting) | The sort specification for this attribute. |
| [distance-metric](#distance-metric) | Specifies the distance metric to use with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator. Only relevant for tensor attribute fields. |
| mutable | 

Marks the attribute as a special mutable attribute that can be updated by a [mutate](#mutate) operation during query evaluation.

 |

An attribute is [multivalued](../../querying/searching-multivalue-fields)if assigning it multiple values during indexing, by using a multivalued field type like array or map, or by using e.g. [split](../writing/indexing-language.html#split) /[for\_each](../writing/indexing-language.html#for_each)or by letting multiple fields write their value to the attribute field.

Note that [normalizing](#normalizing) and[tokenization](../../linguistics/linguistics.html#tokenization)is not supported for attribute fields.

Queries in attribute fields are not normalized, nor stemmed. Use [index](#index) on fields to enable. Both _index_ and _attribute_ can be set on a field.

## sorting

Contained in [attribute](#attribute) or[field](#field). Specifies how sorting should be done.

```
sorting : [property]
```
or
```
sorting {
    [property]
    …
}
```

| Property | Description |
| --- | --- |
| order | `ascending` (default) or `descending`. Used unless overridden using [order by](../querying/yql.html#function) in query. |
| function | [Sort function](../querying/yql.html#function): `uca` (default), `lowercase` or `raw`. Note that if no language or locale is specified in the query, the field, or generally for the query, `lowercase` will be used instead of `uca`. See [order by](../querying/yql.html#order-by) for details. |
| strength | [UCA sort strength](../querying/yql.html#strength), default `primary` - see [strength](../querying/yql.html#strength) for values. Values set in the query override the schema definition. |
| locale | [UCA locale](../querying/yql.html#locale), default none, indicating that it is inferred from the query. It should only be set here if the attribute is filled with data in one language only. See [locale](../querying/yql.html#locale) for details. Values set in the query override the schema definition. |

## distance-metric

Specifies the distance metric to use with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator to calculate the distance between document positions and the query position. Only relevant for tensor attribute fields, where each tensor holds one or multiple vectors.

Which distance metric to use depends on the model used to produce the vectors; it must match the distance metric used during representation learning (model learning). If you are using an "off-the-shelf" model to vectorize your data, please ensure that the distance metric matches the distance metric suggested for use with the model. Different types of vectorization models use different types of distance metrics.

 **Important:** When changing the `distance-metric` or `max-links-per-node`, the content nodes must be restarted to rebuild the HNSW index - see[changes that require restart but not re-feed](#changes-that-require-restart-but-not-re-feed)

The calculated distance will be used to select the closest hits for _nearestNeighbor_ query operator, but also to build the [HNSW](../../querying/approximate-nn-hnsw) index (if specified) and to produce the [distance](../ranking/rank-features.html#distance(dimension,name)) and [closeness](../ranking/rank-features.html#closeness(dimension,name)) ranking features.

```
distance-metric: [metric]
```
These are the available metrics; the expressions given for _distance_ and _closeness_assume a query vector _qv = [x0, x1, ...]_ and an attribute vector _av = [y0, y1, ...]_with same dimension of size _n_ for all vectors.

| Metric | Description | distance | closeness |
| --- | --- | --- | --- |
| euclidean | The normal [euclidean](#euclidean) (aka L2) distance. | d=∑n(xi-yi)2 with range: `[0,inf)` | 1.01.0+d |
| angular | The [angle](#angular) between _qv_ and _av_ vectors. | d=cos-1(q→⋅a→| q→ |⋅| a→ |) with range: `[0,pi]` | 1.01.0+d |
| dotproduct | Used for [maximal inner product search](#dotproduct). | d=-(q→⋅a→) with range: `[-inf,+inf]` | -d=q→⋅a→ |
| prenormalized-angular | Assumes normalized vectors, see [note](#prenormalized-angular) below. | d=1.0-(q→⋅a→| q→ |2) with range: `[0,2]` | 1.01.0+d |
| geodegrees | Assumes geographical coordinates, see [note](#geodegrees) below. | d= great-circle in km; range: `[0,20015]` | 1.01.0+d |
| hamming | Only useful for binary tensors using \<int8\> precision, see [note](#hamming) below. | d=∑npopcount(xiXORyi) ; range: `[0,8*n]` | 1.01.0+d |

### euclidean

The default metric is [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) which is just the length of a line segment between the two points. To compute the Euclidean distance directly in a ranking expression instead of fetching one already computed in a nearestNeighbor query operator, use the [Euclidean\_distance helper function](../ranking/ranking-expressions.html#euclidean-distance-t):

```
function mydistance() {
        expression: euclidean_distance(attribute(myembedding), query(myqueryvector), mydim))
    }
```

### angular

The _angular_ distance metric computes the _angle_ between the vectors. Its range is `[0,pi]`, which is the angular distance. This is also known as ordering by [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) where the score function is just the cosine of the angle. To compute the angular distance directly in a ranking expression, use the [cosine\_similarity helper function](../ranking/ranking-expressions.html#cosine-similarity-t):

```
function angle() {
        expression: acos(cosine_similarity(attribute(myembedding), query(myqueryvector), mydim))
    }
```
 Conversely, the cosine similarity can be recovered from the [distance rank-feature](../ranking/rank-features.html#distance(dimension,name)) when using a nearestNeighbor query operator:
```
rank-profile cosine {
        first-phase {
            expression: cos(distance(field, myembedding))
        }
    }
```
 If possible, it's slightly better for performance to normalize both query and document vectors to the same L2 norm and use the `prenormalized-angular` metric instead; but note that returned distance and closeness will be different.
### dotproduct

The _dotproduct_ distance metric is used to _mathematically transform_ a "maximum inner product" search into a form where it can be solved by nearest neighbor search, where the dotproduct is used as a score directly (large positive dotproducts are considered "nearby"). Internally, an extra dimension is added (ensuring that all vectors are normalized to the same length) and a distance similar to _prenormalized-angular_ is used to build the HNSW index. For details, see [this high level guide](https://towardsdatascience.com/maximum-inner-product-search-using-nearest-neighbor-search-algorithms-c125d24777ef) based on [section 3.1 Order Preserving Transformations in this paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/XboxInnerProduct.pdf).

Note that the _distance_ and _closeness_ rank-features will not have the usual semantic meanings when using the _dotproduct_ distance metric. In particular, _closeness_ will just return the dot product ∑n(xi\*yi) which may have any negative or positive value, and _distance_ is just the negative dot product. If a normalized closeness in range `[0,1]` is needed, an appropriate [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) must be applied. For example, if your attribute is named "foobar", and the maximum dotproduct seen is around 4000, the expression `sigmoid(0.001*closeness(field,foobar))` could be a possible choice.

The _dotproduct_ distance metric is useful for some vectorization models, including matrix factorization, that use "maximum inner product" (MIP), with vectors that aren't normalized. These models use both direction and magnitude.

### prenormalized-angular

The _prenormalized-angular_ distance metric **must only be used** when **both** query and document vectors are normalized. This metric was previously named "innerproduct" and required unit-length vectors. The new version computes the length of the query vector once and assumes all other vectors are of the same length.

Using _prenormalized-angular_ with vectors that are not normalized causes unpredictable nearest neighbor search, and is observed to give bad results both for performance and quality.

The length, magnitude, or norm of a vector _x_ is calculated as `length = sqrt(sum(pow(xi,2)))`. The unit length normalized vector is then given by `[xi/length]`. Zero vectors may not be used at all.

The Vespa _prenormalized-angular_ computes the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) and uses `1.0 - cos(angle)` as the distance metric. It gives exactly the same ordering as `angular` distance, but with a distance in the range [0,2], since cosine similarity has range [1,-1], so the end result is 0.0 for same direction vectors, 1.0 for a right angle, and 2.0 for vectors with exactly opposite directions. Getting the cosine score (or angle) is therefore easy:

```
rank-profile cosine {
        first-phase {
          expression: 1.0 - distance(field, embedding)
        }
        function angle() {
          expression: acos(1.0 - distance(field, embedding))
        }
    }
```
 To compute the cosine similarity directly in a ranking expression instead of fetching one already computed in a nearestNeighbor query operator, use the [cosine\_similarity helper function](../ranking/ranking-expressions.html#cosine-similarity-t):
```
function mysimilarity() {
        expression: cosine_similarity(attribute(myembedding), query(myqueryvector), mydim))
    }
```

### geodegrees

The _geodegrees_ distance metric is only valid for geographical coordinates (two-dimensional vectors containing latitude and longitude on Earth, in degrees). It computes the great-circle distance (in kilometers) between two geographical points using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula). See [geodegrees system test](https://github.com/vespa-engine/system-test/blob/master/tests/search/nearest_neighbor/geo.sd) for an example.

### hamming

The [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) metric counts the number of dimensions where the vectors have different coordinates. This isn't useful for floating-point data since it means you only get 1 bit of information from each floating-point number. Instead, it should be used for binary data, where each bit is considered a separate coordinate. Practically, this means you should use the `int8` [cell value type](../../performance/feature-tuning.html#cell-value-types) for your tensor, with the usual encoding from bit pattern to numerical value, for example:

- `00000000` → `0` (hex `00`)
- `00010001` → `17` (hex `11`)
- `00101010` → `42` (hex `2A`)
- `01111111` → `127` (hex `7F`)
- `10000000` → `-128` (hex `80`)
- `10000001` → `-127` (hex `81`)
- `11111110` → `-2` (hex `FE`)
- `11111111` → `-1` (hex `FF`)

Feeding data for this use case may be done with ["hex dump"](document-json-format.html#tensor-hex-dump) format instead of numbers in range `[-128,127]` both to have a more natural format for representing binary data, and to avoid the overhead of parsing a large JSON array of numbers.

## bolding

Contained in [field](#field) or [summary](#summary). Highlight matching query terms in the [summary](#summary):

```
bolding: on
```

The default is no bolding, set `bolding: on` to enable it. Note that this command is overridden by `summary: dynamic`. If both are specified, bolding will be ignored. The difference between using bolding instead of `summary: dynamic` is the latter will provide a dynamic abstract in addition to highlighting query terms, while the first only highlights. Bolding is only supported for [index](#indexing-index) fields of type string or array\<string\>.

The default XML element used to highlight the search terms is \<hi\> - to override, set _container.qr-searchers_ configuration. Example using `<strong>`:

```
```
<container>
    <search>
        <config name="container.qr-searchers">
            <tag>
                <bold>
                    <open>&lt;strong&gt;</open>
                    <close>&lt;/strong&gt;</close>
                </bold>
                <separator>...</separator>
            </tag>
        </config>
    </search>
</container>
```
```

Maximum field byte length for bolding is 64Mb - field values larger than this will be represented as a snippet as in `summary: dynamic`.

## id

Contained in [field](#field). Sets the numerical ID of this field. All fields have a document-internal ID internally for transfer and storage. IDs are usually determined programmatically as a 31-bit number. Some storage and transfer space can be saved by instead explicitly setting IDs to a 7-bit number.

```
id: [positive integer]
```

An ID must satisfy these requirements:

- Must be a positive integer
- Must be less than 100 or larger than 127
- Must be unique within the document and all documents this document inherits

## index

Contained in [field](#field) or [schema](#schema). Sets index parameters.

Content in [string](#string)-fields with _index_ is [normalized](#normalizing) and [tokenized](../../linguistics/linguistics.html#tokenization) by default. The field can be single- or multivalued (e.g. `array<string>`).

For [tensor](#tensor)-typed fields, _index_ creates an [HNSW](#index-hnsw) index for [Approximate Nearest Neighbor](../../querying/nearest-neighbor-search-guide) queries, with a default [euclidean](#euclidean) distance metric. The index is built after a [content node restart](#changes-that-require-restart-but-not-re-feed) (automated on Vespa Cloud).

Examples:

```
index [index-name]: [property]
```
or
```
index [index-name] {
    [property]
    [property]
    …
}
```

 **Deprecated:** If `index-name` is specified, it will be used instead of the field name as the name of the index. This use is deprecated, use a synthetic field with the wanted name outside the `document` block instead - see an [example](/en/writing/indexing.html#date-indexing).
Parameters:

| Property | Occurrence | Description |
| --- | --- | --- |
| [stemming](#stemming) | Zero to one | Set the stemming of this index. Indexes without a stemming setting get their stemming setting from the fields added to the index. Setting this explicitly is useful if fields with conflicting stemming settings are added to this index. |
| arity | One (mandatory for predicate fields), else zero. | Set the [arity value for a predicate field](../../schemas/predicate-fields.html#index-size). The data type for the containing field must be `predicate`. |
| lower-bound | Zero to one | Set the [lower bound value for a predicate field](../../schemas/predicate-fields.html#upper-and-lower-bounds). The data type for the containing field must be `predicate`. |
| upper-bound | Zero to one | Set the [upper bound value for predicate fields](../../schemas/predicate-fields.html#upper-and-lower-bounds). The data type for the containing field must be `predicate`. |
| dense-posting-list-threshold | Zero to one | Set the [dense posting list threshold value for predicate fields](../../schemas/predicate-fields.html#dense-posting-list-threshold). The data type for the containing field must be `predicate`. |
| enable-bm25 | Zero to one | Enable this index field to be used with the [bm25 rank feature](../ranking/rank-features.html#bm25). This creates posting lists for the [indexes](../../content/proton.html#index) for this field that has interleaved features in the document id streams. This makes it fast to compute the _bm25_ score. See the [BM25 reference](/en/ranking/bm25.html) for details and example use. |
| [hnsw](#index-hnsw) | Zero to one | Specifies optional parameters for an HNSW index to enable faster, approximate nearest neighbor search. Only supported for tensor attribute fields with tensor types with: 
- One indexed dimension - single vector per document
- One or more mapped dimensions and one indexed dimension - multiple vectors per document

 Used in combination with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator. |

## hnsw

Contained in [index](#index). Specifies optional parameters for an HNSW index to enable faster, approximate nearest neighbor search using the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator.

 **Note:** Specifying the `index` keyword in the [indexing](#indexing) statement of a tensor creates an HNSW index with default settings, even if this block is not specified! 
This implements a modified version of the Hierarchical Navigable Small World (HNSW) graphs algorithm ([paper](https://arxiv.org/abs/1603.09320)).

Only supported for the following tensor attribute field types:

- Single vector per document: Tensor type with one indexed dimension. Example: `tensor<float>(x[3])`
- Multiple vectors per document: Tensor type with one or more mapped dimensions and one indexed dimension. Examples: `tensor<float>(m{},x[3])`, `tensor<float>(m{},n{},x[3])`

HNSW indexes are not supported in[streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

```
hnsw {
    [parameter]: [value]
    [parameter]: [value]
    ...
}
```

The following parameters are used when building the index graph:

| Parameter | Description |
| --- | --- |
| max-links-per-node | Specifies how many links per HNSW node to select when building the graph. The default value is 16. In [HNSWlib](https://github.com/nmslib/hnswlib/blob/master/ALGO_PARAMS.md) (implementation based on the paper) this parameter is known as _M_. |
| neighbors-to-explore-at-insert | Specifies how many neighbors to explore when inserting a document in the HNSW graph. The default value is 200. In HNSWlib, this parameter is known as _ef\_construction_. |

The [distance metric](#distance-metric) specified on the _attribute_ is used when building and searching the graph. Example:

```
field text_embedding type tensor<float>(x[384]) {
    indexing: summary | attribute | index
    attribute {
        distance-metric: prenormalized-angular
    }
    index {
        hnsw {
            max-links-per-node: 24
            neighbors-to-explore-at-insert: 200
        }
    }
}
```

See[Approximate Nearest Neighbor Search using HNSW Index](../../querying/approximate-nn-hnsw)for examples of use, and see[Approximate Nearest Neighbor Search in Vespa - Part 1](https://blog.vespa.ai/approximate-nearest-neighbor-search-in-vespa-part-1/) blog post for how the Vespa team selected HNSW as the baseline algorithm for extension and integration in Vespa.

## indexing

Contained in [field](#field) or[struct-field](#struct-field). One or more Indexing Language instructions used to produce index, attribute and summary data from this field. Indexing instructions have pipeline semantics similar to Unix shell commands. The value of the field enters the pipeline during indexing, and the pipeline puts the value into the desired index structures, possibly doing transformations and pulling in other values along the way.

```
indexing: [index-statement]
```
or
```
indexing {
    [indexing-statement];
    [indexing-statement];
    …
}
```

If the field containing this is defined outside the document, it must start with an indexing statement which outputs a value (either "input [fieldname]" to fetch a field value, or a literal, e.g, "some-value" ). Fields in documents will use the value of the enclosing field as input (input [fieldname]) if one isn't explicitly provided.

Specify the operations separated by the pipe (`|`) character. For advanced processing needs, use the [indexing language](../writing/indexing-language.html), or write a [document processor](../../applications/document-processors.html). Supported expressions for fields are:

| expression | description |
| --- | --- |
| attribute | 

[Attribute](../../content/attributes.html) is used to make a field available for sorting, grouping, ranking and searching using [match](#match) mode `word`.

 |
| index | 

Creates a searchable [index](../../content/proton.html#index) for the values of this field using [match](#match) mode `text`. By default, the index name will be the same as the name of the schema field. Use a [fieldset](#fieldset) to combine fields in the same set for searching.

 |
| set\_language | Sets document language - [details](../writing/indexing-language.html#set_language). |
| summary | Includes the value of this field in a [summary](../writing/indexing-language.html#summary) field. Modify summary output by using [summary:](#summary) (e.g., to generate dynamic teasers). |

When combining both `index` and `attribute` in the indexing statement for a field, e.g `indexing: summary | attribute | index`, the [match](#match) mode becomes `text` for the field. So searches in this field will not search the contents in the [attribute](#attribute) but the index.

Find examples and more details in the [Text Matching](../../querying/text-matching.html) guide.

## match

Contained in [field](#field), [fieldset](#fieldset) or[struct-field](#struct-field). Sets the matching method to use for this field to something other than the default token matching.

```
match: [property]
```
or
```
match {
    [property]
    [property]
    …
}
```

Whether the match type is `text`, `word` or `exact`, all term matching will be done after [normalization](../../linguistics/linguistics.html#normalization)and locale-independent lowercasing (in that order).

Find examples and more details in the [Text Matching](../../querying/text-matching.html) guide. Also see search using [regular expressions](../querying/yql.html#matches).

| Property | Valid with | Description |
| --- | --- | --- |
| text | index | 

The default for string fields with `index`. Can not be combined with exact matching. The field is matched per [token](../../linguistics/linguistics.html#tokenization).

 |
| exact | index, attribute | 

Can not be combined with _text_ matching.

The field is matched _exactly_: Strings containing any characters whatsoever will be indexed and matched as-is. Lowercasing is still performed unless `match: cased` is also used. In queries, the exact match string ends at the exact match terminator (below).

A field with `match: exact` is considered to be a [filter field](#filter), just as if `rank: filter` was specified. This is because there is only one word per field (or per item in the case of multivalued types such as `array<string>`), so there is little ranking information. Turn off the implicit `rank: filter` by adding `rank: normal`.

 |
| exact-terminator | index, attribute | 

Only valid for `match: exact`. Default is `@@`. Specify terminator in [query strings](../api/query.html#model.querystring). If the query strings can contain `@@`, set a different terminator, or use `match: word`, see below. Example - use:

```
match {
    exact
    exact-terminator: "@%"
}
```

on a field called `tag` to make query `tag:a b c!@%` match documents with the string _a b c!_

Example using the default terminator: If `tag` is an exact match field, the query:

```
someword AND (tag:!*!@@ OR tag:(kanoo)@@)
```
 matches documents with `someword` and either `!*!` or `(kanoo)` as a tag. Note that without the `@@` terminating the second tag string, the second tag value would be `(kanoo))`. |
| word | index, attribute | 

This is the default matching mode for [string attributes](../../content/attributes.html). It cannot be combined with _text_ matching.

Match word means that the entire content of the field is indexed as a single word.

Word matching is like exact matching, but with more advanced query parsing. The query terms are heuristically parsed, taking into account some usual query syntax characters. One can also use double quotes to include spaces, stars, or exclamation marks.

Example: If `artist` is a string attribute, the query:

```
foo AND (artist:"'N Sync" OR artist:"*NSYNC" OR artist:A*teens OR artist:"Wham!")
```

matches documents with `foo` and at least one of `'N Sync` or `*NSYNC` or `A*teens` or `Wham!` in the artist field

Note that without the quotes, the space in `'N Sync` would end that word and would result in a search for just `'N`, similarly the `!` would mean to increase the weight of a `Wham` term if not quoted.

 |
| prefix | attribute | 

Has no effect, as [attributes](../../content/attributes.html) always support prefix searches. Prefix matching must be [specified in the query](../querying/yql.html#prefix). See also [regular expressions](../querying/yql.html#matches).

 |
| substring | [Streaming mode](../../performance/streaming-search.html) only | 

Set default match mode to _substring_ for the field. Only available in streaming search. As the data structures in streaming search support substring searches, one can always set substring matching in the query, without setting the field to the substring default. Also see [regular expressions](../querying/yql.html#matches).

 |
| suffix | [Streaming mode](../../performance/streaming-search.html) only | 

Like substring above.

 |
| uncased | index, attribute | 

Use case-insensitive matching (the default).

 |
| cased | index, attribute | 

Use case-sensitive matching. Usually only used together with `match: exact` or `match: word` modes. When using `match: text`, note that if you are using a custom [linguistics implementation](../../linguistics/linguistics.html#creating-a-custom-linguistics-implementation), this will only have effect for string index fields if that implementation produces cased tokens.

 |
| max-length | index | 

Limit the length of the field that will be used for matching. By default, only the first 1M characters are indexed.

When adjusting this limit, it might also be needed to adjust [max-occurrences](#max-occurrences).

 |
| max-occurrences | index | 

Configure the maximum number of occurrences that will be indexed for each unique token/term in the field for a given document. If this limit is reached, consecutive occurrences of the same token/term are ignored for that document. The default value is 10000.

Adjusting this limit might be needed when using the [phrase](../querying/yql.html#phrase), [near](../querying/yql.html#near), or [onear](../querying/yql.html#onear) query operators to query documents with large field values (see [max-length](#max-length)) that contain more than 10000 occurrences of common tokens/terms. When using these operators, it is only possible to match among the first _max-occurrences_ of a token/term in a document.

 |
| max-token-length | index | 

Configure the max length of tokens that will be indexed for the field. Longer tokens are silently ignored. The unit is characters (cf. java.lang.String.length()). The default value is 1000.

 |
| gram | index | 

This field is matched using n-grams. For example, with the default gram size 2, the string "hi blue" is tokenized to "hi bl lu ue" both in the index and in queries to the index.

N-gram matching is useful mainly as an alternative to [segmentation](../../linguistics/linguistics.html#tokenization) in CJK languages. Typically, it results in increased recall and lower precision. However, as Vespa usually uses proximity in ranking, the precision offset may not be of much importance. Grams consume more resources than other matching methods because both indexes and queries will have more terms, and the terms contain repetition of the same letters. On the other hand, CPU-intensive CJK segmentation is avoided.

It may also be used for substring matching in general.

 |
| gram-size | index | 

A positive, nonzero number, default 2. Sets the gram size when gram matching is used. Example:

```
match {
    gram
    gram-size: 3
}
```
 |

## rank

Contained in [field](#field), [struct-field](#struct-field) or[rank-profile](#rank-profile). Set the kind of ranking calculations that will be done for the field. Even though the actual ranking expressions decide the ranking, this setting tells Vespa which preparatory calculations and which data structures are needed for the field.

```
rank [field-name]: [ranking settings]
```
or
```
rank {
    [ranking setting]
}
```
The field name should only be specified when used inside a rank-profile. The following ranking settings are supported in addition to the default:

| Ranking setting | Description |
| --- | --- |
| filter | 

Indicates that matching in this field should use fast bit vector data structures only. This saves CPU during matching, but only a few simple ranking features will be available for the field. This setting is appropriate for fields typically used for filtering or simple boosting purposes, like filtering or boosting on the language of the document.

- For _index_ fields, this setting does not change index formats but helps choose the most compact representation when matching against the field. 
- For _attribute_ fields with _fast-search_ this setting builds additional posting list representations (bit vectors) can significantly speed up query evaluation. 

See [feature tuning](../../performance/feature-tuning.html#when-to-use-fast-search-for-attribute-fields) and [the practical search performance guide](../../performance/practical-search-performance-guide.html).

 |
| normal | 

The reverse of `filter`. Matching in this field will use normal data structures and give normal match information for ranking. Used to turn off implicit `rank: filter` when using [match: exact](#exact). If both `filter` and `normal` are set somehow, the effect is as if only `normal` was specified.

 |

Related: See the [filter](../querying/yql.html#filter) query annotation for how to annotate query terms as filters.

### filter-threshold

Contained in a [rank-profile](#rank-profile). Used to optimize query performance when searching large text [index](../../basics/schemas.html#document-fields) fields, by allowing a per query combination of [rank: filter](#filter) and [rank: normal](#normal) behavior. See [profile-level filter-threshold](#filter-threshold) for how to use the same value for all _index_ fields.

```
rank [field-name] {
    filter-threshold: 0.05
}
```

| Setting | Description |
| --- | --- |
| filter-threshold | 

Threshold value (in the range [0.0, 1.0]) deciding when matching in this _index_ field should be treated as a filter. This happens for query terms with [estimated hit ratios](../../learn/glossary.html#estimated-hit-ratio) (in the range [0.0, 1.0]) that are above the _filter-threshold_. Then, fast bitvector data structures are used, similar to when the field is set to [rank: filter](#filter). This saves CPU and Disk I/O during matching and typically results in faster query evaluation, with the downside being that only a boolean signal is available for ranking (the document being a match or not). [BM25](../../ranking/bm25.html) handles this by assuming one occurrence of the query term in the document, and the field length being equal to the average field length.

Use this to optimize query performance when searching large text _index_ fields with e.g. the [weakAnd](../../ranking/wand.html#weakand) query operator and [BM25](../../ranking/bm25.html) ranking. Query terms that are common in the corpus (e.g., stopwords) are treated as filters with faster matching and simplified ranking, while other query terms are handled as usual with full ranking.

In testing with various text datasets (e.g., Wikipedia), a _filter-threshold_ setting of 0.05 has been shown to be a good starting point. [Read more](../../performance/feature-tuning.html#posting-lists).

This setting is only relevant for [index](../../basics/schemas.html#document-fields) fields, and cannot be used in combination with [rank: filter](#filter). Has no effect in [streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

 |

### element-gap

Contained in a [rank-profile](#rank-profile). Used to specify the gap between positions in adjacent elements in multi-value fields. The default value is `infinity`. It should be specified as `infinity` or as a positive integer number.

Consider an `array<string>` field with three elements `["a c", "x b x a x x x x x x b", "x x d"]`. Normally, distance calculation is only performed within an element, thus the minimum forward distance between occurrences for terms _a_ and _b_ is 7. By setting the `element-gap` for the field to 0, adjacent elements are considered and the minimum forward distance between occurrences for terms _a_ and _b_ becomes 3. The minimum distance between occurrences for terms _c_ and _d_ is not calculated since they are not in adjacent elements.

The `element-gap` setting affects the [nativeProximity](/en/reference/ranking/rank-features.html#nativeProximity) rank feature, the [near](/en/reference/querying/yql.html#near) query operator and the [onear](/en/reference/querying/yql.html#onear) query operator.

```
rank [field-name] {
    element-gap: 0
}
```

No restart or reindexing is required when changing this setting, it is immediately effective.

## query-command

Contained in [fieldset](#fieldset), [field](#field) or[struct-field](#struct-field). Specifies a function to be performed on query terms to the indexes of this field when searching. The Search Container server has support for writing Vespa Searcher plugins that process these commands.

```
query-command: [an identifier or quoted string]
```

If you write a plugin searcher that needs some index-specific configuration parameter, that parameter can be set here.

There is one built-in query-command available: `phrase-segmenting`. If this is set, terms connected by non-word characters in user queries (such as "a.b") will be parsed to a phrase item, instead of by default, an AND item where these terms have connectivity set to 1.

## rank-type

Contained in [field](#field) or[rank-profile](#rank-profile). Selects the low-level rank settings to be used for this field when using `nativeRank`.

```
rank-type [field-name]: [rank-type-name]
```
The field name can be skipped inside fields. Defined rank types are:

| Type | Description |
| --- | --- |
| identity | Used for fields that contains only what this document _is_, e.g., "Title". Complete identity hits will get a high rank. |
| about | Some text which is (only) about this document, e.g. "Description". About hits get high rank on partial matches and higher for matches early in the text and repetitive matches. This is the default rank type. |
| tags | Used for simple tag fields of type tag. The tags rank type uses a logarithmic table to give more relative boost in the low range: As tags are added, they should have a significant impact on the rank score, but as more and more tags are added, each new tag should contribute less. |
| empty | Gives no relevancy effect on matches. Used for fields you just want to treat as filters. |

For `nativeRank`, one can specify a rank type per field. If the supported rank types do not meet requirements, one can explicitly configure the native rank features using rank-properties. See the [native rank reference](../ranking/nativerank.html) for more information.

## weakand

Contained in [rank-profile](#rank-profile).

Tunes the [weakAnd](../../ranking/wand.html#weakand) algorithm to automatically exclude terms and documents with expected low query significance based on document frequency statistics present in the document corpus. This makes matching faster at the cost of potentially reduced recall.

```
weakand {
    [body]
}
```

Note that all document frequency calculations are done using _content node-local_ document statistics (i.e. [global significance](../../ranking/significance#global-significance-model) does not have an effect). This means results may differ across different content nodes and/or content node groups.

The body of a `weakand` statement consists of:

| Property | Occurrence | Description |
| --- | --- | --- |
| stopword-limit | Zero to one | 

A number in the range [0, 1]. Represents the maximum [normalized document frequency](../../learn/glossary.html#document-frequency-normalized) a query term can have in the corpus (i.e. the ratio of all documents where the term occurs at least once) before it's considered a stopword and dropped entirely from being a part of the `weakAnd` evaluation. This makes matching faster at the cost of potentially producing more hits. Dropped terms are not exposed as part of ranking.

Example:

```
stopword-limit: 0.60
```

This will drop all query terms that occur in at least 60% of the documents.

Using `stopword-limit` is similar to explicitly removing stopwords from the query up front, but has the benefit of dynamically adapting to the actual document corpus and not having to know—or specify—a set of stopwords. [Read more](../../performance/feature-tuning.html#posting-lists).

 |
| adjust-target | Zero to one | 

A number in the range [0, 1] representing [normalized document frequency](../../learn/glossary.html#document-frequency-normalized). Used to derive a per-query document score threshold, where documents scoring lower than the threshold will not be considered as potential hits from the `weakAnd` operator. The score threshold is selected to be equal to that of the query term whose document frequency is _closest_ to the configured `adjust-target` value.

This can be used to efficiently _exclude_ documents that only match terms that occur very frequently in the document corpus. Such terms are likely to be stopwords that have low semantic value for the query, and excluding documents only containing them is likely to have only a minor impact on recall.

This makes overall matching faster by reducing the number of hits produced by the `weakAnd` operator.

Example:

```
adjust-target: 0.01
```

This excludes documents that only have terms that occur in more than approximately 1% of the document corpus. The actual threshold is query-specific and based on the query term score whose document frequency is closest to 1%.

`adjust-target` can be used together with [stopword-limit](#weakand-stopword-limit) to efficiently prune both terms and documents with low significance when processing queries. [Read more](../../performance/feature-tuning.html#posting-lists).

 |
| allow-drop-all | Zero to one | 

A boolean value. The default behavior of `weakAnd` is to always keep at least one term (the least common one) even though it is considered a stopword. This is to avoid dropping all query terms in order to make sure that some hits are produced.

If set to `true`, the `weakAnd` operator will allow removal of all query terms if they are all considered stopwords (i.e., if `stopword-limit` is set and all query terms are above the limit).

This may be desired (and significantly improve query performance) if `weakAnd` is used together with another query operator, e.g. the [nearestNeighbor](../../querying/nearest-neighbor-search#querying-using-nearestneighbor-query-operator) operator.

Be aware that if this is set to `true` and all query terms are considered stopwords, the `weakAnd` operator will not produce _any_ hits. And by extension, if `weakAnd` is used by itself, the query may return no hits.

Example:

```
weakand-allow-drop-all: true
```

This overrides the default behavior of `weakAnd` and allows all query terms to be dropped if they are all considered stopwords.

 **Important:** Defaults to `false` if not specified. 
 |

## summary-to

 **Deprecated:** Use [document-summary](#document-summary) instead.
 Contained in [field](#field) or [struct-field](#struct-field). Specifies the name of the document summaries that should contain this field.
```
summary-to: [summary-name], [summary-name], …
```

Fields with summary will always be part of the default summary regardless of this setting. Use explicit [document-summary](#document-summary) instead. See also [document summaries](../../querying/document-summaries.html).

## summary

Contained in [field](#field) or[document-summary](#document-summary) or[struct-field](#struct-field). Declares a summary field.

```
summary: [property]
```
or
```
summary [name] {
    [body]
}
```
The summary _name_ can be skipped if this is set inside a field. The name will then be the same as the name of the source field._full_ summary is the default. Long field values (like document content fields) should be made _dynamic_. The body of a summary may contain:

| Name | Occurrence | Description |
| --- | --- | --- |
| full | Zero to one | Returns the full field value in the summary (the default). |
| bolding: on | Zero to one | Specifies whether the content of this field should be [bolded](#bolding). Only supported for [index](#indexing-index) fields of type string or array\<string\>. |
| dynamic | Zero to one | Make the value returned in results from this summary field a _dynamic abstract_ of the source field by extracting fragments of text around matching query terms. Matching query terms will also be highlighted, in similarity with the bolding feature. This highlighting is not affected by the query-argument bolding. The default XML element used to highlight query terms is`<hi>` - refer to [bolding](#bolding) for how to configure. _dynamic_ is only supported for [index](#indexing-index) fields of type string or array\<string\>. For array\<string\> fields, a dynamic abstract is created per string item in the array. |
| source | Zero to one | 

Specifies the name of the field or fields from which the value of this summary field should be fetched. If multiple fields are specified, the value will be taken from the first field if that has a value, from the second if the first one is empty, and so on.

```
source: [field-name], [field-name], …
```

When this is not specified, the source field is assumed to be the field with the same name as the summary field.

Refer to [attribute](#add-or-remove-an-existing-document-field-from-document-summary) and [non-attribute](#add-or-remove-a-new-non-attribute-document-field-from-document-summary) fields for modifying a schema.

 |
| to | Zero to one | Specifies the name of the document summaries that this should be included in.
```
to: [document-summary-name], [document-summary-name], …
```
 This can only be specified in fields, not in the explicit document summaries. When this is not specified, the field will go to the `default` document summary. |
| matched-elements-only | Zero to one | 

Specifies that only the matched elements in a searchable [array of primitive](#array), [weightedset](#weightedset), [array of struct](#array) or [map type](#map) field are returned as part of document summary. For array of struct or map type fields, this is typically used in accordance with the [sameElement](../querying/yql.html#sameelement) operator, but it can also be used when searching directly on a sub-struct field. It is also supported when the field is [imported](#import-field).

See [example use](#map) and example schemas:

- [matched elements only](https://github.com/vespa-engine/system-test/blob/master/tests/search/matched_elements_only/indexed/test.sd)
- [array of struct and map type](https://github.com/vespa-engine/system-test/blob/master/tests/search/struct_and_map_types/attribute_fields/test.sd)

 |
| select-elements-by | Zero to one | 

Use a summary feature to control which elements in an [array of primitive](#array) or [array of struct](#array) field are returned as part of document summary.

```
select-elements-by: <summary-feature-name>
```

The summary feature used must be a tensor with a single mapped dimension. An element will be returned if its id is a label along the mapped dimension of this tensor.

- [schema example](https://github.com/vespa-engine/system-test/blob/master/tests/search/chunk_selection/test.sd)

 |
| tokens | Zero to one | 

Make the value returned in results from this summary field be an array of the tokens indexed in the source field. Multiple tokens at the same location are put into a nested array.

The source field must be specified, and it must be an [index](#indexing-index) or[attribute](#indexing-attribute) field of type string, array\<string\> or weightedset\<string\>. If the source field is of type weightedset\<string\> then the summary field is rendered as if the source field was of type array\<string\>, weights are not shown.

This is mainly useful for [linguistics transformations debugging](../../querying/text-matching.html#tokens-example), to correlate query trace with the tokens indexed.

 |

Read more about [document summaries](../../querying/document-summaries.html).

## weight

Contained in [field](#field). The weight of a field - the default is 100. The field weight is used when calculating the [rank scores](../../basics/ranking.html).

```
weight: [positive integer]
```

## weightedset

Contained in [field](#field) of type weightedset. Properties of a weighted set.

```
weightedset: [property]
```
or
```
weightedset {
    [property]
    [property]
    …
}
```

| Property | Occurrence | Description |
| --- | --- | --- |
| create-if-nonexistent | Zero to one | If the weight of a key is adjusted in a document using a partial update increment or decrement command, but the key is currently not present, the command will be ignored by default. Set this to make keys to be created in this case instead. This is useful when the weight is used to represent the count of the key.
```
field tag type weightedset<string> {
    indexing: attribute | summary
    weightedset {
        create-if-nonexistent
        remove-if-zero
    }
}
```
 |
| remove-if-zero | Zero to one | This is the companion of `create-if-nonexistent` for the converse case: By default, keys may have zero as weight. With this turned on, keys whose weight is adjusted (or set) to zero will be removed. |

## import field

Contained in [schema](#schema). Using a [reference](#reference) to a document type, import a field from that document type into this schema to be used for matching, ranking, grouping, and sorting. Only attribute fields can be imported. Importing fields are not supported in[streaming search](../../performance/streaming-search.html#differences-in-streaming-search).

The imported field inherits all but the following properties from the parent field:

- [attribute: fast-access](#attribute)

Refer to [parent/child](../../schemas/parent-child.html) for a complete example. Note that the imported field is put outside the document type:

```
schema myschema {
    document myschema {
        field parentschema_ref type reference<parentschema> {
            indexing: attribute
        }
    }
    import field parentschema_ref.name as parent_name {}
}
```

Extra restrictions apply for some of the field types:

| Field type | Restriction |
| --- | --- |
| array of struct | Can be imported if at least one of the struct fields has an attribute. All struct fields with attributes must have primitive types. Only the struct fields with attributes will be visible. |
| map of struct | Can be imported if the key field has an attribute, and at least one of the struct fields has an attribute. All struct fields with attributes must have primitive types. Only the key field and the struct fields with attributes will be visible. |
| map | Can be imported if both key and value fields have primitive types and have attributes. |
| position | Can be imported if it has an attribute. |
| array of position | Can be imported if it has an attribute. |

To use an imported field in summary, create an explicit[document summary](#document-summary) containing the field.

Imported fields can be used to expire documents, but [read this first](../../schemas/documents.html#document-expiry).

## Document and search field types

Note that it is possible to make a document field of one type into one or more instances of another search field, by declaring a field outside the document, which uses other fields as input. For example, to create an integer attribute for a string containing a comma-separated list of integers in the document, do like this:

```
schema example {
    document example {
        field yearlist type string { # Comma-separated years
        }
    }

    field year type array<int> { # Search field using the yearlist value
        indexing: input yearlist | split "," | attribute
    }
}
```

## Modifying schemas

This section describes how a schema in a live application can be modified—categories:

1. [Valid changes without restart or re-feed](#valid-changes-without-restart-or-re-feed)
2. [Changes that require restart but not re-feed](#changes-that-require-restart-but-not-re-feed)
3. [Changes that require reindexing](#changes-that-require-reindexing)
4. [Changes that require re-feed](#changes-that-require-re-feed)

When running `vespa prepare` on a new application package, the changes in the schema files are compared with the files in the current active package. If some of the changes require restart or re-feed, the output from `vespa prepare`specifies which actions are needed.

 **Important:** For changes that are not covered below, and no output is returned from `vespa prepare`, the impact is undefined and in no way guaranteed to allow a system to stay live until re-feeding. Changes not related to the schema are discussed in [admin procedures](/en/operations/self-managed/admin-procedures.html).

### Valid changes without restart or re-feed

Procedure:

1. Run `vespa prepare` on the changed application
2. Run `vespa activate`. The changes will take effect immediately

Changes:

| Change | Description |
| --- | --- |
| Add a new document field | Add a new document field as index, attribute, summary or any combination of these. Existing documents will implicitly get the new field with no content. Documents fed after the change can specify the new field. If the field has existed with the same type earlier, then old content _may or may not_ reappear |
| Remove a document field | Existing documents will no longer see the removed field, but the field data is not completely removed from the search node |
| Add or remove an existing document field from document summary | 

Add an existing field to summary or any number of summary classes, and remove an existing field from summary or any number of summary classes. Example:

```
document-summary short-summary {
        summary artist {}
    }
```

A change adding an [attribute](../../content/attributes.html) field with a new name to a summary class using [source](#source) does not require restart or re-feed:

```
field artist type string {
            indexing: summary | attribute
    }

    document-summary rename-summary {
        summaryartist\_name{source: artist}
    }
```

Also see [non-attribute](#add-or-remove-a-new-non-attribute-document-field-from-document-summary) fields.

 |
| Remove the attribute aspect from a field that is also an index field | This is the only scenario of changing the attribute aspect of a document field that is allowed without restart |
| Add, change or remove field sets | Change [fieldsets](#fieldset) used to group fields together for searching |
| Change the alias or sorting attribute settings for an attribute field | |
| Add, change or remove rank profiles | |
| Change document field weights | |
| Add, change or remove field aliases | |
| Add, change or remove rank settings for a field | Exception: Changing `rank: filter` on an attribute field in mode _index_ requires restart. See details in [next section](#changes-that-require-restart-but-not-re-feed) |
| Add or remove a schema | Removing a schema definition file will make [proton](../../content/proton.html) drop all documents of that type, subsequently releasing memory and disk. |

### Changes that require restart but not re-feed

Procedure:

1. Run `vespa prepare` on the changed application. Output specifies which restart actions are needed 
2. Run `vespa activate`
3. Restart `services` on the services specified in the `prepare` output

Changes:

| Change | Description |
| --- | --- |
| Change the attribute aspect of a document field | Add or remove a field as attribute. When adding, the attribute is populated based on the field value in stored documents during restart. When removing, the field value in stored documents is updated based on the content in the attribute during restart. |
| Change the attribute settings for an attribute field | Change the following attribute settings: `fast-search`, `fast-access`, `fast-rank`, `paged`. |
| Change the rank filter setting for an attribute field | Add or remove `rank: filter` on an attribute field. |
| Change the hnsw index settings for a tensor attribute field | Adding or removing the [hnsw index](#index-hnsw) on a tensor attribute field, or changing the `distance-metric` or `max-links-per-node` requires a restart to rebuild the index. Changing `neighbors-to-explore-at-insert` requires a restart, but does not rebuild the index. |
| Change the distance metric for a tensor attribute field | Change, add, or remove the [distance metric](#distance-metric) on a tensor attribute field. If no distance metric is specified, _euclidean_ is used as the default. |

Example: Given a content cluster _mycluster_ with mode _index_:

```
schema test {
    document test {
        field f1 type string { indexing: summary }
    }
}
```
Then add field `f1` as an attribute:
```
schema test {
    document test {
        field f1 type string { indexing: attribute | summary }
    }
}
```
The following is output from `vespa prepare` - which restart actions are needed:
```
WARNING: Change(s) between active and new application that require restart:
In cluster 'mycluster' of type 'search':
    Restart services of type 'searchnode' because:
        1) Document type 'test': Field 'f1' changed: add attribute aspect
```

### Changes that require reindexing

All the changes listed below require [reindexing](../../operations/reindexing.html)of all documents. Unlike re-feed, which requires an external source of data, reindexing is done using documents stored in Vespa, and is automatic (once triggered). It can also run concurrently with feed and serving, but until reindexing is complete, affected fields will be empty or have potentially wrong annotations not matching the query processing. Procedure:

1. Run `vespa prepare` on the changed application. Output specifies which reindexing actions are needed 
2. Run `vespa activate`
3. [Enable reindexing](../api/deploy-v2.html#reindex) for the indicated document types and clusters
4. Run `vespa prepare` and `vespa activate` again to start reindexing process

Changes:

| Change | Description |
| --- | --- |
| Change index aspect of a document field | This changes the document processing pipeline before documents arrive in the backend. Only documents fed after index aspect was added will have annotations and be present in the reverse index. Only documents fed after index aspect was removed will avoid disk bloat due to unneeded annotations. |
| Switch stemming/normalizing on or off | 

This changes the document processing pipeline before documents arrive in the backend, and what annotations are made for an indexed field.

 **Important:** If not re-feeding after such a change, serving works, but recall is undefined as the index has been produced using a different setting than the one used when doing stemming/normalizing of the query terms.
 |
| Add, change, or remove match settings for a field | 

Example: Adding `match: word` to a field.

This changes the document processing pipeline before documents arrive in the backend, and what annotations are made for an indexed field.

 **Important:** If not reindexing after such a change, serving works, but recall is undefined as the index has been produced using one match mode while run-time is using a different match mode.
 |
| Add or remove a new non-attribute document field from document summary | 

A change adding an [index or summary](/en/basics/schemas.html#document-fields) field (without [attribute](/en/content/attributes.html)) with a new name to a summary class using [source](#source) requires re-index:

```
field artist type string {
            indexing: summary | index
    }

    document-summary rename-summary {
        summaryartist\_name{source: artist}
    }
```

Also see [attribute](#add-or-remove-an-existing-document-field-from-document-summary) fields.

 |

Example: Given a content cluster _mycluster_ with mode _index_:
```
schema test {
    document test {
        field f1 type string { indexing: summary }
    }
}
```
Then add field `f1` as an index:
```
schema test {
    document test {
        field f1 type string { indexing: index | summary }
    }
}
```
The following is output from `vespa prepare` - which reindex actions are needed:
```
WARNING: Change(s) between active and new application that require re-index:
Reindex document type 'test' in cluster 'mycluster' because:
    1) Document type 'test': Field 'f1' changed: add index aspect, indexing script: '{ input f1 | summary f1; }' -> '{ input f1 | tokenize normalize stem:"SHORTEST" | index f1 | summary f1; }'
```

### Changes that require re-feed

All the changes listed below require re-feeding of all documents. Unless a change is listed in the above sections, treat it as if it were listed here. Until re-feed is complete, affected fields will be empty or have potentially wrong annotations not matching the query processing. Procedure:

1. Run `vespa prepare` on the changed application. Output specifies which re-feed actions are needed 
2. Stop feeding, wait until done
3. Run `vespa activate`
4. Re-feed all documents

Changes:

| Change | Description |
| --- | --- |
| Change a document field's data type or collection type | 

Existing documents will no longer have any content for this field. To populate the field, re-feed the existing documents using the new type for this field. There will be no automatic conversion from old to new field type.

 **Important:** If not re-feeding after such a change, serving works, but searching this field will not give any results
 |
| Change a tensor attribute's tensor type | |

Example: Given a content cluster _mycluster_ with mode _index_:
```
schema test {
    document test {
        field f1 type string { indexing: summary }
    }
}
```
Then change field `f1` to hold an int:
```
schema test {
    document test {
        field f1 type int { indexing: summary }
    }
}
```
The following is output from `vespa prepare` - which re-feed actions are needed:
```
WARNING: Change(s) between active and new application that require re-feed:
Re-feed document type 'test' in cluster 'mycluster' because:
    1) Document type 'test': Field 'f1' changed: data type: 'string' -> 'int'
```

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Syntax](#syntax)
- [Elements](#elements)
- [schema](#schema)
- [document](#document)
- [struct](#struct)
- [field](#field)
- [struct-field](#struct-field)
- [fieldset](#fieldset)
- [compression](#compression)
- [rank-profile](#rank-profile)
- [match-phase](#match-phase)
- [strict](#strict)
- [diversity](#diversity)
- [first-phase](#firstphase-rank)
- [expression](#expression)
- [rank-features](#rank-features)
- [inputs](#inputs)
- [constants](#constants)
- [rank-properties](#rank-properties)
- [function (inline)? [name]](#function-rank)
- [second-phase](#secondphase-rank)
- [global-phase](#globalphase-rank)
- [summary-features](#summary-features)
- [match-features](#match-features)
- [mutate](#mutate)
- [constant](#constant)
- [raw-as-base64-in-summary](#raw-as-base64-in-summary)
- [onnx-model](#onnx-model)
- [significance](#significance)
- [document-summary](#document-summary)
- [stemming](#stemming)
- [normalizing](#normalizing)
- [dictionary](#dictionary)
- [Dictionary Types](#)
- [Case Handling for String Fields](#)
- [Important Rules for String Fields with Dictionaries](#)
- [Example: Case-Sensitive Hash Dictionary](#)
- [attribute](#attribute)
- [sorting](#sorting)
- [distance-metric](#distance-metric)
- [euclidean](#euclidean)
- [angular](#angular)
- [dotproduct](#dotproduct)
- [prenormalized-angular](#prenormalized-angular)
- [geodegrees](#geodegrees)
- [hamming](#hamming)
- [bolding](#bolding)
- [id](#id)
- [index](#index)
- [hnsw](#index-hnsw)
- [indexing](#indexing)
- [match](#match)
- [rank](#rank)
- [filter-threshold](#rank-filter-threshold)
- [element-gap](#rank-element-gap)
- [query-command](#query-command)
- [rank-type](#rank-type)
- [weakand](#weakand)
- [summary-to](#summary-to)
- [summary](#summary)
- [weight](#weight)
- [weightedset](#weightedset-properties)
- [import field](#import-field)
- [Document and search field types](#document-and-search-field-types)
- [Modifying schemas](#modifying-schemas)
- [Valid changes without restart or re-feed](#valid-changes-without-restart-or-re-feed)
- [Changes that require restart but not re-feed](#changes-that-require-restart-but-not-re-feed)
- [Changes that require reindexing](#changes-that-require-reindexing)
- [Changes that require re-feed](#changes-that-require-re-feed)

