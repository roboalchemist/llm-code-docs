# Annotation Interface SpringBootTest

---

@Target(TYPE)
@Retention(RUNTIME)
@Documented
@Inherited
@BootstrapWith(SpringBootTestContextBootstrapper.class)
@ExtendWith(org.springframework.test.context.junit.jupiter.SpringExtension.class)
public @interface SpringBootTest
Annotation that can be specified on a test class that runs Spring Boot based tests.
Provides the following features over and above the regular *Spring TestContext
Framework*:

- Uses `SpringBootContextLoader` as the default `ContextLoader` when no
specific `@ContextConfiguration(loader=...)` is
defined.

- Automatically searches for a
`@SpringBootConfiguration` when nested
`@Configuration` is not used, and no explicit `classes` are
specified.

- Allows custom `Environment` properties to be defined using the
`properties attribute`.

- Allows application arguments to be defined using the `args
attribute`.

- Provides support for different `webEnvironment` modes,
including the ability to start a fully running web server listening on a
`defined` or `random` port when `spring-boot-web-server` is on the classpath.

Since:
1.4.0
See Also:

- `ContextConfiguration`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`SpringBootTest.UseMainMethod`

Enumeration of how the main method of the
`@SpringBootConfiguration`-annotated class is used
when creating and running the `SpringApplication` under test.

`static enum `
`SpringBootTest.WebEnvironment`

An enumeration web environment modes.

- 

## Optional Element Summary

Optional Elements

Modifier and Type
Optional Element
Description
`String[]`
`args`

Application arguments that should be passed to the application under test.

`Class<?>[]`
`classes`

The *component classes* to use for loading an
`ApplicationContext`.

`String[]`
`properties`

Properties in form key=value that should be added to the Spring
`Environment` before the test runs.

`SpringBootTest.UseMainMethod`
`useMainMethod`

The type of main method usage to employ when creating the `SpringApplication`
under test.

`String[]`
`value`

Alias for `properties()`.

`SpringBootTest.WebEnvironment`
`webEnvironment`

The type of web environment to create when applicable.

- 

## Element Details

  - 

### value

@AliasFor("properties")
String[] value
Alias for `properties()`.

Returns:
the properties to apply

Default:
`{}`

  - 

### properties

@AliasFor("value")
String[] properties
Properties in form key=value that should be added to the Spring
`Environment` before the test runs.

Returns:
the properties to add

Default:
`{}`

  - 

### args

String[] args
Application arguments that should be passed to the application under test.

Returns:
the application arguments to pass to the application under test.
Since:
2.2.0
See Also:

    - `ApplicationArguments`

    - `SpringApplication.run(String...)`

Default:
`{}`

  - 

### classes

Class<?>[] classes
The *component classes* to use for loading an
`ApplicationContext`. Can also
be specified using
`@ContextConfiguration(classes=...)`. If no
explicit classes are defined the test will look for nested
`@Configuration` classes, before falling back to a
`@SpringBootConfiguration` search.

Returns:
the component classes used to load the application context
See Also:

    - `ContextConfiguration.classes()`

Default:
`{}`

  - 

### webEnvironment

SpringBootTest.WebEnvironment webEnvironment
The type of web environment to create when applicable. Defaults to
`SpringBootTest.WebEnvironment.MOCK`.

Returns:
the type of web environment

Default:
`MOCK`

  - 

### useMainMethod

SpringBootTest.UseMainMethod useMainMethod
The type of main method usage to employ when creating the `SpringApplication`
under test.

Returns:
the type of main method usage
Since:
3.0.0

Default:
`NEVER`