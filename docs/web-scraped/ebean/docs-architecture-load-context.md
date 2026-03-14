# Source: https://ebean.io/docs/architecture/load-context

Title: Ebean versus JPA

URL Source: https://ebean.io/docs/architecture/load-context

Markdown Content:
Overview
--------

The job of the `Load Context` is to support secondary loading queries (both eager and lazy) with batch loading (to avoid N + 1) and propagating key query execution context from the origin query to the secondary queries.

Batch Loading
-------------

The load context provides the batch loading mechanism, solving the [N + 1](https://ebean.io/docs/query/nplus1) issue for Ebean. As such, it is one of the most important internal features of Ebean ORM.

Propagate query context
-----------------------

When secondary queries load additional parts of the object graph, Ebean propagates key query execution context from the `origin query` to the secondary queries including:

*   `History` asOf timestamp or version timestamps
*   `Draftable` state
*   `Soft delete` state
*   `Read auditing` state
*   `Document store` state
*   `Read only` state
