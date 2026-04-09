Package jakarta.faces.annotation

# Annotation Interface RequestMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface RequestMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `ExternalContext.getRequestMap()` to be
 injected as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`RequestMap.Literal`

 Supports inline instantiation of the `RequestMap` qualifier.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final jakarta.enterprise.util.TypeLiteral<Map<String,Object>>`
`TYPE`

 Instance of the generic `ApplicationMap` type.

-

## Field Details

-

### TYPE

static final jakarta.enterprise.util.TypeLiteral<Map<String,Object>> TYPE

 Instance of the generic `ApplicationMap` type.
