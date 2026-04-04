# Source: https://firebase.google.com/docs/firestore/firestore-for-rtdb.md.txt

<br />

You can use bothFirebase Realtime DatabaseandCloud Firestorein your app, and leverage each database solution's benefits to fit your needs. For example, you might want to leverageRealtime Database's support for presence, as outlined in[Build Presence inCloud Firestore](https://firebase.google.com/docs/firestore/solutions/presence).

Learn more about the[differences between the databases](https://firebase.google.com/docs/firestore/rtdb-vs-firestore).

## Moving data toCloud Firestore

If you've decided you want to migrate some of your data fromRealtime DatabasetoCloud Firestore, consider the following flow. Because every database has unique needs and structural considerations, there isn't an automated migration path. Instead, you can follow this general progression:

1. **Map the data structure and security rules fromRealtime DatabasetoCloud Firestore.** BothRealtime DatabaseandCloud Firestorerely on Firebase Authentication, so you don't need to change user authentication for your app. However, the security rules and data model are different and it's important to carefully account for those divergences before you start moving data to Cloud Firestore.

2. **Move historical data.** As you're setting up your new data structure inCloud Firestore, you can map and move existing data fromRealtime Databaseto your newCloud Firestoreinstance. However, if you're using both databases in your app, you don't need to move historical data out ofRealtime Database.

3. **Mirror new data to Firestore in realtime.** Use Cloud Functions to write new data to your newCloud Firestoredatabase as it gets added toRealtime Database.

4. **MakeCloud Firestoreyour primary database for the migrated data.** Once you've migrated some of your data, useCloud Firestoreas your primary database and reduce yourRealtime Databaseuse for the migrated data. Consider versions of your app that are still tied toRealtime Databasefor that data and how you plan to continue supporting them.

Make sure you account for[billing costs](https://firebase.google.com/pricing#blaze-calculator)for both[Realtime Database](https://firebase.google.com/docs/database/usage/billing)and[Cloud Firestore](https://firebase.google.com/docs/firestore/pricing).

## Map your data

Data inRealtime Databaseis structured as a single tree, whileCloud Firestoresupports more explicit data hierarchies through documents, collections, and subcollections. If you move some of your data fromRealtime DatabasetoCloud Firestore, you might want to consider a different architecture for your data.

### Major differences to consider

If you move data from your existingRealtime Databasetree toCloud Firestoredocuments and collections, keep in mind the following major differences between the databases that might impact how you structure data inCloud Firestore:

- Shallow queries offer more flexibility in hierarchical data structures.
- Complex queries offer more granularity and reduce the need for duplicate data.
- Query cursors offer more robust pagination.
- Transactions no longer require a common root for all your data, and are more efficient.
- Billing costs differ betweenRealtime DatabaseandCloud Firestore. In many cases,Cloud Firestoremight be more expensive thanRealtime Database, particularly if you rely on many small operations. Consider reducing the number of operations on your database and avoiding unnecessary writes. Learn more about the differences in[billing](https://firebase.google.com/docs/firestore/rtdb-vs-firestore#pricing)betweenRealtime DatabaseandCloud Firestore.

### Best practices in action

The following example reflects some of the considerations you might make as you shift your data between databases. You can leverage shallow reads and improved querying capabilities for more natural data structures than you may have used withRealtime Database.

Consider a city guide app that helps users find notable landmarks in cities around the world. SinceRealtime Databaselacks shallow reads, you might have had to structure the data in two top-level nodes, as follows:  

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

Cloud Firestorehas shallow reads, so querying for documents in a collection doesn't pull in data from subcollections. Consequently, you can store landmark information in a subcollection:  

    // /cities/$CITY_ID
    {
      name: "New York",
      population: 8000000,
      capital: False,
      landmarks: [... subcollection ...]
    }

Documents have a maximum size of 1MB, which is another reason to store landmarks as a subcollection, keeping each city document small, rather than bloating documents with nested lists.

Cloud Firestore's advanced querying capabilities reduce the need to duplicate data for common access patterns. For example, consider a screen in the city guide app that shows all of the capital cities ordered by population. InRealtime Database, the most efficient way to do this is to maintain a separate list of capital cities that duplicates data from the`cities`list, as follows:  

    {
       cities: {
        // ...
       },

       capital-cities: {
         // ...
       }
    }

InCloud Firestore, you can express a list of capital cities in order of population as a single query:  

    db.collection('cities')
        .where('capital', '==', true)
        .orderBy('population')

Read more about the[Cloud Firestoredata model](https://firebase.google.com/docs/firestore/data-model)and take a look at our[Solutions](https://firebase.google.com/docs/firestore/solutions)for more ideas on how to structure yourCloud Firestoredatabase.

## Secure your data

Whether you're using[Cloud FirestoreSecurity Rules](https://firebase.google.com/docs/firestore/security/get-started)for Android, Apple, or Web clients, or[Identity Access Management (IAM)](https://firebase.google.com/docs/firestore/security/iam)for servers, make sure you're securing your data inCloud Firestoreas well asRealtime Database. User authentication is handled by Authentication for both databases, so you don't need to change your implementation of Authentication when you start usingCloud Firestore.

### Major differences to consider

- Mobile and web SDKs useCloud FirestoreSecurity Rules, while server SDKs use Identity Access Management (IAM) to secure data.
- Cloud FirestoreSecurity Rulesdon't cascade unless you use a wildcard. Documents and collections don't otherwise inherit rules.
- You no longer need to validate data separately (as you did in[Realtime Database](https://firebase.google.com/docs/database/security/rules-conditions#validaterules)).
- Cloud Firestorechecks rules before executing a query to make sure that the user has the appropriate access for all data returned by the query.

## Move historical data toCloud Firestore

Once you've mapped your data and security structures toCloud Firestore's data and security models, you can start adding your data. If you plan to query historical data after you move your app fromRealtime DatabasetoCloud Firestore, add an export of your old data to your newCloud Firestoredatabase. If you plan to use bothRealtime DatabaseandCloud Firestorein your app, you can skip this step.

To avoid overwriting new data with old data, you might want to add your historical data first. If you add new data to both databases simultaneously, as discussed in the next step, make sure you give precedence to new data added toCloud FirestorebyCloud Functions.

To migrate historical data toCloud Firestore, follow these steps:

1. Export your data fromRealtime Databaseor[use a recent backup](https://firebase.google.com/docs/database/backups).
   1. Go to the[Realtime Databasesection](https://console.firebase.google.com/project/_/database/)in theFirebaseconsole.
   2. From the**Data** tab, select your database's root-level node and select**Export JSON**from the menu.
2. Create your new database inCloud Firestoreand[add your data](https://firebase.google.com/docs/firestore/manage-data/add-data).

   Consider the following strategies as you move some of your data toCloud Firestore:
   - Write a custom script that ports your data for you. While we can't offer a template for this script, because every database will have unique needs,Cloud Firestoreexperts on our[Slack channel](https://firebase.community/)or on[Stack Overflow](https://stackoverflow.com/questions/tagged/firebase)can review your script or offer advice for your specific situation.
   - Use the server SDKs (Node.js, Java, Python, or Go) to write data directly toCloud Firestore. For instructions on setting up the server SDKs, see[Get Started](https://firebase.google.com/docs/firestore/quickstart).
   - To expedite large data migrations, use[batched writes](https://firebase.google.com/docs/firestore/manage-data/transactions#batched-writes)and send up to 500 operations in a single network request.
   - To stay under[Cloud Firestorerate limits](https://firebase.google.com/docs/firestore/quotas#limits), limit operations to 500 writes/second for each collection.

## Add new data toCloud Firestore

To maintain parity between your databases, add new data to both databases in realtime. UseCloud Functionsto trigger a write toCloud Firestorewhenever a client writes toRealtime Database. Make sure thatCloud Firestoregives precedence to new data coming fromCloud Functionsover any writes you're making from your historical data migration.

Create a function to write new or changing data toCloud Firestoreevery time a client writes data toRealtime Database. Learn more about[Realtime Databasetriggers](https://firebase.google.com/docs/functions/database-events)forCloud Functions.

## MakeCloud Firestoreyour primary database for the migrated data

If you've decided to useCloud Firestoreas your primary database for some of your data, make sure you account for any data-mirroring functions you've set up and validate yourCloud FirestoreSecurity Rules.

1. If you usedCloud Functionsto maintain parity between your databases, make sure you're not duplicating write operations across both databases in a loop. Switch your function to write to a single database, or remove the function completely and start phasing out write functionality for the migrated data in apps still tied toRealtime Database. How you handle this for your app depends on your specific needs and your users.

2. Verify that your data is properly secured. Validate yourCloud FirestoreSecurity Rulesor IAM setup.