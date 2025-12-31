# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.md.txt

# DebugAppCheckTestHelper

# DebugAppCheckTestHelper


```
class DebugAppCheckTestHelper
```

<br />

*** ** * ** ***

Helper class for using [DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory) in integration tests.

Example Usage:  

```kotlin
@RunWith(AndroidJunit4.class)
public class MyTests {
  private final DebugAppCheckTestHelper debugAppCheckTestHelper =
      DebugAppCheckTestHelper.fromInstrumentationArgs();

  @Test
  public void testWithDefaultApp() {
    debugAppCheckTestHelper.withDebugProvider(() -> {
      // Test code that requires a debug AppCheckToken
    });
  }

  @Test
  public void testWithNonDefaultApp() {
    debugAppCheckTestHelper.withDebugProvider(
        FirebaseApp.getInstance("nonDefaultApp"),
        () -> {
          // Test code that requires a debug AppCheckToken
        });
  }
}
```  

```kotlin
// In build.gradle.kts
android {
  defaultConfig {
    System.getenv("FIREBASE_APP_CHECK_DEBUG_SECRET")?.let { token ->
      testInstrumentationRunnerArguments(
          mapOf("firebaseAppCheckDebugSecret" to token))
    }
  }
}
```

## Summary

|                                                                                                                                             ### Nested types                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `interface `[DebugAppCheckTestHelper.MaybeThrowingRunnable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable)`<E : `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`?>` |

|                                                                     ### Public functions                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[DebugAppCheckTestHelper](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper) | [fromInstrumentationArgs](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#fromInstrumentationArgs())`()` Creates a [DebugAppCheckTestHelper](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper) instance with a debug secret obtained from [InstrumentationRegistry](https://developer.android.com/reference/kotlin/androidx/test/platform/app/InstrumentationRegistry.html) arguments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                  | `<E : `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`?> `[withDebugProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>))`(` ` runnable: `[DebugAppCheckTestHelper.MaybeThrowingRunnable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable)`<E!>` `)` Installs a [DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory) to the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) and runs the test code in `runnable`.                                                                                                                                                      |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                  | `<E : `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`?> `[withDebugProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.FirebaseApp,com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>))`(` ` firebaseApp: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`,` ` runnable: `[DebugAppCheckTestHelper.MaybeThrowingRunnable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable)`<E!>` `)` Installs a [DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory) to the provided [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) and runs the test code in `runnable`. |

## Public functions

### fromInstrumentationArgs

```
java-staticÂ funÂ fromInstrumentationArgs():Â DebugAppCheckTestHelper
```

Creates a [DebugAppCheckTestHelper](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper) instance with a debug secret obtained from [InstrumentationRegistry](https://developer.android.com/reference/kotlin/androidx/test/platform/app/InstrumentationRegistry.html) arguments.  

### withDebugProvider

```
funÂ <EÂ :Â Throwable?> withDebugProvider(
Â Â Â Â runnable:Â DebugAppCheckTestHelper.MaybeThrowingRunnable<E!>
):Â Unit
```

Installs a [DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory) to the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) and runs the test code in `runnable`.  

|                                                                                                                                                                                     Throws                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper: `[com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)) |   |

### withDebugProvider

```
funÂ <EÂ :Â Throwable?> withDebugProvider(
Â Â Â Â firebaseApp:Â FirebaseApp,
Â Â Â Â runnable:Â DebugAppCheckTestHelper.MaybeThrowingRunnable<E!>
):Â Unit
```

Installs a [DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory) to the provided [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) and runs the test code in `runnable`.  

|                                                                                                                                                                                                     Throws                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper: `[com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.FirebaseApp,com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)) |   |