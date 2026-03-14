# Source: https://ebean.io/docs/architecture/compare-jpa

Title: Ebean versus JPA

URL Source: https://ebean.io/docs/architecture/compare-jpa

Markdown Content:
Sessionless architecture
------------------------

JPA is architected such that entity beans must be `attached` to the `PersistenceContext` in order to be `persisted`.

That is, JPA mandates `attach/detach` semantics. This has a number of consequences including:

*   Developers can't easily take control and persist selected objects
*   All attached beans must be in a valid state to flush
*   Flush implicitly flushes all dirty state (so dirty state created _anywhere_ flushes implicitly)
*   Flush can reorder statements in unexpected ways (causing deadlocks)
*   The EntityManager scope must now be managed along with the transaction scope

### Ebean architecture

*   No Entity manager, only manage transactions
*   Dirty state on each entity bean
*   Persisting (save, delete) does not require the PersistenceContext
*   PersistenceContext attached to the Transaction
*   Partially populated beans are always expected

* * *

Persist features
----------------

### JDBC batch control

With JPA there is:

*   No control over JDBC batch size
*   No ability to turn off getGeneratedKeys to optimise large inserts
*   No ability to turn off cascade behavior (to take full control)

Using JDBC batch is important so that we can get optimal performance when persisting. With Ebean there is a JDBC batch buffer attached to the transaction that can seamlessly batch up persistence calls using JDBC batch.

Ebean provides full control over JDBC batch via the transaction, including the `batch size`, `getGeneratedKeys`, and `cascade behavior`. In contrast to JPA, it is easy to fully control and optimise batch processing with Ebean.

### Transaction

Ebean provides the ability on a transaction to:

*   Register transaction callbacks (Post commit callback etc)
*   Set and get user defined objects
*   Specify if L2 cache should be skipped for the transaction

### Raw JDBC

Ebean provides access to the underlying `java.sql.Connection` for performing raw JDBC if needed along with a `transaction.addModification(table, ...)` method to tell Ebean what tables were modified for L2 cache invalidation.

Ebean also has built in `SqlUpdate` and `CallableSql` for easy SQL bulk statements and calling stored procedures.

### Transaction Isolation level

Ebean lets you start a transaction at a higher isolation level. JPA does not support this.

### Stateless updates

Ebean allows us to populate a bean (or object graph) and `update()` without loading the object object. This is useful in REST-like API's where we want to populate an entity object graph from JSON and perform an update.

* * *

Query features
--------------

### findCount

Ebean has built in `findCount` which takes a copy of the query and optimises it for executing a count (by removing fetch, ordering etc). In JPA we would use the `count() function` and can't use the same query to for a `findList` type query.

### findPagedList

JPA has no support for a `PagedList` query that supports finding the "total count" for the query as well as a page of results. (Spring Data JPA helps fill this gap somewhat).

### findEach

JPA has no support for executing large queries. Ebean has `findEach` for executing large queries (cursors / streaming) that takes into account the scope of the persistence context, JDBC driver, fetchSize, and MySql specific treatment (because MySql has specific issues to deal with).

### findMap

JPA has no equivalent to Ebean's `findMap` which returns the objects mapped by a property.

### Async queries

Ebean has built in support for executing queries in the background returning `Futures` with `findFutureList(), findFutureCount() and findFutureIds().` This provides an easy way to execute queries that can be cancelled.

Internally findFutureCount() is used as part of `PagedList` query such that the total count query can be executed in parallel to the findList() query.

### As of history query

JPA has no support for SQL2011 [`AS OF`](https://ebean.io/docs/features/history#as-of-query) queries yet.

### Versions between history query

JPA has no support for SQL2011 [`VERSIONS BETWEEN`](https://ebean.io/docs/features/history#versions-between-query) queries yet.

### Generics

JPA missed using generics with it's initial API and hence has both `Query` and `TypedQuery` which is not ideal.

### JPQL

`JPQL` has both poor support for `partial objects` and poor support for `optimising complex queries for N + 1` by defining what part of the object graph should be fetched.

In it's current state `JPQL` is a poor language for optimising ORM queries. JPA 2.1 added in support for `fetch groups` as a query hint but there are a number of issues with this: being rather inelegant to use, only a query hint with relatively poor support and ultimately missing some important features for controlling object graph construction from mixed sources (L2, L3 and DB).

The emphasis on annotations `FetchType.Eager` and `FetchType.Lazy` and limitations in JPQL has put JPA in a bad position for optimising ORM queries. It will be interesting if they can get to the level of control over object graph construction that Ebean supports.

### Type safe queries

One could argue there is a bit more "ceremony" with JPA Criteria queries that make the query more verbose and harder to read.

##### Ebean "Query beans"

LocalDate today = new LocalDate();

List<Customer> customers =
  new QCustomer()
    .birthday.equalTo(today)
    .createdAt.before(today.minusYears(2))
    .findList();

##### JPA Criteria

LocalDate today = new LocalDate();

EntityManager em = ...;

CriteriaBuilder builder = em.getCriteriaBuilder();
CriteriaQuery<Customer> query = builder.createQuery(Customer.class);
Root<Customer> root = query.from(Customer.class);

Predicate hasBirthday = builder.equal(root.get(Customer_.birthday), today);
Predicate isLongTermCustomer = builder.lessThan(root.get(Customer_.createdAt), today.minusYears(2);
query.where(builder.and(hasBirthday, isLongTermCustomer));

List<Customer> customers = em.createQuery(query.select(root)).getResultList();

Java annotation processing is used by both Ebean (to generate "Query beans") and JPA (to generate [JPA Query Meta model classes](https://docs.jboss.org/hibernate/orm/5.0/topical/html/metamodelgen/MetamodelGenerator.html) in order to provide type safe query construction and execution.

* * *

Mapping
-------

### Constructor

Unlike JPA Ebean does not require a default constructor.

### @View

Ebean has built in support for entities based on database views.

### Entities without @Id

Ebean does not require entities to have an @Id property. These entities are considered "read only" and automatically bypass the persistence context. These entities are typically used for reporting purposes.

### Naming convention

The JPA spec naming convention includes both mixed case and underscores - it is odd. Ebean's default naming convention of `UnderscoreNamingConvention` matches Hibernates `ImprovedNamingStrategy` and not the JPA spec naming convention.

### Auditing & @History

Ebean has built in support for `@WhenCreated`, `@WhenModified`, `@WhoCreated` , `@WhoModified` and full [SQL2011 @History support](https://ebean.io/docs/features/history).

### JSON in DB

Ebean includes mapping support for Postgres JSONB, JSON and similar types for Oracle, MySql (and shortly SQL Server).

### DB ARRAY

Ebean includes mapping support for Postgres ARRAY type.

### @SoftDelete

Ebean includes support for [`@SoftDelete`](https://ebean.io/docs/features/softdelete) with associated delete permanent, cascading behavior and query support.

### @Draftable

Ebean includes support for [`@Draftable`](https://ebean.io/docs/features/draftable) which provides "live" and "editing" capability with `publish()` and `restore()` function.
