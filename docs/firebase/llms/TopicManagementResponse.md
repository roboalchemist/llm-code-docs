# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.md.txt

# TopicManagementResponse

public class **TopicManagementResponse** extends Object  
The response produced by FCM topic management operations.  

### Nested Class Summary

|-------|---|---|---------------------------|
| class | [TopicManagementResponse.Error](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error) || A topic management error. |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| List\<[TopicManagementResponse.Error](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error)\> | [getErrors](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse#getErrors())() Gets a list of errors encountered while executing the topic management operation.                                          |
| int                                                                                                                                                                  | [getFailureCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse#getFailureCount())() Gets the number of registration tokens that could not be subscribed or unsubscribed, and resulted in an error. |
| int                                                                                                                                                                  | [getSuccessCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse#getSuccessCount())() Gets the number of registration tokens that were successfully subscribed or unsubscribed.                      |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public List\<[TopicManagementResponse.Error](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error)\>
**getErrors**
()

Gets a list of errors encountered while executing the topic management operation.  

##### Returns

- A non-null list.  

#### public int
**getFailureCount**
()

Gets the number of registration tokens that could not be subscribed or unsubscribed, and
resulted in an error.  

##### Returns

- The number of failures.  

#### public int
**getSuccessCount**
()

Gets the number of registration tokens that were successfully subscribed or unsubscribed.  

##### Returns

- The number of successes.