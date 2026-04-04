# Source: https://firebase.google.com/docs/firestore/enterprise/supported-features-70.md.txt

<br />

The following tables include a breakdown of MongoDB 7.0 features supported by Cloud Firestore with MongoDB compatibility. For differences in behavior, see[Behavior differences](https://firebase.google.com/docs/firestore/enterprise/behavior-differences).

<br />

## Query and projection operators

Cloud Firestore with MongoDB compatibility supports the following query and projection operators:

### Array operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$all`       | Yes           |
| `$elemMatch` | Yes           |
| `$size`      | Yes           |

### Bitwise operators

|  **Operator**   | **Supported** |
|-----------------|---------------|
| `$bitsAllClear` | No            |
| `$bitsAllSet`   | No            |
| `$bitsAnyClear` | No            |
| `$bitsAnySet`   | No            |

### Comment operator

| **Operator** | **Supported** |
|--------------|---------------|
| `$comment`   | No            |

### Comparison operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$eq`        | Yes           |
| `$gt`        | Yes           |
| `$gte`       | Yes           |
| `$in`        | Yes           |
| `$lt`        | Yes           |
| `$lte`       | Yes           |
| `$ne`        | Yes           |
| `$nin`       | Yes           |

### Element operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$exists`    | Yes           |
| `$type`      | Yes           |

### Evaluation query operators

| **Operator**  | **Supported** |
|---------------|---------------|
| `$expr`       | Yes           |
| `$jsonSchema` | No            |
| `$mod`        | Yes           |
| `$regex`      | Yes           |
| `$text`       | No            |
| `$where`      | No            |

### Logical operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$and`       | Yes           |
| `$nor`       | Yes           |
| `$not`       | Yes           |
| `$or`        | Yes           |

### Projection operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$`          | Yes           |
| `$elemMatch` | Yes           |
| `$meta`      | No            |
| `$slice`     | Yes           |

## Update operators

Cloud Firestore with MongoDB compatibility supports the following update operators.

### Array operators

|   **Operator**    | **Supported** |
|-------------------|---------------|
| `$`               | Yes           |
| `$[]`             | Yes           |
| `$[<identifier>]` | Yes           |
| `$addToSet`       | Yes           |
| `$percentile`     | Yes           |
| `$pop`            | Yes           |
| `$pull`           | Yes           |
| `$pullAll`        | Yes           |
| `$push`           | Yes           |

### Bitwise operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$bit`       | Yes           |

### Field operators

|  **Operator**  | **Supported** |
|----------------|---------------|
| `$currentDate` | Yes           |
| `$inc`         | Yes           |
| `$max`         | Yes           |
| `$min`         | Yes           |
| `$mul`         | Yes           |
| `$rename`      | Yes           |
| `$set`         | Yes           |
| `$setOnInsert` | Yes           |
| `$unset`       | Yes           |

### Update modifiers

| **Modifier** | **Supported** |
|--------------|---------------|
| `$each`      | Yes           |
| `$position`  | Yes           |
| `$slice`     | Yes           |
| `$sort`      | Yes           |

## Aggregation pipeline operators

Cloud Firestore with MongoDB compatibility supports the following aggregation pipeline operators.

### Accumulators

| **Expression**  | **Supported** |
|-----------------|---------------|
| `$accumulator`  | No            |
| `$addToSet`     | Yes           |
| `$avg`          | Yes           |
| `$bottom`       | No            |
| `$bottomN`      | No            |
| `$count`        | Yes           |
| `$first`        | Yes           |
| `$firstN`       | No            |
| `$last`         | Yes           |
| `$lastN`        | No            |
| `$max`          | Yes           |
| `$maxN`         | No            |
| `$median`       | No            |
| `$mergeObjects` | Yes           |
| `$min`          | Yes           |
| `$minN`         | No            |
| `$percentile`   | No            |
| `$push`         | Yes           |
| `$stdDevPop`    | No            |
| `$stdDevSamp`   | No            |
| `$sum`          | Yes           |
| `$top`          | No            |
| `$topN`         | No            |

### Accumulator expressions

| **Expression** | **Supported** |
|----------------|---------------|
| `$avg`         | Yes           |
| `$first`       | Yes           |
| `$last`        | Yes           |
| `$max`         | Yes           |
| `$median`      | Yes           |
| `$min`         | Yes           |
| `$percentile`  | Yes           |
| `$stdDevPop`   | No            |
| `$stdDevSamp`  | No            |
| `$sum`         | Yes           |

### Arithmetic operators

**Limitations** : Arithmetic operators don't support`decimal128`values.

| **Operator** | **Supported** |
|--------------|---------------|
| `$abs`       | Yes           |
| `$add`       | Yes           |
| `$ceil`      | Yes           |
| `$divide`    | Yes           |
| `$exp`       | Yes           |
| `$floor`     | Yes           |
| `$ln`        | Yes           |
| `$log`       | Yes           |
| `$log10`     | Yes           |
| `$mod`       | Yes           |
| `$multiply`  | Yes           |
| `$pow`       | Yes           |
| `$round`     | Yes           |
| `$sqrt`      | Yes           |
| `$subtract`  | Yes           |
| `$trunc`     | Yes           |

### Array operators

|   **Operator**   | **Supported** |
|------------------|---------------|
| `$arrayElemAt`   | Yes           |
| `$arrayToObject` | Yes           |
| `$concatArrays`  | Yes           |
| `$filter`        | Yes           |
| `$firstN`        | Yes           |
| `$in`            | Yes           |
| `$indexOfArray`  | Yes           |
| `$isArray`       | Yes           |
| `$lastN`         | Yes           |
| `$map`           | Yes           |
| `$maxN`          | Yes           |
| `$minN`          | Yes           |
| `$objectToArray` | Yes           |
| `$range`         | Yes           |
| `$reduce`        | Yes           |
| `$reverseArray`  | Yes           |
| `$size`          | Yes           |
| `$slice`         | Yes           |
| `$sortArray`     | Yes           |
| `$zip`           | Yes           |

### Boolean operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$and`       | Yes           |
| `$not`       | Yes           |
| `$or`        | Yes           |

### Comparison operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$cmp`       | Yes           |
| `$eq`        | Yes           |
| `$gt`        | Yes           |
| `$gte`       | Yes           |
| `$lt`        | Yes           |
| `$lte`       | Yes           |
| `$ne`        | Yes           |

### Conditional expression operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$cond`      | Yes           |
| `$ifNull`    | Yes           |
| `$switch`    | Yes           |

### Data size operators

<br />

| **Operator**  | **Supported** |
|---------------|---------------|
| `$binarySize` | Yes           |
| `$bsonSize`   | Yes           |

### Date operators

|   **Operator**    | **Supported** |
|-------------------|---------------|
| `$dateAdd`        | Yes           |
| `$dateDiff`       | Yes           |
| `$dateFromParts`  | Yes           |
| `$dateFromString` | Yes           |
| `$dateSubtract`   | Yes           |
| `$dateToParts`    | Yes           |
| `$dateToString`   | Yes           |
| `$dateTrunc`      | Yes           |
| `$dayOfMonth`     | Yes           |
| `$dayOfWeek`      | Yes           |
| `$dayOfYear`      | Yes           |
| `$hour`           | Yes           |
| `$isoDayOfWeek`   | Yes           |
| `$isoWeek`        | Yes           |
| `$isoWeekYear`    | Yes           |
| `$millisecond`    | Yes           |
| `$minute`         | Yes           |
| `$month`          | Yes           |
| `$second`         | Yes           |
| `$toDate`         | Yes           |
| `$week`           | Yes           |
| `$year`           | Yes           |

### Timestamp operators

<br />

|  **Operator**  | **Supported** |
|----------------|---------------|
| `$tsIncrement` | No            |
| `$tsSecond`    | No            |

### Miscellaneous operators

|    **Operator**     |  **Supported**  |
|---------------------|-----------------|
| `$getField`         | Yes             |
| `$natural`          | Yes (ascending) |
| `$rand`             | Yes             |
| `$sampleRate`       | No              |
| `$toHashedIndexKey` | No              |

### Literal expression operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$literal`   | Yes           |

### Object operators

|   **Operator**   | **Supported** |
|------------------|---------------|
| `$mergeObjects`  | Yes           |
| `$objectToArray` | Yes           |
| `$setField`      | No            |

### Set operators

|    **Operator**    | **Supported** |
|--------------------|---------------|
| `$allElementsTrue` | Yes           |
| `$anyElementTrue`  | Yes           |
| `$setDifference`   | Yes           |
| `$setEquals`       | Yes           |
| `$setIntersection` | Yes           |
| `$setIsSubset`     | Yes           |
| `$setUnion`        | Yes           |

### Stage operators

|     **Operator**     |                  **Supported**                   |
|----------------------|--------------------------------------------------|
| `$addFields`         | Yes                                              |
| `$bucket`            | Yes                                              |
| `$bucketAuto`        | No                                               |
| `$changeStreams`     | No                                               |
| `$collStats`         | No                                               |
| `$count`             | Yes                                              |
| `$currentOp`         | No                                               |
| `$documents`         | Yes                                              |
| `$facet`             | Yes                                              |
| `$geoNear`           | No                                               |
| `$graphLookup`       | No                                               |
| `$group`             | Yes                                              |
| `$indexStats`        | No                                               |
| `$limit`             | Yes                                              |
| `$listLocalSessions` | No                                               |
| `$listSessions`      | No                                               |
| `$lookup`            | Yes Doesn't support the`let`and`pipeline`fields. |
| `$match`             | Yes                                              |
| `$merge`             | No                                               |
| `$out`               | No                                               |
| `$planCacheStats`    | No                                               |
| `$project`           | Yes                                              |
| `$redact`            | No                                               |
| `$replaceRoot`       | Yes                                              |
| `$replaceWith`       | Yes                                              |
| `$sample`            | No                                               |
| `$set`               | Yes                                              |
| `$search`            | No                                               |
| `$setWindowFields`   | No                                               |
| `$skip`              | Yes                                              |
| `$sort`              | Yes                                              |
| `$sortByCount`       | Yes                                              |
| `$unionWith`         | Yes                                              |
| `$unset`             | Yes                                              |
| `$unwind`            | Yes                                              |

### String operators

|   **Operator**    | **Supported** |
|-------------------|---------------|
| `$concat`         | Yes           |
| `$dateFromString` | Yes           |
| `$dateToString`   | Yes           |
| `$indexOfBytes`   | Yes           |
| `$indexOfCP`      | Yes           |
| `$ltrim`          | Yes           |
| `$regexFind`      | Yes           |
| `$regexFindAll`   | Yes           |
| `$regexMatch`     | Yes           |
| `$replaceAll`     | Yes           |
| `$replaceOne`     | Yes           |
| `$rtrim`          | Yes           |
| `$split`          | Yes           |
| `$strcasecmp`     | Yes           |
| `$strLenBytes`    | Yes           |
| `$strLenCP`       | Yes           |
| `$substr`         | Yes           |
| `$substrBytes`    | Yes           |
| `$substrCP`       | Yes           |
| `$toLower`        | Yes           |
| `$toString`       | Yes           |
| `$toUpper`        | Yes           |
| `$trim`           | Yes           |

### System variables

|  **Variable**   | **Supported** |
|-----------------|---------------|
| `$$CLUSTERTIME` | No            |
| `$$CURRENT`     | No            |
| `$$DESCEND`     | No            |
| `$$KEEP`        | No            |
| `$$NOW`         | Yes           |
| `$$PRUNE`       | No            |
| `$$REMOVE`      | Yes           |
| `$$ROOT`        | Yes           |

### Text operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$meta`      | No            |

### Trigonometry operators

<br />

|    **Operator**     | **Supported** |
|---------------------|---------------|
| `$acos`             | No            |
| `$acosh`            | No            |
| `$asin`             | No            |
| `$asinh`            | No            |
| `$atan`             | No            |
| `$atan2`            | No            |
| `$atanh`            | No            |
| `$cos`              | No            |
| `$cosh`             | No            |
| `$degreesToRadians` | No            |
| `$radiansToDegrees` | No            |
| `$sin`              | No            |
| `$sinh`             | No            |
| `$tan`              | No            |
| `$tanh`             | No            |

### Type operators

| **Operator**  | **Supported** |
|---------------|---------------|
| `$convert`    | Yes           |
| `$isNumber`   | Yes           |
| `$toBool`     | Yes           |
| `$toDate`     | Yes           |
| `$toDecimal`  | Yes           |
| `$toDouble`   | Yes           |
| `$toInt`      | Yes           |
| `$toLong`     | Yes           |
| `$toObjectId` | Yes           |
| `$toString`   | Yes           |
| `$type`       | Yes           |

### Variable operators

| **Operator** | **Supported** |
|--------------|---------------|
| `$let`       | Yes           |

## Geospatial

Cloud Firestore with MongoDB compatibility supports the following Geospatial operators.

### Geometry specifiers

|  **Specifier**  | **Supported** |
|-----------------|---------------|
| `$box`          | No            |
| `$center`       | No            |
| `$centerSphere` | No            |
| `$geometry`     | No            |
| `$maxDistance`  | No            |
| `$minDistance`  | No            |
| `$polygon`      | No            |
| `$uniqueDocs`   | No            |

### Query selectors

|   **Selector**   | **Supported** |
|------------------|---------------|
| `$geoIntersects` | No            |
| `$geoWithin`     | No            |
| `$near`          | No            |
| `$nearSphere`    | No            |
| `$nearSphere`    | No            |
| `$uniqueDocs`    | No            |

## Indexes and index properties

Cloud Firestore with MongoDB compatibility supports the following indexes and index operators.

### Indexes

| **Index type** | **Supported** |
|----------------|---------------|
| 2d             | No            |
| 2dsphere       | No            |
| Compound       | Yes           |
| Hashed         | No            |
| Multikey       | Yes           |
| Single Field   | Yes           |
| Text           | No            |

### Index properties

|   **Property**   | **Supported** |
|------------------|---------------|
| Background       | Yes           |
| Case Insensitive | No            |
| Hidden           | No            |
| Partial          | No            |
| Non-Sparse       | Yes           |
| Sparse           | Yes           |
| Text             | No            |
| TTL              | No            |
| Unique           | Yes           |
| Wildcard         | No            |
| Vector           | No            |

## Database commands

Cloud Firestore with MongoDB compatibility supports the following database commands.

### Aggregation

| **Command** |                                   **Supported**                                   |
|-------------|-----------------------------------------------------------------------------------|
| `aggregate` | Yes                                                                               |
| `count`     | Yes                                                                               |
| `distinct`  | Yes                                                                               |
| `group`     | No The`$group`stage in aggregations is supported whereas the group command isn't. |
| `mapReduce` | No                                                                                |

### Authentication

|  **Command**   | **Supported** |
|----------------|---------------|
| `authenticate` | No            |
| `getnonce`     | No            |
| `logout`       | No            |

### Query and write operations

|       **Command**        |                             **Supported**                             |
|--------------------------|-----------------------------------------------------------------------|
| `watch`(Change Streams)  | No                                                                    |
| `delete`                 | Yes                                                                   |
| `eval`                   | No                                                                    |
| `find`                   | Yes                                                                   |
| `findAndModify`          | Yes                                                                   |
| `getLastError`           | Yes                                                                   |
| `getMore`                | Yes                                                                   |
| `getPrevError`           | No                                                                    |
| `GridFS`                 | No                                                                    |
| `insert`                 | Yes                                                                   |
| `parallelCollectionScan` | No                                                                    |
| `replaceOne`             | No The`replaceOne`driver method is supported with the`update`command. |
| `resetError`             | No                                                                    |
| `update`                 | Yes                                                                   |

### Session commands

|        **Command**         |                         **Supported**                         |
|----------------------------|---------------------------------------------------------------|
| `abortTransaction`         | Yes                                                           |
| `commitTransaction`        | Yes                                                           |
| `endSessions`              | Yes                                                           |
| `killAllSessions`          | No                                                            |
| `killAllSessionsByPattern` | No                                                            |
| `killSessions`             | No                                                            |
| `refreshSessions`          | No                                                            |
| `startSession`             | Sessions can be started using the`startSession`driver method. |

## Administrative commands

Cloud Firestore with MongoDB compatibility supports the following administrative commands.

|          **Command**          |                                                              **Supported**                                                               |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `cloneCollectionAsCapped`     | No                                                                                                                                       |
| `collMod`                     | No                                                                                                                                       |
| `collMod: expireAfterSeconds` | No                                                                                                                                       |
| `convertToCapped`             | No                                                                                                                                       |
| `copydb`                      | No                                                                                                                                       |
| `create`                      | Yes                                                                                                                                      |
| `createIndex`                 | Yes To create indexes, see[Manage indexes](https://firebase.google.com/docs/firestore/enterprise/indexing).                              |
| `createIndexes`               | Yes To create indexes, see[Manage indexes](https://firebase.google.com/docs/firestore/enterprise/indexing).                              |
| `createView`                  | No                                                                                                                                       |
| `currentOp`                   | No                                                                                                                                       |
| `drop`                        | No                                                                                                                                       |
| `dropDatabase`                | No To delete a database, see[Delete a database](https://firebase.google.com/docs/firestore/enterprise/create-databases#delete-database). |
| `dropIndex`                   | Yes To delete indexes, see[Manage indexes](https://firebase.google.com/docs/firestore/enterprise/indexing).                              |
| `dropIndexes`                 | No                                                                                                                                       |
| `filemd5`                     | No                                                                                                                                       |
| `getAuditConfig`              | No                                                                                                                                       |
| `killCursors`                 | Yes                                                                                                                                      |
| `killOp`                      | No                                                                                                                                       |
| `listCollections`             | Yes                                                                                                                                      |
| `listDatabases`               | Yes                                                                                                                                      |
| `listIndexes`                 | Yes                                                                                                                                      |
| `reIndex`                     | No                                                                                                                                       |
| `renameCollection`            | No                                                                                                                                       |
| `setAuditConfig`              | No                                                                                                                                       |

### Diagnostic commands

|    **Command**     |                                                                     **Supported**                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `buildInfo`        | Yes                                                                                                                                                   |
| `collStats`        | No                                                                                                                                                    |
| `connectionStatus` | Yes                                                                                                                                                   |
| `connPoolStats`    | No                                                                                                                                                    |
| `dataSize`         | No                                                                                                                                                    |
| `dbHash`           | No                                                                                                                                                    |
| `dbStats`          | No                                                                                                                                                    |
| `explain`          | Yes For behavior differences and limitations, see[Query Explain](https://firebase.google.com/docs/firestore/enterprise/query-explain#explain-command) |
| `features`         | No                                                                                                                                                    |
| `hello`            | Yes                                                                                                                                                   |
| `hostInfo`         | Yes                                                                                                                                                   |
| `listCommands`     | No                                                                                                                                                    |
| `profiler`         | No                                                                                                                                                    |
| `serverStatus`     | No                                                                                                                                                    |
| `top`              | No                                                                                                                                                    |
| `whatsmyuri`       | No                                                                                                                                                    |

### Role management commands

To manage database access, Cloud Firestore with MongoDB compatibility supports[Identity and Access Management roles and permissions](https://firebase.google.com/docs/firestore/enterprise/security/iam).

|        **Command**         | **Supported** |
|----------------------------|---------------|
| `createRole`               | No            |
| `dropAllRolesFromDatabase` | No            |
| `dropRole`                 | No            |
| `grantRolesToRole`         | No            |
| `revokePrivilegesFromRole` | No            |
| `revokeRolesFromRole`      | No            |
| `rolesInfo`                | No            |
| `updateRole`               | No            |

## What's next

- Run the[Quickstart: Create a database and connect to it](https://firebase.google.com/docs/firestore/enterprise/create-and-query-database).
- Learn about[Behavior differences](https://firebase.google.com/docs/firestore/enterprise/behavior-differences).