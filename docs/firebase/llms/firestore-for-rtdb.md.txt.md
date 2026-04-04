# Source: https://firebase.google.com/docs/firestore/firestore-for-rtdb.md.txt

You can use both Firebase Realtime Database and Cloud Firestore in your app, and
leverage each database solution's benefits to fit your needs. For example, you
might want to leverage Realtime Database's support for presence, as outlined in
[Build Presence in Cloud Firestore](https://firebase.google.com/docs/firestore/solutions/presence).

Learn more about
the [differences between the databases](https://firebase.google.com/docs/firestore/rtdb-vs-firestore).

## Moving data to Cloud Firestore

If you've decided you want to migrate some of your data from Realtime Database to
Cloud Firestore, consider the following flow. Because every database has
unique needs and structural considerations, there isn't an
automated migration path. Instead, you can follow this general progression:

1. **Map the data structure and security rules from Realtime Database to
   Cloud Firestore.**
   Both Realtime Database and Cloud Firestore rely on Firebase Authentication,
   so you don't need to change user authentication for your app. However, the
   security rules and data model are different and it's important to carefully
   account for those divergences before you start moving data to Cloud
   Firestore.

2. **Move historical data.**
   As you're setting up your new data structure in Cloud Firestore, you can
   map and move existing data from Realtime Database to your new Cloud Firestore
   instance. However, if you're using both databases in your app,
   you don't need to move historical data out of Realtime Database.

3. **Mirror new data to Firestore in realtime.**
   Use Cloud Functions to write new data to your new Cloud Firestore
   database as it gets added to Realtime Database.

4. **Make Cloud Firestore your primary database for the migrated data.**
   Once you've migrated some of your data, use Cloud Firestore
   as your primary database and reduce your Realtime Database use for the migrated
   data. Consider versions of your app that are still tied to
   Realtime Database for that data and how you plan to continue supporting them.

Make sure you account for [billing costs](https://firebase.google.com/pricing#blaze-calculator)
for both [Realtime Database](https://firebase.google.com/docs/database/usage/billing)
and [Cloud Firestore](https://firebase.google.com/docs/firestore/pricing).

## Map your data

Data in Realtime Database is structured as a single tree, while Cloud Firestore
supports more explicit data hierarchies through documents, collections, and
subcollections. If you move some of your data from Realtime Database to
Cloud Firestore, you might want to consider a different architecture
for your data.

### Major differences to consider

If you move data from your existing Realtime Database tree to Cloud Firestore
documents and collections, keep in mind the following major differences between
the databases that might impact how you structure data in Cloud Firestore:

- Shallow queries offer more flexibility in hierarchical data structures.
- Complex queries offer more granularity and reduce the need for duplicate data.
- Query cursors offer more robust pagination.
- Transactions no longer require a common root for all your data, and are more efficient.
- Billing costs differ between Realtime Database and Cloud Firestore. In many cases, Cloud Firestore might be more expensive than Realtime Database, particularly if you rely on many small operations. Consider reducing the number of operations on your database and avoiding unnecessary writes. Learn more about the differences in [billing](https://firebase.google.com/docs/firestore/rtdb-vs-firestore#pricing) between Realtime Database and Cloud Firestore.

### Best practices in action

The following example reflects some of the considerations you might make as you
shift your data between databases. You can leverage shallow reads and improved
querying capabilities for more natural data structures than you may have used
with Realtime Database.

Consider a city guide app that helps users find notable landmarks in cities
around the world. Since Realtime Database lacks shallow reads, you might have had to
structure the data in two top-level nodes, as follows:

    // /cities/$CITY_KEY
    {
      name: "New York",
      population: 8000000,
      capital: False
    }

    // /city-landmark/$CITY_KEY/$LANDMARK_KEY
    {
      name: "Empire State Building",
      category: "Architecture"
    }

Cloud Firestore has shallow reads, so querying for documents in a collection
doesn't pull in data from subcollections. Consequently, you can store landmark
information in a subcollection:

    // /cities/$CITY_ID
    {
      name: "New York",
      population: 8000000,
      capital: False,
      landmarks: [... subcollection ...]
    }

Documents have a maximum size of 1MB, which is another reason to store
landmarks as a subcollection, keeping each city document small, rather than
bloating documents with nested lists.

Cloud Firestore's advanced querying capabilities reduce the need to
duplicate data for common access patterns. For example, consider a screen in
the city guide app that shows all of the capital cities ordered by population.
In Realtime Database, the most efficient way to do this is to maintain a separate
list of capital cities that duplicates data from the `cities` list, as follows:

    {
       cities: {
        // ...
       },

       capital-cities: {
         // ...
       }
    }

In Cloud Firestore, you can express a list of capital cities in order of
population as a single query:

    db.collection('cities')
        .where('capital', '==', true)
        .orderBy('population')

Read more about the [Cloud Firestore data model](https://firebase.google.com/docs/firestore/data-model) and take a
look at our [Solutions](https://firebase.google.com/docs/firestore/solutions) for more ideas on how to structure your
Cloud Firestore database.

## Secure your data

Whether you're using [Cloud Firestore Security Rules](https://firebase.google.com/docs/firestore/security/get-started) for
Android, Apple, or Web clients, or [Identity Access Management (IAM)](https://firebase.google.com/docs/firestore/security/iam)
for servers, make sure you're securing your data in Cloud Firestore as well
as Realtime Database. User authentication is handled by Authentication for both databases,
so you don't need to change your implementation of Authentication when you start
using Cloud Firestore.

### Major differences to consider

- Mobile and web SDKs use Cloud Firestore Security Rules, while server SDKs use Identity Access Management (IAM) to secure data.
- Cloud Firestore Security Rules don't cascade unless you use a wildcard. Documents and collections don't otherwise inherit rules.
- You no longer need to validate data separately (as you did in [Realtime Database](https://firebase.google.com/docs/database/security/rules-conditions#validaterules)).
- Cloud Firestore checks rules before executing a query to make sure that the user has the appropriate access for all data returned by the query.

## Move historical data to Cloud Firestore

Once you've mapped your data and security structures to Cloud Firestore's
data and security models, you can start adding your data.
If you plan to query historical data after you move your app from Realtime Database
to Cloud Firestore, add an export of your old data to your new
Cloud Firestore database. If you plan to use both Realtime Database and
Cloud Firestore in your app, you can skip this step.

To avoid overwriting new data with old data, you might want to add your
historical data first. If you add new data to both databases simultaneously, as
discussed in the next step, make sure you give precedence to new data added to
Cloud Firestore by Cloud Functions.

To migrate historical data to Cloud Firestore, follow these steps:

1. Export your data from Realtime Database or [use a recent backup](https://firebase.google.com/docs/database/backups).
   1. Go to the [Realtime Database section](https://console.firebase.google.com/project/_/database/) in the Firebase console.
   2. From the **Data** tab, select your database's root-level node and select **Export JSON** from the menu.
2. Create your new database in Cloud Firestore and
   [add your data](https://firebase.google.com/docs/firestore/manage-data/add-data).

   Consider the following strategies as you move some of your data to Cloud Firestore:
   - Write a custom script that ports your data for you. While we can't offer a template for this script, because every database will have unique needs, Cloud Firestore experts on our [Slack channel](https://firebase.community/) or on [Stack Overflow](https://stackoverflow.com/questions/tagged/firebase) can review your script or offer advice for your specific situation.
   - Use the server SDKs (Node.js, Java, Python, or Go) to write data directly to Cloud Firestore. For instructions on setting up the server SDKs, see [Get Started](https://firebase.google.com/docs/firestore/quickstart).
   - To expedite large data migrations, use [batched writes](https://firebase.google.com/docs/firestore/manage-data/transactions#batched-writes) and send up to 500 operations in a single network request.
   - To stay under [Cloud Firestore rate limits](https://firebase.google.com/docs/firestore/quotas#limits), limit operations to 500 writes/second for each collection.

## Add new data to Cloud Firestore

To maintain parity between your databases, add new data to both databases in
realtime. Use Cloud Functions to trigger a write to Cloud Firestore
whenever a client writes to Realtime Database. Make sure that Cloud Firestore
gives precedence to new data coming from Cloud Functions over any writes
you're making from your historical data migration.

Create a function to write new or changing data to Cloud Firestore
every time a client writes data to Realtime Database. Learn more about
[Realtime Database triggers](https://firebase.google.com/docs/functions/database-events) for Cloud Functions.

## Make Cloud Firestore your primary database for the migrated data

If you've decided to use Cloud Firestore as your primary database for some
of your data, make sure you account for any data-mirroring functions you've
set up and validate your Cloud Firestore Security Rules.

1. If you used Cloud Functions to maintain parity between your databases,
   make sure you're not duplicating write operations across both databases in a
   loop. Switch your function to write to a single database, or remove the
   function completely and start phasing out write functionality for the
   migrated data in apps still tied to Realtime Database. How you handle this for
   your app depends on your specific needs and your users.

2. Verify that your data is properly secured. Validate your Cloud Firestore Security Rules
   or IAM setup.