predicates

# Module function

Source

## Structs§

FnPredicatePredicate that wraps a function over a reference that returns a `bool`.
This type is returned by the `predicate::function` function.

## Functions§

functionCreates a new predicate that wraps over the given function. The returned
type implements `Predicate` and therefore has all combinators available to
it.
