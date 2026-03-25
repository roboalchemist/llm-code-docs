Package jakarta.faces.annotation

# Annotation Interface View

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Retention(RUNTIME)
@Qualifier
@Documented
public @interface View

 The presence of this annotation on a target (type, method, parameter or field) within an application is used to indicate that
 this target is somehow handling a Faces View Id or Ids.

 The exact way in which such view is handled depends on the annotated element in question.

Since:
4.0

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`View.Literal`

Supports inline instantiation of the `View` annotation.

-

## Optional Element Summary

Optional Elements

Modifier and Type
Optional Element
Description
`String`
`value`

 Set the Faces View Id pattern.

-

## Element Details

-

### value

String value

 Set the Faces View Id pattern.

 The Faces View Id pattern can represent a single view, such as "/index.xhtml",
 or a pattern like "/foo/bar/*". Though the exact interpretation of the Faces View Id
 for a single view is ultimately defined by the annotated element, in general it should
 align with the return value from an action expression
 (see `ActionSource.setActionExpression(jakarta.el.MethodExpression)`

Returns:
the Faces View Id pattern

Default:
""
