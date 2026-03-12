# Source: https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/

Title: Query tuning - Cypher Manual

URL Source: https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/

Markdown Content:
Query tuning - Cypher Manual
===============

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#)[Use necessary cookies only](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#)

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

[Search](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#search)

[Skip to content](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#skip-to-content "Skip to content")

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
*   [Execution plans and query tuning](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/)
*   [Query tuning](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/)

[Raise an issue](https://github.com/neo4j/docs-cypher/issues/new/?title=Docs%20Feedback%20modules/ROOT/pages/planning-and-tuning/query-tuning.adoc%20(ref:%20cypher-25)&body=%3E%20Do%20not%20include%20confidential%20information,%20personal%20data,%20sensitive%20data,%20or%20other%20regulated%20data.)

Query tuning
============

Neo4j aims to execute queries as fast as possible. However, when optimizing for maximum query execution performance, it may be helpful to rephrase queries using knowledge about the domain and the application.

This page contains information about how to tune queries using different strategies.

For information about changing the runtime of a query, see the page about [Cypher® runtime concepts](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/runtimes/concepts/).

[](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#_general_recommendations)General recommendations
----------------------------------------------------------------------------------------------------------------------------------

The overall goal of manual query performance optimization is to ensure that only necessary data is retrieved from the graph.

Queries should aim to filter data as early as possible in order to reduce the amount of work that has to be done in the later stages of query execution. This also applies to what gets returned: returning whole nodes and relationships ought to be avoided in favour of selecting and returning only the data that is needed. You should also make sure to set an upper limit on variable-length patterns, so they don’t cover larger portions of the dataset than needed.

Each Cypher® query gets optimized and transformed into an [execution plan](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/execution-plans/) by the Cypher query planner. To minimize the resources used for this, try to use parameters instead of literals when possible. This allows Cypher® to re-use queries instead of having to parse and build new execution plans.

To read more about the execution plan operators mentioned in this section, see [Operators](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/operators/).

[](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#_query_options)Query options
--------------------------------------------------------------------------------------------------------------

Query execution can be fine-tuned through the use of query options.

In order to use one or more of these options, the query must be prepended with `CYPHER`, followed by the query option(s), as exemplified thus:

Copied!

```syntax
CYPHER query-option [further-query-options] query
```

For information about the various runtimes available in Cypher®, see [Cypher runtimes](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/runtimes/).

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-planner)Cypher planner

The Cypher® planner takes a Cypher query and computes an execution plan that solves it. For any given query there is likely a number of execution plan candidates that each solve the query in a different way. The planner uses a search algorithm to find the execution plan with the lowest estimated execution cost.

This table describes the available planner options:

| Query option | Description | Default |
| --- | --- | --- |
| `planner=cost` | Use cost based planning with default limits on plan search space and time. |  |
| `planner=idp` | Synonym for `planner=cost`. |  |
| `planner=dp` | Use cost based planning without limits on plan search space and time to perform an exhaustive search for the best execution plan. Using this option can significantly _increase_ the planning time of the query. |  |

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-connect-components-planner)Cypher connect-components planner

Deprecated

One part of the Cypher® planner is responsible for combining sub-plans for separate patterns into larger plans - a task referred to as _connecting components_.

This table describes the available query options for the connect-components planner:

| Query option | Description | Default |
| --- | --- | --- |
| `connectComponentsPlanner=greedy` | Use a greedy approach when combining sub-plans. Using this option can significantly _reduce_ the planning time of the query. |  |
| `connectComponentsPlanner=idp` | Use the cost based IDP search algorithm when combining sub-plans. Using this option can significantly _increase_ the planning time of the query but usually finds better plans. |  |

The Cypher® query option `connectComponentsPlanner` is deprecated and will be removed without a replacement. The product’s default behavior of using a cost-based IDP search algorithm when combining sub-plans will be kept.

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-update-strategy)Cypher update strategy

This option affects the eagerness of updating queries.

The possible values are:

| Query option | Description | Default |
| --- | --- | --- |
| `updateStrategy=default` | Update queries are executed eagerly when needed. |  |
| `updateStrategy=eager` | Update queries are always executed eagerly. |  |

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-expression-engine)Cypher expression engine

This option affects how the runtime evaluates expressions.

The possible values are:

| Query option | Description | Default |
| --- | --- | --- |
| `expressionEngine=default` | Compile expressions and use the compiled expression engine when needed. |  |
| `expressionEngine=interpreted` | Always use the _interpreted_ expression engine. |  |
| `expressionEngine=compiled` | Always compile expressions and use the _compiled_ expression engine. |  |

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-operator-engine)Cypher operator engine

This query option affects whether the pipelined runtime attempts to generate compiled code for groups of operators.

The possible values are:

| Query option | Description | Default |
| --- | --- | --- |
| `operatorEngine=default` | Attempt to generate compiled operators when applicable. |  |
| `operatorEngine=interpreted` | Never attempt to generate compiled operators. |  |
| `operatorEngine=compiled` | Always attempt to generate _compiled_ operators. Cannot be used together with `runtime=slotted`. |  |

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-interpreted-pipes-fallback)Cypher interpreted pipes fallback

This query option affects how the pipelined runtime behaves for operators it does not directly support.

The available options are:

| Query option | Description | Default |
| --- | --- | --- |
| `interpretedPipesFallback=default` | Equivalent to `interpretedPipesFallback=whitelisted_plans_only`. |  |
| `interpretedPipesFallback=disabled` | If the plan contains any operators not supported by the pipelined runtime then another runtime is chosen to execute the entire plan. Cannot be used together with `runtime=slotted`. |  |
| `interpretedPipesFallback=whitelisted_plans_only` | Parts of the execution plan can be executed on another runtime. Only certain operators are allowed to execute on another runtime. Cannot be used together with `runtime=slotted`. |  |
| `interpretedPipesFallback=all` | Parts of the execution plan may be executed on another runtime. Any operator is allowed to execute on another runtime. Queries with this option set might produce incorrect results, or fail. Cannot be used together with or `runtime=slotted`. This setting is experimental, and using it in a production environment is discouraged. |  |

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-replanning)Cypher replanning

Translating a query string into an efficient execution plan can be an expensive operation. Once an execution plan is obtained for a query, it is placed in a cache. If the exact same query is to be executed again, the planning step is skipped. Instead, the execution plan is obtained from the cache.

"Replanning" refers to cases where a query must be planned again, even though it has been planned before. Cypher® replanning occurs in the following circumstances:

*   When the query is not in the cache. This can either be when the server is first started or restarted, if the cache has recently been cleared, or if [`server.memory.query_cache.per_db_cache_num_entries`](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings#config_server.memory.query_cache.per_db_cache_num_entries) was exceeded.

*   When the time has passed the [`dbms.cypher.min_replan_interval`](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings#config_dbms.cypher.min_replan_interval) value, and the database statistics have changed more than the [`dbms.cypher.statistics_divergence_threshold`](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings#config_dbms.cypher.statistics_divergence_threshold) value.

*   When the cached query plan has notifications that have become invalid. Consider that a query plan had the notification `01N50: Label does not exist`. After adding a node with the label that did not exist before and running the same query again, replanning the query is required.

There may be situations where [Cypher® query planning](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/execution-plans/) can occur at a non-ideal time. For example, when a query must be as fast as possible and a valid plan is already in place.

Replanning is not performed for all queries at once; it is performed in the same thread as running the query, and can block the query. However, replanning one query does not replan any other queries.

There are three different replan options available:

| Option | Description | Default |
| --- | --- | --- |
| `replan=default` | This is the planning and replanning option as described above. |  |
| `replan=force` | This will force a replan, even if the plan is valid according to the planning rules. Once the new plan is complete, it replaces the existing one in the query cache. |  |
| `replan=skip` | If a valid plan already exists, it will be used even if the planning rules would normally dictate that it should be replanned. |  |

The replan option is prepended to queries.

For example:

Copied!

```syntax
CYPHER replan=force MATCH ...
```

In a mixed workload, you can force replanning by using the Cypher® `EXPLAIN` commands. This can be useful to schedule replanning of queries which are expensive to plan, at known times of low load. Using `EXPLAIN` will make sure the query is only planned, but not executed.

For example:

Copied!

```syntax
CYPHER replan=force EXPLAIN MATCH ...
```

During times of known high load, `replan=skip` can be useful to not introduce unwanted latency spikes.

When a schema change is committed while a query is being planned, replanning occurs for the query that is being planned. For example, dropping an index is a schema change. The schema change can make the obtained execution plan invalid or inefficient. Instead of continuing with the obtained execution plan, the query will be planned again. The Cypher® option `replan` does not have any effect on replanning due to schema changes.

### [](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-infer-schema-parts)Cypher infer schema parts

For some queries, the planner can infer predicates such as labels or types from the graph structure, thereby enhancing its ability to estimate the number of rows each operator will produce. (See [Understanding execution plans - Reading execution plans](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/execution-plans/#reading-execution-plans) for more information about the role of operators and estimated row counts in query execution plans.) The option `inferSchemaParts` controls the extent to which the planner should infer predicates.

| Option | Description |
| --- | --- |
| `inferSchemaParts=off` | No predicates are inferred. |
| `inferSchemaParts=most_selective_label` | Relationship types are used to infer labels on connected nodes. The label corresponding to the smallest number of nodes is used to estimate rows. Avoiding the inference of multiple labels improves accuracy for nodes with several dependent labels, such as every `:Actor` being a `:Person`. |

If this query option is not provided, then the value set in [Operations Manual → Configuration settings → dbms.cypher.infer_schema_parts](https://neo4j.com/docs/operations-manual/current/configuration/configuration-settings/#config_dbms.cypher.infer_schema_parts) will be used.

[Parallel runtime: reference](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/runtimes/reference/)[Query caches](https://neo4j.com/docs/cypher-manual/current/query-caches/)

Contents
--------

*   [General recommendations](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#_general_recommendations)
*   [Query options](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#_query_options)
*   [Cypher planner](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-planner)
*   [Cypher connect-components planner](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-connect-components-planner)
*   [Cypher update strategy](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-update-strategy)
*   [Cypher expression engine](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-expression-engine)
*   [Cypher operator engine](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-operator-engine)
*   [Cypher interpreted pipes fallback](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-interpreted-pipes-fallback)
*   [Cypher replanning](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-replanning)
*   [Cypher infer schema parts](https://neo4j.com/docs/cypher-manual/current/planning-and-tuning/query-tuning/#cypher-infer-schema-parts)

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

![Image 2](blob:https://neo4j.com/9bbf2b84-62eb-4313-808f-db391d7cf857)
