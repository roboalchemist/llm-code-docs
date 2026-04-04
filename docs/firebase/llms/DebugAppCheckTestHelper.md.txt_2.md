# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.md.txt

# DebugAppCheckTestHelper

# DebugAppCheckTestHelper


```
class DebugAppCheckTestHelper
```

<br />

*** ** * ** ***

Helper class for using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` in integration tests.

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

| ### Nested types |
|---|
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable<E : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?>` |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#fromInstrumentationArgs()()` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper` instance with a debug secret obtained from `https://developer.android.com/reference/kotlin/androidx/test/platform/app/InstrumentationRegistry.html` arguments. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `<E : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)( runnable: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable<E!> )` Installs a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and runs the test code in `runnable`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `<E : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.FirebaseApp,com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)( firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, runnable: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable<E!> )` Installs a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and runs the test code in `runnable`. |

## Public functions

### fromInstrumentationArgs

```
java-static fun fromInstrumentationArgs(): DebugAppCheckTestHelper
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper` instance with a debug secret obtained from `https://developer.android.com/reference/kotlin/androidx/test/platform/app/InstrumentationRegistry.html` arguments.

### withDebugProvider

```
fun <E : Throwable?> withDebugProvider(
    runnable: DebugAppCheckTestHelper.MaybeThrowingRunnable<E!>
): Unit
```

Installs a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and runs the test code in `runnable`.

| Throws |
|---|---|
| `com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)` |   |

### withDebugProvider

```
fun <E : Throwable?> withDebugProvider(
    firebaseApp: FirebaseApp,
    runnable: DebugAppCheckTestHelper.MaybeThrowingRunnable<E!>
): Unit
```

Installs a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and runs the test code in `runnable`.

| Throws |
|---|---|
| `com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.FirebaseApp,com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)` |   |