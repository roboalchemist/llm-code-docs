# Annotation Interface TestConfiguration

---

@Target(TYPE)
@Retention(RUNTIME)
@Documented
@Configuration
@TestComponent
public @interface TestConfiguration
`@Configuration` that can be used to define additional beans or
customizations for a test. Unlike regular `@Configuration` classes the use of
`@TestConfiguration` does not prevent auto-detection of
`@SpringBootConfiguration`.

Since:
1.4.0
See Also:

- `SpringBootTestContextBootstrapper`

- 

## Optional Element Summary

Optional Elements

Modifier and Type
Optional Element
Description
`boolean`
`proxyBeanMethods`

Specify whether `@Bean` methods should get proxied in order to enforce
bean lifecycle behavior, e.g.

`String`
`value`

Explicitly specify the name of the Spring bean definition associated with this
Configuration class.

- 

## Element Details

  - 

### value

@AliasFor(annotation=org.springframework.context.annotation.Configuration.class)
String value
Explicitly specify the name of the Spring bean definition associated with this
Configuration class. See `Configuration.value()` for details.

Returns:
the specified bean name, if any

Default:
`""`

  - 

### proxyBeanMethods

@AliasFor(annotation=org.springframework.context.annotation.Configuration.class)
boolean proxyBeanMethods
Specify whether `@Bean` methods should get proxied in order to enforce
bean lifecycle behavior, e.g. to return shared singleton bean instances even in
case of direct `@Bean` method calls in user code. This feature requires
method interception, implemented through a runtime-generated CGLIB subclass which
comes with limitations such as the configuration class and its methods not being
allowed to declare `final`.

The default is `true`, allowing for 'inter-bean references' within the
configuration class as well as for external calls to this configuration's
`@Bean` methods, e.g. from another configuration class. If this is not needed
since each of this particular configuration's `@Bean` methods is
self-contained and designed as a plain factory method for container use, switch
this flag to `false` in order to avoid CGLIB subclass processing.

Turning off bean method interception effectively processes `@Bean` methods
individually like when declared on non-`@Configuration` classes, a.k.a.
"@Bean Lite Mode" (see `@Bean's javadoc`). It is therefore behaviorally
equivalent to removing the `@Configuration` stereotype.

Returns:
whether to proxy `@Bean` methods
Since:
2.2.1

Default:
`true`