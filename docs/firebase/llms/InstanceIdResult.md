# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/iid/InstanceIdResult.md.txt

# InstanceIdResult

public interface **InstanceIdResult**  
**This interface is deprecated.**   

Firebase Instance ID has been replaced with [FirebaseInstallations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations)
for app instance identifiers and `FirebaseMessaging.getToken()` for FCM
registration tokens.

Result object obtained from requests for an Instance ID and token.  

### Public Method Summary

|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract [String](https://developer.android.com/reference/java/lang/String.html) | [getId](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/InstanceIdResult#getId())() Returns the stable identifier that uniquely identifies this application instance.                  |
| abstract [String](https://developer.android.com/reference/java/lang/String.html) | [getToken](https://firebase.google.com/docs/reference/android/com/google/firebase/iid/InstanceIdResult#getToken())() Returns the token that authorizes performing actions on behalf of this application instance. |

## Public Methods

#### public abstract [String](https://developer.android.com/reference/java/lang/String.html) **getId** ()

Returns the stable identifier that uniquely identifies this application
instance.  

#### public abstract [String](https://developer.android.com/reference/java/lang/String.html) **getToken** ()

Returns the token that authorizes performing actions on behalf of this application
instance.

For example, this token authorizes sending messages via Firebase Cloud
Messaging.