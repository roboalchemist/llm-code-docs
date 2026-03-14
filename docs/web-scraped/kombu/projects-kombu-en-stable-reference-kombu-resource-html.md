# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html

Title: kombu.resource — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html

Published Time: Mon, 29 Dec 2025 20:31:32 GMT

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.resource.html).

Resource Management - `kombu.resource`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#resource-management-kombu-resource "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Generic resource pool implementation.

_class_ kombu.resource.Resource(_limit=None_, _preload=None_, _close\_after\_fork=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource "Link to this definition")
Pool of resources.

_exception_ LimitExceeded[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.LimitExceeded "Link to this definition")
Limit exceeded.

acquire(_block=False_, _timeout=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.acquire)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.acquire "Link to this definition")
Acquire resource.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#arguments "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

> block (bool): If the limit is exceeded,
> then block until there is an available item.
> 
> timeout (float): Timeout to wait
> if `block` is true. Default is `None` (forever).

raises LimitExceeded:
if block is false and the limit has been exceeded.:

close_after_fork _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.close_after_fork "Link to this definition")close_resource(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.close_resource)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.close_resource "Link to this definition")collect_resource(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.collect_resource)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.collect_resource "Link to this definition")force_close_all(_close\_pool=True_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.force_close_all)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.force_close_all "Link to this definition")
Close and remove all resources in the pool (also those in use).

Used to close resources from parent processes after fork (e.g. sockets/connections).

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#id1 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

> close_pool (bool): If True (default) then the pool is marked
> as closed. In case of False the pool can be reused.

_property_ limit[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.limit "Link to this definition")prepare(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.prepare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.prepare "Link to this definition")release(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.release)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.release "Link to this definition")release_resource(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.release_resource)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.release_resource "Link to this definition")replace(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.replace)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.replace "Link to this definition")
Replace existing resource with a new instance.

This can be used in case of defective resources.

resize(_limit_, _force=False_, _ignore\_errors=False_, _reset=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.resize)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.resize "Link to this definition")setup()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/resource.html#Resource.setup)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.resource.html#kombu.resource.Resource.setup "Link to this definition")
