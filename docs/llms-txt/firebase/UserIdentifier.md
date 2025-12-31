# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier.md.txt

# UserIdentifier

public abstract class **UserIdentifier** extends Object  

|---|---|---|
| Known Direct Subclasses [EmailIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/EmailIdentifier), [PhoneIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/PhoneIdentifier), [ProviderIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderIdentifier), [UidIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UidIdentifier) |-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------| | [EmailIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/EmailIdentifier)       | Used for looking up an account by email.        | | [PhoneIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/PhoneIdentifier)       | Used for looking up an account by phone number. | | [ProviderIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderIdentifier) | Used for looking up an account by provider.     | | [UidIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UidIdentifier)           | Used for looking up an account by uid.          | |||

Identifies a user to be looked up.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------|
|   | [UserIdentifier](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier#UserIdentifier())() |

### Public Method Summary

|-----------------|----------------------------------------------------------------------------------------------------------------------------------|
| abstract String | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserIdentifier#toString())() |

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

## Public Constructors

#### public
**UserIdentifier**
()

<br />

## Public Methods

#### public abstract String
**toString**
()

<br />