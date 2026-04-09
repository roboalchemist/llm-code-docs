predicates

# Module path

Source

## Structs§

BinaryFilePredicatePredicate that compares file matchesExistencePredicatePredicate that checks if a file is presentFileContentPredicatePredicate adapter that converts a `path` predicate to a byte predicate on its content.FileTypePredicatePredicate that checks the `std::fs::FileType`.StrFilePredicatePredicate that compares string content of files

## Traits§

PredicateFileContentExt`Predicate` extension adapting a `slice` Predicate.

## Functions§

eq_fileCreates a new `Predicate` that ensures complete equalityexistsCreates a new `Predicate` that ensures the path exists.is_dirCreates a new `Predicate` that ensures the path points to a directory.is_fileCreates a new `Predicate` that ensures the path points to a file.is_symlinkCreates a new `Predicate` that ensures the path points to a symlink.missingCreates a new `Predicate` that ensures the path doesn’t exist.
