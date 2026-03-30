proptest
# Module arbitrary 
Source 
## Modules§
functorProvides higher order `Arbitrary` traits.
This is mainly for use by `proptest_derive`.
## Traits§
ArbitraryArbitrary determines a canonical `Strategy` for the implementing type.
## Functions§
anyGenerates a `Strategy` producing `Arbitrary` values of
`A`. Unlike `arbitrary`, it should be used for being
explicit on what `A` is. For clarity, this may be a good idea.any_withGenerates a `Strategy` producing `Arbitrary` values of `A` with the
given configuration arguments passed in `args`. Unlike `arbitrary_with`,
it should be used for being explicit on what `A` is.
For clarity, this may be a good idea.arbitraryGenerates a `Strategy` producing `Arbitrary` values of `A`.
Works better with type inference than `any::<A>()`.arbitrary_withGenerates a `Strategy` producing `Arbitrary` values of `A` with the
given configuration arguments passed in `args`.
Works better with type inference than `any_with::<A>(args)`.
## Type Aliases§
MappedA normal map from a strategy of `I` to `O`.ParamsFor`ParamsFor` allows you to mention the type of `Parameters` for the input
type `A` without directly using associated types or without resorting to
existential types. This way, if implementation of `Arbitrary` changes,
your tests should not break.SMappedA static map from a strategy of `I` to `O`.StrategyFor`StrategyFor` allows you to mention the type of `Strategy` for the input
type `A` without directly using associated types or without resorting to
existential types. This way, if implementation of `Arbitrary` changes,
your tests should not break. This can be especially beneficial when the
type of `Strategy` that you are dealing with is very long in name
(the case with generics).