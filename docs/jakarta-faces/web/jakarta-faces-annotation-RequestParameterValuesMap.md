Package jakarta.faces.annotation

# Annotation Interface RequestParameterValuesMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface RequestParameterValuesMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String []>` causes the map returned from
 `ExternalContext.getRequestParameterValuesMap()` to be injected as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`RequestParameterValuesMap.Literal`

 Supports inline instantiation of the `RequestParameterValuesMap` qualifier.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final jakarta.enterprise.util.TypeLiteral<Map<String,String[]>>`
`TYPE`

 Instance of the generic `RequestParameterValuesMap` type.

-

## Field Details

-

### TYPE

static final jakarta.enterprise.util.TypeLiteral<Map<String,String[]>> TYPE

 Instance of the generic `RequestParameterValuesMap` type.
