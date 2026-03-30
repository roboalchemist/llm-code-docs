# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder.md.txt

# ConsentBuilder

# ConsentBuilder


```
public final class ConsentBuilder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Helper class used to enable fluent syntax in `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1)`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder#ConsentBuilder()()` |

| ### Public methods |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder#getAdStorage()()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder#getAnalyticsStorage()()` |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder#setAdStorage(com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus)(https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus adStorage)` |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder#setAnalyticsStorage(com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus)(https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus analyticsStorage)` |

## Public constructors

### ConsentBuilder

```
public ConsentBuilder()
```

## Public methods

### getAdStorage

```
public final FirebaseAnalytics.ConsentStatus getAdStorage()
```

### getAnalyticsStorage

```
public final FirebaseAnalytics.ConsentStatus getAnalyticsStorage()
```

### setAdStorage

```
public final void setAdStorage(FirebaseAnalytics.ConsentStatus adStorage)
```

### setAnalyticsStorage

```
public final void setAnalyticsStorage(FirebaseAnalytics.ConsentStatus analyticsStorage)
```