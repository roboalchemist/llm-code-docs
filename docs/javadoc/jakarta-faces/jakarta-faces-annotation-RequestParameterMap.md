Package jakarta.faces.annotation

# Annotation Interface RequestParameterMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface RequestParameterMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String>` causes the map returned from `ExternalContext.getRequestParameterMap()`
 to be injected as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`RequestParameterMap.Literal`

 Supports inline instantiation of the `RequestParameterMap` qualifier.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final jakarta.enterprise.util.TypeLiteral<Map<String,String>>`
`TYPE`

 Instance of the generic `RequestParameterMap` type.

-

## Field Details

-

### TYPE

static final jakarta.enterprise.util.TypeLiteral<Map<String,String>> TYPE

 Instance of the generic `RequestParameterMap` type.
