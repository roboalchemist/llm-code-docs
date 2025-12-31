# Source: https://docs.apify.com/sdk/python/reference/class/CachedRequest.md

# CachedRequest<!-- -->

Pydantic model for cached request information.

Only internal structure.

## Index[**](#Index)

### Properties

* [**hydrated](https://docs.apify.com/sdk/python/sdk/python/reference/class/CachedRequest.md#hydrated)
* [**id](https://docs.apify.com/sdk/python/sdk/python/reference/class/CachedRequest.md#id)
* [**lock\_expires\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/CachedRequest.md#lock_expires_at)
* [**was\_already\_handled](https://docs.apify.com/sdk/python/sdk/python/reference/class/CachedRequest.md#was_already_handled)

## Properties<!-- -->[**](#Properties)

### [**](#hydrated)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_models.py#L103)hydrated

**hydrated: Request | None

The hydrated request object (the original one).

### [**](#id)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_models.py#L97)id

**id: str

Id of the request.

### [**](#lock_expires_at)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_models.py#L106)lock\_expires\_at

**lock\_expires\_at: datetime | None

The expiration time of the lock on the request.

### [**](#was_already_handled)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_models.py#L100)was\_already\_handled

**was\_already\_handled: bool

Whether the request was already handled.
