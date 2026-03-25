# Class AnnotationCustomizableTypeExcludeFilter

java.lang.Object
org.springframework.boot.context.TypeExcludeFilter
org.springframework.boot.test.context.filter.annotation.AnnotationCustomizableTypeExcludeFilter

All Implemented Interfaces:
`org.springframework.beans.factory.Aware, org.springframework.beans.factory.BeanClassLoaderAware, org.springframework.beans.factory.BeanFactoryAware, org.springframework.core.type.filter.TypeFilter`

Direct Known Subclasses:
`StandardAnnotationCustomizableTypeExcludeFilter`

---

public abstract class AnnotationCustomizableTypeExcludeFilter
extends org.springframework.boot.context.TypeExcludeFilter
implements org.springframework.beans.factory.BeanClassLoaderAware
Abstract base class for a `TypeExcludeFilter` that can be customized using an
annotation.

Since:
4.0.0

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`protected static enum `
`AnnotationCustomizableTypeExcludeFilter.FilterType`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`AnnotationCustomizableTypeExcludeFilter()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected boolean`
`defaultInclude(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)`
 
`boolean`
`equals(@Nullable Object obj)`
 
`protected boolean`
`exclude(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)`
 
`protected abstract Set<Class<?>>`
`getComponentIncludes()`
 
`protected abstract Set<Class<?>>`
`getDefaultIncludes()`
 
`protected abstract org.springframework.context.annotation.ComponentScan.Filter[]`
`getFilters(AnnotationCustomizableTypeExcludeFilter.FilterType type)`
 
`protected abstract boolean`
`hasAnnotation()`
 
`int`
`hashCode()`
 
`protected boolean`
`include(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)`
 
`protected final boolean`
`isTypeOrAnnotated(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory,
 Class<?> type)`
 
`protected abstract boolean`
`isUseDefaultFilters()`
 
`boolean`
`match(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)`
 
`void`
`setBeanClassLoader(ClassLoader classLoader)`
 

### Methods inherited from class org.springframework.boot.context.TypeExcludeFilter

`setBeanFactory`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### AnnotationCustomizableTypeExcludeFilter

public AnnotationCustomizableTypeExcludeFilter()

- 

## Method Details

  - 

### setBeanClassLoader

public void setBeanClassLoader(ClassLoader classLoader)

Specified by:
`setBeanClassLoader` in interface `org.springframework.beans.factory.BeanClassLoaderAware`

  - 

### match

public boolean match(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)
              throws IOException

Specified by:
`match` in interface `org.springframework.core.type.filter.TypeFilter`
Overrides:
`match` in class `org.springframework.boot.context.TypeExcludeFilter`
Throws:
`IOException`

  - 

### include

protected boolean include(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)
                   throws IOException

Throws:
`IOException`

  - 

### defaultInclude

protected boolean defaultInclude(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)
                          throws IOException

Throws:
`IOException`

  - 

### exclude

protected boolean exclude(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory)
                   throws IOException

Throws:
`IOException`

  - 

### isTypeOrAnnotated

protected final boolean isTypeOrAnnotated(org.springframework.core.type.classreading.MetadataReader metadataReader,
 org.springframework.core.type.classreading.MetadataReaderFactory metadataReaderFactory,
 Class<?> type)
                                   throws IOException

Throws:
`IOException`

  - 

### hasAnnotation

protected abstract boolean hasAnnotation()

  - 

### getFilters

protected abstract org.springframework.context.annotation.ComponentScan.Filter[] getFilters(AnnotationCustomizableTypeExcludeFilter.FilterType type)

  - 

### isUseDefaultFilters

protected abstract boolean isUseDefaultFilters()

  - 

### getDefaultIncludes

protected abstract Set<Class<?>> getDefaultIncludes()

  - 

### getComponentIncludes

protected abstract Set<Class<?>> getComponentIncludes()

  - 

### equals

public boolean equals(@Nullable Object obj)

Overrides:
`equals` in class `org.springframework.boot.context.TypeExcludeFilter`

  - 

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `org.springframework.boot.context.TypeExcludeFilter`