# Source: https://tortoise.github.io/transactions.html

Title: Transactions - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/transactions.html

Markdown Content:
Tortoise ORM provides a simple way to manage transactions. You can use the `atomic()` decorator or `in_transaction()` context manager.

`atomic()` and `in_transaction()` can be nested. The inner blocks will create transaction savepoints, and if an exception is raised and then caught outside of a nested block, the transaction will be rolled back to the state before the block was entered. The outermost block will be the one that actually commits the transaction. The savepoints are supported for Postgres, MySQL, MSSQL and SQLite. For other databases, it is advised to propagate the exception to the outermost block to ensure that the transaction is rolled back.

> ```
> # this block will commit changes on exit
> async with in_transaction():
>     await MyModel.create(name='foo')
>     try:
>         # this block will create a savepoint and rollback to it if an exception is raised
>         async with in_transaction():
>             await MyModel.create(name='bar')
>             # this will rollback to the savepoint, meaning that
>             # the 'bar' record will not be created, however,
>             # the 'foo' record will be created
>             raise Exception()
>     except Exception:
>         pass
> ```

When using `asyncio.gather` or similar ways to spin up concurrent tasks in a transaction block, avoid having nested transaction blocks in the concurrent tasks. Transactions are stateful and nested blocks are expected to run sequentially, not concurrently.

tortoise.transactions.atomic(_[connection\_name](https://tortoise.github.io/transactions.html#tortoise.transactions.atomic.connection\_name "tortoise.transactions.atomic.connection\_name (Python parameter) — name of connection to run with, optional if you have only one db connection")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/transactions.html#atomic)[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.atomic "Link to this definition")
Transaction decorator.

You can wrap your function with this decorator to run it into one transaction. If error occurs transaction will rollback.

Parameters:[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.atomic-parameters "Permalink to this headline")connection_name=`None`[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.atomic.connection_name "Permalink to this definition")
name of connection to run with, optional if you have only one db connection

Return type:[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.atomic-return-type "Permalink to this headline")
`Callable`

tortoise.transactions.in_transaction(_[connection\_name](https://tortoise.github.io/transactions.html#tortoise.transactions.in\_transaction.connection\_name "tortoise.transactions.in\_transaction.connection\_name (Python parameter) — name of connection to run with, optional if you have only one db connection")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/transactions.html#in_transaction)[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.in_transaction "Link to this definition")
Transaction context manager.

You can run your code inside `async with in_transaction():` statement to run it into one transaction. If error occurs transaction will rollback.

Parameters:[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.in_transaction-parameters "Permalink to this headline")connection_name=`None`[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.in_transaction.connection_name "Permalink to this definition")
name of connection to run with, optional if you have only one db connection

Return type:[¶](https://tortoise.github.io/transactions.html#tortoise.transactions.in_transaction-return-type "Permalink to this headline")
`TransactionContext`[~T_conn]
