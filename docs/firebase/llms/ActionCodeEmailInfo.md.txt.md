# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeEmailInfo.md.txt

# ActionCodeEmailInfo

# ActionCodeEmailInfo


```
public abstract class ActionCodeEmailInfo extends ActionCodeInfo
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo) ||
|   | ↳ | [com.google.firebase.auth.ActionCodeEmailInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeEmailInfo) |

*** ** * ** ***

Holds information regarding out-of-band operations that involve an email change.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeEmailInfo#ActionCodeEmailInfo()()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeEmailInfo#getEmail()()` Returns the email on the account after the application of the out-of-band code. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeEmailInfo#getPreviousEmail()()` Returns the email on the account before the application of the out-of-band code. |

| ### Inherited fields |
|---|
| From [com.google.firebase.auth.ActionCodeInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo) |---|---| | `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `@https://firebase.google.com/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation(value = "hide_members_annotation") https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo#email()` Member variable holding the email for this ActionCode Info | |

## Public constructors

### ActionCodeEmailInfo

```
public ActionCodeEmailInfo()
```

## Public methods

### getEmail

```
public @NonNull String getEmail()
```

Returns the email on the account after the application of the out-of-band code.

### getPreviousEmail

```
public abstract @NonNull String getPreviousEmail()
```

Returns the email on the account before the application of the out-of-band code.