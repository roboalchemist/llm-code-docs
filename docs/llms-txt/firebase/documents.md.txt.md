# Source: https://firebase.google.com/docs/firestore/pipelines/stages/input/documents.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## Description

Returns documents by looking up a fixed set of predefined documents.

The stage must take one or more documents as input and cannot contain documents
with duplicate paths. If a referenced document does not exist, no
results will be produced for that document path.

This stage behaves similar to Firestore's `batchGet` and allows
filtering on the results directly rather than performing post-filtering steps
after the batch operation.

## Syntax

### Node.js

    const results = await db.pipeline()
      .documents(
        db.collection("cities").doc("SF"),
        db.collection("cities").doc("NY"))
      .execute();

## Client examples

### Web

```javascript
const results = await execute(db.pipeline()
  .documents([
    doc(db, "cities", "SF"),
    doc(db, "cities", "DC"),
    doc(db, "cities", "NY")
  ])
);
```

##### Swift

```swift
let results = try await db.pipeline()
  .documents([
    db.collection("cities").document("SF"),
    db.collection("cities").document("DC"),
    db.collection("cities").document("NY")
  ]).execute()
```

### Kotlin

```kotlin
val results = db.pipeline()
    .documents(
        db.collection("cities").document("SF"),
        db.collection("cities").document("DC"),
        db.collection("cities").document("NY")
    ).execute()
```

### Java

```java
Task<Pipeline.Snapshot> results = db.pipeline()
    .documents(
        db.collection("cities").document("SF"),
        db.collection("cities").document("DC"),
        db.collection("cities").document("NY")
    ).execute();
```

##### Python

```python
results = (
    client.pipeline()
    .documents(
        client.collection("cities").document("SF"),
        client.collection("cities").document("DC"),
        client.collection("cities").document("NY"),
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot results =
    firestore
        .pipeline()
        .documents(
            firestore.collection("cities").document("SF"),
            firestore.collection("cities").document("DC"),
            firestore.collection("cities").document("NY"))
        .execute()
        .get();
```

## Behavior

In order to use the `documents` stage, it must appear as the first stage
in the pipeline.

The order of documents returned from the `documents` stage is unstable and
shouldn't be relied upon. A subsequent sort stage can be used to obtain a
deterministic ordering.

For example, for the following documents:

### Node.js

    await db.collection('cities').doc('SF').set({name: 'San Francsico', state: 'California'});
    await db.collection('cities').doc('NYC').set({name: 'New York City', state: 'New York'});
    await db.collection('cities').doc('CHI').set({name: 'Chicago', state: 'Illinois'});

The `documents` stage can be used to retrieve only the `SF` and `NYC` documents
and then sort them in ascending order of name.

### Node.js

    const results = await db.pipeline()
      .documents(
        db.collection('cities').doc('SF'),
        db.collection('cities').doc('NYC'))
      .sort(field("name").ascending())
      .execute();

This query produces the following documents:

      {name: 'New York City', state: 'New York'}
      {name: 'San Francsico', state: 'California'}