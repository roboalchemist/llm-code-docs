# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus.md.txt

# UrlRetrievalStatus

# UrlRetrievalStatus


```
class UrlRetrievalStatus
```

<br />

*** ** * ** ***

The status of a URL retrieval.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus.Companion#ERROR()` The URL retrieval failed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus.Companion#PAYWALL()` The URL retrieval failed because the content is behind a paywall. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus.Companion#SUCCESS()` The URL retrieval was successful. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus.Companion#UNSAFE()` The URL retrieval failed because the content is unsafe. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus.Companion#UNSPECIFIED()` Unspecified retrieval status. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus#name()` The name of the retrieval status. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlRetrievalStatus#ordinal()` The ordinal value of the retrieval status. |

## Public companion properties

### ERROR

```
val ERROR: UrlRetrievalStatus
```

The URL retrieval failed.

### PAYWALL

```
val PAYWALL: UrlRetrievalStatus
```

The URL retrieval failed because the content is behind a paywall.

### SUCCESS

```
val SUCCESS: UrlRetrievalStatus
```

The URL retrieval was successful.

### UNSAFE

```
val UNSAFE: UrlRetrievalStatus
```

The URL retrieval failed because the content is unsafe.

### UNSPECIFIED

```
val UNSPECIFIED: UrlRetrievalStatus
```

Unspecified retrieval status.

## Public properties

### name

```
val name: String
```

The name of the retrieval status.

### ordinal

```
val ordinal: Int
```

The ordinal value of the retrieval status.