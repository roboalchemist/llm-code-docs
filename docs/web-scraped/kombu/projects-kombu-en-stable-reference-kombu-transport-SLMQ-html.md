# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html

Title: kombu.transport.SLMQ — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.SLMQ.html).

SoftLayer Message Queue transport module for kombu.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: No

*   Supports Priority: No

*   Supports TTL: No

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#connection-string "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> _Unreviewed_

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#transport-options "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> _Unreviewed_

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.SLMQ.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SLMQ.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport "Link to this definition")
SLMQ Transport.

_class_ Channel(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "Link to this definition")
SLMQ Channel.

basic_ack(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.basic_ack "Link to this definition")
Acknowledge message.

basic_cancel(_consumer\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.basic_consume "Link to this definition")
Consume from queue.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.conninfo "Link to this definition")default_visibility_timeout _=1800_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.default_visibility_timeout "Link to this definition")delete_message(_queue_, _message\_id_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.delete_message "Link to this definition")domain_format _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.domain_format "Link to this definition")entity_name(_name_, _table={33:95,34:95,35:95,36:95,37:95,38:95,39:95,40:95,41:95,42:95,43:95,44:95,45:95,46:95,47:95,58:95,59:95,60:95,61:95,62:95,63:95,64:95,91:95,92:95,93:95,94:95,96:95,123:95,124:95,125:95,126:95}_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.entity_name "Link to this definition")
Format AMQP queue name into a valid SLQS queue name.

_property_ queue_name_prefix[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.queue_name_prefix "Link to this definition")_property_ slmq[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.slmq "Link to this definition")_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.transport_options "Link to this definition")_property_ visibility_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel.visibility_timeout "Link to this definition")connection_errors _=(<class'amqp.exceptions.ConnectionError'>,None,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

default_port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.default_port "Link to this definition")
port number used when no port is specified.

polling_interval _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.SLMQ.Channel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SLMQ.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel "Link to this definition")
SLMQ Channel.

basic_ack(_delivery\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SLMQ.html#Channel.basic_ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.basic_ack "Link to this definition")
Acknowledge message.

basic_cancel(_consumer\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SLMQ.html#Channel.basic_cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SLMQ.html#Channel.basic_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.basic_consume "Link to this definition")
Consume from queue.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.conninfo "Link to this definition")default_visibility_timeout _=1800_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.default_visibility_timeout "Link to this definition")delete_message(_queue_, _message\_id_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SLMQ.html#Channel.delete_message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.delete_message "Link to this definition")domain_format _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.domain_format "Link to this definition")entity_name(_name_, _table={33:95,34:95,35:95,36:95,37:95,38:95,39:95,40:95,41:95,42:95,43:95,44:95,45:95,46:95,47:95,58:95,59:95,60:95,61:95,62:95,63:95,64:95,91:95,92:95,93:95,94:95,96:95,123:95,124:95,125:95,126:95}_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/SLMQ.html#Channel.entity_name)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.entity_name "Link to this definition")
Format AMQP queue name into a valid SLQS queue name.

_property_ queue_name_prefix[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.queue_name_prefix "Link to this definition")_property_ slmq[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.slmq "Link to this definition")_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.transport_options "Link to this definition")_property_ visibility_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Channel.visibility_timeout "Link to this definition")
