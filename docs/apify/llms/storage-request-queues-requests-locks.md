# Source: https://docs.apify.com/api/v2/storage-request-queues-requests-locks.md

# Requests locks - Introduction

This section describes API endpoints to create, manage, and delete request locks within request queues.

Request queue is a storage for a queue of HTTP URLs to crawl, which is typically used for deep crawling of websites where you start with several URLs and then recursively follow links to other pages. The storage supports both breadth-first and depth-first crawling orders.

For more information, see the [Request queue documentation](https://docs.apify.com/platform/storage/request-queue).

note

Some of the endpoints do not require the authentication token, the calls are authenticated using the hard-to-guess ID of the queue.

<!-- -->

## [Unlock requests](https://docs.apify.com/api/v2/request-queue-requests-unlock-post.md)

[/request-queues/{queueId}/requests/unlock](https://docs.apify.com/api/v2/request-queue-requests-unlock-post.md)

## [Get head](https://docs.apify.com/api/v2/request-queue-head-get.md)

[/request-queues/{queueId}/head](https://docs.apify.com/api/v2/request-queue-head-get.md)

## [Get head and lock](https://docs.apify.com/api/v2/request-queue-head-lock-post.md)

[/request-queues/{queueId}/head/lock](https://docs.apify.com/api/v2/request-queue-head-lock-post.md)

## [Prolong request lock](https://docs.apify.com/api/v2/request-queue-request-lock-put.md)

[/request-queues/{queueId}/requests/{requestId}/lock](https://docs.apify.com/api/v2/request-queue-request-lock-put.md)

## [Delete request lock](https://docs.apify.com/api/v2/request-queue-request-lock-delete.md)

[/request-queues/{queueId}/requests/{requestId}/lock](https://docs.apify.com/api/v2/request-queue-request-lock-delete.md)
