# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.md.txt

# Firebase

# Firebase


```
object Firebase
```

<br />

*** ** * ** ***

All fields in this object are deprecated; Use `com.google.firebase.Firebase` instead.

Single access point to all firebase SDKs from Kotlin. Acts as a target for extension methods provided by sdks.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

|                                       ### Extension functions                                       |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)    | [Firebase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase)`.`[app](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).app(kotlin.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.                                                                                                                                                                                                                                                                                                                        |
| [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`?` | [Firebase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase)`.`~~[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).initialize(android.content.Context))~~`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                                                                                                                                                                                                                                             |
| [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)    | [Firebase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase)`.`~~[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions))~~`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`, options: `[FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                                                                                    |
| [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)    | [Firebase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase)`.`~~[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String))~~`(` ` context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`,` ` options: `[FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`,` ` name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) `)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

|                                         ### Extension properties                                         |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)         | [Firebase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase)`.`[app](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).app()) Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.         |
| [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions) | [Firebase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase)`.`[options](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).options()) Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions

### app

```
funÂ Firebase.app(name:Â String):Â FirebaseApp
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns a named firebase app instance.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### initialize

```
funÂ Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).initialize(android.content.Context))(context:Â Context):Â FirebaseApp?
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### initialize

```
funÂ Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions))(context:Â Context,Â options:Â FirebaseOptions):Â FirebaseApp
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### initialize

```
funÂ Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String))(
Â Â Â Â context:Â Context,
Â Â Â Â options:Â FirebaseOptions,
Â Â Â Â name:Â String
):Â FirebaseApp
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

## Extension properties

### app

```
valÂ Firebase.app:Â FirebaseApp
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns the default firebase app instance.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### options

```
valÂ Firebase.options:Â FirebaseOptions
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns options of default FirebaseApp

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)