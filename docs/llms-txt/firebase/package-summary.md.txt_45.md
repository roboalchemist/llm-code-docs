# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/package-summary.md.txt

# io.fabric.sdk.android

### Interfaces

|---|---|
| [InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)\<T\> | Callback to use when monitoring `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric` initialization. |
| [KitGroup](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/KitGroup) | Wrapper for a set of logically grouped `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit`'s. |
| [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger) | Interface to support custom logger. |

### Classes

|---|---|
| [ActivityLifecycleManager](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager) | This is a convenience class that wraps the ActivityLifecycleCallbacks registration. |
| [ActivityLifecycleManager.Callbacks](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks) | Override the methods corresponding to the activity. |
| [DefaultLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/DefaultLogger) | Default logger that logs to android.util.Log. |
| [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) | Fabric initializes and stores the provided `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit`'s. |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | Fluent API for creating `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric` instances. |
| [InitializationCallback.Empty](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.Empty) |   |
| [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)\<Result\> | The base class to extend from for classes needing initialization with `https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#with(android.content.Context, io.fabric.sdk.android.Kit...)` |
| [KitInfo](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/KitInfo) |   |
| [SilentLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger) | Silent logger that does nothing. |

### Exceptions

|---|---|
| [InitializationException](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationException) | Represents a Fabric initialization error. |