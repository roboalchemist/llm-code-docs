# Source: https://firebase.google.com/docs/firestore/standard-edition.md.txt

<br />

The Firestore Core operations in the Standard edition provide a broad
suite of capabilities as a document database, including fluent SDKs for a large
number of programming languages, real-time and offline support, high
availability in single and multi-region configurations, and a convenient
serverless operation model with seamless autoscaling.

## Key features

The Standard edition represents the Firestore experience, optimized
for rapid application development using Core operations.

- **Data Model:** Cloud Firestore utilizes a flexible, NoSQL hierarchical data structure where data is stored in documents organized into collections and subcollections.
- **Real-time and Offline:** These operations include built-in support for real-time listen queries that update client apps instantly when data changes, as well as robust offline persistence for mobile and web clients.
- **Querying:** Core operations support expressive and efficient queries, allowing for chained filters and sorting. A key characteristic is that query performance is proportional to the size of the result set, not the total size of the dataset.

### Indexing

In the Standard edition, indexing is strictly enforced with the use
of Core operations.

- **Mandatory Indexing:** All queries must be backed by an index. If a Core operation attempts to run a query without an appropriate index, it will fail rather than perform a collection scan.
- **Automatic Indexes:** To simplify development, Firestore automatically creates single-field indexes for all fields in a document.
- **Manual Composite Indexes:** For complex Core operations involving multiple fields, developers must manually create composite indexes. An example of this is a query filtering on one field and sorting by another. The client SDK facilitates this by providing an error link that directs the developer to the Firebase console to create the specific missing index.

### Billing and Limits

The [billing model](https://cloud.google.com/firestore/pricing) for
Core operations in the Standard edition is based on the
count of documents or indexes processed rather than the size of the data
processed (with the exception of storage). The following prices are shown in
`us-central1`.

- Document-Based Charges: You are charged for the number of documents read,
  written, and deleted.

  - Reads: $0.03 per 100k reads or $0.30 per million reads, charged per document.
  - Writes: $0.09 per 100k writes or $0.90 per million writes, charged per document.
  - Deletes: $0.01 per 100k deletes or $0.10 per million deletes.
- Index Write Costs: Unlike the Enterprise edition, there is no specific
  charge for writing index entries; index updates are included in the cost of
  the document write. However, you are charged for the storage space these
  indexes consume.

- Real-time listen queries: Real-time updates are billed as standard document
  reads. You are charged one read each time a document is added or updated in
  the listener's result set.

- Index Entry Reads: While most Core operations are billed by
  document count, specific complex operations---such as aggregation queries
  (count, sum, avg) or vector search---charge for the number of index entries
  read.

- Free Quota: The Standard edition includes a daily free tier of
  50,000 reads,
  20,000 writes, and 20,000 deletes.