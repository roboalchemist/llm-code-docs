# Source: https://firebase.google.com/docs/firestore/pipelines/functions/vector-functions.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## **Vector Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/vector-functions#cosine_distance` | Returns the cosine distance between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/vector-functions#dot_product` | Returns the dot product between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/vector-functions#euclidean_distance` | Returns the euclidean distance between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/vector-functions#manhattan_distance` | Returns the manhattan distance between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/vector-functions#vector_length` | Returns the number of elements in a vector |

### COSINE_DISTANCE

**Syntax:**

    cosine_distance(x: VECTOR, y: VECTOR) -> FLOAT64

**Description:**

Returns the cosine distance between `x` and `y`.

##### Node.js

```javascript
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").cosineDistance(sampleVector).as("cosineDistance")
  )
  .execute();
```

### Web

```javascript
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").cosineDistance(sampleVector).as("cosineDistance")));
```

##### Swift

```swift
let sampleVector = [0.0, 1, 2, 3, 4, 5]
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").cosineDistance(sampleVector).as("cosineDistance")
  ])
  .execute()
```

### Kotlin

```kotlin
val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").cosineDistance(sampleVector).alias("cosineDistance")
    )
    .execute()
```

### Java

```java
double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").cosineDistance(sampleVector).alias("cosineDistance")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.vector import Vector

sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("embedding").cosine_distance(sample_vector).as_("cosineDistance")
    )
    .execute()
)
```

##### Java

```java
double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(cosineDistance(field("embedding"), sampleVector).as("cosineDistance"))
        .execute()
        .get();
```

### DOT_PRODUCT

**Syntax:**

    dot_product(x: VECTOR, y: VECTOR) -> FLOAT64

**Description:**

Returns the dot product of `x` and `y`.

##### Node.js

```javascript
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").dotProduct(sampleVector).as("dotProduct")
  )
  .execute();
```

### Web

```javascript
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").dotProduct(sampleVector).as("dotProduct")
  )
);
```

##### Swift

```swift
let sampleVector = [0.0, 1, 2, 3, 4, 5]
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").dotProduct(sampleVector).as("dotProduct")
  ])
  .execute()
```

### Kotlin

```kotlin
val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").dotProduct(sampleVector).alias("dotProduct")
    )
    .execute()
```

### Java

```java
double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").dotProduct(sampleVector).alias("dotProduct")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.vector import Vector

sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("embedding").dot_product(sample_vector).as_("dotProduct"))
    .execute()
)
```

##### Java

```java
double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(dotProduct(field("embedding"), sampleVector).as("dotProduct"))
        .execute()
        .get();
```

### EUCLIDEAN_DISTANCE

**Syntax:**

    euclidean_distance(x: VECTOR, y: VECTOR) -> FLOAT64

**Description:**

Computes the euclidean distance between `x` and `y`.

##### Node.js

```javascript
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
  )
  .execute();
```

### Web

```javascript
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
  )
);
```

##### Swift

```swift
let sampleVector = [0.0, 1, 2, 3, 4, 5]
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
  ])
  .execute()
```

### Kotlin

```kotlin
val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").euclideanDistance(sampleVector).alias("euclideanDistance")
    )
    .execute()
```

### Java

```java
double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").euclideanDistance(sampleVector).alias("euclideanDistance")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.vector import Vector

sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("embedding")
        .euclidean_distance(sample_vector)
        .as_("euclideanDistance")
    )
    .execute()
)
```

##### Java

```java
double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(euclideanDistance(field("embedding"), sampleVector).as("euclideanDistance"))
        .execute()
        .get();
```

### MANHATTAN_DISTANCE

**Syntax:**

    manhattan_distance(x: VECTOR, y: VECTOR) -> FLOAT64

**Description:**

Computes the manhattan distance between `x` and `y`.

### VECTOR_LENGTH

**Syntax:**

    vector_length(vector: VECTOR) -> INT64

**Description:**

Returns the number of elements in a `VECTOR`.

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").vectorLength().as("vectorLength")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").vectorLength().as("vectorLength")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").vectorLength().as("vectorLength")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").vectorLength().alias("vectorLength")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").vectorLength().alias("vectorLength")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("embedding").vector_length().as_("vectorLength"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(vectorLength(field("embedding")).as("vectorLength"))
        .execute()
        .get();
```