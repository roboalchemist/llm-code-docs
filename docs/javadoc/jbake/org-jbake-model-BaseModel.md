Package org.jbake.model

# Class BaseModel

java.lang.Object
java.util.AbstractMap<K,V>
java.util.HashMap<String,Object>
org.jbake.model.BaseModel

All Implemented Interfaces:
`Serializable`, `Cloneable`, `Map<String,Object>`

Direct Known Subclasses:
`DocumentModel`, `TemplateModel`

---

public abstract class BaseModel
extends HashMap<String,Object>

See Also:

- Serialized Form

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.util.AbstractMap

`AbstractMap.SimpleEntry<K extends Object,V extends Object>, AbstractMap.SimpleImmutableEntry<K extends Object,V extends Object>`

## Nested classes/interfaces inherited from interface java.util.Map

`Map.Entry<K extends Object,V extends Object>`

- 

## Constructor Summary

Constructors

Constructor
Description
`BaseModel()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`getUri()`
 
`void`
`setName(String name)`
 
`void`
`setUri(String uri)`
 

### Methods inherited from class java.util.HashMap

`clear, clone, compute, computeIfAbsent, computeIfPresent, containsKey, containsValue, entrySet, forEach, get, getOrDefault, isEmpty, keySet, merge, put, putAll, putIfAbsent, remove, remove, replace, replace, replaceAll, size, values`

### Methods inherited from class java.util.AbstractMap

`equals, hashCode, toString`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.util.Map

`equals, hashCode`

- 

## Constructor Details

  - 

### BaseModel

public BaseModel()

- 

## Method Details

  - 

### getUri

public String getUri()

  - 

### setUri

public void setUri(String uri)

  - 

### setName

public void setName(String name)