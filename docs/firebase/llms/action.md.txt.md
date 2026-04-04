# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action.md.txt

# Action

# Action


```
public class Action
```

<br />

*** ** * ** ***

Encapsulates an Action for a Firebase In App Message.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action#actionUrl()` !!!!!WARNING!!!!! We are overriding equality in this class. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action#button()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action#getActionUrl()()` Gets the URL associated with this action |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action#getButton()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` associated with this action |

## Public fields

### actionUrl

```
public final @Nullable String actionUrl
```

!!!!!WARNING!!!!! We are overriding equality in this class. Please add equality checks for all new private class members.

### button

```
public final @Nullable Button button
```

## Public methods

### getActionUrl

```
public @Nullable String getActionUrl()
```

Gets the URL associated with this action

### getButton

```
public @Nullable Button getButton()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` associated with this action