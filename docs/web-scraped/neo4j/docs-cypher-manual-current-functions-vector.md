# Source: https://neo4j.com/docs/cypher-manual/current/functions/vector/

Title: Vector functions - Cypher Manual

URL Source: https://neo4j.com/docs/cypher-manual/current/functions/vector/

Markdown Content:
Vector functions - Cypher Manual
===============

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/docs/cypher-manual/current/functions/vector/#)[Use necessary cookies only](https://neo4j.com/docs/cypher-manual/current/functions/vector/#)

[![Image 1: Neo4j Docs](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)[Docs](https://neo4j.com/docs/)

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

[Search](https://neo4j.com/docs/cypher-manual/current/functions/vector/#search)

[Skip to content](https://neo4j.com/docs/cypher-manual/current/functions/vector/#skip-to-content "Skip to content")

Cypher Manual

Product Version

*       *   [Introduction](https://neo4j.com/docs/cypher-manual/current/introduction/)
        *   [Overview](https://neo4j.com/docs/cypher-manual/current/introduction/cypher-overview/)
        *   [Cypher and Neo4j](https://neo4j.com/docs/cypher-manual/current/introduction/cypher-neo4j/)
        *   [Cypher and Aura](https://neo4j.com/docs/cypher-manual/current/introduction/cypher-aura/)

    *   [Queries](https://neo4j.com/docs/cypher-manual/current/queries/)
        *   [Core concepts](https://neo4j.com/docs/cypher-manual/current/queries/concepts/)
        *   [Basic queries](https://neo4j.com/docs/cypher-manual/current/queries/basic/)
        *   [Select Cypher version](https://neo4j.com/docs/cypher-manual/current/queries/select-version/)
        *   [Composed queries](https://neo4j.com/docs/cypher-manual/current/queries/composed-queries/)
            *   [Combined queries (`UNION`)](https://neo4j.com/docs/cypher-manual/current/queries/composed-queries/combined-queries/)
            *   [Conditional queries (`WHEN`)](https://neo4j.com/docs/cypher-manual/current/queries/composed-queries/conditional-queries/)
            *   [Sequential queries (`NEXT`)](https://neo4j.com/docs/cypher-manual/current/queries/composed-queries/sequential-queries/)

    *   [Clauses](https://neo4j.com/docs/cypher-manual/current/clauses/)
        *   [Clause composition](https://neo4j.com/docs/cypher-manual/current/clauses/clause-composition/)
        *   [CALL procedure](https://neo4j.com/docs/cypher-manual/current/clauses/call/)
        *   [CREATE](https://neo4j.com/docs/cypher-manual/current/clauses/create/)
        *   [DELETE](https://neo4j.com/docs/cypher-manual/current/clauses/delete/)
        *   [FILTER](https://neo4j.com/docs/cypher-manual/current/clauses/filter/)
        *   [FINISH](https://neo4j.com/docs/cypher-manual/current/clauses/finish/)
        *   [FOREACH](https://neo4j.com/docs/cypher-manual/current/clauses/foreach/)
        *   [LET](https://neo4j.com/docs/cypher-manual/current/clauses/let/)
        *   [LIMIT](https://neo4j.com/docs/cypher-manual/current/clauses/limit/)
        *   [LOAD CSV](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/)
        *   [MATCH](https://neo4j.com/docs/cypher-manual/current/clauses/match/)
        *   [MERGE](https://neo4j.com/docs/cypher-manual/current/clauses/merge/)
        *   [OPTIONAL MATCH](https://neo4j.com/docs/cypher-manual/current/clauses/optional-match/)
        *   [ORDER BY](https://neo4j.com/docs/cypher-manual/current/clauses/order-by/)
        *   [REMOVE](https://neo4j.com/docs/cypher-manual/current/clauses/remove/)
        *   [RETURN](https://neo4j.com/docs/cypher-manual/current/clauses/return/)
        *   [SEARCH](https://neo4j.com/docs/cypher-manual/current/clauses/search/)
        *   [SET](https://neo4j.com/docs/cypher-manual/current/clauses/set/)
        *   [SHOW FUNCTIONS](https://neo4j.com/docs/cypher-manual/current/clauses/listing-functions/)
        *   [SHOW PROCEDURES](https://neo4j.com/docs/cypher-manual/current/clauses/listing-procedures/)
        *   [SHOW SETTINGS](https://neo4j.com/docs/cypher-manual/current/clauses/listing-settings/)
        *   [SHOW TRANSACTIONS](https://neo4j.com/docs/cypher-manual/current/clauses/transaction-clauses/#query-listing-transactions)
        *   [SKIP](https://neo4j.com/docs/cypher-manual/current/clauses/skip/)
        *   [TERMINATE TRANSACTIONS](https://neo4j.com/docs/cypher-manual/current/clauses/transaction-clauses/#query-terminate-transactions)
        *   [UNWIND](https://neo4j.com/docs/cypher-manual/current/clauses/unwind/)
        *   [USE](https://neo4j.com/docs/cypher-manual/current/clauses/use/)
        *   [WHERE](https://neo4j.com/docs/cypher-manual/current/clauses/where/)
        *   [WITH](https://neo4j.com/docs/cypher-manual/current/clauses/with/)

    *   [Subqueries](https://neo4j.com/docs/cypher-manual/current/subqueries/)
        *   [CALL subqueries](https://neo4j.com/docs/cypher-manual/current/subqueries/call-subquery/)
        *   [CALL subqueries in transactions](https://neo4j.com/docs/cypher-manual/current/subqueries/subqueries-in-transactions/)
        *   [COLLECT subqueries](https://neo4j.com/docs/cypher-manual/current/subqueries/collect/)
        *   [COUNT subqueries](https://neo4j.com/docs/cypher-manual/current/subqueries/count/)
        *   [EXISTS subqueries](https://neo4j.com/docs/cypher-manual/current/subqueries/existential/)

    *   [Patterns](https://neo4j.com/docs/cypher-manual/current/patterns/)
        *   [Primer](https://neo4j.com/docs/cypher-manual/current/patterns/primer/)
        *   [Fixed-length patterns](https://neo4j.com/docs/cypher-manual/current/patterns/fixed-length-patterns/)
        *   [Variable-length patterns](https://neo4j.com/docs/cypher-manual/current/patterns/variable-length-patterns/)
        *   [Shortest paths](https://neo4j.com/docs/cypher-manual/current/patterns/shortest-paths/)
        *   [Non-linear patterns](https://neo4j.com/docs/cypher-manual/current/patterns/non-linear-patterns/)
        *   [Match modes](https://neo4j.com/docs/cypher-manual/current/patterns/match-modes/)
        *   [Syntax and semantics](https://neo4j.com/docs/cypher-manual/current/patterns/reference/)

    *   [Values and types](https://neo4j.com/docs/cypher-manual/current/values-and-types/)
        *   [Property, structural, and constructed values](https://neo4j.com/docs/cypher-manual/current/values-and-types/property-structural-constructed/)
        *   [Boolean, numeric, and string literals](https://neo4j.com/docs/cypher-manual/current/values-and-types/boolean-numeric-string/)
        *   [Temporal values](https://neo4j.com/docs/cypher-manual/current/values-and-types/temporal/)
        *   [Spatial values](https://neo4j.com/docs/cypher-manual/current/values-and-types/spatial/)
        *   [Lists](https://neo4j.com/docs/cypher-manual/current/values-and-types/lists/)
        *   [Maps](https://neo4j.com/docs/cypher-manual/current/values-and-types/maps/)
        *   [Vectors](https://neo4j.com/docs/cypher-manual/current/values-and-types/vector/)
        *   [Graph references](https://neo4j.com/docs/cypher-manual/current/values-and-types/graph-references/)
        *   [Working with `null`](https://neo4j.com/docs/cypher-manual/current/values-and-types/working-with-null/)
        *   [Casting data values](https://neo4j.com/docs/cypher-manual/current/values-and-types/casting-data/)
        *   [Equality, ordering, and comparison of value types](https://neo4j.com/docs/cypher-manual/current/values-and-types/ordering-equality-comparison/)

    *   [Expressions](https://neo4j.com/docs/cypher-manual/current/expressions/)
        *   [Predicates](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/)
            *   [Boolean operators](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/boolean-operators/)
            *   [Comparison operators](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/comparison-operators/)
            *   [List operators](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/list-operators/)
            *   [String operators](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/string-operators/)
            *   [Label expression predicates](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/label-expression-predicates/)
            *   [Path pattern expressions](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/path-pattern-expressions/)
            *   [Type predicate expressions](https://neo4j.com/docs/cypher-manual/current/expressions/predicates/type-predicate-expressions/)

        *   [Node and relationship operators](https://neo4j.com/docs/cypher-manual/current/expressions/node-relationship-operators/)
        *   [Mathematical operators](https://neo4j.com/docs/cypher-manual/current/expressions/mathematical-operators/)
        *   [String concatenation operators](https://neo4j.com/docs/cypher-manual/current/expressions/string-operators/)
        *   [Temporal operators](https://neo4j.com/docs/cypher-manual/current/expressions/temporal-operators/)
        *   [List expressions](https://neo4j.com/docs/cypher-manual/current/expressions/list-expressions/)
        *   [Map expressions](https://neo4j.com/docs/cypher-manual/current/expressions/map-expressions/)
        *   [Conditional expressions (CASE)](https://neo4j.com/docs/cypher-manual/current/expressions/conditional-expressions/)

    *   [Functions](https://neo4j.com/docs/cypher-manual/current/functions/)
        *   [Aggregating functions](https://neo4j.com/docs/cypher-manual/current/functions/aggregating/)
        *   [Database functions](https://neo4j.com/docs/cypher-manual/current/functions/database/)
        *   [Graph functions](https://neo4j.com/docs/cypher-manual/current/functions/graph/)
        *   [List functions](https://neo4j.com/docs/cypher-manual/current/functions/list/)
        *   [LOAD CSV functions](https://neo4j.com/docs/cypher-manual/current/functions/load-csv/)
        *   Mathematical functions
            *   [Logarithmic functions](https://neo4j.com/docs/cypher-manual/current/functions/mathematical-logarithmic/)
            *   [Numeric functions](https://neo4j.com/docs/cypher-manual/current/functions/mathematical-numeric/)
            *   [Trigonometric functions](https://neo4j.com/docs/cypher-manual/current/functions/mathematical-trigonometric/)

        *   [Predicate functions](https://neo4j.com/docs/cypher-manual/current/functions/predicate/)
        *   [Scalar functions](https://neo4j.com/docs/cypher-manual/current/functions/scalar/)
        *   [Spatial functions](https://neo4j.com/docs/cypher-manual/current/functions/spatial/)
        *   [String functions](https://neo4j.com/docs/cypher-manual/current/functions/string/)
        *   Temporal functions
            *   [Duration functions](https://neo4j.com/docs/cypher-manual/current/functions/temporal/duration/)
            *   [Instant type functions](https://neo4j.com/docs/cypher-manual/current/functions/temporal/)
            *   [Format functions](https://neo4j.com/docs/cypher-manual/current/functions/temporal/format/)

        *   [User-defined functions](https://neo4j.com/docs/cypher-manual/current/functions/user-defined/)
        *   [Vector functions](https://neo4j.com/docs/cypher-manual/current/functions/vector/)

    *   [Indexes](https://neo4j.com/docs/cypher-manual/current/indexes/)
        *   [Search-performance indexes](https://neo4j.com/docs/cypher-manual/current/indexes/search-performance-indexes/)
            *   [Create indexes](https://neo4j.com/docs/cypher-manual/current/indexes/search-performance-indexes/create-indexes/)
            *   [Show indexes](https://neo4j.com/docs/cypher-manual/current/indexes/search-performance-indexes/list-indexes/)
            *   [Drop indexes](https://neo4j.com/docs/cypher-manual/current/indexes/search-performance-indexes/drop-indexes/)
            *   [The impact of indexes on query performance](https://neo4j.com/docs/cypher-manual/current/indexes/search-performance-indexes/using-indexes/)
            *   [Index hints for the Cypher planner](https://neo4j.com/docs/cypher-manual/current/indexes/search-performance-indexes/index-hints/)

        *   [Semantic indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/)
            *   [Full-text indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/)
            *   [Vector indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/)

        *   [Syntax](https://neo4j.com/docs/cypher-manual/current/indexes/syntax/)

    *   [Schema](https://neo4j.com/docs/cypher-manual/current/schema/)
        *   [Graph types (Preview feature)](https://neo4j.com/docs/cypher-manual/current/schema/graph-types/)
            *   [Set graph types](https://neo4j.com/docs/cypher-manual/current/schema/graph-types/set-graph-types/)
            *   [Extend graph types](https://neo4j.com/docs/cypher-manual/current/schema/graph-types/extend-graph-types/)
            *   [Alter element types](https://neo4j.com/docs/cypher-manual/current/schema/graph-types/alter-element-types/)
            *   [Show graph types](https://neo4j.com/docs/cypher-manual/current/schema/graph-types/list-graph-types/)
            *   [Drop graph type elements](https://neo4j.com/docs/cypher-manual/current/schema/graph-types/drop-graph-type-elements/)

        *   [Constraints](https://neo4j.com/docs/cypher-manual/current/schema/constraints/)
            *   [Create constraints](https://neo4j.com/docs/cypher-manual/current/schema/constraints/create-constraints/)
            *   [Show constraints](https://neo4j.com/docs/cypher-manual/current/schema/constraints/list-constraints/)
            *   [Drop constraints](https://neo4j.com/docs/cypher-manual/current/schema/constraints/drop-constraints/)

        *   [Syntax](https://neo4j.com/docs/cypher-manual/current/schema/syntax/)

    *   [Execution plans and query tuning](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/)
        *   [Understanding execution plans](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/execution-plans/)
        *   [Operators](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/operators/)
            *   [Operators in detail](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/operators/operators-detail/)

        *   [Cypher runtimes](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/runtimes/)
            *   [Concepts](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/runtimes/concepts/)
            *   [Parallel runtime: reference](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/runtimes/reference/)

        *   [Query tuning](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/)

    *   [Query caches](https://neo4j.com/docs/cypher-manual/current/query-caches/)
        *   [Unifying query caches](https://neo4j.com/docs/cypher-manual/current/query-caches/unified-query-caches/)

    *   [Administration](https://neo4j.com/docs/cypher-manual/current/administration/)
    *   [Syntax](https://neo4j.com/docs/cypher-manual/current/syntax/)
        *   [Parsing](https://neo4j.com/docs/cypher-manual/current/syntax/parsing/)
        *   [Naming rules and recommendations](https://neo4j.com/docs/cypher-manual/current/syntax/naming/)
        *   [Variables](https://neo4j.com/docs/cypher-manual/current/syntax/variables/)
        *   [Keywords](https://neo4j.com/docs/cypher-manual/current/syntax/keywords/)
        *   [Parameters](https://neo4j.com/docs/cypher-manual/current/syntax/parameters/)
        *   [Comments](https://neo4j.com/docs/cypher-manual/current/syntax/comments/)

    *   [Additions, deprecations, removals, and compatibility](https://neo4j.com/docs/cypher-manual/current/deprecations-additions-removals-compatibility/)
    *   Appendix
        *   [Cypher styleguide](https://neo4j.com/docs/cypher-manual/current/styleguide/)
        *   [GQL conformance](https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/)
            *   [Supported mandatory GQL features](https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/supported-mandatory/)
            *   [Currently unsupported mandatory GQL features](https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/unsupported-mandatory/)
            *   [Supported optional GQL features](https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/supported-optional/)
            *   [Optional GQL features and analogous Cypher](https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/analogous-cypher/)
            *   [Additional Cypher features](https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/additional-cypher/)

        *   [Tutorials and extended examples](https://neo4j.com/docs/cypher-manual/current/appendix/tutorials/)
            *   [Basic query tuning example](https://neo4j.com/docs/cypher-manual/current/appendix/tutorials/basic-query-tuning/)
            *   [Advanced query tuning example](https://neo4j.com/docs/cypher-manual/current/appendix/tutorials/advanced-query-tuning/)

**Is this page helpful?**

[](https://neo4j.com/docs)
*   [Cypher Manual](https://neo4j.com/docs/cypher-manual/current/introduction/)
*   [Functions](https://neo4j.com/docs/cypher-manual/current/functions/)
*   [Vector functions](https://neo4j.com/docs/cypher-manual/current/functions/vector/)

[Raise an issue](https://github.com/neo4j/docs-cypher/issues/new/?title=Docs%20Feedback%20modules/ROOT/pages/functions/vector.adoc%20(ref:%20cypher-25)&body=%3E%20Do%20not%20include%20confidential%20information,%20personal%20data,%20sensitive%20data,%20or%20other%20regulated%20data.)

Vector functions
================

Vector functions allow you to construct [`VECTOR` values](https://neo4j.com/docs/cypher-manual/current/values-and-types/vector/), compute the similarity and distance of vector pairs, and calculate the size of a vector.

[](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector)vector()

Cypher 25 only Introduced in Neo4j 2025.10
---------------------------------------------------------------------------------------------------------------------------------------

Details**Syntax**`vector(vectorValue, dimension, coordinateType)`
**Description**Constructs a [`VECTOR`](https://neo4j.com/docs/cypher-manual/current/values-and-types/vector/) value.
**Arguments****Name****Type****Description**
`vectorValue``STRING` | `LIST<INTEGER | FLOAT>`The numeric values to create the vector coordinates from.
`dimension``INTEGER`The dimension (number of coordinates) of the vector.
`coordinateType``[INTEGER64, INTEGER32, INTEGER16, INTEGER8, FLOAT64, FLOAT32]`The type of each coordinate in the vector.
**Returns**[`VECTOR`](https://neo4j.com/docs/cypher-manual/current/values-and-types/vector/)

Considerations`VECTOR` values can be [stored as properties](https://neo4j.com/docs/cypher-manual/current/values-and-types/vector/#store-vector-properties).
If a `STRING` is used in `vectorValue`, it must start and end with square brackets (`[]`). The values inside the brackets must be comma-separated numbers, represented in either decimal or scientific notation.
`null`, `NaN`, and `Infinity` values are not allowed as coordinate values.
If `vectorValue` contains elements that are not of the specified `coordinateType`, they will be coerced to that coordinate type if possible. This includes the potential of lossy conversion in cases where a larger type, e.g. `INTEGER64` does not fit into the specified type, e.g. `FLOAT32`.
`dimension` must be greater than `0` and less than or equal to `4096`.
A `null``vectorValue` or `dimension` will return `null`.

Example 1. Construct a `VECTOR` value

Query

Query

Copied!

```cypher
RETURN vector([1, 2, 3], 3, INTEGER) AS vector
```

Result| vector |
| --- |
| `vector([1, 2, 3], 3, INTEGER NOT NULL)` |
| Rows: 1 |

Example 2. Construct a `VECTOR` value with a `STRING` as `vectorValue`

Query

Query

Copied!

```cypher
RETURN vector("[1.05000e+00, 0.123, 5]", 3, FLOAT) AS vector
```

Result| vector |
| --- |
| `vector([1.05, 0.123, 5.0], 3, FLOAT NOT NULL)` |
| Rows: 1 |

Example 3. `null` values

Query

Query

Copied!

```cypher
RETURN vector(null, 3, FLOAT32) AS nullVectorValue,
       vector([1, 2, 3], null, INTEGER8) AS nullDimension
```

Result| nullVectorValue | nullDimension |
| --- | --- |
| `null` | `null` |
| Rows: 1 |

[](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-similarity-cosine)vector.similarity.cosine()
------------------------------------------------------------------------------------------------------------------------

Details**Syntax**`vector.similarity.cosine(a, b)`
**Description**Returns a `FLOAT` representing the similarity between the argument vectors based on their cosine.
**Arguments****Name****Type****Description**
`a``VECTOR` | `LIST<INTEGER | FLOAT>`A vector or list value representing the first vector.
`b``VECTOR` | `LIST<INTEGER | FLOAT>`A vector or list value representing the second vector.
**Returns**`FLOAT`

Considerations`vector.similarity.cosine(null, null)` returns `null`.
`vector.similarity.cosine(null, b)` returns `null`.
`vector.similarity.cosine(a, null)` returns `null`.
Both vectors must be of the same dimension.
Both vectors must be [**valid**](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/#similarity-functions) with respect to cosine similarity.
The implementation is the same of the latest vector index provider (`vector-2.0`).
The similarity score ranges from `0` and `1`, with scores closer to `1` indicating a higher degree of similarity.
The input arguments `a` and `b` accept `VECTOR` values as of Neo4j 2025.10.
Floating point operations are performed with `float32` arithmetic.

For more details, see the [vector index documentation](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/#similarity-functions).

[](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-similarity-euclidean)vector.similarity.euclidean()
------------------------------------------------------------------------------------------------------------------------------

Details**Syntax**`vector.similarity.euclidean(a, b)`
**Description**Returns a `FLOAT` representing the similarity between the argument vectors based on their Euclidean distance.
**Arguments****Name****Type****Description**
`a``VECTOR` | `LIST<INTEGER | FLOAT>`A vector or list value representing the first vector.
`b``VECTOR` | `LIST<INTEGER | FLOAT>`A vector or list value representing the second vector.
**Returns**`FLOAT`

Considerations`vector.similarity.euclidean(null, null)` returns `null`.
`vector.similarity.euclidean(null, b)` returns `null`.
`vector.similarity.euclidean(a, null)` returns `null`.
Both vectors must be of the same dimension.
Both vectors must be [**valid**](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/#similarity-functions) with respect to Euclidean similarity.
The implementation is the same of the latest available vector index provider (`vector-2.0`).
The similarity score ranges from `0` and `1`, with scores closer to `1` indicating a higher degree of similarity.
The input arguments `a` and `b` accept `VECTOR` values as of Neo4j 2025.10.
Floating point operations are performed with `float32` arithmetic.

For more details, see the [vector index documentation](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/#similarity-functions).

Example 4. k-Nearest Neighbors

_k_-nearest neighbor queries return the _k_ entities with the highest similarity scores based on comparing their associated vectors with a query vector. Such queries can be run against vector indexes in the form of _approximate_ _k_-nearest neighbor (k-ANN) queries, whose returned entities have a high probability of being among the true _k_ nearest neighbors. However, they can also be expressed as an exhaustive search using vector similarity functions directly. While this is typically significantly slower than using an index, it is exact rather than approximate and does not require an existing index. This can be useful for one-off queries on small datasets.

To create the graph used in this example, run the following query on an empty Neo4j database:

Copied!

```cypher
CREATE
  (:Node { id: 1, vector: vector([1.0, 4.0, 2.0], 3, FLOAT32) }),
  (:Node { id: 2, vector: vector([3.0, -2.0, 1.0], 3, FLOAT32) }),
  (:Node { id: 3, vector: vector([2.0, 8.0, 3.0], 3, FLOAT32) });
```

Given a parameter `query` (here set to `[4.0, 5.0, 6.0]`), you can query for the two nearest neighbors by Euclidean distance. This is achieved by matching on all candidate vectors and ordering by the similarity score:

Copied!

```cypher
MATCH (node:Node)
WITH node, vector.similarity.euclidean($query, node.vector) AS score
RETURN node, score
ORDER BY score DESCENDING
LIMIT 2
```

This returns the two nearest neighbors.

| node | score |
| --- | --- |
| `(:Node {vector: vector([2.0, 8.0, 3.0], 3, FLOAT32 NOT NULL), id: 3})` | `0.043478261679410934` |
| `(:Node {vector: vector([1.0, 4.0, 2.0], 3, FLOAT32 NOT NULL), id: 1})` | `0.03703703731298447` |
| Rows: 2 |

[](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector_dimension_count)vector_dimension_count()

Cypher 25 only Introduced in Neo4j 2025.10
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Details**Syntax**`vector_dimension_count(vector)`
**Description**Returns the dimension of a `VECTOR`.
**Arguments****Name****Type****Description**
`vector``VECTOR`The vector to calculate the dimension of.
**Returns**`INTEGER`

You can also use the [`size()`](https://neo4j.com/docs/cypher-manual/current/functions/scalar/#functions-size) function to return the dimension of a `VECTOR` value.

Example 5. Calculate the size of a `VECTOR`

Query

Query

Copied!

```cypher
RETURN vector_dimension_count(vector([1, 2, 3], 3, INTEGER8)) AS size
```

Result| size |
| --- |
| `3` |
| Rows: 1 |

[](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector_distance)vector_distance()

Cypher 25 only Introduced in Neo4j 2025.10
---------------------------------------------------------------------------------------------------------------------------------------------------------

Details**Syntax**`vector_distance(vector1, vector2, vectorDistanceMetric)`
**Description**Returns a `FLOAT` representing the distance between the two vector values based on the selected `vectorDistanceMetric` algorithm.
**Arguments****Name****Type****Description**
`vector1``VECTOR`The first vector.
`vector2``VECTOR`The second vector.
`vectorDistanceMetric``[EUCLIDEAN, EUCLIDEAN_SQUARED, MANHATTAN, COSINE, DOT, HAMMING]`The vector distance algorithm to calculate the distance by.
**Returns**`FLOAT`

Supported `vectorDistanceMetric` algorithms| Distance Type | Formula |
| --- | --- |
| `EUCLIDEAN` | √( (A₁ - B₁)² + (A₂ - B₂)² + …​ + (Aᴰ - Bᴰ)² ) |
| `EUCLIDEAN_SQUARED` | (A₁ - B₁)² + (A₂ - B₂)² + …​ + (Aᴰ - Bᴰ)² |
| `MANHATTAN` | |A₁ - B₁| + |A₂ - B₂| + …​ + |Aᴰ - Bᴰ| |
| `COSINE` | 1 - ( (A₁×B₁ + A₂×B₂ + …​ + Aᴰ×Bᴰ) / ( √(A₁² + A₂² + …​ + Aᴰ²) × √(B₁² + B₂² + …​ + Bᴰ²) ) ) |
| `DOT` | - (A₁×B₁ + A₂×B₂ + …​ + Aᴰ×Bᴰ) |
| `HAMMING` | Number of dimensions in which `vector1` and `vector2` differ. |

Considerations The smaller the returned number, the more similar the vectors; the larger the number, the more distant the vectors. This is in contrast to the similarity functions where the closer to `1` the result is the higher the degree of similarity.
Floating point operations are performed with `float32` arithmetic.

Example 6. Calculate the distance between two vectors using the `COSINE` distance

Query

Query

Copied!

```cypher
RETURN vector_distance(vector([1, 2, 3], 3, INTEGER8), vector([1, 2, 4], 3, INTEGER8), COSINE) AS distance
```

Result| distance |
| --- |
| `0.008539855480194092` |
| Rows: 1 |

Example 7. Calculate the distance between two vectors using the `EUCLIDEAN` distance

Query

Query

Copied!

```cypher
RETURN vector_distance(vector([1.0, 5.0, 3.0, 6.7], 4, FLOAT32), vector([5.0, 2.5, 3.1, 9.0], 4, FLOAT32), EUCLIDEAN)
```

Result| distance |
| --- |
| `5.248809337615967` |
| Rows: 1 |

[](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector_norm)vector_norm()

Cypher 25 only Introduced in Neo4j 2025.20
-------------------------------------------------------------------------------------------------------------------------------------------------

Details**Syntax**`vector_norm(vector, vectorDistanceMetric)`
**Description**Returns a `FLOAT` representing the distance between the given vector and an origin vector, which is a vector with the same dimension with all coordinates set to zero, calculated using the specified `vectorDistanceMetric`.
**Arguments****Name****Type****Description**
`vector``VECTOR`A vector for which the norm to the origin vector will be computed.
`vectorDistanceMetric``[EUCLIDEAN, MANHATTAN]`The vector distance algorithm to calculate the distance by.
**Returns**`FLOAT`

Supported `vectorDistanceMetric` algorithms| Distance Type | Formula |
| --- | --- |
| `EUCLIDEAN` | √( (A₁ - B₁)² + (A₂ - B₂)² + …​ + (Aᴰ - Bᴰ)² ) |
| `MANHATTAN` | |A₁ - B₁| + |A₂ - B₂| + …​ + |Aᴰ - Bᴰ| |

Example 8. Measure the norm between a vector and an origin vector using the `EUCLIDEAN` distance

Considerations Floating point operations are performed with `float32` arithmetic.

Query

Query

Copied!

```cypher
RETURN vector_norm(vector([1.0, 5.0, 3.0, 6.7], 4, FLOAT32), EUCLIDEAN) AS norm
```

Result| norm |
| --- |
| `8.93812084197998` |
| Rows: 1 |

Example 9. Measure the norm between a vector and an origin vector using the `EUCLIDEAN` distance

Query

Query

Copied!

```cypher
RETURN vector_norm(vector([1.0, 5.0, 3.0, 6.7], 4, FLOAT32), MANHATTAN) AS norm
```

Result| norm |
| --- |
| `15.699999809265137` |
| Rows: 1 |

[User-defined functions](https://neo4j.com/docs/cypher-manual/current/functions/user-defined/)[Indexes](https://neo4j.com/docs/cypher-manual/current/indexes/)

Contents
--------

*   [vector()](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector)
*   [vector.similarity.cosine()](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-similarity-cosine)
*   [vector.similarity.euclidean()](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-similarity-euclidean)
*   [vector_dimension_count()](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector_dimension_count)
*   [vector_distance()](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector_distance)
*   [vector_norm()](https://neo4j.com/docs/cypher-manual/current/functions/vector/#functions-vector_norm)

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

![Image 2](blob:https://neo4j.com/4ba568b2-a336-4f4d-a250-abcef9ba4888)
