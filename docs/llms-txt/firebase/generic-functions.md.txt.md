# Source: https://firebase.google.com/docs/firestore/pipelines/functions/generic-functions.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

## **Generic Functions**

|---|---|
| Name | Description |
| `https://firebase.google.com/docs/firestore/pipelines/functions/generic-functions#concat` | Concatenates two or more values of same type. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/generic-functions#length` | Calculates the length of a `String`, `Bytes`, `Array`, `Vector`, or `Map`. |
| `https://firebase.google.com/docs/firestore/pipelines/functions/generic-functions#reverse` | Reverses a `String`, `Bytes`, or `Array`. |

## Client Examples

##### Node.js

```javascript
concat(constant("Author ID: "), field("authorId"));
```

### Web

```javascript
concat(constant("Author ID: "), field("authorId"));
```

##### Swift

```swift
let displayString = Constant("Author ID: ").concat([Field("authorId")])
```

### Kotlin

```kotlin
val displayString = constant("Author ID: ").concat(field("authorId"))
```

### Java

```java
Expression displayString = constant("Author ID: ").concat(field("authorId"));
```

##### Python

```python
Constant.of("Author ID: ").concat(Field.of("authorId"))
```

### CONCAT

**Syntax:**

    concat[T <: STRING | BYTES | ARRAY](values:T ...) -> T

**Description:**

Concatenates two or more values of same type.

**Examples:**

| values | `concat(values)` |
|---|---|
| "abc", "def" | "abcdef" |
| \[1, 2\], \[3, 4\] | \[1, 2, 3, 4\] |
| b"abc", b"def" | b"abcdef" |
| "abc", \[1,2,3\], "ghi" | error |
| \[1,2,3\] | error |
| "abc", null | null |

### LENGTH

**Syntax:**

    length[T <: STRING | BYTES | ARRAY | VECTOR | MAP](value: T) -> INT64

**Description:**

Calculates the length of a `String`, `Bytes`, `Array`, `Vector`, or `Map` value.

**Examples:**

| value | `length(value)` |
|---|---|
| "hello" | 5 |
| \[1, 2, 3, 4\] | 4 |
| b"abcde" | 5 |
| null | null |
| 1 | error |

### REVERSE

**Syntax:**

    reverse[T <: STRING | BYTES | ARRAY](value: T) -> T

**Description:**

Reverses a `String`, `Bytes`, or `Array` value.

**Examples:**

| value | `reverse(value)` |
|---|---|
| "hello" | "olleh" |
| \[1, 2, 3\] | \[3, 2, 1\] |
| b"abc" | b"cba" |
| 23 | error |
| null | null |