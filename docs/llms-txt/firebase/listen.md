# Source: https://firebase.google.com/docs/firestore/query-data/listen.md.txt

<br />

You can*listen* to a document with the`onSnapshot()`method. An initial call using the callback you provide creates a document snapshot immediately with the current contents of the single document. Then, each time the contents change, another call updates the document snapshot.
**Note:** Realtime listeners are not supported in the PHP client library.  

### Web

```javascript
import { doc, onSnapshot } from "firebase/firestore";

const unsub = onSnapshot(doc(db, "cities", "SF"), (doc) => {
    console.log("Current data: ", doc.data());
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/listen_document.js#L8-L12
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").doc("SF")
    .onSnapshot((doc) => {
        console.log("Current data: ", doc.data());
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L623-L626
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
db.collection("cities").document("SF")
  .addSnapshotListener { documentSnapshot, error in
    guard let document = documentSnapshot else {
      print("Error fetching document: \(error!)")
      return
    }
    guard let data = document.data() else {
      print("Document data was empty.")
      return
    }
    print("Current data: \(data)")
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L773-L784
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"]
    addSnapshotListener:^(FIRDocumentSnapshot *snapshot, NSError *error) {
      if (snapshot == nil) {
        NSLog(@"Error fetching document: %@", error);
        return;
      }
      NSLog(@"Current data: %@", snapshot.data);
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L695-L702
```

### Kotlin

```kotlin
val docRef = db.collection("cities").document("SF")
docRef.addSnapshotListener { snapshot, e ->
    if (e != null) {
        Log.w(TAG, "Listen failed.", e)
        return@addSnapshotListener
    }

    if (snapshot != null && snapshot.exists()) {
        Log.d(TAG, "Current data: ${snapshot.data}")
    } else {
        Log.d(TAG, "Current data: null")
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L525-L537
```

### Java

```java
final DocumentReference docRef = db.collection("cities").document("SF");
docRef.addSnapshotListener(new EventListener<DocumentSnapshot>() {
    @Override
    public void onEvent(@Nullable DocumentSnapshot snapshot,
                        @Nullable FirebaseFirestoreException e) {
        if (e != null) {
            Log.w(TAG, "Listen failed.", e);
            return;
        }

        if (snapshot != null && snapshot.exists()) {
            Log.d(TAG, "Current data: " + snapshot.getData());
        } else {
            Log.d(TAG, "Current data: null");
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L681-L697
```

### Dart

```dart
final docRef = db.collection("cities").doc("SF");
docRef.snapshots().listen(
      (event) => print("current data: ${event.data()}"),
      onError: (error) => print("Listen failed: $error"),
    );
https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L525-L530
```

Often, you want your UI to react to changes in the contents of a Firestore document or collection. You can do so with a`StreamBuilder`widget that consumes the Firestore snapshot stream:  

```dart
class UserInformation extends StatefulWidget {
  @override
  _UserInformationState createState() => _UserInformationState();
}

class _UserInformationState extends State<UserInformation> {
  final Stream<QuerySnapshot> _usersStream =
      FirebaseFirestore.instance.collection('users').snapshots();

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<QuerySnapshot>(
      stream: _usersStream,
      builder: (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
        if (snapshot.hasError) {
          return const Text('Something went wrong');
        }

        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Text("Loading");
        }

        return ListView(
          children: snapshot.data!.docs
              .map((DocumentSnapshot document) {
                Map<String, dynamic> data =
                    document.data()! as Map<String, dynamic>;
                return ListTile(
                  title: Text(data['full_name']),
                  subtitle: Text(data['company']),
                );
              })
              .toList()
              .cast(),
        );
      },
    );
  }
}https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/widgets/user_info_streambuilder.dart#L5-L43
```

##### Java

    DocumentReference docRef = db.collection("cities").document("SF");
    docRef.addSnapshotListener(
        new EventListener<DocumentSnapshot>() {
          @Override
          public void onEvent(@Nullable DocumentSnapshot snapshot, @Nullable FirestoreException e) {
            if (e != null) {
              System.err.println("Listen failed: " + e);
              return;
            }

            if (snapshot != null && snapshot.exists()) {
              System.out.println("Current data: " + snapshot.getData());
            } else {
              System.out.print("Current data: null");
            }
          }
        });  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ListenDataSnippets.java#L53-L74

##### Python


    # Create an Event for notifying main thread.
    callback_done = threading.Event()

    # Create a callback on_snapshot function to capture changes
    def on_snapshot(doc_snapshot, changes, read_time):
        for doc in doc_snapshot:
            print(f"Received document snapshot: {doc.id}")
        callback_done.set()

    doc_ref = db.collection("cities").document("SF")

    # Watch the document
    doc_watch = doc_ref.on_snapshot(on_snapshot)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L676-L689

##### C++

```c++
DocumentReference doc_ref = db->Collection("cities").Document("SF");
doc_ref.AddSnapshotListener(
    [](const DocumentSnapshot& snapshot, Error error, const std::string& errorMsg) {
      if (error == Error::kErrorOk) {
        if (snapshot.exists()) {
          std::cout << "Current data: " << snapshot << std::endl;
        } else {
          std::cout << "Current data: null" << std::endl;
        }
      } else {
        std::cout << "Listen failed: " << error << std::endl;
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L613-L625
```

##### Node.js

    const doc = db.collection('cities').doc('SF');

    const observer = doc.onSnapshot(docSnapshot => {
      console.log(`Received doc snapshot: ${docSnapshot}`);
      // ...
    }, err => {
      console.log(`Encountered error: ${err}`);
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L781-L791

##### Go

    import (
    	"context"
    	"fmt"
    	"io"
    	"time"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    )

    // listenDocument listens to a single document.
    func listenDocument(ctx context.Context, w io.Writer, projectID, collection string) error {
    	// projectID := "project-id"
    	// Ð¡ontext with timeout stops listening to changes.
    	ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    	defer cancel()

    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()

    	it := client.Collection(collection).Doc("SF").Snapshots(ctx)
    	for {
    		snap, err := it.Next()
    		// DeadlineExceeded will be returned when ctx is cancelled.
    		if status.Code(err) == codes.DeadlineExceeded {
    			return nil
    		}
    		if err != nil {
    			return fmt.Errorf("Snapshots.Next: %w", err)
    		}
    		if !snap.Exists() {
    			fmt.Fprintf(w, "Document no longer exists\n")
    			return nil
    		}
    		fmt.Fprintf(w, "Received document snapshot: %v\n", snap.Data())
    	}
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/listen_document.go#L18-L61

##### PHP

```php
// Not supported in the PHP client library
```

##### Unity

```c#
DocumentReference docRef = db.Collection("cities").Document("SF");
docRef.Listen(snapshot => {
    Debug.Log("Callback received document snapshot.");
    Debug.Log(String.Format("Document data for {0} document:", snapshot.Id));
    Dictionary<string, object> city = snapshot.ToDictionary();
    foreach (KeyValuePair<string, object> pair in city) {
        Debug.Log(String.Format("{0}: {1}", pair.Key, pair.Value));
    }
});
```

##### C#

    DocumentReference docRef = db.Collection("cities").Document("SF");
    FirestoreChangeListener listener = docRef.Listen(snapshot =>
    {
        Console.WriteLine("Callback received document snapshot.");
        Console.WriteLine("Document exists? {0}", snapshot.Exists);
        if (snapshot.Exists)
        {
            Console.WriteLine("Document data for {0} document:", snapshot.Id);
            Dictionary<string, object> city = snapshot.ToDictionary();
            foreach (KeyValuePair<string, object> pair in city)
            {
                Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
            }
        }
    });  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/ListenData/Program.cs#L40-L54

##### Ruby

    doc_ref = firestore.col(collection_path).doc document_path
    snapshots = []

    # Watch the document.
    listener = doc_ref.listen do |snapshot|
      puts "Received document snapshot: #{snapshot.document_id}"
      snapshots << snapshot
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/query_watch.rb#L24-L31

### Events for local changes

Local writes in your app will invoke snapshot listeners immediately. This is because of an important feature called "latency compensation." When you perform a write, your listeners will be notified with the new data*before*the data is sent to the backend.

Retrieved documents have a`metadata.hasPendingWrites`property that indicates whether the document has local changes that haven't been written to the backend yet. You can use this property to determine the source of events received by your snapshot listener:  

### Web

```javascript
import { doc, onSnapshot } from "firebase/firestore";

const unsub = onSnapshot(doc(db, "cities", "SF"), (doc) => {
  const source = doc.metadata.hasPendingWrites ? "Local" : "Server";
  console.log(source, " data: ", doc.data());
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/listen_document_local.js#L8-L13
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").doc("SF")
    .onSnapshot((doc) => {
        var source = doc.metadata.hasPendingWrites ? "Local" : "Server";
        console.log(source, " data: ", doc.data());
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L638-L642
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
db.collection("cities").document("SF")
  .addSnapshotListener { documentSnapshot, error in
    guard let document = documentSnapshot else {
      print("Error fetching document: \(error!)")
      return
    }
    let source = document.metadata.hasPendingWrites ? "Local" : "Server"
    print("\(source) data: \(document.data() ?? [:])")
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L790-L798
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"]
    addSnapshotListener:^(FIRDocumentSnapshot *snapshot, NSError *error) {
      if (snapshot == nil) {
        NSLog(@"Error fetching document: %@", error);
        return;
      }
      NSString *source = snapshot.metadata.hasPendingWrites ? @"Local" : @"Server";
      NSLog(@"%@ data: %@", source, snapshot.data);
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L708-L716
```

### Kotlin

```kotlin
val docRef = db.collection("cities").document("SF")
docRef.addSnapshotListener { snapshot, e ->
    if (e != null) {
        Log.w(TAG, "Listen failed.", e)
        return@addSnapshotListener
    }

    val source = if (snapshot != null && snapshot.metadata.hasPendingWrites()) {
        "Local"
    } else {
        "Server"
    }

    if (snapshot != null && snapshot.exists()) {
        Log.d(TAG, "$source data: ${snapshot.data}")
    } else {
        Log.d(TAG, "$source data: null")
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L543-L561
```

### Java

```java
final DocumentReference docRef = db.collection("cities").document("SF");
docRef.addSnapshotListener(new EventListener<DocumentSnapshot>() {
    @Override
    public void onEvent(@Nullable DocumentSnapshot snapshot,
                        @Nullable FirebaseFirestoreException e) {
        if (e != null) {
            Log.w(TAG, "Listen failed.", e);
            return;
        }

        String source = snapshot != null && snapshot.getMetadata().hasPendingWrites()
                ? "Local" : "Server";

        if (snapshot != null && snapshot.exists()) {
            Log.d(TAG, source + " data: " + snapshot.getData());
        } else {
            Log.d(TAG, source + " data: null");
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L703-L722
```

### Dart

```dart
final docRef = db.collection("cities").doc("SF");
docRef.snapshots().listen(
  (event) {
    final source = (event.metadata.hasPendingWrites) ? "Local" : "Server";
    print("$source data: ${event.data()}");
  },
  onError: (error) => print("Listen failed: $error"),
);
https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L536-L544
```

##### Java

```java
# Not yet supported in the Java client library
```

##### Python

```python
// Not yet supported in Python client library
```

##### C++

```c++
DocumentReference doc_ref = db->Collection("cities").Document("SF");
doc_ref.AddSnapshotListener([](const DocumentSnapshot& snapshot,
                               Error error, const std::string& errorMsg) {
  if (error == Error::kErrorOk) {
    const char* source =
        snapshot.metadata().has_pending_writes() ? "Local" : "Server";
    if (snapshot.exists()) {
      std::cout << source << " data: " << snapshot.Get("name").string_value()
                << std::endl;
    } else {
      std::cout << source << " data: null" << std::endl;
    }
  } else {
    std::cout << "Listen failed: " << error << std::endl;
  }
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L647-L662
```

##### Node.js

```javascript
// Not yet supported in the Node.js client library
```

##### Go

```go
// Not yet supported in the Go client library
```

##### PHP

```php
// Not supported in the PHP client library
```

##### Unity

```c#
DocumentReference docRef = db.Collection("cities").Document("SF");
docRef.Listen(
  snapshot =>
  {
      string source = (snapshot != null && snapshot.Metadata.HasPendingWrites) ? "Local" : "Server";
      string snapshotData = "null";
      if (snapshot != null && snapshot.Exists)
      {
          System.Text.StringBuilder builder = new System.Text.StringBuilder();
          IDictionary<string, object> dict = snapshot.ToDictionary();
          foreach (var KVPair in dict)
          {
              builder.Append($"{KVPair.Key}: {KVPair.Value}\n");
          }
          snapshotData = builder.ToString();
      }
      Debug.Log($"{source} data: ${snapshotData}");
  });
```

##### C#

```c#
// Not yet supported in the C# client library
```

##### Ruby

```ruby
// Not yet supported in the Ruby client library
```

### Events for metadata changes

When listening for changes to a document, collection, or query, you can pass options to control the granularity of events that your listener will receive.

By default, listeners are not notified of changes that only affect metadata. Consider what happens when your app writes a new document:

1. A change event is immediately fired with the new data. The document has not yet been written to the backend so the "pending writes" flag is`true`.
2. The document is written to the backend.
3. The backend notifies the client of the successful write. There is no change to the document data, but there is a metadata change because the "pending writes" flag is now`false`.

If you want to receive snapshot events when the document or query metadata changes, pass a listen options object when attaching your listener.
**Note:** You can pass listener options as shown in the following samples. You can also use the configuration interfaces for snapshot options[described below](https://firebase.google.com/docs/firestore/query-data/listen#events-local-only)to explicitly configure events for metadata changes. For more information, see the reference documentation for[Kotlin + KTX Android](),[Java Android](),[Swift](),[Objective-C](), and[Web modular]().  

### Web

```javascript
import { doc, onSnapshot } from "firebase/firestore";

const unsub = onSnapshot(
  doc(db, "cities", "SF"), 
  { includeMetadataChanges: true }, 
  (doc) => {
    // ...
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/listen_with_metadata.js#L8-L15
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").doc("SF")
    .onSnapshot({
        // Listen for document metadata changes
        includeMetadataChanges: true
    }, (doc) => {
        // ...
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L654-L660
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Listen to document metadata.
db.collection("cities").document("SF")
  .addSnapshotListener(includeMetadataChanges: true) { documentSnapshot, error in
    // ...
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L804-L808
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Listen for metadata changes.
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"]
    addSnapshotListenerWithIncludeMetadataChanges:YES
                                         listener:^(FIRDocumentSnapshot *snapshot, NSError *error) {
   // ...
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L722-L727
```

### Kotlin

```kotlin
// Listen for metadata changes to the document.
val docRef = db.collection("cities").document("SF")
docRef.addSnapshotListener(MetadataChanges.INCLUDE) { snapshot, e ->
    // ...
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L567-L571
```

### Java

```java
// Listen for metadata changes to the document.
DocumentReference docRef = db.collection("cities").document("SF");
docRef.addSnapshotListener(MetadataChanges.INCLUDE, new EventListener<DocumentSnapshot>() {
    @Override
    public void onEvent(@Nullable DocumentSnapshot snapshot,
                        @Nullable FirebaseFirestoreException e) {
        // ...
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L728-L736
```

### Dart

```dart
final docRef = db.collection("cities").doc("SF");
docRef.snapshots(includeMetadataChanges: true).listen((event) {
  // ...
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L550-L553
```

##### Java

```java
// Not yet supported in the Java client library
```

##### Python

```python
// Not yet supported in Python client library
```

##### C++

```c++
DocumentReference doc_ref = db->Collection("cities").Document("SF");
doc_ref.AddSnapshotListener(
    MetadataChanges::kInclude,
    [](const DocumentSnapshot& snapshot, Error error, const std::string& errorMsg) { /* ... */ });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L690-L693
```

##### Node.js

```javascript
// Not yet supported the Node.js client library
```

##### Go

```go
// Not yet supported in the Go client library
```

##### PHP

```php
// Not supported in the PHP client library
```

##### Unity

```c#
DocumentReference docRef = db.Collection("cities").Document("SF");
docRef.Listen(MetadataChanges.Include, snapshot =>
{
    // ...
});
```

##### C#

```c#
// Not yet supported in the C# client library
```

##### Ruby

```ruby
// Not yet supported in the Ruby client library
```
| **Note:** If you just want to know when your write has completed, you can listen to the completion callback rather than using`hasPendingWrites`. In JavaScript, use the`Promise`returned from your write operation by attaching a`.then()`callback. In Swift, pass a completion callback to your write function.

### Configure listeners for local changes only

Cloud Firestoresnapshot listeners take an initial snapshot from the local cache and concurrently fetch corresponding data from the server.

In some cases, you may not want follow-up fetches from the server. Client SDKs allow you to configure listeners to fire only with respect to data in the local cache. This helps you avoid unnecessary server calls and their costs, and leverage the client-side cache, which reflects local data and mutations.

Here, snapshot options are set in client code to allow listening for local changes only.  
<br />

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from the namespaced API.  

```gdscript
const unsubscribe = onSnapshot(
   doc(db, "cities", "SF"),
    { 
      includeMetadataChanges: true,
      source:'cache'
     },
    (documentSnapshot) => {//...}
  );
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from the namespaced API.  

```scilab
// Not yet supported in the Web namespaced API
```

<br />

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Set up listener options
let options = SnapshotListenOptions()
    .withSource(ListenSource.cache)
    .withIncludeMetadataChanges(true)
db.collection("cities").document("SF")
  .addSnapshotListener(options: options) { documentSnapshot, error in
    // ...
  }
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Set up listener options
FIRSnapshotListenOptions *options = [[FIRSnapshotListenOptions alloc] init];
FIRSnapshotListenOptions *optionsWithSourceAndMetadata = 
                    [[options optionsWithIncludeMetadataChanges:YES] 
                      optionsWithSource:FIRListenSourceCache];
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"]
  addSnapshotListenerWithOptions:optionsWithSourceAndMetadata
  listener: ^ (FIRDocumentSnapshot * snapshot, NSError * error) {
    //...
  }
];
```

### Kotlin

```kotlin
// Set up listener options
val options = SnapshotListenOptions.Builder()
  .setMetadataChanges(MetadataChanges.INCLUDE)
  .setSource(ListenSource.CACHE)
  .build();
db.collection("cities").document("SF")
  .addSnapshotListener(options) { snapshot, error ->
    //...
  }
```

### Java

```java
// Set up listener options
SnapshotListenOptions options = new SnapshotListenOptions.Builder()
  .setMetadataChanges(MetadataChanges.INCLUDE)
  .setSource(ListenSource.CACHE)
  .build();
db.collection("cities").document("SF").addSnapshotListener(options, new EventListener<DocumentSnapshot>() {
    //...
  });
```

<br />

<br />

### Dart

```dart
// Not yet supported in this client library
```

<br />

##### Java

```java
# Not yet supported in the Java client library
```

##### Python

```python
// Not yet supported in Python client library
```

##### C++

```c++
// Not yet supported in the C++ client library
```

##### Node.js

```javascript
// Not yet supported in the Node.js client library
```

##### Go

```go
// Not yet supported in the Go client library
```

##### PHP

```php
// Not yet supported in the PHP client library
```

##### Unity

```c#
// Not yet supported in the Unity client library
```

##### C#

```c#
// Not yet supported in the C# client library
```

##### Ruby

```ruby
// Not yet supported in the Ruby client library
```

<br />

<br />

## Listen to multiple documents in a collection

As with documents, you can use`onSnapshot()`instead of`get()`to listen to the results of a query. This creates a query snapshot. For example, to listen to the documents with state`CA`:  

### Web

```javascript
import { collection, query, where, onSnapshot } from "firebase/firestore";

const q = query(collection(db, "cities"), where("state", "==", "CA"));
const unsubscribe = onSnapshot(q, (querySnapshot) => {
  const cities = [];
  querySnapshot.forEach((doc) => {
      cities.push(doc.data().name);
  });
  console.log("Current cities in CA: ", cities.join(", "));
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/listen_multiple.js#L8-L17
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").where("state", "==", "CA")
    .onSnapshot((querySnapshot) => {
        var cities = [];
        querySnapshot.forEach((doc) => {
            cities.push(doc.data().name);
        });
        console.log("Current cities in CA: ", cities.join(", "));
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L703-L710
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
db.collection("cities").whereField("state", isEqualTo: "CA")
  .addSnapshotListener { querySnapshot, error in
    guard let documents = querySnapshot?.documents else {
      print("Error fetching documents: \(error!)")
      return
    }
    let cities = documents.compactMap { $0["name"] }
    print("Current cities in CA: \(cities)")
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L854-L862
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[self.db collectionWithPath:@"cities"] queryWhereField:@"state" isEqualTo:@"CA"]
    addSnapshotListener:^(FIRQuerySnapshot *snapshot, NSError *error) {
      if (snapshot == nil) {
        NSLog(@"Error fetching documents: %@", error);
        return;
      }
      NSMutableArray *cities = [NSMutableArray array];
      for (FIRDocumentSnapshot *document in snapshot.documents) {
        [cities addObject:document.data[@"name"]];
      }
      NSLog(@"Current cities in CA: %@", cities);
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L778-L789
```

### Kotlin

```kotlin
db.collection("cities")
    .whereEqualTo("state", "CA")
    .addSnapshotListener { value, e ->
        if (e != null) {
            Log.w(TAG, "Listen failed.", e)
            return@addSnapshotListener
        }

        val cities = ArrayList<String>()
        for (doc in value!!) {
            doc.getString("name")?.let {
                cities.add(it)
            }
        }
        Log.d(TAG, "Current cites in CA: $cities")
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L625-L640
```

### Java

```java
db.collection("cities")
        .whereEqualTo("state", "CA")
        .addSnapshotListener(new EventListener<QuerySnapshot>() {
            @Override
            public void onEvent(@Nullable QuerySnapshot value,
                                @Nullable FirebaseFirestoreException e) {
                if (e != null) {
                    Log.w(TAG, "Listen failed.", e);
                    return;
                }

                List<String> cities = new ArrayList<>();
                for (QueryDocumentSnapshot doc : value) {
                    if (doc.get("name") != null) {
                        cities.add(doc.getString("name"));
                    }
                }
                Log.d(TAG, "Current cites in CA: " + cities);
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L802-L821
```

### Dart

```dart
db
    .collection("cities")
    .where("state", isEqualTo: "CA")
    .snapshots()
    .listen((event) {
  final cities = [];
  for (var doc in event.docs) {
    cities.add(doc.data()["name"]);
  }
  print("cities in CA: ${cities.join(", ")}");
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L559-L569
```

##### Java

    db.collection("cities")
        .whereEqualTo("state", "CA")
        .addSnapshotListener(
            new EventListener<QuerySnapshot>() {
              @Override
              public void onEvent(
                  @Nullable QuerySnapshot snapshots, @Nullable FirestoreException e) {
                if (e != null) {
                  System.err.println("Listen failed:" + e);
                  return;
                }

                List<String> cities = new ArrayList<>();
                for (DocumentSnapshot doc : snapshots) {
                  if (doc.get("name") != null) {
                    cities.add(doc.getString("name"));
                  }
                }
                System.out.println("Current cites in CA: " + cities);
              }
            });  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ListenDataSnippets.java#L85-L110

##### Python


    # Create an Event for notifying main thread.
    callback_done = threading.Event()

    # Create a callback on_snapshot function to capture changes
    def on_snapshot(col_snapshot, changes, read_time):
        print("Callback received query snapshot.")
        print("Current cities in California:")
        for doc in col_snapshot:
            print(f"{doc.id}")
        callback_done.set()

    col_query = db.collection("cities").where(filter=FieldFilter("state", "==", "CA"))

    # Watch the collection query
    query_watch = col_query.on_snapshot(on_snapshot)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L712-L728

##### C++

```c++
db->Collection("cities")
    .WhereEqualTo("state", FieldValue::String("CA"))
    .AddSnapshotListener([](const QuerySnapshot& snapshot, Error error, const std::string& errorMsg) {
      if (error == Error::kErrorOk) {
        std::vector<std::string> cities;
        std::cout << "Current cities in CA: " << error << std::endl;
        for (const DocumentSnapshot& doc : snapshot.documents()) {
          cities.push_back(doc.Get("name").string_value());
          std::cout << "" << cities.back() << std::endl;
        }
      } else {
        std::cout << "Listen failed: " << error << std::endl;
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L709-L722
```

##### Node.js

    const query = db.collection('cities').where('state', '==', 'CA');

    const observer = query.onSnapshot(querySnapshot => {
      console.log(`Received query snapshot of size ${querySnapshot.size}`);
      // ...
    }, err => {
      console.log(`Encountered error: ${err}`);
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L742-L752

##### Go

    import (
    	"context"
    	"fmt"
    	"io"
    	"time"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    )

    // listenMultiple listens to a query, returning the names of all cities
    // for a state.
    func listenMultiple(ctx context.Context, w io.Writer, projectID, collection string) error {
    	// projectID := "project-id"
    	ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    	defer cancel()

    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()

    	it := client.Collection(collection).Where("state", "==", "CA").Snapshots(ctx)
    	for {
    		snap, err := it.Next()
    		// DeadlineExceeded will be returned when ctx is cancelled.
    		if status.Code(err) == codes.DeadlineExceeded {
    			return nil
    		}
    		if err != nil {
    			return fmt.Errorf("Snapshots.Next: %w", err)
    		}
    		if snap != nil {
    			for {
    				doc, err := snap.Documents.Next()
    				if err == iterator.Done {
    					break
    				}
    				if err != nil {
    					return fmt.Errorf("Documents.Next: %w", err)
    				}
    				fmt.Fprintf(w, "Current cities in California: %v\n", doc.Ref.ID)
    			}
    		}
    	}
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/listen_multiple.go#L18-L67

##### PHP

```php
// Not supported in the PHP client library
```

##### Unity

```c#
Query query = db.Collection("cities").WhereEqualTo("State", "CA");

ListenerRegistration listener = query.Listen(snapshot => {
  Debug.Log("Callback received query snapshot.");
  Debug.Log("Current cities in California:");
  foreach (DocumentSnapshot documentSnapshot in snapshot.Documents) {
    Debug.Log(documentSnapshot.Id);
  }
});
```

##### C#

    CollectionReference citiesRef = db.Collection("cities");
    Query query = db.Collection("cities").WhereEqualTo("State", "CA");

    FirestoreChangeListener listener = query.Listen(snapshot =>
    {
        Console.WriteLine("Callback received query snapshot.");
        Console.WriteLine("Current cities in California:");
        foreach (DocumentSnapshot documentSnapshot in snapshot.Documents)
        {
            Console.WriteLine(documentSnapshot.Id);
        }
    });  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/ListenData/Program.cs#L81-L92

##### Ruby

    query = firestore.col(collection_path).where :state, :==, "CA"
    docs = []

    # Watch the collection query.
    listener = query.listen do |snapshot|
      puts "Callback received query snapshot."
      puts "Current cities in California:"
      snapshot.docs.each do |doc|
        puts doc.document_id
        docs << doc
      end
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/query_watch.rb#L146-L157

The snapshot handler will receive a new query snapshot every time the query results change (that is, when a document is added, removed, or modified).
| **Important:** As explained above under[Events for local changes](https://firebase.google.com/docs/firestore/query-data/listen#events-local-changes), you will receive events*immediately* for your local writes. Your listener can use the`metadata.hasPendingWrites`field on each document to determine whether the document has local changes that have not yet been written to the backend.

## View changes between snapshots

It is often useful to see the actual changes to query results between query snapshots, instead of simply using the entire query snapshot. For example, you may want to maintain a cache as individual documents are added, removed, and modified.  

### Web

```javascript
import { collection, query, where, onSnapshot } from "firebase/firestore";

const q = query(collection(db, "cities"), where("state", "==", "CA"));
const unsubscribe = onSnapshot(q, (snapshot) => {
  snapshot.docChanges().forEach((change) => {
    if (change.type === "added") {
        console.log("New city: ", change.doc.data());
    }
    if (change.type === "modified") {
        console.log("Modified city: ", change.doc.data());
    }
    if (change.type === "removed") {
        console.log("Removed city: ", change.doc.data());
    }
  });
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/listen_diffs.js#L8-L23
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities").where("state", "==", "CA")
    .onSnapshot((snapshot) => {
        snapshot.docChanges().forEach((change) => {
            if (change.type === "added") {
                console.log("New city: ", change.doc.data());
            }
            if (change.type === "modified") {
                console.log("Modified city: ", change.doc.data());
            }
            if (change.type === "removed") {
                console.log("Removed city: ", change.doc.data());
            }
        });
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L721-L734
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
db.collection("cities").whereField("state", isEqualTo: "CA")
  .addSnapshotListener { querySnapshot, error in
    guard let snapshot = querySnapshot else {
      print("Error fetching snapshots: \(error!)")
      return
    }
    snapshot.documentChanges.forEach { diff in
      if (diff.type == .added) {
        print("New city: \(diff.document.data())")
      }
      if (diff.type == .modified) {
        print("Modified city: \(diff.document.data())")
      }
      if (diff.type == .removed) {
        print("Removed city: \(diff.document.data())")
      }
    }
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L868-L885
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[self.db collectionWithPath:@"cities"] queryWhereField:@"state" isEqualTo:@"CA"]
    addSnapshotListener:^(FIRQuerySnapshot *snapshot, NSError *error) {
      if (snapshot == nil) {
        NSLog(@"Error fetching documents: %@", error);
        return;
      }
      for (FIRDocumentChange *diff in snapshot.documentChanges) {
        if (diff.type == FIRDocumentChangeTypeAdded) {
          NSLog(@"New city: %@", diff.document.data);
        }
        if (diff.type == FIRDocumentChangeTypeModified) {
          NSLog(@"Modified city: %@", diff.document.data);
        }
        if (diff.type == FIRDocumentChangeTypeRemoved) {
          NSLog(@"Removed city: %@", diff.document.data);
        }
      }
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L795-L812
```

### Kotlin

```kotlin
db.collection("cities")
    .whereEqualTo("state", "CA")
    .addSnapshotListener { snapshots, e ->
        if (e != null) {
            Log.w(TAG, "listen:error", e)
            return@addSnapshotListener
        }

        for (dc in snapshots!!.documentChanges) {
            when (dc.type) {
                DocumentChange.Type.ADDED -> Log.d(TAG, "New city: ${dc.document.data}")
                DocumentChange.Type.MODIFIED -> Log.d(TAG, "Modified city: ${dc.document.data}")
                DocumentChange.Type.REMOVED -> Log.d(TAG, "Removed city: ${dc.document.data}")
            }
        }
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L646-L661
```

### Java

```java
db.collection("cities")
        .whereEqualTo("state", "CA")
        .addSnapshotListener(new EventListener<QuerySnapshot>() {
            @Override
            public void onEvent(@Nullable QuerySnapshot snapshots,
                                @Nullable FirebaseFirestoreException e) {
                if (e != null) {
                    Log.w(TAG, "listen:error", e);
                    return;
                }

                for (DocumentChange dc : snapshots.getDocumentChanges()) {
                    switch (dc.getType()) {
                        case ADDED:
                            Log.d(TAG, "New city: " + dc.getDocument().getData());
                            break;
                        case MODIFIED:
                            Log.d(TAG, "Modified city: " + dc.getDocument().getData());
                            break;
                        case REMOVED:
                            Log.d(TAG, "Removed city: " + dc.getDocument().getData());
                            break;
                    }
                }

            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L827-L853
```

### Dart

```dart
db
    .collection("cities")
    .where("state", isEqualTo: "CA")
    .snapshots()
    .listen((event) {
  for (var change in event.docChanges) {
    switch (change.type) {
      case DocumentChangeType.added:
        print("New City: ${change.doc.data()}");
        break;
      case DocumentChangeType.modified:
        print("Modified City: ${change.doc.data()}");
        break;
      case DocumentChangeType.removed:
        print("Removed City: ${change.doc.data()}");
        break;
    }
  }
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L575-L593
```

##### Java

    db.collection("cities")
        .whereEqualTo("state", "CA")
        .addSnapshotListener(
            new EventListener<QuerySnapshot>() {
              @Override
              public void onEvent(
                  @Nullable QuerySnapshot snapshots, @Nullable FirestoreException e) {
                if (e != null) {
                  System.err.println("Listen failed: " + e);
                  return;
                }

                for (DocumentChange dc : snapshots.getDocumentChanges()) {
                  switch (dc.getType()) {
                    case ADDED:
                      System.out.println("New city: " + dc.getDocument().getData());
                      break;
                    case MODIFIED:
                      System.out.println("Modified city: " + dc.getDocument().getData());
                      break;
                    case REMOVED:
                      System.out.println("Removed city: " + dc.getDocument().getData());
                      break;
                    default:
                      break;
                  }
                }
              }
            });  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ListenDataSnippets.java#L121-L154

##### C++

```c++
db->Collection("cities")
    .WhereEqualTo("state", FieldValue::String("CA"))
    .AddSnapshotListener([](const QuerySnapshot& snapshot, Error error, const std::string& errorMsg) {
      if (error == Error::kErrorOk) {
        for (const DocumentChange& dc : snapshot.DocumentChanges()) {
          switch (dc.type()) {
            case DocumentChange::Type::kAdded:
              std::cout << "New city: "
                        << dc.document().Get("name").string_value() << std::endl;
              break;
            case DocumentChange::Type::kModified:
              std::cout << "Modified city: "
                        << dc.document().Get("name").string_value() << std::endl;
              break;
            case DocumentChange::Type::kRemoved:
              std::cout << "Removed city: "
                        << dc.document().Get("name").string_value() << std::endl;
              break;
          }
        }
      } else {
        std::cout << "Listen failed: " << error << std::endl;
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L741-L764
```

##### Python


    # Create an Event for notifying main thread.
    delete_done = threading.Event()

    # Create a callback on_snapshot function to capture changes
    def on_snapshot(col_snapshot, changes, read_time):
        print("Callback received query snapshot.")
        print("Current cities in California: ")
        for change in changes:
            if change.type.name == "ADDED":
                print(f"New city: {change.document.id}")
            elif change.type.name == "MODIFIED":
                print(f"Modified city: {change.document.id}")
            elif change.type.name == "REMOVED":
                print(f"Removed city: {change.document.id}")
                delete_done.set()

    col_query = db.collection("cities").where(filter=FieldFilter("state", "==", "CA"))

    # Watch the collection query
    query_watch = col_query.on_snapshot(on_snapshot)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L747-L768

##### Node.js

    const observer = db.collection('cities').where('state', '==', 'CA')
      .onSnapshot(querySnapshot => {
        querySnapshot.docChanges().forEach(change => {
          if (change.type === 'added') {
            console.log('New city: ', change.doc.data());
          }
          if (change.type === 'modified') {
            console.log('Modified city: ', change.doc.data());
          }
          if (change.type === 'removed') {
            console.log('Removed city: ', change.doc.data());
          }
        });
      });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L758-L775

##### Go

    import (
    	"context"
    	"fmt"
    	"io"
    	"time"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    )

    // listenChanges listens to a query, returning the list of document changes.
    func listenChanges(ctx context.Context, w io.Writer, projectID, collection string) error {
    	// projectID := "project-id"
    	ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    	defer cancel()

    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()

    	it := client.Collection(collection).Where("state", "==", "CA").Snapshots(ctx)
    	for {
    		snap, err := it.Next()
    		// DeadlineExceeded will be returned when ctx is cancelled.
    		if status.Code(err) == codes.DeadlineExceeded {
    			return nil
    		}
    		if err != nil {
    			return fmt.Errorf("Snapshots.Next: %w", err)
    		}
    		if snap != nil {
    			for _, change := range snap.Changes {
    				switch change.Kind {
    				case firestore.DocumentAdded:
    					fmt.Fprintf(w, "New city: %v\n", change.Doc.Data())
    				case firestore.DocumentModified:
    					fmt.Fprintf(w, "Modified city: %v\n", change.Doc.Data())
    				case firestore.DocumentRemoved:
    					fmt.Fprintf(w, "Removed city: %v\n", change.Doc.Data())
    				}
    			}
    		}
    	}
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/listen_changes.go#L18-L65

##### PHP

```php
// Not supported in the PHP client library
```

##### Unity

```c#
Query query = db.Collection("cities").WhereEqualTo("State", "CA");

ListenerRegistration listener = query.Listen(snapshot =>
{
    foreach (DocumentChange change in snapshot.GetChanges())
    {
        if (change.ChangeType == DocumentChange.Type.Added)
        {
            Debug.Log(String.Format("New city: {0}", change.Document.Id));
        }
        else if (change.ChangeType == DocumentChange.Type.Modified)
        {
            Debug.Log(String.Format("Modified city: {0}", change.Document.Id));
        }
        else if (change.ChangeType == DocumentChange.Type.Removed)
        {
            Debug.Log(String.Format("Removed city: {0}", change.Document.Id));
        }
    }
});
```

##### C#

    CollectionReference citiesRef = db.Collection("cities");
    Query query = db.Collection("cities").WhereEqualTo("State", "CA");

    FirestoreChangeListener listener = query.Listen(snapshot =>
    {
        foreach (DocumentChange change in snapshot.Changes)
        {
            if (change.ChangeType.ToString() == "Added")
            {
                Console.WriteLine("New city: {0}", change.Document.Id);
            }
            else if (change.ChangeType.ToString() == "Modified")
            {
                Console.WriteLine("Modified city: {0}", change.Document.Id);
            }
            else if (change.ChangeType.ToString() == "Removed")
            {
                Console.WriteLine("Removed city: {0}", change.Document.Id);
            }
        }
    });  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/ListenData/Program.cs#L118-L138

##### Ruby

    query = firestore.col(collection_path).where :state, :==, "CA"
    added = []
    modified = []
    removed = []

    # Watch the collection query.
    listener = query.listen do |snapshot|
      puts "Callback received query snapshot."
      puts "Current cities in California:"
      snapshot.changes.each do |change|
        if change.added?
          puts "New city: #{change.doc.document_id}"
          added << snapshot
        elsif change.modified?
          puts "Modified city: #{change.doc.document_id}"
          modified << snapshot
        elsif change.removed?
          puts "Removed city: #{change.doc.document_id}"
          removed << snapshot
        end
      end
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/query_watch.rb#L59-L80

| **Important:** The first query snapshot contains`added`events for all existing documents that match the query. This is because you're getting a set of changes that bring your query snapshot current with the initial state of the query. This allows you, for instance, to directly populate your UI from the changes you receive in the first query snapshot, without needing to add special logic for handling the initial state.

The initial state can come from the server directly, or from a local cache. If there is state available in a local cache, the query snapshot will be initially populated with the cached data, then updated with the server's data when the client has caught up with the server's state.

## Detach a listener

When you are no longer interested in listening to your data, you must detach your listener so that your event callbacks stop getting called. This allows the client to stop using bandwidth to receive updates. For example:  

### Web

```javascript
import { collection, onSnapshot } from "firebase/firestore";

const unsubscribe = onSnapshot(collection(db, "cities"), () => {
  // Respond to data
  // ...
});

// Later ...

// Stop listening to changes
unsubscribe();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/detach_listener.js#L8-L18
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var unsubscribe = db.collection("cities")
    .onSnapshot(() => {
      // Respond to data
      // ...
    });

// Later ...

// Stop listening to changes
unsubscribe();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L744-L753
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let listener = db.collection("cities").addSnapshotListener { querySnapshot, error in
  // ...
}

// ...

// Stop listening to changes
listener.remove()https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L912-L920
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
id<FIRListenerRegistration> listener = [[self.db collectionWithPath:@"cities"]
    addSnapshotListener:^(FIRQuerySnapshot *snapshot, NSError *error) {
      // ...
}];

// ...

// Stop listening to changes
[listener remove];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L838-L846
```

### Kotlin

```kotlin
val query = db.collection("cities")
val registration = query.addSnapshotListener { snapshots, e ->
    // ...
}

// ...

// Stop listening to changes
registration.remove()https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L690-L698
```

### Java

```java
Query query = db.collection("cities");
ListenerRegistration registration = query.addSnapshotListener(
        new EventListener<QuerySnapshot>() {
            // ...
        });

// ...

// Stop listening to changes
registration.remove();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L887-L902
```

### Dart

```dart
final collection = db.collection("cities");
final listener = collection.snapshots().listen((event) {
  // ...
});
listener.cancel();https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L599-L603
```

##### Java

    Query query = db.collection("cities");
    ListenerRegistration registration =
        query.addSnapshotListener(
            new EventListener<QuerySnapshot>() {
              // ...
            });

    // ...

    // Stop listening to changes
    registration.remove();  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ListenDataSnippets.java#L163-L178

##### Python

    # Terminate watch on a document
    doc_watch.unsubscribe()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L704-L705

##### C++

```c++
// Add a listener
Query query = db->Collection("cities");
ListenerRegistration registration = query.AddSnapshotListener(
    [](const QuerySnapshot& snapshot, Error error, const std::string& errorMsg) { /* ... */ });
// Stop listening to changes
registration.Remove();https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L779-L784
```

##### Node.js

    const unsub = db.collection('cities').onSnapshot(() => {
    });

    // ...

    // Stop listening for changes
    unsub();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L797-L803

##### Go

    // Ð¡ontext with timeout stops listening to changes.
    ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    defer cancel()  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/listen_document.go#L33-L35

##### PHP

```php
// Not supported in the PHP client library
```

##### Unity

```c#
listener.Stop();
```

##### C#

    await listener.StopAsync();  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/ListenData/Program.cs#L73-L73

##### Ruby

    listener.stop  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/query_watch.rb#L49-L49

## Handle listen errors

A listen may occasionally fail --- for example, due to security permissions, or if you tried to listen on an invalid query. (Learn more about[valid and invalid queries](https://firebase.google.com/docs/firestore/query-data/queries#compound_queries).) To handle these failures, you can provide an error callback when you attach your snapshot listener. After an error, the listener will not receive any more events, and there is no need to detach your listener.  

### Web

```javascript
import { collection, onSnapshot } from "firebase/firestore";

const unsubscribe = onSnapshot(
  collection(db, "cities"), 
  (snapshot) => {
    // ...
  },
  (error) => {
    // ...
  });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/handle_listen_errors.js#L8-L17
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
db.collection("cities")
    .onSnapshot((snapshot) => {
        // ...
    }, (error) => {
        // ...
    });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L760-L765
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
db.collection("cities")
  .addSnapshotListener { querySnapshot, error in
    if let error = error {
      print("Error retreiving collection: \(error)")
    }
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L926-L931
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[self.db collectionWithPath:@"cities"]
    addSnapshotListener:^(FIRQuerySnapshot *snapshot, NSError *error) {
      if (error != nil) {
        NSLog(@"Error retreving collection: %@", error);
      }
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L852-L857
```

### Kotlin

```kotlin
db.collection("cities")
    .addSnapshotListener { snapshots, e ->
        if (e != null) {
            Log.w(TAG, "listen:error", e)
            return@addSnapshotListener
        }

        for (dc in snapshots!!.documentChanges) {
            if (dc.type == DocumentChange.Type.ADDED) {
                Log.d(TAG, "New city: ${dc.document.data}")
            }
        }
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L704-L716
```

### Java

```java
db.collection("cities")
        .addSnapshotListener(new EventListener<QuerySnapshot>() {
            @Override
            public void onEvent(@Nullable QuerySnapshot snapshots,
                                @Nullable FirebaseFirestoreException e) {
                if (e != null) {
                    Log.w(TAG, "listen:error", e);
                    return;
                }

                for (DocumentChange dc : snapshots.getDocumentChanges()) {
                    if (dc.getType() == Type.ADDED) {
                        Log.d(TAG, "New city: " + dc.getDocument().getData());
                    }
                }

            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L908-L925
```

### Dart

```dart
final docRef = db.collection("cities");
docRef.snapshots().listen(
      (event) => print("listener attached"),
      onError: (error) => print("Listen failed: $error"),
    );https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L609-L613
```

##### Java

    db.collection("cities")
        .addSnapshotListener(
            new EventListener<QuerySnapshot>() {
              @Override
              public void onEvent(
                  @Nullable QuerySnapshot snapshots, @Nullable FirestoreException e) {
                if (e != null) {
                  System.err.println("Listen failed: " + e);
                  return;
                }

                for (DocumentChange dc : snapshots.getDocumentChanges()) {
                  if (dc.getType() == Type.ADDED) {
                    System.out.println("New city: " + dc.getDocument().getData());
                  }
                }
              }
            });  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/ListenDataSnippets.java#L185-L202

##### Python

```python
// Snippet coming soon
```

##### C++

```c++
// Snippet coming soon.
```

##### Node.js

    db.collection('cities')
      .onSnapshot((snapshot) => {
        //...
      }, (error) => {
        //...
      });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L809-L814

##### Go

    import (
    	"context"
    	"fmt"
    	"io"
    	"time"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    )

    // listenErrors demonstrates how to handle listening errors.
    func listenErrors(ctx context.Context, w io.Writer, projectID, collection string) error {
    	// projectID := "project-id"
    	ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    	defer cancel()

    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("firestore.NewClient: %w", err)
    	}
    	defer client.Close()

    	it := client.Collection(collection).Snapshots(ctx)
    	for {
    		snap, err := it.Next()
    		// Canceled will be returned when ctx is cancelled and DeadlineExceeded will
    		// be returned when ctx reaches its deadline.
    		if e := status.Code(err); e == codes.Canceled || e == codes.DeadlineExceeded {
    			return nil
    		}
    		if err != nil {
    			return fmt.Errorf("Snapshots.Next: %w", err)
    		}
    		if snap != nil {
    			for _, change := range snap.Changes {
    				if change.Kind == firestore.DocumentAdded {
    					fmt.Fprintf(w, "New city: %v\n", change.Doc.Data())
    				}
    			}
    		}
    	}
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/listen_errors.go#L18-L61

##### PHP

```php
// Not supported in the PHP client library
```

##### Unity

```c#
ListenerRegistration registration =
db.Collection("cities").Listen(
  querySnapshot =>
  {
      // ...
  });

registration.ListenerTask.ContinueWithOnMainThread(
    listenerTask =>
    {
        if (listenerTask.IsFaulted)
        {
            Debug.LogError($"Listen failed: {listenerTask.Exception}");
            // ...
            // Handle the listener error.
            // ...
        }
    });
```

##### C#

```c#
// Snippet coming soon
```

##### Ruby

    listener = firestore.col(collection_path).listen do |snapshot|
      snapshot.changes.each do |change|
        puts "New city: #{change.doc.document_id}" if change.added?
      end
    end

    # Register to be notified when unhandled errors occur.
    listener.on_error do |error|
      puts "Listen failed: #{error.message}"
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/query_watch.rb#L125-L134

## What's next

- [Combine listeners with simple and compound queries](https://firebase.google.com/docs/firestore/query-data/queries).
- [Order and limit the documents retrieved](https://firebase.google.com/docs/firestore/query-data/order-limit-data).
- [Understand billing for listeners](https://firebase.google.com/docs/firestore/pricing#operations).