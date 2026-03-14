# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/airbyte-results.md

# Module airbyte.results

Copy Page

Module which defines the `ReadResult` and `WriteResult` classes.

These classes are used to return information about read and write operations, respectively. They contain information such as the number of records read or written, the cache object, and the state handlers for a sync.

## Classes[​](#classes "Direct link to Classes")

`ReadResult(*, source_name: str, processed_streams: list[str], cache: CacheBase, progress_tracker: ProgressTracker)` : The result of a read operation.

This class is used to return information about the read operation, such as the number of records read. It should not be created directly, but instead returned by the write method of a destination.

Initialize a read result.

This class should not be created directly. Instead, it should be returned by the `read` method of the `Source` class.

### Ancestors (in MRO)[​](#ancestors-in-mro "Direct link to Ancestors (in MRO)")

* collections.abc.Mapping
* collections.abc.Collection
* collections.abc.Sized
* collections.abc.Iterable
* collections.abc.Container

### Instance variables[​](#instance-variables "Direct link to Instance variables")

`cache: CacheBase` : Return the cache object.

`processed_records: int` : The total number of records read from the source.

`streams: Mapping[str, CachedDataset]` : Return a mapping of stream names to cached datasets.

### Methods[​](#methods "Direct link to Methods")

`get_sql_engine(self) ‑> Engine` : Return the SQL engine used by the cache.

`WriteResult(*, destination: AirbyteWriterInterface | Destination, source_data: Source | ReadResult, catalog_provider: CatalogProvider, state_writer: StateWriterBase, progress_tracker: ProgressTracker)` : The result of a write operation.

This class is used to return information about the write operation, such as the number of records written. It should not be created directly, but instead returned by the write method of a destination.

Initialize a write result.

This class should not be created directly. Instead, it should be returned by the `write` method of the `Destination` class.

### Instance variables[​](#instance-variables-1 "Direct link to Instance variables")

`processed_records: int` : The total number of records written to the destination.

### Methods[​](#methods-1 "Direct link to Methods")

`get_state_provider(self) ‑> StateProviderBase` : Return the state writer as a state provider.

As a public interface, we only expose the state writer as a state provider. This is because the state writer itself is only intended for internal use. As a state provider, the state writer can be used to read the state artifacts that were written. This can be useful for testing or debugging.
