# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.md.txt

# AndroidNotification

public class **AndroidNotification** extends Object  
Represents the Android-specific notification options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message).
Instances of this class are thread-safe and immutable.  

### Nested Class Summary

|-------|---|---|---|
| class | [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) ||   |
| enum  | [AndroidNotification.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Priority) ||   |
| enum  | [AndroidNotification.Proxy](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Proxy) ||   |
| enum  | [AndroidNotification.Visibility](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Visibility) ||   |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification#builder())() Creates a new [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder). |

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

#### public static [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder)
**builder**
()

Creates a new [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder).  

##### Returns

- A [AndroidNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification.Builder) instance.