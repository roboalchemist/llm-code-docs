# Source: https://firebase.google.com/docs/firestore/query-data/order-limit-data.md.txt

Cloud Firestore provides powerful query functionality for specifying which
documents you want to retrieve from a collection. These queries can also be used
with either `get()` or `addSnapshotListener()`, as described in [Get
Data](https://firebase.google.com/docs/firestore/query-data/get-data).

> [!NOTE]
> **Note:** While the code samples cover multiple languages, the text explaining the samples refers to the Web method names.

## Order and limit data

By default, a query retrieves all documents that satisfy the query in ascending
order by document ID. You can specify the sort order for your data using
`orderBy()`, and you can limit the number of documents retrieved using
`limit()`. If you specify a `limit()`, the value must be greater than or equal
to zero.

> [!NOTE]
> **Note:** An `orderBy()` clause also [filters for existence of the given field](https://firebase.google.com/docs/firestore/query-data/order-limit-data#orderby_and_existence). The result set will not include documents that do not contain the given field.

For example, you could query for the first 3 cities alphabetically
with:

### Web

```javascript
import { query, orderBy, limit } from "firebase/firestore";  

const q = query(citiesRef, orderBy("name"), limit(3));
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
citiesRef.orderBy("name").limit(3);
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
citiesRef.order(by: "name").limit(to: 3)
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
[[citiesRef queryOrderedByField:@"name"] queryLimitedTo:3];
```

### Kotlin

```kotlin
citiesRef.orderBy("name").limit(3)
```

### Java

```java
citiesRef.orderBy("name").limit(3);
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef.orderBy("name").limit(3);
```

##### Java

    Query query = cities.orderBy("name").limit(3);
    Query query = cities.orderBy("name").limitToLast(3);https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L264-L264

##### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name").limit_to_last(2)
    results = query.get()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L578-L580

### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name").limit_to_last(2)
    results = await query.get()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L563-L565

##### C++

```c++
cities_ref.OrderBy("name").Limit(3);
```

##### Node.js

    const firstThreeRes = await citiesRef.orderBy('name').limit(3).get();https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L688-L688

##### Go

    query := cities.OrderBy("name", firestore.Asc).Limit(3)
    query := cities.OrderBy("name", firestore.Asc).LimitToLast(3)https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/query.go#L155-L155

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $query = $citiesRef->orderBy('name')->limit(3);https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/query_order_limit.php#L41-L41

##### Unity

```c#
Query query = citiesRef.OrderBy("Name").Limit(3);
```

##### C#

    Query query = citiesRef.OrderBy("Name").Limit(3);https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/OrderLimitData/Program.cs#L44-L44

##### Ruby

    query = cities_ref.order("name").limit(3)https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/order_limit_data.rb#L25-L25

You could also sort in descending order to get the *last* 3 cities:

### Web

```javascript
import { query, orderBy, limit } from "firebase/firestore";  

const q = query(citiesRef, orderBy("name", "desc"), limit(3));
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
citiesRef.orderBy("name", "desc").limit(3);
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
citiesRef.order(by: "name", descending: true).limit(to: 3)
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
[[citiesRef queryOrderedByField:@"name" descending:YES] queryLimitedTo:3];
```

### Kotlin

```kotlin
citiesRef.orderBy("name", Query.Direction.DESCENDING).limit(3)
```

### Java

```java
citiesRef.orderBy("name", Direction.DESCENDING).limit(3);
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef.orderBy("name", descending: true).limit(3);
```

##### Java

    Query query = cities.orderBy("name", Direction.DESCENDING).limit(3);https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L290-L290

##### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L539-L541

### Python

    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L529-L531

##### C++

```c++
cities_ref.OrderBy("name", Query::Direction::kDescending).Limit(3);
```

##### Node.js

    const lastThreeRes = await citiesRef.orderBy('name', 'desc').limit(3).get();https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L692-L692

##### Go

    query := cities.OrderBy("name", firestore.Desc).Limit(3)https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/query.go#L164-L164

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $query = $citiesRef->orderBy('name', 'DESC')->limit(3);https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/query_order_desc_limit.php#L41-L41

##### Unity

```c#
Query query = citiesRef.OrderByDescending("Name").Limit(3);
```

##### C#

    Query query = citiesRef.OrderByDescending("Name").Limit(3);https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/OrderLimitData/Program.cs#L58-L58

##### Ruby

    query = cities_ref.order("name", "desc").limit(3)https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/order_limit_data.rb#L40-L40

You can also order by multiple fields. For example, if you wanted to order by
state, and within each state order by population in descending order:

### Web

```javascript
import { query, orderBy } from "firebase/firestore";  

const q = query(citiesRef, orderBy("state"), orderBy("population", "desc"));
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
citiesRef.orderBy("state").orderBy("population", "desc");
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
citiesRef
  .order(by: "state")
  .order(by: "population", descending: true)
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
[[citiesRef queryOrderedByField:@"state"] queryOrderedByField:@"population" descending:YES];
```

### Kotlin

```kotlin
citiesRef.orderBy("state").orderBy("population", Query.Direction.DESCENDING)
```

### Java

```java
citiesRef.orderBy("state").orderBy("population", Direction.DESCENDING);
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef.orderBy("state").orderBy("population", descending: true);
```

##### Java

    Query query = cities.orderBy("state").orderBy("population", Direction.DESCENDING);https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L277-L277

##### Python

    cities_ref = db.collection("cities")
    ordered_city_ref = cities_ref.order_by("state").order_by(
        "population", direction=firestore.Query.DESCENDING
    )https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L552-L555

### Python

    cities_ref = db.collection("cities")
    cities_ref.order_by("state").order_by(
        "population", direction=firestore.Query.DESCENDING
    )https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L539-L542

##### C++

```c++
cities_ref.OrderBy("state").OrderBy("name", Query::Direction::kDescending);
```

##### Node.js

    const byStateByPopRes = await citiesRef.orderBy('state').orderBy('population', 'desc').get();https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L696-L696

##### Go

    query := client.Collection("cities").OrderBy("state", firestore.Asc).OrderBy("population", firestore.Desc)https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/query.go#L172-L172

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $query = $citiesRef->orderBy('state')->orderBy('population', 'DESC');https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/query_order_multi.php#L41-L41

##### Unity

```c#
Query query = citiesRef.OrderBy("State").OrderByDescending("Population");
```

##### C#

    Query query = citiesRef.OrderBy("State").OrderByDescending("Population");https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/OrderLimitData/Program.cs#L72-L72

##### Ruby

    query = cities_ref.order("state").order("population", "desc")https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/order_limit_data.rb#L55-L55

You can combine `where()` filters with `orderBy()` and `limit()`. In the
following example, the queries define a population threshold, sort by population
in ascending order, and return only the first few results that exceed the
threshold:

### Web

```javascript
import { query, where, orderBy, limit } from "firebase/firestore";  

const q = query(citiesRef, where("population", ">", 100000), orderBy("population"), limit(2));
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
citiesRef.where("population", ">", 100000).orderBy("population").limit(2);
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
citiesRef
  .whereField("population", isGreaterThan: 100000)
  .order(by: "population")
  .limit(to: 2)
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
[[[citiesRef queryWhereField:@"population" isGreaterThan:@100000]
    queryOrderedByField:@"population"]
    queryLimitedTo:2];
```

### Kotlin

```kotlin
citiesRef.whereGreaterThan("population", 100000).orderBy("population").limit(2)
```

### Java

```java
citiesRef.whereGreaterThan("population", 100000).orderBy("population").limit(2);
```

### Dart

```dart
final citiesRef = db.collection("cities");
citiesRef
    .where("population", isGreaterThan: 100000)
    .orderBy("population")
    .limit(2);
```

##### Java

    Query query = cities.whereGreaterThan("population", 2500000L).orderBy("population").limit(2);https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L303-L303

##### Python

    cities_ref = db.collection("cities")
    query = (
        cities_ref.where(filter=FieldFilter("population", ">", 2500000))
        .order_by("population")
        .limit(2)
    )
    results = query.stream()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L563-L569

### Python

    cities_ref = db.collection("cities")
    query = (
        cities_ref.where(filter=FieldFilter("population", ">", 2500000))
        .order_by("population")
        .limit(2)
    )
    results = query.stream()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L549-L555

##### C++

```c++
cities_ref.WhereGreaterThan("population", FieldValue::Integer(100000))
    .OrderBy("population")
    .Limit(2);
```

##### Node.js

    const biggestRes = await citiesRef.where('population', '>', 2500000)
      .orderBy('population').limit(2).get();https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L700-L701

##### Go

    query := cities.Where("population", ">", 2500000).OrderBy("population", firestore.Desc).Limit(2)https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/query.go#L180-L180

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $query = $citiesRef
        ->where('population', '>', 2500000)
        ->orderBy('population')
        ->limit(2);https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/query_order_limit_field_valid.php#L41-L44

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
        .Limit(2);https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/OrderLimitData/Program.cs#L86-L89

##### Ruby

    query = cities_ref.where("population", ">", 2_500_000).order("population").limit(2)https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/order_limit_data.rb#L70-L70

However, if you have a filter with a range comparison (`<`, `<=`, `>`, `>=`),
your first ordering must be on the same field, see the list of `orderBy()`
limitations below.

## Limitations

Note the following restriction for `orderBy()` clauses:

- An `orderBy()` clause also [filters for existence of the given fields](https://firebase.google.com/docs/firestore/query-data/order-limit-data#orderby_and_existence). The result set will not include documents that do not contain the given fields.

## `orderBy` and existence

When you order a query by a given field, the query can return only the
documents where the order-by field exists.

For example, the following query would not return any documents where the
`population` field is not set, even if they otherwise meet the query filters.

##### Java

```java
db.collection("cities").whereEqualTo("country", "USA").orderBy("population");
```

A related effect applies to inequalities. A query with an inequality filter
on a field also implies ordering by that field. The following
query does not return documents without a `population` field even
if `country = USA` in that document . As a workaround, you can execute
separate queries for each ordering or you can assign a value for all fields
that you order by.

##### Java

```java
db.collection("cities").where(or("country", USA"), greaterThan("population", 250000));
```

The query above includes an implied order-by on the inequality and is
equivalent to the following:

##### Java

```java
db.collection("cities").where(or("country", USA"), greaterThan("population", 250000)).orderBy("population");
```