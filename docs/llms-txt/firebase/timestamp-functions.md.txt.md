# Source: https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## **Timestamp Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#current_timestamp` | Generates a `TIMESTAMP` corresponding to the request time. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_trunc` | Truncates a `TIMESTAMP` to a given granularity. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#unix_micros_to_timestamp` | Converts the number of microseconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#unix_millis_to_timestamp` | Converts the number of milliseconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#unix_seconds_to_timestamp` | Converts the number of seconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_add` | Adds a time interval to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_sub` | Subtracts a time interval to a `TIMESTAMP` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_to_unix_micros` | Converts a `TIMESTAMP` to the number of microseconds since `1970-01-01 00:00:00 UTC` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_to_unix_millis` | Converts a `TIMESTAMP` to the number of milliseconds since `1970-01-01 00:00:00 UTC` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_to_unix_seconds` | Converts a `TIMESTAMP` to the number of seconds since `1970-01-01 00:00:00 UTC` |

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

Adds an `amount` of `unit` from `timestamp`. The `amount` argument can be negative, in that case it is equivalent to [TIMESTAMP_SUB](https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_sub).

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

Subtracts an `amount` of `unit` from `timestamp`. The `amount` argument can be negative, in that case it is equivalent to [TIMESTAMP_ADD](https://firebase.google.com/docs/firestore/pipelines/functions/timestamp-functions#timestamp_add).

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