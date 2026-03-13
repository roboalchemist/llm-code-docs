Package jakarta.faces.annotation

# Annotation Interface SessionMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface SessionMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `ExternalContext.getSessionMap()` to be
 injected as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`SessionMap.Literal`

 Supports inline instantiation of the `SessionMap` qualifier.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final jakarta.enterprise.util.TypeLiteral<Map<String,Object>>`
`TYPE`

 Instance of the generic `SessionMap` type.

-

## Field Details

-

### TYPE

static final jakarta.enterprise.util.TypeLiteral<Map<String,Object>> TYPE

 Instance of the generic `SessionMap` type.
