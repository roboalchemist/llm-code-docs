# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.md.txt

# ListResult

# ListResult


```
class ListResult
```

<br />

*** ** * ** ***

Contains the prefixes and items returned by a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)` call.

## Summary

| ### Public properties |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#items()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#pageToken()` |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#prefixes()` |

| ### Extension functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its items. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its prefixes. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its pageToken. |

## Public properties

### items

```
val items: (Mutable)List<StorageReference!>!
```

### pageToken

```
val pageToken: String?
```

### prefixes

```
val prefixes: (Mutable)List<StorageReference!>!
```

## Extension functions

### component1

```
operator fun ListResult.component1(): List<StorageReference>
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its items.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | the items of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` |

### component2

```
operator fun ListResult.component2(): List<StorageReference>
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its prefixes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | the prefixes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` |

### component3

```
operator fun ListResult.component3(): String?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its pageToken.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the pageToken of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` |