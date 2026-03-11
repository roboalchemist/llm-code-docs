# Source: https://docs.knock.app/api-reference/overview/bulk-endpoints.md

# Bulk endpoints

Knock exposes several endpoints that enqueue and return a `BulkOperation`. These endpoints perform their logic asynchronously, and you use the `BulkOperation` record to track progress.

In some cases, a bulk endpoint will accept a large set of entities to perform some action upon. In others, a bulk endpoint will accept a set of filter parameters and then execute an action across a large set of data on your account.

See the [Bulk operations section](/api-reference/bulk_operations) for more information on parsing and polling bulk operation statuses.
