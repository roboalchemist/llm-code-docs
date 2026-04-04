# Source: https://firebase.google.com/docs/firestore/enterprise/quotas.md.txt

This page describes the request quotas and limits for Cloud Firestore.

## Free tier usage

Cloud Firestore offers a free tier that lets you get started with
Cloud Firestore at no cost. The free tier amounts are listed in the following
table.

Free tier amounts are applied daily and reset at midnight Pacific time.

The free tier applies to only one Cloud Firestore database per project.
The first database that is created in a project without a free tier database
will get the free tier. If the database with the free tier applied is deleted,
the next database created will receive the free tier.

<br />

| Free tier | Quota |
|---|---|
| Stored data | 1 GiB |
| Read units | 50,000 per day |
| Write units | 40,000 per day |
| Outbound data transfer | 10 GiB per month |

<br />

The following operations and features don't include free usage.
You must [enable billing](https://cloud.google.com/billing/docs/how-to/modify-project) to use these features:

- Managed deletes (TTL)
- Backup data
- Restore operations

For more information about how these features are billed, see
[Storage pricing](https://cloud.google.com/firestore/enterprise/pricing#storage-size#storage-size).

## Standard limits

The following tables show the limits that apply to
Cloud Firestore. These are hard limits unless otherwise noted.

### Databases

| Limit | Details |
|---|---|
| Maximum number of databases per project | 100 [Contact support](https://cloud.google.com/support-hub) to request an increase to this limit. |
| Maximum number of [customer-managed encryption keys (CMEK) databases](https://firebase.google.com/docs/firestore/enterprise/cmek) per project | 0 By default the quota is 0 because this feature is behind an allowlist. You can request to increase the quota by filling in [the CMEK access request form](https://docs.google.com/forms/d/e/1FAIpQLSfKs8wJf4IXu1NizvfyU2vT59JDbdPvkehMVZ2ab5l_aDLIIA/viewform?resourcekey=0-O15dlRFvA0JIDmh6VFUEcA). |

### Collections, documents, and fields

| Limit | Details |
|---|---|
| Constraints on collection names | - Must be valid UTF-8 characters - Must be no longer than 1,500 bytes - Can't match the regular expression `__.*__` - Can't contain `$` - Can't be the empty string (`""`) - Can't contain the null character - Can't begin with \`system.\` and can't contain \`.system.\`. |
| Constraints on document IDs (`_id`) | - Must be an ObjectId, String, 64-bit integer, 32-bit integer, Double, Binary, or Object. Other BSON types are not supported. - Must be no larger than 1,500 bytes - For Object-typed IDs: - Each value within an Object-typed ID must also be of a supported ID type (ObjectId, String, 64-bit integer, 32-bit integer, Double, Binary, or Object) or an Array of values, each of which is of a supported ID type. - For String-typed IDs: - Must be valid UTF-8 characters - Can't match the regular expression `__.*__` |
| Maximum size for a document | 4 MiB |
| Constraints on field names | - Must be valid UTF-8 characters - Can't be the empty string (`""`) - Can't match the regular expression `__.*__` |
| Maximum size of a field name | 1,500 bytes |
| Maximum size of a field path | 1,500 bytes |
| Maximum size of a field value | 4 MiB - 89 bytes |
| Maximum depth of fields in a map or array | 20 Map and array fields add one level to the overall depth of an object. For example, the following object has a total depth of three levels: ``` { nested_object: {      #depth 1 nested_array: [     #depth 2 { foo: "bar"      #depth 3 } ] } } ``` |

### Reads, writes, and transactions

| Limit | Details |
|---|---|
| Memory limit for a query | 128 MiB |
| Time limit for a transaction | 270 seconds, with a 60-second idle expiration time |

### Indexes

| Limit | Details |
|---|---|
| Maximum number of indexes for a database | 1000 [Contact support](https://cloud.google.com/support-hub) to request an increase to this limit. |
| Maximum number of index entries for each document | 40,000 |
| Maximum number of fields in an index | 100 |
| Maximum size of an index entry | 7.5 KiB |
| Maximum sum of the sizes of a document's index entries | 8 MiB |

### Time to live (TTL)

| Limit | Details |
|---|---|
| Maximum number of TTL configurations for a database | 500 |

### Saved queries limits

> [!WARNING]
>
> **Preview
> --- Saved queries**
>
>
> This feature is
>
> subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the
> [Service Specific
> Terms](https://firebase.google.com/terms/service-terms#1).
>
> Pre-GA features are available "as is" and might have limited support.
>
> For more information, see the
> [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages).

| Value | Limit |
|---|---|
| Maximum number of saved queries per project (including saved queries for other Google Cloud products) | 10,000 |
| Maximum size for each query | 1 MiB |