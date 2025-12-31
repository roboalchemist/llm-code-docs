# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener.md.txt

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
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract void`    | [onAppCheckTokenChanged](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener#onAppCheckTokenChanged(com.google.firebase.appcheck.AppCheckToken))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken)` token)` This method gets invoked on the UI thread on changes to the token state. |

## Public methods

### onAppCheckTokenChanged

```
abstractÂ voidÂ onAppCheckTokenChanged(@NonNull AppCheckTokenÂ token)
```

This method gets invoked on the UI thread on changes to the token state. Does not trigger on token expiry.