# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.ActionResult.md.txt

# AppIndexApi.ActionResult

public static interface **AppIndexApi.ActionResult**  
**This interface is deprecated.**   

Use [AppIndexApi.start(GoogleApiClient, Action)](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi#start(com.google.android.gms.common.api.GoogleApiClient,%20com.google.android.gms.appindexing.Action)) and [AppIndexApi.end(GoogleApiClient, Action)](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi#end(com.google.android.gms.common.api.GoogleApiClient,%20com.google.android.gms.appindexing.Action)).  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract [PendingResult](https://developers.google.com/android/reference/com/google/android/gms/common/api/PendingResult.html)\<[Status](https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html)\> | [end](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.ActionResult#end(com.google.android.gms.common.api.GoogleApiClient))([GoogleApiClient](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient.html) apiClient) Indicates that a user completed an action.                                                                                                |
| abstract [PendingResult](https://developers.google.com/android/reference/com/google/android/gms/common/api/PendingResult.html)\<[Status](https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html)\> | [getPendingResult](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.ActionResult#getPendingResult())() Represents the result of a call to the [AppIndexApi.action(GoogleApiClient, Action)](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi#action(com.google.android.gms.common.api.GoogleApiClient,%20com.google.android.gms.appindexing.Action)) API. |

## Public Methods

#### public abstract [PendingResult](https://developers.google.com/android/reference/com/google/android/gms/common/api/PendingResult.html)\<[Status](https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html)\>
**end** ([GoogleApiClient](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient.html) apiClient)

Indicates that a user completed an action.  

##### Parameters

| apiClient | The [GoogleApiClient](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient.html) configured to use the [AppIndex.API](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndex#API). The client should be connecting or connected. |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- The [PendingResult](https://developers.google.com/android/reference/com/google/android/gms/common/api/PendingResult.html) which can optionally be used to determine if the call succeeded.  

#### public abstract [PendingResult](https://developers.google.com/android/reference/com/google/android/gms/common/api/PendingResult.html)\<[Status](https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html)\>
**getPendingResult** ()

Represents the result of a call to the [AppIndexApi.action(GoogleApiClient, Action)](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi#action(com.google.android.gms.common.api.GoogleApiClient,%20com.google.android.gms.appindexing.Action)) API.  

##### Returns

- The [PendingResult](https://developers.google.com/android/reference/com/google/android/gms/common/api/PendingResult.html) which can optionally be used to determine if the [AppIndexApi.action(GoogleApiClient, Action)](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi#action(com.google.android.gms.common.api.GoogleApiClient,%20com.google.android.gms.appindexing.Action)) method succeeded.