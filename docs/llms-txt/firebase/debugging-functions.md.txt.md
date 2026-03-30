# Source: https://firebase.google.com/docs/firestore/pipelines/functions/debugging-functions.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## **Debugging Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/debugging-functions#exists` | Returns `TRUE` if the value is not an absent value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/debugging-functions#is_absent` | Returns `TRUE` if the value is an absent value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/debugging-functions#if_absent` | Replaces the value with an expression if it is absent |
| `https://firebase.google.com/docs/firestore/pipelines/functions/debugging-functions#is_error` | Catches and checks if an error has been thrown by the underlying expression |
| `https://firebase.google.com/docs/firestore/pipelines/functions/debugging-functions#if_error` | Replaces the value with an expression if it has thrown an error |

### EXISTS

**Syntax:**

    exists(value: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` is not the absent value.

**Examples:**

| `value` | `exists(value)` |
|---|---|
| 0L | `TRUE` |
| "foo" | `TRUE` |
| `NULL` | `TRUE` |
| `ABSENT` | `FALSE` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("rating").exists().as("hasRating"))
  .execute();
```

### Web

**Example:**

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("rating").exists().as("hasRating"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("rating").exists().as("hasRating")])
  .execute()
```

### Kotlin

**Example:**

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("rating").exists().alias("hasRating"))
    .execute()
```

### Java

**Example:**

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("rating").exists().alias("hasRating"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").exists().as_("hasRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(exists(field("rating")).as("hasRating"))
        .execute()
        .get();
```

### IS_ABSENT

**Syntax:**

    is_absent(value: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` is the absent value, and `FALSE` otherwise. Absent values
are values that are missing from the input, such as a missing document field.

**Examples:**

| `value` | `is_absent(value)` |
|---|---|
| 0L | `FALSE` |
| "foo" | `FALSE` |
| `NULL` | `FALSE` |
| `ABSENT` | `TRUE` |

### IF_ABSENT

**Syntax:**

    if_absent(value: ANY, replacement: ANY) -> ANY

**Description:**

If `value` is an absent value, evaluates and returns `replacement`. Otherwise returns `value`.

**Examples:**

| `value` | `replacement` | `if_absent(value, replacement)` |
|---|---|---|
| 5L | 0L | 5L |
| `NULL` | 0L | `NULL` |
| `ABSENT` | 0L | 0L |

### IS_ERROR

**Syntax:**

    is_error(try: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if an error is thrown during the evaluation of `try`. Returns `FALSE` otherwise.

### IF_ERROR

**Syntax:**

    if_error(try: ANY, catch: ANY) -> ANY

**Description:**

If an error is thrown during the evaluation of `try`, evaluates and returns `replacement`. Otherwise returns the resolved value of `try`.