# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult.ActionDataKey.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.ActionDataKey.md.txt

# ActionCodeResult.ActionDataKey

# ActionCodeResult.ActionDataKey


```
@IntDef(valueÂ =Â )
@Retention(valueÂ =Â RetentionPolicy.SOURCE)
annotation ActionCodeResult.ActionDataKey
```

<br />

*** ** * ** ***

Keys to access the account information related to an out of band code. `FROM_EMAIL` at all times signifies the email which was the current email before the application of the out of band code. `EMAIL` signifies the current email associated with the account, which may have changed as a result of the [Operation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeResult.Operation) performed.