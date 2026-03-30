druid

# Module env

Source

## Structs§

EnvAn environment passed down through all widget traversals.KeyA typed `Env` key.MissingKeyErrorAn error type for when a key is missing from the `Env`.ValueTypeErrorThe error type for environment access.

## Enums§

KeyOrValueEither a concrete `T` or a `Key<T>` that can be resolved in the `Env`.ValueA dynamic type representing all values that can be stored in an environment.

## Traits§

KeyLikeA trait for anything that can resolve a value of some type from the `Env`.ValueTypeValues which can be stored in an environment.
