# Source: https://docs.vespa.ai/en/basics/whats-more.html.md

# What's more

 

The _Vespa basics_ articles introduces the central concepts in Vespa, but can't cover everything needed to build complete applications. Some additional important features are:

- **[Grouping and aggregation](../querying/grouping.html)** (faceting): Grouping in the query language lets you specify hierarchical groupings and aggregations that will be performed over all the matches to a query distributed over all participating nodes. 
- **Streaming search**: In applications where queries search fixed small subsets of all data (such as a user or tenant) it is not cost-effective to build indexes. For these use case Vespa supports a [streaming mode](../performance/streaming-search.html) which delivers low-latency search without the cost of maintaining indexes or even keeping data in memory. 
- **Application components**: Applications can include Java components that implement application logic, such as intercepting queries and results and implement custom workflows ([Searchers](../applications/searchers.html)), modify write operations ([document processors](../applications/document-processors.html)), and implementing custom API's ([handlers](../applications/request-handlers.html)). 
- **Parent-child relations**: Joins are not supported in Vespa because they wouldn't scale, but the special case where one side of the join is much smaller than the other is supported. This is called a [parent-child relation](../schemas/parent-child.html). 
- **Federation**: Most applications federate over multiple types of content. Vespa will federate over all schemas and clusters by default, and includes a [federation framework](../querying/federation.html) which lets you define application specific schemes to formulate queries to each content type, include content from other services, combine content in application-specific ways and so on. 
- **Predicate fields**: Sometimes it is useful to allow documents to specify when they should be matched, as conditions on properties sent with the query, for example to let content target specific kinds of users. This can be done using [predicate fields](../schemas/predicate-fields.html). 
- **Geo search**: By using [geo fields](../querying/geo-search.html), you can find documents within a given area, use distance to the query in ranking, or even retrieve by distance to a path for route planning. 
- **Mutable attributes**: By defining [mutable attributes](../reference/schemas/schemas.html#mutate) on the documents, applications can collect statistics in real time on each document to track how often they are matched, ranked, and returned in results.

Read more in the full [features](../learn/features.html) list.

 Copyright © 2025 - [Cookie Preferences](#)

