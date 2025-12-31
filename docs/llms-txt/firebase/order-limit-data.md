# Source: https://firebase.google.com/docs/firestore/query-data/order-limit-data.md.txt

<br />

Cloud Firestoreprovides powerful query functionality for specifying which documents you want to retrieve from a collection. These queries can also be used with either`get()`or`addSnapshotListener()`, as described in[Get Data](https://firebase.google.com/docs/firestore/query-data/get-data).
| **Note:** While the code samples cover multiple languages, the text explaining the samples refers to the Web method names.

## Order and limit data

By default, a query retrieves all documents that satisfy the query in ascending order by document ID. You can specify the sort order for your data using`orderBy()`, and you can limit the number of documents retrieved using`limit()`. If you specify a`limit()`, the value must be greater than or equal to zero.
| **Note:** An`orderBy()`clause also[filters for existence of the given field](https://firebase.google.com/docs/firestore/query-data/order-limit-data#orderby_and_existence). The result set will not include documents that do not contain the given field.

For example, you could query for the first 3 cities alphabetically with:  

### Web

```javascript
import { query, orderBy, limit } from "firebase/firestore";  

const q = query(citiesRef, orderBy("name"), limit(3));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/order_and_limit.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
citiesRef.orderBy("name").limit(3);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L928-L928
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
citiesRef.order(by: "name").limit(to: 3)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1021-L1021
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[citiesRef queryOrderedByField:@"name"] queryLimitedTo:3];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L933-L933
```

### Kotlin

```kotlin
citiesRef.orderBy("name").limit(3)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L927-L927
```

### Java

```java
citiesRef.orderBy("name").limit(3);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1120-L1120
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef.orderBy("name").limit(3);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L957-L958
```

##### Java

    Query query = cities.orderBy("name").limit(3);
    Query query = cities.orderBy("name").limitToLast(3);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L264-L264

##### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name").limit_to_last(2)
    results = query.get()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L578-L580

### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name").limit_to_last(2)
    results = await query.get()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L563-L565

##### C++

```c++
cities_ref.OrderBy("name").Limit(3);https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1063-L1063
```

##### Node.js

    const firstThreeRes = await citiesRef.orderBy('name').limit(3).get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L688-L688

##### Go

    query := cities.OrderBy("name", firestore.Asc).Limit(3)
    query := cities.OrderBy("name", firestore.Asc).LimitToLast(3)  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L155-L155

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $query = $citiesRef->orderBy('name')->limit(3);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_order_limit.php#L41-L41

##### Unity

```c#
Query query = citiesRef.OrderBy("Name").Limit(3);
```

##### C#

    Query query = citiesRef.OrderBy("Name").Limit(3);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/OrderLimitData/Program.cs#L44-L44

##### Ruby

    query = cities_ref.order("name").limit(3)  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/order_limit_data.rb#L25-L25

You could also sort in descending order to get the*last*3 cities:  

### Web

```javascript
import { query, orderBy, limit } from "firebase/firestore";  

const q = query(citiesRef, orderBy("name", "desc"), limit(3));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/order_and_limit_desc.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
citiesRef.orderBy("name", "desc").limit(3);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L935-L935
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
citiesRef.order(by: "name", descending: true).limit(to: 3)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1029-L1029
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[citiesRef queryOrderedByField:@"name" descending:YES] queryLimitedTo:3];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L940-L940
```

### Kotlin

```kotlin
citiesRef.orderBy("name", Query.Direction.DESCENDING).limit(3)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L931-L931
```

### Java

```java
citiesRef.orderBy("name", Direction.DESCENDING).limit(3);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1124-L1124
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef.orderBy("name", descending: true).limit(3);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L964-L965
```

##### Java

    Query query = cities.orderBy("name", Direction.DESCENDING).limit(3);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L290-L290

##### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L539-L541

### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L529-L531

##### C++

```c++
cities_ref.OrderBy("name", Query::Direction::kDescending).Limit(3);https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1068-L1068
```

##### Node.js

    const lastThreeRes = await citiesRef.orderBy('name', 'desc').limit(3).get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L692-L692

##### Go

    query := cities.OrderBy("name", firestore.Desc).Limit(3)  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L164-L164

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $query = $citiesRef->orderBy('name', 'DESC')->limit(3);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_order_desc_limit.php#L41-L41

##### Unity

```c#
Query query = citiesRef.OrderByDescending("Name").Limit(3);
```

##### C#

    Query query = citiesRef.OrderByDescending("Name").Limit(3);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/OrderLimitData/Program.cs#L58-L58

##### Ruby

    query = cities_ref.order("name", "desc").limit(3)  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/order_limit_data.rb#L40-L40

You can also order by multiple fields. For example, if you wanted to order by state, and within each state order by population in descending order:  

### Web

```javascript
import { query, orderBy } from "firebase/firestore";  

const q = query(citiesRef, orderBy("state"), orderBy("population", "desc"));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/order_multiple.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
citiesRef.orderBy("state").orderBy("population", "desc");https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L942-L942
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
citiesRef
  .order(by: "state")
  .order(by: "population", descending: true)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1037-L1039
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[citiesRef queryOrderedByField:@"state"] queryOrderedByField:@"population" descending:YES];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L947-L947
```

### Kotlin

```kotlin
citiesRef.orderBy("state").orderBy("population", Query.Direction.DESCENDING)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L935-L935
```

### Java

```java
citiesRef.orderBy("state").orderBy("population", Direction.DESCENDING);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1128-L1128
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef.orderBy("state").orderBy("population", descending: true);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L971-L972
```

##### Java

    Query query = cities.orderBy("state").orderBy("population", Direction.DESCENDING);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L277-L277

##### Python

    cities_ref = db.collection("cities")
    ordered_city_ref = cities_ref.order_by("state").order_by(
        "population", direction=firestore.Query.DESCENDING
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L552-L555

### Python

    cities_ref = db.collection("cities")
    cities_ref.order_by("state").order_by(
        "population", direction=firestore.Query.DESCENDING
    )  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L539-L542

##### C++

```c++
cities_ref.OrderBy("state").OrderBy("name", Query::Direction::kDescending);https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1074-L1074
```

##### Node.js

    const byStateByPopRes = await citiesRef.orderBy('state').orderBy('population', 'desc').get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L696-L696

##### Go

    query := client.Collection("cities").OrderBy("state", firestore.Asc).OrderBy("population", firestore.Desc)  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L172-L172

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $query = $citiesRef->orderBy('state')->orderBy('population', 'DESC');  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_order_multi.php#L41-L41

##### Unity

```c#
Query query = citiesRef.OrderBy("State").OrderByDescending("Population");
```

##### C#

    Query query = citiesRef.OrderBy("State").OrderByDescending("Population");  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/OrderLimitData/Program.cs#L72-L72

##### Ruby

    query = cities_ref.order("state").order("population", "desc")  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/order_limit_data.rb#L55-L55

You can combine`where()`filters with`orderBy()`and`limit()`. In the following example, the queries define a population threshold, sort by population in ascending order, and return only the first few results that exceed the threshold:  

### Web

```javascript
import { query, where, orderBy, limit } from "firebase/firestore";  

const q = query(citiesRef, where("population", ">", 100000), orderBy("population"), limit(2));https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/filter_and_order.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
citiesRef.where("population", ">", 100000).orderBy("population").limit(2);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L949-L949
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
citiesRef
  .whereField("population", isGreaterThan: 100000)
  .order(by: "population")
  .limit(to: 2)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L1047-L1050
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
[[[citiesRef queryWhereField:@"population" isGreaterThan:@100000]
    queryOrderedByField:@"population"]
    queryLimitedTo:2];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L954-L956
```

### Kotlin

```kotlin
citiesRef.whereGreaterThan("population", 100000).orderBy("population").limit(2)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L939-L939
```

### Java

```java
citiesRef.whereGreaterThan("population", 100000).orderBy("population").limit(2);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1132-L1132
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef
    .where("population", isGreaterThan: 100000)
    .orderBy("population")
    .limit(2);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L978-L982
```

##### Java

    Query query = cities.whereGreaterThan("population", 2500000L).orderBy("population").limit(2);  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L303-L303

##### Python

    cities_ref = db.collection("cities")
    query = (
        cities_ref.where(filter=FieldFilter("population", ">", 2500000))
        .order_by("population")
        .limit(2)
    )
    results = query.stream()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L563-L569

### Python

    cities_ref = db.collection("cities")
    query = (
        cities_ref.where(filter=FieldFilter("population", ">", 2500000))
        .order_by("population")
        .limit(2)
    )
    results = query.stream()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L549-L555

##### C++

```c++
cities_ref.WhereGreaterThan("population", FieldValue::Integer(100000))
    .OrderBy("population")
    .Limit(2);https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1082-L1084
```

##### Node.js

    const biggestRes = await citiesRef.where('population', '>', 2500000)
      .orderBy('population').limit(2).get();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L700-L701

##### Go

    query := cities.Where("population", ">", 2500000).OrderBy("population", firestore.Desc).Limit(2)  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/query.go#L180-L180

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $query = $citiesRef
        ->where('population', '>', 2500000)
        ->orderBy('population')
        ->limit(2);  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/query_order_limit_field_valid.php#L41-L44

##### Unity

```c#
Query query = citiesRef
    .WhereGreaterThan("Population", 2500000)
    .OrderBy("Population")
    .Limit(2);
```

##### C#

    Query query = citiesRef
        .WhereGreaterThan("Population", 2500000)
        .OrderBy("Population")
        .Limit(2);  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/OrderLimitData/Program.cs#L86-L89

##### Ruby

    query = cities_ref.where("population", ">", 2_500_000).order("population").limit(2)  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/order_limit_data.rb#L70-L70

However, if you have a filter with a range comparison (`<`,`<=`,`>`,`>=`), your first ordering must be on the same field, see the list of`orderBy()`limitations below.

## Limitations

Note the following restriction for`orderBy()`clauses:

- An`orderBy()`clause also[filters for existence of the given fields](https://firebase.google.com/docs/firestore/query-data/order-limit-data#orderby_and_existence). The result set will not include documents that do not contain the given fields.

## `orderBy`and existence

When you order a query by a given field, the query can return only the documents where the order-by field exists.

For example, the following query would not return any documents where the`population`field is not set, even if they otherwise meet the query filters.  

##### Java

```java
db.collection("cities").whereEqualTo("country", "USA").orderBy("population");
```

A related effect applies to inequalities. A query with an inequality filter on a field also implies ordering by that field. The following query does not return documents without a`population`field even if`country = USA`in that document . As a workaround, you can execute separate queries for each ordering or you can assign a value for all fields that you order by.  

##### Java

```java
db.collection("cities").where(or("country", USA"), greaterThan("population", 250000));
```

The query above includes an implied order-by on the inequality and is equivalent to the following:  

##### Java

```java
db.collection("cities").where(or("country", USA"), greaterThan("population", 250000)).orderBy("population");
```