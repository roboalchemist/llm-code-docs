# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.md.txt

# ListVersionsOptions

public final class **ListVersionsOptions** extends Object  
A class representing options for Remote Config list versions operation.  

### Nested Class Summary

|-------|---|---|---|
| class | [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) ||   |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions#builder())() Creates a new [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder). |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)        | [toBuilder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions#toBuilder())() Creates a new `Builder` from the options object.                                                                                                                       |

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

#### public static [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**builder**
()

Creates a new [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder).  

##### Returns

- A [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) instance.  

#### public [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**toBuilder**
()

Creates a new `Builder` from the options object.

The new builder is not backed by this object's values; that is, changes made to the new
builder don't change the values of the origin object.