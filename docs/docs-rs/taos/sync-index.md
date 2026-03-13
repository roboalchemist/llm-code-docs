taos
# Module sync 
Source 
## Re-exports§
`pub use super::Stmt;``pub use super::Consumer;``pub use super::MessageSet;``pub use super::Offset;``pub use super::TmqBuilder;``pub use super::Taos;``pub use super::TaosBuilder;`
## Structs§
AddressA simple struct to represent a server address, with host:port or socket path.CodeThe error code.DeErrorA minimal representation of all possible errors that can occur using the
`IntoDeserializer` trait.DsnA DSN(**Data Source Name**) parser.FieldA `Field` represents the name and data type of one column or tag.IBlockIterIRowsIterMetaAlterRawBlockRaw data block format (B for bytes):RawErrorThe `Error` type, a wrapper around raw libtaos.so client errors or
dynamic error types that could be integrated into anyhow::Error.RawMetaTagWithValue
## Enums§
AlterTypeBorrowedValueColumnViewDsnErrorError caused by pest DSN parser.JsonMetaMetaCreateMetaDropMetaUnitPrecisionThe precision of a timestamp or a database.TimeoutTyTDengine data type enumeration.Value
## Traits§
AsConsumerBindableFetchableInlinableIf one struct could be serialized/flattened to bytes array, we call it **inlinable**.InlinableReadInlinableWriteIntoDsnIsDataIsMetaIsOffsetExtract offset information.ItertoolsAn `Iterator` blanket implementation that provides extra adaptors and
methods.QueryableThe synchronous query trait for TDengine connection.TBuilderA struct is `Connectable` when it can be build from a `Dsn`.
## Type Aliases§
RawResult