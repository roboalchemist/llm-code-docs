# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.md.txt

# DebugAppCheckTestHelper

# DebugAppCheckTestHelper


```
public final class DebugAppCheckTestHelper
```

<br />

*** ** * ** ***

Helper class for using `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` in integration tests.

Example Usage:

```
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

```
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
| `public interface https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable<E extends https://developer.android.com/reference/kotlin/java/lang/Throwable.html>` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#fromInstrumentationArgs()()` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper` instance with a debug secret obtained from `https://developer.android.com/reference/kotlin/androidx/test/platform/app/InstrumentationRegistry.html` arguments. |
| `void` | `<E extends https://developer.android.com/reference/kotlin/java/lang/Throwable.html> https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable<E> runnable )` Installs a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and runs the test code in `runnable`. |
| `void` | `<E extends https://developer.android.com/reference/kotlin/java/lang/Throwable.html> https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.FirebaseApp,com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper.MaybeThrowingRunnable<E> runnable )` Installs a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and runs the test code in `runnable`. |

## Public methods

### fromInstrumentationArgs

```
public static @NonNull DebugAppCheckTestHelper fromInstrumentationArgs()
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper` instance with a debug secret obtained from `https://developer.android.com/reference/kotlin/androidx/test/platform/app/InstrumentationRegistry.html` arguments.

### withDebugProvider

```
public void <E extends Throwable> withDebugProvider(
    @NonNull DebugAppCheckTestHelper.MaybeThrowingRunnable<E> runnable
)
```

Installs a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and runs the test code in `runnable`.

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>) com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper` |   |

### withDebugProvider

```
public void <E extends Throwable> withDebugProvider(
    @NonNull FirebaseApp firebaseApp,
    @NonNull DebugAppCheckTestHelper.MaybeThrowingRunnable<E> runnable
)
```

Installs a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` to the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and runs the test code in `runnable`.

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/testing/DebugAppCheckTestHelper#withDebugProvider(com.google.firebase.FirebaseApp,com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper.MaybeThrowingRunnable<E>) com.google.firebase.appcheck.debug.testing.DebugAppCheckTestHelper` |   |