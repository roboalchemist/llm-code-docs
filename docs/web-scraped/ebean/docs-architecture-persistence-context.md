# Source: https://ebean.io/docs/architecture/persistence-context

Title: Ebean's PersistenceContext

URL Source: https://ebean.io/docs/architecture/persistence-context

Markdown Content:
Videos
------

Definition
----------

Although Ebean doesn't have a JPA Entity Manager, it does have a persistence context. Any ORM worth using needs a persistence context in order to build consistent object graphs.

#### JPA v1.0 specification - section 5.1

> "A persistence context is a set of managed entity instances in which for any persistent entity identity there is a unique entity instance. Within the persistence context, the entity instances and their lifecycle are managed by the entity manager."

Ebean has a persistence context to ensure `unique entity instance.` but has a different approach to the lifecycle management compared with JPA. Ebean has no entity manager and no persist/merge/flush lifecycle methods and the persistence context is not actually involved in persisting.

Unique Entity Instances
-----------------------

Ebean uses the persistence context for queries and lazy loading (when it is building object graphs). This is to ensure that `consistent object graphs` are constructed (1 unique instance per identity).

> Ensuring unique instances equates to building a consistent object graph

For example, in fetching a list of orders and their customers … the persistence context ensures that you only get 1 customer instance for it's given id (e.g. you are NOT allowed to have 2 or more instances of "customer id=7".

The "persistence context" ensures the user/application code works with unique entity instances.

For example, if you didn't have a persistence context and did allow 2 or more instances of "customer 7" … and modified one instance but not the other … things get very ugly.

Persisting
----------

Ebean has a different approach to lifecycle management. With Ebean each bean has it's own dirty checking (detects when it has been modified and holds it's old/original values for optimistic concurrency checking).

This means that Ebean does not need or use the persistence context when persisting beans.

> Ebean's persistence context is not involved in persisting.

With JPA implementations the dirty checking is performed by the entity manager. The entity manager generally holds the old/original values for optimistic concurrency checking and the beans need to be 'attached' to an entity manager to be 'flushed' (as an insert/update/delete). [Note: JDO based JPA implementations do this a bit differently].

Pro's for Ebean's approach:

*   No need to manage Entity Manager's
*   save/delete simpler that attached/detached beans with persist/merge/flush etc

Con's for Ebean's approach:

*   Ebean makes an assumption that scalar types are immutable. Most scalar types (String, Integer, Double, Float, BigDecimal etc) are immutable, but some like `java.util.Date` are not. If you mutate a mutable scalar like `java.util.Date`, Ebean will NOT detect the change – instead you have to set a different `java.util.Date` instance. 

Scopes
------

Ebean has 3 scopes for the the persistence context - `Transaction scope`, `Query scope` and `Per Object Graph scope`.

Transaction scope
-----------------

With Ebean, the persistence context is transaction scoped by default. When you begin a new transaction (implicitly or explicitly) Ebean will start a new persistence context.

The persistence context lives beyond the end of a transaction. This enables any lazy loading done after the transaction ends to use the same persistence context that the instance was created with.

This means, a persistence context

*   Starts when a transaction starts
*   Is used during the transactions scope to build all object graphs (queries)
*   Lives beyond the end of a transaction so that all lazy loading occurring on that object graph also uses the same persistence context 

### Transaction scoped persistence context as a "first level cache"

The persistence context is sometimes described as the "first level cache" or L1 cache. I have also seen it described as the "transactional cache" in that it is most frequently scoped to a transaction.

// a new persistence context started with the transaction
Ebean.beginTransaction();
try {
  // find "order 72" results in that instance being put
  // into the persistence context
  Order order = Ebean.find(Order.class, 72);

  // finds an existing "order 72" in the persistence context
  // ... so just returns that instance
  Order o2 = Ebean.find(Order.class, 72);
  Order o3 = Ebean.getReference(Order.class, 72);

  // all the same instance
  Assert.assertTrue(order == o2);
  Assert.assertTrue(order == o3);
} finally {
  Ebean.endTransaction();
}

The code above shows that there is only 1 instance of "Order 72". As we try to fetch it again, (during the scope of a single persistence context) we end up getting back the same instance.

However, typically we don't write code that fetches the same Order multiple times in a single transaction. The code above is not something we would typically write.

A more realistic example would be when the persistence context is used:

// a new persistence context started with the transaction
Ebean.beginTransaction();

try {
  // find "customer 1" results in this instance being
  // put into the persistence context
  Customer customer = Ebean.find(Customer.class, 1);

  // for this example … "customer 1" placed "order 72"
  // when "order 72" is fetched/built it has a foreign
  // key value customer_id = 1...
  // As customer 1 is already in the persistence context
  // this same instance of customer 1 is used
  Order order = Ebean.find(Order.class, 72);
  Customer customerB = order.getCustomer();

  // they are the same instance
  Assert.assertTrue(customer == customerB);
} finally {
  Ebean.endTransaction();
}

From these examples you should see that the persistence context acts as a cache to some degree. It can sometimes reduce the number of database queries required when you get object graphs and navigate them.

The primary function of the persistence context is to ensure unique instances for a given identity (so that the object graphs are constructed in a consistent manner). That it sometimes looks/acts like a cache is a side effect.

Query Scope
-----------

The purpose of the query scope is to effectively bypass a transaction scoped persistence context (L1 cache) in order to read fresh data from the database.

The general scenario is that you are in the middle of a transaction and you want to make sure that a particular query hits the database to get fresh data. In doing so, we want to avoid using the current transaction-scoped persistence context.

// transaction with a persistence context
Transaction transaction = ...

// Fetch customer 42 hitting the database
// ... ignoring the transaction persistence context
Customer customer = Ebean.find(Customer.class)
      .setId(42)
      // ignore transaction persistence context
      .setPersistenceContextScope(QUERY)
      .findOne();

Object graph scope - large queries
----------------------------------

When you use a `findEach()`, `findStream()` or `findIterate()` streaming type query then Ebean uses a special scope for the persistence context. These queries are expected to iterate through arbitrarily large query requests, so we don't want to hold all the object graphs in memory.

For these streaming queries, Ebean creates a new `PersistenceContext` when iteration occurs and the scope effectively becomes per object graph.
