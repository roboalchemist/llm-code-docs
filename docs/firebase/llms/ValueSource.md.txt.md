# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ValueSource.md.txt

# ValueSource

public final enum **ValueSource** extends Enum\<E extends Enum\<E\>\>  
Indicates the source of a value.
"static" indicates the value was defined by a static constant.
"default" indicates the value was defined by default config.
"remote" indicates the value was defined by config produced by evaluating a template.

### Inherited Method Summary

From class java.lang.Enum

|---|---|
| final Object | clone() |
| final int | compareTo(E arg0) |
| int | compareTo(Object arg0) |
| final boolean | equals(Object arg0) |
| final void | finalize() |
| final Class\<E\> | getDeclaringClass() |
| final int | hashCode() |
| final String | name() |
| final int | ordinal() |
| String | toString() |
| static \<T extends Enum\<T\>\> T | valueOf(Class\<T\> arg0, String arg1) |

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

From interface java.lang.Comparable

|---|---|
| abstract int | compareTo(T arg0) |

## Enum Values

#### public static final ValueSource
**DEFAULT**

<br />

#### public static final ValueSource
**REMOTE**

<br />

#### public static final ValueSource
**STATIC**

<br />