# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp.md.txt

# FirebaseApp

# FirebaseApp


```
public class FirebaseApp
```

<br />

*** ** * ** ***

The entry point of Firebase SDKs. It holds common configuration and state for Firebase APIs. Most applications don't need to directly interact with FirebaseApp.

For a vast majority of apps, `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider` will handle the initialization of Firebase for the default project that it's configured to work with, via the data contained in the app's `google-services.json` file. This `
ContentProvider` is merged into the app's manifest by default when building with Gradle, and it runs automatically at app launch. **No additional lines of code are needed in this case.**

In the event that an app requires access to another Firebase project **in addition to** the default project, `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)` must be used to create that relationship programmatically. The name parameter must be unique. To connect to the resources exposed by that project, use the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` object returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance(java.lang.String)`, passing it the same name used with `
initializeApp`. This object must be passed to the static accessor of the feature that provides the resource. For example, getInstance is used to access the storage bucket provided by the additional project, whereas getInstance is used to access the default project.

Any `FirebaseApp` initialization must occur only in the main process of the app. Use of Firebase in processes other than the main process is not supported and will likely cause problems related to resource contention.

## Summary

| ### Constants |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#DEFAULT_APP_NAME() = "[DEFAULT]"` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/android/content/Context.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#applicationContext()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#name()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#options()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getApplicationContext()()` Returns the application `https://developer.android.com/reference/kotlin/android/content/Context.html`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getApps(android.content.Context)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context)` Returns a mutable list of all FirebaseApps. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance()()` Returns the default (first initialized) instance of the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the instance identified by the unique name, or throws if it does not exist. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getName()()` Returns the unique name of this app. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getOptions()()` Returns the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions`. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#hashCode()()` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#initializeApp(android.content.Context)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context)` Initializes the default FirebaseApp instance using string resource values - populated from google-services.json. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options)` Initializes the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name )` A factory method to initialize a `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#setAutomaticResourceManagementEnabled(boolean)(boolean enabled)` If set to true it indicates that Firebase should close database connections automatically when the app is in the background. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#toString()()` |

## Constants

### DEFAULT_APP_NAME

```
public static final @NonNull String DEFAULT_APP_NAME = "[DEFAULT]"
```

## Public fields

### applicationContext

```
public final Context applicationContext
```

### name

```
public final String name
```

### options

```
public final FirebaseOptions options
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### getApplicationContext

```
public @NonNull Context getApplicationContext()
```

Returns the application `https://developer.android.com/reference/kotlin/android/content/Context.html`.

### getApps

```
public static @NonNull List<FirebaseApp> getApps(@NonNull Context context)
```

Returns a mutable list of all FirebaseApps.

### getInstance

```
public static @NonNull FirebaseApp getInstance()
```

Returns the default (first initialized) instance of the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if the default app was not initialized. |

### getInstance

```
public static @NonNull FirebaseApp getInstance(@NonNull String name)
```

Returns the instance identified by the unique name, or throws if it does not exist.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | represents the name of the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` was not initialized, either via `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)`. |

### getName

```
public @NonNull String getName()
```

Returns the unique name of this app.

### getOptions

```
public @NonNull FirebaseOptions getOptions()
```

Returns the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions`.

### hashCode

```
public int hashCode()
```

### initializeApp

```
public static @Nullable FirebaseApp initializeApp(@NonNull Context context)
```

Initializes the default FirebaseApp instance using string resource values - populated from google-services.json. It also initializes Firebase Analytics for the current process.

This method is called at app startup time by `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider`. Call this method before any Firebase APIs in components outside the main process.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` values used by the default app instance are read from string resources.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | the default FirebaseApp, if either it has been initialized previously, or Firebase API keys are present in string resources. Returns null otherwise. |

### initializeApp

```
public static @NonNull FirebaseApp initializeApp(@NonNull Context context, @NonNull FirebaseOptions options)
```

Initializes the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance. Same as `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#initializeApp(android.content.Context,com.google.firebase.FirebaseOptions,java.lang.String)`, but it uses `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#DEFAULT_APP_NAME()` as name.

It's only required to call this to initialize Firebase if it's **not possible** to do so automatically in `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider`. Automatic initialization that way is the expected situation.

### initializeApp

```
public static @NonNull FirebaseApp initializeApp(
    @NonNull Context context,
    @NonNull FirebaseOptions options,
    @NonNull String name
)
```

A factory method to initialize a `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context` | represents the `https://developer.android.com/reference/kotlin/android/content/Context.html` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options` | represents the global `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | unique name for the app. It is an error to initialize an app with an already existing name. Starting and ending whitespace characters in the name are ignored (trimmed). |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if an app with the same name has already been initialized. |

### setAutomaticResourceManagementEnabled

```
public void setAutomaticResourceManagementEnabled(boolean enabled)
```

If set to true it indicates that Firebase should close database connections automatically when the app is in the background. Disabled by default.

### toString

```
public String toString()
```