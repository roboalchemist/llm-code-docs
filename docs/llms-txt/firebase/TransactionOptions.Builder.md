# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder.md.txt

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

|                                                                                                                                                                                                 ### Public constructors                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#Builder())`()` Constructs a new `TransactionOptions` Builder object.                                                                                                                                                                                                                               |
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#Builder(com.google.firebase.firestore.TransactionOptions))`(options: `[TransactionOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions)`)` Constructs a new `TransactionOptions` Builder based on an existing ` TransactionOptions` object. |

|                                                           ### Public functions                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [TransactionOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#build())`()` Build the `TransactionOptions` object.                                                                                                                                                 |
| [TransactionOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder) | [setMaxAttempts](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder#setMaxAttempts(int))`(maxAttempts: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Set maximum number of attempts to commit, after which transaction fails. |

## Public constructors

### Builder

```
Builder()
```

Constructs a new `TransactionOptions` Builder object.  

### Builder

```
Builder(options:Â TransactionOptions)
```

Constructs a new `TransactionOptions` Builder based on an existing `
TransactionOptions` object.  

## Public functions

### build

```
funÂ build():Â TransactionOptions
```

Build the `TransactionOptions` object.  

|                                                         Returns                                                          |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| [TransactionOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions) | The built `TransactionOptions` object |

### setMaxAttempts

```
funÂ setMaxAttempts(maxAttempts:Â Int):Â TransactionOptions.Builder
```

Set maximum number of attempts to commit, after which transaction fails.

The default value is 5. Setting the value to less than 1 will result in an [IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html).  

|                                                                 Returns                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [TransactionOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder) | This builder |