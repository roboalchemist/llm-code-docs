# Crate taos 
Source 
## Re-exports§
`pub use taos_query;`
## Modules§
synctokioA runtime for writing reliable network applications without compromising speed.
## Structs§
AddressA simple struct to represent a server address, with host:port or socket path.AsyncBlocksAsyncDeserializedAsyncRowsCodeThe error code.ConsumerDataDeErrorA minimal representation of all possible errors that can occur using the
`IntoDeserializer` trait.DsnA DSN(**Data Source Name**) parser.ErrorThe `Error` type, a wrapper around raw libtaos.so client errors or
dynamic error types that could be integrated into anyhow::Error.FieldA `Field` represents the name and data type of one column or tag.MetaMetaAlterOffsetRawBlockRaw data block format (B for bytes):RawErrorThe `Error` type, a wrapper around raw libtaos.so client errors or
dynamic error types that could be integrated into anyhow::Error.RawMetaResultSetStmtTagWithValueTaosTaosBuilderTmqBuilder
## Enums§
AlterTypeBorrowedValueColumnViewDsnErrorError caused by pest DSN parser.JsonMetaMetaCreateMetaDropMetaUnitPrecisionThe precision of a timestamp or a database.TimeoutTyTDengine data type enumeration.Value
## Traits§
AsAsyncConsumerAsyncBindableAsyncFetchableAsyncInlinableIf one struct could be serialized/flattened to bytes array, we call it **inlinable**.AsyncInlinableReadAsyncInlinableWriteAsyncQueryableThe synchronous query trait for TDengine connection.AsyncTBuilderA struct is `Connectable` when it can be build from a `Dsn`.HelpersInlinableIf one struct could be serialized/flattened to bytes array, we call it **inlinable**.InlinableReadInlinableWriteIntoDsnIsAsyncDataIsAsyncMetaIsOffsetExtract offset information.ItertoolsAn `Iterator` blanket implementation that provides extra adaptors and
methods.StreamA stream of values produced asynchronously.StreamExtAn extension trait for `Stream`s that provides a variety of convenient
combinator functions.TryStreamExtAdapters specific to `Result`-returning streams
## Type Aliases§
MessageSetPoolRawResultTaosPool