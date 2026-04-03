# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/critical-sound.md.txt

# FirebaseAdmin.Messaging.CriticalSound Class Reference

# FirebaseAdmin.Messaging.CriticalSound

The sound configuration for APNs critical alerts.

## Summary

|                                                                                                                                                    ### Properties                                                                                                                                                     ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [Critical](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/critical-sound#class_firebase_admin_1_1_messaging_1_1_critical_sound_1aaed5bccc335f4f892f6431751586156b) | `bool` Gets or sets a value indicating whether to set the critical alert flag on the sound configuration. |
| [Name](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/critical-sound#class_firebase_admin_1_1_messaging_1_1_critical_sound_1a97d671611857eefb47a2d03b876a8a3e)     | `string` Gets or sets the name of the sound to be played.                                                 |
| [Volume](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/critical-sound#class_firebase_admin_1_1_messaging_1_1_critical_sound_1afee82731e086ede1a7251370c63ebd9d)   | `double` Gets or sets the volume for the critical alert's sound.                                          |

## Properties

### Critical

```text
bool Critical
```  
Gets or sets a value indicating whether to set the critical alert flag on the sound configuration.  

### Name

```text
string Name
```  
Gets or sets the name of the sound to be played.

This should be a sound file in your app's main bundle or in the `Library/Sounds` folder of your app's container directory. Specify the string `default` to play the system sound.  

### Volume

```text
double Volume
```  
Gets or sets the volume for the critical alert's sound.

Must be a value between 0.0 (silent) and 1.0 (full volume).