# Source: https://firebase.google.com/docs/firestore/pipelines/functions/all_functions.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## **Aggregate**

All aggregate functions can be used as top-level expressions in the
`aggregate(...)` stage.

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#count` | Returns the number of documents. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#count_if` | Returns the count of documents where an expression evaluates to `TRUE` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#count_distinct` | Returns the count of unique, non `NULL` values |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#sum` | Returns the sum of all `NUMERIC` values |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#average` | Returns the average of all `NUMERIC` values |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#minimum` | Returns the minimum non `NULL` value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#maximum` | Returns the maximum non `NULL` value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#first` | Returns the `expression` value for the first document. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#last` | Returns the `expression` value for the last document. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_agg` | Returns an array of all input values. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_agg_distinct` | Returns an array of all distinct input values. |

### COUNT

**Syntax:**

    count() -> INT64
    count(expression: ANY) -> INT64

**Description:**

Returns the count of documents from the previous stage where `expression`
evaluates to any non-`NULL` value. If no `expression` is provided, returns the
total count of documents from the previous stage.

##### Node.js

```javascript
// Total number of books in the collection
const countOfAll = await db.pipeline()
  .collection("books")
  .aggregate(countAll().as("count"))
  .execute();

// Number of books with nonnull `ratings` field
const countField = await db.pipeline()
  .collection("books")
  .aggregate(field("ratings").count().as("count"))
  .execute();
```

### Web

```javascript
// Total number of books in the collection
const countOfAll = await execute(db.pipeline()
  .collection("books")
  .aggregate(countAll().as("count"))
);

// Number of books with nonnull `ratings` field
const countField = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("ratings").count().as("count"))
);
```

##### Swift

```swift
// Total number of books in the collection
let countAll = try await db.pipeline()
  .collection("books")
  .aggregate([CountAll().as("count")])
  .execute()

// Number of books with nonnull `ratings` field
let countField = try await db.pipeline()
  .collection("books")
  .aggregate([Field("ratings").count().as("count")])
  .execute()
```

### Kotlin

```kotlin
// Total number of books in the collection
val countAll = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.countAll().alias("count"))
    .execute()

// Number of books with nonnull `ratings` field
val countField = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.count("ratings").alias("count"))
    .execute()
```

### Java

```java
// Total number of books in the collection
Task<Pipeline.Snapshot> countAll = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.countAll().alias("count"))
    .execute();

// Number of books with nonnull `ratings` field
Task<Pipeline.Snapshot> countField = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.count("ratings").alias("count"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Count

# Total number of books in the collection
count_all = (
    client.pipeline().collection("books").aggregate(Count().as_("count")).execute()
)

# Number of books with nonnull `ratings` field
count_field = (
    client.pipeline()
    .collection("books")
    .aggregate(Count("ratings").as_("count"))
    .execute()
)
```

##### Java

```java
// Total number of books in the collection
Pipeline.Snapshot countAll =
    firestore.pipeline().collection("books").aggregate(countAll().as("count")).execute().get();

// Number of books with nonnull `ratings` field
Pipeline.Snapshot countField =
    firestore
        .pipeline()
        .collection("books")
        .aggregate(count("ratings").as("count"))
        .execute()
        .get();
```

### COUNT_IF

**Syntax:**

    count_if(expression: BOOLEAN) -> INT64

**Description:**

Returns the number of documents from the previous stage where `expression`
evaluates to `TRUE`.

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .aggregate(
    field("rating").greaterThan(4).countIf().as("filteredCount")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(
    field("rating").greaterThan(4).countIf().as("filteredCount")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .aggregate([
    AggregateFunction("count_if", [Field("rating").greaterThan(4)]).as("filteredCount")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .aggregate(
        AggregateFunction.countIf(field("rating").greaterThan(4)).alias("filteredCount")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .aggregate(
        AggregateFunction.countIf(field("rating").greaterThan(4)).alias("filteredCount")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .aggregate(Field.of("rating").greater_than(4).count_if().as_("filteredCount"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .aggregate(countIf(field("rating").greaterThan(4)).as("filteredCount"))
        .execute()
        .get();
```

### COUNT_DISTINCT

**Syntax:**

    count_distinct(expression: ANY) -> INT64

**Description:**

Returns the number of unique non-`NULL`, non-`ABSENT` values of `expression`.

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .aggregate(field("author").countDistinct().as("unique_authors"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("author").countDistinct().as("unique_authors"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .aggregate([AggregateFunction("count_distinct", [Field("author")]).as("unique_authors")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.countDistinct("author").alias("unique_authors"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.countDistinct("author").alias("unique_authors"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .aggregate(Field.of("author").count_distinct().as_("unique_authors"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .aggregate(countDistinct("author").as("unique_authors"))
        .execute()
        .get();
```

### SUM

**Syntax:**

    sum(expression: ANY) -> NUMBER

**Description:**

Returns the sum for all numerical values, ignoring non-numeric values. Returns
`NaN` if any values are `NaN`.

The output will have the same type as the widest input type except in these cases:

- An `INTEGER` will be converted to a `DOUBLE` if it cannot be represented as an `INTEGER`.

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("cities")
  .aggregate(field("population").sum().as("totalPopulation"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("cities")
  .aggregate(field("population").sum().as("totalPopulation"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("cities")
  .aggregate([Field("population").sum().as("totalPopulation")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("cities")
    .aggregate(AggregateFunction.sum("population").alias("totalPopulation"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("cities")
    .aggregate(AggregateFunction.sum("population").alias("totalPopulation"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("cities")
    .aggregate(Field.of("population").sum().as_("totalPopulation"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("cities")
        .aggregate(sum("population").as("totalPopulation"))
        .execute()
        .get();
```

### AVERAGE

**Syntax:**

    average(expression: ANY) -> FLOAT64

**Description:**

Returns the average for all numerical values, ignoring non-numeric values.
Evaluates to `NaN` if any values are `NaN`, or `NULL` if no numerical values are
aggregated.

The output will have the same type as the input type except in these cases:

- An `INTEGER` will be converted to a `DOUBLE` if it cannot be represented as an `INTEGER`.

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("cities")
  .aggregate(field("population").average().as("averagePopulation"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("cities")
  .aggregate(field("population").average().as("averagePopulation"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("cities")
  .aggregate([Field("population").average().as("averagePopulation")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("cities")
    .aggregate(AggregateFunction.average("population").alias("averagePopulation"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("cities")
    .aggregate(AggregateFunction.average("population").alias("averagePopulation"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("cities")
    .aggregate(Field.of("population").average().as_("averagePopulation"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("cities")
        .aggregate(average("population").as("averagePopulation"))
        .execute()
        .get();
```

### MINIMUM

**Syntax:**

    minimum(expression: ANY) -> ANY

**Description:**

Returns the minimum non-`NULL`, non-absent value of the `expression` when evaluated on each document.

If there are no non-`NULL`, non-absent values, `NULL` is returned. This includes when no documents are considered.

If there are multiple minimum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://firebase.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .aggregate(field("price").minimum().as("minimumPrice"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("price").minimum().as("minimumPrice"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .aggregate([Field("price").minimum().as("minimumPrice")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.minimum("price").alias("minimumPrice"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.minimum("price").alias("minimumPrice"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .aggregate(Field.of("price").minimum().as_("minimumPrice"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .aggregate(minimum("price").as("minimumPrice"))
        .execute()
        .get();
```

### MAXIMUM

**Syntax:**

    maximum(expression: ANY) -> ANY

**Description:**

Returns the maximum non-`NULL`, non-absent value of the `expression` when evaluated on each document.

If there are no non-`NULL`, non-absent values, `NULL` is returned. This includes when no documents are considered.

If there are multiple maximum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://firebase.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .aggregate(field("price").maximum().as("maximumPrice"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("price").maximum().as("maximumPrice"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .aggregate([Field("price").maximum().as("maximumPrice")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.maximum("price").alias("maximumPrice"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .aggregate(AggregateFunction.maximum("price").alias("maximumPrice"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .aggregate(Field.of("price").maximum().as_("maximumPrice"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .aggregate(maximum("price").as("maximumPrice"))
        .execute()
        .get();
```

### FIRST

**Syntax:**

    first(expression: ANY) -> ANY

**Description:**

Returns the value of `expression` for the first returned document.

### LAST

**Syntax:**

    last(expression: ANY) -> ANY

**Description:**

Returns the value of `expression` for the last returned document.

### ARRAY_AGG

**Syntax:**

    array_agg(expression: ANY) -> ARRAY<ANY>

**Description:**

Returns an array containing all values of `expression` when evaluated on each document.

If the expression resolves to an absent value, it is converted to `NULL`.

The order of elements in the output array is not stable and shouldn't be relied upon.

### ARRAY_AGG_DISTINCT

**Syntax:**

    array_agg_distinct(expression: ANY) -> ARRAY<ANY>

**Description:**

Returns an array containing all distinct values of `expression` when evaluated on each document.

If the expression resolves to an absent value, it is converted to `NULL`.

The order of elements in the output array is not stable and shouldn't be relied upon.

## **Arithmetic Functions**

All arithmetic functions in Cloud Firestore have the following behaviors:

- Evaluates to `NULL` if any of the input parameters is `NULL`.
- Evaluates to `NaN` if any of the arguments is `NaN`.
- Generates an error if an overflow or underflow occurs.

Additionally, when an arithmetic function takes multiple numeric arguments of
different types (for example: `add(5.0, 6)`), Cloud Firestore implicitly
converts arguments to the widest input type. If only `INT32` inputs are provided, the return type will be `INT64`.

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#abs` | Returns the absolute value of a `number` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#add` | Returns the value of `x + y` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#subtract` | Returns the value of `x - y` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#multiply` | Returns the value of `x * y` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#divide` | Returns the value of `x / y` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#mod` | Returns the remainder of the division of `x / y` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#ceil` | Returns the ceiling of a `number` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#floor` | Returns the floor of a `number` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#round` | Rounds a `number` to `places` decimal places |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#pow` | Returns the value of `base^exponent` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#sqrt` | Returns the square root of a `number` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#exp` | Returns Euler's number raised to the power of `exponent` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#ln` | Returns the natural logarithm of a `number` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#log` | Returns the logarithm of a `number` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#log10` | Returns the logarithm of a `number` to base `10` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#rand` | Returns a pseudo-random floating point number |

### ABS

**Syntax:**

    abs[N <: INT32 | INT64 | FLOAT64](number: N) -> N

**Description:**

Returns the absolute value of a `number`.

- Throws an error when the function would overflow an `INT32` or `INT64` value.

**Examples:**

| number | `abs(number)` |
|---|---|
| 10 | 10 |
| -10 | 10 |
| 10L | 10L |
| -0.0 | 0.0 |
| 10.5 | 10.5 |
| -10.5 | 10.5 |
| -2^31^ | `[error]` |
| -2^63^ | `[error]` |

### ADD

**Syntax:**

    add[N <: INT32 | INT64 | FLOAT64](x: N, y: N) -> N

**Description:**

Returns the value of `x + y`.

**Examples:**

| x | y | `add(x, y)` |
|---|---|---|
| 20 | 3 | 23 |
| 10.0 | 1 | 11.0 |
| 22.5 | 2.0 | 24.5 |
| INT64.MAX | 1 | `[error]` |
| INT64.MIN | -1 | `[error]` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("soldBooks").add(field("unsoldBooks")).as("totalBooks"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("soldBooks").add(field("unsoldBooks")).as("totalBooks"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("soldBooks").add(Field("unsoldBooks")).as("totalBooks")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(Expression.add(field("soldBooks"), field("unsoldBooks")).alias("totalBooks"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(Expression.add(field("soldBooks"), field("unsoldBooks")).alias("totalBooks"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("soldBooks").add(Field.of("unsoldBooks")).as_("totalBooks"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(add(field("soldBooks"), field("unsoldBooks")).as("totalBooks"))
        .execute()
        .get();
```

### SUBTRACT

**Syntax:**

    subtract[N <: INT32 | INT64 | FLOAT64](x: N, y: N) -> N

**Description:**

Returns the value of `x - y`.

**Examples:**

| x | y | `subtract(x, y)` |
|---|---|---|
| 20 | 3 | 17 |
| 10.0 | 1 | 9.0 |
| 22.5 | 2.0 | 20.5 |
| INT64.MAX | -1 | `[error]` |
| INT64.MIN | 1 | `[error]` |

##### Node.js

```javascript
const storeCredit = 7;
const result = await db.pipeline()
  .collection("books")
  .select(field("price").subtract(constant(storeCredit)).as("totalCost"))
  .execute();
```

### Web

```javascript
const storeCredit = 7;
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("price").subtract(constant(storeCredit)).as("totalCost"))
);
```

##### Swift

```swift
let storeCredit = 7
let result = try await db.pipeline()
  .collection("books")
  .select([Field("price").subtract(Constant(storeCredit)).as("totalCost")])
  .execute()
```

### Kotlin

```kotlin
val storeCredit = 7
val result = db.pipeline()
    .collection("books")
    .select(Expression.subtract(field("price"), storeCredit).alias("totalCost"))
    .execute()
```

### Java

```java
int storeCredit = 7;
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(Expression.subtract(field("price"), storeCredit).alias("totalCost"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

store_credit = 7
result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("price").subtract(store_credit).as_("totalCost"))
    .execute()
)
```

##### Java

```java
int storeCredit = 7;
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(subtract(field("price"), storeCredit).as("totalCost"))
        .execute()
        .get();
```

### MULTIPLY

**Syntax:**

    multiply[N <: INT32 | INT64 | FLOAT64](x: N, y: N) -> N

**Description:**

Returns the value of `x * y`.

**Examples:**

| x | y | `multiply(x, y)` |
|---|---|---|
| 20 | 3 | 60 |
| 10.0 | 1 | 10.0 |
| 22.5 | 2.0 | 45.0 |
| INT64.MAX | 2 | `[error]` |
| INT64.MIN | 2 | `[error]` |
| FLOAT64.MAX | FLOAT64.MAX | `+inf` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("price").multiply(field("soldBooks")).as("revenue"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("price").multiply(field("soldBooks")).as("revenue"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("price").multiply(Field("soldBooks")).as("revenue")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(Expression.multiply(field("price"), field("soldBooks")).alias("revenue"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(Expression.multiply(field("price"), field("soldBooks")).alias("revenue"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("price").multiply(Field.of("soldBooks")).as_("revenue"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(multiply(field("price"), field("soldBooks")).as("revenue"))
        .execute()
        .get();
```

### DIVIDE

**Syntax:**

    divide[N <: INT32 | INT64 | FLOAT64](x: N, y: N) -> N

**Description:**

Returns the value of `x / y`. Integer division is truncated.

**Examples:**

| x | y | `divide(x, y)` |
|---|---|---|
| 20 | 3 | 6 |
| 10.0 | 3 | 3.333... |
| 22.5 | 2 | 11.25 |
| 10 | 0 | `[error]` |
| 1.0 | 0.0 | `+inf` |
| -1.0 | 0.0 | `-inf` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("ratings").divide(field("soldBooks")).as("reviewRate"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("ratings").divide(field("soldBooks")).as("reviewRate"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("ratings").divide(Field("soldBooks")).as("reviewRate")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(Expression.divide(field("ratings"), field("soldBooks")).alias("reviewRate"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(Expression.divide(field("ratings"), field("soldBooks")).alias("reviewRate"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("ratings").divide(Field.of("soldBooks")).as_("reviewRate"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(divide(field("ratings"), field("soldBooks")).as("reviewRate"))
        .execute()
        .get();
```

### MOD

**Syntax:**

    mod[N <: INT32 | INT64 | FLOAT64](x: N, y: N) -> N

**Description:**

Returns the remainder of `x / y`.

- Throws an `error` when `y` is zero for integer types (`INT64`).
- Returns `NaN` when `y` is zero for float types (`FLOAT64`).

**Examples:**

| x | y | `mod(x, y)` |
|---|---|---|
| 20 | 3 | 2 |
| -10 | 3 | -1 |
| 10 | -3 | 1 |
| -10 | -3 | -1 |
| 10 | 1 | 0 |
| 22.5 | 2 | 0.5 |
| 22.5 | 0.0 | `NaN` |
| 25 | 0 | `[error]` |

##### Node.js

```javascript
const displayCapacity = 1000;
const result = await db.pipeline()
  .collection("books")
  .select(field("unsoldBooks").mod(constant(displayCapacity)).as("warehousedBooks"))
  .execute();
```

### Web

```javascript
const displayCapacity = 1000;
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("unsoldBooks").mod(constant(displayCapacity)).as("warehousedBooks"))
);
```

##### Swift

```swift
let displayCapacity = 1000
let result = try await db.pipeline()
  .collection("books")
  .select([Field("unsoldBooks").mod(Constant(displayCapacity)).as("warehousedBooks")])
  .execute()
```

### Kotlin

```kotlin
val displayCapacity = 1000
val result = db.pipeline()
    .collection("books")
    .select(Expression.mod(field("unsoldBooks"), displayCapacity).alias("warehousedBooks"))
    .execute()
```

### Java

```java
int displayCapacity = 1000;
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(Expression.mod(field("unsoldBooks"), displayCapacity).alias("warehousedBooks"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

display_capacity = 1000
result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("unsoldBooks").mod(display_capacity).as_("warehousedBooks"))
    .execute()
)
```

##### Java

```java
int displayCapacity = 1000;
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(mod(field("unsoldBooks"), displayCapacity).as("warehousedBooks"))
        .execute()
        .get();
```

### CEIL

**Syntax:**

    ceil[N <: INT32 | INT64 | FLOAT64](number: N) -> N

**Description:**

Returns the smallest integer value that isn't less than `number`.

**Examples:**

| number | `ceil(number)` |
|---|---|
| 20 | 20 |
| 10 | 10 |
| 0 | 0 |
| 24L | 24L |
| -0.4 | -0.0 |
| 0.4 | 1.0 |
| 22.5 | 23.0 |
| `+inf` | `+inf` |
| `-inf` | `-inf` |

##### Node.js

```javascript
const booksPerShelf = 100;
const result = await db.pipeline()
  .collection("books")
  .select(
    field("unsoldBooks").divide(constant(booksPerShelf)).ceil().as("requiredShelves")
  )
  .execute();
```

### Web

```javascript
const booksPerShelf = 100;
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("unsoldBooks").divide(constant(booksPerShelf)).ceil().as("requiredShelves")
  )
);
```

##### Swift

```swift
let booksPerShelf = 100
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("unsoldBooks").divide(Constant(booksPerShelf)).ceil().as("requiredShelves")
  ])
  .execute()
```

### Kotlin

```kotlin
val booksPerShelf = 100
val result = db.pipeline()
    .collection("books")
    .select(
        Expression.divide(field("unsoldBooks"), booksPerShelf).ceil().alias("requiredShelves")
    )
    .execute()
```

### Java

```java
int booksPerShelf = 100;
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        Expression.divide(field("unsoldBooks"), booksPerShelf).ceil().alias("requiredShelves")
    )
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

books_per_shelf = 100
result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("unsoldBooks")
        .divide(books_per_shelf)
        .ceil()
        .as_("requiredShelves")
    )
    .execute()
)
```

##### Java

```java
int booksPerShelf = 100;
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(ceil(divide(field("unsoldBooks"), booksPerShelf)).as("requiredShelves"))
        .execute()
        .get();
```

### FLOOR

**Syntax:**

    floor[N <: INT32 | INT64 | FLOAT64](number: N) -> N

**Description:**

Returns the largest integer value that isn't greater than `number`.

**Examples:**

| number | `floor(number)` |
|---|---|
| 20 | 20 |
| 10 | 10 |
| 0 | 0 |
| 2147483648 | 2147483648 |
| -0.4 | -1.0 |
| 0.4 | 0.0 |
| 22.5 | 22.0 |
| `+inf` | `+inf` |
| `-inf` | `-inf` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .addFields(
    field("wordCount").divide(field("pages")).floor().as("wordsPerPage")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .addFields(
    field("wordCount").divide(field("pages")).floor().as("wordsPerPage")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .addFields([
    Field("wordCount").divide(Field("pages")).floor().as("wordsPerPage")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .addFields(
        Expression.divide(field("wordCount"), field("pages")).floor().alias("wordsPerPage")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .addFields(
        Expression.divide(field("wordCount"), field("pages")).floor().alias("wordsPerPage")
    )
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .add_fields(
        Field.of("wordCount").divide(Field.of("pages")).floor().as_("wordsPerPage")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .addFields(floor(divide(field("wordCount"), field("pages"))).as("wordsPerPage"))
        .execute()
        .get();
```

### ROUND

**Syntax:**

    round[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](number: N) -> N
    round[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](number: N, places: INT64) -> N

**Description:**

Rounds `places` digits off a `number`. Rounds digits from the right of the decimal point if `places` is positive, and to the left of the decimal point if it is negative.

- If only `number` is provided, rounds to the nearest whole value.
- Rounds away from zero in halfway cases.
- An `error` is thrown if rounding with a negative `places` value results in overflow.

**Examples:**

| number | places | `round(number, places)` |
|---|---|---|
| 15.5 | 0 | 16.0 |
| -15.5 | 0 | -16.0 |
| 15 | 1 | 15 |
| 15 | 0 | 15 |
| 15 | -1 | 20 |
| 15 | -2 | 0 |
| 15.48924 | 1 | 15.5 |
| 2^31^-1 | -1 | `[error]` |
| 2^63^-1L | -1 | `[error]` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("soldBooks").multiply(field("price")).round().as("partialRevenue"))
  .aggregate(field("partialRevenue").sum().as("totalRevenue"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("soldBooks").multiply(field("price")).round().as("partialRevenue"))
  .aggregate(field("partialRevenue").sum().as("totalRevenue"))
  );
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("soldBooks").multiply(Field("price")).round().as("partialRevenue")])
  .aggregate([Field("partialRevenue").sum().as("totalRevenue")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(Expression.multiply(field("soldBooks"), field("price")).round().alias("partialRevenue"))
    .aggregate(AggregateFunction.sum("partialRevenue").alias("totalRevenue"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(Expression.multiply(field("soldBooks"), field("price")).round().alias("partialRevenue"))
    .aggregate(AggregateFunction.sum("partialRevenue").alias("totalRevenue"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("soldBooks")
        .multiply(Field.of("price"))
        .round()
        .as_("partialRevenue")
    )
    .aggregate(Field.of("partialRevenue").sum().as_("totalRevenue"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(round(multiply(field("soldBooks"), field("price"))).as("partialRevenue"))
        .aggregate(sum("partialRevenue").as("totalRevenue"))
        .execute()
        .get();
```

### POW

**Syntax:**

    pow(base: FLOAT64, exponent: FLOAT64) -> FLOAT64

**Description:**

Returns the value `base` raised to the power of `exponent`.

- Throws an error if `base <= 0` and `exponent` is negative.

- For any `exponent`, `pow(1, exponent)` is 1.

- For any `base`, `pow(base, 0)` is 1.

**Examples:**

| base | exponent | `pow(base, exponent)` |
|---|---|---|
| 2 | 3 | 8.0 |
| 2 | -3 | 0.125 |
| `+inf` | 0 | 1.0 |
| 1 | `+inf` | 1.0 |
| -1 | 0.5 | `[error]` |
| 0 | -1 | `[error]` |

##### Node.js

```javascript
const googleplex = { latitude: 37.4221, longitude: 122.0853 };
const result = await db.pipeline()
  .collection("cities")
  .addFields(
    field("lat").subtract(constant(googleplex.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("latitudeDifference"),
    field("lng").subtract(constant(googleplex.longitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("longitudeDifference")
  )
  .select(
    field("latitudeDifference").add(field("longitudeDifference")).sqrt()
      // Inaccurate for large distances or close to poles
      .as("approximateDistanceToGoogle")
  )
  .execute();
```

### Web

```javascript
const googleplex = { latitude: 37.4221, longitude: 122.0853 };
const result = await execute(db.pipeline()
  .collection("cities")
  .addFields(
    field("lat").subtract(constant(googleplex.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("latitudeDifference"),
    field("lng").subtract(constant(googleplex.longitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("longitudeDifference")
  )
  .select(
    field("latitudeDifference").add(field("longitudeDifference")).sqrt()
      // Inaccurate for large distances or close to poles
      .as("approximateDistanceToGoogle")
  )
);
```

##### Swift

```swift
let googleplex = CLLocation(latitude: 37.4221, longitude: 122.0853)
let result = try await db.pipeline()
  .collection("cities")
  .addFields([
    Field("lat").subtract(Constant(googleplex.coordinate.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("latitudeDifference"),
    Field("lng").subtract(Constant(googleplex.coordinate.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("longitudeDifference")
  ])
  .select([
    Field("latitudeDifference").add(Field("longitudeDifference")).sqrt()
      // Inaccurate for large distances or close to poles
      .as("approximateDistanceToGoogle")
  ])
  .execute()
```

### Kotlin

```kotlin
val googleplex = GeoPoint(37.4221, -122.0853)
val result = db.pipeline()
    .collection("cities")
    .addFields(
        field("lat").subtract(googleplex.latitude)
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("latitudeDifference"),
        field("lng").subtract(googleplex.longitude)
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("longitudeDifference")
    )
    .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
            // Inaccurate for large distances or close to poles
            .alias("approximateDistanceToGoogle")
    )
    .execute()
```

### Java

```java
GeoPoint googleplex = new GeoPoint(37.4221, -122.0853);
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("cities")
    .addFields(
        field("lat").subtract(googleplex.getLatitude())
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("latitudeDifference"),
        field("lng").subtract(googleplex.getLongitude())
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("longitudeDifference")
    )
    .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
            // Inaccurate for large distances or close to poles
            .alias("approximateDistanceToGoogle")
    )
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

googleplexLat = 37.4221
googleplexLng = -122.0853
result = (
    client.pipeline()
    .collection("cities")
    .add_fields(
        Field.of("lat")
        .subtract(googleplexLat)
        .multiply(111)  # km per degree
        .pow(2)
        .as_("latitudeDifference"),
        Field.of("lng")
        .subtract(googleplexLng)
        .multiply(111)  # km per degree
        .pow(2)
        .as_("longitudeDifference"),
    )
    .select(
        Field.of("latitudeDifference")
        .add(Field.of("longitudeDifference"))
        .sqrt()
        # Inaccurate for large distances or close to poles
        .as_("approximateDistanceToGoogle")
    )
    .execute()
)
```

##### Java

```java
double googleplexLat = 37.4221;
double googleplexLng = -122.0853;
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("cities")
        .addFields(
            pow(multiply(subtract(field("lat"), googleplexLat), 111), 2)
                .as("latitudeDifference"),
            pow(multiply(subtract(field("lng"), googleplexLng), 111), 2)
                .as("longitudeDifference"))
        .select(
            sqrt(add(field("latitudeDifference"), field("longitudeDifference")))
                // Inaccurate for large distances or close to poles
                .as("approximateDistanceToGoogle"))
        .execute()
        .get();
```

### SQRT

**Syntax:**

    sqrt[N <: FLOAT64 | DECIMAL128](number: N) -> N

**Description:**

Returns the square root of a `number`.

- Throws an `error` if `number` is negative.

**Examples:**

| number | `sqrt(number)` |
|---|---|
| 25 | 5.0 |
| 12.002 | 3.464... |
| 0.0 | 0.0 |
| `NaN` | `NaN` |
| `+inf` | `+inf` |
| `-inf` | `[error]` |
| `x < 0` | `[error]` |

##### Node.js

```javascript
const googleplex = { latitude: 37.4221, longitude: 122.0853 };
const result = await db.pipeline()
  .collection("cities")
  .addFields(
    field("lat").subtract(constant(googleplex.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("latitudeDifference"),
    field("lng").subtract(constant(googleplex.longitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("longitudeDifference")
  )
  .select(
    field("latitudeDifference").add(field("longitudeDifference")).sqrt()
      // Inaccurate for large distances or close to poles
      .as("approximateDistanceToGoogle")
  )
  .execute();
```

### Web

```javascript
const googleplex = { latitude: 37.4221, longitude: 122.0853 };
const result = await execute(db.pipeline()
  .collection("cities")
  .addFields(
    field("lat").subtract(constant(googleplex.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("latitudeDifference"),
    field("lng").subtract(constant(googleplex.longitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("longitudeDifference")
  )
  .select(
    field("latitudeDifference").add(field("longitudeDifference")).sqrt()
      // Inaccurate for large distances or close to poles
      .as("approximateDistanceToGoogle")
  )
);
```

##### Swift

```swift
let googleplex = CLLocation(latitude: 37.4221, longitude: 122.0853)
let result = try await db.pipeline()
  .collection("cities")
  .addFields([
    Field("lat").subtract(Constant(googleplex.coordinate.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("latitudeDifference"),
    Field("lng").subtract(Constant(googleplex.coordinate.latitude))
      .multiply(111 /* km per degree */)
      .pow(2)
      .as("longitudeDifference")
  ])
  .select([
    Field("latitudeDifference").add(Field("longitudeDifference")).sqrt()
      // Inaccurate for large distances or close to poles
      .as("approximateDistanceToGoogle")
  ])
  .execute()
```

### Kotlin

```kotlin
val googleplex = GeoPoint(37.4221, -122.0853)
val result = db.pipeline()
    .collection("cities")
    .addFields(
        field("lat").subtract(googleplex.latitude)
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("latitudeDifference"),
        field("lng").subtract(googleplex.longitude)
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("longitudeDifference")
    )
    .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
            // Inaccurate for large distances or close to poles
            .alias("approximateDistanceToGoogle")
    )
    .execute()
```

### Java

```java
GeoPoint googleplex = new GeoPoint(37.4221, -122.0853);
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("cities")
    .addFields(
        field("lat").subtract(googleplex.getLatitude())
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("latitudeDifference"),
        field("lng").subtract(googleplex.getLongitude())
            .multiply(111 /* km per degree */)
            .pow(2)
            .alias("longitudeDifference")
    )
    .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
            // Inaccurate for large distances or close to poles
            .alias("approximateDistanceToGoogle")
    )
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

googleplexLat = 37.4221
googleplexLng = -122.0853
result = (
    client.pipeline()
    .collection("cities")
    .add_fields(
        Field.of("lat")
        .subtract(googleplexLat)
        .multiply(111)  # km per degree
        .pow(2)
        .as_("latitudeDifference"),
        Field.of("lng")
        .subtract(googleplexLng)
        .multiply(111)  # km per degree
        .pow(2)
        .as_("longitudeDifference"),
    )
    .select(
        Field.of("latitudeDifference")
        .add(Field.of("longitudeDifference"))
        .sqrt()
        # Inaccurate for large distances or close to poles
        .as_("approximateDistanceToGoogle")
    )
    .execute()
)
```

##### Java

```java
double googleplexLat = 37.4221;
double googleplexLng = -122.0853;
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("cities")
        .addFields(
            pow(multiply(subtract(field("lat"), googleplexLat), 111), 2)
                .as("latitudeDifference"),
            pow(multiply(subtract(field("lng"), googleplexLng), 111), 2)
                .as("longitudeDifference"))
        .select(
            sqrt(add(field("latitudeDifference"), field("longitudeDifference")))
                // Inaccurate for large distances or close to poles
                .as("approximateDistanceToGoogle"))
        .execute()
        .get();
```

### EXP

**Syntax:**

    exp(exponent: FLOAT64) -> FLOAT64

**Description:**

Returns the value of Euler's number raised to the power of `exponent`, also called the natural exponential function.

**Examples:**

| exponent | `exp(exponent)` |
|---|---|
| 0.0 | 1.0 |
| 10 | `e^10` (`FLOAT64`) |
| `+inf` | `+inf` |
| `-inf` | 0 |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("rating").exp().as("expRating"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("rating").exp().as("expRating"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("rating").exp().as("expRating")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("rating").exp().alias("expRating"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("rating").exp().alias("expRating"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").exp().as_("expRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(exp(field("rating")).as("expRating"))
        .execute()
        .get();
```

### LN

**Syntax:**

    ln(number: FLOAT64) -> FLOAT64

**Description:**

Returns the natural logarithm of `number`. This function is equivalent to `log(number)`.

**Examples:**

| number | `ln(number)` |
|---|---|
| 1 | 0.0 |
| 2L | 0.693... |
| 1.0 | 0.0 |
| `e` (`FLOAT64`) | 1.0 |
| `-inf` | `NaN` |
| `+inf` | `+inf` |
| `x <= 0` | `[error]` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("rating").ln().as("lnRating"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("rating").ln().as("lnRating"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("rating").ln().as("lnRating")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("rating").ln().alias("lnRating"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("rating").ln().alias("lnRating"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").ln().as_("lnRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(ln(field("rating")).as("lnRating"))
        .execute()
        .get();
```

### LOG

**Syntax:**

    log(number: FLOAT64, base: FLOAT64) -> FLOAT64
    log(number: FLOAT64) -> FLOAT64

**Description:**

Returns the logarithm of a `number` to `base`.

- If only `number` is provided, returns the logarithm of `number` to `base` (synonymous to `ln(number)`).

**Examples:**

| number | base | `log(number, base)` |
|---|---|---|
| 100 | 10 | 2.0 |
| `-inf` | `Numeric` | `NaN` |
| `Numeric`. | `+inf` | `NaN` |
| `number <= 0` | `Numeric` | `[error]` |
| `Numeric` | `base <= 0` | `[error]` |
| `Numeric` | 1.0 | `[error]` |

### LOG10

**Syntax:**

    log10(x: FLOAT64) -> FLOAT64

**Description:**

Returns the logarithm of a `number` to base `10`.

**Examples:**

| number | `log10(number)` |
|---|---|
| 100 | 2.0 |
| `-inf` | `NaN` |
| `+inf` | `+inf` |
| `x <= 0` | `[error]` |

### RAND

**Syntax:**

    rand() -> FLOAT64

**Description:**

Return a pseudo-random floating point number, chosen uniformly between `0.0` (inclusive) and `1.0` (exclusive).

## **Array Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array` | Returns an `ARRAY` containing one element for each input argument |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_concat` | Concatenates multiple arrays into a single `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_contains` | Returns `TRUE` if a given `ARRAY` contains a particular value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_contains_all` | Returns `TRUE` if all values are present in the `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_contains_any` | Returns `TRUE` if any of the values are present in the `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_first` | Returns the first element in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_first_n` | Returns the first `n` elements in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_get` | Returns the element at a given index in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_index_of` | Returns the index of the first occurrence of a value in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_index_of_all` | Returns all indexes of a value in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_length` | Returns the number of elements in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_last` | Returns the last element in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_last_n` | Returns the last `n` elements in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_reverse` | Reverses the order of elements in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#array_slice` | Returns a slice of an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#maximum` | Returns the maximum value in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#maximum_n` | Returns the `n` largest values in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#minimum` | Returns the minimum value in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#minimum_n` | Returns the `n` smallest values in an `ARRAY` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#sum` | Returns the sum of all `NUMERIC` values in an `ARRAY`. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#join` | Produces a concatenation of the elements in an `ARRAY` as a `STRING` value. |

### ARRAY

**Syntax:**

    array(values: ANY...) -> ARRAY

**Description:**

Constructs an array from the given elements.

- If an argument does not exist, it is replaced with `NULL` in the resulting array.

**Examples:**

| values | `array(values)` |
|---|---|
| () | \[\] |
| (1, 2, 3) | \[1, 2, 3\] |
| ("a", 1, true) | \["a", 1, true\] |
| (1, null) | \[1, null\] |
| (1, \[2, 3\]) | \[1, \[2, 3\]\] |

### ARRAY_CONCAT

**Syntax:**

    array_concat(arrays: ARRAY...) -> ARRAY

**Description:**

Concatenates two or more arrays into a single `ARRAY`.

**Examples:**

| arrays | `array_concat(arrays)` |
|---|---|
| (\[1, 2\], \[3, 4\]) | \[1, 2, 3, 4\] |
| (\["a", "b"\], \["c"\]) | \["a", "b", "c"\] |
| (\[1\], \[2\], \[3\]) | \[1, 2, 3\] |
| (\[\], \[1, 2\]) | \[1, 2\] |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("genre").arrayConcat([field("subGenre")]).as("allGenres"))
  .execute();
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("genre").arrayConcat([Field("subGenre")]).as("allGenres")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayConcat(field("subGenre")).alias("allGenres"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayConcat(field("subGenre")).alias("allGenres"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("genre").array_concat(Field.of("subGenre")).as_("allGenres"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(arrayConcat(field("genre"), field("subGenre")).as("allGenres"))
        .execute()
        .get();
```

### ARRAY_CONTAINS

**Syntax:**

    array_contains(array: ARRAY, value: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` is found in the `array`, and `FALSE` otherwise.

**Examples:**

| array | value | `array_contains(array, value)` |
|---|---|---|
| \[1, 2, 3\] | 2 | true |
| \[\[1, 2\], \[3\]\] | \[1, 2\] | true |
| \[1, null\] | null | true |
| "abc" | ANY | error |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("genre").arrayContains(constant("mystery")).as("isMystery"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("genre").arrayContains(constant("mystery")).as("isMystery"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("genre").arrayContains(Constant("mystery")).as("isMystery")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayContains("mystery").alias("isMystery"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayContains("mystery").alias("isMystery"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("genre").array_contains("mystery").as_("isMystery"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(arrayContains(field("genre"), "mystery").as("isMystery"))
        .execute()
        .get();
```

### ARRAY_CONTAINS_ALL

**Syntax:**

    array_contains_all(array: ARRAY, search_values: ARRAY) -> BOOLEAN

**Description:**

Returns `TRUE` if all `search_values` are found in the `array`, and `FALSE` otherwise.

**Examples:**

| array | search_values | `array_contains_all(array, search_values)` |
|---|---|---|
| \[1, 2, 3\] | \[1, 2\] | true |
| \[1, 2, 3\] | \[1, 4\] | false |
| \[1, null\] | \[null\] | true |
| \[NaN\] | \[NaN\] | true |
| \[\] | \[\] | true |
| \[1, 2, 3\] | \[\] | true |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("genre")
      .arrayContainsAll([constant("fantasy"), constant("adventure")])
      .as("isFantasyAdventure")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("genre")
      .arrayContainsAll([constant("fantasy"), constant("adventure")])
      .as("isFantasyAdventure")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("genre")
      .arrayContainsAll([Constant("fantasy"), Constant("adventure")])
      .as("isFantasyAdventure")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("genre")
            .arrayContainsAll(listOf("fantasy", "adventure"))
            .alias("isFantasyAdventure")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("genre")
            .arrayContainsAll(Arrays.asList("fantasy", "adventure"))
            .alias("isFantasyAdventure")
    )
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("genre")
        .array_contains_all(["fantasy", "adventure"])
        .as_("isFantasyAdventure")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            arrayContainsAll(field("genre"), Arrays.asList("fantasy", "adventure"))
                .as("isFantasyAdventure"))
        .execute()
        .get();
```

### ARRAY_CONTAINS_ANY

**Syntax:**

    array_contains_any(array: ARRAY, search_values: ARRAY) -> BOOLEAN

**Description:**

Returns `TRUE` if any of the `search_values` are found in the `array`, and `FALSE` otherwise.

**Examples:**

| array | search_values | `array_contains_any(array, search_values)` |
|---|---|---|
| \[1, 2, 3\] | \[4, 1\] | true |
| \[1, 2, 3\] | \[4, 5\] | false |
| \[1, 2, null\] | \[null\] | true |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("genre")
      .arrayContainsAny([constant("fantasy"), constant("nonfiction")])
      .as("isMysteryOrFantasy")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("genre")
      .arrayContainsAny([constant("fantasy"), constant("nonfiction")])
      .as("isMysteryOrFantasy")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("genre")
      .arrayContainsAny([Constant("fantasy"), Constant("nonfiction")])
      .as("isMysteryOrFantasy")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("genre")
            .arrayContainsAny(listOf("fantasy", "nonfiction"))
            .alias("isMysteryOrFantasy")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("genre")
            .arrayContainsAny(Arrays.asList("fantasy", "nonfiction"))
            .alias("isMysteryOrFantasy")
    )
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("genre")
        .array_contains_any(["fantasy", "nonfiction"])
        .as_("isMysteryOrFantasy")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            arrayContainsAny(field("genre"), Arrays.asList("fantasy", "nonfiction"))
                .as("isMysteryOrFantasy"))
        .execute()
        .get();
```

### ARRAY_GET

**Syntax:**

    array_get(array: ARRAY, index: INT64) -> ANY

**Description:**

Returns the element at the 0-based `index` in `array`.

- If `index` is negative, elements are accessed from the end of array, where `-1` is the last element.
- If `array` is not of type `ARRAY` and not `null`, returns an error.
- If `index` is out of bounds, the function returns an absent value.
- If `index` is not of type `INT64`, the function returns an error.

**Examples:**

| array | index | `array_get(array, index)` |
|---|---|---|
| \[1, 2, 3\] | 0 | 1 |
| \[1, 2, 3\] | -1 | 3 |
| \[1, 2, 3\] | 3 | absent |
| \[1, 2, 3\] | -4 | absent |
| "abc" | 0 | error |
| null | 0 | null |
| `Array` | "a" | error |
| `Array` | 2.0 | error |

### ARRAY_LENGTH

**Syntax:**

    array_length(array: ARRAY) -> INT64

**Description:**

Returns the number of elements in `array`.

**Examples:**

| array | `array_length(array)` |
|---|---|
| \[1, 2, 3\] | 3 |
| \[\] | 0 |
| \[1, 1, 1\] | 3 |
| \[1, null\] | 2 |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("genre").arrayLength().as("genreCount"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("genre").arrayLength().as("genreCount"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("genre").arrayLength().as("genreCount")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayLength().alias("genreCount"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayLength().alias("genreCount"))
    .execute();
    
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("genre").array_length().as_("genreCount"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(arrayLength(field("genre")).as("genreCount"))
        .execute()
        .get();
```

### ARRAY_REVERSE

**Syntax:**

    array_reverse(array: ARRAY) -> ARRAY

**Description:**

Reverses the given `array`.

**Examples:**

| array | `array_reverse(array)` |
|---|---|
| \[1, 2, 3\] | \[3, 2, 1\] |
| \["a", "b"\] | \["b", "a"\] |
| \[1, 2, 2, 3\] | \[3, 2, 2, 1\] |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(arrayReverse(field("genre")).as("reversedGenres"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("genre").arrayReverse().as("reversedGenres"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("genre").arrayReverse().as("reversedGenres")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayReverse().alias("reversedGenres"))
    .execute()
```

```java
    Java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("genre").arrayReverse().alias("reversedGenres"))
    .execute();
  
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("genre").array_reverse().as_("reversedGenres"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(arrayReverse(field("genre")).as("reversedGenres"))
        .execute()
        .get();
```

### ARRAY_FIRST

**Syntax:**

    array_first(array: ARRAY) -> ANY

**Description:**

Returns the first element in `array`. This is equivalent to `array_get(array, 0)`.

- If `array` is empty, returns an absent value.

**Examples:**

| array | `array_first(array)` |
|---|---|
| \[1, 2, 3\] | 1 |
| \[\] | absent |

### ARRAY_FIRST_N

**Syntax:**

    array_first_n(array: ARRAY, n: INT64) -> ARRAY

**Description:**

Returns the first `n` elements of `array`. This is equivalent to `array_slice(array, 0, n)`.

- If `n` is negative, returns an error.

**Examples:**

| array | n | `array_first_n(array, n)` |
|---|---|---|
| \[1, 2, 3, 4, 5\] | 3 | \[1, 2, 3\] |
| \[1, 2\] | 3 | \[1, 2\] |
| \[1, 2, 3\] | 0 | \[\] |

### ARRAY_INDEX_OF

**Syntax:**

    array_index_of(array: ARRAY, value: ANY) -> INT64

**Description:**

Returns the 0-based index of the first occurrence of `value` in `array`. Returns -1 if `value` is not found.

**Examples:**

| array | value | `array_index_of(array, value)` |
|---|---|---|
| \[1, 2, 3, 2\] | 2 | 1 |
| \[1, 2, 3\] | 4 | -1 |
| \[1, null, 3\] | null | 1 |

### ARRAY_INDEX_OF_ALL

**Syntax:**

    array_index_of_all(array: ARRAY, value: ANY) -> ARRAY<INT64>

**Description:**

Returns an array containing the 0-based indexes of all occurrences of `value` in `array`. Returns `[]` if `value` is not found.

**Examples:**

| array | value | `array_index_of_all(array, value)` |
|---|---|---|
| \[1, 2, 3, 2\] | 2 | \[1, 3\] |
| \[1, 2, 3\] | 4 | \[\] |
| \[1, null, 3, null\] | null | \[1, 3\] |

### ARRAY_LAST

**Syntax:**

    array_last(array: ARRAY) -> ANY

**Description:**

Returns the last element in `array`. This is equivalent to `array_get(array, -1)`.

- If `array` is empty, returns an absent value.

**Examples:**

| array | `array_last(array)` |
|---|---|
| \[1, 2, 3\] | 3 |
| \[\] | absent |

### ARRAY_LAST_N

**Syntax:**

    array_last_n(array: ARRAY, n: INT64) -> ARRAY

**Description:**

Returns the last `n` elements of `array`.

- If `n` is negative, returns an error.

**Examples:**

| array | n | `array_last_n(array, n)` |
|---|---|---|
| \[1, 2, 3, 4, 5\] | 3 | \[3, 4, 5\] |
| \[1, 2\] | 3 | \[1, 2\] |
| \[1, 2, 3\] | 0 | \[\] |

### ARRAY_SLICE

**Syntax:**

    array_slice(array: ARRAY, offset: INT64, length: INT64) -> ARRAY

**Description:**

Returns a subset of `array` starting from 0-based index `offset`, and including `length` elements.

- If `offset` is negative, it indicates the start position from the end of the array, with `-1` being the last element.
- If `length` is greater than the number of elements remaining in the array after `offset`, the result extends to the end of the array.
- `length` must be non-negative, otherwise returns an error.

**Examples:**

| array | offset | length | `array_slice(array, offset, length)` |
|---|---|---|---|
| \[1, 2, 3, 4, 5\] | 1 | 3 | \[2, 3, 4\] |
| \[1, 2, 3, 4, 5\] | -2 | 2 | \[4, 5\] |
| \[1, 2, 3\] | 1 | 5 | \[2, 3\] |
| \[1, 2, 3\] | 3 | 2 | \[\] |

### MAXIMUM

**Syntax:**

    maximum(array: ARRAY) -> ANY

**Description:**

Returns the maximum value in `array`.

- `NULL` values are ignored during comparison.
- If `array` is empty or only contains `NULL` values, returns `NULL`.

**Examples:**

| array | `maximum(array)` |
|---|---|
| \[1, 5, 2\] | 5 |
| \[1, null, 5\] | 5 |
| \["a", "c", "b"\] | "c" |
| \[null, null\] | null |
| \[\] | null |

### MAXIMUM_N

**Syntax:**

    maximum_n(array: ARRAY, n: INT64) -> ARRAY

**Description:**

Returns an array of the `n` largest values in `array` in descending order.

- `NULL` values are ignored.
- If `n` is negative, returns an error.

**Examples:**

| array | n | `maximum_n(array, n)` |
|---|---|---|
| \[1, 5, 2, 4, 3\] | 3 | \[5, 4, 3\] |
| \[1, null, 5\] | 3 | \[5, 1\] |

### MINIMUM

**Syntax:**

    minimum(array: ARRAY) -> ANY

**Description:**

Returns the minimum value in `array`.

- `NULL` values are ignored during comparison.
- If `array` is empty or only contains `NULL` values, returns `NULL`.

**Examples:**

| array | `minimum(array)` |
|---|---|
| \[1, 5, 2\] | 1 |
| \[5, null, 1\] | 1 |
| \["a", "c", "b"\] | "a" |
| \[null, null\] | null |
| \[\] | null |

### MINIMUM_N

**Syntax:**

    minimum_n(array: ARRAY, n: INT64) -> ARRAY

**Description:**

Returns an array of the `n` smallest values in `array` in ascending order.

- `NULL` values are ignored.
- If `n` is negative, returns an error.

**Examples:**

| array | n | `minimum_n(array, n)` |
|---|---|---|
| \[1, 5, 2, 4, 3\] | 3 | \[1, 2, 3\] |
| \[5, null, 1\] | 3 | \[1, 5\] |

### SUM

**Syntax:**

    sum(array: ARRAY) -> INT64 | FLOAT64

**Description:**

Returns the sum of all `NUMERIC` values in an `ARRAY`.

- Non-numeric values in the array are ignored.
- If any numeric value in the array is `NaN`, the function returns `NaN`.
- The return type is determined by the widest numeric type in the array: `INT64` \< `FLOAT64`.
- If 64-bit integer overflow occurs before any floating point value is summed, an error is returned. If floating point values are summed, overflow will result in +/- infinity.
- If the array contains no numeric values at all, the function returns `NULL`.

**Examples:**

| array | `sum(array)` |
|---|---|
| \[1, 2, 3\] | 6L |
| \[1L, 2L, 3L\] | 6L |
| \[2000000000, 2000000000\] | 4000000000L |
| \[10, 20.5\] | 30.5 |
| \[1, "a", 2\] | 3L |
| \[INT64.MAX_VALUE, 1\] | error |
| \[INT64.MAX_VALUE, 1, -1.0\] | error |
| \[INT64.MAX_VALUE, 1.0\] | 9.223372036854776e+18 |

### JOIN

**Syntax:**

    join[T <: STRING | BYTES](array: ARRAY<T>, delimiter: T) -> STRING
    join[T <: STRING | BYTES](array: ARRAY<T>, delimiter: T, null_text: T) -> STRING

**Description:**

Returns a concatenation of the elements in `array` as a `STRING`. The `array` can be of `STRING` or `BYTES` data types.

- All elements in `array`, `delimiter`, and `null_text` must be of the same type; they must all be `STRING`s or all be `BYTES`.
- If `null_text` is provided, any `NULL` values in `array` are replaced with `null_text`.
- If `null_text` is not provided, `NULL` values in `array` are omitted from the result.

**Examples:**

When `null_text` is not provided:

| array | delimiter | `join(array, delimiter)` |
|---|---|---|
| \["a", "b", "c"\] | "," | "a,b,c" |
| \["a", null, "c"\] | "," | "a,c" |
| \[b'a', b'b', b'c'\] | b',' | b'a,b,c' |
| \["a", b'c'\] | "," | error |
| \["a", "c"\] | b',' | error |
| \[b'a', b'c'\] | "," | error |

When `null_text` is provided:

| array | delimiter | null_text | `join(array, delimiter, null_text)` |
|---|---|---|---|
| \["a", null, "c"\] | "," | "MISSING" | "a,MISSING,c" |
| \[b'a', null, b'c'\] | b',' | b'NULL' | b'a,NULL,c' |
| \[null, "b", null\] | "," | "MISSING" | "MISSING,b,MISSING" |
| \[b'a', null, null\] | b',' | b'NULL' | b'a,NULL,NULL' |
| \["a", null\] | "," | b'N' | error |
| \[b'a', null\] | b',' | "N" | error |

## **Comparison Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#equal` | Equality comparison |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#greater_than` | Greater than comparison |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#greater_than_or_equal` | Greater than or equal comparison |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#less_than` | Less than comparison |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#less_than_or_equal` | Less than or equal comparison |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#not_equal` | Not equals comparison |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#cmp` | General comparison |

### EQUAL

**Syntax:**

    equal(x: ANY, y: ANY) -> BOOLEAN

**Examples:**

| `x` | `y` | `equal(x, y)` |
|---|---|---|
| 1L | 1L | `TRUE` |
| 1.0 | 1L | `TRUE` |
| -1.0 | 1L | `FALSE` |
| NaN | NaN | `TRUE` |
| `NULL` | `NULL` | `TRUE` |
| `NULL` | `ABSENT` | `FALSE` |

**Description:**

Returns `TRUE` if `x` and `y` are equal, and `FALSE` otherwise.

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("rating").equal(5).as("hasPerfectRating"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("rating").equal(5).as("hasPerfectRating"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("rating").equal(5).as("hasPerfectRating")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("rating").equal(5).alias("hasPerfectRating"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("rating").equal(5).alias("hasPerfectRating"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").equal(5).as_("hasPerfectRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(equal(field("rating"), 5).as("hasPerfectRating"))
        .execute()
        .get();
```

### GREATER_THAN

**Syntax:**

    greater_than(x: ANY, y: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `x` is greater than `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

| `x` | `y` | `greater_than(x, y)` |
|---|---|---|
| 1L | 0.0 | `TRUE` |
| 1L | 1L | `FALSE` |
| 1L | 2L | `FALSE` |
| "foo" | 0L | `FALSE` |
| 0L | "foo" | `FALSE` |
| NaN | 0L | `FALSE` |
| 0L | NaN | `FALSE` |
| `NULL` | `NULL` | `FALSE` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("rating").greaterThan(4).as("hasHighRating"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("rating").greaterThan(4).as("hasHighRating"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("rating").greaterThan(4).as("hasHighRating")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("rating").greaterThan(4).alias("hasHighRating"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("rating").greaterThan(4).alias("hasHighRating"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").greater_than(4).as_("hasHighRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(greaterThan(field("rating"), 4).as("hasHighRating"))
        .execute()
        .get();
```

### GREATER_THAN_OR_EQUAL

**Syntax:**

    greater_than_or_equal(x: ANY, y: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `x` is greater than or equal to `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

| `x` | `y` | `greater_than_or_equal(x, y)` |
|---|---|---|
| 1L | 0.0 | `TRUE` |
| 1L | 1L | `TRUE` |
| 1L | 2L | `FALSE` |
| "foo" | 0L | `FALSE` |
| 0L | "foo" | `FALSE` |
| NaN | 0L | `FALSE` |
| 0L | NaN | `FALSE` |
| `NULL` | `NULL` | `TRUE` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("published").greaterThanOrEqual(1900).as("publishedIn20thCentury"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("published").greaterThanOrEqual(1900).as("publishedIn20thCentury"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("published").greaterThanOrEqual(1900).as("publishedIn20thCentury")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("published").greaterThanOrEqual(1900).alias("publishedIn20thCentury"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("published").greaterThanOrEqual(1900).alias("publishedIn20thCentury"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("published")
        .greater_than_or_equal(1900)
        .as_("publishedIn20thCentury")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(greaterThanOrEqual(field("published"), 1900).as("publishedIn20thCentury"))
        .execute()
        .get();
```

### LESS_THAN

**Syntax:**

    less_than(x: ANY, y: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `x` is less than `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

| `x` | `y` | `less_than(x, y)` |
|---|---|---|
| 1L | 0.0 | `FALSE` |
| 1L | 1L | `FALSE` |
| 1L | 2L | `TRUE` |
| "foo" | 0L | `FALSE` |
| 0L | "foo" | `FALSE` |
| NaN | 0L | `FALSE` |
| 0L | NaN | `FALSE` |
| `NULL` | `NULL` | `FALSE` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("published").lessThan(1923).as("isPublicDomainProbably"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("published").lessThan(1923).as("isPublicDomainProbably"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("published").lessThan(1923).as("isPublicDomainProbably")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("published").lessThan(1923).alias("isPublicDomainProbably"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("published").lessThan(1923).alias("isPublicDomainProbably"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("published").less_than(1923).as_("isPublicDomainProbably"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(lessThan(field("published"), 1923).as("isPublicDomainProbably"))
        .execute()
        .get();
```

### LESS_THAN_OR_EQUAL

**Syntax:**

    less_than_or_equal(x: ANY, y: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `x` is less than or equal to `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

| `x` | `y` | `less_than(x, y)` |
|---|---|---|
| 1L | 0.0 | `FALSE` |
| 1L | 1L | `TRUE` |
| 1L | 2L | `TRUE` |
| "foo" | 0L | `FALSE` |
| 0L | "foo" | `FALSE` |
| NaN | 0L | `FALSE` |
| 0L | NaN | `FALSE` |
| `NULL` | `NULL` | `TRUE` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(field("rating").lessThanOrEqual(2).as("hasBadRating"))
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("rating").lessThanOrEqual(2).as("hasBadRating"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([Field("rating").lessThanOrEqual(2).as("hasBadRating")])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(field("rating").lessThanOrEqual(2).alias("hasBadRating"))
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(field("rating").lessThanOrEqual(2).alias("hasBadRating"))
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").less_than_or_equal(2).as_("hasBadRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(lessThanOrEqual(field("rating"), 2).as("hasBadRating"))
        .execute()
        .get();
```

### NOT_EQUAL

**Syntax:**

    not_equal(x: ANY, y: ANY) -> BOOLEAN

**Description:**

Returns `TRUE` if `x` is not equal to `y`, and `FALSE` otherwise.

**Examples:**

| `x` | `y` | `not_equal(x, y)` |
|---|---|---|
| 1L | 1L | `FALSE` |
| 1.0 | 1L | `FALSE` |
| -1.0 | 1L | `TRUE` |
| NaN | 0L | `TRUE` |
| NaN | NaN | `FALSE` |
| `NULL` | `NULL` | `FALSE` |
| `NULL` | `ABSENT` | `TRUE` |

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

### CMP

**Syntax:**

    cmp(x: ANY, y: ANY) -> Int64

**Description:**

Compares `x` \& `y`, returning:

- `1L` if `x` is greater than `y`.
- `-1L` if `x` is less than `y`.
- `0L` otherwise.

Unlike other comparison functions, the `cmp(...)` function works across types,
following the same ordering used in the `sort(...)` stage. See
[value type order](https://firebase.google.com/docs/firestore/manage-data/data-types) for how values are ordered across types.

**Examples:**

| `x` | `y` | `cmp(x, y)` |
|---|---|---|
| 1L | 1L | 0L |
| 1.0 | 1L | 0L |
| -1.0 | 1L | -1L |
| 42.5D | "foo" | -1L |
| `NULL` | `NULL` | 0L |
| `NULL` | `ABSENT` | 0L |

## **Debugging Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#exists` | Returns `TRUE` if the value is not an absent value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#is_absent` | Returns `TRUE` if the value is an absent value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#if_absent` | Replaces the value with an expression if it is absent |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#is_error` | Catches and checks if an error has been thrown by the underlying expression |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#if_error` | Replaces the value with an expression if it has thrown an error |

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

## **Logical Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#and` | Performs a logical AND |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#or` | Performs a logical OR |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#xor` | Performs a logical XOR |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#not` | Performs a logical NOT |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#conditional` | Branches evaluation based on a conditional expression. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#equal_any` | Checks if a value is equal to any elements in an array |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#not_equal_any` | Checks if a value is not equal to any elements in an array |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#maximum` | Returns the maximum value in a set of values |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#minimum` | Returns the minimum value in a set of values |

### AND

**Syntax:**

    and(x: BOOLEAN...) -> BOOLEAN

**Description:**

Returns the logical AND of two or more boolean values.

Returns `NULL` if the result can't be derived due to any of the given values being `ABSENT` or `NULL`.

**Examples:**

| `x` | `y` | `and(x, y)` |
|---|---|---|
| `TRUE` | `TRUE` | `TRUE` |
| `FALSE` | `TRUE` | `FALSE` |
| `NULL` | `TRUE` | `NULL` |
| `ABSENT` | `TRUE` | `NULL` |
| `NULL` | `FALSE` | `FALSE` |
| `FALSE` | `ABSENT` | `FALSE` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    and(field("rating").greaterThan(4), field("price").lessThan(10))
      .as("under10Recommendation")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    and(field("rating").greaterThan(4), field("price").lessThan(10))
      .as("under10Recommendation")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    (Field("rating").greaterThan(4) && Field("price").lessThan(10))
      .as("under10Recommendation")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        Expression.and(field("rating").greaterThan(4),
          field("price").lessThan(10))
            .alias("under10Recommendation")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        Expression.and(
            field("rating").greaterThan(4),
            field("price").lessThan(10)
        ).alias("under10Recommendation")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field, And

result = (
    client.pipeline()
    .collection("books")
    .select(
        And(
            Field.of("rating").greater_than(4), Field.of("price").less_than(10)
        ).as_("under10Recommendation")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            and(greaterThan(field("rating"), 4), lessThan(field("price"), 10))
                .as("under10Recommendation"))
        .execute()
        .get();
```

### OR

**Syntax:**

    or(x: BOOLEAN...) -> BOOLEAN

**Description:**

Returns the logical OR of two or more boolean values.

Returns `NULL` if the result can't be derived due to any of the given values being `ABSENT` or `NULL`.

**Examples:**

| `x` | `y` | `or(x, y)` |
|---|---|---|
| `TRUE` | `TRUE` | `TRUE` |
| `FALSE` | `TRUE` | `TRUE` |
| `NULL` | `TRUE` | `TRUE` |
| `ABSENT` | `TRUE` | `TRUE` |
| `NULL` | `FALSE` | `NULL` |
| `FALSE` | `ABSENT` | `NULL` |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    or(field("genre").equal("Fantasy"), field("tags").arrayContains("adventure"))
      .as("matchesSearchFilters")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    or(field("genre").equal("Fantasy"), field("tags").arrayContains("adventure"))
      .as("matchesSearchFilters")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    (Field("genre").equal("Fantasy") || Field("tags").arrayContains("adventure"))
      .as("matchesSearchFilters")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        Expression.or(field("genre").equal("Fantasy"),
          field("tags").arrayContains("adventure"))
            .alias("matchesSearchFilters")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        Expression.or(
            field("genre").equal("Fantasy"),
            field("tags").arrayContains("adventure")
        ).alias("matchesSearchFilters")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field, And, Or

result = (
    client.pipeline()
    .collection("books")
    .select(
        Or(
            Field.of("genre").equal("Fantasy"),
            Field.of("tags").array_contains("adventure"),
        ).as_("matchesSearchFilters")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            or(equal(field("genre"), "Fantasy"), arrayContains(field("tags"), "adventure"))
                .as("matchesSearchFilters"))
        .execute()
        .get();
```

### XOR

**Syntax:**

    xor(x: BOOLEAN...) -> BOOLEAN

**Description:**

Returns the logical XOR of two or more boolean values.

Returns `NULL` if any of the given values are `ABSENT` or `NULL`.

**Examples:**

| `x` | `y` | `xor(x, y)` |
|---|---|---|
| `TRUE` | `TRUE` | `FALSE` |
| `FALSE` | `FALSE` | `FALSE` |
| `FALSE` | `TRUE` | `TRUE` |
| `NULL` | `TRUE` | `NULL` |
| `ABSENT` | `TRUE` | `NULL` |
| `NULL` | `FALSE` | `NULL` |
| `FALSE` | `ABSENT` | `NULL` |

##### Node.js

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    xor(field("tags").arrayContains("magic"), field("tags").arrayContains("nonfiction"))
      .as("matchesSearchFilters")
  )
);
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    xor(field("tags").arrayContains("magic"), field("tags").arrayContains("nonfiction"))
      .as("matchesSearchFilters")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    (Field("tags").arrayContains("magic") ^ Field("tags").arrayContains("nonfiction"))
      .as("matchesSearchFilters")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        Expression.xor(field("tags").arrayContains("magic"),
          field("tags").arrayContains("nonfiction"))
            .alias("matchesSearchFilters")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        Expression.xor(
            field("tags").arrayContains("magic"),
            field("tags").arrayContains("nonfiction")
        ).alias("matchesSearchFilters")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field, Xor

result = (
    client.pipeline()
    .collection("books")
    .select(
        Xor(
            [
                Field.of("tags").array_contains("magic"),
                Field.of("tags").array_contains("nonfiction"),
            ]
        ).as_("matchesSearchFilters")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            xor(
                    arrayContains(field("tags"), "magic"),
                    arrayContains(field("tags"), "nonfiction"))
                .as("matchesSearchFilters"))
        .execute()
        .get();
```

### NOT

**Syntax:**

    not(x: BOOLEAN) -> BOOLEAN

**Description:**

Returns the logical NOT of a boolean value.

##### Node.js

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("tags").arrayContains("nonfiction").not()
      .as("isFiction")
  )
);
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("tags").arrayContains("nonfiction").not()
      .as("isFiction")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    (!Field("tags").arrayContains("nonfiction"))
      .as("isFiction")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        Expression.not(
            field("tags").arrayContains("nonfiction")
        ).alias("isFiction")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        Expression.not(
            field("tags").arrayContains("nonfiction")
        ).alias("isFiction")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field, Not

result = (
    client.pipeline()
    .collection("books")
    .select(Not(Field.of("tags").array_contains("nonfiction")).as_("isFiction"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(not(arrayContains(field("tags"), "nonfiction")).as("isFiction"))
        .execute()
        .get();
```

### CONDITIONAL

**Syntax:**

    conditional(condition: BOOLEAN, true_case: ANY, false_case: ANY) -> ANY

**Description:**

Evaluates and returns the `true_case` if the `condition` evaluates to `TRUE`.

Evaluates and returns the `false_case` if the condition resolves to `FALSE`, `NULL`, or an `ABSENT` value.

**Examples:**

| `condition` | `true_case` | `false_case` | `conditional(condition, true_case, false_case)` |
|---|---|---|---|
| `TRUE` | 1L | 0L | 1L |
| `FALSE` | 1L | 0L | 0L |
| `NULL` | 1L | 0L | 0L |
| `ABSENT` | 1L | 0L | 0L |

##### Node.js

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("tags").arrayConcat([
      field("pages").greaterThan(100)
        .conditional(constant("longRead"), constant("shortRead"))
    ]).as("extendedTags")
  )
);
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("tags").arrayConcat([
      field("pages").greaterThan(100)
        .conditional(constant("longRead"), constant("shortRead"))
    ]).as("extendedTags")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("tags").arrayConcat([
      ConditionalExpression(
        Field("pages").greaterThan(100),
        then: Constant("longRead"),
        else: Constant("shortRead")
      )
    ]).as("extendedTags")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("tags").arrayConcat(
            Expression.conditional(
                field("pages").greaterThan(100),
                constant("longRead"),
                constant("shortRead")
            )
        ).alias("extendedTags")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("tags").arrayConcat(
            Expression.conditional(
                field("pages").greaterThan(100),
                constant("longRead"),
                constant("shortRead")
            )
        ).alias("extendedTags")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import (
    Field,
    Constant,
    Conditional,
)

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("tags")
        .array_concat(
            Conditional(
                Field.of("pages").greater_than(100),
                Constant.of("longRead"),
                Constant.of("shortRead"),
            )
        )
        .as_("extendedTags")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            arrayConcat(
                    field("tags"),
                    conditional(
                        greaterThan(field("pages"), 100),
                        constant("longRead"),
                        constant("shortRead")))
                .as("extendedTags"))
        .execute()
        .get();
```

### EQUAL_ANY

**Syntax:**

    equal_any(value: ANY, search_space: ARRAY) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` is in the `search_space` array.

**Examples:**

| `value` | `search_space` | `equal_any(value, search_space)` |
|---|---|---|
| 0L | \[1L, 2L, 3L\] | `FALSE` |
| 2L | \[1L, 2L, 3L\] | `TRUE` |
| `NULL` | \[1L, 2L, 3L\] | `FALSE` |
| `NULL` | \[1L, `NULL`\] | `TRUE` |
| `ABSENT` | \[1L, `NULL`\] | `FALSE` |
| NaN | \[1L, NaN, 3L\] | `TRUE` |

##### Node.js

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("genre").equalAny(["Science Fiction", "Psychological Thriller"])
      .as("matchesGenreFilters")
  )
);
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("genre").equalAny(["Science Fiction", "Psychological Thriller"])
      .as("matchesGenreFilters")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("genre").equalAny(["Science Fiction", "Psychological Thriller"])
      .as("matchesGenreFilters")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("genre").equalAny(listOf("Science Fiction", "Psychological Thriller"))
            .alias("matchesGenreFilters")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("genre").equalAny(Arrays.asList("Science Fiction", "Psychological Thriller"))
            .alias("matchesGenreFilters")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("genre")
        .equal_any(["Science Fiction", "Psychological Thriller"])
        .as_("matchesGenreFilters")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            equalAny(field("genre"), Arrays.asList("Science Fiction", "Psychological Thriller"))
                .as("matchesGenreFilters"))
        .execute()
        .get();
```

### NOT_EQUAL_ANY

**Syntax:**

    not_equal_any(value: ANY, search_space: ARRAY) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` is not in the `search_space` array.

**Examples:**

| `value` | `search_space` | `not_equal_any(value, search_space)` |
|---|---|---|
| 0L | \[1L, 2L, 3L\] | `TRUE` |
| 2L | \[1L, 2L, 3L\] | `FALSE` |
| `NULL` | \[1L, 2L, 3L\] | `TRUE` |
| `NULL` | \[1L, `NULL`\] | `FALSE` |
| `ABSENT` | \[1L, `NULL`\] | `TRUE` |
| NaN | \[1L, NaN, 3L\] | `FALSE` |

##### Node.js

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("author").notEqualAny(["George Orwell", "F. Scott Fitzgerald"])
      .as("byExcludedAuthors")
  )
);
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("author").notEqualAny(["George Orwell", "F. Scott Fitzgerald"])
      .as("byExcludedAuthors")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("author").notEqualAny(["George Orwell", "F. Scott Fitzgerald"])
      .as("byExcludedAuthors")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("author").notEqualAny(listOf("George Orwell", "F. Scott Fitzgerald"))
            .alias("byExcludedAuthors")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("author").notEqualAny(Arrays.asList("George Orwell", "F. Scott Fitzgerald"))
            .alias("byExcludedAuthors")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("author")
        .not_equal_any(["George Orwell", "F. Scott Fitzgerald"])
        .as_("byExcludedAuthors")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(
            notEqualAny(field("author"), Arrays.asList("George Orwell", "F. Scott Fitzgerald"))
                .as("byExcludedAuthors"))
        .execute()
        .get();
```

### MAXIMUM

**Syntax:**

    maximum(x: ANY...) -> ANY
    maximum(x: ARRAY) -> ANY

**Description:**

Returns the maximum non-`NULL`, non-`ABSENT` value in a series of values `x`.

If there are no non-`NULL`, non-`ABSENT` values, `NULL` is returned.

If there are multiple maximum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://firebase.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

**Examples:**

| `x` | `y` | `maximum(x, y)` |
|---|---|---|
| `FALSE` | `TRUE` | `TRUE` |
| `FALSE` | -10L | -10L |
| 0.0 | -5L | 0.0 |
| "foo" | "bar" | "foo" |
| "foo" | \["foo"\] | \["foo"\] |
| `ABSENT` | `ABSENT` | `NULL` |
| `NULL` | `NULL` | `NULL` |

##### Node.js

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("price").maximum().as("maximumPrice"))
);
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("price").maximum().as("maximumPrice"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("rating").logicalMaximum([1]).as("flooredRating")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("rating").logicalMaximum(1).alias("flooredRating")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("rating").logicalMaximum(1).alias("flooredRating")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").logical_maximum(1).as_("flooredRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(logicalMaximum(field("rating"), 1).as("flooredRating"))
        .execute()
        .get();
```

### MINIMUM

**Syntax:**

    minimum(x: ANY...) -> ANY
    minimum(x: ARRAY) -> ANY

**Description:**

Returns the minimum non-`NULL`, non-`ABSENT` value in a series of values `x`.

If there are no non-`NULL`, non-`ABSENT` values, `NULL` is returned.

If there are multiple minimum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://firebase.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

**Examples:**

| `x` | `y` | `minimum(x, y)` |
|---|---|---|
| `FALSE` | `TRUE` | `FALSE` |
| `FALSE` | -10L | `FALSE` |
| 0.0 | -5L | -5L |
| "foo" | "bar" | "bar" |
| "foo" | \["foo"\] | "foo" |
| `ABSENT` | `ABSENT` | `NULL` |
| `NULL` | `NULL` | `NULL` |

##### Node.js

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("price").minimum().as("minimumPrice"))
);
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .aggregate(field("price").minimum().as("minimumPrice"))
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("rating").logicalMinimum([5]).as("cappedRating")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("rating").logicalMinimum(5).alias("cappedRating")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("rating").logicalMinimum(5).alias("cappedRating")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("rating").logical_minimum(5).as_("cappedRating"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(logicalMinimum(field("rating"), 5).as("cappedRating"))
        .execute()
        .get();
```

## **Map Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map` | Constructs a map value from a series of key-value pairs |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map_get` | Returns the value in a map given a specified key |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map_set` | Returns a copy of a map with a series of updated keys |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map_remove` | Returns a copy of a map with a series of keys removed |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map_merge` | Merges a series of maps together. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#current_context` | Returns the current context as a map. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map_keys` | Returns an array of all keys in a map. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map_values` | Returns an array of all values in a map. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#map_entries` | Returns an array of key-value pairs of a map. |

### MAP

**Syntax:**

    map(key: STRING, value: ANY, ...) -> MAP

**Description:**

Constructs a map from a series of key-value pairs.

### MAP_GET

**Syntax:**

    map_get(map: ANY, key: STRING) -> ANY

**Description:**

Returns the value in a map given a specified key. Returns an `ABSENT` value if the `key` does not exist in the map, or if the `map` argument is not a `MAP`.

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("awards").mapGet("pulitzer").as("hasPulitzerAward")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("awards").mapGet("pulitzer").as("hasPulitzerAward")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("awards").mapGet("pulitzer").as("hasPulitzerAward")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("awards").mapGet("pulitzer").alias("hasPulitzerAward")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("awards").mapGet("pulitzer").alias("hasPulitzerAward")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("awards").map_get("pulitzer").as_("hasPulitzerAward"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(mapGet(field("awards"), "pulitzer").as("hasPulitzerAward"))
        .execute()
        .get();
```

### MAP_SET

**Syntax:**

    map_set(map: MAP, key: STRING, value: ANY, ...) -> MAP

**Description:**

Returns a copy of the `map` value with its contents updated by a series of key-value pairs.

If the given resolves to an absent value, the associated key is removed from the map.

If the `map` argument is not a `MAP`, returns an absent value.

### MAP_REMOVE

**Syntax:**

    map_remove(map: MAP, key: STRING...) -> MAP

**Description:**

Returns a copy of the `map` value with a series of keys removed.

### MAP_MERGE

**Syntax:**

    map_merge(maps: MAP...) -> MAP

Merges the contents of 2 or more maps. If multiple maps have conflicting values, the last value is used.

### CURRENT_CONTEXT

**Syntax:**

    current_context() -> MAP

Returns a map consisting of all available fields in the current point of execution.

### MAP_KEYS

**Syntax:**

    map_keys(map: MAP) -> ARRAY<STRING>

**Description:**

Returns an array containing all keys of the `map` value.

### MAP_VALUES

**Syntax:**

    map_values(map: MAP) -> ARRAY<ANY>

**Description:**

Returns an array containing all values of the `map` value.

### MAP_ENTRIES

**Syntax:**

    map_entries(map: MAP) -> ARRAY<MAP>

**Description:**

Returns an array containing all key-value pairs in the `map` value.

Each key-value pair will be in the form of a map with two entries, `k` and `v`.

**Examples:**

| `map` | `map_entries(map)` |
|---|---|
| {} | \[\] |
| {"foo" : 2L} | \[{"k": "foo", "v" : 2L}\] |
| {"foo" : "bar", "bar" : "foo"} | \[{"k": "foo", "v" : "bar" }, {"k" : "bar", "v": "foo"}\] |

## **String Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#byte_length` | Returns the number of `BYTES` in a `STRING` or `BYTES` value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#char_length` | Returns the number of unicode characters in a `STRING` value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#starts_with` | Returns `TRUE` if a `STRING` begins with a given prefix |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#ends_with` | Returns `TRUE` if a `STRING` ends with a given postfix |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#like` | Returns `TRUE` if a `STRING` matches a pattern |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#regex_contains` | Returns `TRUE` if a value is a partial or full match for a regular expression |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#regex_match` | Returns `TRUE` if any part of a value matches a regular expression |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#string_concat` | Concatenates multiple `STRING` into a `STRING` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#string_contains` | Returns `TRUE` if a value contains a `STRING` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#to_upper` | Converts a `STRING` or `BYTES` value to uppercase. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#to_lower` | Converts a `STRING` or `BYTES` value to lowercase. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#substring` | Gets a substring of a `STRING` or `BYTES` value. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#string_reverse` | Reverses a `STRING` or `BYTES` value. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#trim` | Trims leading and trailing characters from a `STRING` or `BYTES` value. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#split` | Splits a `STRING` or `BYTES` value into an array. |

### BYTE_LENGTH

**Syntax:**

    byte_length[T <: STRING | BYTES](value: T) -> INT64

**Description:**

Returns the number of `BYTES` in a `STRING` or `BYTES` value.

**Examples:**

| value | `byte_length(value)` |
|---|---|
| "abc" | 3 |
| "xyzabc" | 6 |
| b"abc" | 3 |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("title").byteLength().as("titleByteLength")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("title").byteLength().as("titleByteLength")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("title").byteLength().as("titleByteLength")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("title").byteLength().alias("titleByteLength")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("title").byteLength().alias("titleByteLength")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("title").byte_length().as_("titleByteLength"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(byteLength(field("title")).as("titleByteLength"))
        .execute()
        .get();
```

### CHAR_LENGTH

**Syntax:**

    char_length(value: STRING) -> INT64

**Description:**

Returns the number of unicode code points in `STRING` value.

**Examples:**

| value | `char_length(value)` |
|---|---|
| "abc" | 3 |
| "hello" | 5 |
| "world" | 5 |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("title").charLength().as("titleCharLength")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("title").charLength().as("titleCharLength")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("title").charLength().as("titleCharLength")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("title").charLength().alias("titleCharLength")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("title").charLength().alias("titleCharLength")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("title").char_length().as_("titleCharLength"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(charLength(field("title")).as("titleCharLength"))
        .execute()
        .get();
```

### STARTS_WITH

**Syntax:**

    starts_with(value: STRING, prefix: STRING) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` begins with `prefix`.

**Examples:**

| value | prefix | `starts_with(value, prefix)` |
|---|---|---|
| "abc" | "a" | true |
| "abc" | "b" | false |
| "abc" | "" | true |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("title").startsWith("The")
      .as("needsSpecialAlphabeticalSort")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("title").startsWith("The")
      .as("needsSpecialAlphabeticalSort")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("title").startsWith("The")
      .as("needsSpecialAlphabeticalSort")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("title").startsWith("The")
            .alias("needsSpecialAlphabeticalSort")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("title").startsWith("The")
            .alias("needsSpecialAlphabeticalSort")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("title").starts_with("The").as_("needsSpecialAlphabeticalSort")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(startsWith(field("title"), "The").as("needsSpecialAlphabeticalSort"))
        .execute()
        .get();
```

### ENDS_WITH

**Syntax:**

    ends_with(value: STRING, postfix: STRING) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` ends with `postfix`.

**Examples:**

| value | postfix | `ends_with(value, postfix)` |
|---|---|---|
| "abc" | "c" | true |
| "abc" | "b" | false |
| "abc" | "" | true |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("inventory/devices/laptops")
  .select(
    field("name").endsWith("16 inch")
      .as("16InLaptops")
  )
  .execute();
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("inventory/devices/laptops")
  .select([
    Field("name").endsWith("16 inch")
      .as("16InLaptops")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("inventory/devices/laptops")
    .select(
        field("name").endsWith("16 inch")
            .alias("16InLaptops")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("inventory/devices/laptops")
    .select(
        field("name").endsWith("16 inch")
            .alias("16InLaptops")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("inventory/devices/laptops")
    .select(Field.of("name").ends_with("16 inch").as_("16InLaptops"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("inventory/devices/laptops")
        .select(endsWith(field("name"), "16 inch").as("16InLaptops"))
        .execute()
        .get();
```

### LIKE

**Syntax:**

    like(value: STRING, pattern: STRING) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` matches `pattern`.

**Examples:**

| value | pattern | `like(value, pattern)` |
|---|---|---|
| "Firestore" | "Fire%" | true |
| "Firestore" | "%store" | true |
| "Datastore" | "Data_tore" | true |
| "100%" | "100\\%" | true |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("genre").like("%Fiction")
      .as("anyFiction")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("genre").like("%Fiction")
      .as("anyFiction")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("genre").like("%Fiction")
      .as("anyFiction")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("genre").like("%Fiction")
            .alias("anyFiction")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("genre").like("%Fiction")
            .alias("anyFiction")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("genre").like("%Fiction").as_("anyFiction"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(like(field("genre"), "%Fiction").as("anyFiction"))
        .execute()
        .get();
```

### REGEX_CONTAINS

**Syntax:**

    regex_contains(value: STRING, pattern: STRING) -> BOOLEAN

**Description:**

Returns `TRUE` if some part of `value` matches `pattern`. If `pattern` is not a valid regular expression, this function returns an `error`.

Regular expressions follow the syntax of the [re2](https://github.com/google/re2/wiki/Syntax) library.

**Examples:**

| value | pattern | `regex_contains(value, pattern)` |
|---|---|---|
| "Firestore" | "Fire" | true |
| "Firestore" | "store$" | true |
| "Firestore" | "data" | false |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("title").regexContains("Firestore (Enterprise|Standard)")
      .as("isFirestoreRelated")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("title").regexContains("Firestore (Enterprise|Standard)")
      .as("isFirestoreRelated")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("title").regexContains("Firestore (Enterprise|Standard)")
      .as("isFirestoreRelated")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("title").regexContains("Firestore (Enterprise|Standard)")
            .alias("isFirestoreRelated")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("title").regexContains("Firestore (Enterprise|Standard)")
            .alias("isFirestoreRelated")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(
        Field.of("title")
        .regex_contains("Firestore (Enterprise|Standard)")
        .as_("isFirestoreRelated")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(
            regexContains(field("title"), "Firestore (Enterprise|Standard)")
                .as("isFirestoreRelated"))
        .execute()
        .get();
```

### REGEX_MATCH

**Syntax:**

    regex_match(value: STRING, pattern: STRING) -> BOOLEAN

**Description:**

Returns `TRUE` if `value` fully matches `pattern`. If `pattern` is not a valid regular expression, this function returns an `error`.

Regular expressions follow the syntax of the [re2](https://github.com/google/re2/wiki/Syntax) library.

**Examples:**

| value | pattern | `regex_match(value, pattern)` |
|---|---|---|
| "Firestore" | "F.\*store" | true |
| "Firestore" | "Fire" | false |
| "Firestore" | "\^F.\*e$" | true |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("title").regexMatch("Firestore (Enterprise|Standard)")
      .as("isFirestoreExactly")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("title").regexMatch("Firestore (Enterprise|Standard)")
      .as("isFirestoreExactly")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("title").regexMatch("Firestore (Enterprise|Standard)")
      .as("isFirestoreExactly")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("title").regexMatch("Firestore (Enterprise|Standard)")
            .alias("isFirestoreExactly")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("title").regexMatch("Firestore (Enterprise|Standard)")
            .alias("isFirestoreExactly")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(
        Field.of("title")
        .regex_match("Firestore (Enterprise|Standard)")
        .as_("isFirestoreExactly")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(
            regexMatch(field("title"), "Firestore (Enterprise|Standard)")
                .as("isFirestoreExactly"))
        .execute()
        .get();
```

### STRING_CONCAT

**Syntax:**

    string_concat(values: STRING...) -> STRING

**Description:**

Concatenates two or more `STRING` values into a single result.

**Examples:**

| arguments | `string_concat(values...)` |
|---|---|
| `()` | error |
| `("a")` | "a" |
| `("abc", "def")` | "abcdef" |
| `("a", "", "c")` | "ac" |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("title").stringConcat(" by ", field("author"))
      .as("fullyQualifiedTitle")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("title").stringConcat(" by ", field("author"))
      .as("fullyQualifiedTitle")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("title").concat([" by ", Field("author")])
      .as("fullyQualifiedTitle")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("title").concat(" by ", field("author"))
            .alias("fullyQualifiedTitle")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("title").concat(" by ", field("author"))
            .alias("fullyQualifiedTitle")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("title")
        .concat(" by ", Field.of("author"))
        .as_("fullyQualifiedTitle")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(stringConcat(field("title"), " by ", field("author")).as("fullyQualifiedTitle"))
        .execute()
        .get();
```

### STRING_CONTAINS

**Syntax:**

    string_contains(value: STRING, substring: STRING) -> BOOLEAN

**Description:**

Checks if `value` contains the literal String `substring`.

**Examples:**

| value | substring | `string_contains(value, substring)` |
|---|---|---|
| "abc" | "b" | true |
| "abc" | "d" | false |
| "abc" | "" | true |
| "a.c" | "." | true |
| "☃☃☃" | "☃" | true |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("articles")
  .select(
    field("body").stringContains("Firestore")
      .as("isFirestoreRelated")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("articles")
  .select(
    field("body").stringContains("Firestore")
      .as("isFirestoreRelated")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("articles")
  .select([
    Field("body").stringContains("Firestore")
      .as("isFirestoreRelated")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("articles")
    .select(
        field("body").stringContains("Firestore")
            .alias("isFirestoreRelated")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("articles")
    .select(
        field("body").stringContains("Firestore")
            .alias("isFirestoreRelated")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("articles")
    .select(Field.of("body").string_contains("Firestore").as_("isFirestoreRelated"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("articles")
        .select(stringContains(field("body"), "Firestore").as("isFirestoreRelated"))
        .execute()
        .get();
```

### TO_UPPER

**Syntax:**

    to_upper[T <: STRING | BYTES](value: T) -> T

**Description:**

Converts a `STRING` or `BYTES` value to uppercase.

If a byte or char does not correspond to a UTF-8 lowercase alphabetic character, it is passed through unchanged.

**Examples:**

| value | `to_upper(value)` |
|---|---|
| "abc" | "ABC" |
| "AbC" | "ABC" |
| b"abc" | b"ABC" |
| b"a1c" | b"A1C" |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("authors")
  .select(
    field("name").toUpper()
      .as("uppercaseName")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("authors")
  .select(
    field("name").toUpper()
      .as("uppercaseName")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("authors")
  .select([
    Field("name").toUpper()
      .as("uppercaseName")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("authors")
    .select(
        field("name").toUpper()
            .alias("uppercaseName")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("authors")
    .select(
        field("name").toUpper()
            .alias("uppercaseName")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("authors")
    .select(Field.of("name").to_upper().as_("uppercaseName"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("authors")
        .select(toUpper(field("name")).as("uppercaseName"))
        .execute()
        .get();
```

### TO_LOWER

**Syntax:**

    to_lower[T <: STRING | BYTES](value: T) -> T

**Description:**

Converts a `STRING` or `BYTES` value to lowercase.

If a byte or char does not correspond to a UTF-8 uppercase alphabetic character, it is passed through unchanged.

**Examples:**

| value | `to_lower(value)` |
|---|---|
| "ABC" | "abc" |
| "AbC" | "abc" |
| "A1C" | "a1c" |
| b"ABC" | b"abc" |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("authors")
  .select(
    field("genre").toLower().equal("fantasy")
      .as("isFantasy")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("authors")
  .select(
    field("genre").toLower().equal("fantasy")
      .as("isFantasy")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("authors")
  .select([
    Field("genre").toLower().equal("fantasy")
      .as("isFantasy")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("authors")
    .select(
        field("genre").toLower().equal("fantasy")
            .alias("isFantasy")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("authors")
    .select(
        field("genre").toLower().equal("fantasy")
            .alias("isFantasy")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("authors")
    .select(Field.of("genre").to_lower().equal("fantasy").as_("isFantasy"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("authors")
        .select(equal(toLower(field("genre")), "fantasy").as("isFantasy"))
        .execute()
        .get();
```

### SUBSTRING

**Syntax:**

    substring[T <: STRING | BYTES](input: T, position: INT64) -> T
    substring[T <: STRING | BYTES](input: T, position: INT64, length: INT64) -> T

**Description:**

Returns a substring of `input` starting at `position` (zero-based index) and
including up to `length` entries. If no `length` is provided, returns the substring
from `position` to the end of the `input`.

- If `input` is a `STRING` value, `position` and `length` are measured in unicode
  code points. If it is a `BYTES` value, they are measured in bytes.

- If `position` is greater than the length of the `input`, an empty substring is returned. If `position` plus `length` is greater than the length of `input`, the substring is truncated to the end of `input`.

- If `position` is negative, the position is taken from the end of the input. If the negative `position` is greater than the size of the input, the position is set to zero. `length` must be non-negative.

**Examples:**

When `length` is not provided:

| input | position | `substring(input, position)` |
|---|---|---|
| "abc" | 0 | "abc" |
| "abc" | 1 | "bc" |
| "abc" | 3 | "" |
| "abc" | -1 | "c" |
| b"abc" | 1 | b"bc" |

When `length` is provided:

| input | position | length | `substring(input, position, length)` |
|---|---|---|---|
| "abc" | 0 | 1 | "a" |
| "abc" | 1 | 2 | "bc" |
| "abc" | -1 | 1 | "c" |
| b"abc" | 0 | 1 | b"a" |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .where(field("title").startsWith("The "))
  .select(
    field("title").substring(4)
      .as("titleWithoutLeadingThe")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .where(field("title").startsWith("The "))
  .select(
    field("title").substring(4)
      .as("titleWithoutLeadingThe")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .where(Field("title").startsWith("The "))
  .select([
    Field("title").substring(position: 4)
      .as("titleWithoutLeadingThe")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .where(field("title").startsWith("The "))
    .select(
        field("title")
          .substring(constant(4),
            field("title").charLength().subtract(4))
            .alias("titleWithoutLeadingThe")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .where(field("title").startsWith("The "))
    .select(
        field("title").substring(
          constant(4),
            field("title").charLength().subtract(4))
            .alias("titleWithoutLeadingThe")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .where(Field.of("title").starts_with("The "))
    .select(Field.of("title").substring(4).as_("titleWithoutLeadingThe"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .where(startsWith(field("title"), "The "))
        .select(
            substring(field("title"), constant(4), field("title").charLength())
                .as("titleWithoutLeadingThe"))
        .execute()
        .get();
```

### STRING_REVERSE

**Syntax:**

    string_reverse[T <: STRING | BYTES](input: T) -> T

**Description:**

Returns the supplied input in reverse order.

Characters are delineated by Unicode code points when the input is a `STRING`, and bytes when the input is a `BYTES` value.

**Examples:**

| input | `string_reverse(input)` |
|---|---|
| "abc" | "cba" |
| "a🌹b" | "b🌹a" |
| "hello" | "olleh" |
| b"abc" | b"cba" |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("books")
  .select(
    field("name").reverse().as("reversedName")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("name").reverse().as("reversedName")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("name").reverse().as("reversedName")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("name").reverse().alias("reversedName")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("name").reverse().alias("reversedName")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("name").string_reverse().as_("reversedName"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(reverse(field("name")).as("reversedName"))
        .execute()
        .get();
```

### TRIM

**Syntax:**

    trim[T <: STRING | BYTES](input: T, values_to_trim: T) -> T
    trim[T <: STRING | BYTES](input: T) -> T

**Description:**

Trims a specified set of `BYTES` or `CHARS` from the beginning and end of the
supplied `input`.

- If no `values_to_trim` are provided, trims whitespace characters.

**Examples:**

When `values_to_trim` is not provided:

| input | `trim(input)` |
|---|---|
| " foo " | "foo" |
| b" foo " | b"foo" |
| "foo" | "foo" |
| "" | "" |
| " " | "" |
| "\\t foo \\n" | "foo" |
| b"\\t foo \\n" | b"foo" |
| "\\r\\f\\v foo \\r\\f\\v" | "foo" |
| b"\\r\\f\\v foo \\r\\f\\v" | b"foo" |

When `values_to_trim` is provided:

| input | values_to_trim | `trim(input, values_to_trim)` |
|---|---|---|
| "abcbfooaacb" | "abc" | "foo" |
| "abcdaabadbac" | "abc" | "daabad" |
| b"C1C2C3" | b"C1" | b"C2C3" |
| b"C1C2" | "foo" | error |
| "foo" | b"C1" | error |

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("name").trim().as("whitespaceTrimmedName")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("name").trim(" \n\t").as("whitespaceTrimmedName")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("books")
    .select(
        field("name").trim().alias("whitespaceTrimmedName")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("name").trim().alias("whitespaceTrimmedName")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("name").trim().as_("whitespaceTrimmedName"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(trim(field("name")).as("whitespaceTrimmedName"))
        .execute()
        .get();
```

### SPLIT

**Syntax:**

    split(input: STRING) -> ARRAY<STRING>
    split[T <: STRING | BYTES](input: T, delimiter: T) -> ARRAY<T>

**Description:**

Splits a `STRING` or `BYTES` value, using a delimiter.

- For `STRING` the default delimiter is the comma `,`. The delimiter is treated as a single string.

- For `BYTES`, you must specify a delimiter.

- Splitting on an empty delimiter produces an array of Unicode codepoints for `STRING` values, and an array of `BYTES` for `BYTES` values.

- Splitting an empty `STRING` returns an `ARRAY` with a single empty `STRING`.

**Examples:**

When `delimiter` is not provided:

| input | `split(input)` |
|---|---|
| "foo,bar,foo" | \["foo", "bar", "foo"\] |
| "foo" | \["foo"\] |
| ",foo," | \["", "foo", ""\] |
| "" | \[""\] |
| b"C120C2C4" | error |

When `delimiter` is provided:

| input | delimiter | `split(input, delimiter)` |
|---|---|---|
| "foo bar foo" | " " | \["foo", "bar", "foo"\] |
| "foo bar foo" | "z" | \["foo bar foo"\] |
| "abc" | "" | \["a", "b", "c"\] |
| b"C1,C2,C4" | b"," | \[b"C1", b"C2", b"C4"\] |
| b"ABC" | b"" | \[b"A", b"B", b"C"\] |
| "foo" | b"C1" | error |

## **Timestamp Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#current_timestamp` | Generates a `TIMESTAMP` corresponding to the request time. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_trunc` | Truncates a `TIMESTAMP` to a given granularity. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#unix_micros_to_timestamp` | Converts the number of microseconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#unix_millis_to_timestamp` | Converts the number of milliseconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#unix_seconds_to_timestamp` | Converts the number of seconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_add` | Adds a time interval to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_sub` | Subtracts a time interval to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_to_unix_micros` | Converts a `TIMESTAMP` to the number of microseconds since `1970-01-01 00:00:00 UTC` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_to_unix_millis` | Converts a `TIMESTAMP` to the number of milliseconds since `1970-01-01 00:00:00 UTC` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_to_unix_seconds` | Converts a `TIMESTAMP` to the number of seconds since `1970-01-01 00:00:00 UTC` |

### CURRENT_TIMESTAMP

**Syntax:**

    current_timestamp() -> TIMESTAMP

**Description:**

Gets the timestamp at the beginning of request time `input` (interpreted as the number of microseconds since `1970-01-01 00:00:00 UTC`).

This is stable within a query, and will always resolve to the same value if called multiple times.

### TIMESTAMP_TRUNC

**Syntax:**

    timestamp_trunc(timestamp: TIMESTAMP, granularity: STRING[, timezone: STRING]) -> TIMESTAMP

**Description:**

Truncates a timestamp down to a given granularity.

The `granularity` argument must be a string and one of the following:

- `microsecond`
- `millisecond`
- `second`
- `minute`
- `hour`
- `day`
- `week`
- `week([weekday])`
- `month`
- `quarter`
- `year`
- `isoyear`

If the `timezone` argument is provided, truncation will be based on the given timezone's calendar boundaries (e.g. day truncation will truncate to midnight in the given timezone). The truncation will respect daylight savings time.

If `timezone` is not provided, truncation will be based on `UTC` calendar boundaries.

The `timezone` argument should be a string representation of a timezone from the tz database, for example `America/New_York`. A custom time offset can also be used by specifying an offset from `GMT`.

**Examples:**

| `timestamp` | `granularity` | `timezone` | `timestamp_trunc(timestamp, granularity, timezone)` |
|---|---|---|---|
| 2000-01-01 10:20:30:123456 UTC | "second" | Not provided | 2001-01-01 10:20:30 UTC |
| 1997-05-31 04:30:30 UTC | "day" | Not provided | 1997-05-31 00:00:00 UTC |
| 1997-05-31 04:30:30 UTC | "day" | "America/Los_Angeles" | 1997-05-30 07:00:00 UTC |
| 2001-03-16 04:00:00 UTC | "week(friday) | Not provided | 2001-03-16 00:00:00 UTC |
| 2001-03-23 04:00:00 UTC | "week(friday) | "America/Los_Angeles" | 2001-03-23 17:00:00 UTC |
| 2026-01-24 20:00:00 UTC | "month" | "GMT+06:32:43" | 2026-01-01T06:32:43 UTC |

### UNIX_MICROS_TO_TIMESTAMP

**Syntax:**

    unix_micros_to_timestamp(input: INT64) -> TIMESTAMP

**Description:**

Converts `input` (interpreted as the number of microseconds since `1970-01-01 00:00:00 UTC`) to a `TIMESTAMP`. Throws an `error` if `input` cannot be converted to a valid `TIMESTAMP`.

**Examples:**

| `input` | `unix_micros_to_timestamp(input)` |
|---|---|
| 0L | 1970-01-01 00:00:00 UTC |
| 400123456L | 1970-01-01 00:06:40.123456 UTC |
| -1000000L | 1969-12-31 23:59:59 UTC |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("createdAtMicros").unixMicrosToTimestamp().as("createdAtString")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("createdAtMicros").unixMicrosToTimestamp().as("createdAtString")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("createdAtMicros").unixMicrosToTimestamp().as("createdAtString")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAtMicros").unixMicrosToTimestamp().alias("createdAtString")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAtMicros").unixMicrosToTimestamp().alias("createdAtString")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(
        Field.of("createdAtMicros")
        .unix_micros_to_timestamp()
        .as_("createdAtString")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(unixMicrosToTimestamp(field("createdAtMicros")).as("createdAtString"))
        .execute()
        .get();
```

### UNIX_MILLIS_TO_TIMESTAMP

**Syntax:**

    unix_millis_to_timestamp(input: INT64) -> TIMESTAMP

**Description:**

Converts `input` (interpreted as the number of milliseconds since `1970-01-01 00:00:00 UTC`) to a `TIMESTAMP`. Throws an `error` if `input` cannot be converted to a valid `TIMESTAMP`.

**Examples:**

| `input` | `unix_millis_to_timestamp(input)` |
|---|---|
| 0L | 1970-01-01 00:00:00 UTC |
| 4000123L | 1970-01-01 01:06:40.123 UTC |
| -1000000L | 1969-12-31 23:43:20 UTC |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("createdAtMillis").unixMillisToTimestamp().as("createdAtString")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("createdAtMillis").unixMillisToTimestamp().as("createdAtString")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("createdAtMillis").unixMillisToTimestamp().as("createdAtString")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAtMillis").unixMillisToTimestamp().alias("createdAtString")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAtMillis").unixMillisToTimestamp().alias("createdAtString")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(
        Field.of("createdAtMillis")
        .unix_millis_to_timestamp()
        .as_("createdAtString")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(unixMillisToTimestamp(field("createdAtMillis")).as("createdAtString"))
        .execute()
        .get();
```

### UNIX_SECONDS_TO_TIMESTAMP

**Syntax:**

    unix_seconds_to_timestamp(input: INT64) -> TIMESTAMP

**Description:**

Converts `input` (interpreted as the number of seconds since `1970-01-01 00:00:00 UTC`) to a `TIMESTAMP`. Throws an `error` if `input` cannot be converted to a valid `TIMESTAMP`.

**Examples:**

| `input` | `unix_seconds_to_timestamp(input)` |
|---|---|
| 0L | 1970-01-01 00:00:00 UTC |
| 60L | 1970-01-01 00:01:00 UTC |
| -300L | 1969-12-31 23:55:00 UTC |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("createdAtSeconds").unixSecondsToTimestamp().as("createdAtString")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("createdAtSeconds").unixSecondsToTimestamp().as("createdAtString")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("createdAtSeconds").unixSecondsToTimestamp().as("createdAtString")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAtSeconds").unixSecondsToTimestamp().alias("createdAtString")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAtSeconds").unixSecondsToTimestamp().alias("createdAtString")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(
        Field.of("createdAtSeconds")
        .unix_seconds_to_timestamp()
        .as_("createdAtString")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(unixSecondsToTimestamp(field("createdAtSeconds")).as("createdAtString"))
        .execute()
        .get();
```

### TIMESTAMP_ADD

**Syntax:**

    timestamp_add(timestamp: TIMESTAMP, unit: STRING, amount: INT64) -> TIMESTAMP

**Description:**

Adds an `amount` of `unit` from `timestamp`. The `amount` argument can be negative, in that case it is equivalent to [TIMESTAMP_SUB](https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_sub).

The `unit` argument must be a string and one of the following:

- `microsecond`
- `millisecond`
- `second`
- `minute`
- `hour`
- `day`

Throws an error if the resulting timestamp does not fit within the `TIMESTAMP` range.

**Examples:**

| `timestamp` | `unit` | `amount` | `timestamp_add(timestamp, unit, amount)` |
|---|---|---|---|
| 2025-02-20 00:00:00 UTC | "minute" | 2L | 2025-02-20 00:02:00 UTC |
| 2025-02-20 00:00:00 UTC | "hour" | -4L | 2025-02-19 20:00:00 UTC |
| 2025-02-20 00:00:00 UTC | "day" | 5L | 2025-02-25 00:00:00 UTC |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("createdAt").timestampAdd("day", 3653).as("expiresAt")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("createdAt").timestampAdd("day", 3653).as("expiresAt")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("createdAt").timestampAdd(3653, .day).as("expiresAt")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAt")
          .timestampAdd("day", 3653)
          .alias("expiresAt")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("createdAt").timestampAdd("day", 3653).alias("expiresAt")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(Field.of("createdAt").timestamp_add("day", 3653).as_("expiresAt"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(timestampAdd(field("createdAt"), "day", 3653).as("expiresAt"))
        .execute()
        .get();
```

### TIMESTAMP_SUB

**Syntax:**

    timestamp_sub(timestamp: TIMESTAMP, unit: STRING, amount: INT64) -> TIMESTAMP

**Description:**

Subtracts an `amount` of `unit` from `timestamp`. The `amount` argument can be negative, in that case it is equivalent to [TIMESTAMP_ADD](https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#timestamp_add).

The `unit` argument must be a string and one of the following:

- `microsecond`
- `millisecond`
- `second`
- `minute`
- `hour`
- `day`

Throws an error if the resulting timestamp does not fit within the `TIMESTAMP` range.

**Examples:**

| `timestamp` | `unit` | `amount` | `timestamp_sub(timestamp, unit, amount)` |
|---|---|---|---|
| 2026-07-04 00:00:00 UTC | "minute" | 40L | 2026-07-03 23:20:00 UTC |
| 2026-07-04 00:00:00 UTC | "hour" | -24L | 2026-07-05 00:00:00 UTC |
| 2026-07-04 00:00:00 UTC | "day" | 3L | 2026-07-01 00:00:00 UTC |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("expiresAt").timestampSubtract("day", 14).as("sendWarningTimestamp")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("expiresAt").timestampSubtract("day", 14).as("sendWarningTimestamp")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("expiresAt").timestampSubtract(14, .day).as("sendWarningTimestamp")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("expiresAt")
          .timestampSubtract("day", 14)
          .alias("sendWarningTimestamp")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("expiresAt").timestampSubtract("day", 14).alias("sendWarningTimestamp")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(
        Field.of("expiresAt")
        .timestamp_subtract("day", 14)
        .as_("sendWarningTimestamp")
    )
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(timestampSubtract(field("expiresAt"), "day", 14).as("sendWarningTimestamp"))
        .execute()
        .get();
```

### TIMESTAMP_TO_UNIX_MICROS

**Syntax:**

    timestamp_to_unix_micros(input: TIMESTAMP) -> INT64

**Description:**

Converts `input` to the number of microseconds since `1970-01-01 00:00:00 UTC`. Truncates higher levels of precision by rounding down to the beginning of the microsecond.

**Examples:**

| `input` | `timestamp_to_unix_micros(input)` |
|---|---|
| 1970-01-01 00:00:00 UTC | 0L |
| 1970-01-01 00:06:40.123456 UTC | 400123456L |
| 1969-12-31 23:59:59 UTC | -1000000L |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("dateString").timestampToUnixMicros().as("unixMicros")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("dateString").timestampToUnixMicros().as("unixMicros")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("dateString").timestampToUnixMicros().as("unixMicros")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("dateString").timestampToUnixMicros().alias("unixMicros")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("dateString").timestampToUnixMicros().alias("unixMicros")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(Field.of("dateString").timestamp_to_unix_micros().as_("unixMicros"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(timestampToUnixMicros(field("dateString")).as("unixMicros"))
        .execute()
        .get();
```

### TIMESTAMP_TO_UNIX_MILLIS

**Syntax:**

    timestamp_to_unix_millis(input: TIMESTAMP) -> INT64

**Description:**

Converts `input` to the number of milliseconds since `1970-01-01 00:00:00 UTC`. Truncates higher levels of precision by rounding down to the beginning of the millisecond.

**Examples:**

| `input` | `timestamp_to_unix_millis(input)` |
|---|---|
| 1970-01-01 00:00:00 UTC | 0L |
| 1970-01-01 01:06:40.123 UTC | 4000123L |
| 1969-12-31 23:43:20 | -1000000L |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("dateString").timestampToUnixMillis().as("unixMillis")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("dateString").timestampToUnixMillis().as("unixMillis")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("dateString").timestampToUnixMillis().as("unixMillis")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("dateString").timestampToUnixMillis().alias("unixMillis")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("dateString").timestampToUnixMillis().alias("unixMillis")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(Field.of("dateString").timestamp_to_unix_millis().as_("unixMillis"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(timestampToUnixMillis(field("dateString")).as("unixMillis"))
        .execute()
        .get();
```

### TIMESTAMP_TO_UNIX_SECONDS

**Syntax:**

    timestamp_to_unix_seconds(input: TIMESTAMP) -> INT64

**Description:**

Converts `input` to the number of seconds since `1970-01-01 00:00:00 UTC`. Truncates higher levels of precision by rounding down to the beginning of the second.

**Examples:**

| `input` | `timestamp_to_unix_seconds(input)` |
|---|---|
| 1970-01-01 00:00:00 UTC | 0L |
| 1970-01-01 00:01:00 UTC | 60L |
| 1969-12-31 23:55:00 UTC | -300L |

##### Node.js

```javascript
const result = await db.pipeline()
  .collection("documents")
  .select(
    field("dateString").timestampToUnixSeconds().as("unixSeconds")
  )
  .execute();
```

### Web

```javascript
const result = await execute(db.pipeline()
  .collection("documents")
  .select(
    field("dateString").timestampToUnixSeconds().as("unixSeconds")
  )
);
```

##### Swift

```swift
let result = try await db.pipeline()
  .collection("documents")
  .select([
    Field("dateString").timestampToUnixSeconds().as("unixSeconds")
  ])
  .execute()
```

### Kotlin

```kotlin
val result = db.pipeline()
    .collection("documents")
    .select(
        field("dateString").timestampToUnixSeconds().alias("unixSeconds")
    )
    .execute()
```

### Java

```java
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("documents")
    .select(
        field("dateString").timestampToUnixSeconds().alias("unixSeconds")
    )
    .execute();
```

##### Python

```python
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("documents")
    .select(Field.of("dateString").timestamp_to_unix_seconds().as_("unixSeconds"))
    .execute()
)
```

##### Java

```java
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("documents")
        .select(timestampToUnixSeconds(field("dateString")).as("unixSeconds"))
        .execute()
        .get();
```

## **Type Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#type` | Returns the type of the value as a `STRING`. |

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

## **Vector Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#cosine_distance` | Returns the cosine distance between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#dot_product` | Returns the dot product between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#euclidean_distance` | Returns the euclidean distance between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#manhattan_distance` | Returns the manhattan distance between two vectors |
| `https://firebase.google.com/docs/firestore/pipelines/functions/all_functions#vector_length` | Returns the number of elements in a vector |

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