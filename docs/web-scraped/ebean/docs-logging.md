# Source: https://ebean.io/docs/logging

Title: Logging | Ebean

URL Source: https://ebean.io/docs/logging

Markdown Content:
Ebean uses [SLF4J](https://www.slf4j.org/) for logging.

Typical logback configuration
-----------------------------

<logger name="io.ebean.DDL" level="TRACE"/>

<logger name="io.ebean.SQL" level="TRACE"/>
<logger name="io.ebean.TXN" level="TRACE"/>
<logger name="io.ebean.SUM" level="TRACE"/>

<!-- L2 logging -->
<logger name="io.ebean.cache.QUERY" level="TRACE"/>
<logger name="io.ebean.cache.BEAN" level="TRACE"/>
<logger name="io.ebean.cache.COLL" level="TRACE"/>
<logger name="io.ebean.cache.NATKEY" level="TRACE"/>

<!-- Testing with Docker containers -->
<logger name="io.ebean.docker" level="TRACE"/>

SQL
---

During development it is expected that you include logging of `io.ebean.SQL` and `io.ebean.TXN`. These log the sql statements executed, bind values for statement execution.

<!-- SQL and bind values -->
<logger name="io.ebean.SQL" level="TRACE"/>

Transaction
-----------

During development it is expected that you include logging of `io.ebean.SQL` and `io.ebean.TXN`. These log the transaction demarcation.

<!-- Transaction Commit and Rollback events -->
<logger name="io.ebean.TXN" level="TRACE"/>

DDL
---

<logger name="io.ebean.DDL" level="TRACE"/>

Docker logging
--------------

Logging of docker commands used to start test containers with [ebean-test](https://ebean.io/docs/testing).

<!-- Docker commands for starting test containers -->
<logger name="io.ebean.docker" level="TRACE"/>

Summary logging
---------------

The summary logging of `io.ebean.SUM` is useful for showing lazy loading queries and how they relate back to origin queries. This is useful when looking at more complex object graphs are built. In tuning queries for N+1 etc.

<!-- Summary level details -->
<logger name="io.ebean.SUM" level="TRACE"/>

L2 Cache logging
----------------

The L2 cache events can be logged using the logger entries below. This is useful when you are starting out using the L2 cache and looking at the behaviour with L2 caching.

<!-- L2 logging -->
<logger name="io.ebean.cache.QUERY" level="TRACE"/>
<logger name="io.ebean.cache.BEAN" level="TRACE"/>
<logger name="io.ebean.cache.COLL" level="TRACE"/>
<logger name="io.ebean.cache.NATKEY" level="TRACE"/>

Elastic logging
---------------

Logging queries and updates to ElasticSearch.

<!-- Elastic logging -->
<logger name="io.ebean.ELA" level="TRACE"/>
<logger name="io.ebean.ELQ" level="TRACE"/>
<logger name="io.ebean.BULK" level="TRACE"/>

[Edit Page](https://github.com/ebean-orm/website-source/blob/master/docs/logging/index.html)

[Next: Query](https://ebean.io/docs/query)
