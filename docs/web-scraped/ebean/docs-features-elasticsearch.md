# Source: https://ebean.io/docs/features/elasticsearch

Title: ElasticSearch integration and mapping with Ebean ORM

URL Source: https://ebean.io/docs/features/elasticsearch

Markdown Content:
Videos
------

Testing
-------

For how to configure for testing goto [docs / testing / elasticsearch](https://ebean.io/docs/testing/elasticsearch).

Why integrate?
--------------

There are quite a few different reasons why ElasticSearch integration is useful to applications using Ebean ORM.

#### ElasticSearch value

*   Provides 'full text search'
*   Provides something like DB materialised views
*   Scaling read access
*   Read access performance (Document storage)
*   Fixes issues with L2 cache
*   Provides L3 cache

#### Provides 'full text search'

Many modern applications provide a single search input field to operate in a 'Google search' fashion. For example, searching for customers including their name and address (street, city, country etc).

ElasticSearch uses analysers and inverted indexes to make "text search" fast and efficient. OLTP databases generally provide very different indexing via BTree and BitMap indexes which are orientated towards the needs of OLTP (short transactions, self balancing etc).

#### Provides something like DB materialised views

Many databases provide materialised views which are generally derived / calculated views used to provide faster views of the data. Materialised views are often refreshed periodically and used by applications knowing that the derived / calculated data is only refreshed periodically and potentially stale. For example, product pricing might be refreshed every midnight.

ElasticSearch indexes can be viewed in a similar way to DB materialised views. They represent a materialised (document orientated) view of the data which can be updated in near real time with each commit or updated in a more periodic batch fashion.

#### Scaling read access

ElasticSearch architecturally has built in horizontal scaling and this can be used to provide an easier / cheaper way to scale read access when compared to scaling a more traditional OLTP database. Note that the access is not equivalent to that provided by most OLTP databases in that it does not provide the same transactional read consistency guarantees and is 'near' real time (usually lags by a second etc) - however, these limitations are often acceptable given the improved read scalability.

#### Read access performance (denormalised document storage)

ElasticSearch can also be viewed as a document store and often the 'documents' stored are denormalised and contain derived and joined information. This means a retrieve of a single document in elastic search can compete with a SQL query would involve many joins. For example, an Order document might be denormalised and otherwise in a SQL query join Order, OrderDetails, Customer and Product tables.

The traditional downsides of denormalised data exist but when your OLTP database is still the primary data store and ElasticSearch is a secondary store then storing 'denormalised documents' is nicely manageable.

#### Fixes an issue with L2 cache

ElasticSearch can be used as an effective replacement of the **L2 query cache** on types that experience a reasonable amount of insert, update or delete changes.

Essentially if an application is reliant on the `L2 Query cache` on a bean type that is frequently changed (Inserts, updates or deletes) then this will result in load on the database due to ineffective utilisation of the L2 Query cache (as it is frequently invalidated).

ElasticSearch provides many "exact value / term" predicates that map well to "relational" predicates and many relational/orm queries can be reasonably executed against ElasticSearch. If there is a need to scale "find many" queries against frequently updated tables then ElasticSearch can provide a good solution with the caveat that ElasticSearch indexes might be slightly out of date.

#### Provides L3 cache

For Ebean we have the term `L3 cache` which means the remote part of an `L2 cache`. That is, the L2 cache has a "Near cache" and "Remote cache" and "L3 cache" here means the remote part of an L2 cache.

Ebean can use ElasticSearch as an L3 cache (instead of the more traditional Hazelcast/Infinispan/etc distributed caches). If there is a miss in the local L2 cache Ebean can go and hit ElasticSearch rather than the database with the benefits that ElasticSearch is known to have all the data and have it in denormalised form (so a single hit against ElasticSearch might populate more of the graph than a traditional DB hit).

ORM graphs as JSON documents
----------------------------

ORM graphs naturally map to JSON documents. Ebean also has built in support for marshalling/unmarshalling to and from JSON as well as executing large queries efficiently. This makes it is completely natural and reasonable for example to execute a large query over all the objects of a certain type and covert those object graphs to JSON and send to ElasticSearch.

The caveat is that ORM graphs are typically well structured (semi-structured if you include storing JSON in the DB which is well supported by Postgres and Oracle). In terms of mapping ORM graphs to ElasticSearch documents we typically need to take mapping into account such as identifying properties that are 'codes' (and should not be analysed) and identifying properties that we want in analysed and raw form (to support the order by clause for queries).

Automatic sync
--------------

The core integration function is to provide good mechanisms to sync changes to ElasticSearch. That is, when Ebean processes changes to the database it automatically knows what updates it needs to make to the indexes and providing features such that you can control how and when those updates occur.

Ebean determines from the mapping what index update events are required and you can control if these updates are sent to ElasticSearch immediately in the background or queued for later processing or ignored (when you want full control over the indexing).

Query
-----

You can always query ElasticSearch directly without using Ebean and that will fit well with some use cases. In addition Ebean provides good support for executing queries with a number of benefits.

#### Automatic use of 'raw' fields

Ebean will automatically translate expressions to use associated 'raw' fields for sort (order by) clauses and in the case of term expressions. That is, Ebean knows via mapping which properties have associated non-analyzed (raw) fields and will use these where needed (order by and term expression).

#### Persistence Context

Used when we want to fetch from ElasticSearch and then persist to our OLTP DB. The Persistence context is used to de-duplicate beans when the object graph is built from JSON documents giving us a consistent graph (which is what we typically want for persisting). The persistence context also plays a part in query joins (merging multiple JSON sources of the same bean together).

#### Load Context - Lazy loading & query joins

Like ORM queries we can use the Load Context to provide efficient batch lazy loading and query joins. Object graphs built from ElasticSearch can invoke lazy loading (to L2, other indexes and fallback to the OLTP DB when a bean type is mapped to an Elastic index). The Load context also provides "query joins" such that we can build a result by joining to other indexes. For example, fetch from the customer index and join the contacts index (In ElasticSearch terminology this would be described as an "application side join". We can do this efficiently by batch loading as we do in traditional ORM query joins (to avoid N + 1).

#### Query beans - type safe query building

We can use query beans to build the query in a type safe manor which is good for long term maintenance with compile time protection against schema and type changes.

#### Hit DB or Elastic?

The ability to write an ORM query and then painlessly change it to hit ElasticSearch gives application developers the ability to delay the decision and fairly painlessly change between hitting the DB or Elastic. This is not a 'perfect' swap with considerations for case insensitivity of predicates and read consistency (and no support for sub-queries) but for a great many cases this ability to easily swap between the two allows developers to get on with building with the knowledge they can later revisit (and change the implementation to hit Elastic without changing the semantics in terms of persistence context, lazy loading, saving back to the DB etc).

That is, this provides a low barrier path to horizontally scaling reads.

#### useDocStore(true)

On an Ebean query you just need to set `useDocStore(true)` and then the query will execute against ElasticSearch. The only query expressions that can't be translated to ElasticSearch are sub-query expressions - otherwise all the expressions can be translated to ElasticSearch expressions.

##### Example: find paged list

PagedList<Product> products = server.find(Product.class)
  .setUseDocStore(true) // hit Elastic index
  .where().startsWith("sku", "C00")
  .setMaxRows(20)
  .findPagedList();

##### Example: find by id

Product product = server.find(Product.class)
  .setUseDocStore(true) // hit Elastic index
  .setId(1)
  .findOne();

### Mapping relational expressions

Most "relational/exact value" expressions map directly to ElasticSearch expressions with some exceptions.

*   Note that Like, StartsWith, EndsWith and Contains are all effectively case insensitive in ElasticSearch.
*   Sub-query IN - this is currently not supported/translated
*   Sub-query EXISTS - this is currently not supported/translated

### Partial objects - select() and fetch()

Just like ORM queries you can optimise an ElasticSearch query to only fetch the part of the document that you need. You can use the normal Ebean query select() and fetch() to define what part of the document to fetch back and Ebean will apply that to the ElasticSearch query.

List<Customer> customers =
  server.find(Customer.class)
    .useDocStore(true)
    // only fetch id, status and name from index
    // ... as a performance optimisation
    .select("status, name")
    .where().istartWith("name", "Rob")
    .findList();

### Query joins

Like ORM queries you can "query join" multiple indexes.

// fetch from the customer index
// ... "join" the contacts index

List<Customer> customers = server.find(Customer.class)
  .setUseDocStore(true)
  // fetch related contacts from the contacts index
  .fetch("contacts", new FetchConfig().query())
  .findList();

// fetch from the order index
// ... "join" the customer index
//
// internally this merges the customer details
// ... from the order index with the customer details
// ... from the customer index

List<Order> orders = server.find(Order.class)
  .setUseDocStore(true)
  // say the order index only embeds customer(id,name)
  // so we additionally fetch (and merge) all customer
  // details including the billingAddress and shippingAddress
  // from the customer index
  .fetch("customer", new FetchConfig().query())
  .findList();

Support for this can change the decisions on how much denormalisation/embedded documents is used for specific indexes. For example, in an "Order" index you need to decide how much of the customer will be included/embedded into the order. You can embedded the customer(id,name) or customer(id,name,billingAddress(*)) etc. The ability to easily join the "customer index" (to fetch whatever customer details is required) means that you may choose to embed less of the customer into the order document.

Query - Full text
-----------------

Full text query expressions are also exposed by Ebean. These are only used for "document store" queries and are not used for normal ORM queries that go to the OLTP database.

Instead of using `where()` you can use `text()` to add "full text" search expressions to the query like `match`, `multi-match`, `common terms`, `text simple query` and `text query`. These map directly to the corresponding ElasticSearch full text expressions.

Note that when you add a "text expression" the query is automatically set to `useDocStore(true)`.

PagedList<Customer> customers = server.find(Customer.class)
  .text()
    .match("name", "Rob")
    .findPagedList();

PagedList<Customer> customers = server.find(Customer.class)
  .text()
    .match("name", "Rob")
    .match("notes", "kung fu")
    .findPagedList();

PagedList<Customer> customers = server.find(Customer.class)
  .text()
  .must()
    .match("customer.name", "Rob")
    .eq("status", Order.Status.COMPLETE)
    .findPagedList();

MultiMatch match = MultiMatch.fields("name", "notes").boost(2).opAnd();

PagedList<Customer> customers = server.find(Customer.class)
  .text()
    .multiMatch("Rob", match)
    .findPagedList();

Currently out of scope
----------------------

The following features are currently considered out of scope.

#### ElasticSearch parent/child mapping

ElasticSearch provides a parent/child mapping as an alternative to nested/embedded/denormalised approach. At this stage support for this is out of scope and instead the nesting/denormalisation approach is preferred.

Note that Ebean can use "query joins" to fetch join multiple indexes into a single result.
