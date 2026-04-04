# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.md.txt

# ActionCodeResult

# ActionCodeResult


```
public interface ActionCodeResult
```

<br />

*** ** * ** ***

Interface for holding the information related to an out of band code.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/androidx/annotation/IntDef.html(value = ) @https://developer.android.com/reference/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) public annotation https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey` Keys to access the account information related to an out of band code. |
| `@https://developer.android.com/reference/androidx/annotation/IntDef.html(value = ) @https://developer.android.com/reference/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) public annotation https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` Holds the possible operations that an out of band code can perform, which are password reset, verify email, and recover email. |

| ### Constants |
|---|---|
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#EMAIL() = 0` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey` which is used to key calls to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getData(int)`. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#ERROR() = 3` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that there was some error in determining what the out of band code is for. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#FROM_EMAIL() = 1` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey` which is used to key calls to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getData(int)`. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#PASSWORD_RESET() = 0` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for a password reset. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#RECOVER_EMAIL() = 2` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for email recovery. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#REVERT_SECOND_FACTOR_ADDITION() = 6` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for reverting a second factor addition. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#SIGN_IN_WITH_EMAIL_LINK() = 4` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for signing in a user via an email link. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#VERIFY_BEFORE_CHANGE_EMAIL() = 5` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for verifying and updating the user's email. |
| `default static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#VERIFY_EMAIL() = 1` Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for email verification. |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `[getData](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getData(int))(@https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey int key)` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getInfo()`. <br /> |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getInfo()()` Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo` object that holds information regarding the operation being performed. |
| `abstract int` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getOperation()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` for which this out of band code was intended. |

## Constants

### EMAIL

```
default static final int EMAIL = 0
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey` which is used to key calls to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getData(int)`. This signifies the email before the application of the out of band code.

### ERROR

```
default static final int ERROR = 3
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that there was some error in determining what the out of band code is for.

### FROM_EMAIL

```
default static final int FROM_EMAIL = 1
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey` which is used to key calls to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getData(int)`. This signifies the current email associated with the account, which may have changed as a result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` performed.

### PASSWORD_RESET

```
default static final int PASSWORD_RESET = 0
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for a password reset.

### RECOVER_EMAIL

```
default static final int RECOVER_EMAIL = 2
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for email recovery.

### REVERT_SECOND_FACTOR_ADDITION

```
default static final int REVERT_SECOND_FACTOR_ADDITION = 6
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for reverting a second factor addition.

### SIGN_IN_WITH_EMAIL_LINK

```
default static final int SIGN_IN_WITH_EMAIL_LINK = 4
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for signing in a user via an email link.

### VERIFY_BEFORE_CHANGE_EMAIL

```
default static final int VERIFY_BEFORE_CHANGE_EMAIL = 5
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for verifying and updating the user's email.

### VERIFY_EMAIL

```
default static final int VERIFY_EMAIL = 1
```

Represents an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` signifying that the out of band code was for email verification.

## Public methods

### getData

```
abstract @Nullable String [getData](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getData(int))(@ActionCodeResult.ActionDataKey int key)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#getInfo()`.

Getter for fields pertaining to the operation being performed. Keyed by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey`.

### getInfo

```
abstract @Nullable ActionCodeInfo getInfo()
```

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo` object that holds information regarding the operation being performed.

For `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#VERIFY_EMAIL()` and `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#PASSWORD_RESET()` operations, this will be an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeInfo`

For a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#REVERT_SECOND_FACTOR_ADDITION()` operation, this will be an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeMultiFactorInfo`

For `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#RECOVER_EMAIL()` and `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#VERIFY_BEFORE_CHANGE_EMAIL()` operations, this will return

For a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult#SIGN_IN_WITH_EMAIL_LINK()` operation, this will return null.

Returns null if an error occurred.

### getOperation

```
@ActionCodeResult.Operation
abstract int getOperation()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` for which this out of band code was intended.