# Source: https://vincit.github.io/objection.js/guide/transactions.html

Title: Transactions | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/transactions.html

Markdown Content:
Transactions are atomic and isolated units of work in relational databases. If you are not familiar with transactions, I suggest you read up on them. [The wikipedia article(opens new window)](https://en.wikipedia.org/wiki/Database_transaction) is a good place to start.

[#](https://vincit.github.io/objection.js/guide/transactions.html#creating-a-transaction) Creating a transaction
----------------------------------------------------------------------------------------------------------------

In objection, a transaction can be started by calling the [Model.transaction](https://vincit.github.io/objection.js/api/model/static-methods.html#static-transaction) function:

The first argument is a callback that gets called with the transaction object as an argument once the transaction has been successfully started. The transaction object is actually just a [knex transaction object(opens new window)](https://knexjs.org/guide/transactions.html) and you can start the transaction just as well using [knex.transaction(opens new window)](http://knexjs.org/#Transactions) function.

The transaction is committed if the promise returned from the callback is resolved successfully. If the returned Promise is rejected or an error is thrown inside the callback the transaction is rolled back.

The above example works if you have installed a knex instance globally using the `Model.knex()` method. If you haven't, you can pass the knex instance as the first argument to the `transaction` method

Or just simply use `knex.transaction`

TIP

Note: Even if you start a transaction using `Person.transaction` it doesn't mean that the transaction is just for `Persons`. It's just a normal knex transaction, no matter what model you use to start it. You can even use the `Model` base class if you want.

An alternative way to start a transaction is to use the [Model.startTransaction()](https://vincit.github.io/objection.js/api/model/static-methods.html#static-starttransaction) method:

There's also a third way to use transactions, which is described in detail [later](https://vincit.github.io/objection.js/guide/transactions.html#binding-models-to-a-transaction).

[#](https://vincit.github.io/objection.js/guide/transactions.html#using-a-transaction) Using a transaction
----------------------------------------------------------------------------------------------------------

After you have created a transaction, you need to tell objection which queries should be executed inside that transaction. There are two ways to do that:

1.   [By passing the transaction object to each query](https://vincit.github.io/objection.js/guide/transactions.html#passing-around-a-transaction-object)
2.   [By binding models to the transaction](https://vincit.github.io/objection.js/guide/transactions.html#binding-models-to-a-transaction)

### [#](https://vincit.github.io/objection.js/guide/transactions.html#passing-around-a-transaction-object) Passing around a transaction object

The most straightforward way to use a transaction is to explicitly give it to each query you start. [query](https://vincit.github.io/objection.js/api/model/static-methods.html#static-query), [$query](https://vincit.github.io/objection.js/api/model/instance-methods.html#query) and [$relatedQuery](https://vincit.github.io/objection.js/api/model/instance-methods.html#relatedquery) accept a transaction as their last argument.

Note that you can pass either a normal knex instance or a transaction to [query](https://vincit.github.io/objection.js/api/model/static-methods.html#static-query), [$relatedQuery](https://vincit.github.io/objection.js/api/model/instance-methods.html#relatedquery) etc. allowing you to build helper functions and services that can be used with or without a transaction. When a transaction is not wanted, just pass in the normal knex instance (or nothing at all if you have installed the knex object globally using [Model.knex(knex)](https://vincit.github.io/objection.js/api/model/static-methods.html#static-knex)):

### [#](https://vincit.github.io/objection.js/guide/transactions.html#binding-models-to-a-transaction) Binding models to a transaction

The second way to use transactions avoids passing around a transaction object by "binding" model classes to a transaction. You pass all models you want to bind as arguments to the [objection.transaction](https://vincit.github.io/objection.js/api/objection/#transaction) method and as the last argument you provide a callback that receives **copies** of the models that have been bound to a newly started transaction. All queries started through the bound copies take part in the transaction and you don't need to pass around a transaction object. Note that the models passed to the callback are actual copies of the models passed as arguments to [objection.transaction](https://vincit.github.io/objection.js/api/objection/#transaction) and starting a query through any other object will **not** be executed inside a transaction.

You only need to give the [objection.transaction](https://vincit.github.io/objection.js/api/objection/#transaction) function the model classes you use explicitly. All the related model classes are implicitly bound to the same transaction:

The only way you can mess up with the transactions is if you _explicitly_ start a query using a model class that is not bound to the transaction:

The transaction object is always passed as the last argument to the callback:

Originally we advertised this way of doing transactions as a remedy to the transaction passing plague but it has turned out to be pretty error-prone. This approach is handy for single inline functions that do a handful of operations, but becomes tricky when you have to call services and helper methods that also perform database queries. To get the helpers and service functions to participate in the transaction you need to pass around the bound copies of the model classes. If you `require` the same models in the helpers and start queries through them, they will **not** be executed in the transaction since the required models are not the bound copies, but the original models from which the copies were taken.

[#](https://vincit.github.io/objection.js/guide/transactions.html#setting-the-isolation-level) Setting the isolation level
--------------------------------------------------------------------------------------------------------------------------

You can use `raw` to set the isolation level (among other things):
