# Source: https://firebase.google.com/docs/firestore/pipelines/stages/transformation/union.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## Description

Merges the documents from another pipeline with those in the current pipeline.

## Syntax

### Node.js

    const results = await db.pipeline()
      .collection("cities/SF/restaurants")
      .union(db.pipeline().collection("cities/NYC/restaurants"))
      .execute();

## Client examples

##### Node.js

```javascript
  const results = await db.pipeline()
    .collection("cities/SF/restaurants")
    .where(eq("type", "chinese"))
    .union(db.pipeline()
      .collection("cities/NYC/restaurants")
      .where(eq("type", "italian")))
    .where(gte("rating", 4.5))
    .execute();
    
```

### Web

```javascript
const results = await execute(db.pipeline()
  .collection("cities/SF/restaurants")
  .where(field("type").equal("Chinese"))
  .union(db.pipeline()
    .collection("cities/NY/restaurants")
    .where(field("type").equal("Italian")))
  .where(field("rating").greaterThanOrEqual(4.5))
  .sort(field("__name__").descending())
);
```

##### Swift

```swift
let results = try await db.pipeline()
  .collection("cities/SF/restaurants")
  .where(Field("type").equal("Chinese"))
  .union(with: db.pipeline()
    .collection("cities/NY/restaurants")
    .where(Field("type").equal("Italian")))
  .where(Field("rating").greaterThanOrEqual(4.5))
  .sort([Field("__name__").descending()])
  .execute()
```

### Kotlin

```kotlin
val results = db.pipeline()
    .collection("cities/SF/restaurants")
    .where(field("type").equal("Chinese"))
    .union(db.pipeline()
        .collection("cities/NY/restaurants")
        .where(field("type").equal("Italian")))
    .where(field("rating").greaterThanOrEqual(4.5))
    .sort(field("__name__").descending())
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> results = db.pipeline()
    .collection("cities/SF/restaurants")
    .where(field("type").equal("Chinese"))
    .union(db.pipeline()
        .collection("cities/NY/restaurants")
        .where(field("type").equal("Italian")))
    .where(field("rating").greaterThanOrEqual(4.5))
    .sort(field("__name__").descending())
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

results = (
    client.pipeline()
    .collection("cities/SF/restaurants")
    .where(Field.of("type").equal("Chinese"))
    .union(
        client.pipeline()
        .collection("cities/NY/restaurants")
        .where(Field.of("type").equal("Italian"))
    )
    .where(Field.of("rating").greater_than_or_equal(4.5))
    .sort(Field.of("__name__").descending())
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot results =
    firestore
        .pipeline()
        .collection("cities/SF/restaurants")
        .where(field("type").equal("Chinese"))
        .union(
            firestore
                .pipeline()
                .collection("cities/NY/restaurants")
                .where(field("type").equal("Italian")))
        .where(field("rating").greaterThanOrEqual(4.5))
        .sort(descending(field("__name__")))
        .execute()
        .get();
```

## Behavior

This stage runs multiple pipelines in parallel and concatenates the results together.

### Non-Deterministic Order of Results

The order in which results are combined between the two pipelines is
non-deterministic. Any perceived order is unstable and shouldn't be relied upon. A following `sort` stage can be added if a stable order is required.

##### Node.js

```javascript
  const results = await db.pipeline()
    .collection("cities/SF/restaurants")
    .where(eq("type", "chinese"))
    .union(db.pipeline()
      .collection("cities/NYC/restaurants")
      .where(eq("type", "italian")))
    .where(gte("rating", 4.5))
    .sort(Field.of("__name__"))
    .execute();
    
```

### Kotlin

```kotlin
val results = db.pipeline()
    .collection("cities/SF/restaurants")
    .where(field("type").equal("Chinese"))
    .union(db.pipeline()
        .collection("cities/NY/restaurants")
        .where(field("type").equal("Italian")))
    .where(field("rating").greaterThanOrEqual(4.5))
    .sort(field("__name__").descending())
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> results = db.pipeline()
    .collection("cities/SF/restaurants")
    .where(field("type").equal("Chinese"))
    .union(db.pipeline()
        .collection("cities/NY/restaurants")
        .where(field("type").equal("Italian")))
    .where(field("rating").greaterThanOrEqual(4.5))
    .sort(field("__name__").descending())
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

results = (
    client.pipeline()
    .collection("cities/SF/restaurants")
    .where(Field.of("type").equal("Chinese"))
    .union(
        client.pipeline()
        .collection("cities/NY/restaurants")
        .where(Field.of("type").equal("Italian"))
    )
    .where(Field.of("rating").greater_than_or_equal(4.5))
    .sort(Field.of("__name__").descending())
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot results =
    firestore
        .pipeline()
        .collection("cities/SF/restaurants")
        .where(field("type").equal("Chinese"))
        .union(
            firestore
                .pipeline()
                .collection("cities/NY/restaurants")
                .where(field("type").equal("Italian")))
        .where(field("rating").greaterThanOrEqual(4.5))
        .sort(descending(field("__name__")))
        .execute()
        .get();
```

### Duplicate Results

The `union` stage does not deduplicate results. A following `distinct` or `aggregate` stage can be added if duplicate results need to be removed.