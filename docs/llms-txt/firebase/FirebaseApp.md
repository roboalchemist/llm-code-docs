# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp.md.txt

# FirebaseApp

# FirebaseApp


```
class FirebaseApp
```

<br />

*** ** * ** ***

The entry point of Firebase SDKs. It holds common configuration and state for Firebase APIs. Most applications don't need to directly interact with FirebaseApp.

For a vast majority of apps, [FirebaseInitProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider) will handle the initialization of Firebase for the default project that it's configured to work with, via the data contained in the app's `google-services.json` file. This `
ContentProvider` is merged into the app's manifest by default when building with Gradle, and it runs automatically at app launch. **No additional lines of code are needed in this case.**

In the event that an app requires access to another Firebase project **in addition to** the default project, [initializeApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)) must be used to create that relationship programmatically. The name parameter must be unique. To connect to the resources exposed by that project, use the [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) object returned by [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance(java.lang.String)), passing it the same name used with `
initializeApp`. This object must be passed to the static accessor of the feature that provides the resource. For example, getInstance is used to access the storage bucket provided by the additional project, whereas getInstance is used to access the default project.

Any `FirebaseApp` initialization must occur only in the main process of the app. Use of Firebase in processes other than the main process is not supported and will likely cause problems related to resource contention.

## Summary

|                                      ### Constants                                       |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [DEFAULT_APP_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#DEFAULT_APP_NAME())` = "[DEFAULT]"` |

|                                                                                                                                                 ### Public functions                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                   | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `java-static (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`!>` | [getApps](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getApps(android.content.Context))`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`)` Returns a mutable list of all FirebaseApps.                                                                                                                                                                                                                                                                                                                                                                        |
| `java-static `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)                                                                                                                                                                                                       | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance())`()` Returns the default (first initialized) instance of the [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                          |
| `java-static `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)                                                                                                                                                                                                       | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the instance identified by the unique name, or throws if it does not exist.                                                                                                                                                                                                                                                                                                                                        |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                                                                                                           | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#hashCode())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `java-static `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`?`                                                                                                                                                                                                    | [initializeApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context))`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`)` Initializes the default FirebaseApp instance using string resource values - populated from google-services.json.                                                                                                                                                                                                                                                                                       |
| `java-static `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)                                                                                                                                                                                                       | [initializeApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions))`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`, options: `[FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`)` Initializes the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance.                                                                                                            |
| `java-static `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)                                                                                                                                                                                                       | [initializeApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String))`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`, options: `[FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`, name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` A factory method to initialize a [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp). |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                                                                                                         | [setAutomaticResourceManagementEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#setAutomaticResourceManagementEnabled(boolean))`(enabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` If set to true it indicates that Firebase should close database connections automatically when the app is in the background.                                                                                                                                                                                                                                               |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                                                                                                                                                  | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#toString())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

|                                            ### Public properties                                            |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`!`                   | [applicationContext](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#applicationContext()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                         | [name](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#name())                             |
| [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`!` | [options](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#options())                       |

## Constants

### DEFAULT_APP_NAME

```
constÂ valÂ DEFAULT_APP_NAME = "[DEFAULT]":Â String
```  

## Public functions

### equals

```
funÂ equals(o:Â Any!):Â Boolean
```  

### getApps

```
java-staticÂ funÂ getApps(context:Â Context):Â (Mutable)List<FirebaseApp!>
```

Returns a mutable list of all FirebaseApps.  

### getInstance

```
java-staticÂ funÂ getInstance():Â FirebaseApp
```

Returns the default (first initialized) instance of the [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).  

|                                                                          Throws                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html) | if the default app was not initialized. |

### getInstance

```
java-staticÂ funÂ getInstance(name:Â String):Â FirebaseApp
```

Returns the instance identified by the unique name, or throws if it does not exist.  

|                                        Parameters                                        |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | represents the name of the [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance. |

|                                                                          Throws                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html) | if the [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) was not initialized, either via [initializeApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)). |

### hashCode

```
funÂ hashCode():Â Int
```  

### initializeApp

```
java-staticÂ funÂ initializeApp(context:Â Context):Â FirebaseApp?
```

Initializes the default FirebaseApp instance using string resource values - populated from google-services.json. It also initializes Firebase Analytics for the current process.

This method is called at app startup time by [FirebaseInitProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider). Call this method before any Firebase APIs in components outside the main process.

The [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions) values used by the default app instance are read from string resources.  

|                                               Returns                                               |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`?` | the default FirebaseApp, if either it has been initialized previously, or Firebase API keys are present in string resources. Returns null otherwise. |

### initializeApp

```
java-staticÂ funÂ initializeApp(context:Â Context,Â options:Â FirebaseOptions):Â FirebaseApp
```

Initializes the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance. Same as [initializeApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)), but it uses [DEFAULT_APP_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#DEFAULT_APP_NAME()) as name.

It's only required to call this to initialize Firebase if it's **not possible** to do so automatically in [FirebaseInitProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider). Automatic initialization that way is the expected situation.  

### initializeApp

```
java-staticÂ funÂ initializeApp(context:Â Context,Â options:Â FirebaseOptions,Â name:Â String):Â FirebaseApp
```

A factory method to initialize a [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).  

|                                                     Parameters                                                      |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)                   | represents the [Context](https://developer.android.com/reference/kotlin/android/content/Context.html)                                                                    |
| `options: `[FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions) | represents the global [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)                                           |
| `name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                            | unique name for the app. It is an error to initialize an app with an already existing name. Starting and ending whitespace characters in the name are ignored (trimmed). |

|                                             Returns                                              |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) | an instance of [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) |

|                                                                          Throws                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html) | if an app with the same name has already been initialized. |

### setAutomaticResourceManagementEnabled

```
funÂ setAutomaticResourceManagementEnabled(enabled:Â Boolean):Â Unit
```

If set to true it indicates that Firebase should close database connections automatically when the app is in the background. Disabled by default.  

### toString

```
funÂ toString():Â String!
```  

## Public properties

### applicationContext

```
valÂ applicationContext:Â Context!
```  

### name

```
valÂ name:Â String!
```  

### options

```
valÂ options:Â FirebaseOptions!
```