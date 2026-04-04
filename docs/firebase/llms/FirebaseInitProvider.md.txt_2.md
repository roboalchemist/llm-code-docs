# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider.md.txt

# FirebaseInitProvider

# FirebaseInitProvider


```
class FirebaseInitProvider : ContentProvider
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [android.content.ContentProvider](https://developer.android.com/reference/kotlin/android/content/ContentProvider.html) ||
|   | ↳ | [com.google.firebase.provider.FirebaseInitProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider) |

*** ** * ** ***

Initializes Firebase APIs at app startup time.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#FirebaseInitProvider()()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#attachInfo(android.content.Context,android.content.pm.ProviderInfo)(context: https://developer.android.com/reference/kotlin/android/content/Context.html, info: https://developer.android.com/reference/kotlin/android/content/pm/ProviderInfo.html)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#delete(android.net.Uri,java.lang.String,java.lang.String[])(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html, selection: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, selectionArgs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#getType(android.net.Uri)(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html)` |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#insert(android.net.Uri,android.content.ContentValues)(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html, values: https://developer.android.com/reference/kotlin/android/content/ContentValues.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#onCreate()()` Called before `https://developer.android.com/reference/kotlin/android/app/Application.html#onCreate--`. |
| `https://developer.android.com/reference/kotlin/android/database/Cursor.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)( uri: https://developer.android.com/reference/kotlin/android/net/Uri.html, projection: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?, selection: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, selectionArgs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?, sortOrder: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/provider/FirebaseInitProvider#update(android.net.Uri,android.content.ContentValues,java.lang.String,java.lang.String[])( uri: https://developer.android.com/reference/kotlin/android/net/Uri.html, values: https://developer.android.com/reference/kotlin/android/content/ContentValues.html?, selection: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, selectionArgs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>? )` |

| ### Inherited Constants |
|---|
| From [android.content.ComponentCallbacks2](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_BACKGROUND-- = 40` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_COMPLETE-- = 80` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_MODERATE-- = 60` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_CRITICAL-- = 15` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_LOW-- = 10` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_MODERATE-- = 5` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_UI_HIDDEN-- = 20` | |

| ### Inherited functions |
|---|
| From [android.content.ContentProvider](https://developer.android.com/reference/kotlin/android/content/ContentProvider.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/android/content/ContentProviderResult.html!>!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#applyBatch-java.lang.String-java.util.ArrayList&lt;android.content.ContentProviderOperation&gt;-( authority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, operations: https://developer.android.com/reference/kotlin/java/util/ArrayList.html<https://developer.android.com/reference/kotlin/android/content/ContentProviderOperation.html!>! )` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#bulkInsert-android.net.Uri-android.content.ContentValues[]-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/android/content/ContentValues.html!>!)` | | `https://developer.android.com/reference/kotlin/android/os/Bundle.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#call-java.lang.String-java.lang.String-java.lang.String-android.os.Bundle-(authority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, method: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, arg: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, extras: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `https://developer.android.com/reference/kotlin/android/net/Uri.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#canonicalize-android.net.Uri-(url: https://developer.android.com/reference/kotlin/android/net/Uri.html!)` | | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.CallingIdentity.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#clearCallingIdentity--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#dump-java.io.FileDescriptor-java.io.PrintWriter-java.lang.String[]-(fd: https://developer.android.com/reference/kotlin/java/io/FileDescriptor.html!, writer: https://developer.android.com/reference/kotlin/java/io/PrintWriter.html!, args: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>!)` | | `https://developer.android.com/reference/kotlin/android/content/AttributionSource.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingAttributionSource--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingAttributionTag--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingPackage--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getCallingPackageUnchecked--()` | | `https://developer.android.com/reference/kotlin/android/content/Context.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getContext--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/android/content/pm/PathPermission.html!>!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getPathPermissions--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getReadPermission--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getStreamTypes-android.net.Uri-java.lang.String-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, mimeTypeFilter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getTypeAnonymous-android.net.Uri-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#getWritePermission--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#isTemporary--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onCallingPackageChanged--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onConfigurationChanged-android.content.res.Configuration-(newConfig: https://developer.android.com/reference/kotlin/android/content/res/Configuration.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onLowMemory--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#onTrimMemory-int-(level: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | | `https://developer.android.com/reference/kotlin/android/content/res/AssetFileDescriptor.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openAssetFile-android.net.Uri-java.lang.String-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, mode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` | | `https://developer.android.com/reference/kotlin/android/os/ParcelFileDescriptor.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openFile-android.net.Uri-java.lang.String-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, mode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` | | `https://developer.android.com/reference/kotlin/android/os/ParcelFileDescriptor.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openFileHelper-android.net.Uri-java.lang.String-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, mode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` | | `https://developer.android.com/reference/kotlin/android/os/ParcelFileDescriptor.html!` | `<T> https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openPipeHelper-android.net.Uri-java.lang.String-android.os.Bundle-T-android.content.ContentProvider.PipeDataWriter&lt;T&gt;-( uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, opts: https://developer.android.com/reference/kotlin/android/os/Bundle.html!, args: T!, func: https://developer.android.com/reference/kotlin/android/content/ContentProvider.PipeDataWriter.html<T!>! )` | | `https://developer.android.com/reference/kotlin/android/content/res/AssetFileDescriptor.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#openTypedAssetFile-android.net.Uri-java.lang.String-android.os.Bundle-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, mimeTypeFilter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, opts: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#refresh-android.net.Uri-android.os.Bundle-android.os.CancellationSignal-(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html!, extras: https://developer.android.com/reference/kotlin/android/os/Bundle.html!, cancellationSignal: https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html!)` | | `https://developer.android.com/reference/kotlin/android/content/Context.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#requireContext--()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#restoreCallingIdentity-android.content.ContentProvider.CallingIdentity-(identity: https://developer.android.com/reference/kotlin/android/content/ContentProvider.CallingIdentity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#setPathPermissions-android.content.pm.PathPermission[]-(permissions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/android/content/pm/PathPermission.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#setReadPermission-java.lang.String-(permission: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#setWritePermission-java.lang.String-(permission: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#shutdown--()` | | `https://developer.android.com/reference/kotlin/android/net/Uri.html!` | `https://developer.android.com/reference/kotlin/android/content/ContentProvider.html#uncanonicalize-android.net.Uri-(url: https://developer.android.com/reference/kotlin/android/net/Uri.html!)` | |

## Public constructors

### FirebaseInitProvider

```
FirebaseInitProvider()
```

## Public functions

### attachInfo

```
fun attachInfo(context: Context, info: ProviderInfo): Unit
```

### delete

```
fun delete(uri: Uri, selection: String?, selectionArgs: Array<String!>?): Int
```

### getType

```
fun getType(uri: Uri): String?
```

### insert

```
fun insert(uri: Uri, values: ContentValues?): Uri?
```

### onCreate

```
fun onCreate(): Boolean
```

Called before `https://developer.android.com/reference/kotlin/android/app/Application.html#onCreate--`.

### query

```
fun query(
    uri: Uri,
    projection: Array<String!>?,
    selection: String?,
    selectionArgs: Array<String!>?,
    sortOrder: String?
): Cursor?
```

### update

```
fun update(
    uri: Uri,
    values: ContentValues?,
    selection: String?,
    selectionArgs: Array<String!>?
): Int
```