# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener.md.txt

# FirebaseAppCheck.AppCheckListener

# FirebaseAppCheck.AppCheckListener


```
public interface FirebaseAppCheck.AppCheckListener
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener#onAppCheckTokenChanged(com.google.firebase.appcheck.AppCheckToken)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken token)` This method gets invoked on the UI thread on changes to the token state. |

## Public methods

### onAppCheckTokenChanged

```
abstract void onAppCheckTokenChanged(@NonNull AppCheckToken token)
```

This method gets invoked on the UI thread on changes to the token state. Does not trigger on token expiry.