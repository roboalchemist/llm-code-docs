# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html

Title: Virtual AMQ Exchange Implementation - kombu.transport.virtual.exchange — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.virtual.exchange.html).

Virtual AMQ Exchange.

Implementations of the standard exchanges defined by the AMQ protocol (excluding the headers exchange).

*   [Direct](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#direct)

*   [Topic](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#topic)

*   [Fanout](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#fanout)

*   [Interface](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#interface)

[Direct](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#direct "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.exchange.DirectExchange(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#DirectExchange)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.DirectExchange "Link to this definition")
Direct exchange.

The direct exchange routes based on exact routing keys.

deliver(_message_, _exchange_, _routing\_key_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#DirectExchange.deliver)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.DirectExchange.deliver "Link to this definition")lookup(_table_, _exchange_, _routing\_key_, _default_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#DirectExchange.lookup)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.DirectExchange.lookup "Link to this definition")
Lookup all queues matching routing_key in exchange.

Returns:
**str**

Return type:
queue name, or ‘default’ if no queues matched.

type _='direct'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.DirectExchange.type "Link to this definition")
[Topic](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#topic "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.exchange.TopicExchange(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#TopicExchange)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.TopicExchange "Link to this definition")
Topic exchange.

The topic exchange routes messages based on words separated by dots, using wildcard characters `*` (any single word), and `#` (one or more words).

deliver(_message_, _exchange_, _routing\_key_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#TopicExchange.deliver)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.TopicExchange.deliver "Link to this definition")key_to_pattern(_rkey_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#TopicExchange.key_to_pattern)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.TopicExchange.key_to_pattern "Link to this definition")
Get the corresponding regex for any routing key.

lookup(_table_, _exchange_, _routing\_key_, _default_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#TopicExchange.lookup)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.TopicExchange.lookup "Link to this definition")
Lookup all queues matching routing_key in exchange.

Returns:
**str**

Return type:
queue name, or ‘default’ if no queues matched.

prepare_bind(_queue_, _exchange_, _routing\_key_, _arguments_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#TopicExchange.prepare_bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.TopicExchange.prepare_bind "Link to this definition")
Prepare queue-binding.

Returns:
**Tuple[str, Pattern, str]** – to be stored for bindings to this exchange.

Return type:
of (routing_key, regex, queue)

type _='topic'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.TopicExchange.type "Link to this definition")wildcards _={'#':'.*?','*':'.*?[^\\.]'}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.TopicExchange.wildcards "Link to this definition")
map of wildcard to regex conversions

[Fanout](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#fanout "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.exchange.FanoutExchange(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#FanoutExchange)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.FanoutExchange "Link to this definition")
Fanout exchange.

The fanout exchange implements broadcast messaging by delivering copies of all messages to all queues bound to the exchange.

To support fanout the virtual channel needs to store the table as shared state. This requires that the Channel.supports_fanout attribute is set to true, and the Channel._queue_bind and Channel.get_table methods are implemented.

deliver(_message_, _exchange_, _routing\_key_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#FanoutExchange.deliver)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.FanoutExchange.deliver "Link to this definition")lookup(_table_, _exchange_, _routing\_key_, _default_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#FanoutExchange.lookup)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.FanoutExchange.lookup "Link to this definition")
Lookup all queues matching routing_key in exchange.

Returns:
**str**

Return type:
queue name, or ‘default’ if no queues matched.

type _='fanout'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.FanoutExchange.type "Link to this definition")
[Interface](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#interface "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.exchange.ExchangeType(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#ExchangeType)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.ExchangeType "Link to this definition")
Base class for exchanges.

Implements the specifics for an exchange type.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#arguments "Link to this heading")

> channel (ChannelT): AMQ Channel.

equivalent(_prev_, _exchange_, _type_, _durable_, _auto\_delete_, _arguments_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#ExchangeType.equivalent)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.ExchangeType.equivalent "Link to this definition")
Return true if prev and exchange is equivalent.

lookup(_table_, _exchange_, _routing\_key_, _default_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#ExchangeType.lookup)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.ExchangeType.lookup "Link to this definition")
Lookup all queues matching routing_key in exchange.

Returns:
**str**

Return type:
queue name, or ‘default’ if no queues matched.

prepare_bind(_queue_, _exchange_, _routing\_key_, _arguments_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/exchange.html#ExchangeType.prepare_bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.ExchangeType.prepare_bind "Link to this definition")
Prepare queue-binding.

Returns:
**Tuple[str, Pattern, str]** – to be stored for bindings to this exchange.

Return type:
of (routing_key, regex, queue)

type _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.ExchangeType.type "Link to this definition")
