# Source: https://www.psycopg.org/docs/

Title: Psycopg – PostgreSQL database adapter for Python — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/

Markdown Content:
Psycopg – PostgreSQL database adapter for Python[¶](https://www.psycopg.org/docs/#psycopg-postgresql-database-adapter-for-python "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

[Psycopg](https://psycopg.org/) is the most popular [PostgreSQL](https://www.postgresql.org/) database adapter for the [Python](https://www.python.org/) programming language. Its main features are the complete implementation of the Python [DB API 2.0](https://www.python.org/dev/peps/pep-0249/) specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent `INSERT`s or `UPDATE`s.

Psycopg 2 is mostly implemented in C as a [libpq](https://www.postgresql.org/docs/current/static/libpq.html) wrapper, resulting in being both efficient and secure. It features client-side and [server-side](https://www.psycopg.org/docs/usage.html#server-side-cursors) cursors, [asynchronous communication](https://www.psycopg.org/docs/advanced.html#async-support) and [notifications](https://www.psycopg.org/docs/advanced.html#async-notify), [COPY](https://www.psycopg.org/docs/usage.html#copy) support. Many Python types are supported out-of-the-box and [adapted to matching PostgreSQL data types](https://www.psycopg.org/docs/usage.html#python-types-adaptation); adaptation can be extended and customized thanks to a flexible [objects adaptation system](https://www.psycopg.org/docs/advanced.html#adapting-new-types).

Psycopg 2 is both Unicode and Python 3 friendly.

Contents

* [Installation](https://www.psycopg.org/docs/install.html)
  * [Quick Install](https://www.psycopg.org/docs/install.html#quick-install)
  * [Prerequisites](https://www.psycopg.org/docs/install.html#prerequisites)
  * [Non-standard builds](https://www.psycopg.org/docs/install.html#non-standard-builds)
  * [Running the test suite](https://www.psycopg.org/docs/install.html#running-the-test-suite)
  * [If you still have problems](https://www.psycopg.org/docs/install.html#if-you-still-have-problems)

* [Basic module usage](https://www.psycopg.org/docs/usage.html)
  * [Passing parameters to SQL queries](https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries)
  * [Adaptation of Python values to SQL types](https://www.psycopg.org/docs/usage.html#adaptation-of-python-values-to-sql-types)
  * [Transactions control](https://www.psycopg.org/docs/usage.html#transactions-control)
  * [Server side cursors](https://www.psycopg.org/docs/usage.html#server-side-cursors)
  * [Thread and process safety](https://www.psycopg.org/docs/usage.html#thread-and-process-safety)
  * [Using COPY TO and COPY FROM](https://www.psycopg.org/docs/usage.html#using-copy-to-and-copy-from)
  * [Access to PostgreSQL large objects](https://www.psycopg.org/docs/usage.html#access-to-postgresql-large-objects)
  * [Two-Phase Commit protocol support](https://www.psycopg.org/docs/usage.html#two-phase-commit-protocol-support)

* [The `psycopg2` module content](https://www.psycopg.org/docs/module.html)
  * [Exceptions](https://www.psycopg.org/docs/module.html#exceptions)
  * [Type Objects and Constructors](https://www.psycopg.org/docs/module.html#type-objects-and-constructors)

* [The `connection` class](https://www.psycopg.org/docs/connection.html)
* [The `cursor` class](https://www.psycopg.org/docs/cursor.html)
* [More advanced topics](https://www.psycopg.org/docs/advanced.html)
  * [Connection and cursor factories](https://www.psycopg.org/docs/advanced.html#connection-and-cursor-factories)
  * [Adapting new Python types to SQL syntax](https://www.psycopg.org/docs/advanced.html#adapting-new-python-types-to-sql-syntax)
  * [Type casting of SQL types into Python objects](https://www.psycopg.org/docs/advanced.html#type-casting-of-sql-types-into-python-objects)
  * [Asynchronous notifications](https://www.psycopg.org/docs/advanced.html#asynchronous-notifications)
  * [Asynchronous support](https://www.psycopg.org/docs/advanced.html#asynchronous-support)
  * [Support for coroutine libraries](https://www.psycopg.org/docs/advanced.html#support-for-coroutine-libraries)
  * [Replication protocol support](https://www.psycopg.org/docs/advanced.html#replication-protocol-support)

* [`psycopg2.extensions` – Extensions to the DB API](https://www.psycopg.org/docs/extensions.html)
  * [Classes definitions](https://www.psycopg.org/docs/extensions.html#classes-definitions)
  * [SQL adaptation protocol objects](https://www.psycopg.org/docs/extensions.html#sql-adaptation-protocol-objects)
  * [Database types casting functions](https://www.psycopg.org/docs/extensions.html#database-types-casting-functions)
  * [Additional exceptions](https://www.psycopg.org/docs/extensions.html#additional-exceptions)
  * [Coroutines support functions](https://www.psycopg.org/docs/extensions.html#coroutines-support-functions)
  * [Other functions](https://www.psycopg.org/docs/extensions.html#other-functions)
  * [Isolation level constants](https://www.psycopg.org/docs/extensions.html#isolation-level-constants)
  * [Transaction status constants](https://www.psycopg.org/docs/extensions.html#transaction-status-constants)
  * [Connection status constants](https://www.psycopg.org/docs/extensions.html#connection-status-constants)
  * [Poll constants](https://www.psycopg.org/docs/extensions.html#poll-constants)
  * [Additional database types](https://www.psycopg.org/docs/extensions.html#additional-database-types)

* [`psycopg2.extras` – Miscellaneous goodies for Psycopg 2](https://www.psycopg.org/docs/extras.html)
  * [Connection and cursor subclasses](https://www.psycopg.org/docs/extras.html#connection-and-cursor-subclasses)
  * [Replication support objects](https://www.psycopg.org/docs/extras.html#replication-support-objects)
  * [Additional data types](https://www.psycopg.org/docs/extras.html#additional-data-types)
  * [Fast execution helpers](https://www.psycopg.org/docs/extras.html#fast-execution-helpers)
  * [Coroutine support](https://www.psycopg.org/docs/extras.html#coroutine-support)

* [`psycopg2.errors` – Exception classes mapping PostgreSQL errors](https://www.psycopg.org/docs/errors.html)
  * [SQLSTATE exception classes](https://www.psycopg.org/docs/errors.html#sqlstate-exception-classes)

* [`psycopg2.sql` – SQL string composition](https://www.psycopg.org/docs/sql.html)
  * [Module usage](https://www.psycopg.org/docs/sql.html#module-usage)
  * [`sql` objects](https://www.psycopg.org/docs/sql.html#sql-objects)

* [`psycopg2.tz` – `tzinfo` implementations for Psycopg 2](https://www.psycopg.org/docs/tz.html)
* [`psycopg2.pool` – Connections pooling](https://www.psycopg.org/docs/pool.html)
* [`psycopg2.errorcodes` – Error codes defined by PostgreSQL](https://www.psycopg.org/docs/errorcodes.html)
* [Frequently Asked Questions](https://www.psycopg.org/docs/faq.html)
  * [Meta](https://www.psycopg.org/docs/faq.html#meta)
  * [Problems with transactions handling](https://www.psycopg.org/docs/faq.html#problems-with-transactions-handling)
  * [Problems with type conversions](https://www.psycopg.org/docs/faq.html#problems-with-type-conversions)
  * [Best practices](https://www.psycopg.org/docs/faq.html#best-practices)
  * [Problems compiling and installing psycopg2](https://www.psycopg.org/docs/faq.html#problems-compiling-and-installing-psycopg2)

* [Release notes](https://www.psycopg.org/docs/news.html)
  * [Current release](https://www.psycopg.org/docs/news.html#current-release)
  * [What’s new in psycopg 2.9](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9)
  * [What’s new in psycopg 2.8](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-8)
  * [What’s new in psycopg 2.7](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-7)
  * [What’s new in psycopg 2.6](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-6)
  * [What’s new in psycopg 2.5](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-5)
  * [What’s new in psycopg 2.4](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-4)
  * [What’s new in psycopg 2.3](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-3)
  * [What’s new in psycopg 2.2](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-2)
  * [What’s new in psycopg 2.0](https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-0)

* [License](https://www.psycopg.org/docs/license.html)
  * [psycopg2 and the LGPL](https://www.psycopg.org/docs/license.html#psycopg2-and-the-lgpl)
  * [Alternative licenses](https://www.psycopg.org/docs/license.html#alternative-licenses)

Indices and tables

* [Index](https://www.psycopg.org/docs/genindex.html)

* [Module Index](https://www.psycopg.org/docs/py-modindex.html)

* [Search Page](https://www.psycopg.org/docs/search.html)
