# Source: https://ebean.io/docs/features/l2cache

Title: L2 Cache | Ebean ORM

URL Source: https://ebean.io/docs/features/l2cache

Markdown Content:
Overview
--------

The goal of the L2 cache is to gain very significant performance improvement by not having to hit the database to read some information.

For example, instead of performing a "find by id" or "find by unique key" query we can get Ebean to effectively lookup the result in the L2 cache. If we are using _near caching_ then this might often result in an in-memory lookup into a local Map and not even require a remote call so be very fast.

It is called the "Level 2 cache" because the persistence context is often referred to as the "Level 1 cache".

The "L2 cache" has 2 main caches – "Bean caches" and "Query caches".

### Bean Caches

Bean caches hold entity beans and are keyed by their _Id_ values and optionally also by their _natural key_. The bean cache can be used with:

*   Find by id(s)
*   Find by natural key(s)

### Query Caches

Query caches hold the results of queries (Lists, Sets, Maps of entity beans and Count) and are keyed by a hash of the query and its bind values.

The entries in a query cache are invalidated by ANY change to the underlying table – insert, update or delete. This means that the query cache is generally only useful on entities that are relatively infrequently modified (typically "lookup tables" such as countries, currencies, status codes etc).

The query cache can be used with:

*   Find list/set/map queries

Eventual consistency
--------------------

Ebean L2 caching uses _eventual consistency_.

This means it operates a bit like "replication lag". Data returned from the L2 cache can be (milliseconds) out of date. Changes will be made to the cache in a relatively short time (milliseconds) but there isn't the guarantee of read consistency that our transactional database provides.

With Ebean L2 caching there is no attempt to provide transactional read consistency. If part of an application needs transactional read consistency then we should _use the database_ to do that.

Invalidation
------------

Ebean will automatically invalidate the cache when [beans are persisted](https://ebean.io/docs/features/l2cache/invalidation#bean) or [update queries](https://ebean.io/docs/features/l2cache/invalidation#table) are executed.

In addition we can explicitly [invalidate parts of the cache](https://ebean.io/docs/features/l2cache/invalidation#explicit) programmatically.

#### Background notification

By default Ebean will perform L2 cache updates and invalidation in the background. If we want cache updates and invalidation to execute in the foreground then we need to set `notifyL2CacheInForeground` to true.

Near cache
----------

A cache that runs in the same process as Ebean is a _Near cache_. Performing a hit against a near cache is an in-memory Map lookup and does not go over the network. Hits against a near cache are very fast - it's effectively a local in-memory Map get().

Ebean L2 bean caches for Redis, Hazelcast and Ignite all have a Near cache option. When this is enabled then there is a local in-process cache that is used and hit first, and then only if there is a miss on the near cache does the request go to the remote Redis | Hazelcast | Ignite cache.

For example, using ebean-redis with bean caching on Customer with near cache enabled:

@Cache(nearCache=true)
@Entity
public class Customer

*   First hit the local in-memory near cache, if hit return the Customer
*   Second, hit the remote Redis cache, if hit return the Customer
*   Third, query the database, return the Customer, also loading Redis cache and near cache

Note that all Query caches are implemented as near cache only.

Regions
-------

We use "Regions" to group caches so that we can enable and disable L2 caching by "region groups".

This provides a mechanism where we can "feature toggle" / enable L2 caching by named regions.

Let's say our application rolls out, and it uses L2 caching for Product (and we call that region "product-region"). Now, we develop further and as part of that want to use L2 caching for Price but, we don't yet want to enable that in all environments (e.g. we don't want it enabled in production). In dev and test we might enable the l2 cache regions "product-region,price-region" but in production only enable "product-region".

@Entity
@Cache(region = "product-region")
public class Product

#### enabledL2Regions

ebean.enabledL2Regions=product-region,price-region

Configuration
-------------

Configuration options that can be set via `DatabaseConfig`.

| Parameter | Default | Description |
| --- | --- | --- |
| disableL2Cache | false | Set to true to globally disable L2 caching |
| enabledL2Regions |  | Set the enabled L2 cache regions (comma delimited). By default all regions are enabled. |
| localOnlyL2Cache | false | Set to true to effectively disable L2 cache plugins (like ebean-redis, ebean-hazelcast) |
| notifyL2CacheInForeground | false | Set to true for cache notifications and invalidation to run in the foreground. Generally we want to perform L2 cache notification in the background and not impact the performance of executing transactions. |
|  |  |  |
| cacheMaxSize | 10000 |  |
| cacheMaxIdleTime | 10mins |  |
| cacheMaxTimeToLive | 6hrs |  |
| queryCacheMaxSize | 1000 |  |
| queryCacheMaxIdleTime | 10mins |  |
| queryCacheMaxTimeToLive | 6hrs |  |
