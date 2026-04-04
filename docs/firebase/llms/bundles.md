# Source: https://firebase.google.com/docs/firestore/bundles.md.txt

<br />

<br />

| **Note:** Data bundles is an optional, advancedCloud Firestorefeature. We cover data bundles here along with basic concepts for understandingCloud Firestoreso you're aware of features that can help you manage query costs once your app has scaled up. Before you consider data bundles, in addition to reading the other overview and concept topics, be sure to read the guide for[performingCloud Firestorequeries](https://firebase.google.com/docs/firestore/query-data/queries).

Cloud Firestoredata bundles are static data files built by you fromCloud Firestoredocument and query snapshots, and published by you on a CDN, hosting service or other solution. Data bundles include both the documents you want to provide to your client apps and metadata about the queries that generated them. You use client SDKs to download bundles over the network or from local storage, after which you load bundle data to theCloud Firestorelocal cache. Once a bundle is loaded, a client app can query documents from the local cache or the backend.

With data bundles, your apps can load the results of common queries sooner, since documents are available at start-up without the need for calls to theCloud Firestorebackend. If results are loaded from local cache, you also benefit from reduced access costs. Instead of paying for a million app instances to query the same initial 100 documents, you pay only for the queries needed to bundle those 100 documents.

Cloud Firestoredata bundles are built to work well with other Firebase backend products. Take a look at an[integrated solution](https://firebase.google.com/docs/firestore/solutions/serve-bundles)in which bundles are built byCloud Functionsand served to users withFirebase Hosting.

Using a bundle with your app involves three steps:

1. Building the bundle with the Admin SDK
2. Serving the bundle from local storage or from a CDN
3. Loading bundles in the client

## What is a data bundle?

A data bundle is a static binary file built by you to package one or more*document and/or query snapshots* and from which you can extract*named queries*. As we discuss below, the server-side SDKs let you build bundles and client SDKs provide methods to let you load bundles to the local cache.

Named queries are an especially powerful feature of bundles. Named queries are`Query`objects you can extract from a bundle, then use immediately to query data either from cache or from the backend, as you do normally in any part of your app that talks toCloud Firestore.

## Building data bundles on the server

Using the Node.js or Java[Admin SDK](https://firebase.google.com/docs/admin/setup)gives you complete control over what to include in the bundles and how to serve them.
**Note:** Make sure to bundle only publicly readable data. The Admin SDK acts as a privileged user and does not evaluate Security Rules; therefore, it will bundle any documents or queried data regardless of your security rules.  

##### Node.js

```javascript
var bundleId = "latest-stories";

var bundle = firestore.bundle(bundleId);

var docSnapshot = await firestore.doc('stories/stories').get();
var querySnapshot = await firestore.collection('stories').get();

// Build the bundle
// Note how querySnapshot is named "latest-stories-query"
var bundleBuffer = bundle.add(docSnapshot); // Add a document
                   .add('latest-stories-query', querySnapshot) // Add a named query.
                   .build()
      
```

##### Java

```java
Firestore db = FirestoreClient.getFirestore(app);

// Query the 50 latest stories
QuerySnapshot latestStories = db.collection("stories")
    .orderBy("timestamp", Direction.DESCENDING)
    .limit(50)
    .get()
    .get();

// Build the bundle from the query results
FirestoreBundle bundle = db.bundleBuilder("latest-stories")
    .add("latest-stories-query", latestStories)
    .build();
      
```

##### Python

```python
from google.cloud import firestore
from google.cloud.firestore_bundle import FirestoreBundle

db = firestore.Client()
bundle = FirestoreBundle("latest-stories")

doc_snapshot = db.collection("stories").document("news-item").get()
query = db.collection("stories")._query()

# Build the bundle
# Note how `query` is named "latest-stories-query"
bundle_buffer: str = bundle.add_document(doc_snapshot).add_named_query(
    "latest-stories-query", query,
).build()
      
```

## Serving data bundles

You can serve bundles to your client apps from a CDN or by downloading them from, for example,Cloud Storage.

Assume the bundle created in the previous section has been saved to a file named`bundle.txt`and posted on a server. This bundle file is like any other asset you can serve over the web, as shown here for a simple Node.js Express app.  

    const fs = require('fs');
    const server = require('http').createServer();

    server.on('request', (req, res) => {
      const src = fs.createReadStream('./bundle.txt');
      src.pipe(res);
    });

    server.listen(8000);

## Loading data bundles in the client

You load Firestore bundles by fetching them from a remote server, whether by making an HTTP request, calling a storage API or using any other technique for fetching binary files on a network.

Once fetched, using theCloud Firestoreclient SDK, your app calls the`loadBundle`method, which returns a task tracking object, the completion of which you can monitor much as you monitor the status of a Promise. On successful bundle loading task completion, bundle contents are available in the local cache.  

### Web

```javascript
import { loadBundle, namedQuery, getDocsFromCache } from "firebase/firestore";

async function fetchFromBundle() {
  // Fetch the bundle from Firebase Hosting, if the CDN cache is hit the 'X-Cache'
  // response header will be set to 'HIT'
  const resp = await fetch('/createBundle');

  // Load the bundle contents into the Firestore SDK
  await loadBundle(db, resp.body);

  // Query the results from the cache
  const query = await namedQuery(db, 'latest-stories-query');
  const storiesSnap = await getDocsFromCache(query);

  // Use the results
  // ...
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-solution-bundles/fs_bundle_load.js#L8-L24
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// If you are using module bundlers.
import firebase from "firebase/app";
import "firebase/firestore";
import "firebase/firestore/bundle"; // This line enables bundle loading as a side effect.

// ...

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
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.solution-bundles.js#L2-L29
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Utility function for errors when loading bundles.
func bundleLoadError(reason: String) -> NSError {
  return NSError(domain: "FIRSampleErrorDomain",
                 code: 0,
                 userInfo: [NSLocalizedFailureReasonErrorKey: reason])
}

func fetchRemoteBundle(for firestore: Firestore,
                       from url: URL) async throws -> LoadBundleTaskProgress {
  guard let inputStream = InputStream(url: url) else {
    let error = self.bundleLoadError(reason: "Unable to create stream from the given url: \(url)")
    throw error
  }

  return try await firestore.loadBundle(inputStream)
}

// Fetches a specific named query from the provided bundle.
func loadQuery(named queryName: String,
               fromRemoteBundle bundleURL: URL,
               with store: Firestore) async throws -> Query {
  let _ = try await fetchRemoteBundle(for: store, from: bundleURL)
  if let query = await store.getQuery(named: queryName) {
    return query
  } else {
    throw bundleLoadError(reason: "Could not find query named \(queryName)")
  }
}

// Load a query and fetch its results from a bundle.
func runStoriesQuery() async {
  let queryName = "latest-stories-query"
  let firestore = Firestore.firestore()
  let remoteBundle = URL(string: "https://example.com/createBundle")!

  do {
    let query = try await loadQuery(named: queryName,
                                    fromRemoteBundle: remoteBundle,
                                    with: firestore)
    let snapshot = try await query.getDocuments()
    print(snapshot)
    // handle query results
  } catch {
    print(error)
  }
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/SolutionBundles.swift#L22-L67
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Utility function for errors when loading bundles.
- (NSError *)bundleLoadErrorWithReason:(NSString *)reason {
  return [NSError errorWithDomain:@"FIRSampleErrorDomain"
                             code:0
                         userInfo:@{NSLocalizedFailureReasonErrorKey: reason}];
}

// Loads a remote bundle from the provided url.
- (void)fetchRemoteBundleForFirestore:(FIRFirestore *)firestore
                              fromURL:(NSURL *)url
                           completion:(void (^)(FIRLoadBundleTaskProgress *_Nullable,
                                                NSError *_Nullable))completion {
  NSInputStream *inputStream = [NSInputStream inputStreamWithURL:url];
  if (inputStream == nil) {
    // Unable to create input stream.
    NSError *error =
        [self bundleLoadErrorWithReason:
            [NSString stringWithFormat:@"Unable to create stream from the given url: %@", url]];
    completion(nil, error);
    return;
  }

  [firestore loadBundleStream:inputStream
                   completion:^(FIRLoadBundleTaskProgress * _Nullable progress,
                                NSError * _Nullable error) {
    if (progress == nil) {
      completion(nil, error);
      return;
    }

    if (progress.state == FIRLoadBundleTaskStateSuccess) {
      completion(progress, nil);
    } else {
      NSError *concreteError =
          [self bundleLoadErrorWithReason:
              [NSString stringWithFormat:
                  @"Expected bundle load to be completed, but got %ld instead",
                  (long)progress.state]];
      completion(nil, concreteError);
    }
    completion(nil, nil);
  }];
}

// Loads a bundled query.
- (void)loadQueryNamed:(NSString *)queryName
   fromRemoteBundleURL:(NSURL *)url
         withFirestore:(FIRFirestore *)firestore
            completion:(void (^)(FIRQuery *_Nullable, NSError *_Nullable))completion {
  [self fetchRemoteBundleForFirestore:firestore
                              fromURL:url
                           completion:^(FIRLoadBundleTaskProgress *progress, NSError *error) {
    if (error != nil) {
      completion(nil, error);
      return;
    }

    [firestore getQueryNamed:queryName completion:^(FIRQuery *query) {
      if (query == nil) {
        NSString *errorReason =
            [NSString stringWithFormat:@"Could not find query named %@", queryName];
        NSError *error = [self bundleLoadErrorWithReason:errorReason];
        completion(nil, error);
        return;
      }
      completion(query, nil);
    }];
  }];
}

- (void)runStoriesQuery {
  NSString *queryName = @"latest-stories-query";
  FIRFirestore *firestore = [FIRFirestore firestore];
  NSURL *bundleURL = [NSURL URLWithString:@"https://example.com/createBundle"];
  [self loadQueryNamed:queryName
   fromRemoteBundleURL:bundleURL
         withFirestore:firestore
            completion:^(FIRQuery *query, NSError *error) {
    // Handle query results
  }];
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/FIRSolutionsBundleViewController.m#L33-L113
```

### Kotlin

```kotlin
@Throws(IOException::class)
fun getBundleStream(urlString: String?): InputStream {
    val url = URL(urlString)
    val connection = url.openConnection() as HttpURLConnection
    return connection.inputStream
}

@Throws(IOException::class)
fun fetchFromBundle() {
    val bundleStream = getBundleStream("https://example.com/createBundle")
    val loadTask = db.loadBundle(bundleStream)

    // Chain the following tasks
    // 1) Load the bundle
    // 2) Get the named query from the local cache
    // 3) Execute a get() on the named query
    loadTask.continueWithTask<Query> { task ->
        // Close the stream
        bundleStream.close()

        // Calling .result propagates errors
        val progress = task.getResult(Exception::class.java)

        // Get the named query from the bundle cache
        db.getNamedQuery("latest-stories-query")
    }.continueWithTask { task ->
        val query = task.getResult(Exception::class.java)!!

        // get() the query results from the cache
        query.get(Source.CACHE)
    }.addOnCompleteListener { task ->
        if (!task.isSuccessful) {
            Log.w(TAG, "Bundle loading failed", task.exception)
            return@addOnCompleteListener
        }

        // Get the QuerySnapshot from the bundle
        val storiesSnap = task.result

        // Use the results
        // ...
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/SolutionBundles.kt#L18-L60
```

### Java

```java
public InputStream getBundleStream(String urlString) throws IOException {
    URL url = new URL(urlString);
    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    return connection.getInputStream();
}

public void fetchBundleFrom() throws IOException {
    final InputStream bundleStream = getBundleStream("https://example.com/createBundle");
    LoadBundleTask loadTask = db.loadBundle(bundleStream);

    // Chain the following tasks
    // 1) Load the bundle
    // 2) Get the named query from the local cache
    // 3) Execute a get() on the named query
    loadTask.continueWithTask(new Continuation<LoadBundleTaskProgress, Task<Query>>() {
        @Override
        public Task<Query> then(@NonNull Task<LoadBundleTaskProgress> task) throws Exception {
            // Close the stream
            bundleStream.close();

            // Calling getResult() propagates errors
            LoadBundleTaskProgress progress = task.getResult(Exception.class);

            // Get the named query from the bundle cache
            return db.getNamedQuery("latest-stories-query");
        }
    }).continueWithTask(new Continuation<Query, Task<QuerySnapshot>>() {
        @Override
        public Task<QuerySnapshot> then(@NonNull Task<Query> task) throws Exception {
            Query query = task.getResult(Exception.class);

            // get() the query results from the cache
            return query.get(Source.CACHE);
        }
    }).addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
        @Override
        public void onComplete(@NonNull Task<QuerySnapshot> task) {
            if (!task.isSuccessful()) {
                Log.w(TAG, "Bundle loading failed", task.getException());
                return;
            }

            // Get the QuerySnapshot from the bundle
            QuerySnapshot storiesSnap = task.getResult();

            // Use the results
            // ...
        }
    });
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/SolutionBundles.java#L32-L81
```

### Dart

```dart
// Get a bundle from a server
final url = Uri.https('example.com', '/create-bundle');
final response = await http.get(url);
String body = response.body;
final buffer = Uint8List.fromList(body.codeUnits);

// Load a bundle from a buffer
LoadBundleTask task = FirebaseFirestore.instance.loadBundle(buffer);
await task.stream.toList();

// Use the cached named query
final results = await FirebaseFirestore.instance.namedQueryGet(
  "latest-stories-query",
  options: const GetOptions(
    source: Source.cache,
  ),
);
https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L109-L126
```

##### C++

```c++
db->LoadBundle("bundle_name", [](const LoadBundleTaskProgress& progress) {
  switch(progress.state()) {
    case LoadBundleTaskProgress::State::kError: {
      // The bundle load has errored. Handle the error in the returned future.
      return;
    }
    case LoadBundleTaskProgress::State::kInProgress: {
      std::cout << "Bytes loaded from bundle: " << progress.bytes_loaded()
                << std::endl;
      break;
    }
    case LoadBundleTaskProgress::State::kSuccess: {
      std::cout << "Bundle load succeeeded" << std::endl;
      break;
    }
  }
}).OnCompletion([db](const Future<LoadBundleTaskProgress>& future) {
  if (future.error() != Error::kErrorOk) {
    // Handle error...
    return;
  }

  const std::string& query_name = "latest_stories_query";
  db->NamedQuery(query_name).OnCompletion([](const Future<Query>& query_future){
    if (query_future.error() != Error::kErrorOk) {
      // Handle error...
      return;
    }

    const Query* query = query_future.result();
    query->Get().OnCompletion([](const Future<QuerySnapshot> &){
      // ...
    });
  });
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1215-L1249
```

Note that if you load a named query from a bundle built less than 30 minutes prior, once you use it to read from the backend rather than cache, you will only pay for database reads needed to update documents to match what is stored on the backend; that is, you only pay for the deltas.

## What next?

- Refer to the data bundles API reference documentation for the client side ([Apple](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore#bundles),[Android](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#loadBundle(java.nio.ByteBuffer)),[web](https://firebase.google.com/docs/reference/js/firebase.firestore.Firestore#loadbundle)) and server side ([Node.js](https://googleapis.dev/nodejs/firestore/latest/Firestore.html#bundle)).

- If you haven't already, take a look at the[Cloud FunctionsandFirebase Hostingsolution for building and serving bundles](https://firebase.google.com/docs/firestore/solutions/serve-bundles).