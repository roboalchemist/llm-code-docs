# Source: https://ebean.io/docs/transactions

Title: Transactions | Ebean

URL Source: https://ebean.io/docs/transactions

Markdown Content:
@Transactional
--------------

Annotate methods with `@Transactional` and all database queries and changes will occur in a single transaction.

The transaction will use the [default database](https://ebean.io/docs/intro/database/#default), be put into the "thread local scope" and will commit if the methods completes successfully.

@Transactional
public void process(OffsetDateTime startOffset) {
  ...
  customer.save();
  contact.save();
}

Transaction.current()
---------------------

Use `Transaction.current()` to return the current transaction from "thread local scope" of the [default database](https://ebean.io/docs/intro/database/#default).

@Transactional
public void process(OffsetDateTime startOffset) {
  ...
  Transaction txn = Transaction.current();
  ...
}

use `database.currentTransaction()` to return the current transaction for a given database that is typically not the default database.

Database otherDb = DB.byName("other");

Transaction txn = otherDb.currentTransaction();

beginTransaction()
------------------

As an alternative to _@Transactional_ we can use `beginTransaction()` to start an explicit transaction. The transaction is put into the "thread local scope" and used by any subsequent queries, save, delete etc.

We should use a _try with resources_ block to ensure that the transaction is closed if any error occurs in the block.

try (Transaction transaction = DB.beginTransaction()) {

  // do stuff...
  Customer customer = ...
  customer.save();

  Order order = ...
  order.save();

  transaction.commit();
}

#### Kotlin transaction.use { }

Kotlin `use` is used similarly to _try with resources_ to ensure the transaction is closed.

DB.beginTransaction().use { transaction ->

  // do stuff...
  val customer = ...
  customer.save();

  val order = ...
  order.save();

  transaction.commit()
}

commit(), rollback(), end()
---------------------------

Often with a _try with resources_ block we don't need explicit calls to `transaction.rollback()` or `transaction.end()` like the example for [beginTransaction()](https://ebean.io/docs/transactions#beginTransaction) above.

`rollback()` will rollback the transaction and commonly we use that in a catch block.

`end()` will rollback the transaction if it has not already been committed. We primarily use `end()` in a finally block.

Transaction transaction = DB.beginTransaction()
try {
  // do stuff...
  Customer customer = ...
  customer.save();

  Order order = ...
  order.save();

  transaction.commit();

} catch (SomeException e) {
  transaction.rollback();

} finally {
  transaction.end();  // rollback if not committed
}

commitAndContinue()
-------------------

Occasionally in larger transactions we get to a point where we would like to commit the changes to this point but then carry on processing with subsequent changes potentially failing. We use `transaction.commitAndContinue()` for this.

setRollbackOnly()
-----------------

We use `transaction.setRollbackOnly()` such that a transaction will not commit but only rollback.

We can make use of this when some processing has a sort of "preview" mode where we process changes but then do not commit. This can also be useful in some testing scenarios.

createTransaction()
-------------------

`database.createTransaction()` will create a transaction but it will _NOT_ be put in "thread local scope". We generally use this when we have a transaction that we want to pass between threads.

For example: start a transaction, obtain a row lock, if that is successful pass the transaction to a task to execute via a background thread.

When we use `createTransaction()` we must explicitly use the transaction in queries and saving etc. We explicitly specify the transaction with query beans via ... and _model.save(transaction)_ etc.

try (Transaction transaction = DB.getDefault().createTransaction()) {

  ...
  var customer = new QCustomer(transaction) // explicit transaction
    .name.eq("Rob")
    .findOne();
  ...
  customer.update(transaction);  // explicit transaction

}

Implicit transactions
---------------------

When no transactions are specified explicitly Ebean will create a transaction to perform the action.

#### Query - read only transaction

For queries Ebean will look to use a read only transaction. If a `Read Only DataSource` has be configured Ebean will look to use that by default.

#### Insert, Update, Delete

For all persist requests like save, insert, update, delete Ebean will create a transaction and perform a `COMMIT` at the end of the operation.

[Edit Page](https://github.com/ebean-orm/website-source/blob/master/docs/transactions/index.html)

[Next: Batch](https://ebean.io/docs/transactions/batch)
