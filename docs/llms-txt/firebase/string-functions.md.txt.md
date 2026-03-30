# Source: https://firebase.google.com/docs/firestore/pipelines/functions/string-functions.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## **String Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#byte_length` | Returns the number of `BYTES` in a `STRING` or `BYTES` value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#char_length` | Returns the number of unicode characters in a `STRING` value |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#starts_with` | Returns `TRUE` if a `STRING` begins with a given prefix |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#ends_with` | Returns `TRUE` if a `STRING` ends with a given postfix |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#like` | Returns `TRUE` if a `STRING` matches a pattern |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#regex_contains` | Returns `TRUE` if a value is a partial or full match for a regular expression |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#regex_match` | Returns `TRUE` if any part of a value matches a regular expression |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#string_concat` | Concatenates multiple `STRING` into a `STRING` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#string_contains` | Returns `TRUE` if a value contains a `STRING` |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#to_upper` | Converts a `STRING` or `BYTES` value to uppercase. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#to_lower` | Converts a `STRING` or `BYTES` value to lowercase. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#substring` | Gets a substring of a `STRING` or `BYTES` value. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#string_reverse` | Reverses a `STRING` or `BYTES` value. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#trim` | Trims leading and trailing characters from a `STRING` or `BYTES` value. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/string-functions#split` | Splits a `STRING` or `BYTES` value into an array. |

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