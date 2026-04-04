# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.remoteconfiguser.md.txt

# remoteConfig.RemoteConfigUser interface

An interface representing metadata for a Remote Config account that performed the update. Contains the same fields as \[`RemoteConfigUser`\](/docs/reference/remote-config/rest/v1/Version#remoteconfiguser).

**Signature:**  

    export interface RemoteConfigUser 

## Properties

|                                                                         Property                                                                          |  Type  |                              Description                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------|
| [email](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.remoteconfiguser.md#remoteconfigremoteconfiguseremail)       | string | Email address of the Remote Config account that performed the update. |
| [imageUrl](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.remoteconfiguser.md#remoteconfigremoteconfiguserimageurl) | string | Image URL of the Remote Config account that performed the update.     |
| [name](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.remoteconfiguser.md#remoteconfigremoteconfigusername)         | string | Name of the Remote Config account that performed the update.          |

## remoteConfig.RemoteConfigUser.email

Email address of the Remote Config account that performed the update.

**Signature:**  

    email: string;

## remoteConfig.RemoteConfigUser.imageUrl

Image URL of the Remote Config account that performed the update.

**Signature:**  

    imageUrl?: string;

## remoteConfig.RemoteConfigUser.name

Name of the Remote Config account that performed the update.

**Signature:**  

    name?: string;