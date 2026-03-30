# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider.md.txt

# FirebaseInitProvider

# FirebaseInitProvider


```
public class FirebaseInitProvider extends ContentProvider
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [android.content.ContentProvider](https://developer.android.com/reference/kotlin/android/content/ContentProvider.html) ||
|   | ↳ | [com.google.firebase.provider.FirebaseInitProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider) |

*** ** * ** ***

Initializes Firebase APIs at app startup time.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#FirebaseInitProvider()()` |

| ### Public methods |
|---|---|
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#attachInfo(android.content.Context,android.content.pm.ProviderInfo)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/pm/ProviderInfo.html info)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#delete(android.net.Uri,java.lang.String,java.lang.String[])( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html selection, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html String[] selectionArgs )` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#getType(android.net.Uri)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#insert(android.net.Uri,android.content.ContentValues)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/content/ContentValues.html values)` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#onCreate()()` Called before `https://developer.android.com/reference/kotlin/android/app/Application.html#onCreate--`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/database/Cursor.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html String[] projection, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html selection, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html String[] selectionArgs, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html sortOrder )` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/provider/FirebaseInitProvider#update(android.net.Uri,android.content.ContentValues,java.lang.String,java.lang.String[])( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/content/ContentValues.html values, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html selection, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html String[] selectionArgs )` |

| ### Inherited Constants |
|---|
| From [android.content.ComponentCallbacks2](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html) |---|---| | `static final int` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_BACKGROUND-- = 40` | | `static final int` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_COMPLETE-- = 80` | | `static final int` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_MODERATE-- = 60` | | `static final int` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_CRITICAL-- = 15` | | `static final int` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_LOW-- = 10` | | `static final int` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_MODERATE-- = 5` | | `static final int` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_UI_HIDDEN-- = 20` | |

| ### Inherited methods |
|---|
| From [android.content.ContentProvider](https://developer.android.com/reference/kotlin/android/content/ContentProvider.html) |---|---| | `ContentProviderResult[]` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#applyBatch-java.lang.String-java.util.ArrayList&lt;android.content.ContentProviderOperation&gt;-( https://developer.android.com/reference/kotlin/java/lang/String.html authority, https://developer.android.com/reference/kotlin/java/util/ArrayList.html<https://developer.android.com/reference/kotlin/android/content/ContentProviderOperation.html> operations )` | | `int` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#bulkInsert-android.net.Uri-android.content.ContentValues[]-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri, ContentValues[] values)` | | `https://developer.android.com/reference/kotlin/android/os/Bundle.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#call-java.lang.String-java.lang.String-java.lang.String-android.os.Bundle-(https://developer.android.com/reference/kotlin/java/lang/String.html authority, https://developer.android.com/reference/kotlin/java/lang/String.html method, https://developer.android.com/reference/kotlin/java/lang/String.html arg, https://developer.android.com/reference/kotlin/android/os/Bundle.html extras)` | | `https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#canonicalize-android.net.Uri-(https://developer.android.com/reference/kotlin/android/net/Uri.html url)` | | `final https://developer.android.com/reference/kotlin/android/content/ContentProvider.CallingIdentity.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#clearCallingIdentity--()` | | `void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#dump-java.io.FileDescriptor-java.io.PrintWriter-java.lang.String[]-(https://developer.android.com/reference/kotlin/java/io/FileDescriptor.html fd, https://developer.android.com/reference/kotlin/java/io/PrintWriter.html writer, String[] args)` | | `final https://developer.android.com/reference/kotlin/android/content/AttributionSource.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingAttributionSource--()` | | `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingAttributionTag--()` | | `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingPackage--()` | | `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingPackageUnchecked--()` | | `final https://developer.android.com/reference/kotlin/android/content/Context.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getContext--()` | | `final PathPermission[]` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getPathPermissions--()` | | `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getReadPermission--()` | | `String[]` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getStreamTypes-android.net.Uri-java.lang.String-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri, https://developer.android.com/reference/kotlin/java/lang/String.html mimeTypeFilter)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getTypeAnonymous-android.net.Uri-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri)` | | `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getWritePermission--()` | | `boolean` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#isTemporary--()` | | `void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onCallingPackageChanged--()` | | `void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onConfigurationChanged-android.content.res.Configuration-(https://developer.android.com/reference/kotlin/android/content/res/Configuration.html newConfig)` | | `void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onLowMemory--()` | | `void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onTrimMemory-int-(int level)` | | `https://developer.android.com/reference/kotlin/android/content/res/AssetFileDescriptor.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openAssetFile-android.net.Uri-java.lang.String-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri, https://developer.android.com/reference/kotlin/java/lang/String.html mode)` | | `https://developer.android.com/reference/kotlin/android/os/ParcelFileDescriptor.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openFile-android.net.Uri-java.lang.String-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri, https://developer.android.com/reference/kotlin/java/lang/String.html mode)` | | `final https://developer.android.com/reference/kotlin/android/os/ParcelFileDescriptor.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openFileHelper-android.net.Uri-java.lang.String-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri, https://developer.android.com/reference/kotlin/java/lang/String.html mode)` | | `https://developer.android.com/reference/kotlin/android/os/ParcelFileDescriptor.html` | `<T> https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openPipeHelper-android.net.Uri-java.lang.String-android.os.Bundle-T-android.content.ContentProvider.PipeDataWriter&lt;T&gt;-( https://developer.android.com/reference/kotlin/android/net/Uri.html uri, https://developer.android.com/reference/kotlin/java/lang/String.html mimeType, https://developer.android.com/reference/kotlin/android/os/Bundle.html opts, T args, https://developer.android.com/reference/kotlin/android/content/ContentProvider.PipeDataWriter.html<T> func )` | | `https://developer.android.com/reference/kotlin/android/content/res/AssetFileDescriptor.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openTypedAssetFile-android.net.Uri-java.lang.String-android.os.Bundle-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri, https://developer.android.com/reference/kotlin/java/lang/String.html mimeTypeFilter, https://developer.android.com/reference/kotlin/android/os/Bundle.html opts)` | | `boolean` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#refresh-android.net.Uri-android.os.Bundle-android.os.CancellationSignal-(https://developer.android.com/reference/kotlin/android/net/Uri.html uri, https://developer.android.com/reference/kotlin/android/os/Bundle.html extras, https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html cancellationSignal)` | | `final https://developer.android.com/reference/kotlin/android/content/Context.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#requireContext--()` | | `final void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#restoreCallingIdentity-android.content.ContentProvider.CallingIdentity-(https://developer.android.com/reference/kotlin/android/content/ContentProvider.CallingIdentity.html identity)` | | `final void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#setPathPermissions-android.content.pm.PathPermission[]-(PathPermission[] permissions)` | | `final void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#setReadPermission-java.lang.String-(https://developer.android.com/reference/kotlin/java/lang/String.html permission)` | | `final void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#setWritePermission-java.lang.String-(https://developer.android.com/reference/kotlin/java/lang/String.html permission)` | | `void` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#shutdown--()` | | `https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#uncanonicalize-android.net.Uri-(https://developer.android.com/reference/kotlin/android/net/Uri.html url)` | |

## Public constructors

### FirebaseInitProvider

```
public FirebaseInitProvider()
```

## Public methods

### attachInfo

```
public void attachInfo(@NonNull Context context, @NonNull ProviderInfo info)
```

### delete

```
public int delete(
    @NonNull Uri uri,
    @Nullable String selection,
    @Nullable String[] selectionArgs
)
```

### getType

```
public @Nullable String getType(@NonNull Uri uri)
```

### insert

```
public @Nullable Uri insert(@NonNull Uri uri, @Nullable ContentValues values)
```

### onCreate

```
public boolean onCreate()
```

Called before `https://developer.android.com/reference/kotlin/android/app/Application.html#onCreate--`.

### query

```
public @Nullable Cursor query(
    @NonNull Uri uri,
    @Nullable String[] projection,
    @Nullable String selection,
    @Nullable String[] selectionArgs,
    @Nullable String sortOrder
)
```

### update

```
public int update(
    @NonNull Uri uri,
    @Nullable ContentValues values,
    @Nullable String selection,
    @Nullable String[] selectionArgs
)
```