# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html

Title: Azure Storage Queues Transport - kombu.transport.azurestoragequeues — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.azurestoragequeues.html).

Azure Storage Queues transport module for kombu.

More information about Azure Storage Queues: [https://azure.microsoft.com/en-us/services/storage/queues/](https://azure.microsoft.com/en-us/services/storage/queues/)

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#features "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: _Unreviewed_

*   Supports Topic: _Unreviewed_

*   Supports Fanout: _Unreviewed_

*   Supports Priority: _Unreviewed_

*   Supports TTL: _Unreviewed_

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#connection-string "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string has the following formats:

azurestoragequeues://<STORAGE_ACCOUNT_ACCESS_KEY>@<STORAGE_ACCOUNT_URL>
azurestoragequeues://<SAS_TOKEN>@<STORAGE_ACCOUNT_URL>
azurestoragequeues://DefaultAzureCredential@<STORAGE_ACCOUNT_URL>
azurestoragequeues://ManagedIdentityCredential@<STORAGE_ACCOUNT_URL>

Note that if the access key for the storage account contains a forward slash (`/`), it will have to be regenerated before it can be used in the connection URL.

azurestoragequeues://DefaultAzureCredential@<STORAGE_ACCOUNT_URL>
azurestoragequeues://ManagedIdentityCredential@<STORAGE_ACCOUNT_URL>

If you wish to use an Azure Managed Identity you may use the `DefaultAzureCredential` format of the connection string which will use `DefaultAzureCredential` class in the azure-identity package. You may want to read the azure-identity documentation for more information on how the `DefaultAzureCredential` works.

[https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python) .. _Azure Managed Identity: [https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#transport-options "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   `queue_name_prefix`

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#transport "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.azurestoragequeues.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azurestoragequeues.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport "Link to this definition")
Azure Storage Queues transport.

_class_ Channel(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel "Link to this definition")
Azure Storage Queues channel.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.basic_consume "Link to this definition")
Consume from queue.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.conninfo "Link to this definition")domain_format _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_ _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.domain_format "Link to this definition")entity_name(_name_, _table={33:45,34:45,35:45,36:45,37:45,38:45,39:45,40:45,41:45,42:45,43:45,44:45,45:45,46:45,47:45,58:45,59:45,60:45,61:45,62:45,63:45,64:45,91:45,92:45,93:45,94:45,95:45,96:45,123:45,124:45,125:45,126:45}_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.entity_name "Link to this definition")
Format AMQP queue name into a valid Azure Storage Queue name.

no_ack _:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")_ _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.no_ack "Link to this definition")_property_ queue_name_prefix _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.queue_name_prefix "Link to this definition")_property_ queue_service _:[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.queue_service "Link to this definition")_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.Channel.transport_options "Link to this definition")_classmethod_ as_uri(_uri:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _include\_password:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")=False_, _mask:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")='**'_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azurestoragequeues.html#Transport.as_uri)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.as_uri "Link to this definition")
Customise the display format of the URI.

can_parse_url _:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")_ _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.can_parse_url "Link to this definition")
Set to True if [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") should pass the URL unmodified.

default_port _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")_ _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.default_port "Link to this definition")
port number used when no port is specified.

_static_ parse_uri(_uri:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")][[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azurestoragequeues.html#Transport.parse_uri)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.parse_uri "Link to this definition")polling_interval _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_ _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#channel "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.azurestoragequeues.Channel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azurestoragequeues.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel "Link to this definition")
Azure Storage Queues channel.

basic_consume(_queue_, _no\_ack_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azurestoragequeues.html#Channel.basic_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.basic_consume "Link to this definition")
Consume from queue.

_property_ conninfo[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.conninfo "Link to this definition")domain_format _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_ _='kombu%(vhost)s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.domain_format "Link to this definition")entity_name(_name_, _table={33:45,34:45,35:45,36:45,37:45,38:45,39:45,40:45,41:45,42:45,43:45,44:45,45:45,46:45,47:45,58:45,59:45,60:45,61:45,62:45,63:45,64:45,91:45,92:45,93:45,94:45,95:45,96:45,123:45,124:45,125:45,126:45}_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/azurestoragequeues.html#Channel.entity_name)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.entity_name "Link to this definition")
Format AMQP queue name into a valid Azure Storage Queue name.

no_ack _:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")_ _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.no_ack "Link to this definition")_property_ queue_name_prefix _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.queue_name_prefix "Link to this definition")_property_ queue_service _:[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.queue_service "Link to this definition")_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.azurestoragequeues.html#kombu.transport.azurestoragequeues.Channel.transport_options "Link to this definition")
