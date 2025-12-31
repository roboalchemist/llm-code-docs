# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex.md.txt

# AppIndex

public final class **AppIndex** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

Please [Migrate to the
Firebase App Indexing API](https://firebase.google.com/docs/app-indexing/android/migrate)  

### Field Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| public static final [Api](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.html)\<[Api.ApiOptions.NoOptions](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.ApiOptions.NoOptions.html)\> | [API](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex#API)                     | Token to pass to [GoogleApiClient.Builder.addApi(Api)](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient.Builder.html#addApi(com.google.android.gms.common.api.Api<?%20extends%20com.google.android.gms.common.api.Api.ApiOptions.NotRequiredOptions>)) to enable the AppIndex features. |
| public static final [Api](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.html)\<[Api.ApiOptions.NoOptions](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.ApiOptions.NoOptions.html)\> | [APP_INDEX_API](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex#APP_INDEX_API) | *This field is deprecated. Use [API](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex#API) instead.*                                                                                                                                                                                       |
| public static final [AppIndexApi](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi)                                                                                                                                 | [AppIndexApi](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex#AppIndexApi)     | Methods for indexing actions that users are performing in your app to Google.                                                                                                                                                                                                                                                            |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Fields

#### public static final [Api](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.html)\<[Api.ApiOptions.NoOptions](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.ApiOptions.NoOptions.html)\>
**API**

Token to pass to [GoogleApiClient.Builder.addApi(Api)](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient.Builder.html#addApi(com.google.android.gms.common.api.Api<?%20extends%20com.google.android.gms.common.api.Api.ApiOptions.NotRequiredOptions>)) to enable the AppIndex features.  

#### public static final [Api](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.html)\<[Api.ApiOptions.NoOptions](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.ApiOptions.NoOptions.html)\>
**APP_INDEX_API**

**This field is deprecated.**   

Use [API](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex#API)
instead.  

#### public static final [AppIndexApi](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi)
**AppIndexApi**

Methods for indexing actions that users are performing in your app to Google. To use
this API, [API](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex#API)
must be enabled on your [GoogleApiClient](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient.html).