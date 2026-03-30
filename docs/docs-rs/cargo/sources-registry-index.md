cargo::sources

# Module registry

Source

## Structs§

RegistryConfigThe `config.json` file stored in the index.RegistrySourceA `Source` implementation for a local or a remote registry.

## Enums§

IndexSummaryA parsed representation of a summary from the index. This is usually parsed
from a line from a raw index file, or a JSON blob from on-disk index cache.LoadResponseResult from loading data from a registry.MaybeLockThe status of `RegistryData::download` which indicates if a `.crate`
file has already been downloaded, or if not then the URL to download.

## Constants§

CRATES_IO_DOMAINCRATES_IO_HTTP_INDEXCRATES_IO_INDEXCRATES_IO_REGISTRY

## Traits§

RegistryDataAn abstract interface to handle both a local and remote registry.
