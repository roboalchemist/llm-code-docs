Package org.jbake.app.configuration

# Class Property

java.lang.Object
org.jbake.app.configuration.Property

All Implemented Interfaces:
`Comparable<Property>`

---

public class Property
extends Object
implements Comparable<Property>

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`Property.Group`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`Property(String key,
 String description)`
 
`Property(String key,
 String description,
 Property.Group group)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`compareTo(Property other)`
 
`boolean`
`equals(Object o)`
 
`String`
`getDescription()`
 
`Property.Group`
`getGroup()`
 
`String`
`getKey()`
 
`int`
`hashCode()`
 
`String`
`toString()`
 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Property

public Property(String key,
 String description)

  - 

### Property

public Property(String key,
 String description,
 Property.Group group)

- 

## Method Details

  - 

### getKey

public String getKey()

  - 

### getDescription

public String getDescription()

  - 

### getGroup

public Property.Group getGroup()

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`

  - 

### equals

public boolean equals(Object o)

Overrides:
`equals` in class `Object`

  - 

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`

  - 

### compareTo

public int compareTo(Property other)

Specified by:
`compareTo` in interface `Comparable<Property>`