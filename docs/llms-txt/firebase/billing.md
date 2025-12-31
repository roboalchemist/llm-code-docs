# Source: https://firebase.google.com/docs/database/usage/billing.md.txt

<br />

Firebase bills for the data you store in your database and all outbound network traffic at the session layer (layer 5) of the OSI model. Storage is billed at $5 for each GB/month, evaluated daily. Billing is not affected by the location of your database. Outbound traffic includes connection and encryption overhead from all database operations and data downloaded through database reads. Both database reads and writes can lead to connection costs on your bill. All traffic to and from your database, including operations denied by security rules, leads to billable costs.

Some common examples of billed traffic include:

- **Data downloaded:**When clients get data from your database, Firebase charges for the downloaded data. Typically, this makes up the bulk of your bandwidth costs, but it isn't the only factor in your bill.
- **Protocol overhead:**Some additional traffic between the server and clients is necessary to establish and maintain a session. Depending on the underlying protocol, this traffic might include: Firebase Realtime Database's realtime protocol overhead, WebSocket overhead, and HTTP header overhead. Each time a connection is established, this overhead, combined with any SSL encryption overhead, contributes to the connection costs. Although this isn't a lot of bandwidth for a single request, it can be a substantial part of your bill if your payloads are tiny or you make frequent, short connections.
- **SSL encryption overhead:** There is a cost associated with the SSL encryption overhead necessary for secure connections. On average, this cost is approximately 3.5KB for the initial handshake, and approximately tens of bytes for TLS record headers on each outgoing message. For most apps, this is a small percentage of your bill. However, this can become a large percentage if your specific case requires a lot of SSL handshakes. For example, devices that don't support[TLS session tickets](https://tools.ietf.org/html/rfc5077)might require large numbers of SSL connection handshakes.
- **Firebaseconsole data:** Although this isn't usually a significant portion ofRealtime Databasecosts, Firebase charges for data that you read and write from theFirebaseconsole.

| When your project is on the Blaze pricing plan,[**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)using the console. You can use the[Blaze plan calculator](https://firebase.google.com/pricing#blaze-calculator)to estimate your monthly costs.
|
| Be aware that**budget alerts do*not*cap your usage or charges** --- they are*alerts* about your costs so that you can take action, if needed. For example, you might consider[using budget notifications to programmatically disableCloud Billingon a project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

## Estimate your billed usage

To see your currentRealtime Databaseconnections and data usage, check the[Usage](https://console.firebase.google.com/project/_/database/usage/current-billing/)tab in theFirebaseconsole. You can check usage over the current billing period, the last 30 days, or the last 24 hours.

Firebase shows usage statistics for the following metrics:

- **Connections:**The number of simultaneous, currently open, realtime connections to your database. This includes the following realtime connections: WebSocket, long polling, and HTML server-sent events. It does not include RESTful requests.
- **Storage:**How much data is stored in your database. This doesn't include Firebase hosting or data stored through other Firebase products.
- **Downloads:**All bytes downloaded from your database, including protocol and encryption overhead.
- **Load:**This graph shows how much of your database is in use, processing requests, over a given 1-minute interval. You might see performance issues as your database approaches 100%.

## Optimize usage

There are a few best practices you can employ to optimize your database usage and bandwidth costs.

- **Use the native SDKs:**Whenever possible, use the SDKs that correspond to your app's platform, instead of the REST API. The SDKs maintain open connections, reducing the SSL encryption costs that typically add up with the REST API.
- **Check for bugs:** If your bandwidth costs are unexpectedly high, verify that your app isn't syncing more data or syncing more often than you originally intended. To pinpoint issues, use the[profiler tool](https://firebase.google.com/docs/database/usage/profile)to measure your read operations and turn on debug logging in the[Android](https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger),[Objective-C](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Enums/FIRLoggerLevel), and[Web](https://firebase.google.com/docs/reference/js/database#enablelogging)SDKs. Check background and sync processes in your app to make sure everything is working as you intended.
- **Reduce connections:** If possible, try to optimize your connection bandwidth. Frequent, small REST requests can be more costly than a single, continuous connection using the native SDK. If you do use the REST API, consider using an HTTP keep-alive or[server-sent events](https://firebase.google.com/docs/reference/rest/database#section-streaming), which can reduce costs from SSL handshakes.
- **Use TLS session tickets:** Reduce SSL encryption overhead costs on resumed connections by issuing[TLS session tickets](https://tools.ietf.org/html/rfc5077). This is particularly helpful if you do require frequent, secure connections to the database.
- **Index queries:** [Indexing your data](https://firebase.google.com/docs/database/security/indexing-data)reduces the total bandwidth you use for queries, which has the double benefit of lowering your costs and increasing your database's performance. Use the profiler tool to[find unindexed queries](https://firebase.google.com/docs/database/usage/profile#unindexed_queries)in your database.
- **Optimize your listeners:** Add queries to limit the data that your listen operations return and use listeners that only download updates to data --- for example,`on()`instead of`once()`. Additionally, place your listeners as far down the path as you can to limit the amount of data they sync.
- **Reduce storage costs:**Run periodic cleanup jobs and reduce any duplicate data in your database.
- **Use Rules:** Prevent any potentially costly, unauthorized operations on your database. For example, usingFirebase Realtime DatabaseSecurity Rulescould avoid a scenario where a malicious user repeatedly downloads your entire database. Learn more about[using Firebase Realtime Database Rules](https://firebase.google.com/docs/database/security).

| **Note about the profiler tool:** The profiler tool doesn't account for network traffic. It only records an estimate of the application data sent in responses. The profiler tool is intended to give you an overall picture of your database's performance, to help you monitor operations and troubleshoot issues,**not to estimate billing** . To learn more, see[the profiler tool documentation](https://firebase.google.com/docs/database/usage/profile).

The best optimization plan for your app depends on your particular use case. While this isn't an exhaustive list of best practices, you can find more advice and tips from the Firebase experts on our[Slack channel](https://firebase.community/)or on[Stack Overflow](https://stackoverflow.com/questions/tagged/firebase).