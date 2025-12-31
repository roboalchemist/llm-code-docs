# Source: https://firebase.google.com/docs/firestore/understand-reads-writes-scale.md.txt

# Source: https://firebase.google.com/docs/firestore/enterprise/understand-reads-writes-scale.md.txt

<br />

<br />

|--------------------------------------------------------|
| *Relevant to Cloud Firestore Enterprise edition only.* |

<br />

Read this document to make informed decisions on architecting your applications for high performance and reliability. This document includes advancedCloud Firestoretopics. If you're just starting out withCloud Firestore, see the[quickstart guide](https://firebase.google.com/docs/firestore/enterprise/create-and-query-database)instead. To make sure that your applications continue to perform well as your database size and traffic increase, it helps to understand the mechanics of reads and writes in the Firestore backend. You must also understand the interaction of your read and writes with the storage layer and the underlying constraints that may affect performance.

To learn about some best practices before architecting your application, read the following:

- Understand the[high level components](https://cloud.google.com/firestore/mongodb-compatibility/docs/understand-reads-writes-scale#understand_the_high_level_components)of an API request.
- All[writes](https://cloud.google.com/firestore/mongodb-compatibility/docs/understand-reads-writes-scale#understand_the_life_of_a_write)are handled as read-write transactions to ensure ACID properties. If a write involves multiple splits, it may require a two-phase commit process.
- [Reads](https://cloud.google.com/firestore/mongodb-compatibility/docs/understand-reads-writes-scale#understand_the_life_of_a_read), by default, are "strongly consistent" and use a timestamp-based approach to avoid locks.
- To maintain high performance, you should[avoid hotspots](https://cloud.google.com/firestore/mongodb-compatibility/docs/understand-reads-writes-scale#avoid_hotspots)by distributing operations across the key range and keeping transactions small.