# Source: https://firebase.google.com/docs/firestore/pipelines/functions/type-functions.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## **Type Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/type-functions#type` | Returns the type of the value as a `STRING`. |

### TYPE

**Syntax:**

    type(input: ANY) -> STRING

**Description:**

Returns a string representation of the `input` type.

If given an absent value, returns `NULL`.

**Examples:**

| `input` | `type(input)` |
|---|---|
| NULL | "null" |
| true | "boolean" |
| 1 | "int32" |
| -3L | "int64" |
| 3.14 | "float64" |
| 2024-01-01T00:00:00Z UTC | "timestamp" |
| "foo" | "string" |
| b"foo" | "bytes" |
| \[1, 2\] | "array" |
| {"a": 1} | "map" |
| `path("c/d")` | "reference" |
| `vector([1.0, 2.0])` | "vector" |
| ABSENT | NULL |

**Client examples**

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("title").notEqual("1984").as("not1984"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("title").notEqual("1984").as("not1984"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("title").notEqual("1984").as("not1984")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("title").notEqual("1984").alias("not1984"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("title").notEqual("1984").alias("not1984"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("title").not_equal("1984").as_("not1984"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(notEqual(field("title"), "1984").as("not1984"))
        .execute()
        .get();
```