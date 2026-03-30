# Package org.springframework.boot.test.context

---

@NullMarked
package org.springframework.boot.test.context

Support for mapping annotation attribute values in the Spring `Environment`.

- 

Related Packages

Package
Description
org.springframework.boot.test.context.assertj

AssertJ support for ApplicationContexts.

org.springframework.boot.test.context.runner

Test utilities to run application contexts for testing.

- 

Class
Description
AnnotatedClassFinder

Utility class to find a class annotated with a particular annotation in a hierarchy.

ConfigDataApplicationContextInitializer

`ApplicationContextInitializer` that can be used with the
`ContextConfiguration.initializers()` to trigger loading of `ConfigData`
such as application.properties.

FilteredClassLoader

Test `URLClassLoader` that can filter the classes and resources it can load.

FilteredClassLoader.ClassFilter

Filter to restrict the classes that can be loaded.

FilteredClassLoader.ClassPathResourceFilter

Filter to restrict the resources that can be loaded.

FilteredClassLoader.PackageFilter

Filter to restrict the packages that can be loaded.

PropertyMapping

Indicates that attributes from a test annotation should be mapped into a
`@PropertySource`.

PropertyMapping.Skip

Controls when mapping is skipped.

ReactiveWebMergedContextConfiguration

Encapsulates the *merged* context configuration declared on a test class and all
of its superclasses for a reactive web application.

SpringBootContextLoader

A `ContextLoader` that can be used to test Spring Boot applications (those that
normally startup using `SpringApplication`).

SpringBootTest

Annotation that can be specified on a test class that runs Spring Boot based tests.

SpringBootTest.UseMainMethod

Enumeration of how the main method of the
`@SpringBootConfiguration`-annotated class is used
when creating and running the `SpringApplication` under test.

SpringBootTest.WebEnvironment

An enumeration web environment modes.

SpringBootTestAotProcessor

Entry point for AOT processing of a Spring Boot application's tests.

SpringBootTestContextBootstrapper

`TestContextBootstrapper` for Spring Boot.

TestComponent

`@Component` that can be used when a bean is intended only for tests,
and should be excluded from Spring Boot's component scanning.

TestConfiguration

`@Configuration` that can be used to define additional beans or
customizations for a test.