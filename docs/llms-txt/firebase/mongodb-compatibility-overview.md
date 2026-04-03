# Source: https://firebase.google.com/docs/firestore/enterprise/mongodb-compatibility-overview.md.txt

<br />

<br />

|--------------------------------------------------------|
| *Relevant to Cloud Firestore Enterprise edition only.* |

<br />

Cloud Firestore with MongoDB compatibility enables developers to use existing MongoDB application code, drivers, tools, and the open-source ecosystem of MongoDB integrations withCloud Firestore.

Cloud Firestoreoffers a differentiated serverless document database service, featuring multi-region replication with strong consistency, virtually unlimited scalability, industry-leading high availability of up to 99.999% SLA, and single-digit milliseconds read performance.

Cloud Firestore with MongoDB compatibility is available as part of the[Enterprise edition](https://firebase.google.com/docs/firestore/editions).

## Key Capabilities

Cloud Firestore with MongoDB compatibility offers a number of key capabilities:

|              **Differentiator**              |                                                                                                                                             **Description**                                                                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MongoDB compatibility**                    | Cloud Firestoreprovides a MongoDB compatible API allowing you to useCloud Firestoreas the database for your existing MongoDB applications.                                                                                                                                                              |
| **Serverless**                               | Cloud Firestoreuses a pay-per-use model.Cloud Firestoredoes not require any pre-provisioning of resources and auto scales to match your load.                                                                                                                                                           |
| **Virtually unlimited scale**                | Cloud Firestoreseamlessly scales compute and storage on-demand without the need to configure capacity, sharding or provision storage \& I/O.                                                                                                                                                            |
| **Industry-leading High Availability**       | AllCloud Firestoredatabases offer high availability, with 99.99% availability for regional and 99.999% availability for multi-regional deployments. Cloud Firestorehas automatic multi-region data replication, strongly-consistent queries, atomic batch operations, and transaction support.          |
| **Single digit milliseconds read latency**   | Cloud Firestoreoffers single digit millisecond read latency.                                                                                                                                                                                                                                            |
| **Enterprise-grade security and monitoring** | SecureCloud Firestorewith centralizedGoogle Cloudgovernance. Achieve enhanced visibility and simplified management of yourCloud Firestoredatabase fleet with our integrated Database Center. Benefit from a unified fleet view and simplified management through centralized control and AI assistance. |

## How does it work?

Cloud Firestoreis a cloud-first, NoSQL document database offering MongoDB compatibility.

Following the Cloud Firestore with MongoDB compatibility data model, you store data in documents that contain fields mapping to values. These documents are stored in collections, which are containers for your documents that you can use to organize your data and build queries. Documents support many different[data types](https://firebase.google.com/docs/firestore/enterprise/supported-data-types-drivers), from strings and numbers, to complex, embedded objects.

Additionally, querying inCloud Firestoreis expressive, efficient, and flexible. You can use standard MongoDB driver or the MongoDB Query Language (MQL). You can create shallow queries to retrieve data at the document level without needing to retrieve the entire collection, and add sorting, filtering, and limits to your queries or cursors to paginate your results.

Finally, Cloud Firestore with MongoDB compatibility is fully integrated withGoogle Cloudgovernance services as described in[identity and access management](https://firebase.google.com/docs/firestore/enterprise/security/iam).

## What's next

- [Get started with Cloud Firestore with MongoDB compatibility](https://firebase.google.com/docs/firestore/enterprise/create-and-query-database)