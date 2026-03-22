# Annotation Interface PropertyMapping

---

@Retention(RUNTIME)
@Target({TYPE,METHOD})
@Documented
public @interface PropertyMapping
Indicates that attributes from a test annotation should be mapped into a
`@PropertySource`. Can be used at the type level, or on individual
attributes. For example, the following annotation declaration: 

```

@Retention(RUNTIME)
@PropertyMapping("my.example")
public @interface Example {

  String name();

}

```
 When used on a test class as follows: 

```

@Example(name="Spring")
public class MyTest {
}

```
 will result in a my.example.name property being added with the value
"Spring".

Since:
4.0.0
See Also:

- `AnnotationsPropertySource`

- `TestPropertySource`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum `
`PropertyMapping.Skip`

Controls when mapping is skipped.

- 

## Optional Element Summary

Optional Elements

Modifier and Type
Optional Element
Description
`PropertyMapping.Skip`
`skip`

Determines if mapping should be skipped.

`String`
`value`

Defines the property mapping.

- 

## Element Details

  - 

### value

String value
Defines the property mapping. When used at the type-level, this value will be used
as a prefix for all mapped attributes. When used on an attribute, the value
overrides the generated (kebab case) name.

Returns:
the property mapping

Default:
`""`

  - 

### skip

PropertyMapping.Skip skip
Determines if mapping should be skipped. When specified at the type-level indicates
if skipping should occur by default or not. When used at the attribute-level,
overrides the type-level default.

Returns:
if mapping should be skipped

Default:
`NO`