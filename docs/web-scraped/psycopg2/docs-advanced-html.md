# Source: https://www.psycopg.org/docs/advanced.html

Title: More advanced topics — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/advanced.html

Published Time: Sun, 08 Mar 2026 18:42:13 GMT

Markdown Content:
More advanced topics — Psycopg 2.9.11 documentation
===============

[Psycopg 2.9.11 documentation](https://www.psycopg.org/docs/index.html)
=======================================================================

* ← [The `cursor` class](https://www.psycopg.org/docs/cursor.html "Previous document")
* [`psycopg2.extensions` – Extensions to the DB API](https://www.psycopg.org/docs/extensions.html "Next document") →

* [Home](https://www.psycopg.org/docs/index.html)

More advanced topics[¶](https://www.psycopg.org/docs/advanced.html#more-advanced-topics "Link to this heading")
===============================================================================================================

Connection and cursor factories[¶](https://www.psycopg.org/docs/advanced.html#connection-and-cursor-factories "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

Psycopg exposes two new-style classes that can be sub-classed and expanded to adapt them to the needs of the programmer: [`psycopg2.extensions.cursor`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.cursor "psycopg2.extensions.cursor") and [`psycopg2.extensions.connection`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.connection "psycopg2.extensions.connection"). The [`connection`](https://www.psycopg.org/docs/connection.html#connection "connection") class is usually sub-classed only to provide an easy way to create customized cursors but other uses are possible. [`cursor`](https://www.psycopg.org/docs/cursor.html#cursor "cursor") is much more interesting, because it is the class where query building, execution and result type-casting into Python variables happens.

The [`extras`](https://www.psycopg.org/docs/extras.html#module-psycopg2.extras "psycopg2.extras") module contains several examples of [connection and cursor subclasses](https://www.psycopg.org/docs/extras.html#cursor-subclasses).

Note

If you only need a customized cursor class, since Psycopg 2.5 you can use the [`cursor_factory`](https://www.psycopg.org/docs/connection.html#connection.cursor_factory "connection.cursor_factory") parameter of a regular connection instead of creating a new `connection` subclass.

An example of cursor subclass performing logging is:

import psycopg2
import psycopg2.extensions
import logging

class LoggingCursor(psycopg2.extensions.cursor):
    def execute(self, sql, args=None):
        logger = logging.getLogger('sql_debug')
        logger.info(self.mogrify(sql, args))

        try:
            psycopg2.extensions.cursor.execute(self, sql, args)
        except Exception, exc:
            logger.error("%s: %s" % (exc. __class__ . __name__ , exc))
            raise

conn = psycopg2.connect(DSN)
cur = conn.cursor(cursor_factory=LoggingCursor)
cur.execute("INSERT INTO mytable VALUES (%s, %s, %s);",
             (10, 20, 30))

Adapting new Python types to SQL syntax[¶](https://www.psycopg.org/docs/advanced.html#adapting-new-python-types-to-sql-syntax "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Any Python class or type can be adapted to an SQL string. Adaptation mechanism is similar to the Object Adaptation proposed in the [**PEP 246**](https://peps.python.org/pep-0246/) and is exposed by the [`psycopg2.extensions.adapt()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.adapt "psycopg2.extensions.adapt") function.

The [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") method adapts its arguments to the [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote") protocol. Objects that conform to this protocol expose a `getquoted()` method returning the SQL representation of the object as a string (the method must return `bytes` in Python 3). Optionally the conform object may expose a [`prepare()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote.prepare "psycopg2.extensions.ISQLQuote.prepare") method.

There are two basic ways to have a Python object adapted to SQL:

* the object itself is conform, or knows how to make itself conform. Such object must expose a `__conform__()` method that will be called with the protocol object as argument. The object can check that the protocol is `ISQLQuote`, in which case it can return `self` (if the object also implements `getquoted()`) or a suitable wrapper object. This option is viable if you are the author of the object and if the object is specifically designed for the database (i.e. having Psycopg as a dependency and polluting its interface with the required methods doesn’t bother you). For a simple example you can take a look at the source code for the [`psycopg2.extras.Inet`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Inet "psycopg2.extras.Inet") object.

* If implementing the `ISQLQuote` interface directly in the object is not an option (maybe because the object to adapt comes from a third party library), you can use an _adaptation function_, taking the object to be adapted as argument and returning a conforming object. The adapter must be registered via the [`register_adapter()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_adapter "psycopg2.extensions.register_adapter") function. A simple example wrapper is `psycopg2.extras.UUID_adapter` used by the [`register_uuid()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_uuid "psycopg2.extras.register_uuid") function.

A convenient object to write adapters is the [`AsIs`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.AsIs "psycopg2.extensions.AsIs") wrapper, whose `getquoted()` result is simply the `str()`ing conversion of the wrapped object.

Example: mapping of a `Point` class into the [`point`](https://www.postgresql.org/docs/current/static/datatype-geometric.html#DATATYPE-GEOMETRIC) PostgreSQL geometric type:

>>> from psycopg2.extensions import adapt, register_adapter, AsIs

>>> class Point(object):
...    def  **init** (self, x, y):
...        self.x = x
...        self.y = y

>>> def adapt_point(point):
...     x = adapt(point.x).getquoted()
...     y = adapt(point.y).getquoted()
...     return AsIs("'(%s, %s)'" % (x, y))

>>> register_adapter(Point, adapt_point)

>>> cur.execute("INSERT INTO atable (apoint) VALUES (%s)",
...             (Point(1.23, 4.56),))

The above function call results in the SQL command:

INSERT INTO atable (apoint) VALUES ('(1.23, 4.56)');

Type casting of SQL types into Python objects[¶](https://www.psycopg.org/docs/advanced.html#type-casting-of-sql-types-into-python-objects "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

PostgreSQL objects read from the database can be adapted to Python objects through an user-defined adapting function. An adapter function takes two arguments: the object string representation as returned by PostgreSQL and the cursor currently being read, and should return a new Python object. For example, the following function parses the PostgreSQL `point` representation into the previously defined `Point` class:

>>> def cast_point(value, cur):
...    if value is None:
...        return None
...
...    # Convert from (f1, f2) syntax using a regular expression.
...    m = re.match(r"\(([^)]+),([^)]+)\)", value)
...    if m:
...        return Point(float(m.group(1)), float(m.group(2)))
...    else:
...        raise InterfaceError("bad point representation: %r" % value)

In order to create a mapping from a PostgreSQL type (either standard or user-defined), its OID must be known. It can be retrieved either by the second column of the [`cursor.description`](https://www.psycopg.org/docs/cursor.html#cursor.description "cursor.description"):

>>> cur.execute("SELECT NULL::point")
>>> point_oid = cur.description[0][1]
>>> point_oid
600

or by querying the system catalog for the type name and namespace (the namespace for system objects is `pg_catalog`):

>>> cur.execute("""
...  SELECT pg_type.oid
...  FROM pg_type JOIN pg_namespace
...  ON typnamespace = pg_namespace.oid
...  WHERE typname = %(typename)s
...  AND nspname = %(namespace)s""",
...    {'typename': 'point', 'namespace': 'pg_catalog'})
>>> point_oid = cur.fetchone()[0]
>>> point_oid
600

After you know the object OID, you can create and register the new type:

>>> POINT = psycopg2.extensions.new_type((point_oid,), "POINT", cast_point)
>>> psycopg2.extensions.register_type(POINT)

The [`new_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.new_type "psycopg2.extensions.new_type") function binds the object OIDs (more than one can be specified) to the adapter function. [`register_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_type "psycopg2.extensions.register_type") completes the spell. Conversion is automatically performed when a column whose type is a registered OID is read:

>>> cur.execute("SELECT '(10.2,20.3)'::point")
>>> point = cur.fetchone()[0]
>>> print(type(point), point.x, point.y)
<class 'Point'> 10.2 20.3

A typecaster created by `new_type()` can be also used with [`new_array_type()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.new_array_type "psycopg2.extensions.new_array_type") to create a typecaster converting a PostgreSQL array into a Python list.

Asynchronous notifications[¶](https://www.psycopg.org/docs/advanced.html#asynchronous-notifications "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

Psycopg allows asynchronous interaction with other database sessions using the facilities offered by PostgreSQL commands [`LISTEN`](https://www.postgresql.org/docs/current/static/sql-listen.html) and [`NOTIFY`](https://www.postgresql.org/docs/current/static/sql-notify.html). Please refer to the PostgreSQL documentation for examples about how to use this form of communication.

Notifications are instances of the [`Notify`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify "psycopg2.extensions.Notify") object made available upon reception in the [`connection.notifies`](https://www.psycopg.org/docs/connection.html#connection.notifies "connection.notifies") list. Notifications can be sent from Python code simply executing a `NOTIFY` command in an [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") call.

Because of the way sessions interact with notifications (see [`NOTIFY`](https://www.postgresql.org/docs/current/static/sql-notify.html) documentation), you should keep the connection in [`autocommit`](https://www.psycopg.org/docs/connection.html#connection.autocommit "connection.autocommit") mode if you wish to receive or send notifications in a timely manner.

Notifications are received after every query execution. If the user is interested in receiving notifications but not in performing any query, the [`poll()`](https://www.psycopg.org/docs/connection.html#connection.poll "connection.poll") method can be used to check for new messages without wasting resources.

A simple application could poll the connection from time to time to check if something new has arrived. A better strategy is to use some I/O completion function such as [`select()`](https://docs.python.org/3/library/select.html#select.select "(in Python v3.14)") to sleep until awakened by the kernel when there is some data to read on the connection, thereby using no CPU unless there is something to read:

import select
import psycopg2
import psycopg2.extensions

conn = psycopg2.connect(DSN)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("LISTEN test;")

print("Waiting for notifications on channel 'test'")
while True:
    if select.select([conn],[],[],5) == ([],[],[]):
        print("Timeout")
    else:
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            print("Got NOTIFY:", notify.pid, notify.channel, notify.payload)

Running the script and executing a command such as `NOTIFY test, 'hello'` in a separate **psql** shell, the output may look similar to:

Waiting for notifications on channel 'test'
Timeout
Timeout
Got NOTIFY: 6535 test hello
Timeout
...

Note that the payload is only available from PostgreSQL 9.0: notifications received from a previous version server will have the [`payload`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify.payload "psycopg2.extensions.Notify.payload") attribute set to the empty string.

Changed in version 2.3: Added [`Notify`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.Notify "psycopg2.extensions.Notify") object and handling notification payload.

Changed in version 2.7: The [`notifies`](https://www.psycopg.org/docs/connection.html#connection.notifies "connection.notifies") attribute is writable: it is possible to replace it with any object exposing an `append()` method. An useful example would be to use a [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "(in Python v3.14)") object.

Asynchronous support[¶](https://www.psycopg.org/docs/advanced.html#asynchronous-support "Link to this heading")
---------------------------------------------------------------------------------------------------------------

Added in version 2.2.

Psycopg can issue asynchronous queries to a PostgreSQL database. An asynchronous communication style is established passing the parameter _async_=1 to the [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect") function: the returned connection will work in _asynchronous mode_.

In asynchronous mode, a Psycopg connection will rely on the caller to poll the socket file descriptor, checking if it is ready to accept data or if a query result has been transferred and is ready to be read on the client. The caller can use the method [`fileno()`](https://www.psycopg.org/docs/connection.html#connection.fileno "connection.fileno") to get the connection file descriptor and [`poll()`](https://www.psycopg.org/docs/connection.html#connection.poll "connection.poll") to make communication proceed according to the current connection state.

The following is an example loop using methods `fileno()` and `poll()` together with the Python [`select()`](https://docs.python.org/3/library/select.html#select.select "(in Python v3.14)") function in order to carry on asynchronous operations with Psycopg:

def wait(conn):
    while True:
        state = conn.poll()
        if state == psycopg2.extensions.POLL_OK:
            break
        elif state == psycopg2.extensions.POLL_WRITE:
            select.select([], [conn.fileno()], [])
        elif state == psycopg2.extensions.POLL_READ:
            select.select([conn.fileno()], [], [])
        else:
            raise psycopg2.OperationalError("poll() returned %s" % state)

The above loop of course would block an entire application: in a real asynchronous framework, `select()` would be called on many file descriptors waiting for any of them to be ready. Nonetheless the function can be used to connect to a PostgreSQL server only using nonblocking commands and the connection obtained can be used to perform further nonblocking queries. After `poll()` has returned [`POLL_OK`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.POLL_OK "psycopg2.extensions.POLL_OK"), and thus `wait()` has returned, the connection can be safely used:

>>> aconn = psycopg2.connect(database='test', async=1)
>>> wait(aconn)
>>> acurs = aconn.cursor()

Note that there are a few other requirements to be met in order to have a completely non-blocking connection attempt: see the libpq documentation for [`PQconnectStart()`](https://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-PQCONNECTSTARTPARAMS).

The same loop should be also used to perform nonblocking queries: after sending a query via [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") or [`callproc()`](https://www.psycopg.org/docs/cursor.html#cursor.callproc "cursor.callproc"), call `poll()` on the connection available from [`cursor.connection`](https://www.psycopg.org/docs/cursor.html#cursor.connection "cursor.connection") until it returns `POLL_OK`, at which point the query has been completely sent to the server and, if it produced data, the results have been transferred to the client and available using the regular cursor methods:

>>> acurs.execute("SELECT pg_sleep(5); SELECT 42;")
>>> wait(acurs.connection)
>>> acurs.fetchone()[0]
42

When an asynchronous query is being executed, [`connection.isexecuting()`](https://www.psycopg.org/docs/connection.html#connection.isexecuting "connection.isexecuting") returns `True`. Two cursors can’t execute concurrent queries on the same asynchronous connection.

There are several limitations in using asynchronous connections: the connection is always in [`autocommit`](https://www.psycopg.org/docs/connection.html#connection.autocommit "connection.autocommit") mode and it is not possible to change it. So a transaction is not implicitly started at the first query and is not possible to use methods [`commit()`](https://www.psycopg.org/docs/connection.html#connection.commit "connection.commit") and [`rollback()`](https://www.psycopg.org/docs/connection.html#connection.rollback "connection.rollback"): you can manually control transactions using [`execute()`](https://www.psycopg.org/docs/cursor.html#cursor.execute "cursor.execute") to send database commands such as `BEGIN`, `COMMIT` and `ROLLBACK`. Similarly [`set_session()`](https://www.psycopg.org/docs/connection.html#connection.set_session "connection.set_session") can’t be used but it is still possible to invoke the `SET` command with the proper `default_transaction_...` parameter.

With asynchronous connections it is also not possible to use [`set_client_encoding()`](https://www.psycopg.org/docs/connection.html#connection.set_client_encoding "connection.set_client_encoding"), [`executemany()`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany"), [large objects](https://www.psycopg.org/docs/usage.html#large-objects), [named cursors](https://www.psycopg.org/docs/usage.html#server-side-cursors).

[COPY commands](https://www.psycopg.org/docs/usage.html#copy) are not supported either in asynchronous mode, but this will be probably implemented in a future release.

Support for coroutine libraries[¶](https://www.psycopg.org/docs/advanced.html#support-for-coroutine-libraries "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

Added in version 2.2.

Psycopg can be used together with [coroutine](https://en.wikipedia.org/wiki/Coroutine)-based libraries and participate in cooperative multithreading.

Coroutine-based libraries (such as [Eventlet](https://eventlet.net/) or [gevent](http://www.gevent.org/)) can usually patch the Python standard library in order to enable a coroutine switch in the presence of blocking I/O: the process is usually referred as making the system _green_, in reference to the [green threads](https://en.wikipedia.org/wiki/Green_threads).

Because Psycopg is a C extension module, it is not possible for coroutine libraries to patch it: Psycopg instead enables cooperative multithreading by allowing the registration of a _wait callback_ using the [`psycopg2.extensions.set_wait_callback()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.set_wait_callback "psycopg2.extensions.set_wait_callback") function. When a wait callback is registered, Psycopg will use [libpq non-blocking calls](https://www.postgresql.org/docs/current/static/libpq-async.html) instead of the regular blocking ones, and will delegate to the callback the responsibility to wait for the socket to become readable or writable.

Working this way, the caller does not have the complete freedom to schedule the socket check whenever they want as with an [asynchronous connection](https://www.psycopg.org/docs/advanced.html#async-support), but has the advantage of maintaining a complete DB API 2.0 semantics: from the point of view of the end user, all Psycopg functions and objects will work transparently in the coroutine environment (blocking the calling green thread and giving other green threads the possibility to be scheduled), allowing non modified code and third party libraries (such as [SQLAlchemy](https://www.sqlalchemy.org/)) to be used in coroutine-based programs.

Warning

Psycopg connections are not _green thread safe_ and can’t be used concurrently by different green threads. Trying to execute more than one command at time using one cursor per thread will result in an error (or a deadlock on versions before 2.4.2).

Therefore, programmers are advised to either avoid sharing connections between coroutines or to use a library-friendly lock to synchronize shared connections, e.g. for pooling.

Coroutine libraries authors should provide a callback implementation (and possibly a method to register it) to make Psycopg as green as they want. An example callback (using `select()` to block) is provided as [`psycopg2.extras.wait_select()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.wait_select "psycopg2.extras.wait_select"): it boils down to something similar to:

def wait_select(conn):
    while True:
        state = conn.poll()
        if state == extensions.POLL_OK:
            break
        elif state == extensions.POLL_READ:
            select.select([conn.fileno()], [], [])
        elif state == extensions.POLL_WRITE:
            select.select([], [conn.fileno()], [])
        else:
            raise OperationalError("bad state from poll: %s" % state)

Providing callback functions for the single coroutine libraries is out of psycopg2 scope, as the callback can be tied to the libraries’ implementation details. You can check the [psycogreen](https://github.com/psycopg/psycogreen/) project for further informations and resources about the topic.

Warning

[COPY commands](https://www.psycopg.org/docs/usage.html#copy) are currently not supported when a wait callback is registered, but they will be probably implemented in a future release.

[Large objects](https://www.psycopg.org/docs/usage.html#large-objects) are not supported either: they are not compatible with asynchronous connections.

Replication protocol support[¶](https://www.psycopg.org/docs/advanced.html#replication-protocol-support "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

Added in version 2.7.

Modern PostgreSQL servers (version 9.0 and above) support replication. The replication protocol is built on top of the client-server protocol and can be operated using `libpq`, as such it can be also operated by `psycopg2`. The replication protocol can be operated on both synchronous and [asynchronous](https://www.psycopg.org/docs/advanced.html#async-support) connections.

Server version 9.4 adds a new feature called _Logical Replication_.

See also

* PostgreSQL [Streaming Replication Protocol](https://www.postgresql.org/docs/current/static/protocol-replication.html)

### Logical replication Quick-Start[¶](https://www.psycopg.org/docs/advanced.html#logical-replication-quick-start "Link to this heading")

You must be using PostgreSQL server version 9.4 or above to run this quick start.

Make sure that replication connections are permitted for user `postgres` in `pg_hba.conf` and reload the server configuration. You also need to set `wal_level=logical` and `max_wal_senders`, `max_replication_slots` to value greater than zero in `postgresql.conf` (these changes require a server restart). Create a database `psycopg2_test`.

Then run the following code to quickly try the replication support out. This is not production code – it’s only intended as a simple demo of logical replication:

from  **future**  import print_function
import sys
import psycopg2
import psycopg2.extras

conn = psycopg2.connect('dbname=psycopg2_test user=postgres',
   connection_factory=psycopg2.extras.LogicalReplicationConnection)
cur = conn.cursor()
try:
    # test_decoding produces textual output
    cur.start_replication(slot_name='pytest', decode=True)
except psycopg2.ProgrammingError:
    cur.create_replication_slot('pytest', output_plugin='test_decoding')
    cur.start_replication(slot_name='pytest', decode=True)

class DemoConsumer(object):
    def  **call** (self, msg):
        print(msg.payload)
        msg.cursor.send_feedback(flush_lsn=msg.data_start)

democonsumer = DemoConsumer()

print("Starting streaming, press Control-C to end...", file=sys.stderr)
try:
   cur.consume_stream(democonsumer)
except KeyboardInterrupt:
   cur.close()
   conn.close()
   print("The slot 'pytest' still exists. Drop it with "
      "SELECT pg_drop_replication_slot('pytest'); if no longer needed.",
      file=sys.stderr)
   print("WARNING: Transaction logs will accumulate in pg_xlog "
      "until the slot is dropped.", file=sys.stderr)

You can now make changes to the `psycopg2_test` database using a normal psycopg2 session, `psql`, etc. and see the logical decoding stream printed by this demo client.

This will continue running until terminated with `Control-C`.

For the details see [Replication support objects](https://www.psycopg.org/docs/extras.html#replication-objects).

### [Table of Contents](https://www.psycopg.org/docs/index.html)

* [More advanced topics](https://www.psycopg.org/docs/advanced.html#)
  * [Connection and cursor factories](https://www.psycopg.org/docs/advanced.html#connection-and-cursor-factories)
  * [Adapting new Python types to SQL syntax](https://www.psycopg.org/docs/advanced.html#adapting-new-python-types-to-sql-syntax)
  * [Type casting of SQL types into Python objects](https://www.psycopg.org/docs/advanced.html#type-casting-of-sql-types-into-python-objects)
  * [Asynchronous notifications](https://www.psycopg.org/docs/advanced.html#asynchronous-notifications)
  * [Asynchronous support](https://www.psycopg.org/docs/advanced.html#asynchronous-support)
  * [Support for coroutine libraries](https://www.psycopg.org/docs/advanced.html#support-for-coroutine-libraries)
  * [Replication protocol support](https://www.psycopg.org/docs/advanced.html#replication-protocol-support)
    * [Logical replication Quick-Start](https://www.psycopg.org/docs/advanced.html#logical-replication-quick-start)

### Quick search

* ← [The `cursor` class](https://www.psycopg.org/docs/cursor.html "Previous document")
* [`psycopg2.extensions` – Extensions to the DB API](https://www.psycopg.org/docs/extensions.html "Next document") →

* [Home](https://www.psycopg.org/docs/index.html)

© 2001-2021, Federico Di Gregorio, Daniele Varrazzo, The Psycopg Team.
