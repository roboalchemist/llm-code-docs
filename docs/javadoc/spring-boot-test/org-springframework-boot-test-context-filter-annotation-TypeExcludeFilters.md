# Annotation Interface TypeExcludeFilters

---

@Target(TYPE)
@Retention(RUNTIME)
@Documented
@Inherited
public @interface TypeExcludeFilters
Annotation that can be on tests to define a set of `TypeExcludeFilter` classes
that should be registered with the `ApplicationContext`.

Since:
4.0.0
See Also:

- `TypeExcludeFilter`

- 

## Required Element Summary

Required Elements

Modifier and Type
Required Element
Description
`Class<? extends org.springframework.boot.context.TypeExcludeFilter>[]`
`value`

Specifies `TypeExcludeFilter` classes that should be registered.

- 

## Element Details

  - 

### value

Class<? extends org.springframework.boot.context.TypeExcludeFilter>[] value
Specifies `TypeExcludeFilter` classes that should be registered. Classes
specified here can either have a no-arg constructor or accept a single
`Class<?>` argument if they need access to the `testClass`.

Returns:
the type exclude filters to apply
See Also:

    - `TypeExcludeFilter`