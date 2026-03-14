Package org.apache.commons.validator

# Class FormSetFactory

java.lang.Object
org.apache.commons.digester.AbstractObjectCreationFactory
org.apache.commons.validator.FormSetFactory

All Implemented Interfaces:
`org.apache.commons.digester.ObjectCreationFactory`

---

public class FormSetFactory
extends org.apache.commons.digester.AbstractObjectCreationFactory
Factory class used by Digester to create FormSet's.

Since:
1.2

- 

## Field Summary

### Fields inherited from class org.apache.commons.digester.AbstractObjectCreationFactory

`digester`

- 

## Constructor Summary

Constructors

Constructor
Description
`FormSetFactory()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`Object`
`createObject(Attributes attributes)`

Create or retrieve a `FormSet` for the specified
    attributes.

### Methods inherited from class org.apache.commons.digester.AbstractObjectCreationFactory

`getDigester, setDigester`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### FormSetFactory

public FormSetFactory()
Constructs a new instance.

- 

## Method Details

  - 

### createObject

public Object createObject(Attributes attributes)
                    throws Exception

Create or retrieve a `FormSet` for the specified
    attributes.

Specified by:
`createObject` in interface `org.apache.commons.digester.ObjectCreationFactory`
Specified by:
`createObject` in class `org.apache.commons.digester.AbstractObjectCreationFactory`
Parameters:
`attributes` - The sax attributes for the formset element.
Returns:
The FormSet for a locale.
Throws:
`Exception` - If an error occurs creating the FormSet.