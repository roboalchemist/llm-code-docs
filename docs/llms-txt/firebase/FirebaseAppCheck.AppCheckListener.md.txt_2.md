# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener.md.txt

# FirebaseAppCheck.AppCheckListener

# FirebaseAppCheck.AppCheckListener


```
interface FirebaseAppCheck.AppCheckListener
```

<br />

*** ** * ** ***

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener#onAppCheckTokenChanged(com.google.firebase.appcheck.AppCheckToken)(token: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken)` This method gets invoked on the UI thread on changes to the token state. |

## Public functions

### onAppCheckTokenChanged

```
fun onAppCheckTokenChanged(token: AppCheckToken): Unit
```

This method gets invoked on the UI thread on changes to the token state. Does not trigger on token expiry.