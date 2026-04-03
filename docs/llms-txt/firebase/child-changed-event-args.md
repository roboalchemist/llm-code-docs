# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args.md.txt

# Firebase.Database.ChildChangedEventArgs Class Reference

# Firebase.Database.ChildChangedEventArgs

Child changed event arguments.

## Summary

This data is sent when any of the following events are raised. [Query.ChildAdded](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a6c892241cfe3d3cfa77540d6341a0016) , [Query.ChildChanged](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a71e2af7868312246b5da3024bb13204c) , [Query.ChildRemoved](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1af4ef267bfef07b1969bd1394eb45c428) , or [Query.ChildMoved](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1ade5832ad58d0b31fd5a649019bb8f2c9)

### Inheritance

Inherits from: EventArgs

|                                                                                                                                                                                                                                                                                                                                                                                              ### Properties                                                                                                                                                                                                                                                                                                                                                                                              ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args#class_firebase_1_1_database_1_1_child_changed_event_args_1a7d83985f5b3f11b26bc3d27e61f544a0)     | [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error) The presence of a [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error) indicates that there was an issue subscribing the event to the given [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) location. |
| [PreviousChildName](https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args#class_firebase_1_1_database_1_1_child_changed_event_args_1af625f907b296fdbeeecc85068337540b) | `string` The key name of sibling location ordered before the new child.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Snapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/child-changed-event-args#class_firebase_1_1_database_1_1_child_changed_event_args_1ad9f6609681e00bc3e28b30e4e799e35d)          | [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) Gets the data snapshot for this update if it exists.                                                                                                                                                                                                                                                                                                                                                                            |

## Properties

### DatabaseError

```c#
DatabaseError DatabaseError
```  
The presence of a [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error) indicates that there was an issue subscribing the event to the given [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) location.

The database error.  

### PreviousChildName

```c#
string PreviousChildName
```  
The key name of sibling location ordered before the new child.

This will be null for the first child node of a location.

The name of the previous child.  

### Snapshot

```c#
DataSnapshot Snapshot
```  
Gets the data snapshot for this update if it exists.

The snapshot.