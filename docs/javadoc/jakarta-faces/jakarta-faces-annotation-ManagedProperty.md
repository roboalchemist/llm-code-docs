Package jakarta.faces.annotation

# Annotation Interface ManagedProperty

---

@Qualifier
@Target(FIELD)
@Retention(RUNTIME)
public @interface ManagedProperty

 The presence of this annotation (along with `@Inject`) on a field of any type causes the value returned from
 evaluating an expression language expression to be injected as the value of that field.

 This expression will be evaluated using `Application.evaluateExpressionGet(jakarta.faces.context.FacesContext, String, Class)`,
 which in turn implies that the `FacesContext.getCurrentInstance()` must be available at the moment of the evaluation.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`ManagedProperty.Literal`

 Supports inline instantiation of the `ManagedProperty` qualifier.

-

## Required Element Summary

Required Elements

Modifier and Type
Required Element
Description
`String`
`value`

 Taken to be the value that is injected into the field.

-

## Element Details

-

### value

String value

 Taken to be the value that is injected into the field.

Returns:
the value.
