# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.md.txt

# FirebaseFunctions

# FirebaseFunctions


```
class FirebaseFunctions
```

<br />

*** ** * ** ***

FirebaseFunctions lets you call Cloud Functions for Firebase.

## Summary

|                                             ### Public companion functions                                             |
|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseFunctions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance())`()` Creates a Cloud Functions client with the default app.                                                                                                                                                                                                                                                                                         |
| [FirebaseFunctions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp))`(app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)` Creates a Cloud Functions client with the given app.                                                                                                                                                     |
| [FirebaseFunctions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(kotlin.String))`(regionOrCustomDomain: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates a Cloud Functions client with the default app and given region or custom domain.                                                                                                                                  |
| [FirebaseFunctions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String))`(app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`, regionOrCustomDomain: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates a Cloud Functions client with the given app and region or custom domain. |

|                                                       ### Public functions                                                       |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [HttpsCallableReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference) | [getHttpsCallable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallable(kotlin.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a reference to the callable HTTPS trigger with the given name.                                                                                                                                                                                                                   |
| [HttpsCallableReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference) | [getHttpsCallable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallable(kotlin.String,com.google.firebase.functions.HttpsCallableOptions))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, options: `[HttpsCallableOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions)`)` Returns a reference to the callable HTTPS trigger with the given name and call options.      |
| [HttpsCallableReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference) | [getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallableFromUrl(java.net.URL))`(url: `[URL](https://developer.android.com/reference/kotlin/java/net/URL.html)`)` Returns a reference to the callable HTTPS trigger with the provided URL.                                                                                                                                                                                                              |
| [HttpsCallableReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference) | [getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallableFromUrl(java.net.URL,com.google.firebase.functions.HttpsCallableOptions))`(url: `[URL](https://developer.android.com/reference/kotlin/java/net/URL.html)`, options: `[HttpsCallableOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions)`)` Returns a reference to the callable HTTPS trigger with the provided URL and call options. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                     | [useEmulator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#useEmulator(kotlin.String,kotlin.Int))`(host: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, port: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Modifies this FirebaseFunctions instance to communicate with the Cloud Functions emulator.                                                                                                          |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                     | ~~[useFunctionsEmulator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#useFunctionsEmulator(kotlin.String))~~`(origin: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` **This function is deprecated.** Use useEmulator to connect to the emulator.                                                                                                                                                                                               |

|                                                     ### Extension functions                                                      |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [HttpsCallableReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference) | [FirebaseFunctions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions)`.`[getHttpsCallable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, init: `[HttpsCallableOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Returns a reference to the Callable HTTPS trigger with the given name and call options.   |
| [HttpsCallableReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference) | [FirebaseFunctions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions)`.`[getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1))`(url: `[URL](https://developer.android.com/reference/kotlin/java/net/URL.html)`, init: `[HttpsCallableOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Returns a reference to the Callable HTTPS trigger with the given URL and call options. |

## Public companion functions

### getInstance

```
funÂ getInstance():Â FirebaseFunctions
```

Creates a Cloud Functions client with the default app.  

### getInstance

```
funÂ getInstance(app:Â FirebaseApp):Â FirebaseFunctions
```

Creates a Cloud Functions client with the given app.  

|                                               Parameters                                                |
|---------------------------------------------------------------------------------------------------------|-----------------------------------|
| `app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) | The app for the Firebase project. |

### getInstance

```
funÂ getInstance(regionOrCustomDomain:Â String):Â FirebaseFunctions
```

Creates a Cloud Functions client with the default app and given region or custom domain.  

|                                                Parameters                                                |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `regionOrCustomDomain: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

### getInstance

```
funÂ getInstance(app:Â FirebaseApp,Â regionOrCustomDomain:Â String):Â FirebaseFunctions
```

Creates a Cloud Functions client with the given app and region or custom domain.  

|                                                Parameters                                                |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)  | The app for the Firebase project.                                                                       |
| `regionOrCustomDomain: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

## Public functions

### getHttpsCallable

```
funÂ getHttpsCallable(name:Â String):Â HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the given name.  

### getHttpsCallable

```
funÂ getHttpsCallable(name:Â String,Â options:Â HttpsCallableOptions):Â HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the given name and call options.  

### getHttpsCallableFromUrl

```
funÂ getHttpsCallableFromUrl(url:Â URL):Â HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the provided URL.  

### getHttpsCallableFromUrl

```
funÂ getHttpsCallableFromUrl(url:Â URL,Â options:Â HttpsCallableOptions):Â HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the provided URL and call options.  

### useEmulator

```
funÂ useEmulator(host:Â String,Â port:Â Int):Â Unit
```

Modifies this FirebaseFunctions instance to communicate with the Cloud Functions emulator.

Note: Call this method before using the instance to do any functions operations.  

|                                        Parameters                                        |
|------------------------------------------------------------------------------------------|-------------------------------------------|
| `host: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the emulator host (for example, 10.0.2.2) |
| `port: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)       | the emulator port (for example, 5001)     |

### useFunctionsEmulator

```
funÂ [useFunctionsEmulator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#useFunctionsEmulator(kotlin.String))(origin:Â String):Â Unit
```
| **This function is deprecated.**   
Use useEmulator to connect to the emulator.  

## Extension functions

### getHttpsCallable

```
funÂ FirebaseFunctions.getHttpsCallable(name:Â String,Â init:Â HttpsCallableOptions.Builder.() -> Unit):Â HttpsCallableReference
```

Returns a reference to the Callable HTTPS trigger with the given name and call options.  

### getHttpsCallableFromUrl

```
funÂ FirebaseFunctions.getHttpsCallableFromUrl(url:Â URL,Â init:Â HttpsCallableOptions.Builder.() -> Unit):Â HttpsCallableReference
```

Returns a reference to the Callable HTTPS trigger with the given URL and call options.