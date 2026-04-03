# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error.md.txt

# TopicManagementResponse.Error

public static class **TopicManagementResponse.Error** extends Object  
A topic management error.  

### Public Method Summary

|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int    | [getIndex](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error#getIndex())() Index of the registration token to which this error is related to. |
| String | [getReason](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error#getReason())() String describing the nature of the error.                       |
| String | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse.Error#toString())()                                                                    |

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

#### public int
**getIndex**
()

Index of the registration token to which this error is related to.  

##### Returns

- An index into the original registration token list.  

#### public String
**getReason**
()

String describing the nature of the error.  

##### Returns

- A non-null, non-empty error message.  

#### public String
**toString**
()

<br />