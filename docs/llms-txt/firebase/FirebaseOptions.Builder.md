# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder.md.txt

# FirebaseOptions.Builder

# FirebaseOptions.Builder


```
class FirebaseOptions.Builder
```

<br />

*** ** * ** ***

Builder for constructing FirebaseOptions.

## Summary

|                                                                                                                                                        ### Public constructors                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#Builder())`()` Constructs an empty builder.                                                                                                                                                                                    |
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#Builder(com.google.firebase.FirebaseOptions))`(options: `[FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`)` Initializes the builder's values from the options object. |

|                                                   ### Public functions                                                   |
|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#build())`()`                                                                                                                                         |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder) | [setApiKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setApiKey(java.lang.String))`(apiKey: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)`                       |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder) | [setApplicationId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setApplicationId(java.lang.String))`(applicationId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)`  |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder) | [setDatabaseUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setDatabaseUrl(java.lang.String))`(databaseUrl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)`       |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder) | [setGcmSenderId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setGcmSenderId(java.lang.String))`(gcmSenderId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)`       |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder) | [setProjectId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setProjectId(java.lang.String))`(projectId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)`             |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder) | [setStorageBucket](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String))`(storageBucket: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` |

## Public constructors

### Builder

```
Builder()
```

Constructs an empty builder.  

### Builder

```
Builder(options:Â FirebaseOptions)
```

Initializes the builder's values from the options object.

The new builder is not backed by this objects values, that is changes made to the new builder don't change the values of the origin object.  

## Public functions

### build

```
funÂ build():Â FirebaseOptions
```  

### setApiKey

```
funÂ setApiKey(apiKey:Â String):Â FirebaseOptions.Builder
```  

### setApplicationId

```
funÂ setApplicationId(applicationId:Â String):Â FirebaseOptions.Builder
```  

### setDatabaseUrl

```
funÂ setDatabaseUrl(databaseUrl:Â String?):Â FirebaseOptions.Builder
```  

### setGcmSenderId

```
funÂ setGcmSenderId(gcmSenderId:Â String?):Â FirebaseOptions.Builder
```  

### setProjectId

```
funÂ setProjectId(projectId:Â String?):Â FirebaseOptions.Builder
```  

### setStorageBucket

```
funÂ setStorageBucket(storageBucket:Â String?):Â FirebaseOptions.Builder
```