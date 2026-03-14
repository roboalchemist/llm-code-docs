cargo::sources

# Module source

Source

## Structs§

SourceMapA `HashMap` of `SourceId` to `Box<Source>`.

## Enums§

MaybePackageA download status that represents if a `Package` has already been
downloaded, or if not then a location to download.QueryKindDefines how a dependency query will be performed for a `Source`.

## Traits§

SourceAn abstraction of different sources of Cargo packages.
