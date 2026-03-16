# Interface ContextConsumer<C extends org.springframework.context.ApplicationContext>

Type Parameters:
`C` - the application context type

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

@FunctionalInterface
public interface ContextConsumer<C extends org.springframework.context.ApplicationContext>
Callback interface used to process an `ApplicationContext` with the ability to
throw a (checked) exception.

Since:
2.0.0
See Also:

- `AbstractApplicationContextRunner`

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`accept(C context)`

Performs this operation on the supplied `context`.

`default ContextConsumer<C>`
`andThen(ContextConsumer<? super C> after)`

Returns a composed `ContextConsumer` that performs, in sequence, this
operation followed by the `after` operation.

- 

## Method Details

  - 

### accept

void accept(C context)
     throws Throwable
Performs this operation on the supplied `context`.

Parameters:
`context` - the application context to consume
Throws:
`Throwable` - any exception that might occur in assertions

  - 

### andThen

default ContextConsumer<C> andThen(ContextConsumer<? super C> after)
Returns a composed `ContextConsumer` that performs, in sequence, this
operation followed by the `after` operation.

Parameters:
`after` - the operation to perform after this operation
Returns:
a composed `ContextConsumer` that performs in sequence this operation
followed by the `after` operation
Since:
2.6.0