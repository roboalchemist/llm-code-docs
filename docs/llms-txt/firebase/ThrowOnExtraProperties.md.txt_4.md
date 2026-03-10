# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ThrowOnExtraProperties.md.txt

# ThrowOnExtraProperties

# ThrowOnExtraProperties


```
@Retention(value = RetentionPolicy.RUNTIME)
@Target(value = [ElementType.TYPE])
annotation ThrowOnExtraProperties
```

<br />

*** ** * ** ***

Properties that don't map to class fields when serializing to a class annotated with this annotation cause an exception to be thrown.