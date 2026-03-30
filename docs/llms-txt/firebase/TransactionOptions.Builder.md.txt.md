# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder.md.txt

# TransactionOptions.Builder

# TransactionOptions.Builder


```
public final class TransactionOptions.Builder
```

<br />

*** ** * ** ***

A Builder for creating `TransactionOptions`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder#Builder()()` Constructs a new `TransactionOptions` Builder object. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder#Builder(com.google.firebase.firestore.TransactionOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions options)` Constructs a new `TransactionOptions` Builder based on an existing ` TransactionOptions` object. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder#build()()` Build the `TransactionOptions` object. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder#setMaxAttempts(int)(int maxAttempts)` Set maximum number of attempts to commit, after which transaction fails. |

## Public constructors

### Builder

```
public Builder()
```

Constructs a new `TransactionOptions` Builder object.

### Builder

```
public Builder(@NonNull TransactionOptions options)
```

Constructs a new `TransactionOptions` Builder based on an existing `
TransactionOptions` object.

## Public methods

### build

```
public @NonNull TransactionOptions build()
```

Build the `TransactionOptions` object.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions` | The built `TransactionOptions` object |

### setMaxAttempts

```
public @NonNull TransactionOptions.Builder setMaxAttempts(int maxAttempts)
```

Set maximum number of attempts to commit, after which transaction fails.

The default value is 5. Setting the value to less than 1 will result in an `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder` | This builder |