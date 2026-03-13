Package jakarta.faces.annotation

# Annotation Interface InitParameterMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface InitParameterMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<String,
 String>` causes the map returned from `ExternalContext.getInitParameterMap()` to
 be injected as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`InitParameterMap.Literal`

 Supports inline instantiation of the `InitParameterMap` qualifier.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final jakarta.enterprise.util.TypeLiteral<Map<String,String>>`
`TYPE`

 Instance of the generic `InitParameterMap` type.

-

## Field Details

-

### TYPE

static final jakarta.enterprise.util.TypeLiteral<Map<String,String>> TYPE

 Instance of the generic `InitParameterMap` type.
