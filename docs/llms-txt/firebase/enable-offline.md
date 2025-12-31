# Source: https://firebase.google.com/docs/firestore/manage-data/enable-offline.md.txt

<br />

Cloud Firestoresupports offline data persistence. This feature caches a copy of theCloud Firestoredata that your app is actively using, so your app can access the data when the device is offline. You can write, read, listen to, and query the cached data.

When the device comes back online,Cloud Firestoresynchronizes any local changes made by your app to theCloud Firestorebackend. For multiple changes to the same document, it's last write wins.
| **Note:** Offline persistence is supported only in Android, Apple, and web apps.

To use offline persistence, you don't need to make any changes to the code that you use to accessCloud Firestoredata. With offline persistence enabled, theCloud Firestoreclient library automatically manages online and offline data access and synchronizes local data when the device is back online.

## Configure offline persistence

When you initializeCloud Firestore, you can enable or disable offline persistence:

- For Android and Apple platforms, offline persistence is enabled by default. To disable persistence, set the`PersistenceEnabled`option to`false`.
- For the web, offline persistence is disabled by default. To enable persistence, call the`enablePersistence`method.Cloud Firestore's cache isn't automatically cleared between sessions. Consequently, if your web app handles sensitive information, make sure to ask the user if they're on a trusted device before enabling persistence.

**Important:** For the web, offline persistence is supported only by the Chrome, Safari, and Firefox web browsers.  

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable Web v9 modular SDK and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from version 8.  

```scilab
// Memory cache is the default if no config is specified.
initializeFirestore(app);

// This is the default behavior if no persistence is specified.
initializeFirestore(app, {localCache: memoryLocalCache()});

// Defaults to single-tab persistence if no tab manager is specified.
initializeFirestore(app, {localCache: persistentLocalCache(/*settings*/{})});

// Same as `initializeFirestore(app, {localCache: persistentLocalCache(/*settings*/{})})`,
// but more explicit about tab management.
initializeFirestore(app, 
  {localCache: 
    persistentLocalCache(/*settings*/{tabManager: persistentSingleTabManager()})
});

// Use multi-tab IndexedDb persistence.
initializeFirestore(app, 
  {localCache: 
    persistentLocalCache(/*settings*/{tabManager: persistentMultipleTabManager()})
  });
  
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable Web v9 modular SDK and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from version 8.  

```javascript
firebase.firestore().enablePersistence()
  .catch((err) => {
      if (err.code == 'failed-precondition') {
          // Multiple tabs open, persistence can only be enabled
          // in one tab at a a time.
          // ...
      } else if (err.code == 'unimplemented') {
          // The current browser does not support all of the
          // features required to enable persistence
          // ...
      }
  });
// Subsequent queries will use persistence, if it was enabled successfully  
https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L63-L75
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let settings = FirestoreSettings()

// Use memory-only cache
settings.cacheSettings =
MemoryCacheSettings(garbageCollectorSettings: MemoryLRUGCSettings())

// Use persistent disk cache, with 100 MB cache size
settings.cacheSettings = PersistentCacheSettings(sizeBytes: 100 * 1024 * 1024 as NSNumber)

// Any additional options
// ...

// Enable offline data persistence
let db = Firestore.firestore()
db.settings = settings  
https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1103-L1117
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRFirestoreSettings *settings = [[FIRFirestoreSettings alloc] init];

// Use memory-only cache
settings.cacheSettings = [[FIRMemoryCacheSettings alloc]
    initWithGarbageCollectorSettings:[[FIRMemoryLRUGCSettings alloc] init]];

// Use persistent disk cache (default behavior)
// This example uses 100 MB.
settings.cacheSettings = [[FIRPersistentCacheSettings alloc]
    initWithSizeBytes:@(100 * 1024 * 1024)];

// Any additional options
// ...

// Enable offline data persistence
FIRFirestore *db = [FIRFirestore firestore];
db.settings = settings;https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1005-L1021
```

### Kotlin

```kotlin
val settings = firestoreSettings {
    // Use memory cache
    setLocalCacheSettings(memoryCacheSettings {})
    // Use persistent disk cache (default)
    setLocalCacheSettings(persistentCacheSettings {})
}
db.firestoreSettings = settings  
https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L113-L119
```

### Java

```java
FirebaseFirestoreSettings settings = 
new FirebaseFirestoreSettings.Builder(db.getFirestoreSettings())
    // Use memory-only cache
    .setLocalCacheSettings(MemoryCacheSettings.newBuilder().build())
    // Use persistent disk cache (default)
    .setLocalCacheSettings(PersistentCacheSettings.newBuilder()
                            .build())
    .build();
db.setFirestoreSettings(settings);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L135-L143
```

### Dart

```dart
// Apple and Android
db.settings = const Settings(persistenceEnabled: true);

// Web
await db
    .enablePersistence(const PersistenceSettings(synchronizeTabs: true));https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1072-L1077
```

### Configure cache size

When persistence is enabled,Cloud Firestorecaches every document received from the backend for offline access.Cloud Firestoresets a default threshold for cache size. After exceeding the default,Cloud Firestoreperiodically attempts to clean up older, unused documents. You can configure a different cache size threshold or disable the clean-up process completely:  

### Web

```javascript
import { initializeFirestore, CACHE_SIZE_UNLIMITED } from "firebase/firestore";

const firestoreDb = initializeFirestore(app, {
  cacheSizeBytes: CACHE_SIZE_UNLIMITED
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/fs_setup_cache.js#L8-L12
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
firebase.firestore().settings({
    cacheSizeBytes: firebase.firestore.CACHE_SIZE_UNLIMITED
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L49-L51
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// The default cache size threshold is 100 MB. Configure "cacheSizeBytes"
// for a different threshold (minimum 1 MB) or set to "FirestoreCacheSizeUnlimited"
// to disable clean-up.
let settings = Firestore.firestore().settings
// Set cache size to 100 MB
settings.cacheSettings = PersistentCacheSettings(sizeBytes: 100 * 1024 * 1024 as NSNumber)
Firestore.firestore().settings = settings  
https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L159-L162
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// The default cache size threshold is 100 MB. Configure "cacheSizeBytes"
// for a different threshold (minimum 1 MB) or set to "kFIRFirestoreCacheSizeUnlimited"
// to disable clean-up.
FIRFirestoreSettings *settings = [FIRFirestore firestore].settings;
// Set cache size to 100 MB
settings.cacheSettings =
    [[FIRPersistentCacheSettings alloc] initWithSizeBytes:@(100 * 1024 * 1024)];
[FIRFirestore firestore].settings = settings;https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L82-L86
  
```

### Kotlin

```kotlin

// The default cache size threshold is 100 MB. Configure "setCacheSizeBytes"
// for a different threshold (minimum 1 MB) or set to "CACHE_SIZE_UNLIMITED"
// to disable clean-up.
val settings = FirebaseFirestoreSettings.Builder()
        .setCacheSizeBytes(FirebaseFirestoreSettings.CACHE_SIZE_UNLIMITED)
        .build()
db.firestoreSettings = settings
```

### Java

```java

// The default cache size threshold is 100 MB. Configure "setCacheSizeBytes"
// for a different threshold (minimum 1 MB) or set to "CACHE_SIZE_UNLIMITED"
// to disable clean-up.
FirebaseFirestoreSettings settings = new FirebaseFirestoreSettings.Builder()
        .setCacheSizeBytes(FirebaseFirestoreSettings.CACHE_SIZE_UNLIMITED)
        .build();
db.setFirestoreSettings(settings);
```

### Dart

```dart
db.settings = const Settings(
  persistenceEnabled: true,
  cacheSizeBytes: Settings.CACHE_SIZE_UNLIMITED,
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1083-L1086
```

## Listen to offline data

While the device is offline, if you have enabled offline persistence, your listeners will receive listen events when the locally cached data changes. You can listen to documents, collections, and queries.

To check whether you're receiving data from the server or the cache, use the`fromCache`property on the`SnapshotMetadata`in your snapshot event. If`fromCache`is`true`, the data came from the cache and might be stale or incomplete. If`fromCache`is`false`, the data is complete and current with the latest updates on the server.

By default, no event is raised if*only* the`SnapshotMetadata`changed. If you rely on the`fromCache`values, specify the`includeMetadataChanges`listen option when you attach your listen handler.  

### Web

```javascript
import { collection, onSnapshot, where, query } from "firebase/firestore"; 

const q = query(collection(db, "cities"), where("state", "==", "CA"));
onSnapshot(q, { includeMetadataChanges: true }, (snapshot) => {
    snapshot.docChanges().forEach((change) => {
        if (change.type === "added") {
            console.log("New city: ", change.doc.data());
        }

        const source = snapshot.metadata.fromCache ? "local cache" : "server";
        console.log("Data came from " + source);
    });
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/use_from_cache.js#L8-L20
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").where("state", "==", "CA")
  .onSnapshot({ includeMetadataChanges: true }, (snapshot) => {
      snapshot.docChanges().forEach((change) => {
          if (change.type === "added") {
              console.log("New city: ", change.doc.data());
          }

          var source = snapshot.metadata.fromCache ? "local cache" : "server";
          console.log("Data came from " + source);
      });
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L107-L117
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Listen to metadata updates to receive a server snapshot even if
// the data is the same as the cached data.
db.collection("cities").whereField("state", isEqualTo: "CA")
  .addSnapshotListener(includeMetadataChanges: true) { querySnapshot, error in
    guard let snapshot = querySnapshot else {
      print("Error retreiving snapshot: \(error!)")
      return
    }

    for diff in snapshot.documentChanges {
      if diff.type == .added {
        print("New city: \(diff.document.data())")
      }
    }

    let source = snapshot.metadata.isFromCache ? "local cache" : "server"
    print("Metadata: Data fetched from \(source)")
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1124-L1141
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Listen to metadata updates to receive a server snapshot even if
// the data is the same as the cached data.
[[[db collectionWithPath:@"cities"] queryWhereField:@"state" isEqualTo:@"CA"]
    addSnapshotListenerWithIncludeMetadataChanges:YES
    listener:^(FIRQuerySnapshot *snapshot, NSError *error) {
      if (snapshot == nil) {
        NSLog(@"Error retreiving snapshot: %@", error);
        return;
      }
      for (FIRDocumentChange *diff in snapshot.documentChanges) {
        if (diff.type == FIRDocumentChangeTypeAdded) {
          NSLog(@"New city: %@", diff.document.data);
        }
      }

      NSString *source = snapshot.metadata.isFromCache ? @"local cache" : @"server";
      NSLog(@"Metadata: Data fetched from %@", source);
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1028-L1045
```

### Kotlin

```java
db.collection("cities").whereEqualTo("state", "CA")
    .addSnapshotListener(MetadataChanges.INCLUDE) { querySnapshot, e ->
        if (e != null) {
            Log.w(TAG, "Listen error", e)
            return@addSnapshotListener
        }

        for (change in querySnapshot!!.documentChanges) {
            if (change.type == DocumentChange.Type.ADDED) {
                Log.d(TAG, "New city: ${change.document.data}")
            }

            val source = if (querySnapshot.metadata.isFromCache) {
                "local cache"
            } else {
                "server"
            }
            Log.d(TAG, "Data fetched from $source")
        }
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1055-L1074
```

### Java

```java
db.collection("cities").whereEqualTo("state", "CA")
        .addSnapshotListener(MetadataChanges.INCLUDE, new EventListener<QuerySnapshot>() {
            @Override
            public void onEvent(@Nullable QuerySnapshot querySnapshot,
                                @Nullable FirebaseFirestoreException e) {
                if (e != null) {
                    Log.w(TAG, "Listen error", e);
                    return;
                }

                for (DocumentChange change : querySnapshot.getDocumentChanges()) {
                    if (change.getType() == Type.ADDED) {
                        Log.d(TAG, "New city:" + change.getDocument().getData());
                    }

                    String source = querySnapshot.getMetadata().isFromCache() ?
                            "local cache" : "server";
                    Log.d(TAG, "Data fetched from " + source);
                }

            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1266-L1287
```

### Dart

```dart
db
    .collection("cities")
    .where("state", isEqualTo: "CA")
    .snapshots(includeMetadataChanges: true)
    .listen((querySnapshot) {
  for (var change in querySnapshot.docChanges) {
    if (change.type == DocumentChangeType.added) {
      final source =
          (querySnapshot.metadata.isFromCache) ? "local cache" : "server";

      print("Data fetched from $source}");
    }
  }
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1092-L1105
```

## Get offline data

If you get a document while the device is offline,Cloud Firestorereturns data from the cache.

When querying a collection, an empty result is returned if there are no cached documents. When fetching a specific document, an error is returned instead.

## Query offline data

Querying works with offline persistence. You can retrieve the results of queries with either a direct get or by listening, as described in the preceding sections. You can also create new queries on locally persisted data while the device is offline, but the queries will initially run only against the cached documents.

## Configure offline query indexes

By default, the Firestore SDK scans all documents in a collection in its local cache when executing offline queries. With this default behavior, offline query performance can suffer when users are offline for long periods of time.

With persistent cache enabled, you can improve the performance of offline queries by allowing the SDK to create local query indexes automatically.

Automatic indexing is disabled by default. Your app must enable automatic indexing each time it starts. Control whether automatic indexing is enabled as shown below.  

##### Swift

```swift
if let indexManager = Firestore.firestore().persistentCacheIndexManager {
  // Indexing is disabled by default
  indexManager.enableIndexAutoCreation()
} else {
  print("indexManager is nil")
}
    
```

##### Objective-C

```objective-c
PersistentCacheIndexManager *indexManager = [FIRFirestore firestore].persistentCacheIndexManager;
if (indexManager) {
  // Indexing is disabled by default
  [indexManager enableIndexAutoCreation];
}
    
```

### Kotlin

```kotlin
// return type: PersistentCacheManager?

Firebase.firestore.persistentCacheIndexManager?.apply {
      // Indexing is disabled by default
      enableIndexAutoCreation()
    } ?: println("indexManager is null")
    
```

### Java

```java
// return type: @Nullable PersistentCacheIndexManager
PersistentCacheIndexManager indexManager = FirebaseFirestore.getInstance().getPersistentCacheIndexManager();
if (indexManager != null) {
  // Indexing is disabled by default
  indexManager.enableIndexAutoCreation();
}

// If not check indexManager != null, IDE shows warning: Method invocation 'enableIndexAutoCreation' may produce 'NullPointerException' 
FirebaseFirestore.getInstance().getPersistentCacheIndexManager().enableIndexAutoCreation();
    
```

Once automatic indexing is enabled, the SDK evaluates which collections have a large number of cached documents and optimizes performance of local queries.

The SDK provides a method for deleting query indexes.

## Disable and enable network access

You can use the method below to disable network access for yourCloud Firestoreclient. While network access is disabled, all snapshot listeners and document requests retrieve results from the cache. Write operations are queued until network access is re-enabled.  

### Web

```javascript
import { disableNetwork } from "firebase/firestore"; 

await disableNetwork(db);
console.log("Network disabled!");
// Do offline actions
// ...  
https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/disable_network.js#L8-L15
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
firebase.firestore().disableNetwork()
    .then(() => {
        // Do offline actions
        // ...
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L82-L88
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
Firestore.firestore().disableNetwork { (error) in
  // Do offline things
  // ...
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1147-L1150
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[FIRFirestore firestore] disableNetworkWithCompletion:^(NSError *_Nullable error) {
  // Do offline actions
  // ...
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1051-L1054
```

### Kotlin

```kotlin
db.disableNetwork().addOnCompleteListener {
    // Do offline things
    // ...
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1039-L1042
```

### Java

```java
db.disableNetwork()
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                // Do offline things
                // ...
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1242-L1249
```

### Dart

```dart
db.disableNetwork().then((_) {
  // Do offline things
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1111-L1113
```

Use the following method to re-enable network access:  

### Web

```javascript
import { enableNetwork } from "firebase/firestore"; 

await enableNetwork(db);
// Do online actions
// ...  
https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/enable_network.js#L8-L14
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
firebase.firestore().enableNetwork()
    .then(() => {
        // Do online actions
        // ...
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L93-L99
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
Firestore.firestore().enableNetwork { (error) in
  // Do online things
  // ...
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1154-L1157
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[FIRFirestore firestore] enableNetworkWithCompletion:^(NSError *_Nullable error) {
  // Do online actions
  // ...
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1058-L1061
```

### Kotlin

```kotlin
db.enableNetwork().addOnCompleteListener {
    // Do online things
    // ...
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1046-L1049
```

### Java

```java
db.enableNetwork()
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                // Do online things
                // ...
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1253-L1260
```

### Dart

```dart
db.enableNetwork().then((_) {
  // Back online
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1119-L1121
```