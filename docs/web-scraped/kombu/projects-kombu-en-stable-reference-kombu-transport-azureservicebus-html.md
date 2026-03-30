# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html

Title: Azure Service Bus Transport - kombu.transport.azureservicebus — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.azureservicebus.html).

Azure Service Bus Message Queue transport module for kombu.

Note that the Shared Access Policy used to connect to Azure Service Bus requires Manage, Send and Listen claims since the broker will create new queues and delete old queues as required.

Notes when using with Celery if you are experiencing issues with programs not terminating properly. The Azure Service Bus SDK uses the Azure uAMQP library which in turn creates some threads. If the AzureServiceBus Channel is closed, said threads will be closed properly, but it seems there are times when Celery does not do this so these threads will be left running. As the uAMQP threads are not marked as Daemon threads, they will not be killed when the main thread exits. Setting the `uamqp_keep_alive_interval` transport option to 0 will prevent the keep_alive thread from starting

More information about Azure Service Bus: [https://azure.microsoft.com/en-us/services/service-bus/](https://azure.microsoft.com/en-us/services/service-bus/)

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#features "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: _Unreviewed_

*   Supports Topic: _Unreviewed_

*   Supports Fanout: _Unreviewed_

*   Supports Priority: _Unreviewed_

*   Supports TTL: _Unreviewed_

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#connection-string "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string has the following formats:

azureservicebus://SAS_POLICY_NAME:SAS_KEY@SERVICE_BUSNAMESPACE
azureservicebus://DefaultAzureCredential@SERVICE_BUSNAMESPACE
azureservicebus://ManagedIdentityCredential@SERVICE_BUSNAMESPACE

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#transport-options "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   `queue_name_prefix` - String prefix to prepend to queue names in a service bus namespace.

*   `wait_time_seconds` - Number of seconds to wait to receive messages. Default `5`

*   `peek_lock_seconds` - Number of seconds the message is visible for before it is requeued and sent to another consumer. Default `60`

*   `uamqp_keep_alive_interval` - Interval in seconds the Azure uAMQP library should send keepalive messages. Default `30`

*   `retry_total` - Azure SDK retry total. Default `3`

*   `retry_backoff_factor` - Azure SDK exponential backoff factor. Default `0.8`

*   `retry_backoff_max` - Azure SDK retry total time. Default `120`

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#transport "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.azureservicebus.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport "Link to this definition")
Azure Service Bus transport.

_class_ Channel(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel "Link to this definition")
Azure Service Bus channel.

basic_ack(_delivery\_tag:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _multiple:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")=False_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.basic_ack "Link to this definition")
Acknowledge message.

basic_cancel(_consumer\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.basic_consume "Link to this definition")
Consume from queue.

close()→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.conninfo "Link to this definition")default_peek_lock_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=60_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.default_peek_lock_seconds "Link to this definition")default_retry_backoff_factor _:[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")_ _=0.8_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.default_retry_backoff_factor "Link to this definition")default_retry_backoff_max _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=120_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.default_retry_backoff_max "Link to this definition")default_retry_total _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=3_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.default_retry_total "Link to this definition")default_uamqp_keep_alive_interval _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=30_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.default_uamqp_keep_alive_interval "Link to this definition")default_wait_time_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=5_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.default_wait_time_seconds "Link to this definition")domain_format _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_ _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.domain_format "Link to this definition")entity_name(_name:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _table:[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")[[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)"),[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")]|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.entity_name "Link to this definition")
Format AMQP queue name into a valid ServiceBus queue name.

_property_ peek_lock_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.peek_lock_seconds "Link to this definition")_property_ queue_mgmt_service _:ServiceBusAdministrationClient_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.queue_mgmt_service "Link to this definition")_property_ queue_name_prefix _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.queue_name_prefix "Link to this definition")_property_ queue_service _:ServiceBusClient_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.queue_service "Link to this definition")_property_ retry_backoff_factor _:[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.retry_backoff_factor "Link to this definition")_property_ retry_backoff_max _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.retry_backoff_max "Link to this definition")_property_ retry_total _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.retry_total "Link to this definition")_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.transport_options "Link to this definition")_property_ uamqp_keep_alive_interval _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.uamqp_keep_alive_interval "Link to this definition")_property_ wait_time_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.Channel.wait_time_seconds "Link to this definition")_classmethod_ as_uri(_uri:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _include\_password=False_, _mask='**'_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Transport.as_uri)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.as_uri "Link to this definition")
Customise the display format of the URI.

can_parse_url _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.can_parse_url "Link to this definition")
Set to True if [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") should pass the URL unmodified.

default_port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.default_port "Link to this definition")
port number used when no port is specified.

_static_ parse_uri(_uri:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|DefaultAzureCredential|ManagedIdentityCredential][[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Transport.parse_uri)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.parse_uri "Link to this definition")polling_interval _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#channel "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.azureservicebus.Channel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel "Link to this definition")
Azure Service Bus channel.

basic_ack(_delivery\_tag:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _multiple:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")=False_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Channel.basic_ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.basic_ack "Link to this definition")
Acknowledge message.

basic_cancel(_consumer\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Channel.basic_cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Channel.basic_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.basic_consume "Link to this definition")
Consume from queue.

close()→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Channel.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.conninfo "Link to this definition")default_peek_lock_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=60_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.default_peek_lock_seconds "Link to this definition")default_retry_backoff_factor _:[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")_ _=0.8_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.default_retry_backoff_factor "Link to this definition")default_retry_backoff_max _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=120_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.default_retry_backoff_max "Link to this definition")default_retry_total _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=3_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.default_retry_total "Link to this definition")default_uamqp_keep_alive_interval _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=30_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.default_uamqp_keep_alive_interval "Link to this definition")default_wait_time_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=5_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.default_wait_time_seconds "Link to this definition")domain_format _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_ _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.domain_format "Link to this definition")entity_name(_name:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _table:[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")[[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)"),[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")]|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azureservicebus.html#Channel.entity_name)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.entity_name "Link to this definition")
Format AMQP queue name into a valid ServiceBus queue name.

_property_ peek_lock_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.peek_lock_seconds "Link to this definition")_property_ queue_mgmt_service _:ServiceBusAdministrationClient_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.queue_mgmt_service "Link to this definition")_property_ queue_name_prefix _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.queue_name_prefix "Link to this definition")_property_ queue_service _:ServiceBusClient_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.queue_service "Link to this definition")_property_ retry_backoff_factor _:[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.retry_backoff_factor "Link to this definition")_property_ retry_backoff_max _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.retry_backoff_max "Link to this definition")_property_ retry_total _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.retry_total "Link to this definition")_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.transport_options "Link to this definition")_property_ uamqp_keep_alive_interval _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.uamqp_keep_alive_interval "Link to this definition")_property_ wait_time_seconds _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azureservicebus.html#kombu.transport.azureservicebus.Channel.wait_time_seconds "Link to this definition")
