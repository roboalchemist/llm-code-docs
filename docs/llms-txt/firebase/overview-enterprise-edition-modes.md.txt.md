# Source: https://firebase.google.com/docs/firestore/enterprise/overview-enterprise-edition-modes.md.txt

<br />

The Firestore Enterprise edition features an advanced query engine to support a
broad set of query capabilities. With this, there's a distinct query execution
difference in this edition, making indexes optional. Therefore, single field
indexes are no longer automatically created. While this allows queries to
execute without upfront index configurations, unindexed queries will default to
scanning the entire collection. Developers are empowered to create indexes where
appropriate, to improve latency and costs as the dataset grows.

In addition to the features listed under the Firestore Standard edition, the
Enterprise edition supports the following modes of operation that
you select when creating a database:

- **Firestore in Native mode with Core and Pipeline operations (Preview):** This mode integrates two distinct operations: Core and Pipelines. The Firestore Core operations provide the standard document Create, Read, Update, and Delete (CRUD) functionality, along with built-in support for real-time listen queries and offline persistence. Firestore Pipeline operations employ a flexible query syntax enabling advanced data retrieval operations for applications. For more information on these features, see [Firestore Native
  Mode overview](https://firebase.google.com/docs/firestore/enterprise/pipelines-overview).
- **Firestore with MongoDB compatibility:** This mode enables developers to use existing MongoDB application code, drivers, tools, and the open-source ecosystem of MongoDB integrations with Cloud Firestore. It supports the MongoDB Query Language (MQL) and BSON data types, effectively acting as a drop-in replacement for MongoDB workloads while providing the benefits of Firestore's automatic scaling and high availability. For more information on these features, see [MongoDB compatibility
  overview](https://firebase.google.com/docs/firestore/enterprise/mongodb-compatibility-overview).