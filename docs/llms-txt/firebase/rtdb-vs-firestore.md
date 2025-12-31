# Source: https://firebase.google.com/docs/firestore/rtdb-vs-firestore.md.txt

# Source: https://firebase.google.com/docs/database/rtdb-vs-firestore.md.txt

<br />

Firebase offers two cloud-based, client-accessible document databases. We recommend new customers start withCloud Firestore:

- **Cloud Firestore** is the*recommended*enterprise-grade JSON-compatible document database, trusted by more than 600,000 developers. It's suitable for applications with rich data models requiring queryability, scalability, and high availability. It also offers low latency client synchronization and offline data access.

- **Realtime Database**is the classic Firebase JSON database. It's suitable for applications with simple data models requiring simple lookups and low-latency synchronization with limited scalability.

## What are some other important things to consider?

After thinking about the previous key considerations, you might be ready to[choose a database](https://firebase.google.com/docs/database/rtdb-vs-firestore#choose-a-database). If you're still weighing advantages and disadvantages, this section covers other differences betweenCloud FirestoreandRealtime Database.

### Data model

BothRealtime DatabaseandCloud Firestoreare NoSQL Databases.

| Cloud Firestore | **\[PREFERRED \]** |                                                                                                                     Realtime Database                                                                                                                      |
|-----------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stores data as collections of documents.** - Simple data is easy to store in documents, which are very similar to JSON. - Complex, hierarchical data is easier to organize at scale, using subcollections within documents. - Requires less denormalization and data flattening. Learn more about the[Cloud Firestoredata model](https://firebase.google.com/docs/firestore/data-model). || **Stores data as one large JSON tree.** - Simple data is very easy to store. - Complex, hierarchical data is harder to organize at scale. Learn more about the[Realtime Databasedata model](https://firebase.google.com/docs/database/web/structure-data). |

### Realtime and offline support

Both have mobile-first, realtime SDKs and both support local data storage for offline-ready apps.

| Cloud Firestore | **\[PREFERRED \]** |                 Realtime Database                  |
|-----------------|--------------------|----------------------------------------------------|
| **Offline support for Apple, Android, and web clients.** || **Offline support for Apple and Android clients.** |

### Presence

It can be useful to know when a client is online or offline. FirebaseRealtime Databasecan record client connection status and provide updates every time the client's connection state changes.

| Cloud Firestore | **\[PREFERRED \]** |    Realtime Database    |
|-----------------|--------------------|-------------------------|
| **Not supported natively.** You can build onRealtime Database's support for presence by syncingCloud FirestoreandRealtime DatabaseusingCloud FunctionsSee[Build presence inCloud Firestore](https://firebase.google.com/docs/firestore/solutions/presence). || **Presence supported.** |

### Querying

Retrieve, sort, and filter data from either database through queries.

| Cloud Firestore | **\[PREFERRED \]** |                                                                                                                                                                                                                                            Realtime Database                                                                                                                                                                                                                                            |
|-----------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Indexed queries with compound[sorting and filtering](https://firebase.google.com/docs/firestore/client/query-data).** - You can chain filters and combine filtering and sorting on a property in a single query. - Queries are shallow: they only return documents in a particular collection or collection group and don't return subcollection data. - Queries must always return whole documents. - Queries are indexed by default: Query performance is proportional to the size of your result set, not your dataset. || **Deep queries with limited[sorting and filtering features](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data).** - Queries can sort*or*filter on a property, but not both. - Queries are deep by default: they always return the entire subtree. - Queries can access data at any granularity, down to individual leaf-node values in the JSON tree. - Queries don't require an index; however the performance of certain queries degrades as your dataset grows. |

### Writes and transactions

| Cloud Firestore | **\[PREFERRED \]** |                                                                                                                                                     Realtime Database                                                                                                                                                     |
|-----------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Advanced write and transaction operations.** - [Write data operations](https://firebase.google.com/docs/firestore/manage-data/update-data)through set and update operations as well as advanced transformations such as array and numeric operators. - [Transactions](https://firebase.google.com/docs/firestore/manage-data/update-data#update_data_with_transactions)can atomically read and write data from any part of the database. || **Basic write and transaction operations.** - [Write data](https://firebase.google.com/docs/database/android/read-and-write#basic_write)through set and update operations. - [Transactions](https://firebase.google.com/docs/database/ios/read-and-write#save_data_as_transactions)are atomic on a specific data subtree. |

### Reliability and performance

| Cloud Firestore | **\[PREFERRED \]** |                                                                                                                                                                                                                                           Realtime Database                                                                                                                                                                                                                                            |
|-----------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cloud Firestoreis a[regional and multi-region](https://cloud.google.com/docs/geography-and-regions)solution that scales automatically.** - A low-latency solution, with typical response times no greater than 30 ms. - Houses your data across multiple data centers in distinct regions, ensuring global scalability and strong reliability. - Available in regional or multi-regional configurations around the world. Read more aboutCloud Firestoreperformance and reliability characteristics in the[Service Level Agreement](https://cloud.google.com/firestore/sla). || **Realtime Databaseis a[regional](https://cloud.google.com/docs/geography-and-regions)solution.** - Available in regional configurations. Databases are limited to zonal availability within a region. - Extremely low latency, with typical response times no greater than 10 ms. An ideal option for frequent state-syncing. Read more aboutRealtime Databaseperformance and reliability characteristics in the[Service Level Agreement](https://firebase.google.com/terms/service-level-agreement). |

### Uptime

| Cloud Firestore | **\[PREFERRED \]** |                          Realtime Database                           |
|-----------------|--------------------|----------------------------------------------------------------------|
| **Extremely high uptime performance.** - Typical uptime performance of 99.999%. - If availability is of the utmost importance, for example in ecommerce apps, useCloud Firestore. || **High uptime performance.** - Typical uptime performance of 99.95%. |

### Scalability

| Cloud Firestore | **\[PREFERRED \]** |                                                                                                                            Realtime Database                                                                                                                            |
|-----------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Scaling is automatic.** - Scales completely automatically. No limits on concurrent connections or overall database writes/second rate. - Has[limits](https://firebase.google.com/docs/firestore/quotas)on write rates to individual documents or indexes. || **Scaling requires sharding.** - Scale to around 200,000 concurrent connections and 1,000 writes/second in a single database. Scaling beyond that requires sharding your data across multiple databases. - No local limits on write rates to individual pieces of data. |

### Security

| Cloud Firestore | **\[PREFERRED \]** |                                                                                                                                                                                    Realtime Database                                                                                                                                                                                     |
|-----------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Non-cascading rules that combine authorization and validation.** - Reads and writes from mobile SDKs secured by[Cloud FirestoreSecurity Rules](https://firebase.google.com/docs/firestore/security/get-started). - Reads and writes from server SDKs secured by[Identity and Access Management (IAM)](https://cloud.google.com/firestore/docs/security/iam). - Rules don't cascade unless you use a wildcard. - Rules can constrain queries: If a query's results might contain data the user doesn't have access to, the entire query fails. || **Cascading rules language that separates authorization and validation.** - Reads and writes from mobile SDKs secured by[Realtime DatabaseSecurity Rules](https://firebase.google.com/docs/database/security). - Read and write rules cascade. - You[validate data](https://firebase.google.com/docs/database/security/securing-data#validating_data)separately using the`validate`rule. |

### Pricing

Both solutions are available on the[Spark and Blaze pricing plans](https://firebase.google.com/pricing).

| Cloud Firestore | **\[PREFERRED \]** |                                                                    Realtime Database                                                                    |
|-----------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charges primarily on**operations performed in your database (read, write, delete)** and, at a lower rate, bandwidth and storage. Cloud Firestoresupports monthly[budgets and alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)to avoid spending more than you are comfortable with. Read more about[Cloud Firestorepricing plans](https://firebase.google.com/docs/firestore/pricing). || Charges only for**bandwidth and storage** , but at a higher rate. Read more about[Realtime Databasepricing plans](https://firebase.google.com/pricing). |

## UsingCloud FirestoreandRealtime Database

You can use both databases within the same Firebase app or project. Both NoSQL databases can store the same types of data and the client libraries work in a similar manner. Keep in mind the differences outlined previously if you decide to[use both databases in your app](https://firebase.google.com/docs/firestore/firestore-for-rtdb).

Learn more about the features available in both[Realtime Database](https://firebase.google.com/docs/database)and[Cloud Firestore](https://firebase.google.com/docs/firestore).

## Ready to choose a database?

Hopefully this comparison has helped you settle on a Firebase database solution. Now you can learn how to add a database to your Firebase projects.

- For**Cloud Firestore** , take a look at[Get started with Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart).
- For**Realtime Database** , read the Get Started topic for your platform:[Apple](https://firebase.google.com/docs/database/ios/start),[Android](https://firebase.google.com/docs/database/android/start),[C++](https://firebase.google.com/docs/database/cpp/start),[Unity](https://firebase.google.com/docs/database/unity/start),[Web](https://firebase.google.com/docs/database/web/start), or[REST](https://firebase.google.com/docs/database/rest/start).