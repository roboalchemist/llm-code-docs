# Source: https://docs.apify.com/api/v2/storage-key-value-stores.md

# Key-value stores - Introduction

This section describes API endpoints to manage Key-value stores. Key-value store is a simple storage for saving and reading data records or files. Each data record is represented by a unique key and associated with a MIME content type. Key-value stores are ideal for saving screenshots, Actor inputs and outputs, web pages, PDFs or to persist the state of crawlers.

For more information, see the [Key-value store documentation](https://docs.apify.com/platform/storage/key-value-store).

note

Some of the endpoints do not require the authentication token, the calls are authenticated using a hard-to-guess ID of the key-value store.

<!-- -->

## [Get list of key-value stores](https://docs.apify.com/api/v2/key-value-stores-get.md)

[/key-value-stores](https://docs.apify.com/api/v2/key-value-stores-get.md)

## [Create key-value store](https://docs.apify.com/api/v2/key-value-stores-post.md)

[/key-value-stores](https://docs.apify.com/api/v2/key-value-stores-post.md)

## [Get store](https://docs.apify.com/api/v2/key-value-store-get.md)

[/key-value-stores/{storeId}](https://docs.apify.com/api/v2/key-value-store-get.md)

## [Update store](https://docs.apify.com/api/v2/key-value-store-put.md)

[/key-value-stores/{storeId}](https://docs.apify.com/api/v2/key-value-store-put.md)

## [Delete store](https://docs.apify.com/api/v2/key-value-store-delete.md)

[/key-value-stores/{storeId}](https://docs.apify.com/api/v2/key-value-store-delete.md)

## [Get list of keys](https://docs.apify.com/api/v2/key-value-store-keys-get.md)

[/key-value-stores/{storeId}/keys](https://docs.apify.com/api/v2/key-value-store-keys-get.md)

## [Get record](https://docs.apify.com/api/v2/key-value-store-record-get.md)

[/key-value-stores/{storeId}/records/{recordKey}](https://docs.apify.com/api/v2/key-value-store-record-get.md)

## [Check if a record exists](https://docs.apify.com/api/v2/key-value-store-record-head.md)

[/key-value-stores/{storeId}/records/{recordKey}](https://docs.apify.com/api/v2/key-value-store-record-head.md)

## [Store record](https://docs.apify.com/api/v2/key-value-store-record-put.md)

[/key-value-stores/{storeId}/records/{recordKey}](https://docs.apify.com/api/v2/key-value-store-record-put.md)

## [Delete record](https://docs.apify.com/api/v2/key-value-store-record-delete.md)

[/key-value-stores/{storeId}/records/{recordKey}](https://docs.apify.com/api/v2/key-value-store-record-delete.md)
