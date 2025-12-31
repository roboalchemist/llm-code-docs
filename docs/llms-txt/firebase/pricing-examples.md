# Source: https://firebase.google.com/docs/firestore/enterprise/pricing-examples.md.txt

<br />

<br />

|--------------------------------------------------------|
| *Relevant to Cloud Firestore Enterprise edition only.* |

<br />

This page includes examples of how billing units are calculated in some of the most common scenarios. Note that each query might differ in data processed based on factors such as the query plan, the shape of the data, and the indexes available.

We recommend using the[Query Explain](https://firebase.google.com/docs/firestore/enterprise/query-explain)feature to better understand the cost and performance of your specific queries.

## Read operations

Most read operations entail either performing a point read of a specific document or scanning a rage of data based on an identifier. Read operations consume read units. Read units are calculated in 4 KiB tranches. See the following examples.

### Point reads

Example billing for point reads:

- Point read of a single 1 KiB document. Consumes: 1 read unit
- Point read of a single 4 KiB document. Consumes: 1 read unit
- Point read of a single 1 MiB document. Consumes: 256 read units
- Point read of 100 documents, 1 KiB each. Consumes: 100 read units

### Scanning

The following examples include scenarios that scan documents or index entries.

#### Scanning Documents

- Query which scans 100 documents, 1 KiB each. Consumes: 25 read units

#### Scanning indexes

The scanning cost, in terms of bytes, is the same regardless of whether it is a document or index being scanned. However, index entries are often smaller in size. As a result, they can often provide a more cost effective way of scanning data.

- Query which scans 100 index entries, 1 KiB each. Consumes: 25 read units.
- Query which scans 100 index entries, 128 bytes each. Consumes: 4 read units.

### Minimum document or index entry size

In certain situations it may not be necessary to read the contents of a document or index entry to satisfy a query. This includes simple count queries like counting the total number of documents in a collection. In these situations, a minimum cost of 32 bytes applies per item scanned.

- Count the number of documents in a collection. The query scans 1000 items in the collection. Consumes: 8 read units.

### Combination of scanning and point reads

Many queries perform a combination of scanning and point reads to satisfy an operation.

- Query which scans 128 index entries, 256 bytes each and performs a point read of 128 documents, 4 KiB each. Consumes: 136 read units, comprised of:
  - 128 read units for point reads
  - 8 read units for index scans

### Query Explain

[Query Explain](https://firebase.google.com/docs/firestore/enterprise/query-explain)helps you understand how the database executes your queries. The details provided can help you optimize your queries.

The following costs apply when using Query Explain:

- Query Explain which executes the query: Query cost applies.
- Query Explain using plan only option. Consumes: 1 read unit (minimum cost of a query)

## Write operations

Write operations (creates, updates and deletes) are charged based on the size of the documents and indexes being created, modified, or deleted during the operation. Write operations consume write units. Write units are calculated in 1 KiB tranches.

Simple write operations, like update by document ID, only incur the cost of the writes. Write operations which require querying to satisfy the operation will additionally incur the read costs associated with the query.

See the following examples.

### Creates

- Create a new 10 KiB document with no indexes. Consumes: 10 write units
- Create a 1 KiB document with 1 index entry of 256 bytes on the collection. Consumes: 2 write units

### Updates

- Find a 10 KiB document by document ID and update with no indexes on the collection. Consumes: 10 write units
- Find a 1 KiB document by document ID and update 1 field with 1 index entry of 256 bytes. Consumes: 3 write units. Note: Updating an index entry in this situation consumes 2 write units -- one to delete and one to recreate the index entry.
- Find a 1 KiB document by document ID and update nothing (no changes). Consumes: 1 write units (the minimum write costs)
- Query all 1 KiB documents in a collection, which scans 1,000 documents, and insert a new 256 bytes field with no indexes on the collection: 1000 read units and 1000 writes units.

### Deletes

- Delete a 1 KiB document, which has 1 index on the collection. Consumes: 2 write units
- Delete a 1 KiB document, which has no indexes on the collection. Consumes: 1 write unit

## Index builds

Index builds charge for the index entries created or modified during the build operation. These costs are incurred anytime an index definition is added or removed. The index entries are billed identically to writes incurring 1 write unit per 1KiB.

- Create a new index for a collection containing 500 documents, index entries created are 1 KiB each. Consumes 500 write units.
- Delete an existing index for a collection containing 500 documents, index entries deleted are 1KiB each. Consumes 500 write units.