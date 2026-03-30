# Record Class LocalTestWebServer.BaseUriDetails

java.lang.Object
java.lang.Record
org.springframework.boot.test.http.server.LocalTestWebServer.BaseUriDetails

Record Components:
`port` - the port of the running server
`path` - the path to use

Enclosing class:
`LocalTestWebServer`

---

public static record LocalTestWebServer.BaseUriDetails(int port, String path)
extends Record
Details of the base URI to the local test web server.

Since:
4.0.0

- 

## Constructor Summary

Constructors

Constructor
Description
`BaseUriDetails(int port,
 String path)`

Creates an instance of a `BaseUriDetails` record class.

- 

## Method Summary

Modifier and Type
Method
Description
`final boolean`
`equals(Object o)`

Indicates whether some other object is "equal to" this one.

`final int`
`hashCode()`

Returns a hash code value for this object.

`String`
`path()`

Returns the value of the `path` record component.

`int`
`port()`

Returns the value of the `port` record component.

`final String`
`toString()`

Returns a string representation of this record class.

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### BaseUriDetails

public BaseUriDetails(int port,
 String path)
Creates an instance of a `BaseUriDetails` record class.

Parameters:
`port` - the value for the `port` record component
`path` - the value for the `path` record component

- 

## Method Details

  - 

### toString

public final String toString()
Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.

Specified by:
`toString` in class `Record`
Returns:
a string representation of this object

  - 

### hashCode

public final int hashCode()
Returns a hash code value for this object. The value is derived from the hash code of each of the record components.

Specified by:
`hashCode` in class `Record`
Returns:
a hash code value for this object

  - 

### equals

public final boolean equals(Object o)
Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. Reference components are compared with `Objects::equals(Object,Object)`; primitive components are compared with the `compare` method from their corresponding wrapper classes.

Specified by:
`equals` in class `Record`
Parameters:
`o` - the object with which to compare
Returns:
`true` if this object is the same as the `o` argument; `false` otherwise.

  - 

### port

public int port()
Returns the value of the `port` record component.

Returns:
the value of the `port` record component

  - 

### path

public String path()
Returns the value of the `path` record component.

Returns:
the value of the `path` record component