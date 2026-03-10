# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp.md.txt

# FirebaseApp

# FirebaseApp


```
class FirebaseApp
```

<br />

*** ** * ** ***

The entry point of Firebase SDKs. It holds common configuration and state for Firebase APIs. Most applications don't need to directly interact with FirebaseApp.

For a vast majority of apps, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider` will handle the initialization of Firebase for the default project that it's configured to work with, via the data contained in the app's `google-services.json` file. This `
ContentProvider` is merged into the app's manifest by default when building with Gradle, and it runs automatically at app launch. **No additional lines of code are needed in this case.**

In the event that an app requires access to another Firebase project **in addition to** the default project, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)` must be used to create that relationship programmatically. The name parameter must be unique. To connect to the resources exposed by that project, use the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` object returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance(java.lang.String)`, passing it the same name used with `
initializeApp`. This object must be passed to the static accessor of the feature that provides the resource. For example, getInstance is used to access the storage bucket provided by the additional project, whereas getInstance is used to access the default project.

Any `FirebaseApp` initialization must occur only in the main process of the app. Use of Firebase in processes other than the main process is not supported and will likely cause problems related to resource contention.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#DEFAULT_APP_NAME() = "[DEFAULT]"` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `java-static (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getApps(android.content.Context)(context: https://developer.android.com/reference/kotlin/android/content/Context.html)` Returns a mutable list of all FirebaseApps. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance()()` Returns the default (first initialized) instance of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the instance identified by the unique name, or throws if it does not exist. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#hashCode()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context)(context: https://developer.android.com/reference/kotlin/android/content/Context.html)` Initializes the default FirebaseApp instance using string resource values - populated from google-services.json. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions)(context: https://developer.android.com/reference/kotlin/android/content/Context.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)` Initializes the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)(context: https://developer.android.com/reference/kotlin/android/content/Context.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions, name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` A factory method to initialize a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#setAutomaticResourceManagementEnabled(boolean)(enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` If set to true it indicates that Firebase should close database connections automatically when the app is in the background. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#toString()()` |

| ### Public properties |
|---|---|
| `https://developer.android.com/reference/kotlin/android/content/Context.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#applicationContext()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#name()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#options()` |

## Constants

### DEFAULT_APP_NAME

```
const val DEFAULT_APP_NAME = "[DEFAULT]": String
```

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### getApps

```
java-static fun getApps(context: Context): (Mutable)List<FirebaseApp!>
```

Returns a mutable list of all FirebaseApps.

### getInstance

```
java-static fun getInstance(): FirebaseApp
```

Returns the default (first initialized) instance of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if the default app was not initialized. |

### getInstance

```
java-static fun getInstance(name: String): FirebaseApp
```

Returns the instance identified by the unique name, or throws if it does not exist.

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | represents the name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance. |

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` was not initialized, either via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)`. |

### hashCode

```
fun hashCode(): Int
```

### initializeApp

```
java-static fun initializeApp(context: Context): FirebaseApp?
```

Initializes the default FirebaseApp instance using string resource values - populated from google-services.json. It also initializes Firebase Analytics for the current process.

This method is called at app startup time by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider`. Call this method before any Firebase APIs in components outside the main process.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` values used by the default app instance are read from string resources.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp?` | the default FirebaseApp, if either it has been initialized previously, or Firebase API keys are present in string resources. Returns null otherwise. |

### initializeApp

```
java-static fun initializeApp(context: Context, options: FirebaseOptions): FirebaseApp
```

Initializes the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance. Same as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)`, but it uses `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#DEFAULT_APP_NAME()` as name.

It's only required to call this to initialize Firebase if it's **not possible** to do so automatically in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider`. Automatic initialization that way is the expected situation.

### initializeApp

```
java-static fun initializeApp(context: Context, options: FirebaseOptions, name: String): FirebaseApp
```

A factory method to initialize a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

| Parameters |
|---|---|
| `context: https://developer.android.com/reference/kotlin/android/content/Context.html` | represents the `https://developer.android.com/reference/kotlin/android/content/Context.html` |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` | represents the global `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` |
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | unique name for the app. It is an error to initialize an app with an already existing name. Starting and ending whitespace characters in the name are ignored (trimmed). |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` |

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if an app with the same name has already been initialized. |

### setAutomaticResourceManagementEnabled

```
fun setAutomaticResourceManagementEnabled(enabled: Boolean): Unit
```

If set to true it indicates that Firebase should close database connections automatically when the app is in the background. Disabled by default.

### toString

```
fun toString(): String!
```

## Public properties

### applicationContext

```
val applicationContext: Context!
```

### name

```
val name: String!
```

### options

```
val options: FirebaseOptions!
```