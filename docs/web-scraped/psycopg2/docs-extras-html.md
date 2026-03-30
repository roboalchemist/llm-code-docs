# Source: https://www.psycopg.org/docs/extras.html

Title: psycopg2.extras – Miscellaneous goodies for Psycopg 2 — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/extras.html

Markdown Content:
[`psycopg2.extras`](https://www.psycopg.org/docs/extras.html#module-psycopg2.extras "psycopg2.extras") – Miscellaneous goodies for Psycopg 2[¶](https://www.psycopg.org/docs/extras.html#module-psycopg2.extras "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This module is a generic place used to hold little helper functions and classes until a better place in the distribution is found.

Connection and cursor subclasses[¶](https://www.psycopg.org/docs/extras.html#connection-and-cursor-subclasses "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

A few objects that change the way the results are returned by the cursor or modify the object behavior in some other way. Typically `cursor` subclasses are passed as _cursor\_factory_ argument to [`connect()`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect") so that the connection’s [`cursor()`](https://www.psycopg.org/docs/connection.html#connection.cursor "connection.cursor") method will generate objects of this class. Alternatively a `cursor` subclass can be used one-off by passing it as the _cursor\_factory_ argument to the `cursor()` method.

If you want to use a `connection` subclass you can pass it as the _connection\_factory_ argument of the `connect()` function.

### Dictionary-like cursor[¶](https://www.psycopg.org/docs/extras.html#dictionary-like-cursor "Link to this heading")

The dict cursors allow to access to the attributes of retrieved records using an interface similar to the Python dictionaries instead of the tuples.

>>> dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
>>> dict_cur.execute("INSERT INTO test (num, data) VALUES(%s, %s)",
...                  (100, "abc'def"))
>>> dict_cur.execute("SELECT * FROM test")
>>> rec = dict_cur.fetchone()
>>> rec['id']
1
>>> rec['num']
100
>>> rec['data']
"abc'def"

The records still support indexing as the original tuple:

>>> rec[2]
"abc'def"

_class_ psycopg2.extras.DictCursor(_*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictCursor "Link to this definition")
A cursor that keeps a list of column name -> index [mappings](https://docs.python.org/glossary.html#term-mapping).

_class_ psycopg2.extras.DictConnection[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictConnection "Link to this definition")
A connection that uses [`DictCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictCursor "psycopg2.extras.DictCursor") automatically.

Note

Not very useful since Psycopg 2.5: you can use [`psycopg2.connect`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect")`(dsn, cursor_factory=DictCursor)` instead of `DictConnection`.

_class_ psycopg2.extras.DictRow(_cursor_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictRow "Link to this definition")
A row object that allow by-column-name access to data.

### Real dictionary cursor[¶](https://www.psycopg.org/docs/extras.html#real-dictionary-cursor "Link to this heading")

_class_ psycopg2.extras.RealDictCursor(_*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictCursor "Link to this definition")
A cursor that uses a real dict as the base type for rows.

Note that this cursor is extremely specialized and does not allow the normal access (using integer indices) to fetched data. If you need to access database rows both as a dictionary and a list, then use the generic [`DictCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictCursor "psycopg2.extras.DictCursor") instead of `RealDictCursor`.

_class_ psycopg2.extras.RealDictConnection[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictConnection "Link to this definition")
A connection that uses [`RealDictCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictCursor "psycopg2.extras.RealDictCursor") automatically.

Note

Not very useful since Psycopg 2.5: you can use [`psycopg2.connect`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect")`(dsn, cursor_factory=RealDictCursor)` instead of `RealDictConnection`.

_class_ psycopg2.extras.RealDictRow(_*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictRow "Link to this definition")
A `dict` subclass representing a data record.

### `namedtuple` cursor[¶](https://www.psycopg.org/docs/extras.html#namedtuple-cursor "Link to this heading")

Added in version 2.3.

_class_ psycopg2.extras.NamedTupleCursor[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.NamedTupleCursor "Link to this definition")
A cursor that generates results as [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.14)").

`fetch*()` methods will return named tuples instead of regular tuples, so their elements can be accessed both as regular numeric items as well as attributes.

>>> nt_cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
>>> rec = nt_cur.fetchone()
>>> rec
Record(id=1, num=100, data="abc'def")
>>> rec[1]
100
>>> rec.data
"abc'def"

_class_ psycopg2.extras.NamedTupleConnection[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.NamedTupleConnection "Link to this definition")
A connection that uses [`NamedTupleCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.NamedTupleCursor "psycopg2.extras.NamedTupleCursor") automatically.

Note

Not very useful since Psycopg 2.5: you can use [`psycopg2.connect`](https://www.psycopg.org/docs/module.html#psycopg2.connect "psycopg2.connect")`(dsn, cursor_factory=NamedTupleCursor)` instead of `NamedTupleConnection`.

### Logging cursor[¶](https://www.psycopg.org/docs/extras.html#logging-cursor "Link to this heading")

_class_ psycopg2.extras.LoggingConnection[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LoggingConnection "Link to this definition")
A connection that logs all queries to a file or [logger](https://docs.python.org/library/logging.html) object.

filter(_msg_, _curs_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LoggingConnection.filter "Link to this definition")
Filter the query before logging it.

This is the method to overwrite to filter unwanted queries out of the log or to add some extra data to the output. The default implementation just does nothing.

initialize(_logobj_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LoggingConnection.initialize "Link to this definition")
Initialize the connection to log to `logobj`.

The `logobj` parameter can be an open file object or a Logger/LoggerAdapter instance from the standard logging module.

_class_ psycopg2.extras.LoggingCursor[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LoggingCursor "Link to this definition")
A cursor that logs queries using its connection logging facilities.

_class_ psycopg2.extras.MinTimeLoggingConnection[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingConnection "Link to this definition")
A connection that logs queries based on execution time.

This is just an example of how to sub-class [`LoggingConnection`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LoggingConnection "psycopg2.extras.LoggingConnection") to provide some extra filtering for the logged queries. Both the [`initialize()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingConnection.initialize "psycopg2.extras.MinTimeLoggingConnection.initialize") and [`filter()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingConnection.filter "psycopg2.extras.MinTimeLoggingConnection.filter") methods are overwritten to make sure that only queries executing for more than `mintime` ms are logged.

Note that this connection uses the specialized cursor [`MinTimeLoggingCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingCursor "psycopg2.extras.MinTimeLoggingCursor").

filter(_msg_, _curs_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingConnection.filter "Link to this definition")
Filter the query before logging it.

This is the method to overwrite to filter unwanted queries out of the log or to add some extra data to the output. The default implementation just does nothing.

initialize(_logobj_, _mintime=0_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingConnection.initialize "Link to this definition")
Initialize the connection to log to `logobj`.

The `logobj` parameter can be an open file object or a Logger/LoggerAdapter instance from the standard logging module.

_class_ psycopg2.extras.MinTimeLoggingCursor[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingCursor "Link to this definition")
The cursor sub-class companion to [`MinTimeLoggingConnection`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.MinTimeLoggingConnection "psycopg2.extras.MinTimeLoggingConnection").

Replication support objects[¶](https://www.psycopg.org/docs/extras.html#replication-support-objects "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

See [Replication protocol support](https://www.psycopg.org/docs/advanced.html#replication-support) for an introduction to the topic.

The following replication types are defined:

psycopg2.extras.REPLICATION_LOGICAL[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.REPLICATION_LOGICAL "Link to this definition")psycopg2.extras.REPLICATION_PHYSICAL[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.REPLICATION_PHYSICAL "Link to this definition")_class_ psycopg2.extras.LogicalReplicationConnection(_*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LogicalReplicationConnection "Link to this definition")
This connection factory class can be used to open a special type of connection that is used for logical replication.

Example:

from psycopg2.extras import LogicalReplicationConnection
log_conn = psycopg2.connect(dsn, connection_factory=LogicalReplicationConnection)
log_cur = log_conn.cursor()

_class_ psycopg2.extras.PhysicalReplicationConnection(_*args_, _**kwargs_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.PhysicalReplicationConnection "Link to this definition")
This connection factory class can be used to open a special type of connection that is used for physical replication.

Example:

from psycopg2.extras import PhysicalReplicationConnection
phys_conn = psycopg2.connect(dsn, connection_factory=PhysicalReplicationConnection)
phys_cur = phys_conn.cursor()

Both [`LogicalReplicationConnection`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.LogicalReplicationConnection "psycopg2.extras.LogicalReplicationConnection") and [`PhysicalReplicationConnection`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.PhysicalReplicationConnection "psycopg2.extras.PhysicalReplicationConnection") use [`ReplicationCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor "psycopg2.extras.ReplicationCursor") for actual communication with the server.

The individual messages in the replication stream are represented by [`ReplicationMessage`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage "psycopg2.extras.ReplicationMessage") objects (both logical and physical type):

_class_ psycopg2.extras.ReplicationMessage[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage "Link to this definition")
A replication protocol message.

payload[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage.payload "Link to this definition")
The actual data received from the server.

An instance of either `bytes()` or `unicode()`, depending on the value of `decode` option passed to [`start_replication()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "psycopg2.extras.ReplicationCursor.start_replication") on the connection. See [`read_message()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.read_message "psycopg2.extras.ReplicationCursor.read_message") for details.

data_size[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage.data_size "Link to this definition")
The raw size of the message payload (before possible unicode conversion).

data_start[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage.data_start "Link to this definition")
LSN position of the start of the message.

wal_end[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage.wal_end "Link to this definition")
LSN position of the current end of WAL on the server.

send_time[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage.send_time "Link to this definition")
A [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)") object representing the server timestamp at the moment when the message was sent.

cursor[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage.cursor "Link to this definition")
A reference to the corresponding [`ReplicationCursor`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor "psycopg2.extras.ReplicationCursor") object.

_class_ psycopg2.extras.ReplicationCursor[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor "Link to this definition")
A cursor used for communication on replication connections.

create_replication_slot(_slot\_name_, _slot\_type=None_, _output\_plugin=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.create_replication_slot "Link to this definition")
Create streaming replication slot.

Parameters:

* **slot_name** – name of the replication slot to be created

* **slot_type** – type of replication: should be either [`REPLICATION_LOGICAL`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.REPLICATION_LOGICAL "psycopg2.extras.REPLICATION_LOGICAL") or [`REPLICATION_PHYSICAL`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.REPLICATION_PHYSICAL "psycopg2.extras.REPLICATION_PHYSICAL")

* **output_plugin** – name of the logical decoding output plugin to be used by the slot; required for logical replication connections, disallowed for physical

Example:

log_cur.create_replication_slot("logical1", "test_decoding")
phys_cur.create_replication_slot("physical1")

# either logical or physical replication connection

cur.create_replication_slot("slot1", slot_type=REPLICATION_LOGICAL)

When creating a slot on a logical replication connection, a logical replication slot is created by default. Logical replication requires name of the logical decoding output plugin to be specified.

When creating a slot on a physical replication connection, a physical replication slot is created by default. No output plugin parameter is required or allowed when creating a physical replication slot.

In either case the type of slot being created can be specified explicitly using _slot\_type_ parameter.

Replication slots are a feature of PostgreSQL server starting with version 9.4.

drop_replication_slot(_slot\_name_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.drop_replication_slot "Link to this definition")
Drop streaming replication slot.

Parameters:
**slot_name** – name of the replication slot to drop

Example:

# either logical or physical replication connection

cur.drop_replication_slot("slot1")

Replication slots are a feature of PostgreSQL server starting with version 9.4.

start_replication(_slot\_name=None_, _slot\_type=None_, _start\_lsn=0_, _timeline=0_, _options=None_, _decode=False_, _status\_interval=10_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "Link to this definition")
Start replication on the connection.

Parameters:

* **slot_name** – name of the replication slot to use; required for logical replication, physical replication can work with or without a slot

* **slot_type** – type of replication: should be either [`REPLICATION_LOGICAL`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.REPLICATION_LOGICAL "psycopg2.extras.REPLICATION_LOGICAL") or [`REPLICATION_PHYSICAL`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.REPLICATION_PHYSICAL "psycopg2.extras.REPLICATION_PHYSICAL")

* **start_lsn** – the optional LSN position to start replicating from, can be an integer or a string of hexadecimal digits in the form `XXX/XXX`

* **timeline** – WAL history timeline to start streaming from (optional, can only be used with physical replication)

* **options** – a dictionary of options to pass to logical replication slot (not allowed with physical replication)

* **decode** – a flag indicating that unicode conversion should be performed on messages received from the server

* **status_interval** – time between feedback packets sent to the server

If a _slot\_name_ is specified, the slot must exist on the server and its type must match the replication type used.

If not specified using _slot\_type_ parameter, the type of replication is defined by the type of replication connection. Logical replication is only allowed on logical replication connection, but physical replication can be used with both types of connection.

On the other hand, physical replication doesn’t require a named replication slot to be used, only logical replication does. In any case logical replication and replication slots are a feature of PostgreSQL server starting with version 9.4. Physical replication can be used starting with 9.0.

If _start\_lsn_ is specified, the requested stream will start from that LSN. The default is `None` which passes the LSN `0/0` causing replay to begin at the last point for which the server got flush confirmation from the client, or the oldest available point for a new slot.

The server might produce an error if a WAL file for the given LSN has already been recycled or it may silently start streaming from a later position: the client can verify the actual position using information provided by the [`ReplicationMessage`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage "psycopg2.extras.ReplicationMessage") attributes. The exact server behavior depends on the type of replication and use of slots.

The _timeline_ parameter can only be specified with physical replication and only starting with server version 9.3.

A dictionary of _options_ may be passed to the logical decoding plugin on a logical replication slot. The set of supported options depends on the output plugin that was used to create the slot. Must be `None` for physical replication.

If _decode_ is set to `True` the messages received from the server would be converted according to the connection [`encoding`](https://www.psycopg.org/docs/connection.html#connection.encoding "connection.encoding"). _This parameter should not be set with physical replication or with logical replication plugins that produce binary output._

Replication stream should periodically send feedback to the database to prevent disconnect via timeout. Feedback is automatically sent when [`read_message()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.read_message "psycopg2.extras.ReplicationCursor.read_message") is called or during run of the [`consume_stream()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream "psycopg2.extras.ReplicationCursor.consume_stream"). To specify the feedback interval use _status\_interval_ parameter. The value of this parameter must be set to at least 1 second, but it can have a fractional part.

This function constructs a [`START_REPLICATION`](https://www.postgresql.org/docs/current/static/protocol-replication.html) command and calls [`start_replication_expert()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication_expert "psycopg2.extras.ReplicationCursor.start_replication_expert") internally.

After starting the replication, to actually consume the incoming server messages use [`consume_stream()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream "psycopg2.extras.ReplicationCursor.consume_stream") or implement a loop around [`read_message()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.read_message "psycopg2.extras.ReplicationCursor.read_message") in case of [asynchronous connection](https://www.psycopg.org/docs/advanced.html#async-support).

Changed in version 2.8.3: added the _status\_interval_ parameter.

start_replication_expert(_command_, _decode=False_, _status\_interval=10_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication_expert "Link to this definition")
Start replication on the connection using provided [`START_REPLICATION`](https://www.postgresql.org/docs/current/static/protocol-replication.html) command.

Parameters:

* **command** – The full replication command. It can be a string or a [`Composable`](https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable "psycopg2.sql.Composable") instance for dynamic generation.

* **decode** – a flag indicating that unicode conversion should be performed on messages received from the server.

* **status_interval** – time between feedback packets sent to the server

Changed in version 2.8.3: added the _status\_interval_ parameter.

consume_stream(_consume_, _keepalive\_interval=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream "Link to this definition")Parameters:

* **consume** – a callable object with signature `consume(msg)`

* **keepalive_interval** – interval (in seconds) to send keepalive messages to the server

This method can only be used with synchronous connection. For asynchronous connections see [`read_message()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.read_message "psycopg2.extras.ReplicationCursor.read_message").

Before using this method to consume the stream call [`start_replication()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "psycopg2.extras.ReplicationCursor.start_replication") first.

This method enters an endless loop reading messages from the server and passing them to `consume()` one at a time, then waiting for more messages from the server. In order to make this method break out of the loop and return, `consume()` can throw a [`StopReplication`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.StopReplication "psycopg2.extras.StopReplication") exception. Any unhandled exception will make it break out of the loop as well.

The _msg_ object passed to `consume()` is an instance of [`ReplicationMessage`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage "psycopg2.extras.ReplicationMessage") class. See [`read_message()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.read_message "psycopg2.extras.ReplicationCursor.read_message") for details about message decoding.

This method also sends feedback messages to the server every _keepalive\_interval_ (in seconds). The value of this parameter must be set to at least 1 second, but it can have a fractional part. If the _keepalive\_interval_ is not specified, the value of _status\_interval_ specified in the [`start_replication()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "psycopg2.extras.ReplicationCursor.start_replication") or [`start_replication_expert()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication_expert "psycopg2.extras.ReplicationCursor.start_replication_expert") will be used.

The client must confirm every processed message by calling [`send_feedback()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.send_feedback "psycopg2.extras.ReplicationCursor.send_feedback") method on the corresponding replication cursor. A reference to the cursor is provided in the [`ReplicationMessage`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage "psycopg2.extras.ReplicationMessage") as an attribute.

The following example is a sketch implementation of `consume()` callable for logical replication:

class LogicalStreamConsumer(object):

    # ...

    def  __call__ (self, msg):
        self.process_message(msg.payload)
        msg.cursor.send_feedback(flush_lsn=msg.data_start)

consumer = LogicalStreamConsumer()
cur.consume_stream(consumer)

Warning

When using replication with slots, failure to constantly consume _and_ report success to the server appropriately can eventually lead to “disk full” condition on the server, because the server retains all the WAL segments that might be needed to stream the changes via all of the currently open replication slots.

Changed in version 2.8.3: changed the default value of the _keepalive\_interval_ parameter to `None`.

send_feedback(_write\_lsn=0_, _flush\_lsn=0_, _apply\_lsn=0_, _reply=False_, _force=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.send_feedback "Link to this definition")Parameters:

* **write_lsn** – a LSN position up to which the client has written the data locally

* **flush_lsn** – a LSN position up to which the client has processed the data reliably (the server is allowed to discard all and every data that predates this LSN)

* **apply_lsn** – a LSN position up to which the warm standby server has applied the changes (physical replication master-slave protocol only)

* **reply** – request the server to send back a keepalive message immediately

* **force** – force sending a feedback message regardless of status_interval timeout

Use this method to report to the server that all messages up to a certain LSN position have been processed on the client and may be discarded on the server.

If the _reply_ or _force_ parameters are not set, this method will just update internal structures without sending the feedback message to the server. The library sends feedback message automatically when _status\_interval_ timeout is reached. For this to work, you must call [`send_feedback()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.send_feedback "psycopg2.extras.ReplicationCursor.send_feedback") on the same Cursor that you called [`start_replication()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "psycopg2.extras.ReplicationCursor.start_replication") on (the one in `message.cursor`) or your feedback will be lost.

Changed in version 2.8.3: added the _force_ parameter.

Low-level replication cursor methods for [asynchronous connection](https://www.psycopg.org/docs/advanced.html#async-support) operation.

With the synchronous connection a call to [`consume_stream()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream "psycopg2.extras.ReplicationCursor.consume_stream") handles all the complexity of handling the incoming messages and sending keepalive replies, but at times it might be beneficial to use low-level interface for better control, in particular to [`select`](https://docs.python.org/3/library/select.html#module-select "(in Python v3.14)") on multiple sockets. The following methods are provided for asynchronous operation:

read_message()[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.read_message "Link to this definition")
Try to read the next message from the server without blocking and return an instance of [`ReplicationMessage`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage "psycopg2.extras.ReplicationMessage") or `None`, in case there are no more data messages from the server at the moment.

This method should be used in a loop with asynchronous connections (after calling [`start_replication()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "psycopg2.extras.ReplicationCursor.start_replication") once). For synchronous connections see [`consume_stream()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream "psycopg2.extras.ReplicationCursor.consume_stream").

The returned message’s [`payload`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationMessage.payload "psycopg2.extras.ReplicationMessage.payload") is an instance of `unicode` decoded according to connection [`encoding`](https://www.psycopg.org/docs/connection.html#connection.encoding "connection.encoding")_iff_ _decode_ was set to `True` in the initial call to [`start_replication()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.start_replication "psycopg2.extras.ReplicationCursor.start_replication") on this connection, otherwise it is an instance of `bytes` with no decoding.

It is expected that the calling code will call this method repeatedly in order to consume all of the messages that might have been buffered until `None` is returned. After receiving `None` from this method the caller should use `select()` or `poll()` on the corresponding connection to block the process until there is more data from the server.

Last, but not least, this method sends feedback messages when _status\_interval_ timeout is reached or when keepalive message with reply request arrived from the server.

fileno()[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.fileno "Link to this definition")
Call the corresponding connection’s [`fileno()`](https://www.psycopg.org/docs/connection.html#connection.fileno "connection.fileno") method and return the result.

This is a convenience method which allows replication cursor to be used directly in `select()` or `poll()` calls.

io_timestamp[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.io_timestamp "Link to this definition")
A [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)") object representing the timestamp at the moment of last communication with the server (a data or keepalive message in either direction).

feedback_timestamp[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.feedback_timestamp "Link to this definition")
A [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)") object representing the timestamp at the moment when the last feedback message sent to the server.

Added in version 2.8.3.

wal_end[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.wal_end "Link to this definition")
LSN position of the current end of WAL on the server at the moment of last data or keepalive message received from the server.

> Added in version 2.8.

An actual example of asynchronous operation might look like this:

from select import select
from datetime import datetime

def consume(msg):
    # ...
    msg.cursor.send_feedback(flush_lsn=msg.data_start)

status_interval = 10.0
while True:
    msg = cur.read_message()
    if msg:
        consume(msg)
    else:
        now = datetime.now()
        timeout = status_interval - (now - cur.feedback_timestamp).total_seconds()
        try:
            sel = select([cur], [], [], max(0, timeout))
        except InterruptedError:
            pass  # recalculate timeout and continue

_class_ psycopg2.extras.StopReplication[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.StopReplication "Link to this definition")
Exception used to break out of the endless loop in [`consume_stream()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream "psycopg2.extras.ReplicationCursor.consume_stream").

Subclass of `Exception`. Intentionally _not_ inherited from [`Error`](https://www.psycopg.org/docs/module.html#psycopg2.Error "psycopg2.Error") as occurrence of this exception does not indicate an error.

Additional data types[¶](https://www.psycopg.org/docs/extras.html#additional-data-types "Link to this heading")
---------------------------------------------------------------------------------------------------------------

### [JSON](https://www.json.org/) adaptation[¶](https://www.psycopg.org/docs/extras.html#json-adaptation "Link to this heading")

Added in version 2.5.

Changed in version 2.5.4: added `jsonb` support. In previous versions `jsonb` values are returned as strings. See [the FAQ](https://www.psycopg.org/docs/faq.html#faq-jsonb-adapt) for a workaround.

Psycopg can adapt Python objects to and from the PostgreSQL [`json` and `jsonb`](https://www.postgresql.org/docs/current/static/datatype-json.html) types. With PostgreSQL 9.2 and following versions adaptation is available out-of-the-box. To use JSON data with previous database versions (either with the [9.1 json extension](http://people.planetpostgresql.org/andrew/index.php?/archives/255-JSON-for-PG-9.2-...-and-now-for-9.1!.html), but even if you want to convert text fields to JSON) you can use the [`register_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_json "psycopg2.extras.register_json") function.

The Python [`json`](https://docs.python.org/3/library/json.html#module-json "(in Python v3.14)") module is used by default to convert Python objects to JSON and to parse data from the database.

In order to pass a Python object to the database as query argument you can use the [`Json`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Json "psycopg2.extras.Json") adapter:

curs.execute("insert into mytable (jsondata) values (%s)",
    [Json({'a': 100})])

Reading from the database, `json` and `jsonb` values will be automatically converted to Python objects.

Note

If you are using the PostgreSQL `json` data type but you want to read it as string in Python instead of having it parsed, your can either cast the column to `text` in the query (it is an efficient operation, that doesn’t involve a copy):

cur.execute("select jsondata::text from mytable")

or you can register a no-op `loads()` function with [`register_default_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_default_json "psycopg2.extras.register_default_json"):

psycopg2.extras.register_default_json(loads=lambda x: x)

Note

You can use [`register_adapter()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.register_adapter "psycopg2.extensions.register_adapter") to adapt any Python dictionary to JSON, either registering [`Json`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Json "psycopg2.extras.Json") or any subclass or factory creating a compatible adapter:

psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)

This setting is global though, so it is not compatible with similar adapters such as the one registered by [`register_hstore()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_hstore "psycopg2.extras.register_hstore"). Any other object supported by JSON can be registered the same way, but this will clobber the default adaptation rule, so be careful to unwanted side effects.

If you want to customize the adaptation from Python to PostgreSQL you can either provide a custom `dumps()` function to [`Json`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Json "psycopg2.extras.Json"):

curs.execute("insert into mytable (jsondata) values (%s)",
    [Json({'a': 100}, dumps=simplejson.dumps)])

or you can subclass it overriding the [`dumps()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Json.dumps "psycopg2.extras.Json.dumps") method:

class MyJson(Json):
    def dumps(self, obj):
        return simplejson.dumps(obj)

curs.execute("insert into mytable (jsondata) values (%s)",
    [MyJson({'a': 100})])

Customizing the conversion from PostgreSQL to Python can be done passing a custom `loads()` function to [`register_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_json "psycopg2.extras.register_json"). For the builtin data types (`json` from PostgreSQL 9.2, `jsonb` from PostgreSQL 9.4) use [`register_default_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_default_json "psycopg2.extras.register_default_json") and [`register_default_jsonb()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_default_jsonb "psycopg2.extras.register_default_jsonb"). For example, if you want to convert the float values from `json` into [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.14)") you can use:

loads = lambda x: json.loads(x, parse_float=Decimal)
psycopg2.extras.register_json(conn, loads=loads)

Or, if you want to use an alternative JSON module implementation, such as the faster [UltraJSON](https://pypi.org/project/ujson/), you can use:

psycopg2.extras.register_default_json(loads=ujson.loads, globally=True)
psycopg2.extras.register_default_jsonb(loads=ujson.loads, globally=True)

_class_ psycopg2.extras.Json(_adapted_, _dumps=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Json "Link to this definition")
An [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote") wrapper to adapt a Python object to `json` data type.

`Json` can be used to wrap any object supported by the provided _dumps_ function. If none is provided, the standard [`json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps "(in Python v3.14)") is used.

dumps(_obj_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Json.dumps "Link to this definition")
Serialize _obj_ in JSON format.

The default is to call `json.dumps()` or the _dumps_ function provided in the constructor. You can override this method to create a customized JSON wrapper.

psycopg2.extras.register_json(_conn\_or\_curs=None_, _globally=False_, _loads=None_, _oid=None_, _array\_oid=None_, _name='json'_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_json "Link to this definition")
Create and register typecasters converting `json` type to Python objects.

Parameters:

* **conn_or_curs** – a connection or cursor used to find the `json` and `json[]` oids; the typecasters are registered in a scope limited to this object, unless _globally_ is set to `True`. It can be `None` if the oids are provided

* **globally** – if `False` register the typecasters only on _conn\_or\_curs_, otherwise register them globally

* **loads** – the function used to parse the data into a Python object. If `None` use `json.loads()`, where `json` is the module chosen according to the Python version (see above)

* **oid** – the OID of the `json` type if known; If not, it will be queried on _conn\_or\_curs_

* **array_oid** – the OID of the `json[]` array type if known; if not, it will be queried on _conn\_or\_curs_

* **name** – the name of the data type to look for in _conn\_or\_curs_

The connection or cursor passed to the function will be used to query the database and look for the OID of the `json` type (or an alternative type if _name_ if provided). No query is performed if _oid_ and _array\_oid_ are provided. Raise [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") if the type is not found.

Changed in version 2.5.4: added the _name_ parameter to enable `jsonb` support.

psycopg2.extras.register_default_json(_conn\_or\_curs=None_, _globally=False_, _loads=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_default_json "Link to this definition")
Create and register `json` typecasters for PostgreSQL 9.2 and following.

Since PostgreSQL 9.2 `json` is a builtin type, hence its oid is known and fixed. This function allows specifying a customized _loads_ function for the default `json` type without querying the database. All the parameters have the same meaning of [`register_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_json "psycopg2.extras.register_json").

psycopg2.extras.register_default_jsonb(_conn\_or\_curs=None_, _globally=False_, _loads=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_default_jsonb "Link to this definition")
Create and register `jsonb` typecasters for PostgreSQL 9.4 and following.

As in [`register_default_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_default_json "psycopg2.extras.register_default_json"), the function allows to register a customized _loads_ function for the `jsonb` type at its known oid for PostgreSQL 9.4 and following versions. All the parameters have the same meaning of [`register_json()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_json "psycopg2.extras.register_json").

Added in version 2.5.4.

### Hstore data type[¶](https://www.psycopg.org/docs/extras.html#hstore-data-type "Link to this heading")

Added in version 2.3.

The [`hstore`](https://www.postgresql.org/docs/current/static/hstore.html) data type is a key-value store embedded in PostgreSQL. It has been available for several server versions but with the release 9.0 it has been greatly improved in capacity and usefulness with the addition of many functions. It supports GiST or GIN indexes allowing search by keys or key/value pairs as well as regular BTree indexes for equality, uniqueness etc.

Psycopg can convert Python `dict` objects to and from `hstore` structures. Only dictionaries with string/unicode keys and values are supported. `None` is also allowed as value but not as a key. Psycopg uses a more efficient `hstore` representation when dealing with PostgreSQL 9.0 but previous server versions are supported as well. By default the adapter/typecaster are disabled: they can be enabled using the [`register_hstore()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_hstore "psycopg2.extras.register_hstore") function.

psycopg2.extras.register_hstore(_conn\_or\_curs_, _globally=False_, _unicode=False_, _oid=None_, _array\_oid=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_hstore "Link to this definition")
Register adapter and typecaster for `dict`-`hstore` conversions.

Parameters:

* **conn_or_curs** – a connection or cursor: the typecaster will be registered only on this object unless _globally_ is set to `True`

* **globally** – register the adapter globally, not only on _conn\_or\_curs_

* **unicode** – if `True`, keys and values returned from the database will be `unicode` instead of `str`. The option is not available on Python 3

* **oid** – the OID of the `hstore` type if known. If not, it will be queried on _conn\_or\_curs_.

* **array_oid** – the OID of the `hstore` array type if known. If not, it will be queried on _conn\_or\_curs_.

The connection or cursor passed to the function will be used to query the database and look for the OID of the `hstore` type (which may be different across databases). If querying is not desirable (e.g. with [asynchronous connections](https://www.psycopg.org/docs/advanced.html#async-support)) you may specify it in the _oid_ parameter, which can be found using a query such as

```
SELECT
'hstore'::regtype::oid
```

. Analogously you can obtain a value for _array\_oid_ using a query such as `SELECT 'hstore[]'::regtype::oid`.

Note that, when passing a dictionary from Python to the database, both strings and unicode keys and values are supported. Dictionaries returned from the database have keys/values according to the _unicode_ parameter.

The `hstore` contrib module must be already installed in the database (executing the `hstore.sql` script in your `contrib` directory). Raise [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") if the type is not found.

Changed in version 2.4: added the _oid_ parameter. If not specified, the typecaster is installed also if `hstore` is not installed in the `public` schema.

Changed in version 2.4.3: added support for `hstore` array.

### Composite types casting[¶](https://www.psycopg.org/docs/extras.html#composite-types-casting "Link to this heading")

Added in version 2.4.

Using [`register_composite()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_composite "psycopg2.extras.register_composite") it is possible to cast a PostgreSQL composite type (either created with the [`CREATE TYPE`](https://www.postgresql.org/docs/current/static/sql-createtype.html) command or implicitly defined after a table row type) into a Python named tuple, or into a regular tuple if [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.14)") is not found.

>>> cur.execute("CREATE TYPE card AS (value int, suit text);")
>>> psycopg2.extras.register_composite('card', cur)
<psycopg2.extras.CompositeCaster object at 0x...>

>>> cur.execute("select (8, 'hearts')::card")
>>> cur.fetchone()[0]
card(value=8, suit='hearts')

Nested composite types are handled as expected, provided that the type of the composite components are registered as well.

>>> cur.execute("CREATE TYPE card_back AS (face card, back text);")
>>> psycopg2.extras.register_composite('card_back', cur)
<psycopg2.extras.CompositeCaster object at 0x...>

>>> cur.execute("select ((8, 'hearts'), 'blue')::card_back")
>>> cur.fetchone()[0]
card_back(face=card(value=8, suit='hearts'), back='blue')

Adaptation from Python tuples to composite types is automatic instead and requires no adapter registration.

Note

If you want to convert PostgreSQL composite types into something different than a `namedtuple` you can subclass the [`CompositeCaster`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster "psycopg2.extras.CompositeCaster") overriding [`make()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.make "psycopg2.extras.CompositeCaster.make"). For example, if you want to convert your type into a Python dictionary you can use:

>>> class DictComposite(psycopg2.extras.CompositeCaster):
...     def make(self, values):
...         return dict(zip(self.attnames, values))

>>> psycopg2.extras.register_composite('card', cur,
...     factory=DictComposite)

>>> cur.execute("select (8, 'hearts')::card")
>>> cur.fetchone()[0]
{'suit': 'hearts', 'value': 8}

psycopg2.extras.register_composite(_name_, _conn\_or\_curs_, _globally=False_, _factory=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_composite "Link to this definition")
Register a typecaster to convert a composite type into a tuple.

Parameters:

* **name** – the name of a PostgreSQL composite type, e.g. created using the [`CREATE TYPE`](https://www.postgresql.org/docs/current/static/sql-createtype.html) command

* **conn_or_curs** – a connection or cursor used to find the type oid and components; the typecaster is registered in a scope limited to this object, unless _globally_ is set to `True`

* **globally** – if `False` (default) register the typecaster only on _conn\_or\_curs_, otherwise register it globally

* **factory** – if specified it should be a [`CompositeCaster`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster "psycopg2.extras.CompositeCaster") subclass: use it to [customize how to cast composite types](https://www.psycopg.org/docs/extras.html#custom-composite)

Returns:
the registered [`CompositeCaster`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster "psycopg2.extras.CompositeCaster") or _factory_ instance responsible for the conversion

Changed in version 2.4.3: added support for array of composite types

Changed in version 2.5: added the _factory_ parameter

_class_ psycopg2.extras.CompositeCaster(_name_, _oid_, _attrs_, _array\_oid=None_, _schema=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster "Link to this definition")
Helps conversion of a PostgreSQL composite type into a Python object.

The class is usually created by the [`register_composite()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_composite "psycopg2.extras.register_composite") function. You may want to create and register manually instances of the class if querying the database at registration time is not desirable (such as when using an [asynchronous connections](https://www.psycopg.org/docs/advanced.html#async-support)).

make(_values_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.make "Link to this definition")
Return a new Python object representing the data being casted.

_values_ is the list of attributes, already casted into their Python representation.

You can subclass this method to [customize the composite cast](https://www.psycopg.org/docs/extras.html#custom-composite).

Added in version 2.5.

Object attributes:

name[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.name "Link to this definition")
The name of the PostgreSQL type.

schema[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.schema "Link to this definition")
The schema where the type is defined.

Added in version 2.5.

oid[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.oid "Link to this definition")
The oid of the PostgreSQL type.

array_oid[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.array_oid "Link to this definition")
The oid of the PostgreSQL array type, if available.

type[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.type "Link to this definition")
The type of the Python objects returned. If [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.14)") is available, it is a named tuple with attributes equal to the type components. Otherwise it is just the `tuple` object.

attnames[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.attnames "Link to this definition")
List of component names of the type to be casted.

atttypes[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.CompositeCaster.atttypes "Link to this definition")
List of component type oids of the type to be casted.

### Range data types[¶](https://www.psycopg.org/docs/extras.html#range-data-types "Link to this heading")

Added in version 2.5.

Psycopg offers a [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") Python type and supports adaptation between them and PostgreSQL [`range`](https://www.postgresql.org/docs/current/static/rangetypes.html) types. Builtin `range` types are supported out-of-the-box; user-defined `range` types can be adapted using [`register_range()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_range "psycopg2.extras.register_range").

_class_ psycopg2.extras.Range(_lower=None_, _upper=None_, _bounds='[)'_, _empty=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "Link to this definition")
Python representation for a PostgreSQL [`range`](https://www.postgresql.org/docs/current/static/rangetypes.html) type.

Parameters:

* **lower** – lower bound for the range. `None` means unbound

* **upper** – upper bound for the range. `None` means unbound

* **bounds** – one of the literal strings `()`, `[)`, `(]`, `[]`, representing whether the lower or upper bounds are included

* **empty** – if `True`, the range is empty

This Python type is only used to pass and retrieve range values to and from PostgreSQL and doesn’t attempt to replicate the PostgreSQL range features: it doesn’t perform normalization and doesn’t implement all the [operators](https://www.postgresql.org/docs/current/static/functions-range.html#RANGE-OPERATORS-TABLE) supported by the database.

`Range` objects are immutable, hashable, and support the `in` operator (checking if an element is within the range). They can be tested for equivalence. Empty ranges evaluate to `False` in boolean context, nonempty evaluate to `True`.

Changed in version 2.5.3: `Range` objects can be sorted although, as on the server-side, this ordering is not particularly meangingful. It is only meant to be used by programs assuming objects using `Range` as primary key can be sorted on them. In previous versions comparing `Range`s raises `TypeError`.

Although it is possible to instantiate `Range` objects, the class doesn’t have an adapter registered, so you cannot normally pass these instances as query arguments. To use range objects as query arguments you can either use one of the provided subclasses, such as [`NumericRange`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.NumericRange "psycopg2.extras.NumericRange") or create a custom subclass using [`register_range()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_range "psycopg2.extras.register_range").

Object attributes:

isempty[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range.isempty "Link to this definition")
`True` if the range is empty.

lower[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range.lower "Link to this definition")
The lower bound of the range. `None` if empty or unbound.

upper[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range.upper "Link to this definition")
The upper bound of the range. `None` if empty or unbound.

lower_inc[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range.lower_inc "Link to this definition")
`True` if the lower bound is included in the range.

upper_inc[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range.upper_inc "Link to this definition")
`True` if the upper bound is included in the range.

lower_inf[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range.lower_inf "Link to this definition")
`True` if the range doesn’t have a lower bound.

upper_inf[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range.upper_inf "Link to this definition")
`True` if the range doesn’t have an upper bound.

The following [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") subclasses map builtin PostgreSQL `range` types to Python objects: they have an adapter registered so their instances can be passed as query arguments. `range` values read from database queries are automatically casted into instances of these classes.

_class_ psycopg2.extras.NumericRange(_lower=None_, _upper=None_, _bounds='[)'_, _empty=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.NumericRange "Link to this definition")
A [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") suitable to pass Python numeric types to a PostgreSQL range.

PostgreSQL types `int4range`, `int8range`, `numrange` are casted into `NumericRange` instances.

_class_ psycopg2.extras.DateRange(_lower=None_, _upper=None_, _bounds='[)'_, _empty=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DateRange "Link to this definition")
Represents `daterange` values.

_class_ psycopg2.extras.DateTimeRange(_lower=None_, _upper=None_, _bounds='[)'_, _empty=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DateTimeRange "Link to this definition")
Represents `tsrange` values.

_class_ psycopg2.extras.DateTimeTZRange(_lower=None_, _upper=None_, _bounds='[)'_, _empty=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DateTimeTZRange "Link to this definition")
Represents `tstzrange` values.

Note

Python lacks a representation for `infinity` date so Psycopg converts the value to `date.max` and such. When written into the database these dates will assume their literal value (e.g. `9999-12-31` instead of `infinity`). Check [Infinite dates handling](https://www.psycopg.org/docs/usage.html#infinite-dates-handling) for an example of an alternative adapter to map `date.max` to `infinity`. An alternative dates adapter will be used automatically by the [`DateRange`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.DateRange "psycopg2.extras.DateRange") adapter and so on.

Custom `range` types (created with [`CREATE TYPE`](https://www.postgresql.org/docs/current/static/sql-createtype.html)`... AS RANGE`) can be adapted to a custom [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") subclass:

psycopg2.extras.register_range(_pgrange_, _pyrange_, _conn\_or\_curs_, _globally=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_range "Link to this definition")
Create and register an adapter and the typecasters to convert between a PostgreSQL [`range`](https://www.postgresql.org/docs/current/static/rangetypes.html) type and a PostgreSQL [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") subclass.

Parameters:

* **pgrange** – the name of the PostgreSQL `range` type. Can be schema-qualified

* **pyrange** – a [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") strict subclass, or just a name to give to a new class

* **conn_or_curs** – a connection or cursor used to find the oid of the range and its subtype; the typecaster is registered in a scope limited to this object, unless _globally_ is set to `True`

* **globally** – if `False` (default) register the typecaster only on _conn\_or\_curs_, otherwise register it globally

Returns:
[`RangeCaster`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster "psycopg2.extras.RangeCaster") instance responsible for the conversion

If a string is passed to _pyrange_, a new [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") subclass is created with such name and will be available as the [`range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster.range "psycopg2.extras.RangeCaster.range") attribute of the returned [`RangeCaster`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster "psycopg2.extras.RangeCaster") object.

The function queries the database on _conn\_or\_curs_ to inspect the _pgrange_ type and raises [`ProgrammingError`](https://www.psycopg.org/docs/module.html#psycopg2.ProgrammingError "psycopg2.ProgrammingError") if the type is not found. If querying the database is not advisable, use directly the [`RangeCaster`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster "psycopg2.extras.RangeCaster") class and register the adapter and typecasters using the provided functions.

_class_ psycopg2.extras.RangeCaster(_pgrange_, _pyrange_, _oid_, _subtype\_oid_, _array\_oid=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster "Link to this definition")
Helper class to convert between [`Range`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Range "psycopg2.extras.Range") and PostgreSQL range types.

Objects of this class are usually created by [`register_range()`](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_range "psycopg2.extras.register_range"). Manual creation could be useful if querying the database is not advisable: in this case the oids must be provided.

Object attributes:

range[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster.range "Link to this definition")
The `Range` subclass adapted.

adapter[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster.adapter "Link to this definition")
The [`ISQLQuote`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ISQLQuote "psycopg2.extensions.ISQLQuote") responsible to adapt `range`.

typecaster[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster.typecaster "Link to this definition")
The object responsible for casting.

array_typecaster[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RangeCaster.array_typecaster "Link to this definition")
The object responsible to cast arrays, if available, else `None`.

### UUID data type[¶](https://www.psycopg.org/docs/extras.html#uuid-data-type "Link to this heading")

Added in version 2.0.9.

Changed in version 2.0.13: added UUID array support.

>>> psycopg2.extras.register_uuid()
<psycopg2._psycopg.type object at 0x...>

>>> # Python UUID can be used in SQL queries
>>>
>>> import uuid
>>> my_uuid = uuid.UUID('{12345678-1234-5678-1234-567812345678}')
>>> psycopg2.extensions.adapt(my_uuid).getquoted()
"'12345678-1234-5678-1234-567812345678'::uuid"

>>> # PostgreSQL UUID are transformed into Python UUID objects
>>>
>>> cur.execute("SELECT 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'::uuid")
>>> cur.fetchone()[0]
UUID('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11')

psycopg2.extras.register_uuid(_oids=None_, _conn\_or\_curs=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_uuid "Link to this definition")
Create the UUID type and an uuid.UUID adapter.

Parameters:

* **oids** – oid for the PostgreSQL `uuid` type, or 2-items sequence with oids of the type and the array. If not specified, use PostgreSQL standard oids.

* **conn_or_curs** – where to register the typecaster. If not specified, register it globally.

_class_ psycopg2.extras.UUID_adapter(_uuid_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.UUID_adapter "Link to this definition")
Adapt Python’s [uuid.UUID](https://docs.python.org/library/uuid.html) type to PostgreSQL’s [uuid](https://www.postgresql.org/docs/current/static/datatype-uuid.html).

### Networking data types[¶](https://www.psycopg.org/docs/extras.html#networking-data-types "Link to this heading")

By default Psycopg casts the PostgreSQL networking data types (`inet`, `cidr`, `macaddr`) into ordinary strings; array of such types are converted into lists of strings.

Changed in version 2.7: in previous version array of networking types were not treated as arrays.

psycopg2.extras.register_ipaddress(_conn\_or\_curs=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_ipaddress "Link to this definition")
Register conversion support between [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "(in Python v3.14)") objects and [network types](https://www.postgresql.org/docs/current/static/datatype-net-types.html).

Parameters:
**conn_or_curs** – the scope where to register the type casters. If `None` register them globally.

After the function is called, PostgreSQL `inet` values will be converted into [`IPv4Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface "(in Python v3.14)") or [`IPv6Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface "(in Python v3.14)") objects, `cidr` values into into [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "(in Python v3.14)") or [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "(in Python v3.14)").

psycopg2.extras.register_inet(_oid=None_, _conn\_or\_curs=None_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.register_inet "Link to this definition")
Create the INET type and an Inet adapter.

Parameters:

* **oid** – oid for the PostgreSQL `inet` type, or 2-items sequence with oids of the type and the array. If not specified, use PostgreSQL standard oids.

* **conn_or_curs** – where to register the typecaster. If not specified, register it globally.

Deprecated since version 2.7: this function will not receive further development and may disappear in future versions.

>>> psycopg2.extras.register_inet()
<psycopg2._psycopg.type object at 0x...>

>>> cur.mogrify("SELECT %s", (Inet('127.0.0.1/32'),))
"SELECT E'127.0.0.1/32'::inet"

>>> cur.execute("SELECT '192.168.0.1/24'::inet")
>>> cur.fetchone()[0].addr
'192.168.0.1/24'

_class_ psycopg2.extras.Inet(_addr_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.Inet "Link to this definition")
Wrap a string to allow for correct SQL-quoting of inet values.

Note that this adapter does NOT check the passed value to make sure it really is an inet-compatible address but DOES call adapt() on it to make sure it is impossible to execute an SQL-injection by passing an evil value to the initializer.

Deprecated since version 2.7: this object will not receive further development and may disappear in future versions.

Fast execution helpers[¶](https://www.psycopg.org/docs/extras.html#fast-execution-helpers "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

The current implementation of [`executemany()`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany") is (using an extremely charitable understatement) not particularly performing. These functions can be used to speed up the repeated execution of a statement against a set of parameters. By reducing the number of server roundtrips the performance can be [orders of magnitude better](https://github.com/psycopg/psycopg2/issues/491#issuecomment-276551038) than using `executemany()`.

psycopg2.extras.execute_batch(_cur_, _sql_, _argslist_, _page\_size=100_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.execute_batch "Link to this definition")
Execute groups of statements in fewer server roundtrips.

Execute _sql_ several times, against all parameters set (sequences or mappings) found in _argslist_.

The function is semantically similar to

_cur_.[`executemany`](https://www.psycopg.org/docs/cursor.html#cursor.executemany "cursor.executemany")(_sql_, _argslist_)
but has a different implementation: Psycopg will join the statements into fewer multi-statement commands, each one containing at most _page\_size_ statements, resulting in a reduced number of server roundtrips.

After the execution of the function the [`cursor.rowcount`](https://www.psycopg.org/docs/cursor.html#cursor.rowcount "cursor.rowcount") property will **not** contain a total result.

>>> nums = ((1,), (5,), (10,))
>>> execute_batch(cur, "INSERT INTO test (num) VALUES (%s)", nums)

>>> tuples = ((123, "foo"), (42, "bar"), (23, "baz"))
>>> execute_batch(cur, "INSERT INTO test (num, data) VALUES (%s, %s)", tuples)

Added in version 2.7.

Note

`execute_batch()` can be also used in conjunction with PostgreSQL prepared statements using [`PREPARE`](https://www.postgresql.org/docs/current/static/sql-prepare.html), [`EXECUTE`](https://www.postgresql.org/docs/current/static/sql-execute.html), [`DEALLOCATE`](https://www.postgresql.org/docs/current/static/sql-deallocate.html). Instead of executing:

execute_batch(cur,
    "big and complex SQL with %s %s params",
    params_list)

it is possible to execute something like:

cur.execute("PREPARE stmt AS big and complex SQL with $1 $2 params")
execute_batch(cur, "EXECUTE stmt (%s, %s)", params_list)
cur.execute("DEALLOCATE stmt")

which may bring further performance benefits: if the operation to perform is complex, every single execution will be faster as the query plan is already cached; furthermore the amount of data to send on the server will be lesser (one `EXECUTE` per param set instead of the whole, likely longer, statement).

psycopg2.extras.execute_values(_cur_, _sql_, _argslist_, _template=None_, _page\_size=100_, _fetch=False_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.execute_values "Link to this definition")
Execute a statement using `VALUES` with a sequence of parameters.

Parameters:

* **cur** – the cursor to use to execute the query.

* **sql** – the query to execute. It must contain a single `%s` placeholder, which will be replaced by a [VALUES list](https://www.postgresql.org/docs/current/static/queries-values.html). Example: `"INSERT INTO mytable (id, f1, f2) VALUES %s"`.

* **argslist** – sequence of sequences or dictionaries with the arguments to send to the query. The type and content must be consistent with _template_.

* **template** –

the snippet to merge to every item in _argslist_ to compose the query.

    *   If the _argslist_ items are sequences it should contain positional placeholders (e.g. `"(%s, %s, %s)"`, or `"(%s, %s, 42)`” if there are constants value…).

    *   If the _argslist_ items are mappings it should contain named placeholders (e.g. `"(%(id)s, %(f1)s, 42)"`).

If not specified, assume the arguments are sequence and use a simple positional template (i.e. `(%s, %s, ...)`), with the number of placeholders sniffed by the first element in _argslist_.

* **page_size** – maximum number of _argslist_ items to include in every statement. If there are more items the function will execute more than one statement.

* **fetch** – if `True` return the query results into a list (like in a [`fetchall()`](https://www.psycopg.org/docs/cursor.html#cursor.fetchall "cursor.fetchall")). Useful for queries with `RETURNING` clause.

After the execution of the function the [`cursor.rowcount`](https://www.psycopg.org/docs/cursor.html#cursor.rowcount "cursor.rowcount") property will **not** contain a total result.

While `INSERT` is an obvious candidate for this function it is possible to use it with other statements, for example:

>>> cur.execute(
... "create table test (id int primary key, v1 int, v2 int)")

>>> execute_values(cur,
... "INSERT INTO test (id, v1, v2) VALUES %s",
... [(1, 2, 3), (4, 5, 6), (7, 8, 9)])

>>> execute_values(cur,
... """UPDATE test SET v1 = data.v1 FROM (VALUES %s) AS data (id, v1)
... WHERE test.id = data.id""",
... [(1, 20), (4, 50)])

>>> cur.execute("select * from test order by id")
>>> cur.fetchall()
[(1, 20, 3), (4, 50, 6), (7, 8, 9)])

Added in version 2.7.

Changed in version 2.8: added the _fetch_ parameter.

Coroutine support[¶](https://www.psycopg.org/docs/extras.html#coroutine-support "Link to this heading")
-------------------------------------------------------------------------------------------------------

psycopg2.extras.wait_select(_conn_)[¶](https://www.psycopg.org/docs/extras.html#psycopg2.extras.wait_select "Link to this definition")
Wait until a connection or cursor has data available.

The function is an example of a wait callback to be registered with [`set_wait_callback()`](https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.set_wait_callback "psycopg2.extensions.set_wait_callback"). This function uses [`select()`](https://docs.python.org/3/library/select.html#select.select "(in Python v3.14)") to wait for data to become available, and therefore is able to handle/receive SIGINT/KeyboardInterrupt.

Changed in version 2.6.2: allow to cancel a query using Ctrl-C, see [the FAQ](https://www.psycopg.org/docs/faq.html#faq-interrupt-query) for an example.
