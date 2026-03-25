Package jakarta.faces.annotation

# Annotation Interface ApplicationMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface ApplicationMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `ExternalContext.getApplicationMap()` to be
 injected as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`ApplicationMap.Literal`

 Supports inline instantiation of the `ApplicationMap` qualifier.

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
