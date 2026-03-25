Package jakarta.faces.annotation

# Annotation Interface FlowMap

---

@Target({TYPE,METHOD,PARAMETER,FIELD})
@Qualifier
@Retention(RUNTIME)
public @interface FlowMap

 The presence of this annotation (along with `@Inject`) on a field of type `Map<Object,
 Object>` causes the map returned from `FlowHandler.getCurrentFlowScope()` to be
 injected as the value of that field.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`FlowMap.Literal`

 Supports inline instantiation of the `ApplicationMap` qualifier.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final jakarta.enterprise.util.TypeLiteral<Map<Object,Object>>`
`TYPE`

 Instance of the generic `FlowMap` type.

-

## Field Details

-

### TYPE

static final jakarta.enterprise.util.TypeLiteral<Map<Object,Object>> TYPE

 Instance of the generic `FlowMap` type.
