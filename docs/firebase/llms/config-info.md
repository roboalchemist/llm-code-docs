# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info.md.txt

# Firebase.RemoteConfig.ConfigInfo Class Reference

# Firebase.RemoteConfig.ConfigInfo

Describes the state of the most recent Fetch() call.

## Summary

Normally returned as a result of the GetInfo() function.

|                                                                                                                                                                                                          ### Properties                                                                                                                                                                                                           ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FetchTime](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info_1ada9a3e4e6e09dabe133c5e547a2944e1)              | `System.DateTime` The time when the last fetch operation completed.                                                                                                                                                      |
| [LastFetchFailureReason](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info_1a6459600cd270802d927169878bf8dd11) | [FetchFailureReason](https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a41e00bf8ed5b155fb433f5173212787b) The reason the most recent fetch failed. |
| [LastFetchStatus](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info_1a0f2b23084b56f7f0062dbdc48f7aebcd)        | [LastFetchStatus](https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a36d228a1957619a925e1f9f5363e316e) The status of the last fetch request.       |
| [ThrottledEndTime](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info_1a84977f51562d9be4b5551eb9f814a4c1)       | `System.DateTime` The time when Remote Config data refreshes will no longer be throttled.                                                                                                                                |

## Properties

### FetchTime

```c#
System.DateTime FetchTime
```  
The time when the last fetch operation completed.  

### LastFetchFailureReason

```c#
FetchFailureReason LastFetchFailureReason
```  
The reason the most recent fetch failed.  

### LastFetchStatus

```c#
LastFetchStatus LastFetchStatus
```  
The status of the last fetch request.  

### ThrottledEndTime

```c#
System.DateTime ThrottledEndTime
```  
The time when Remote Config data refreshes will no longer be throttled.