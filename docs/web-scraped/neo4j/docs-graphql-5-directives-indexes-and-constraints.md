# Source: https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/

Title: Indexes and constraints - Neo4j GraphQL Library

URL Source: https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/

Markdown Content:
Indexes and constraints - Neo4j GraphQL Library
===============

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#)[Use necessary cookies only](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#)

[![Image 1: Neo4j GraphQL Library](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)[Docs](https://neo4j.com/docs/)

[Docs](https://neo4j.com/docs/)

Neo4j DBMS
*   [Getting Started](https://neo4j.com/docs/getting-started/current/)
*   [Operations](https://neo4j.com/docs/operations-manual/current/)
*   [Migration and Upgrade](https://neo4j.com/docs/migration-guide/current/)
*   [Status Codes](https://neo4j.com/docs/status-codes/current/)
*   [Java Reference](https://neo4j.com/docs/java-reference/current/)
*   [Kerberos Add-on](https://neo4j.com/docs/kerberos-add-on/current/)

[Neo4j Aura](https://neo4j.com/docs/aura/)

Neo4j Tools
*   [Neo4j Bloom](https://neo4j.com/docs/bloom-user-guide/current/)
*   [Neo4j Browser](https://neo4j.com/docs/browser/)
*   [Neo4j Data Importer](https://neo4j.com/docs/data-importer/current/)
*   [Neo4j Desktop](https://neo4j.com/docs/desktop-manual/current/)
*   [Neo4j Ops Manager](https://neo4j.com/docs/ops-manager/current/)
*   [Neodash commercial](https://neo4j.com/docs/neodash-commercial/current/)

Neo4j Graph Data Science
*   [Neo4j Graph Data Science Library](https://neo4j.com/docs/graph-data-science/current/)
*   [Neo4j Graph Data Science Client](https://neo4j.com/docs/graph-data-science-client/current/)

Cypher Query Language
*   [Cypher](https://neo4j.com/docs/cypher-manual/current/)
*   [Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/current/)
*   [APOC Library](https://neo4j.com/docs/apoc/current/)

Generative AI
*   [Neo4j GraphRAG for Python](https://neo4j.com/docs/neo4j-graphrag-python/current/)
*   [Embeddings and vector indexes tutorial](https://neo4j.com/docs/genai/tutorials/embeddings-vector-indexes/)
*   [GenAI integrations](https://neo4j.com/docs/cypher-manual/current/genai-integrations/)
*   [Vector search indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/)
*   [Vector search functions](https://neo4j.com/docs/cypher-manual/current/functions/vector/)
*   [GraphQL vector index search documentation](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_vector_index_search)

Create applications
*   [Python Driver](https://neo4j.com/docs/python-manual/current/)
*   [Go Driver](https://neo4j.com/docs/go-manual/current/)
*   [Java Driver](https://neo4j.com/docs/java-manual/current/)
*   [JDBC Driver](https://neo4j.com/docs/jdbc-manual/current/)
*   [JavaScript Driver](https://neo4j.com/docs/javascript-manual/current/)
*   [.Net Driver](https://neo4j.com/docs/dotnet-manual/current/)
*   [Neo4j GraphQL Library](https://neo4j.com/docs/graphql-manual/current/)
*   [Neo4j Visualization Library](https://neo4j.com/docs/nvl/current/)
*   [OGM Library](https://neo4j.com/docs/ogm-manual/current/)
*   [Spring Data Neo4j](https://docs.spring.io/spring-data/neo4j/docs/current/reference/html/#reference)
*   [HTTP API](https://neo4j.com/docs/http-api/current/)
*   [Neo4j Query API](https://neo4j.com/docs/query-api/current/)
*   [Bolt](https://neo4j.com/docs/bolt/current/)

Connect data sources
*   [Neo4j Connector for Apache Spark](https://neo4j.com/docs/spark/current/)
*   [Neo4j Connector for Apache Kafka](https://neo4j.com/docs/kafka/)
*   [Change Data Capture (CDC)](https://neo4j.com/docs/cdc/)
*   [BigQuery to Neo4j](https://neo4j.com/docs/dataflow-bigquery/)
*   [Google Cloud to Neo4j](https://neo4j.com/docs/dataflow-google-cloud/)

[Labs](https://neo4j.com/labs/)

[GenAI Ecosystem](https://neo4j.com/labs/genai-ecosystem/)
*   [LLM Knowledge Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/)
*   [Vector Index & Search](https://neo4j.com/labs/genai-ecosystem/vector-search/)
*   [LangChain](https://neo4j.com/labs/genai-ecosystem/langchain/)
*   [LangChain.js](https://neo4j.com/labs/genai-ecosystem/langchain-js/)
*   [LlamaIndex](https://neo4j.com/labs/genai-ecosystem/llamaindex/)
*   [Haystack](https://neo4j.com/labs/genai-ecosystem/haystack/)
*   [DSPy](https://neo4j.com/labs/genai-ecosystem/dspy/)

**Developer Tools**
*   [APOC Extended](https://neo4j.com/labs/apoc/)
*   [Aura CLI](https://neo4j.com/labs/aura-cli/)
*   [arrows.app](https://neo4j.com/labs/arrows/)
*   [Cypher Workbench](https://neo4j.com/labs/cypher-workbench/)
*   [ETL Tool](https://neo4j.com/labs/etl-tool/)
*   [NeoDash](https://neo4j.com/labs/neodash/)

**Frameworks & Integrations**
*   [Needle Starter Kit](https://neo4j.com/labs/neo4j-needle-starterkit/)
*   [Neo4j Plugin for Liquibase](https://neo4j.com/labs/liquibase/)
*   [Neo4j Migrations](https://neo4j.com/labs/neo4j-migrations/)
*   [neomodel](https://neo4j.com/labs/neomodel/)

[RDF & Linked Data](https://neo4j.com/labs/neosemantics/)
*   [Neosemantics (Java)](https://neo4j.com/labs/neosemantics/)
*   [RDFLib-Neo4j (Python)](https://neo4j.com/labs/rdflib-neo4j/)

[Get Help](https://neo4j.com/developer/resources/)

[Community Forum](https://dev.neo4j.com/forum)

[Discord Chat](https://dev.neo4j.com/chat)

[Product Support](http://support.neo4j.com/)

[Neo4j Developer Blog](https://neo4j.com/blog/developer/)

[Neo4j Videos](https://neo4j.com/videos/)

[GraphAcademy](https://graphacademy.neo4j.com/?ref=docs-nav)

[Beginners Courses](https://graphacademy.neo4j.com/categories/beginners/?ref=docs-nav)
*   [Neo4j Fundamentals](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/?ref=docs-nav)
*   [Cypher Fundamentals](https://graphacademy.neo4j.com/courses/cypher-fundamentals/?ref=docs-nav)
*   [Importing Data Fundamentals](https://graphacademy.neo4j.com/courses/importing-fundamentals/?ref=docs-nav)
*   [Importing CSV Data](https://graphacademy.neo4j.com/courses/importing-csv-data/?ref=docs-nav)
*   [Graph Data Modeling](https://graphacademy.neo4j.com/courses/modeling-fundamentals/?ref=docs-nav)

[Data Scientist Courses](https://graphacademy.neo4j.com/categories/data-scientist/?ref=docs-nav)
*   [Into to Graph Data Science](https://graphacademy.neo4j.com/courses/gds-product-introduction/?ref=docs-nav)
*   [Graph Data Science Fundamentals](https://graphacademy.neo4j.com/courses/graph-data-science-fundamentals/?ref=docs-nav)
*   [Path Finding](https://graphacademy.neo4j.com/courses/gds-shortest-paths/?ref=docs-nav)

[Generative AI Courses](https://graphacademy.neo4j.com/categories/llms/?ref=docs-nav)
*   [Neo4j & LLM Fundamentals](https://graphacademy.neo4j.com/courses/llm-fundamentals/?ref=docs-nav)
*   [Vector Indexes & Unstructured Data](https://graphacademy.neo4j.com/courses/llm-vectors-unstructured/?ref=docs-nav)
*   [Build a Chatbot with Python](https://graphacademy.neo4j.com/courses/llm-chatbot-python/?ref=docs-nav)
*   [Build a Chatbot with TypeScript](https://graphacademy.neo4j.com/courses/llm-chatbot-typescript/?ref=docs-nav)

[Neo4j Certification](https://graphacademy.neo4j.com/certification/?ref=docs-nav)
*   [Neo4j Certified Professional](https://graphacademy.neo4j.com/certifications/neo4j-certification/?ref=docs-nav)
*   [Neo4j Graph Data Science Certification](https://graphacademy.neo4j.com/certifications/gds-certification/?ref=docs-nav)

[Get Started Free](https://console.neo4j.io/?ref=docs-nav-get-started)

[Search](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#search)

[Skip to content](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#skip-to-content "Skip to content")

Neo4j GraphQL Library

Product Version

*       *   [Introduction](https://neo4j.com/docs/graphql/5/)
    *   **Getting started**
    *   [Creating a new project](https://neo4j.com/docs/graphql/5/getting-started/)
    *   [Neo4j GraphQL Toolbox](https://neo4j.com/docs/graphql/5/getting-started/toolbox/)
    *   **Reference**
    *   [Security](https://neo4j.com/docs/graphql/5/security/)
        *   [Configuration](https://neo4j.com/docs/graphql/5/security/configuration/)
        *   [Authentication](https://neo4j.com/docs/graphql/5/security/authentication/)
        *   [Authorization](https://neo4j.com/docs/graphql/5/security/authorization/)
        *   [Subscriptions authorization](https://neo4j.com/docs/graphql/5/security/subscriptions-authorization/)
        *   [Impersonation and user switching](https://neo4j.com/docs/graphql/5/security/impersonation-and-user-switching/)
        *   [Operation examples](https://neo4j.com/docs/graphql/5/security/operations/)

    *   [Types](https://neo4j.com/docs/graphql/5/types/)
        *   [Scalar](https://neo4j.com/docs/graphql/5/types/scalar/)
        *   [Temporal](https://neo4j.com/docs/graphql/5/types/temporal/)
        *   [Spatial](https://neo4j.com/docs/graphql/5/types/spatial/)
        *   [Interfaces](https://neo4j.com/docs/graphql/5/types/interfaces/)
        *   [Union](https://neo4j.com/docs/graphql/5/types/unions/)
        *   [Relationships](https://neo4j.com/docs/graphql/5/types/relationships/)

    *   [Filtering](https://neo4j.com/docs/graphql/5/filtering/)
    *   [The `Neo4jGraphQL` class](https://neo4j.com/docs/graphql/5/neo4jgraphql-class/)
    *   [Directives](https://neo4j.com/docs/graphql/5/directives/)
        *   [Database mapping](https://neo4j.com/docs/graphql/5/directives/database-mapping/)
        *   [Autogeneration](https://neo4j.com/docs/graphql/5/directives/autogeneration/)
        *   [Schema configuration](https://neo4j.com/docs/graphql/5/directives/schema-configuration/)
            *   [Global configuration](https://neo4j.com/docs/graphql/5/directives/schema-configuration/global-configuration/)
            *   [Type configuration](https://neo4j.com/docs/graphql/5/directives/schema-configuration/type-configuration/)
            *   [Field configuration](https://neo4j.com/docs/graphql/5/directives/schema-configuration/field-configuration/)

        *   [Indexes and constraints](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/)
        *   [Custom logic](https://neo4j.com/docs/graphql/5/directives/custom-logic/)
        *   [Custom directives](https://neo4j.com/docs/graphql/5/directives/custom-directives/)

    *   [Queries and aggregations](https://neo4j.com/docs/graphql/5/queries-aggregations/)
        *   [Queries](https://neo4j.com/docs/graphql/5/queries-aggregations/queries/)
        *   [Aggregations](https://neo4j.com/docs/graphql/5/queries-aggregations/aggregations/)
        *   [Sorting](https://neo4j.com/docs/graphql/5/queries-aggregations/sorting/)
        *   [Pagination](https://neo4j.com/docs/graphql/5/queries-aggregations/pagination/)

    *   [Mutations](https://neo4j.com/docs/graphql/5/mutations/)
        *   [`create`](https://neo4j.com/docs/graphql/5/mutations/create/)
        *   [`update`](https://neo4j.com/docs/graphql/5/mutations/update/)
        *   [`delete`](https://neo4j.com/docs/graphql/5/mutations/delete/)

    *   [Subscriptions](https://neo4j.com/docs/graphql/5/subscriptions/)
        *   [Getting started](https://neo4j.com/docs/graphql/5/subscriptions/getting-started/)
        *   [Events](https://neo4j.com/docs/graphql/5/subscriptions/events/)
        *   [Filtering](https://neo4j.com/docs/graphql/5/subscriptions/filtering/)
        *   [Horizontal scaling](https://neo4j.com/docs/graphql/5/subscriptions/scaling/)
        *   [Engines](https://neo4j.com/docs/graphql/5/subscriptions/engines/)

    *   **How-To**
    *   [Driver configuration](https://neo4j.com/docs/graphql/5/driver-configuration/)
    *   **Products**
    *   [Introspector](https://neo4j.com/docs/graphql/5/introspector/)
    *   [OGM](https://neo4j.com/docs/graphql/5/ogm/)
        *   [Installation](https://neo4j.com/docs/graphql/5/ogm/installation/)
        *   [Directives](https://neo4j.com/docs/graphql/5/ogm/directives/)
        *   [Selection set](https://neo4j.com/docs/graphql/5/ogm/selection-set/)
        *   [Type generation](https://neo4j.com/docs/graphql/5/ogm/type-generation/)
        *   [How to use the OGM with subscriptions](https://neo4j.com/docs/graphql/5/ogm/subscriptions/)
        *   [API Reference](https://neo4j.com/docs/graphql/5/ogm/reference/)

    *   **Frameworks and integrations**
    *   [Apollo Federation](https://neo4j.com/docs/graphql/5/integrations/apollo-federation/)
    *   [Relay Compatibility](https://neo4j.com/docs/graphql/5/integrations/relay-compatibility/)
    *   **Versions and support**
    *   [Migration guide](https://neo4j.com/docs/graphql/5/migration/)
    *   [Deprecations](https://neo4j.com/docs/graphql/5/deprecations/)
    *   [Optimization](https://neo4j.com/docs/graphql/5/optimization/)
    *   [Troubleshooting](https://neo4j.com/docs/graphql/5/troubleshooting/)

**Is this page helpful?**

[](https://neo4j.com/docs)
*   [Neo4j GraphQL Library](https://neo4j.com/docs/graphql/5/)
*   [Directives](https://neo4j.com/docs/graphql/5/directives/)
*   [Indexes and constraints](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/)

[Raise an issue](https://github.com/neo4j/docs-graphql/issues/new/?title=Docs%20Feedback%20modules/ROOT/pages/directives/indexes-and-constraints.adoc%20(ref:%205.x)&body=%3E%20Do%20not%20include%20confidential%20information,%20personal%20data,%20sensitive%20data,%20or%20other%20regulated%20data.)

Indexes and constraints
=======================

This page describes how to use indexes and constraints in the Neo4j GraphQL Library.

[](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_fulltext)`@fulltext`
---------------------------------------------------------------------------------------------

### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_definition)Definition

You can use the `@fulltext` directive to add a [Full text index](https://neo4j.com/docs/cypher-manual/current/indexes-for-full-text-search/) inside Neo4j. For example:

Copied!

```graphql
input FullTextInput {
  indexName: String
  queryName: String
  fields: [String]!
}

"""
Informs @neo4j/graphql that there should be a fulltext index in the database, allows users to search by the index in the generated schema.
"""
directive @fulltext(indexes: [FullTextInput]!) on OBJECT
```

Using this directive does not automatically ensure the existence of these indexes. You need to run a function on server startup. See the section [Asserting constraints](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_asserting_constraints) for details.

### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_usage)Usage

The `@fulltext` directive can be used on nodes. In this example, a `Fulltext` index called "ProductName", for the name `field`, on the `Product` node, is added:

Copied!

```graphql
type Product @fulltext(indexes: [{ indexName: "ProductName", fields: ["name"] }]) {
    name: String!
    color: Color! @relationship(type: "OF_COLOR", direction: OUT)
}
```

When you run [Asserting constraints](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_asserting_constraints), they create the index like so:

Copied!

```cypher
CREATE FULLTEXT INDEX ProductName FOR (n:Product) ON EACH [n.name]
```

For every index specified, a new top level query is generated by the library. For example, for the previous type definitions, the following query and types are generated:

Copied!

```graphql
type Query {
    productsFulltextProductName(phrase: String!, where: ProductFulltextWhere, sort: [ProductFulltextSort!],
    limit: Int, offset: Int): [ProductFulltextResult!]!
}

"""The result of a fulltext search on an index of Product"""
type ProductFulltextResult {
  score: Float
  product: Product
}

"""The input for filtering a fulltext query on an index of Product"""
input ProductFulltextWhere {
  score: FloatWhere
  product: ProductWhere
}

"""The input for sorting a fulltext query on an index of Product"""
input ProductFulltextSort {
  score: SortDirection
  product: ProductSort
}

"""The input for filtering the score of a fulltext search"""
input FloatWhere {
  min: Float
  max: Float
}
```

[View all (13 more lines)](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/)

This query can then be used to perform a [Lucene full-text query](https://lucene.apache.org/) to match and return products. Here is an example of this:

Copied!

```graphql
query {
  productsFulltextProductName(phrase: "Hot sauce", where: { score: { min: 1.1 } } sort: [{ product: { name: ASC } }]) {
    score
    product {
      name
    }
  }
}
```

This query produces results in the following format:

Copied!

```json
{
  "data": {
    "productsFulltextProductName": [
      {
        "score": 2.1265015602111816,
        "product": {
          "name": "Louisiana Fiery Hot Pepper Sauce"
        }
      },
      {
        "score": 1.2077560424804688,
        "product": {
          "name": "Louisiana Hot Spiced Okra"
        }
      },
      {
        "score": 1.3977186679840088,
        "product": {
          "name": "Northwoods Cranberry Sauce"
        }
      }
    ]
  }
}
```

[View all (9 more lines)](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/)

Additionally, it is possible to define a custom query name as part of the `@fulltext` directive by using the `queryName` argument:

Copied!

```graphql
type Product @fulltext(indexes: [{ queryName: "CustomProductFulltextQuery", indexName: "ProductName", fields: ["name"] }]) {
    name: String!
    color: Color! @relationship(type: "OF_COLOR", direction: OUT)
}
```

This produces the following top-level query:

Copied!

```graphql
type Query {
    CustomProductFulltextQuery(phrase: String!, where: ProductFulltextWhere, sort: [ProductFulltextSort!],
    limit: Int, offset: Int): [ProductFulltextResult!]!
}
```

This query can then be used like this:

Copied!

```graphql
query {
  CustomProductFulltextQuery(phrase: "Hot sauce", sort: [{ score: ASC }]) {
    score
    product {
      name
    }
  }
}
```

[](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_unique)`@unique`
-----------------------------------------------------------------------------------------

### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_definition_2)Definition

Unique node property constraints map to `@unique` directives used in your type definitions. They have the following definition:

Copied!

```graphql
"""Informs @neo4j/graphql that there should be a uniqueness constraint in the database for the decorated field."""
directive @unique(
    """The name which should be used for this constraint. By default; type name, followed by an underscore, followed by the field name."""
    constraintName: String
) on FIELD_DEFINITION
```

Using this directive does not automatically ensure the existence of these constraints. Run a function on server startup. See section [Asserting constraints](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_asserting_constraints) for details.

### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_usage_2)Usage

`@unique` directives can only be used in GraphQL object types representing nodes, and they are only applicable for the "main" label for the node.

In the following example, a unique constraint is asserted for the label `Colour` and the property `hexadecimal`:

Copied!

```graphql
type Colour {
    hexadecimal: String! @unique
}
```

In the next example, a unique constraint with name `unique_colour` is asserted for the label `Colour` and the property `hexadecimal`:

Copied!

```graphql
type Colour {
    hexadecimal: String! @unique(constraintName: "unique_colour")
}
```

The `@node` directive is used to change the database label mapping in this next example, so a unique constraint is asserted for the first label in the list, `Color`, and the property `hexadecimal`:

Copied!

```graphql
type Colour @node(labels: ["Color"]) {
    hexadecimal: String! @unique
}
```

In the following example, all labels specified in the `labels` argument of the `@node` directive are also checked when asserting constraints. If there is a unique constraint specified for the `hexadecimal` property of nodes with the `Hue` label, but not the `Color` label, no error is thrown and no new constraints are created when running `assertIndexesAndConstraints`.

Copied!

```graphql
type Colour @node(labels: ["Color", "Hue"]) {
    hexadecimal: String! @unique
}
```

[](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_asserting_constraints)Asserting constraints
--------------------------------------------------------------------------------------------------------------------

In order to ensure that the specified constraints exist in the database, you need to run the function `assertIndexesAndConstraints`. A simple example to create the necessary constraints might look like the following, assuming a valid driver instance in the variable `driver`. This creates two constraints, one for each field decorated with `@id` and `@unique`, and apply the indexes specified in `@fulltext`:

Copied!

```javascript
const typeDefs = `#graphql
    type Color {
        id: ID! @id
        hexadecimal: String! @unique
    }

    type Product @fulltext(indexes: [{ indexName: "ProductName", fields: ["name"] }]) {
        name: String!
        color: Color! @relationship(type: "OF_COLOR", direction: OUT)
    }
`;

const neoSchema = new Neo4jGraphQL({ typeDefs, driver });

const schema = await neoSchema.getSchema();

await neoSchema.assertIndexesAndConstraints({ options: { create: true }});
```

[](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_vector_index_search)`@vector`
------------------------------------------------------------------------------------------------------

With the `@vector` GraphQL directive you can query your database to perform a vector index search. Queries are performed by passing in either a vector index or a query phrase.

A query by vector index finds nodes with a vector embedding similar to that index. That is, the query performs a nearest neighbor search.

In contrast, a query by phrase (a string of text) forwards the phrase to the [Neo4j GenAI plugin](https://neo4j.com/docs/cypher-manual/current/genai-integrations/) and the plugin generates a vector embedding for it. This embedding is then compared to the node vector embeddings in the database.

Prerequisites

*   The database must be Neo4j version 5.15 or higher.

*   The node vector embeddings already exist in the database. See [Vector indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/) to learn more about vector indexes in Cypher and Neo4j.

*   The embeddings must have been created using the same method, that is, the same provider and model. See [Embeddings & Vector Indexes Tutorial](https://neo4j.com/docs/genai/tutorials/embeddings-vector-indexes/) to learn about vector embeddings in Cypher and Neo4j.

*   Queries by vector index cannot be performed across multiple labels.

*   Queries by phrase require credentials for the Neo4j GenAI plugin.

Vector index searches are _read-only_ in the sense that the data which the queries operate on are retrieved from the database but not altered or written back to the database.

### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_definition_3)Definition

Copied!

```graphql
"""Informs @neo4j/graphql that there should be a vector index in the database, allows users to search by the index in the generated schema."""
directive @vector(indexes: [VectorIndexInput]!) on OBJECT
```

`VectorIndexInput` is defined as follows:

Copied!

```graphql
input VectorIndexInput {
  """(Required) The name of the vector index."""
  indexName: String!
  """(Required) The name of the embedding property on the node."""
  embeddingProperty: String!
  """(Required) The name of the query."""
  queryName: String
  """(Optional) The name of the provider."""
  provider: String
}
```

If the optional field `provider` is set, the type is used for a query by phrase, otherwise for a query by vector. Allowed values for the `provider` field are defined by the available [GenAI providers](https://neo4j.com/docs/cypher-manual/current/genai-integrations/#ai-providers).

### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_usage_3)Usage

#### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_query_by_vector_index)Query by vector index

Perform a nearest neighbor search by passing a vector to find nodes with a vector embedding similar to that vector.

Type definition

Type definition

Copied!

```graphql
type Product @vector(indexes: [{
  indexName: "productDescriptionIndex",
  embeddingProperty: "descriptionVector",
  queryName: "searchByDescription"
}]) {
  id: ID!
  name: String!
  description: String!
}
```

This defines the query to be performed on all `Product` nodes which have a vector index named `productDescriptionIndex` for the property `descriptionVector`, implying that a vector embedding has been created for the `description` property of each node.

Example query

Example query

Copied!

```graphql
query FindSimilarProducts($vector: [Float]!) {
  searchByDescription(vector: $vector) {
    edges {
      cursor
      score
      node {
          id
          name
          description
      }
    }
  }
}
```

The input `$vector` is a list of `FLOAT` values and should look similar to this:

An example vector

An example vector

Copied!

```graphql
{
  "vector": [
    0.123456,
    ...,
    0.654321,
  ]
}
```

The query returns all `Product` nodes with a vector embedding on their `descriptionVector` property which is similar to the query argument `$vector`.

#### [](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_query_by_phrase)Query by phrase

Perform a query which utilizes the [Neo4j GenAI plugin](https://neo4j.com/docs/cypher-manual/current/genai-integrations/) to create a vector embedding for a search phrase and then compare it to existing vector embeddings on nodes in the database.

Requires credentials for the plugin.

Ensure your provider credentials are set in the call to Neo4jGraphQL, for example:

Feature configuration

Feature configuration

Copied!

```javascript
const neoSchema = new Neo4jGraphQL({
    typeDefs,
    driver,
    features: {
        vector: {
            OpenAI: {
                token: "my-open-ai-token",
                model: "text-embedding-3-small",
            },
        },
    },
});
```

`OpenAI` is one of the GenAI providers for generating vector embeddings. See [GenAI providers](https://neo4j.com/docs/cypher-manual/current/genai-integrations/#ai-providers) for the full list of providers and their respective identifiers.

Type definition

Type definition

Copied!

```graphql
type Product @vector(indexes: [{
  indexName: "productDescriptionIndex",
  embeddingProperty: "descriptionVector",
  provider: OPEN_AI,  # Assuming this is configured in the server
  queryName: "searchByPhrase"
}]) {
  id: ID!
  name: String!
  description: String!
}
```

This defines the query to be performed on all `Product` nodes which have a vector index named `productDescriptionIndex` for the property `descriptionVector`, implying that a vector embedding has been created for the `description` property of each node.

Example query

Example query

Copied!

```graphql
query SearchProductsByPhrase($phrase: String!) {
  searchByPhrase(phrase: $phrase) {
    edges {
      cursor
      score
      node {
          id
          name
          description
      }
    }
  }
}
```

First, the query passes the query phrase argument `$phrase` to the GenAI plugin and lets it generate a vector embedding for the phrase. Then it returns all `Product` nodes with a vector embedding on their `descriptionVector` property which are similar to the vector embedding generated by the plugin.

[Field configuration](https://neo4j.com/docs/graphql/5/directives/schema-configuration/field-configuration/)[Custom logic](https://neo4j.com/docs/graphql/5/directives/custom-logic/)

Contents
--------

*   [`@fulltext`](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_fulltext)
*   [Definition](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_definition)
*   [Usage](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_usage)
*   [`@unique`](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_unique)
*   [Definition](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_definition_2)
*   [Usage](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_usage_2)
*   [Asserting constraints](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_asserting_constraints)
*   [`@vector`](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_vector_index_search)
*   [Definition](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_definition_3)
*   [Usage](https://neo4j.com/docs/graphql/5/directives/indexes-and-constraints/#_usage_3)

Learn
-----

*   [Sandbox](https://neo4j.com/sandbox/?ref=developer-footer)
*   [Neo4j Community Site](https://community.neo4j.com/?ref=developer-footer)
*   [Neo4j Developer Blog](https://medium.com/neo4j)
*   [Neo4j Videos](https://www.youtube.com/neo4j)
*   [GraphAcademy](https://neo4j.com/graphacademy/?ref=developer-footer)
*   [Neo4j Labs](https://neo4j.com/labs/?ref=developer-footer)

Social
------

*   [Twitter](https://twitter.com/neo4j)
*   [Meetups](https://www.meetup.com/Neo4j-Online-Meetup/)
*   [Github](https://github.com/neo4j/neo4j)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/neo4j)
*   [Want to Speak?](https://docs.google.com/forms/d/e/1FAIpQLSdEcNnMruES5iwvOVYovmS1D_P1ZL_HdUOitFrwrvruv5PZvA/viewform)

[Contact Us →](https://neo4j.com/contact-us/?ref=footer)
--------------------------------------------------------

*   US: 1-855-636-4532
*   Sweden +46 171 480 113
*   UK: +44 20 3868 3223
*   France: +33 (0) 1 88 46 13 20

© 2026 Neo4j, Inc.

[Terms](https://neo4j.com/terms/) | [Privacy](https://neo4j.com/privacy-policy/) | [Sitemap](https://neo4j.com/sitemap/)

Neo4j®, Neo Technology®, Cypher®, Neo4j® Bloom™ and Neo4j® Aura™ are registered trademarks of Neo4j, Inc. All other marks are owned by their respective companies.

AI search

###### AI SEARCH

Ask Neo4j anything or try one of the following questions

How do I model data for a graph database?How do I use the MATCH clause in Cypher?How do I use Neo4j with Python?How do I get started with graph algorithms? 

This is an experimental AI chatbot. All information should be verified.

![Image 2](blob:https://neo4j.com/3dac57ff-09ad-4a83-aabc-9f2c80960fc3)
