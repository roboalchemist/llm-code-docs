Package jakarta.faces.annotation

# Annotation Interface ViewMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface ViewMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 Object>` causes the map returned from `UIViewRoot.getViewMap()` to be injected
 as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`ViewMap.Literal`

 Supports inline instantiation of the `ViewMap` qualifier.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final jakarta.enterprise.util.TypeLiteral<Map<String,Object>>`
`TYPE`

 Instance of the generic `ViewMap` type.

-

## Field Details

-

### TYPE

static final jakarta.enterprise.util.TypeLiteral<Map<String,Object>> TYPE

 Instance of the generic `ViewMap` type.
