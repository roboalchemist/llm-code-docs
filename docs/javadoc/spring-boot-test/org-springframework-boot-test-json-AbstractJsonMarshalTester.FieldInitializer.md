# Class AbstractJsonMarshalTester.FieldInitializer<M>

java.lang.Object
org.springframework.boot.test.json.AbstractJsonMarshalTester.FieldInitializer<M>

Type Parameters:
`M` - the marshaller type

Enclosing class:
`AbstractJsonMarshalTester<T>`

---

protected abstract static class AbstractJsonMarshalTester.FieldInitializer<M>
extends Object
Utility class used to support field initialization. Used by subclasses to support
`initFields`.

Since:
1.4.0

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`FieldInitializer(Class<? extends AbstractJsonMarshalTester> testerClass)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected abstract AbstractJsonMarshalTester<Object>`
`createTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 M marshaller)`
 
`protected void`
`doWithField(Field field,
 Object test,
 org.springframework.beans.factory.ObjectFactory<M> marshaller)`
 
`void`
`initFields(Object testInstance,
 M marshaller)`
 
`void`
`initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<M> marshaller)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### FieldInitializer

protected FieldInitializer(Class<? extends AbstractJsonMarshalTester> testerClass)

- 

## Method Details

  - 

### initFields

public void initFields(Object testInstance,
 M marshaller)

  - 

### initFields

public void initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<M> marshaller)

  - 

### doWithField

protected void doWithField(Field field,
 Object test,
 org.springframework.beans.factory.ObjectFactory<M> marshaller)

  - 

### createTester

protected abstract AbstractJsonMarshalTester<Object> createTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 M marshaller)