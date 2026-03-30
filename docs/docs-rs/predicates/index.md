# Crate predicates

Source

## Modules§

booleanDefinition of boolean logic combinators over `Predicate`s.constantDefinition of a constant (always true or always false) `Predicate`.floatFloat PredicatesfunctionDefinition of `Predicate` for wrapping a `Fn(&T) -> bool`iterDefinition of `Predicate`s for comparisons of membership in a set.nameName predicate expressions.ordDefinition of `Predicate`s for comparisons over `Ord` and `Eq` types.pathPath PredicatespreludeModule that contains the essentials for working with predicates.reflectionIntrospect into the state of a `Predicate`.strString Predicates

## Structs§

BoxPredicate`Predicate` that wraps another `Predicate` as a trait object, allowing
sized storage of predicate types.

## Traits§

PredicateTrait for generically evaluating a type against a dynamically created
predicate function.PredicateBoxExt`Predicate` extension for boxing a `Predicate`.
