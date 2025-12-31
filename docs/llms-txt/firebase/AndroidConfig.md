# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.md.txt

# AndroidConfig

public class **AndroidConfig** extends Object  
Represents the Android-specific options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message).
Instances of this class are thread-safe and immutable.  

### Nested Class Summary

|-------|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| class | [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) ||                                                                                                                                                                     |
| enum  | [AndroidConfig.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Priority) || Priority levels that can be set on an [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig). |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig#builder())() Creates a new [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder). |

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

#### public static [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**builder**
()

Creates a new [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder).  

##### Returns

- A [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) instance.