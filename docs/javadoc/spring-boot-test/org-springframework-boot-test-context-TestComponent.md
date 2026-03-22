# Annotation Interface TestComponent

---

@Target(TYPE)
@Retention(RUNTIME)
@Documented
@Component
public @interface TestComponent
`@Component` that can be used when a bean is intended only for tests,
and should be excluded from Spring Boot's component scanning.

Note that if you directly use `@ComponentScan` rather than relying
on `@SpringBootApplication` you should ensure that a `TypeExcludeFilter` is
declared as an `excludeFilter`.

Since:
1.4.0
See Also:

- `TypeExcludeFilter`

- `TestConfiguration`

- 

## Optional Element Summary

Optional Elements

Modifier and Type
Optional Element
Description
`String`
`value`

The value may indicate a suggestion for a logical component name, to be turned into
a Spring bean in case of an auto-detected component.

- 

## Element Details

  - 

### value

@AliasFor(annotation=org.springframework.stereotype.Component.class)
String value
The value may indicate a suggestion for a logical component name, to be turned into
a Spring bean in case of an auto-detected component.

Returns:
the specified bean name, if any

Default:
`""`