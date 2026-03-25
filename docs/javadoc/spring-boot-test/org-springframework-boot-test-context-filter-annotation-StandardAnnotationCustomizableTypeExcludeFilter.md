# Class StandardAnnotationCustomizableTypeExcludeFilter<A extends Annotation>

java.lang.Object
org.springframework.boot.context.TypeExcludeFilter
org.springframework.boot.test.context.filter.annotation.AnnotationCustomizableTypeExcludeFilter
org.springframework.boot.test.context.filter.annotation.StandardAnnotationCustomizableTypeExcludeFilter<A>

Type Parameters:
`A` - the annotation type

All Implemented Interfaces:
`org.springframework.beans.factory.Aware, org.springframework.beans.factory.BeanClassLoaderAware, org.springframework.beans.factory.BeanFactoryAware, org.springframework.core.type.filter.TypeFilter`

---

public abstract class StandardAnnotationCustomizableTypeExcludeFilter<A extends Annotation>
extends AnnotationCustomizableTypeExcludeFilter
`AnnotationCustomizableTypeExcludeFilter` that can be used to any test annotation
that uses the standard `includeFilters`, `excludeFilters` and
`useDefaultFilters` attributes.

Since:
4.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class AnnotationCustomizableTypeExcludeFilter

`AnnotationCustomizableTypeExcludeFilter.FilterType`

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`StandardAnnotationCustomizableTypeExcludeFilter(Class<?> testClass)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected final org.springframework.core.annotation.MergedAnnotation<A>`
`getAnnotation()`
 
`protected Class<A>`
`getAnnotationType()`
 
`protected Set<Class<?>>`
`getComponentIncludes()`
 
`protected final Set<Class<?>>`
`getDefaultIncludes()`
 
`protected org.springframework.context.annotation.ComponentScan.Filter[]`
`getFilters(AnnotationCustomizableTypeExcludeFilter.FilterType type)`
 
`protected Set<Class<?>>`
`getKnownIncludes()`
 
`protected boolean`
`hasAnnotation()`
 
`protected boolean`
`isUseDefaultFilters()`
 

### Methods inherited from class AnnotationCustomizableTypeExcludeFilter

`defaultInclude, equals, exclude, hashCode, include, isTypeOrAnnotated, match, setBeanClassLoader`

### Methods inherited from class org.springframework.boot.context.TypeExcludeFilter

`setBeanFactory`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### StandardAnnotationCustomizableTypeExcludeFilter

protected StandardAnnotationCustomizableTypeExcludeFilter(Class<?> testClass)

- 

## Method Details

  - 

### getAnnotation

protected final org.springframework.core.annotation.MergedAnnotation<A> getAnnotation()

  - 

### hasAnnotation

protected boolean hasAnnotation()

Specified by:
`hasAnnotation` in class `AnnotationCustomizableTypeExcludeFilter`

  - 

### getFilters

protected org.springframework.context.annotation.ComponentScan.Filter[] getFilters(AnnotationCustomizableTypeExcludeFilter.FilterType type)

Specified by:
`getFilters` in class `AnnotationCustomizableTypeExcludeFilter`

  - 

### isUseDefaultFilters

protected boolean isUseDefaultFilters()

Specified by:
`isUseDefaultFilters` in class `AnnotationCustomizableTypeExcludeFilter`

  - 

### getDefaultIncludes

protected final Set<Class<?>> getDefaultIncludes()

Specified by:
`getDefaultIncludes` in class `AnnotationCustomizableTypeExcludeFilter`

  - 

### getKnownIncludes

protected Set<Class<?>> getKnownIncludes()

  - 

### getComponentIncludes

protected Set<Class<?>> getComponentIncludes()

Specified by:
`getComponentIncludes` in class `AnnotationCustomizableTypeExcludeFilter`

  - 

### getAnnotationType

protected Class<A> getAnnotationType()