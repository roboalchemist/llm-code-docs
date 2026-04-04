# Source: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/llms.txt

# Amazon Keyspaces Streams API Reference

> Amazon Keyspaces (for Apache Cassandra) change data capture (CDC) records change events for Amazon Keyspaces tables. The change events captured in a stream are time-ordered and de-duplicated write operations. Using stream data you can build event driven applications that incorporate near-real time change events from Amazon Keyspaces tables.

- [Welcome](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Operations.html)

- [GetRecords](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_GetRecords.html): Retrieves data records from a specified shard in an Amazon Keyspaces data stream.
- [GetShardIterator](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_GetShardIterator.html): Returns a shard iterator that serves as a bookmark for reading data from a specific position in an Amazon Keyspaces data stream's shard.
- [GetStream](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_GetStream.html): Returns detailed information about a specific data capture stream for an Amazon Keyspaces table.
- [ListStreams](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ListStreams.html): Returns a list of all data capture streams associated with your Amazon Keyspaces account or for a specific keyspace or table.


## [Data Types](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Types.html)

- [KeyspacesCell](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesCell.html): Represents a cell in an Amazon Keyspaces table, containing both the value and metadata about the cell.
- [KeyspacesCellMapDefinition](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesCellMapDefinition.html): Represents a key-value pair within a map data type in Amazon Keyspaces, including the associated metadata.
- [KeyspacesCellValue](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesCellValue.html): Represents the value of a cell in an Amazon Keyspaces table, supporting various data types with type-specific fields.
- [KeyspacesMetadata](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesMetadata.html): Contains metadata information associated with Amazon Keyspaces cells and rows.
- [KeyspacesRow](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_KeyspacesRow.html): Represents a row in an Amazon Keyspaces table, containing regular column values, static column values, and row-level metadata.
- [Record](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Record.html): Represents a change data capture record for a row in an Amazon Keyspaces table, containing both the new and old states of the row.
- [SequenceNumberRange](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_SequenceNumberRange.html): Defines a range of sequence numbers within a change data capture stream's shard for Amazon Keyspaces.
- [Shard](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Shard.html): Represents a uniquely identified group of change records within a change data capture stream for Amazon Keyspaces.
- [ShardFilter](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ShardFilter.html): A filter used to limit the shards returned by a GetStream operation.
- [Stream](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Stream.html): Represents a change data capture stream for an Amazon Keyspaces table, which enables tracking and processing of data changes.


## [Service-specific Errors](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Errors.html)

- [AccessDeniedException](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_AccessDeniedException.html): You don't have sufficient access permissions to perform this operation.
- [InternalServerException](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_InternalServerException.html): The Amazon Keyspaces service encountered an unexpected error while processing the request.
- [ResourceNotFoundException](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ResourceNotFoundException.html): The requested resource doesn't exist or could not be found.
- [ThrottlingException](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ThrottlingException.html): The request rate is too high and exceeds the service's throughput limits.
- [ValidationException](https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ValidationException.html): The request validation failed because one or more input parameters failed validation.
