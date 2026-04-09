# Source: https://ebean.io/docs/persist

Title: Persist - Ebean ORM

URL Source: https://ebean.io/docs/persist

Markdown Content:
Save
----

Save will either insert or update the bean depending on its state.

Order order = new Order();
order.setOrderDate(new Date());
...
// insert the order
order.save();

If the bean was fetched it will be updated...

Order order = DB.find(Order.class, 42);
order.setStatus(SHIPPED);
...
// update the order
order.save();

Save and Delete will CASCADE based on the CascadeType specificed on the associated @OneToMany, @OneToOne etc annotation.

By default save and delete will not cascade so you need to specify a cascade type (such as the one on details below) for save() or delete() to cascade.

...
@Entity
@Table(name="orders")
public class Order {

  ...
  @ManyToOne // no cascading
  Customer customer;

  @OneToMany(cascade=CascadeType.ALL) // save and delete cascaded
  List<OrderDetail> details;
	...

Note the _@OneToMany(cascade=CascadeType.ALL)_ on the details property. This means save() and delete() will both casade from order to its order details.

...
// save the order ... will cascade also saving the order details
DB.save(order);

Delete
------

Delete is very similar to save. Just call DB.delete();

...
Order order = DB.find(Order.class, 12);

// delete the order
// ... this will cascade also deleting the order details
// ... with either CascadeType.ALL or CascadeType.REMOVE
DB.delete(order);

Cascading
---------

The mapping annotations @ManyToOne, @OneToMany, @OneToOne and @ManyToMany provide a cascade attribute which is used to control whether saves and deletes are cascaded.

The default is to not cascade a save or delete (as per JPA spec).

The example below shows the Order entity bean with its mapping annotations. If you save an Order the details will be saved as well but the associated customer will not be saved as there is no cascade atttribute and the default is to not cascade.

...
@Entity
@Table(name="orders")
public class Order {
  ...

  @ManyToOne // no cascading
  Customer customer;

  @OneToMany(cascade=CascadeType.ALL)  // save and delete cascaded
  List<OrderDetail> details;

Bulk updates
------------

Update provides a way on issuing a insert, update or delete statement.

This is useful for updating or deleting multiple rows (or a single row) with a single statement (often described as a "bulk" update).

This is also useful if you want to perform an update or delete without having to execute a query first. This is a typical approach for performing an update in a stateless web application.

The statement can be provided in as raw DML with the table names and column names or in a 'logical' form where entity name is used in place of the table name and property names are used in place of column names.

// orm bulk delete use bean name and bean properties
DB.createUpdate(OrderDetail.class, "delete from orderDetail").execute();

// sql bulk update uses table and column names
DB.sqlUpdate("delete from country").execute();

`

Bulk SQL updates
----------------

In similar fashion to [SqlQuery](https://ebean.io/docs/persist#sqlquery) you can specify a SQL INSERT, UPDATE or DELETE statement with named or positioned parameters.

String dml = "update b_bug set title=:title where id = :id";
int rows = DB.sqlUpdate(dml)
  .setParameter("title", "Updated Again")
  .setParameter("id", 1)
  .execute();

CallableSql
-----------

CallableSql provides a way to call a database stored procedure.

String sql = "{call sp_order_mod(?,?)}";
CallableSql cs = DB.createCallableSql(sql);
cs.setParameter(1, "turbo");
cs.registerOut(2, Types.INTEGER);
DB.execute(cs);

// read the out parameter
Integer returnValue = (Integer) cs.getObject(2);

You can extend CallableSql and you can also get the java.sql.Connection from a Transaction and use raw JDBC API to call a stored procedure.

Raw JDBC
--------

You can't always predict when your application requirements can't be met with the features in Ebean. It is nice to know you can easily use raw JDBC if and when you need to.

The java.sql.Connection object can be returned from a transaction, and with that you can perform any raw JDBC calls you like.

This may be useful for Savepoints, advanced Clob/Blob use or advanced stored procedure calls (if CallableSql doesn't do the business for you).

try (Transaction transaction = DB.beginTransaction()) {

  Connection connection = transaction.getConnection();
  // use raw JDBC
  ...

  transaction.commit();
}

JDBC Batch
----------

Ebean provides support for JDBC batch processing. Batch processing groups related SQL statements into a batch and submits them with one call to the database.

Batch settings can be configured through application.properties or through DatabaseConfig, and can be overridden per transaction.

You can set the batch mode for the entity being saved through setBatch() and for its child collections through setCascadeBatch().

...(under construction)... need to provide better guidance on how to determine batch mode, child batch mode, and batch size

Transaction transaction = database.beginTransaction();
try {
  // turn of cascade persist
  transaction.setCascadePersist(false);

  // control the jdbc batch mode and size
  // transaction.setBatchMode(true); // equivalent to transaction.setBatch(PersistBatch.ALL);
  // transaction.setBatchMode(false); // equivalent to transaction.setBatch(PersistBatch.NONE);
  transaction.setBatch(PersistBatch.ALL); // PersistBatch: NONE, INSERT, ALL
  transaction.setCascadeBatch(PersistBatch.INSERT); // PersistBatch: NONE, INSERT, ALL
  transaction.setBatchSize(30);

  // for a large batch insert if you want to skip
  // getting the generated keys
  transaction.setGetGeneratedKeys(false);

  // for batch processing via raw SQL you can inform
  // Ebean what tables were modified so that it can
  // clear the appropriate L2 caches
  String tableName = "customer";
  boolean inserts = true;
  boolean upates = true;
  boolean deletes = false;
  transaction.addModification(tableName, inserts, updates, deletes);

  ...
} finally {
  transaction.end();
}

example using @Transactional

@Transactional(batchSize = 50)
public void goodStuff() {

    order.save()
    customer.save()
}
