proptest
# Module strategy 
Source 
## Modules§
staticsModified versions of the normal strategy combinators which take specialised
traits instead of normal functions.
## Structs§
BoxedStrategyA boxed `Strategy` trait object as produced by `Strategy::boxed()`.CheckStrategySanityOptionsOptions passed to `check_strategy_sanity()`.Filter`Strategy` and `ValueTree` filter adaptor.FilterMap`Strategy` and `ValueTree` filter_map adaptor.FilterMapValueTree`ValueTree` corresponding to `FilterMap`.FlattenAdaptor that flattens a `Strategy` which produces other `Strategy`s into a
`Strategy` that picks one of those strategies and then picks values from
it.FlattenValueTreeThe `ValueTree` produced by `Flatten`.FuseAdaptor for `Strategy` and `ValueTree` which guards `simplify()` and
`complicate()` to avoid contract violations.IndFlattenSimilar to `Flatten`, but does not shrink the input strategy.IndFlattenMapSimilar to `Map` plus `Flatten`, but does not shrink the input strategy and
passes the original input through.JustA `Strategy` which always produces a single value and never
simplifies.LazyJustA `Strategy` which always produces a single value and never
simplifies. If `T` is `Clone`, you should use `Just` instead.LazyValueTreeRepresents a value tree that is initialized on the first call to any
methods.Map`Strategy` and `ValueTree` map adaptor.MapInto`Strategy` and `ValueTree` map into adaptor.NoShrinkWraps a `Strategy` or `ValueTree` to suppress shrinking of generated
values.Perturb`Strategy` perturbation adaptor.PerturbValueTree`ValueTree` perturbation adaptor.RecursiveReturn type from `Strategy::prop_recursive()`.SBoxedStrategyA boxed `Strategy` trait object which is also `Sync` and
`Send`, as produced by `Strategy::sboxed()`.Shuffle`Strategy` shuffle adaptor.ShuffleValueTree`ValueTree` shuffling adaptor.TupleUnionSimilar to `Union`, but internally uses a tuple to hold the strategies.TupleUnionValueTree`ValueTree` type produced by `TupleUnion`.UnionA `Strategy` which picks from one of several delegate `Strategy`s.UnionValueTree`ValueTree` corresponding to `Union`.
## Traits§
ShuffleableA value which can be used with the `prop_shuffle` combinator.StrategyA strategy for producing arbitrary values of a given type.ValueTreeA generated value and its associated shrinker.
## Functions§
check_strategy_sanityRun some tests on the given `Strategy` to ensure that it upholds the
simplify/complicate contracts.float_to_weightConvert a floating-point weight in the range (0.0,1.0) to a pair of weights
that can be used with `Union` and similar.
## Type Aliases§
LazyJustFnShorthand for `LazyJust<T, fn () -> T>`.NewTreeA new `ValueTree` from a `Strategy` when `Ok` or otherwise `Err`
when a new value-tree can not be produced for some reason such as
in the case of filtering with a predicate which always returns false.
You should pass in your strategy as the type parameter.WA **relative** `weight` of a particular `Strategy` corresponding to `T`
coupled with `T` itself. The weight is currently given in `u32`.WAA **relative** `weight` of a particular `Strategy` corresponding to `T`
coupled with `Arc<T>`. The weight is currently given in `u32`.