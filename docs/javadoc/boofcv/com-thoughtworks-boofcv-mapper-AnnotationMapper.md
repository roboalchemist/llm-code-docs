JavaScript is disabled on your browser.

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

com.thoughtworks.boofcv.mapper

## Class AnnotationMapper

- java.lang.Object

- 

  - MapperWrapper

  - 

    - com.thoughtworks.boofcv.mapper.AnnotationMapper

- 

---

```
public class AnnotationMapper
extends MapperWrapper
```

A mapper that uses annotations to prepare the remaining mappers in the chain.
Since:
  1.3
Author:
  Jörg Schaible

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AnnotationMapper**(Mapper wrapped,
                ConverterRegistry converterRegistry,
                ConverterLookup converterLookup,
                XStreamClassLoader classLoader,
                ReflectionProvider reflectionProvider,
                JVM jvm)`
Construct an AnnotationMapper.

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**autodetectAnnotations**(boolean mode)` 

`java.lang.Class`
`**defaultImplementationOf**(java.lang.Class type)` 

`Converter`
`**getLocalConverter**(java.lang.Class definedIn,
                 java.lang.String fieldName)` 

`void`
`**processAnnotations**(java.lang.Class[] initialTypes)` 

`java.lang.String`
`**realMember**(java.lang.Class type,
          java.lang.String serialized)` 

`java.lang.String`
`**serializedClass**(java.lang.Class type)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AnnotationMapper

```
public AnnotationMapper(Mapper wrapped,
                ConverterRegistry converterRegistry,
                ConverterLookup converterLookup,
                XStreamClassLoader classLoader,
                ReflectionProvider reflectionProvider,
                JVM jvm)
```

Construct an AnnotationMapper.
Parameters:`wrapped` - the next `com.thoughtworks.xstream.mapper.Mapper` in the chainSince:
  1.3

  - 

### Method Detail

    - 

#### realMember

```
public java.lang.String realMember(java.lang.Class type,
                          java.lang.String serialized)
```

    - 

#### serializedClass

```
public java.lang.String serializedClass(java.lang.Class type)
```

    - 

#### defaultImplementationOf

```
public java.lang.Class defaultImplementationOf(java.lang.Class type)
```

    - 

#### getLocalConverter

```
public Converter getLocalConverter(java.lang.Class definedIn,
                          java.lang.String fieldName)
```

    - 

#### autodetectAnnotations

```
public void autodetectAnnotations(boolean mode)
```

    - 

#### processAnnotations

```
public void processAnnotations(java.lang.Class[] initialTypes)
```

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

**Copyright © 2011-2012 Peter Abeles**