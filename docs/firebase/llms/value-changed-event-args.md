# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/value-changed-event-args.md.txt

# Firebase.Database.ValueChangedEventArgs Class Reference

# Firebase.Database.ValueChangedEventArgs

Event arguments passed with the [Query.ValueChanged](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#class_firebase_1_1_database_1_1_query_1a80a78f3505955b9ed2583dc2f14cf739) Event.

## Summary

### Inheritance

Inherits from: EventArgs

|                                                                                                                                                                                                          ### Properties                                                                                                                                                                                                          ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/value-changed-event-args#class_firebase_1_1_database_1_1_value_changed_event_args_1ab9520db2942feab628f8aabff2559750) | [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error) Gets the database error if one exists.                   |
| [Snapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/value-changed-event-args#class_firebase_1_1_database_1_1_value_changed_event_args_1abcf8e1e5d371d9fcca33e068e7f9f284)      | [DataSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot#class_firebase_1_1_database_1_1_data_snapshot) Gets the snapshot for this value update event if it exists. |

## Properties

### DatabaseError

```c#
DatabaseError DatabaseError
```  
Gets the database error if one exists.

The database error.  

### Snapshot

```c#
DataSnapshot Snapshot
```  
Gets the snapshot for this value update event if it exists.

The snapshot.