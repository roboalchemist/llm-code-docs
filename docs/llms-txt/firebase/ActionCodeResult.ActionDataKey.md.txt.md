# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey.md.txt

# ActionCodeResult.ActionDataKey

# ActionCodeResult.ActionDataKey


```
@IntDef(value = )
@Retention(value = RetentionPolicy.SOURCE)
public annotation ActionCodeResult.ActionDataKey
```

<br />

*** ** * ** ***

Keys to access the account information related to an out of band code. `FROM_EMAIL` at all times signifies the email which was the current email before the application of the out of band code. `EMAIL` signifies the current email associated with the account, which may have changed as a result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.Operation` performed.