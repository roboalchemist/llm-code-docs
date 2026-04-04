# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata.md.txt

# UserMetadata

public class **UserMetadata** extends Object  
Contains additional metadata associated with a user account.

### Public Constructor Summary

|---|---|
|   | [UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata#UserMetadata(long))(long creationTimestamp) |
|   | [UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata#UserMetadata(long, long, long))(long creationTimestamp, long lastSignInTimestamp, long lastRefreshTimestamp) |

### Public Method Summary

|---|---|
| long | [getCreationTimestamp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata#getCreationTimestamp())() Returns the time at which the account was created. |
| long | [getLastRefreshTimestamp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata#getLastRefreshTimestamp())() Returns the time at which the user was last active (ID token refreshed). |
| long | [getLastSignInTimestamp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata#getLastSignInTimestamp())() Returns the time at which the user last signed in. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Constructors

#### public
**UserMetadata**
(long creationTimestamp)

<br />

#### public
**UserMetadata**
(long creationTimestamp, long lastSignInTimestamp, long lastRefreshTimestamp)

<br />

## Public Methods

#### public long
**getCreationTimestamp**
()

Returns the time at which the account was created.

##### Returns

- Milliseconds since epoch timestamp.

#### public long
**getLastRefreshTimestamp**
()

Returns the time at which the user was last active (ID token refreshed).

##### Returns

- Milliseconds since epoch timestamp, or 0 if the user was never active.

#### public long
**getLastSignInTimestamp**
()

Returns the time at which the user last signed in.

##### Returns

- Milliseconds since epoch timestamp, or 0 if the user has never signed in.