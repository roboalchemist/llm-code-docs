# Source: https://firebase.google.com/docs/firestore/query-data/query-cursors.md.txt

<br />

With query cursors inCloud Firestore, you can split data returned by a query into batches according to the parameters you define in your query.

Query cursors define the start and end points for a query, allowing you to:

- Return a subset of the data.
- Paginate query results.

However, to define a specific range for a query, you should use the`where()`method described in[Simple Queries](https://firebase.google.com/docs/firestore/query-data/queries#simple_queries).

## Add a simple cursor to a query

Use the`startAt()`or`startAfter()`methods to define the start point for a query. The`startAt()`method includes the start point, while the`startAfter()`method excludes it.

For example, if you use`startAt(A)`in a query, it returns the entire alphabet. If you use`startAfter(A)`instead, it returns`B-Z`.  

### Web

```javascript
import { query, orderBy, startAt } from "firebase/firestore";  

const q = query(citiesRef, orderBy("population"), startAt(1000000));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/order_and_start.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
citiesRef.orderBy("population").startAt(1000000);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L972-L972
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Get all cities with population over one million, ordered by population.
db.collection("cities")
  .order(by: "population")
  .start(at: [1000000])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1169-L1172
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Get all cities with population over one million, ordered by population.
[[[db collectionWithPath:@"cities"]
    queryOrderedByField:@"population"]
    queryStartingAtValues:@[ @1000000 ]];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1073-L1076
```

### Kotlin

```kotlin
// Get all cities with a population >= 1,000,000, ordered by population,
db.collection("cities")
    .orderBy("population")
    .startAt(1000000)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L957-L960
```

### Java

```java
// Get all cities with a population >= 1,000,000, ordered by population,
db.collection("cities")
        .orderBy("population")
        .startAt(1000000);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1150-L1153
```

### Dart

```dart
db.collection("cities").orderBy("population").startAt([1000000]);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1002-L1002
```

##### Java

    Query query = cities.orderBy("population").startAt(4921000L);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L345-L345

##### Python

    cities_ref = db.collection("cities")
    query_start_at = cities_ref.order_by("population").start_at({"population": 1000000})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L617-L618

### Python

    cities_ref = db.collection("cities")
    query_start_at = cities_ref.order_by("population").start_at({"population": 1000000})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L597-L598

##### C++

```c++
// Get all cities with a population >= 1,000,000, ordered by population,
db->Collection("cities")
    .OrderBy("population")
    .StartAt({FieldValue::Integer(1000000)});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1119-L1122
```

##### Node.js

    const startAtRes = await db.collection('cities')
      .orderBy('population')
      .startAt(1000000)
      .get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L878-L881

##### Go

    query := client.Collection("cities").OrderBy("population", firestore.Asc).StartAt(1000000)  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L208-L208

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $query = $citiesRef
        ->orderBy('population')
        ->startAt([1000000]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_cursor_start_at_field_value_single.php#L41-L43

##### Unity

```c#
Query query = citiesRef.OrderBy("Population").StartAt(1000000);
```

##### C#

    Query query = citiesRef.OrderBy("Population").StartAt(1000000);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/PaginateData/Program.cs#L41-L41

##### Ruby

    query = cities_ref.order("population").start_at(1_000_000)  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/paginate_data.rb#L25-L25

Similarly, use the`endAt()`or`endBefore()`methods to define an end point for your query results.  

### Web

```javascript
import { query, orderBy, endAt } from "firebase/firestore";  

const q = query(citiesRef, orderBy("population"), endAt(1000000));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/order_and_end.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
citiesRef.orderBy("population").endAt(1000000);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L979-L979
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Get all cities with population less than one million, ordered by population.
db.collection("cities")
  .order(by: "population")
  .end(at: [1000000])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1176-L1179
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Get all cities with population less than one million, ordered by population.
[[[db collectionWithPath:@"cities"]
    queryOrderedByField:@"population"]
    queryEndingAtValues:@[ @1000000 ]];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1079-L1082
```

### Kotlin

```kotlin
// Get all cities with a population <= 1,000,000, ordered by population,
db.collection("cities")
    .orderBy("population")
    .endAt(1000000)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L964-L967
```

### Java

```java
// Get all cities with a population <= 1,000,000, ordered by population,
db.collection("cities")
        .orderBy("population")
        .endAt(1000000);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1157-L1160
```

### Dart

```dart
db.collection("cities").orderBy("population").endAt([1000000]);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1008-L1008
```

##### Java

    Query query = cities.orderBy("population").endAt(4921000L);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L358-L358

##### Python

    cities_ref = db.collection("cities")
    query_end_at = cities_ref.order_by("population").end_at({"population": 1000000})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L627-L628

### Python

    cities_ref = db.collection("cities")
    query_end_at = cities_ref.order_by("population").end_at({"population": 1000000})  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L607-L608

##### C++

```c++
// Get all cities with a population <= 1,000,000, ordered by population,
db->Collection("cities")
    .OrderBy("population")
    .EndAt({FieldValue::Integer(1000000)});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1128-L1131
```

##### Node.js

    const endAtRes = await db.collection('cities')
      .orderBy('population')
      .endAt(1000000)
      .get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L885-L888

##### Go

    query := client.Collection("cities").OrderBy("population", firestore.Asc).EndAt(1000000)  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L215-L215

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $query = $citiesRef
        ->orderBy('population')
        ->endAt([1000000]);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_cursor_end_at_field_value_single.php#L41-L43

##### Unity

```c#
Query query = citiesRef.OrderBy("Population").EndAt(1000000);
```

##### C#

    Query query = citiesRef.OrderBy("Population").EndAt(1000000);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/PaginateData/Program.cs#L55-L55

##### Ruby

    query = cities_ref.order("population").end_at(1_000_000)  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/paginate_data.rb#L40-L40

## Use a document snapshot to define the query cursor

You can also pass a document snapshot to the cursor clause as the start or end point of the query cursor. The values in the document snapshot serve as the values in the query cursor.

For example, take a snapshot of a "San Francisco" document in your data set of cities and populations. Then, use that document snapshot as the start point for your population query cursor. Your query will return all the cities with a population larger than or equal to San Francisco's, as defined in the document snapshot.  

### Web

```javascript
import { collection, doc, getDoc, query, orderBy, startAt } from "firebase/firestore";  
const citiesRef = collection(db, "cities");

const docSnap = await getDoc(doc(citiesRef, "SF"));

// Get all cities with a population bigger than San Francisco
const biggerThanSf = query(citiesRef, orderBy("population"), startAt(docSnap));
// ...  
https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/start_doc.js#L8-L15
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var citiesRef = db.collection("cities");

return citiesRef.doc("SF").get().then((doc) => {
    // Get all cities with a population bigger than San Francisco
    var biggerThanSf = citiesRef
        .orderBy("population")
        .startAt(doc);

    // ...
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L985-L994
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
db.collection("cities")
  .document("SF")
  .addSnapshotListener { (document, error) in
    guard let document = document else {
      print("Error retreving cities: \(error.debugDescription)")
      return
    }

    // Get all cities with a population greater than or equal to San Francisco.
    let sfSizeOrBigger = db.collection("cities")
      .order(by: "population")
      .start(atDocument: document)
  }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1187-L1199
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[db collectionWithPath:@"cities"] documentWithPath:@"SF"]
    addSnapshotListener:^(FIRDocumentSnapshot *snapshot, NSError *error) {
      if (snapshot == nil) {
        NSLog(@"Error retreiving cities: %@", error);
        return;
      }
      // Get all cities with a population greater than or equal to San Francisco.
      FIRQuery *sfSizeOrBigger = [[[db collectionWithPath:@"cities"]
          queryOrderedByField:@"population"]
          queryStartingAtDocument:snapshot];
    }];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1092-L1102
```

### Kotlin

```kotlin
// Get the data for "San Francisco"
db.collection("cities").document("SF")
    .get()
    .addOnSuccessListener { documentSnapshot ->
        // Get all cities with a population bigger than San Francisco.
        val biggerThanSf = db.collection("cities")
            .orderBy("population")
            .startAt(documentSnapshot)

        // ...
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L971-L981
```

### Java

```java
// Get the data for "San Francisco"
db.collection("cities").document("SF")
        .get()
        .addOnSuccessListener(new OnSuccessListener<DocumentSnapshot>() {
            @Override
            public void onSuccess(DocumentSnapshot documentSnapshot) {
                // Get all cities with a population bigger than San Francisco.
                Query biggerThanSf = db.collection("cities")
                        .orderBy("population")
                        .startAt(documentSnapshot);

                // ...
            }
        });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1164-L1177
```

### Dart

```dart
db.collection("cities").doc("SF").get().then(
  (documentSnapshot) {
    final biggerThanSf = db
        .collection("cities")
        .orderBy("population")
        .startAtDocument(documentSnapshot);
  },
  onError: (e) => print("Error: $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1014-L1022
```

##### Java

    // Fetch the snapshot with an API call, waiting for a maximum of 30 seconds for a result.
    ApiFuture<DocumentSnapshot> future = db.collection("cities").document("SF").get();
    DocumentSnapshot snapshot = future.get(30, TimeUnit.SECONDS);

    // Construct the query
    Query query = db.collection("cities").orderBy("population").startAt(snapshot);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L383-L388

##### Python

    doc_ref = db.collection("cities").document("SF")

    snapshot = doc_ref.get()
    start_at_snapshot = (
        db.collection("cities").order_by("population").start_at(snapshot)
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L637-L642

### Python

    doc_ref = db.collection("cities").document("SF")

    snapshot = await doc_ref.get()
    start_at_snapshot = (
        db.collection("cities").order_by("population").start_at(snapshot)
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L617-L622

##### C++

```c++
db->Collection("cities").Document("SF").Get().OnCompletion(
    [db](const Future<DocumentSnapshot>& future) {
      if (future.error() == Error::kErrorOk) {
        const DocumentSnapshot& document_snapshot = *future.result();
        Query bigger_than_sf = db->Collection("cities")
                                   .OrderBy("population")
                                   .StartAt({document_snapshot});
        // ...
      }
    });https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1152-L1161
```

##### Node.js

    const docRef = db.collection('cities').doc('SF');
    const snapshot = await docRef.get();
    const startAtSnapshot = db.collection('cities')
      .orderBy('population')
      .startAt(snapshot);

    await startAtSnapshot.limit(10).get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L894-L900

##### Go

    cities := client.Collection("cities")
    dsnap, err := cities.Doc("SF").Get(ctx)
    if err != nil {
    	fmt.Println(err)
    }
    query := cities.OrderBy("population", firestore.Asc).StartAt(dsnap.Data()["population"]).Documents(ctx)  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L303-L308

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $citiesRef = $db->collection('samples/php/cities');
    $docRef = $citiesRef->document('SF');
    $snapshot = $docRef->snapshot();

    $query = $citiesRef
        ->orderBy('population')
        ->startAt($snapshot);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_cursor_start_at_document.php#L40-L46

##### Unity

```c#
CollectionReference citiesRef = db.Collection("cities");
DocumentReference docRef = citiesRef.Document("SF");
docRef.GetSnapshotAsync().ContinueWith((snapshotTask) =>
{
    Query query = citiesRef.OrderBy("Population").StartAt(snapshotTask.Result);
});
```

##### C#

    CollectionReference citiesRef = db.Collection("cities");
    DocumentReference docRef = citiesRef.Document("SF");
    DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
    Query query = citiesRef.OrderBy("Population").StartAt(snapshot);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/PaginateData/Program.cs#L68-L71

##### Ruby

    doc_ref = firestore.doc "#{collection_path}/SF"
    snapshot = doc_ref.get
    query = cities_ref.order("population").start_at(snapshot)  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/paginate_data.rb#L102-L104

## Paginate a query

Paginate queries by combining query cursors with the`limit()`method. For example, use the last document in a batch as the start of a cursor for the next batch.  

### Web

```javascript
import { collection, query, orderBy, startAfter, limit, getDocs } from "firebase/firestore";  

// Query the first page of docs
const first = query(collection(db, "cities"), orderBy("population"), limit(25));
const documentSnapshots = await getDocs(first);

// Get the last visible document
const lastVisible = documentSnapshots.docs[documentSnapshots.docs.length-1];
console.log("last", lastVisible);

// Construct a new query starting at this document,
// get the next 25 cities.
const next = query(collection(db, "cities"),
    orderBy("population"),
    startAfter(lastVisible),
    limit(25));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/paginate.js#L8-L23
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var first = db.collection("cities")
        .orderBy("population")
        .limit(25);

return first.get().then((documentSnapshots) => {
  // Get the last visible document
  var lastVisible = documentSnapshots.docs[documentSnapshots.docs.length-1];
  console.log("last", lastVisible);

  // Construct a new query starting at this document,
  // get the next 25 cities.
  var next = db.collection("cities")
          .orderBy("population")
          .startAfter(lastVisible)
          .limit(25);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L1016-L1031
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Construct query for first 25 cities, ordered by population
let first = db.collection("cities")
  .order(by: "population")
  .limit(to: 25)

first.addSnapshotListener { (snapshot, error) in
  guard let snapshot = snapshot else {
    print("Error retreving cities: \(error.debugDescription)")
    return
  }

  guard let lastSnapshot = snapshot.documents.last else {
    // The collection is empty.
    return
  }

  // Construct a new query starting after this document,
  // retrieving the next 25 cities.
  let next = db.collection("cities")
    .order(by: "population")
    .start(afterDocument: lastSnapshot)

  // Use the query for pagination.
  // ...
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1207-L1231
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRQuery *first = [[[db collectionWithPath:@"cities"]
    queryOrderedByField:@"population"]
    queryLimitedTo:25];
[first addSnapshotListener:^(FIRQuerySnapshot *snapshot, NSError *error) {
  if (snapshot == nil) {
    NSLog(@"Error retreiving cities: %@", error);
    return;
  }
  if (snapshot.documents.count == 0) { return; }
  FIRDocumentSnapshot *lastSnapshot = snapshot.documents.lastObject;

  // Construct a new query starting after this document,
  // retreiving the next 25 cities.
  FIRQuery *next = [[[db collectionWithPath:@"cities"]
      queryOrderedByField:@"population"]
      queryStartingAfterDocument:lastSnapshot];
  // Use the query for pagination.
  // ...
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1110-L1128
```

### Kotlin

```kotlin
// Construct query for first 25 cities, ordered by population
val first = db.collection("cities")
    .orderBy("population")
    .limit(25)

first.get()
    .addOnSuccessListener { documentSnapshots ->
        // ...

        // Get the last visible document
        val lastVisible = documentSnapshots.documents[documentSnapshots.size() - 1]

        // Construct a new query starting at this document,
        // get the next 25 cities.
        val next = db.collection("cities")
            .orderBy("population")
            .startAfter(lastVisible)
            .limit(25)

        // Use the query for pagination
        // ...
    }https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L985-L1006
```

### Java

```java
// Construct query for first 25 cities, ordered by population
Query first = db.collection("cities")
        .orderBy("population")
        .limit(25);

first.get()
    .addOnSuccessListener(new OnSuccessListener<QuerySnapshot>() {
        @Override
        public void onSuccess(QuerySnapshot documentSnapshots) {
            // ...

            // Get the last visible document
            DocumentSnapshot lastVisible = documentSnapshots.getDocuments()
                    .get(documentSnapshots.size() -1);

            // Construct a new query starting at this document,
            // get the next 25 cities.
            Query next = db.collection("cities")
                    .orderBy("population")
                    .startAfter(lastVisible)
                    .limit(25);

            // Use the query for pagination
            // ...
        }
    });https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1181-L1206
```

### Dart

```dart
// Construct query for first 25 cities, ordered by population
final first = db.collection("cities").orderBy("population").limit(25);

first.get().then(
  (documentSnapshots) {
    // Get the last visible document
    final lastVisible = documentSnapshots.docs[documentSnapshots.size - 1];

    // Construct a new query starting at this document,
    // get the next 25 cities.
    final next = db
        .collection("cities")
        .orderBy("population")
        .startAfterDocument(lastVisible)
        .limit(25);

    // Use the query for pagination
    // ...
  },
  onError: (e) => print("Error completing: $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1028-L1048
```

##### Java

    // Construct query for first 25 cities, ordered by population.
    CollectionReference cities = db.collection("cities");
    Query firstPage = cities.orderBy("population").limit(25);

    // Wait for the results of the API call, waiting for a maximum of 30 seconds for a result.
    ApiFuture<QuerySnapshot> future = firstPage.get();
    List<QueryDocumentSnapshot> docs = future.get(30, TimeUnit.SECONDS).getDocuments();

    // Construct query for the next 25 cities.
    QueryDocumentSnapshot lastDoc = docs.get(docs.size() - 1);
    Query secondPage = cities.orderBy("population").startAfter(lastDoc).limit(25);

    future = secondPage.get();
    docs = future.get(30, TimeUnit.SECONDS).getDocuments();  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L396-L409

##### Python

    cities_ref = db.collection("cities")
    first_query = cities_ref.order_by("population").limit(3)

    # Get the last document from the results
    docs = first_query.stream()
    last_doc = list(docs)[-1]

    # Construct a new query starting at this document
    # Note: this will not have the desired effect if
    # multiple cities have the exact same population value
    last_pop = last_doc.to_dict()["population"]

    next_query = (
        cities_ref.order_by("population").start_after({"population": last_pop}).limit(3)
    )
    # Use the query for pagination
    # ...  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L651-L667

### Python

    cities_ref = db.collection("cities")
    first_query = cities_ref.order_by("population").limit(3)

    # Get the last document from the results
    docs = [d async for d in first_query.stream()]
    last_doc = list(docs)[-1]

    # Construct a new query starting at this document
    # Note: this will not have the desired effect if
    # multiple cities have the exact same population value
    last_pop = last_doc.to_dict()["population"]

    next_query = (
        cities_ref.order_by("population").start_after({"population": last_pop}).limit(3)
    )
    # Use the query for pagination
    # ...  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L634-L650

##### C++

```c++
// Construct query for first 25 cities, ordered by population
Query first = db->Collection("cities").OrderBy("population").Limit(25);

first.Get().OnCompletion([db](const Future<QuerySnapshot>& future) {
  if (future.error() != Error::kErrorOk) {
    // Handle error...
    return;
  }

  // Get the last visible document
  const QuerySnapshot& document_snapshots = *future.result();
  std::vector<DocumentSnapshot> documents = document_snapshots.documents();
  const DocumentSnapshot& last_visible = documents.back();

  // Construct a new query starting at this document,
  // get the next 25 cities.
  Query next = db->Collection("cities")
                   .OrderBy("population")
                   .StartAfter(last_visible)
                   .Limit(25);

  // Use the query for pagination
  // ...
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1178-L1201
```

##### Node.js

    const first = db.collection('cities')
      .orderBy('population')
      .limit(3);

    const snapshot = await first.get();

    // Get the last document
    const last = snapshot.docs[snapshot.docs.length - 1];

    // Construct a new query starting at this document.
    // Note: this will not have the desired effect if multiple
    // cities have the exact same population value.
    const next = db.collection('cities')
      .orderBy('population')
      .startAfter(last.data().population)
      .limit(3);

    // Use the query for pagination
    // ...  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L906-L927

##### Go

    cities := client.Collection("cities")

    // Get the first 25 cities, ordered by population.
    firstPage := cities.OrderBy("population", firestore.Asc).Limit(25).Documents(ctx)
    docs, err := firstPage.GetAll()
    if err != nil {
    	return err
    }

    // Get the last document.
    lastDoc := docs[len(docs)-1]

    // Construct a new query to get the next 25 cities.
    secondPage := cities.OrderBy("population", firestore.Asc).
    	StartAfter(lastDoc.Data()["population"]).
    	Limit(25)

    // ...  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L222-L239

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $citiesRef = $db->collection('samples/php/cities');
    $firstQuery = $citiesRef->orderBy('population')->limit(3);

    # Get the last document from the results
    $documents = $firstQuery->documents();
    $lastPopulation = 0;
    foreach ($documents as $document) {
        $lastPopulation = $document['population'];
    }

    # Construct a new query starting at this document
    # Note: this will not have the desired effect if multiple cities have the exact same population value
    $nextQuery = $citiesRef->orderBy('population')->startAfter([$lastPopulation]);
    $snapshot = $nextQuery->documents();  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_cursor_pagination.php#L40-L53

##### Unity

```c#
CollectionReference citiesRef = db.Collection("cities");
Query firstQuery = citiesRef.OrderBy("Population").Limit(3);

// Get the last document from the results
firstQuery.GetSnapshotAsync().ContinueWith((querySnapshotTask) =>
{
    long lastPopulation = 0;
    foreach (DocumentSnapshot documentSnapshot in querySnapshotTask.Result.Documents)
    {
        lastPopulation = documentSnapshot.GetValue<long>("Population");
    }

    // Construct a new query starting at this document.
    // Note: this will not have the desired effect if multiple cities have the exact same population value
    Query secondQuery = citiesRef.OrderBy("Population").StartAfter(lastPopulation);
    Task<QuerySnapshot> secondQuerySnapshot = secondQuery.GetSnapshotAsync();
```

##### C#

    CollectionReference citiesRef = db.Collection("cities");
    Query firstQuery = citiesRef.OrderBy("Population").Limit(3);

    // Get the last document from the results
    QuerySnapshot querySnapshot = await firstQuery.GetSnapshotAsync();
    long lastPopulation = 0;
    foreach (DocumentSnapshot documentSnapshot in querySnapshot.Documents)
    {
        lastPopulation = documentSnapshot.GetValue<long>("Population");
    }

    // Construct a new query starting at this document.
    // Note: this will not have the desired effect if multiple cities have the exact same population value
    Query secondQuery = citiesRef.OrderBy("Population").StartAfter(lastPopulation);
    QuerySnapshot secondQuerySnapshot = await secondQuery.GetSnapshotAsync();  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/PaginateData/Program.cs#L84-L98

##### Ruby

    cities_ref  = firestore.col collection_path
    first_query = cities_ref.order("population").limit(3)

    # Get the last document from the results.
    last_population = 0
    first_query.get do |city|
      last_population = city.data[:population]
    end

    # Construct a new query starting at this document.
    # Note: this will not have the desired effect if multiple cities have the exact same population value.
    second_query = cities_ref.order("population").start_after(last_population)
    second_query.get do |city|
      puts "Document #{city.document_id} returned by paginated query cursor."
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/paginate_data.rb#L54-L68

## Set cursor based on multiple fields

When using a cursor based on a field value (not a DocumentSnapshot), you can make the cursor position more precise by adding additional fields. This is particularly useful if your data set includes multiple documents that all have the same value for your cursor field, making the cursor's position ambiguous. You can add additional field values to your cursor to further specify the start or end point and reduce ambiguity.

For example, in a data set containing all the cities named "Springfield" in the United States, there would be multiple start points for a query set to start at "Springfield":

|           Cities           ||
|-------------|---------------|
| Name        | State         |
| Springfield | Massachusetts |
| Springfield | Missouri      |
| Springfield | Wisconsin     |

To start at a specific Springfield, you could add the state as a secondary condition in your cursor clause.  

### Web

```javascript
// Will return all Springfields
import { collection, query, orderBy, startAt } from "firebase/firestore";  
const q1 = query(collection(db, "cities"),
   orderBy("name"),
   orderBy("state"),
   startAt("Springfield"));

// Will return "Springfield, Missouri" and "Springfield, Wisconsin"
const q2 = query(collection(db, "cities"),
   orderBy("name"),
   orderBy("state"),
   startAt("Springfield", "Missouri"));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/start_multiple_orderby.js#L8-L19
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Will return all Springfields
db.collection("cities")
   .orderBy("name")
   .orderBy("state")
   .startAt("Springfield");

// Will return "Springfield, Missouri" and "Springfield, Wisconsin"
db.collection("cities")
   .orderBy("name")
   .orderBy("state")
   .startAt("Springfield", "Missouri");https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L1000-L1010
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Will return all Springfields
db.collection("cities")
  .order(by: "name")
  .order(by: "state")
  .start(at: ["Springfield"])

// Will return "Springfield, Missouri" and "Springfield, Wisconsin"
db.collection("cities")
  .order(by: "name")
  .order(by: "state")
  .start(at: ["Springfield", "Missouri"])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1239-L1249
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Will return all Springfields
[[[[db collectionWithPath:@"cities"]
    queryOrderedByField:@"name"]
    queryOrderedByField:@"state"]
    queryStartingAtValues:@[ @"Springfield" ]];
// Will return "Springfield, Missouri" and "Springfield, Wisconsin"
[[[[db collectionWithPath:@"cities"]
   queryOrderedByField:@"name"]
   queryOrderedByField:@"state"]
   queryStartingAtValues:@[ @"Springfield", @"Missouri" ]];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L1138-L1147
```

### Kotlin

```kotlin
// Will return all Springfields
db.collection("cities")
    .orderBy("name")
    .orderBy("state")
    .startAt("Springfield")

// Will return "Springfield, Missouri" and "Springfield, Wisconsin"
db.collection("cities")
    .orderBy("name")
    .orderBy("state")
    .startAt("Springfield", "Missouri")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1010-L1020
```

### Java

```java
// Will return all Springfields
db.collection("cities")
        .orderBy("name")
        .orderBy("state")
        .startAt("Springfield");

// Will return "Springfield, Missouri" and "Springfield, Wisconsin"
db.collection("cities")
        .orderBy("name")
        .orderBy("state")
        .startAt("Springfield", "Missouri");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1210-L1220
```

### Dart

```dart
// Will return all Springfields
db
    .collection("cities")
    .orderBy("name")
    .orderBy("state")
    .startAt(["Springfield"]);

// Will return "Springfield, Missouri" and "Springfield, Wisconsin"
db
    .collection("cities")
    .orderBy("name")
    .orderBy("state")
    .startAt(["Springfield", "Missouri"]);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L1054-L1066
```

##### Java

    // Will return all Springfields
    Query query1 = db.collection("cities").orderBy("name").orderBy("state").startAt("Springfield");

    // Will return "Springfield, Missouri" and "Springfield, Wisconsin"
    Query query2 =
        db.collection("cities").orderBy("name").orderBy("state").startAt("Springfield", "Missouri");  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L366-L371

##### Python

    start_at_name = (
        db.collection("cities").order_by("name").start_at({"name": "Springfield"})
    )

    start_at_name_and_state = (
        db.collection("cities")
        .order_by("name")
        .order_by("state")
        .start_at({"name": "Springfield", "state": "Missouri"})
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L808-L817

### Python

    start_at_name = (
        db.collection("cities")
        .order_by("name")
        .order_by("state")
        .start_at({"name": "Springfield"})
    )

    start_at_name_and_state = (
        db.collection("cities")
        .order_by("name")
        .order_by("state")
        .start_at({"name": "Springfield", "state": "Missouri"})
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L659-L671

##### C++

```c++
// This is not yet supported.
```

##### Node.js

    // Will return all Springfields
    const startAtNameRes = await db.collection('cities')
      .orderBy('name')
      .orderBy('state')
      .startAt('Springfield')
      .get();

    // Will return 'Springfield, Missouri' and 'Springfield, Wisconsin'
    const startAtNameAndStateRes = await db.collection('cities')
      .orderBy('name')
      .orderBy('state')
      .startAt('Springfield', 'Missouri')
      .get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L933-L945

##### Go

    // Will return all Springfields.
    client.Collection("cities").
    	OrderBy("name", firestore.Asc).
    	OrderBy("state", firestore.Asc).
    	StartAt("Springfield")

    // Will return Springfields where state comes after Wisconsin.
    client.Collection("cities").
    	OrderBy("name", firestore.Asc).
    	OrderBy("state", firestore.Asc).
    	StartAt("Springfield", "Wisconsin")  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L247-L257

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    // Will return all Springfields
    $query1 = $db
        ->collection('samples/php/cities')
        ->orderBy('name')
        ->orderBy('state')
        ->startAt(['Springfield']);

    // Will return "Springfield, Missouri" and "Springfield, Wisconsin"
    $query2 = $db
        ->collection('samples/php/cities')
        ->orderBy('name')
        ->orderBy('state')
        ->startAt(['Springfield', 'Missouri']);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_cursor_start_at_field_value_multi.php#L40-L52

##### Unity

```c#
Query query1 = db.Collection("cities").OrderBy("Name").OrderBy("State").StartAt("Springfield");
Query query2 = db.Collection("cities").OrderBy("Name").OrderBy("State").StartAt("Springfield", "Missouri");
```

##### C#

    Query query1 = db.Collection("cities").OrderBy("Name").OrderBy("State").StartAt("Springfield");
    Query query2 = db.Collection("cities").OrderBy("Name").OrderBy("State").StartAt("Springfield", "Missouri");  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/PaginateData/Program.cs#L110-L111

##### Ruby

    # Will return all Springfields
    query1 = firestore.col(collection_path).order("name").order("state").start_at("Springfield")

    # Will return "Springfield, Missouri" and "Springfield, Wisconsin"
    query2 = firestore.col(collection_path).order("name").order("state").start_at(["Springfield", "Missouri"])  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/paginate_data.rb#L80-L84