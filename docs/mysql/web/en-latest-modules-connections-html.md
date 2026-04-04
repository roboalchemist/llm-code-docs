# Source: https://pymysql.readthedocs.io/en/latest/modules/connections.html

Title: Connection Object — PyMySQL 0.7.2 documentation

URL Source: https://pymysql.readthedocs.io/en/latest/modules/connections.html

Published Time: Wed, 21 May 2025 09:37:12 GMT

Markdown Content:
Connection Object — PyMySQL 0.7.2 documentation
===============

[PyMySQL](https://pymysql.readthedocs.io/en/latest/index.html)

* [User Guide](https://pymysql.readthedocs.io/en/latest/user/index.html)
* [API Reference](https://pymysql.readthedocs.io/en/latest/modules/index.html)
  * [Connection Object](https://pymysql.readthedocs.io/en/latest/modules/connections.html#)
    * [`Connection`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection)
      * [`Connection.begin()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.begin)
      * [`Connection.close()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.close)
      * [`Connection.commit()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.commit)
      * [`Connection.cursor()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.cursor)
      * [`Connection.open`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.open)
      * [`Connection.ping()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.ping)
      * [`Connection.rollback()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.rollback)
      * [`Connection.select_db()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.select_db)
      * [`Connection.set_character_set()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.set_character_set)
      * [`Connection.set_charset()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.set_charset)
      * [`Connection.show_warnings()`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.show_warnings)

  * [Cursor Objects](https://pymysql.readthedocs.io/en/latest/modules/cursors.html)

[PyMySQL](https://pymysql.readthedocs.io/en/latest/index.html)

* [](https://pymysql.readthedocs.io/en/latest/index.html)
* [API Reference](https://pymysql.readthedocs.io/en/latest/modules/index.html)
* Connection Object
* [View page source](https://pymysql.readthedocs.io/en/latest/_sources/modules/connections.rst.txt)

* * *

Connection Object[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#module-pymysql.connections "Link to this heading")
=========================================================================================================================================

_class_ pymysql.connections.Connection(_*_, _user=None_, _password=''_, _host=None_, _database=None_, _unix\_socket=None_, _port=0_, _charset=''_, _collation=None_, _sql\_mode=None_, _read\_default\_file=None_, _conv=None_, _use\_unicode=True_, _client\_flag=0_, _cursorclass=<class'pymysql.cursors.Cursor'>_, _init\_command=None_, _connect\_timeout=10_, _read\_default\_group=None_, _autocommit=False_, _local\_infile=False_, _max\_allowed\_packet=16777216_, _defer\_connect=False_, _auth\_plugin\_map=None_, _read\_timeout=None_, _write\_timeout=None_, _bind\_address=None_, _binary\_prefix=False_, _program\_name=None_, _server\_public\_key=None_, _ssl=None_, _ssl\_ca=None_, _ssl\_cert=None_, _ssl\_disabled=None_, _ssl\_key=None_, _ssl\_key\_password=None_, _ssl\_verify\_cert=None_, _ssl\_verify\_identity=None_, _compress=None_, _named\_pipe=None_, _passwd=None_, _db=None_)[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection "Link to this definition")
Representation of a socket with a mysql server.

The proper way to get an instance of this class is to call connect().

Establish a connection to the MySQL database. Accepts several arguments:

Parameters:

* **host** – Host where the database server is located.

* **user** – Username to log in as.

* **password** – Password to use.

* **database** – Database to use, None to not use a particular one.

* **port** – MySQL port to use, default is usually OK. (default: 3306)

* **bind_address** – When the client has multiple network interfaces, specify the interface from which to connect to the host. Argument can be a hostname or an IP address.

* **unix_socket** – Use a unix socket rather than TCP/IP.

* **read_timeout** – The timeout for reading from the connection in seconds. (default: None - no timeout)

* **write_timeout** – The timeout for writing to the connection in seconds. (default: None - no timeout)

* **charset** (_str_) – Charset to use.

* **collation** (_str_) – Collation name to use.

* **sql_mode** – Default SQL_MODE to use.

* **read_default_file** – Specifies my.cnf file to read these parameters from under the [client] section.

* **conv** – Conversion dictionary to use instead of the default one. This is used to provide custom marshalling and unmarshalling of types. See converters.

* **use_unicode** – Whether or not to default to unicode strings. This option defaults to true.

* **client_flag** – Custom flags to send to MySQL. Find potential values in constants.CLIENT.

* **cursorclass** – Custom cursor class to use.

* **init_command** – Initial SQL statement to run when connection is established.

* **connect_timeout** – The timeout for connecting to the database in seconds. (default: 10, min: 1, max: 31536000)

* **ssl** – A dict of arguments similar to mysql_ssl_set()’s parameters or an ssl.SSLContext.

* **ssl_ca** – Path to the file that contains a PEM-formatted CA certificate.

* **ssl_cert** – Path to the file that contains a PEM-formatted client certificate.

* **ssl_disabled** – A boolean value that disables usage of TLS.

* **ssl_key** – Path to the file that contains a PEM-formatted private key for the client certificate.

* **ssl_key_password** – The password for the client certificate private key.

* **ssl_verify_cert** – Set to true to check the server certificate’s validity.

* **ssl_verify_identity** – Set to true to check the server’s identity.

* **read_default_group** – Group to read from in the configuration file.

* **autocommit** – Autocommit mode. None means use server default. (default: False)

* **local_infile** – Boolean to enable the use of LOAD DATA LOCAL command. (default: False)

* **max_allowed_packet** – Max size of packet sent to server in bytes. (default: 16MB) Only used to limit size of “LOAD LOCAL INFILE” data packet smaller than default (16KB).

* **defer_connect** – Don’t explicitly connect on construction - wait for connect call. (default: False)

* **auth_plugin_map** – A dict of plugin names to a class that processes that plugin. The class will take the Connection object as the argument to the constructor. The class needs an authenticate method taking an authentication packet as an argument. For the dialog plugin, a prompt(echo, prompt) method can be used (if no authenticate method) for returning a string from the user. (experimental)

* **server_public_key** – SHA256 authentication plugin public key value. (default: None)

* **binary_prefix** – Add _binary prefix on bytes and bytearray. (default: False)

* **compress** – Not supported.

* **named_pipe** – Not supported.

* **db** – **DEPRECATED** Alias for database.

* **passwd** – **DEPRECATED** Alias for password.

See [Connection](https://www.python.org/dev/peps/pep-0249/#connection-objects) in the specification.

begin()[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.begin "Link to this definition")
Begin transaction.

close()[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.close "Link to this definition")
Send the quit message and close the socket.

See [Connection.close()](https://www.python.org/dev/peps/pep-0249/#Connection.close) in the specification.

Raises:
**Error** – If the connection is already closed.

commit()[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.commit "Link to this definition")
Commit changes to stable storage.

See [Connection.commit()](https://www.python.org/dev/peps/pep-0249/#commit) in the specification.

cursor(_cursor=None_)[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.cursor "Link to this definition")
Create a new cursor to execute queries with.

Parameters:
**cursor** (`Cursor`, `SSCursor`, `DictCursor`, or `SSDictCursor`.) – The type of cursor to create. None means use Cursor.

_property_ open[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.open "Link to this definition")
Return True if the connection is open.

ping(_reconnect=True_)[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.ping "Link to this definition")
Check if the server is alive.

Parameters:
**reconnect** (_boolean_) – If the connection is closed, reconnect.

Raises:
**Error** – If the connection is closed and reconnect=False.

rollback()[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.rollback "Link to this definition")
Roll back the current transaction.

See [Connection.rollback()](https://www.python.org/dev/peps/pep-0249/#rollback) in the specification.

select_db(_db_)[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.select_db "Link to this definition")
Set current db.

Parameters:
**db** – The name of the db.

set_character_set(_charset_, _collation=None_)[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.set_character_set "Link to this definition")
Set charaset (and collation)

Send “SET NAMES charset [COLLATE collation]” query. Update Connection.encoding based on charset.

set_charset(_charset_)[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.set_charset "Link to this definition")
Deprecated. Use set_character_set() instead.

show_warnings()[](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.show_warnings "Link to this definition")
Send the “SHOW WARNINGS” SQL command.

[Previous](https://pymysql.readthedocs.io/en/latest/modules/index.html "API Reference")[Next](https://pymysql.readthedocs.io/en/latest/modules/cursors.html "Cursor Objects")

* * *

© Copyright 2023, Inada Naoki and GitHub contributors.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
