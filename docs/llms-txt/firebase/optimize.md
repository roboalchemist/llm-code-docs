# Source: https://firebase.google.com/docs/database/usage/optimize.md.txt

<br />

There are a few different ways to improveFirebase Realtime Databaseperformance in your app. To find out what you can do to optimize yourRealtime Databaseperformance, gather data through the differentRealtime Databasemonitoring tools, then make changes to your app orRealtime Databaseuse accordingly.

## MonitorRealtime Databaseperformance

You can gather data about yourRealtime Database's performance through a few different tools, depending on the level of granularity you need:

- **High-level overview:** Use the[the profiler tool](https://firebase.google.com/docs/database/usage/profile)for a list of unindexed queries and a realtime overview of read/write operations.
- **Billed usage estimate:** Use the[usage metrics](https://firebase.google.com/docs/database/usage/billing#console-usage)available in the[Firebaseconsole](https://console.firebase.google.com/project/_/database/usage/current-billing/)to see your billed usage and high-level performance metrics.
- **Detailed drilldown:** Use[Cloud Monitoring](https://firebase.google.com/docs/database/usage/monitor-performance#stackdriver-monitoring)for a more granular look at how your database is performing over time.

| **Check for bugs:** Before you start implementing any changes to your app, verify that it's syncing data the way you originally intended. To pinpoint issues, turn on debug logging in the[Android](https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger),[Objective-C](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Enums/FIRLoggerLevel), and[Web](https://firebase.google.com/docs/reference/js/database#enablelogging)SDKs. Check background and sync processes in your app to make sure it's downloading data at the frequency and volume you intended.

## Improve performance by metric

Once you've gathered data, explore the following best practices and strategies based on the performance area you want to improve.

|                                                                                                                                                                                                                                                                                                                                                                                     Performance improvement strategies at-a-glance                                                                                                                                                                                                                                                                                                                                                                                     |||
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Metric**         | **Description**                                                                                                                                                  | **Best practices**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Load/Utilization   | Optimize how much of your database's capacity is in use processing requests at any given time (reflected in \*\*Load\*\* or \*\*io/database_load\*\* metrics).   | [Optimize your data structure](https://firebase.google.com/docs/database/usage/optimize#data-structure) [Shard data across databases](https://firebase.google.com/docs/database/usage/optimize#shard-data) [Improve listener efficiency](https://firebase.google.com/docs/database/usage/optimize#efficient-listeners) [Limit downloads with query-based rules](https://firebase.google.com/docs/database/usage/optimize#query-rules) [Optimize connections](https://firebase.google.com/docs/database/usage/optimize#open-connections)                                                                                          |
| Active connections | Balance the number of simultaneous, active connections to your database to stay under the 200,000-connection limit.                                              | [Shard data across databases](https://firebase.google.com/docs/database/usage/optimize#shard-data) [Reduce new connections](https://firebase.google.com/docs/database/usage/optimize#open-connections)                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Outgoing bandwidth | If the downloads from your database seem higher than you want them to be, you can improve the efficiency of your read operations and reduce encryption overhead. | [Optimize connections](https://firebase.google.com/docs/database/usage/optimize#open-connections) [Optimize your data structure](https://firebase.google.com/docs/database/usage/optimize#data-structure) [Limit downloads with query-based rules](https://firebase.google.com/docs/database/usage/optimize#query-rules) [Reuse SSL sessions](https://firebase.google.com/docs/database/usage/optimize#ssl-sessions) [Improve listener efficiency](https://firebase.google.com/docs/database/usage/optimize#efficient-listeners) [Restrict access to data](https://firebase.google.com/docs/database/usage/optimize#secure-data) |
| Storage            | Make sure you're not storing unused data, or balance your stored data across other databases and/or Firebase products to remain under quota.                     | [Clean up unused data](https://firebase.google.com/docs/database/usage/optimize#cleanup-storage) [Optimize your data structure](https://firebase.google.com/docs/database/usage/optimize#data-structure) [Shard data across databases](https://firebase.google.com/docs/database/usage/optimize#shard-data) [UseCloud Storage for Firebase](https://firebase.google.com/docs/storage)                                                                                                                                                                                                                                            |

## Optimize connections

RESTful requests like`GET`and`PUT`still require a connection, even though that connection is short-lived. These frequent, short-lived connections can actually add up to significantly more connection costs, database load, and outgoing bandwidth than realtime, active connections to your database.

Whenever possible, use the native SDKs for your app's platform, instead of the REST API. The SDKs maintain open connections, reducing the SSL encryption costs and database load that can add up with the REST API.

If you do use the REST API, consider using an HTTP keep-alive to maintain an open connection or use[server-sent events](https://firebase.google.com/docs/reference/rest/database#section-streaming), which can reduce costs from SSL handshakes.

## Shard data across multiple databases

Splitting your data across multipleRealtime Databaseinstances, otherwise known as database sharding, offers three benefits:

1. Increase the total simultaneous, active connections allowed on your app by splitting them across database instances.
2. Balance load across database instances.
3. If you have independent groups of users that only need access to discrete data sets, use different database instances for higher throughput and lower latency.

If you're on the[Blaze pricing plan](https://firebase.google.com/pricing), you can create multiple database instances within the same Firebase project, leveraging a common user authentication method across database instances.

Learn more about how and when to[shard data](https://firebase.google.com/docs/database/usage/sharding).

## Build efficient data structures

BecauseRealtime Databaseretrieves the data from a path's child nodes as well as the path, it makes sense to keep your data structure as flat as possible. This way, you can selectively retrieve the data you need, without also downloading unnecessary data to clients.

In particular, consider writes and deletes when you're structuring your data. For example, paths with thousands of leaves are potentially expensive to delete. Splitting them up into paths with multiple subtrees and fewer leaves per node can speed up deletes.

Additionally, each write can take up 0.1% of your total database utilization. Structure your data in a way that allows you to batch writes into a single operation as multi-path updates through either the`update()`methods in the SDKs or RESTful`PATCH`requests.

To optimize your data structure and improve performance, follow the[best practices for data structures](https://firebase.google.com/docs/database/ios/structure-data#best_practices_for_data_structure).

## Prevent unauthorized access

Prevent unauthorized operations on your database withRealtime DatabaseSecurity Rules. For example, using rules could avoid a scenario where a malicious user repeatedly downloads your entire database.

Learn more about[using Firebase Realtime Database Rules](https://firebase.google.com/docs/database/security).

## Use query-based rules to limit downloads

Realtime DatabaseSecurity Rulesrestrict access to data in your database, but they can also serve as limits on data returned through read operations. When you use query-based rules, as defined by`query.`expressions like`query.limitToFirst`, queries only retrieve the data bounded by the rule.

For example, the following rule limits read access to only the first 1000 results of a query, as ordered by priority:  

    messages: {
      ".read": "query.orderByKey &&
                query.limitToFirst <= 1000"
    }

    // Example query:
    db.ref("messages").limitToFirst(1000)
                      .orderByKey("value")

Learn more about[Realtime DatabaseSecurity Rules](https://firebase.google.com/docs/database/security).

## Index queries

[Indexing your data](https://firebase.google.com/docs/database/security/indexing-data)reduces the total bandwidth you use for each query your app runs.

## Reuse SSL sessions

Reduce SSL encryption overhead costs on resumed connections by issuing[TLS session tickets](https://tools.ietf.org/html/rfc5077). This is particularly helpful if you do require frequent, secure connections to the database.

## Improve listener efficiency

Place your listeners as far down the path as you can to limit the amount of data they sync. Your listeners should be close to the data you want them to get. Don't listen at the database root, as that results in downloads of your entire database.

Add queries to limit the data that your listen operations return and use listeners that only download updates to data --- for example,`on()`instead of`once()`. Reserve`.once()`for actions that truly don't require data updates. Additionally, sort your queries using`orderByKey()`, whenever possible, for the best performance. Sorting with`orderByChild()`can be 6-8 times slower, and sorting with`orderByValue()`can be very slow for large data sets, since it requires a read of the entire location from the persistence layer.

Make sure to also add listeners dynamically, and remove them when they're no longer necessary.

## Clean up unused data

Periodically remove any unused or duplicate data in your database. You can run[backups](https://firebase.google.com/docs/database/backups)to manually inspect your data or periodically back it up to aGoogle Cloud Storagebucket. Also consider hosting stored data through[Cloud Storage for Firebase](https://firebase.google.com/docs/storage).

## Ship scalable code you can update

Apps built into IoT devices should include scalable code that you can update easily. Make sure to test use cases thoroughly, account for scenarios where you might grow your userbase exponentially, and build in the ability to deploy updates to your code. Carefully consider major changes you might need to make down the line, if, for example, you decide to shard your data.