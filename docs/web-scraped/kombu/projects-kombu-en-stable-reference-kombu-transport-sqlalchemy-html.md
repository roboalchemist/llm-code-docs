# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html

Title: SQLAlchemy Transport Model - kombu.transport.sqlalchemy — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.sqlalchemy.html).

SQLAlchemy Transport module for kombu.

Kombu transport using SQL Database as the message store.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: yes

*   Supports Topic: yes

*   Supports Fanout: no

*   Supports Priority: no

*   Supports TTL: no

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#connection-string "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

sqla+SQL_ALCHEMY_CONNECTION_STRING
sqlalchemy+SQL_ALCHEMY_CONNECTION_STRING

For details about `SQL_ALCHEMY_CONNECTION_STRING` see SQLAlchemy Engine Configuration documentation.

Examples

# PostgreSQL with default driver
sqla+postgresql://scott:tiger@localhost/mydatabase

# PostgreSQL with psycopg2 driver
sqla+postgresql+psycopg2://scott:tiger@localhost/mydatabase

# PostgreSQL with pg8000 driver
sqla+postgresql+pg8000://scott:tiger@localhost/mydatabase

# MySQL with default driver
sqla+mysql://scott:tiger@localhost/foo

# MySQL with mysqlclient driver (a maintained fork of MySQL-Python)
sqla+mysql+mysqldb://scott:tiger@localhost/foo

# MySQL with PyMySQL driver
sqla+mysql+pymysql://scott:tiger@localhost/foo

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#transport-options "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   `queue_tablename`: Name of table storing queues.

*   `message_tablename`: Name of table storing messages.

Moreover parameters of `sqlalchemy.create_engine()` function can be passed as transport options.

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#channel)

*   [SQLAlchemy Transport Model - `kombu.transport.sqlalchemy.models`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#module-kombu.transport.sqlalchemy.models)

    *   [Models](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#models)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.sqlalchemy.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/sqlalchemy.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport "Link to this definition")
The transport class.

_class_ Channel(_connection_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.Channel "Link to this definition")
The channel class.

_property_ message_cls[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.Channel.message_cls "Link to this definition")_property_ queue_cls[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.Channel.queue_cls "Link to this definition")_property_ session[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.Channel.session "Link to this definition")can_parse_url _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.can_parse_url "Link to this definition")
Set to True if [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") should pass the URL unmodified.

connection_errors _=(<class'sqlalchemy.exc.OperationalError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

default_port _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='sqlalchemy'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='sql'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/sqlalchemy.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Transport.driver_version "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.sqlalchemy.Channel(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/sqlalchemy.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Channel "Link to this definition")
The channel class.

_property_ message_cls[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Channel.message_cls "Link to this definition")_property_ queue_cls[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Channel.queue_cls "Link to this definition")_property_ session[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.Channel.session "Link to this definition")
[SQLAlchemy Transport Model - `kombu.transport.sqlalchemy.models`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#module-kombu.transport.sqlalchemy.models "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kombu transport using SQLAlchemy as the message store.

*   [Models](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#models)

### [Models](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#id9)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#models "Link to this heading")

_class_ kombu.transport.sqlalchemy.models.Queue(_name_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/sqlalchemy/models.html#Queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Queue "Link to this definition")
The queue class.

id _=Column(None,Integer(),table=None,primary\_key=True,nullable=False,default=Sequence('queue\_id\_sequence'))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Queue.id "Link to this definition")name _=Column(None,String(length=200),table=None)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Queue.name "Link to this definition")_class_ kombu.transport.sqlalchemy.models.Message(_payload_, _queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/sqlalchemy/models.html#Message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Message "Link to this definition")
The message class.

id _=Column(None,Integer(),table=None,primary\_key=True,nullable=False,default=Sequence('message\_id\_sequence'))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Message.id "Link to this definition")visible _=Column(None,Boolean(),table=None,default=ScalarElementColumnDefault(True))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Message.visible "Link to this definition")sent_at _=Column('timestamp',DateTime(),table=None,onupdate=CallableColumnDefault(<function datetime.now>))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Message.sent_at "Link to this definition")payload _=Column(None,Text(),table=None,nullable=False)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Message.payload "Link to this definition")version _=Column(None,SmallInteger(),table=None,nullable=False,default=ScalarElementColumnDefault(1))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.sqlalchemy.html#kombu.transport.sqlalchemy.models.Message.version "Link to this definition")
