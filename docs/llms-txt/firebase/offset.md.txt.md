# Source: https://firebase.google.com/docs/firestore/pipelines/stages/transformation/offset.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## Description

Skips the first `N` input documents.

## Syntax

### Node.js

    const results = await db.pipeline()
      .collection("/cities")
      .offset(10)
      .execute();

## Client examples

##### Node.js

```javascript
const results = await db.pipeline()
  .collection("cities")
  .offset(10)
  .execute();
```

### Web

```javascript
const results = await execute(db.pipeline()
  .collection("cities")
  .offset(10));
```

##### Swift

```swift
let results = try await db.pipeline()
  .collection("cities")
  .offset(10)
  .execute()
```

### Kotlin

```kotlin
val results = db.pipeline()
    .collection("cities")
    .offset(10)
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> results = db.pipeline()
        .collection("cities")
        .offset(10)
        .execute();
```

##### Python

```python
results = client.pipeline().collection("cities").offset(10).execute()
```

##### Java

```java
Pipeline.Snapshot results =
    firestore.pipeline().collection("cities").offset(10).execute().get();
```

## Behavior

The `offset` stage will skip the first `N` input documents. Unless a `sort` stage is used before the offset, the order in which documents are returned is unstable and repeated executions might produce different results.