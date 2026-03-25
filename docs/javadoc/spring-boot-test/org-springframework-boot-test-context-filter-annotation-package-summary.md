# Package org.springframework.boot.test.context.filter.annotation

---

@NullMarked
package org.springframework.boot.test.context.filter.annotation

Test annotations support for
`TypeExcludeFilter`.

- 

Class
Description
AnnotationCustomizableTypeExcludeFilter

Abstract base class for a `TypeExcludeFilter` that can be customized using an
annotation.

AnnotationCustomizableTypeExcludeFilter.FilterType
 
StandardAnnotationCustomizableTypeExcludeFilter<A extends Annotation>

`AnnotationCustomizableTypeExcludeFilter` that can be used to any test annotation
that uses the standard `includeFilters`, `excludeFilters` and
`useDefaultFilters` attributes.

TypeExcludeFilters

Annotation that can be on tests to define a set of `TypeExcludeFilter` classes
that should be registered with the `ApplicationContext`.