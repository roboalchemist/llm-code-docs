# Source: https://firebase.google.com/docs/firestore/pipelines/stages/transformation/limit.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## Description

Limits the number of documents returned by the pipeline.

## Syntax

### Node.js

    const results = await db.pipeline()
      .collection("/cities")
      .limit(10)
      .execute();

## Client examples

### Web

```javascript
const pipeline = db.pipeline()
  // Step 1: Start a query with collection scope
  .collection("cities")
  // Step 2: Filter the collection
  .where(field("population").greaterThan(100000))
  // Step 3: Sort the remaining documents
  .sort(field("name").ascending())
  // Step 4: Return the top 10. Note applying the limit earlier in the
  // pipeline would have unintentional results.
  .limit(10);
```

##### Swift

```swift
let pipeline = db.pipeline()
  // Step 1: Start a query with collection scope
  .collection("cities")
  // Step 2: Filter the collection
  .where(Field("population").greaterThan(100000))
  // Step 3: Sort the remaining documents
  .sort([Field("name").ascending()])
  // Step 4: Return the top 10. Note applying the limit earlier in the pipeline would have
  // unintentional results.
  .limit(10)
```

### Kotlin

```kotlin
val pipeline = db.pipeline()
    // Step 1: Start a query with collection scope
    .collection("cities")
    // Step 2: Filter the collection
    .where(field("population").greaterThan(100000))
    // Step 3: Sort the remaining documents
    .sort(field("name").ascending())
    // Step 4: Return the top 10. Note applying the limit earlier in the pipeline would have
    // unintentional results.
    .limit(10)
```

### Java

```java
Pipeline pipeline = db.pipeline()
    // Step 1: Start a query with collection scope
    .collection("cities")
    // Step 2: Filter the collection
    .where(field("population").greaterThan(100000))
    // Step 3: Sort the remaining documents
    .sort(field("name").ascending())
    // Step 4: Return the top 10. Note applying the limit earlier in the pipeline would have
    // unintentional results.
    .limit(10);
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

pipeline = (
    client.pipeline()
    .collection("cities")
    .where(Field.of("population").greater_than(100_000))
    .sort(Field.of("name").ascending())
    .limit(10)
)
```

##### Java

```java
Pipeline pipeline =
    firestore
        .pipeline()
        .collection("cities")
        .where(field("population").greaterThan(100_000))
        .sort(ascending(field("name")))
        .limit(10);
```

## Behavior

The `limit` stage will only return the first `N` documents. Unless a `sort` stage is used before the limit, the order in which documents are returned is unstable and repeated executions may produce different results.