# Source: https://www.psycopg.org/docs/pool.html

Title: psycopg2.pool – Connections pooling — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/pool.html

Markdown Content:
Creating new PostgreSQL connections can be an expensive operation. This module offers a few pure Python classes implementing simple connection pooling directly in the client application.

_class_ psycopg2.pool.AbstractConnectionPool(_minconn_, _maxconn_, _\*args_, _\*\*kwargs_)[¶](https://www.psycopg.org/docs/pool.html#psycopg2.pool.AbstractConnectionPool "Link to this definition")
Base class implementing generic key-based pooling code.

New _minconn_ connections are created automatically. The pool will support a maximum of about _maxconn_ connections. _*args_ and _**kwargs_ are passed to the [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect") function.

The following methods are expected to be implemented by subclasses:

getconn(_key=None_)[¶](https://www.psycopg.org/docs/pool.html#psycopg2.pool.AbstractConnectionPool.getconn "Link to this definition")
Get a free connection from the pool.

The _key_ parameter is optional: if used, the connection will be associated to the key and calling `getconn()` with the same key again will return the same connection.

putconn(_conn_, _key=None_, _close=False_)[¶](https://www.psycopg.org/docs/pool.html#psycopg2.pool.AbstractConnectionPool.putconn "Link to this definition")
Put away a connection.

If _close_ is `True`, discard the connection from the pool. _key_ should be used consistently with [`getconn()`](https://www.psycopg.org/docs/pool.html#psycopg2.pool.AbstractConnectionPool.getconn "psycopg2.pool.AbstractConnectionPool.getconn").

closeall()[¶](https://www.psycopg.org/docs/pool.html#psycopg2.pool.AbstractConnectionPool.closeall "Link to this definition")
Close all the connections handled by the pool.

Note that all the connections are closed, including ones eventually in use by the application.

The following classes are [`AbstractConnectionPool`](https://www.psycopg.org/docs/pool.html#psycopg2.pool.AbstractConnectionPool "psycopg2.pool.AbstractConnectionPool") subclasses ready to be used.

_class_ psycopg2.pool.SimpleConnectionPool(_minconn_, _maxconn_, _*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/pool.html#psycopg2.pool.SimpleConnectionPool "Link to this definition")
A connection pool that can’t be shared across different threads.

Note

This pool class is useful only for single-threaded applications.

_class_ psycopg2.pool.ThreadedConnectionPool(_minconn_, _maxconn_, _*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/pool.html#psycopg2.pool.ThreadedConnectionPool "Link to this definition")
A connection pool that works with the threading module.

Note

This pool class can be safely used in multi-threaded applications.
