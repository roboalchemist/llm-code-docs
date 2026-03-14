predicates

# Module ord

Source

## Structs§

EqPredicatePredicate that returns `true` if `variable` matches the pre-defined `Eq`
value, otherwise returns `false`.OrdPredicatePredicate that returns `true` if `variable` matches the pre-defined `Ord`
value, otherwise returns `false`.

## Functions§

eqCreates a new predicate that will return `true` when the given `variable` is
equal to a pre-defined value.geCreates a new predicate that will return `true` when the given `variable` is
greater than or equal to a pre-defined value.gtCreates a new predicate that will return `true` when the given `variable` is
greater than a pre-defined value.leCreates a new predicate that will return `true` when the given `variable` is
less than or equal to a pre-defined value.ltCreates a new predicate that will return `true` when the given `variable` is
less than a pre-defined value.neCreates a new predicate that will return `true` when the given `variable` is
*not* equal to a pre-defined value.
