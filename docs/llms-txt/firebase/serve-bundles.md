# Source: https://firebase.google.com/docs/firestore/solutions/serve-bundles.md.txt

<br />

<br />

Many applications serve the same content to all users on first page load. For example a news site may show the latest stories, or an e-commerce site may show the best-selling items.

If this content is served fromCloud Firestore, each user will issue a new query for the same results when they load the application. Because these results are not cached between users, the application is slower and more expensive than it needs to be.

## Solution: Bundles

Cloud Firestorebundles allow you to assemble data bundles from common query results on the backend using the Firebase Admin SDK, and serve these pre-computed blobs cached on a CDN. This gives your users a much faster first load experience and reduces yourCloud Firestorequery costs.

In this guide we will useCloud Functionsto generate bundles andFirebase Hostingto dynamically cache and serve bundle content. More information about bundles is available in the[guides](https://firebase.google.com/docs/firestore/bundles).

First create a simple public HTTP function to query the 50 latest "stories" and serve the result as a bundle.  

##### Node.js

```javascript
exports.createBundle = functions.https.onRequest(async (request, response) => {
  // Query the 50 latest stories
  const latestStories = await db.collection('stories')
    .orderBy('timestamp', 'desc')
    .limit(50)
    .get();

  // Build the bundle from the query results
  const bundleBuffer = db.bundle('latest-stories')
    .add('latest-stories-query', latestStories)
    .build();

  // Cache the response for up to 5 minutes;
  // see https://firebase.google.com/docs/hosting/manage-cache
  response.set('Cache-Control', 'public, max-age=300, s-maxage=600');

  response.end(bundleBuffer);
});
      
```

##### Java

```java

package com.example;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.FirestoreBundle;
import com.google.cloud.firestore.Query.Direction;
import com.google.cloud.firestore.QuerySnapshot;
import com.google.cloud.functions.HttpFunction;
import com.google.cloud.functions.HttpRequest;
import com.google.cloud.functions.HttpResponse;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import java.io.BufferedWriter;
import java.io.IOException;

public class ExampleFunction implements HttpFunction {

  public static FirebaseApp initializeFirebase() throws IOException {
    if (FirebaseApp.getApps().isEmpty()) {
      FirebaseOptions options = FirebaseOptions.builder()
          .setCredentials(GoogleCredentials.getApplicationDefault())
          .setProjectId("YOUR-PROJECT-ID")
          .build();

      FirebaseApp.initializeApp(options);
    }

    return FirebaseApp.getInstance();
  }

  @Override
  public void service(HttpRequest request, HttpResponse response) throws Exception {
    // Get a Firestore instance
    FirebaseApp app = initializeFirebase();
    Firestore db = FirestoreClient.getFirestore(app);

    // Query the 50 latest stories
    QuerySnapshot latestStories = db.collection("stories")
        .orderBy("timestamp", Direction.DESCENDING)
        .limit(50)
        .get()
        .get();

    // Build the bundle from the query results
    FirestoreBundle bundle = db.bundleBuilder("latest-stores")
        .add("latest-stories-query", latestStories)
        .build();

    // Cache the response for up to 5 minutes
    // see https://firebase.google.com/docs/hosting/manage-cache
    response.appendHeader("Cache-Control", "public, max-age=300, s-maxage=600");

    // Write the bundle to the HTTP response
    BufferedWriter writer = response.getWriter();
    writer.write(new String(bundle.toByteBuffer().array()));
  }
}
      
```

Next configure Firebase Hosting to serve and cache this Cloud Function by modifying`firebase.json`. With this configuration theFirebase HostingCDN will serve the bundle content according to the cache settings set by the Cloud Function. When the cache expires it will refresh the content by triggering the function again.  

    firebase.json
    {
      "hosting": {
        // ...
        "rewrites": [{
          "source": "/createBundle",
          "function": "createBundle"
        }]
      },
      // ...
    }

Finally in your web application, fetch the bundled content from the CDN and load it into the Firestore SDK.  

    // If you are using module bundlers.
    import firebase from "firebase/app";
    import "firebase/firestore";
    import "firebase/firestore/bundle" // This line enables bundle loading as a side effect.

    async function fetchFromBundle() {
      // Fetch the bundle from Firebase Hosting, if the CDN cache is hit the 'X-Cache'
      // response header will be set to 'HIT'
      const resp = await fetch('/createBundle');

      // Load the bundle contents into the Firestore SDK
      await db.loadBundle(resp.body);

      // Query the results from the cache
      // Note: omitting "source: cache" will query the Firestore backend.
      
      const query = await db.namedQuery('latest-stories-query');
      const storiesSnap = await query.get({ source: 'cache' });

      // Use the results
      // ...
    }

## Estimated Savings

Consider a news website which gets 100,000 users per day and each user loads the same 50 top stories on initial load. Without any caching, this would result in 50 x 100,000 = 5,000,000 document reads per day fromCloud Firestore.

Now assume the site adopts the technique above and caches those 50 results for up to 5 minutes. So instead of loading the query results for every user, the results are loaded exactly 12 times per hour. No matter how many users arrive at the site, the number of queries to Cloud Firestore stays the same. Instead of 5,000,000 document reads, this page would use 12 x 24 x 50 = 14,400 document reads per day. The small additional costs for Firebase Hosting andCloud Functionsare easily offset by theCloud Firestorecost savings.

While the developer benefits from the cost savings, the biggest beneficiary is the user. Loading these 50 documents from the Firebase Hosting CDN rather than fromCloud Firestoredirectly can easily shave 100-200ms or more from the content load time of the page. Studies have repeatedly shown that speedy pages mean happier users.