JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

javax.mail

## Class Flags

- java.lang.Object

- 

  - javax.mail.Flags

- 

All Implemented Interfaces:
Serializable, Cloneable

Direct Known Subclasses:
FLAGS

---

```
public class Flags
extends Object
implements Cloneable, Serializable
```

The Flags class represents the set of flags on a Message.  Flags
 are composed of predefined system flags, and user defined flags. 

 A System flag is represented by the `Flags.Flag` 
 inner class. A User defined flag is represented as a String.
 User flags are case-independent. 

 A set of standard system flags are predefined.  Most folder
 implementations are expected to support these flags.  Some
 implementations may also support arbitrary user-defined flags.  The
 `getPermanentFlags` method on a Folder returns a Flags
 object that holds all the flags that are supported by that folder
 implementation. 

 A Flags object is serializable so that (for example) the
 use of Flags objects in search terms can be serialized
 along with the search terms. 

 **Warning:**
 Serialized objects of this class may not be compatible with future
 JavaMail API releases.  The current serialization support is
 appropriate for short term storage. 

 The below code sample illustrates how to set, examine, and get the 
 flags for a message.
 

```

 Message m = folder.getMessage(1);
 m.setFlag(Flags.Flag.DELETED, true); // set the DELETED flag

 // Check if DELETED flag is set on this message
 if (m.isSet(Flags.Flag.DELETED))
        System.out.println("DELETED message");

 // Examine ALL system flags for this message
 Flags flags = m.getFlags();
 Flags.Flag[] sf = flags.getSystemFlags();
 for (int i = 0; i < sf.length; i++) {
        if (sf[i] == Flags.Flag.DELETED)
            System.out.println("DELETED message");
        else if (sf[i] == Flags.Flag.SEEN)
            System.out.println("SEEN message");
      ......
      ......
 }
 
```

 

Author:
John Mani, Bill Shannon
See Also:
`Folder.getPermanentFlags()`, 
Serialized Form

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`Flags.Flag`
This inner class represents an individual system flag.

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Flags()`
Construct an empty Flags object.

`Flags(Flags.Flag flag)`
Construct a Flags object initialized with the given system flag.

`Flags(Flags flags)`
Construct a Flags object initialized with the given flags.

`Flags(String flag)`
Construct a Flags object initialized with the given user flag.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`add(Flags.Flag flag)`
Add the specified system flag to this Flags object.

`void`
`add(Flags f)`
Add all the flags in the given Flags object to this
 Flags object.

`void`
`add(String flag)`
Add the specified user flag to this Flags object.

`void`
`clearSystemFlags()`
Clear all of the system flags.

`void`
`clearUserFlags()`
Clear all of the user flags.

`Object`
`clone()`
Returns a clone of this Flags object.

`boolean`
`contains(Flags.Flag flag)`
Check whether the specified system flag is present in this Flags object.

`boolean`
`contains(Flags f)`
Check whether all the flags in the specified Flags object are
 present in this Flags object.

`boolean`
`contains(String flag)`
Check whether the specified user flag is present in this Flags object.

`boolean`
`equals(Object obj)`
Check whether the two Flags objects are equal.

`Flags.Flag[]`
`getSystemFlags()`
Return all the system flags in this Flags object.

`String[]`
`getUserFlags()`
Return all the user flags in this Flags object.

`int`
`hashCode()`
Compute a hash code for this Flags object.

`void`
`remove(Flags.Flag flag)`
Remove the specified system flag from this Flags object.

`void`
`remove(Flags f)`
Remove all flags in the given Flags object from this 
 Flags object.

`void`
`remove(String flag)`
Remove the specified user flag from this Flags object.

`boolean`
`retainAll(Flags f)`
Remove any flags **not** in the given Flags object.

`String`
`toString()`
Return a string representation of this Flags object.

    - 

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Flags

```
public Flags()
```

Construct an empty Flags object.

    - 

#### Flags

```
public Flags(Flags flags)
```

Construct a Flags object initialized with the given flags.

Parameters:
`flags` - the flags for initialization

    - 

#### Flags

```
public Flags(Flags.Flag flag)
```

Construct a Flags object initialized with the given system flag.

Parameters:
`flag` - the flag for initialization

    - 

#### Flags

```
public Flags(String flag)
```

Construct a Flags object initialized with the given user flag.

Parameters:
`flag` - the flag for initialization

  - 

### Method Detail

    - 

#### add

```
public void add(Flags.Flag flag)
```

Add the specified system flag to this Flags object.

Parameters:
`flag` - the flag to add

    - 

#### add

```
public void add(String flag)
```

Add the specified user flag to this Flags object.

Parameters:
`flag` - the flag to add

    - 

#### add

```
public void add(Flags f)
```

Add all the flags in the given Flags object to this
 Flags object.

Parameters:
`f` - Flags object

    - 

#### remove

```
public void remove(Flags.Flag flag)
```

Remove the specified system flag from this Flags object.

Parameters:
`flag` - the flag to be removed

    - 

#### remove

```
public void remove(String flag)
```

Remove the specified user flag from this Flags object.

Parameters:
`flag` - the flag to be removed

    - 

#### remove

```
public void remove(Flags f)
```

Remove all flags in the given Flags object from this 
 Flags object.

Parameters:
`f` - the flag to be removed

    - 

#### retainAll

```
public boolean retainAll(Flags f)
```

Remove any flags **not** in the given Flags object.
 Useful for clearing flags not supported by a server.  If the
 given Flags object includes the Flags.Flag.USER flag, all user
 flags in this Flags object are retained.

Parameters:
`f` - the flags to keep
Returns:
true if this Flags object changed
Since:
JavaMail 1.6

    - 

#### contains

```
public boolean contains(Flags.Flag flag)
```

Check whether the specified system flag is present in this Flags object.

Parameters:
`flag` - the flag to test
Returns:
true of the given flag is present, otherwise false.

    - 

#### contains

```
public boolean contains(String flag)
```

Check whether the specified user flag is present in this Flags object.

Parameters:
`flag` - the flag to test
Returns:
true of the given flag is present, otherwise false.

    - 

#### contains

```
public boolean contains(Flags f)
```

Check whether all the flags in the specified Flags object are
 present in this Flags object.

Parameters:
`f` - the flags to test
Returns:
true if all flags in the given Flags object are present, 
                otherwise false.

    - 

#### equals

```
public boolean equals(Object obj)
```

Check whether the two Flags objects are equal.

Overrides:
`equals` in class `Object`
Returns:
true if they're equal

    - 

#### hashCode

```
public int hashCode()
```

Compute a hash code for this Flags object.

Overrides:
`hashCode` in class `Object`
Returns:
the hash code

    - 

#### getSystemFlags

```
public Flags.Flag[] getSystemFlags()
```

Return all the system flags in this Flags object.  Returns
 an array of size zero if no flags are set.

Returns:
array of Flags.Flag objects representing system flags

    - 

#### getUserFlags

```
public String[] getUserFlags()
```

Return all the user flags in this Flags object.  Returns
 an array of size zero if no flags are set.

Returns:
array of Strings, each String represents a flag.

    - 

#### clearSystemFlags

```
public void clearSystemFlags()
```

Clear all of the system flags.

Since:
JavaMail 1.6

    - 

#### clearUserFlags

```
public void clearUserFlags()
```

Clear all of the user flags.

Since:
JavaMail 1.6

    - 

#### clone

```
public Object clone()
```

Returns a clone of this Flags object.

Overrides:
`clone` in class `Object`

    - 

#### toString

```
public String toString()
```

Return a string representation of this Flags object.
 Note that the exact format of the string is subject to change.

Overrides:
`toString` in class `Object`

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

Copyright © 2018 Oracle. All rights reserved.