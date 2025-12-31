# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/server-value.md.txt

# Firebase.Database.ServerValue Class Reference

# Firebase.Database.ServerValue

Contains placeholder values to use when writing data to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database).

## Summary

|                                                                                                                                                                                                                                                                                       ### Public static attributes                                                                                                                                                                                                                                                                                        ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Timestamp](https://firebase.google.com/docs/reference/unity/class/firebase/database/server-value#class_firebase_1_1_database_1_1_server_value_1aaa7e7cd15f6a7f958d645cf26645df2b)` = CreateServerValuePlaceholder("timestamp")` | `readonly object` A placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) by the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) servers. |

## Public static attributes

### Timestamp

```c#
readonly object Timestamp =
      CreateServerValuePlaceholder("timestamp")
```  
A placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) by the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) servers.