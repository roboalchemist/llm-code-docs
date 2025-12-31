# Source: https://firebase.google.com/docs/firestore/transaction-data-contention.md.txt

<br />

This page describes transactional data contention, serializability, and isolation. For transaction code samples, see[transactions and batched writes](https://firebase.google.com/docs/firestore/manage-data/transactions)instead.

## Transactions and data contention

For a transaction to succeed, the documents retrieved by its read operations must remain unmodified by operations outside the transaction. If another operation attempts to change one of those documents, that operations enters a state of data contention with the transaction.

Data contention
:   When two or more operations compete to control the same document. For example, one transaction might require a document to remain consistent while a concurrent operation tries to update that document's field values.

Cloud Firestoreresolves data contention by delaying or failing one of the operations. TheCloud Firestoreclient libraries automatically retry transactions that fail due to data contention. After a finite number of retries, the transaction operation fails and returns an error message:  

    ABORTED: Too much contention on these documents. Please try again.

When deciding which operation to fail or delay, behavior depends the type of client library.

Cloud Firestorecan be configured with a concurrency mode:`PESSIMISTIC`or`OPTIMISTIC`. The default for**standard** edition is`PESSIMISTIC`while enterprise edition is`OPTIMISTIC`. (`PESSIMISTIC`) is recommended. The mobile and web SDKs behave independently of this setting as they always emulate optimistic concurrency.

- The mobile/web SDKs use optimistic concurrency controls.

- The server client libraries use pessimistic concurrency controls.

| **Key Term:** In database systems,*concurrency controls*describe how the system resolves data contention between concurrent operations. Systems can implement optimistic or pessimistic concurrency controls.

### Data contention in the mobile/web SDKs

Mobile and web SDKs emulate optimistic concurrency transactions using write preconditions on document versions. This emulation occurs regardless of the database's concurrency mode setting. The mobile and web SDKs do not use the[built-in transactions](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents/commit)feature, so even if the database concurrency mode is configured for`PESSIMISTIC`, mobile clients still behave optimistically.

Optimistic concurrency controls
:   Based on the assumption that data contention is not likely or that it's not efficient to hold database locks. Optimistic transactions do not use database locks to block other operations from changing data.

Mobile/web SDKs use optimistic concurrency controls, because they can operate in environments with high latency and an unreliable network connection. Locking documents in a high latency environment would cause too many data contention failures.

In the Mobile/Web SDKs, a transaction keeps track of all the documents you read inside the transaction. The transaction completes its write operations**only if**none of those documents changed during the transaction's execution. If any document did change, the transaction handler retries the transaction. If the transaction can't get a clean result after a few retries, the transaction fails due to data contention.

### Data contention in the server client libraries

Server client libraries (C#, Go, Java, Node.js, PHP, Python, Ruby) use the[built-in transactions](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents/commit)feature which by default implements pessimistic concurrency controls. These transactions respect the database-level concurrency mode setting (usually`PESSIMISTIC`) and use document locks to prevent conflicting writes.

Pessimistic concurrency controls
:   Based on the assumption that data contention is likely. Pessimistic transactions use database locks to prevent other operations from modifying data.

Server client libraries use pessimistic concurrency controls, because they assume low latency and a reliable connection to the database.
| **Note:** To best ensure low latency, use server client libraries from a[Google Cloudcompute product as close to yourCloud Firestoredatabase as possible](https://cloud.google.com/about/locations#products-available-by-location). A server client library with a high latency connection can run into issues with locking and data contention.

In the server client libraries, transactions place locks on the documents they read. A transaction's lock on a document blocks other transactions, batched writes, and non-transactional writes from changing that document. A transaction releases its document locks at commit time. It also releases its locks if it times out or fails for any reason.

When a transaction locks a document, other write operations must wait for the transaction to release its lock. Transactions acquire their locks in chronological order.

## Serializable isolation

Data contention between transactions is closely related to database isolation levels. A database's*isolation level*describes how well the system handles conflicts between concurrent operations. Conflict comes from the following database requirements:

- Transactions require accurate, consistent data.
- To efficiently use resources, databases execute operations concurrently.

In systems with a low isolation level, a read operation within a transaction might read inaccurate data from uncommitted changes in a concurrent operation.

*Serializable isolation*defines the highest isolation level. Serializable isolation means that:

- You can assume that the database executes transactions in series.
- Transactions are not affected by uncommitted changes in concurrent operations.

This guarantee must hold even while the database executes multiple transactions in parallel. The database must implement concurrency controls to resolve conflicts that would break this guarantee.

Cloud Firestoreguarantees serializable isolation of transactions. Transactions inCloud Firestoreare serialized and isolated by commit time.

### Serializable isolation by commit time

Cloud Firestoreassigns each transaction a commit time which represents a single point in time. WhenCloud Firestorecommits a transaction's changes to the database, you can assume all reads and writes within the transaction take place exactly at the commit time.

Actual execution of a transaction requires some span of time. The execution of a transaction begins before the commit time, and the execution of multiple operations may overlap.Cloud Firestoreupholds serializable isolation and guarantees that:

- Cloud Firestorecommits transactions in order by commit time.
- Cloud Firestoreisolates transactions from concurrent operations with a later commit time.

In the case of data contention between concurrent operations,[Cloud Firestoreuses optimistic and pessimistic concurrency controls to resolve contention.](https://firebase.google.com/docs/firestore/transaction-data-contention#concurrency-controls)

### Isolation within a transaction

Transaction isolation also applies to write operations within a transaction. Queries and reads inside a transaction do not see the results of previous writes inside that transaction. Even if you modify or delete a document within a transaction, all document reads in that transaction return the version of the document at commit time, before the transaction's write operations. Read operations return nothing if the document did not exist then.
| **Note:** Document reads must come before document writes.

### Issues with data contention

For more information on data contention and how to resolve them check out the[troubleshooting page](https://cloud.google.com/firestore/docs/troubleshooting).