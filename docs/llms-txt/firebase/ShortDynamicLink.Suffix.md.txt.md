# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix.md.txt

# ShortDynamicLink.Suffix

# ShortDynamicLink.Suffix


```
@Retention(value = RetentionPolicy.SOURCE)
@IntDef(value = [Suffix.UNGUESSABLE, Suffix.SHORT])
public annotation ShortDynamicLink.Suffix
```

<br />

*** ** * ** ***

Path generation option for short Dynamic Link length

## Summary

| ### Constants |
|---|---|
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix#SHORT() = 2` Shorten the path to a string that is only as long as needed to be unique, with a minimum length of 4 characters. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix#UNGUESSABLE() = 1` Shorten the path to an unguessable string. |

## Constants

### SHORT

```
public static final int SHORT = 2
```

Shorten the path to a string that is only as long as needed to be unique, with a minimum length of 4 characters. Use this method if sensitive information would not be exposed if a short Dynamic Link URL were guessed.

### UNGUESSABLE

```
public static final int UNGUESSABLE = 1
```

Shorten the path to an unguessable string. Such strings are created by base62-encoding randomly generated 96-bit numbers, and consist of 17 alphanumeric characters. Use unguessable strings to prevent your Dynamic Links from being crawled, which can potentially expose sensitive information.