# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder.md.txt

# TransactionOptions.Builder

# TransactionOptions.Builder


```
class TransactionOptions.Builder
```

<br />

*** ** * ** ***

A Builder for creating `TransactionOptions`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#Builder()()` Constructs a new `TransactionOptions` Builder object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#Builder(com.google.firebase.firestore.TransactionOptions)(options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions)` Constructs a new `TransactionOptions` Builder based on an existing ` TransactionOptions` object. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#build()()` Build the `TransactionOptions` object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#setMaxAttempts(int)(maxAttempts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Set maximum number of attempts to commit, after which transaction fails. |

## Public constructors

### Builder

```
Builder()
```

Constructs a new `TransactionOptions` Builder object.

### Builder

```
Builder(options: TransactionOptions)
```

Constructs a new `TransactionOptions` Builder based on an existing `
TransactionOptions` object.

## Public functions

### build

```
fun build(): TransactionOptions
```

Build the `TransactionOptions` object.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions` | The built `TransactionOptions` object |

### setMaxAttempts

```
fun setMaxAttempts(maxAttempts: Int): TransactionOptions.Builder
```

Set maximum number of attempts to commit, after which transaction fails.

The default value is 5. Setting the value to less than 1 will result in an `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder` | This builder |