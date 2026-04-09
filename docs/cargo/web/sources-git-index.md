cargo::sources

# Module git

Source

## Modules§

fetchFor `-Zgitoxide` integration.

## Structs§

GitCheckoutA local checkout of a particular revision from a `GitDatabase`.GitDatabaseA local clone of a remote repository’s database. Multiple `GitCheckout`s
can be cloned from a single `GitDatabase`.GitRemoteA remote repository. It gets cloned into a local `GitDatabase`.GitSource`GitSource` contains one or more packages gathering from a Git repository.
Under the hood it uses `RecursivePathSource` to discover packages inside the
repository.

## Functions§

fetchAttempts to fetch the given git `reference` for a Git repository.resolve_refResolves `GitReference` to an object ID with objects the `repo` currently has.
