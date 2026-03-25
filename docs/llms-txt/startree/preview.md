# Source: https://docs.startree.ai/api-reference/table/preview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# preview

> Simulates a preview of the table given the table config and schema

## OpenAPI

````yaml post /tables/preview
openapi: 3.0.1
info:
  title: Pinot Controller API
  description: APIs for accessing Pinot Controller information
  contact:
    name: https://github.com/apache/pinot
  version: '1.0'
servers:
  - url: https://dev.startree.ai/
security: []
tags:
  - name: AtomicIngestion
  - name: BatchRestart
  - name: ClusterHealth
  - name: Connection
  - name: ConsistentPush
  - name: DedupSnapshot
  - name: PerfAdvisor
  - name: RateLimiter
  - name: Table
  - name: Restream
  - name: Tuner
  - name: AlterTable
  - name: UpsertSnapshot
  - name: Cluster
  - name: User
  - name: Application
  - name: Broker
  - name: AppConfigs
  - name: Auth
  - name: Health
  - name: Logger
  - name: PeriodicTask
  - name: Database
  - name: Instance
  - name: Leader
  - name: Query
  - name: Schema
  - name: Segment
  - name: Tenant
  - name: Task
  - name: Upsert
  - name: Version
  - name: Zookeeper
paths:
  /tables/preview:
    post:
      tags:
        - Table
      summary: preview
      description: Simulates a preview of the table given the table config and schema
      operationId: preview
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TablePreviewApi'
        required: false
      responses:
        '200':
          description: Successful retrieval of table sizes
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TablePreviewApi'
        '500':
          description: Internal server error
          content: {}
      security:
        - oauth: []
components:
  schemas:
    TablePreviewApi:
      type: object
      properties:
        tableConfig:
          $ref: '#/components/schemas/TableConfig'
        schema:
          $ref: '#/components/schemas/Schema'
        tableConfigs:
          $ref: '#/components/schemas/TableConfigs'
        sourceRows:
          type: array
          items:
            $ref: '#/components/schemas/GenericRow'
        rows:
          type: array
          items:
            $ref: '#/components/schemas/GenericRow'
        sourceFiles:
          type: array
          items:
            type: string
        config:
          $ref: '#/components/schemas/TablePreviewConfigApi'
        summary:
          $ref: '#/components/schemas/TablePreviewSummaryApi'
    TableConfig:
      type: object
      properties:
        tableName:
          type: string
        tableType:
          type: string
          readOnly: true
          enum:
            - OFFLINE
            - REALTIME
        segmentsConfig:
          $ref: '#/components/schemas/SegmentsValidationAndRetentionConfig'
        tenants:
          $ref: '#/components/schemas/TenantConfig'
        tableIndexConfig:
          $ref: '#/components/schemas/IndexingConfig'
        metadata:
          $ref: '#/components/schemas/TableCustomConfig'
        quota:
          $ref: '#/components/schemas/QuotaConfig'
        task:
          $ref: '#/components/schemas/TableTaskConfig'
        routing:
          $ref: '#/components/schemas/RoutingConfig'
        query:
          $ref: '#/components/schemas/QueryConfig'
        instanceAssignmentConfigMap:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/InstanceAssignmentConfig'
        fieldConfigList:
          type: array
          items:
            $ref: '#/components/schemas/FieldConfig'
        upsertConfig:
          $ref: '#/components/schemas/UpsertConfig'
        dedupConfig:
          $ref: '#/components/schemas/DedupConfig'
        dimensionTableConfig:
          $ref: '#/components/schemas/DimensionTableConfig'
        ingestionConfig:
          $ref: '#/components/schemas/IngestionConfig'
        tierConfigs:
          type: array
          items:
            $ref: '#/components/schemas/TierConfig'
        isDimTable:
          type: boolean
          readOnly: true
        tunerConfigs:
          type: array
          items:
            $ref: '#/components/schemas/TunerConfig'
        instancePartitionsMap:
          type: object
          additionalProperties:
            type: string
        segmentAssignmentConfigMap:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/SegmentAssignmentConfig'
    Schema:
      type: object
      properties:
        dimensionFieldSpecs:
          type: array
          items:
            $ref: '#/components/schemas/DimensionFieldSpec'
        primaryKeyColumns:
          type: array
          items:
            type: string
        metricFieldSpecs:
          type: array
          items:
            $ref: '#/components/schemas/MetricFieldSpec'
        dateTimeFieldSpecs:
          type: array
          items:
            $ref: '#/components/schemas/DateTimeFieldSpec'
        timeFieldSpec:
          $ref: '#/components/schemas/TimeFieldSpec'
        complexFieldSpecs:
          type: array
          items:
            $ref: '#/components/schemas/ComplexFieldSpec'
        enableColumnBasedNullHandling:
          type: boolean
        schemaName:
          type: string
    TableConfigs:
      required:
        - schema
        - tableName
      type: object
      properties:
        tableName:
          type: string
        schema:
          $ref: '#/components/schemas/Schema'
        offline:
          $ref: '#/components/schemas/TableConfig'
        realtime:
          $ref: '#/components/schemas/TableConfig'
    GenericRow:
      type: object
      properties:
        nullValueFields:
          uniqueItems: true
          type: array
          items:
            type: string
        fieldToValueMap:
          type: object
          additionalProperties:
            type: object
            properties: {}
    TablePreviewConfigApi:
      type: object
      properties:
        sampling:
          $ref: '#/components/schemas/PreviewSamplerConfigApi'
        inference:
          $ref: '#/components/schemas/InferenceConfigApi'
        previewFiles:
          $ref: '#/components/schemas/PreviewFilesConfigApi'
    TablePreviewSummaryApi:
      type: object
      properties:
        getnSourceRows:
          type: integer
          format: int32
        getnSourceColumns:
          type: integer
          format: int32
        getnRows:
          type: integer
          format: int32
        getnColumns:
          type: integer
          format: int32
        batch:
          $ref: '#/components/schemas/BatchSummaryApi'
        realtime:
          $ref: '#/components/schemas/RealtimeSummaryApi'
    SegmentsValidationAndRetentionConfig:
      type: object
      properties:
        timeType:
          type: string
          enum:
            - NANOSECONDS
            - MICROSECONDS
            - MILLISECONDS
            - SECONDS
            - MINUTES
            - HOURS
            - DAYS
        segmentPushFrequency:
          type: string
        segmentAssignmentStrategy:
          type: string
        replicasPerPartition:
          type: string
        replicaGroupStrategyConfig:
          $ref: '#/components/schemas/ReplicaGroupStrategyConfig'
        peerSegmentDownloadScheme:
          type: string
        minimizeDataMovement:
          type: boolean
        segmentPushType:
          type: string
        timeColumnName:
          type: string
        retentionTimeUnit:
          type: string
        retentionTimeValue:
          type: string
        completionConfig:
          $ref: '#/components/schemas/CompletionConfig'
        crypterClassName:
          type: string
        deletedSegmentsRetentionPeriod:
          type: string
        replication:
          type: string
        schemaName:
          type: string
    TenantConfig:
      type: object
      properties:
        broker:
          type: string
          readOnly: true
        server:
          type: string
          readOnly: true
        tagOverrideConfig:
          $ref: '#/components/schemas/TagOverrideConfig'
    IndexingConfig:
      type: object
      properties:
        autoGeneratedInvertedIndex:
          type: boolean
        segmentFormatVersion:
          type: string
        enableDefaultStarTree:
          type: boolean
        starTreeIndexConfigs:
          type: array
          items:
            $ref: '#/components/schemas/StarTreeIndexConfig'
        segmentPartitionConfig:
          $ref: '#/components/schemas/SegmentPartitionConfig'
        nullHandlingEnabled:
          type: boolean
        skipSegmentPreprocess:
          type: boolean
        optimizeDictionaryType:
          type: boolean
        streamConfigs:
          type: object
          additionalProperties:
            type: string
        fstindexType:
          type: string
          enum:
            - LUCENE
            - NATIVE
        rangeIndexVersion:
          type: integer
          format: int32
        jsonIndexColumns:
          type: array
          items:
            type: string
        jsonIndexConfigs:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/JsonIndexConfig'
        mapIndexColumns:
          type: array
          items:
            type: string
        mapIndexConfigs:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/MapIndexConfig'
        bloomFilterConfigs:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/BloomFilterConfig'
        noDictionaryConfig:
          type: object
          additionalProperties:
            type: string
        tierOverwrites:
          $ref: '#/components/schemas/JsonNode'
        aggregateMetrics:
          type: boolean
        optimizeDictionary:
          type: boolean
        columnMinMaxValueGeneratorMode:
          type: string
        enableDynamicStarTreeCreation:
          type: boolean
        columnMajorSegmentBuilderEnabled:
          type: boolean
        optimizeDictionaryForMetrics:
          type: boolean
        noDictionarySizeRatioThreshold:
          type: number
          format: double
        loadMode:
          type: string
        invertedIndexColumns:
          type: array
          items:
            type: string
        noDictionaryColumns:
          type: array
          items:
            type: string
        createInvertedIndexDuringSegmentGeneration:
          type: boolean
        noDictionaryCardinalityRatioThreshold:
          type: number
          format: double
        onHeapDictionaryColumns:
          type: array
          items:
            type: string
        varLengthDictionaryColumns:
          type: array
          items:
            type: string
        bloomFilterColumns:
          type: array
          items:
            type: string
        rangeIndexColumns:
          type: array
          items:
            type: string
        sortedColumn:
          type: array
          items:
            type: string
        segmentNameGeneratorType:
          type: string
    TableCustomConfig:
      type: object
      properties:
        customConfigs:
          type: object
          additionalProperties:
            type: string
          readOnly: true
    QuotaConfig:
      type: object
      properties:
        storage:
          type: string
          readOnly: true
        maxQueriesPerSecond:
          type: string
          readOnly: true
    TableTaskConfig:
      type: object
      properties:
        taskTypeConfigsMap:
          type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: string
          readOnly: true
    RoutingConfig:
      type: object
      properties:
        routingTableBuilderName:
          type: string
          readOnly: true
        segmentPrunerTypes:
          type: array
          readOnly: true
          items:
            type: string
        instanceSelectorType:
          type: string
          readOnly: true
        useFixedReplica:
          type: boolean
          readOnly: true
    QueryConfig:
      type: object
      properties:
        timeoutMs:
          type: integer
          format: int64
          readOnly: true
        disableGroovy:
          type: boolean
          readOnly: true
        useApproximateFunction:
          type: boolean
          readOnly: true
        expressionOverrideMap:
          type: object
          additionalProperties:
            type: string
          readOnly: true
        maxQueryResponseSizeBytes:
          type: integer
          format: int64
          readOnly: true
        maxServerResponseSizeBytes:
          type: integer
          format: int64
          readOnly: true
    InstanceAssignmentConfig:
      required:
        - replicaGroupPartitionConfig
        - tagPoolConfig
      type: object
      properties:
        tagPoolConfig:
          $ref: '#/components/schemas/InstanceTagPoolConfig'
        constraintConfig:
          $ref: '#/components/schemas/InstanceConstraintConfig'
        replicaGroupPartitionConfig:
          $ref: '#/components/schemas/InstanceReplicaGroupPartitionConfig'
        partitionSelector:
          type: string
          readOnly: true
          enum:
            - FD_AWARE_INSTANCE_PARTITION_SELECTOR
            - INSTANCE_REPLICA_GROUP_PARTITION_SELECTOR
            - MIRROR_SERVER_SET_PARTITION_SELECTOR
        minimizeDataMovement:
          type: boolean
          readOnly: true
    FieldConfig:
      required:
        - name
      type: object
      properties:
        name:
          type: string
          readOnly: true
        encodingType:
          type: string
          readOnly: true
          enum:
            - RAW
            - DICTIONARY
        indexType:
          type: string
          readOnly: true
          enum:
            - INVERTED
            - SORTED
            - TEXT
            - FST
            - H3
            - JSON
            - TIMESTAMP
            - VECTOR
            - RANGE
        indexTypes:
          type: array
          readOnly: true
          items:
            type: string
            enum:
              - INVERTED
              - SORTED
              - TEXT
              - FST
              - H3
              - JSON
              - TIMESTAMP
              - VECTOR
              - RANGE
        compressionCodec:
          type: string
          readOnly: true
          enum:
            - PASS_THROUGH
            - SNAPPY
            - ZSTANDARD
            - LZ4
            - GZIP
            - MV_ENTRY_DICT
            - CLP
            - CLPV2
            - CLPV2_ZSTD
            - CLPV2_LZ4
        timestampConfig:
          $ref: '#/components/schemas/TimestampConfig'
        indexes:
          $ref: '#/components/schemas/JsonNode'
        properties:
          type: object
          additionalProperties:
            type: string
          readOnly: true
        tierOverwrites:
          $ref: '#/components/schemas/JsonNode'
    UpsertConfig:
      type: object
      properties:
        defaultPartialUpsertStrategy:
          type: string
          enum:
            - APPEND
            - IGNORE
            - INCREMENT
            - MAX
            - MIN
            - OVERWRITE
            - UNION
        upsertViewRefreshIntervalMs:
          type: integer
          format: int64
        consistencyMode:
          type: string
          enum:
            - NONE
            - SYNC
            - SNAPSHOT
        comparisonColumns:
          type: array
          items:
            type: string
        metadataTTL:
          type: number
          format: double
        deleteRecordColumn:
          type: string
        outOfOrderRecordColumn:
          type: string
        dropOutOfOrderRecord:
          type: boolean
        hashFunction:
          type: string
          enum:
            - NONE
            - MD5
            - MURMUR3
            - UUID
        enableSnapshot:
          type: boolean
        deletedKeysTTL:
          type: number
          format: double
        enablePreload:
          type: boolean
        metadataManagerConfigs:
          type: object
          additionalProperties:
            type: string
        partialUpsertStrategies:
          type: object
          additionalProperties:
            type: string
            enum:
              - APPEND
              - IGNORE
              - INCREMENT
              - MAX
              - MIN
              - OVERWRITE
              - UNION
        partialUpsertMergerClass:
          type: string
        newSegmentTrackingTimeMs:
          type: integer
          format: int64
        metadataManagerClass:
          type: string
        enableDeletedKeysCompactionConsistency:
          type: boolean
        allowPartialUpsertConsumptionDuringCommit:
          type: boolean
        mode:
          type: string
          enum:
            - FULL
            - PARTIAL
            - NONE
    DedupConfig:
      required:
        - dedupEnabled
      type: object
      properties:
        dedupEnabled:
          type: boolean
          readOnly: true
        hashFunction:
          type: string
          readOnly: true
          enum:
            - NONE
            - MD5
            - MURMUR3
            - UUID
        metadataManagerClass:
          type: string
          readOnly: true
        metadataManagerConfigs:
          type: object
          additionalProperties:
            type: string
          readOnly: true
        metadataTTL:
          type: number
          format: double
          readOnly: true
        dedupTimeColumn:
          type: string
          readOnly: true
        enablePreload:
          type: boolean
    DimensionTableConfig:
      type: object
      properties:
        disablePreload:
          type: boolean
          readOnly: true
        errorOnDuplicatePrimaryKey:
          type: boolean
          readOnly: true
    IngestionConfig:
      type: object
      properties:
        batchIngestionConfig:
          $ref: '#/components/schemas/BatchIngestionConfig'
        streamIngestionConfig:
          $ref: '#/components/schemas/StreamIngestionConfig'
        schemaConformingTransformerConfig:
          $ref: '#/components/schemas/SchemaConformingTransformerConfig'
        segmentTimeValueCheck:
          type: boolean
        continueOnError:
          type: boolean
        rowTimeValueCheck:
          type: boolean
        filterConfig:
          $ref: '#/components/schemas/FilterConfig'
        enrichmentConfigs:
          type: array
          items:
            $ref: '#/components/schemas/EnrichmentConfig'
        transformConfigs:
          type: array
          items:
            $ref: '#/components/schemas/TransformConfig'
        complexTypeConfig:
          $ref: '#/components/schemas/ComplexTypeConfig'
        aggregationConfigs:
          type: array
          items:
            $ref: '#/components/schemas/AggregationConfig'
    TierConfig:
      required:
        - name
        - segmentSelectorType
        - storageType
      type: object
      properties:
        name:
          type: string
          readOnly: true
        segmentSelectorType:
          type: string
          readOnly: true
        segmentAge:
          type: string
          readOnly: true
        segmentList:
          type: array
          readOnly: true
          items:
            type: string
        storageType:
          type: string
          readOnly: true
        serverTag:
          type: string
          readOnly: true
        tierBackend:
          type: string
          readOnly: true
        tierBackendProperties:
          type: object
          additionalProperties:
            type: string
          readOnly: true
    TunerConfig:
      required:
        - name
      type: object
      properties:
        name:
          type: string
        tunerProperties:
          type: object
          additionalProperties:
            type: string
    SegmentAssignmentConfig:
      type: object
      properties:
        segmentAssignmentStrategy:
          type: string
          description: Configuration for Segment Assignment Strategy
        assignmentStrategy:
          type: string
    DimensionFieldSpec:
      allOf:
        - $ref: '#/components/schemas/FieldSpec'
        - type: object
    MetricFieldSpec:
      allOf:
        - $ref: '#/components/schemas/FieldSpec'
        - type: object
    DateTimeFieldSpec:
      allOf:
        - $ref: '#/components/schemas/FieldSpec'
        - type: object
          properties:
            granularity:
              type: string
            sampleValue:
              type: object
              properties: {}
            format:
              type: string
    TimeFieldSpec:
      allOf:
        - $ref: '#/components/schemas/FieldSpec'
        - type: object
          properties:
            incomingGranularitySpec:
              $ref: '#/components/schemas/TimeGranularitySpec'
            outgoingGranularitySpec:
              $ref: '#/components/schemas/TimeGranularitySpec'
    ComplexFieldSpec:
      type: object
      properties:
        childFieldSpecs:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/FieldSpec'
        notNull:
          type: boolean
        maxLengthExceedStrategy:
          type: string
          enum:
            - TRIM_LENGTH
            - ERROR
            - SUBSTITUTE_DEFAULT_VALUE
            - NO_ACTION
        defaultNullValueString:
          type: string
        virtualColumnProvider:
          type: string
        transformFunction:
          type: string
        defaultNullValue:
          type: object
          properties: {}
        singleValueField:
          type: boolean
        allowTrailingZeros:
          type: boolean
        maxLength:
          type: integer
          format: int32
        dataType:
          type: string
          enum:
            - INT
            - LONG
            - FLOAT
            - DOUBLE
            - BIG_DECIMAL
            - BOOLEAN
            - TIMESTAMP
            - STRING
            - JSON
            - BYTES
            - STRUCT
            - MAP
            - LIST
            - UNKNOWN
        name:
          type: string
    PreviewSamplerConfigApi:
      type: object
      properties:
        min:
          type: integer
          format: int32
        max:
          type: integer
          format: int32
    InferenceConfigApi:
      type: object
      properties:
        schemaInferenceEnabled:
          type: boolean
    PreviewFilesConfigApi:
      type: object
      properties:
        previewFilesOnly:
          type: boolean
        nfilesToFetch:
          type: integer
          format: int32
    BatchSummaryApi:
      type: object
      properties:
        getnMatchingFiles:
          type: integer
          format: int32
    RealtimeSummaryApi:
      type: object
      properties:
        getnPartitions:
          type: integer
          format: int32
        getnRunnables:
          type: integer
          format: int32
        getnRunnablesWithException:
          type: integer
          format: int32
        partitionMetadataFetchTimeMs:
          type: integer
          format: int64
    ReplicaGroupStrategyConfig:
      required:
        - numInstancesPerPartition
      type: object
      properties:
        partitionColumn:
          type: string
          readOnly: true
        numInstancesPerPartition:
          type: integer
          format: int32
          readOnly: true
    CompletionConfig:
      required:
        - completionMode
      type: object
      properties:
        completionMode:
          type: string
          readOnly: true
    TagOverrideConfig:
      type: object
      properties:
        realtimeConsuming:
          type: string
          readOnly: true
        realtimeCompleted:
          type: string
          readOnly: true
    StarTreeIndexConfig:
      required:
        - dimensionsSplitOrder
      type: object
      properties:
        dimensionsSplitOrder:
          type: array
          readOnly: true
          items:
            type: string
        skipStarNodeCreationForDimensions:
          type: array
          readOnly: true
          items:
            type: string
        functionColumnPairs:
          type: array
          readOnly: true
          items:
            type: string
        aggregationConfigs:
          type: array
          readOnly: true
          items:
            $ref: '#/components/schemas/StarTreeAggregationConfig'
        maxLeafRecords:
          type: integer
          format: int32
          readOnly: true
    SegmentPartitionConfig:
      required:
        - columnPartitionMap
      type: object
      properties:
        columnPartitionMap:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ColumnPartitionConfig'
          readOnly: true
    JsonIndexConfig:
      type: object
      properties:
        disabled:
          type: boolean
          readOnly: true
        maxLevels:
          type: integer
          format: int32
        excludeArray:
          type: boolean
        disableCrossArrayUnnest:
          type: boolean
        includePaths:
          uniqueItems: true
          type: array
          items:
            type: string
        excludePaths:
          uniqueItems: true
          type: array
          items:
            type: string
        excludeFields:
          uniqueItems: true
          type: array
          items:
            type: string
        indexPaths:
          uniqueItems: true
          type: array
          items:
            type: string
        maxValueLength:
          type: integer
          format: int32
        skipInvalidJson:
          type: boolean
    MapIndexConfig:
      type: object
      properties:
        disabled:
          type: boolean
          readOnly: true
        configs:
          type: object
          additionalProperties:
            type: object
            properties: {}
          readOnly: true
    BloomFilterConfig:
      type: object
      properties:
        disabled:
          type: boolean
          readOnly: true
        fpp:
          type: number
          format: double
          readOnly: true
        maxSizeInBytes:
          type: integer
          format: int32
          readOnly: true
        loadOnHeap:
          type: boolean
          readOnly: true
    JsonNode:
      type: object
    InstanceTagPoolConfig:
      required:
        - tag
      type: object
      properties:
        tag:
          type: string
          readOnly: true
        poolBased:
          type: boolean
          readOnly: true
        numPools:
          type: integer
          format: int32
          readOnly: true
        pools:
          type: array
          readOnly: true
          items:
            type: integer
            format: int32
    InstanceConstraintConfig:
      required:
        - constraints
      type: object
      properties:
        constraints:
          type: array
          readOnly: true
          items:
            type: string
    InstanceReplicaGroupPartitionConfig:
      type: object
      properties:
        replicaGroupBased:
          type: boolean
          readOnly: true
        numInstances:
          type: integer
          format: int32
          readOnly: true
        numReplicaGroups:
          type: integer
          format: int32
          readOnly: true
        numInstancesPerReplicaGroup:
          type: integer
          format: int32
          readOnly: true
        numPartitions:
          type: integer
          format: int32
          readOnly: true
        numInstancesPerPartition:
          type: integer
          format: int32
          readOnly: true
        minimizeDataMovement:
          type: boolean
          readOnly: true
        partitionColumn:
          type: string
          readOnly: true
    TimestampConfig:
      type: object
      properties:
        granularities:
          type: array
          readOnly: true
          items:
            type: string
            enum:
              - MILLISECOND
              - SECOND
              - MINUTE
              - HOUR
              - DAY
              - WEEK
              - MONTH
              - QUARTER
              - YEAR
    BatchIngestionConfig:
      type: object
      properties:
        batchConfigMaps:
          type: array
          items:
            type: object
            additionalProperties:
              type: string
        segmentIngestionType:
          type: string
        segmentIngestionFrequency:
          type: string
        consistentDataPush:
          type: boolean
    StreamIngestionConfig:
      type: object
      properties:
        streamConfigMaps:
          type: array
          readOnly: true
          items:
            type: object
            additionalProperties:
              type: string
        columnMajorSegmentBuilderEnabled:
          type: boolean
        trackFilteredMessageOffsets:
          type: boolean
        pauselessConsumptionEnabled:
          type: boolean
    SchemaConformingTransformerConfig:
      type: object
      properties:
        enableIndexableExtras:
          type: boolean
        indexableExtrasField:
          type: string
        enableUnindexableExtras:
          type: boolean
        unindexableExtrasField:
          type: string
        unindexableFieldSuffix:
          type: string
        fieldPathsToDrop:
          uniqueItems: true
          type: array
          items:
            type: string
        fieldPathsToSkipStorage:
          uniqueItems: true
          type: array
          items:
            type: string
        columnNameToJsonKeyPathMap:
          type: object
          additionalProperties:
            type: string
        mergedTextIndexField:
          type: string
        useAnonymousDotInFieldNames:
          type: boolean
        optimizeCaseInsensitiveSearch:
          type: boolean
        reverseTextIndexKeyValueOrder:
          type: boolean
        mergedTextIndexDocumentMaxLength:
          type: integer
          format: int32
        mergedTextIndexBinaryDocumentDetectionMinLength:
          type: integer
          format: int32
        mergedTextIndexPathToExclude:
          uniqueItems: true
          type: array
          items:
            type: string
        fieldsToDoubleIngest:
          uniqueItems: true
          type: array
          items:
            type: string
        jsonKeyValueSeparator:
          type: string
        mergedTextIndexBeginOfDocAnchor:
          type: string
        mergedTextIndexEndOfDocAnchor:
          type: string
        fieldPathsToPreserveInputWithIndex:
          uniqueItems: true
          type: array
          items:
            type: string
        fieldPathsToPreserveInput:
          uniqueItems: true
          type: array
          items:
            type: string
    FilterConfig:
      type: object
      properties:
        filterFunction:
          type: string
          readOnly: true
    EnrichmentConfig:
      type: object
      properties:
        enricherType:
          type: string
          readOnly: true
        properties:
          $ref: '#/components/schemas/JsonNode'
    TransformConfig:
      type: object
      properties:
        columnName:
          type: string
          readOnly: true
        transformFunction:
          type: string
          readOnly: true
    ComplexTypeConfig:
      type: object
      properties:
        fieldsToUnnest:
          type: array
          readOnly: true
          items:
            type: string
        delimiter:
          type: string
          readOnly: true
        collectionNotUnnestedToJson:
          type: string
          readOnly: true
          enum:
            - NONE
            - NON_PRIMITIVE
            - ALL
        prefixesToRename:
          type: object
          additionalProperties:
            type: string
          readOnly: true
    AggregationConfig:
      type: object
      properties:
        columnName:
          type: string
          readOnly: true
        aggregationFunction:
          type: string
          readOnly: true
    FieldSpec:
      type: object
      properties:
        notNull:
          type: boolean
        maxLengthExceedStrategy:
          type: string
          enum:
            - TRIM_LENGTH
            - ERROR
            - SUBSTITUTE_DEFAULT_VALUE
            - NO_ACTION
        defaultNullValueString:
          type: string
        virtualColumnProvider:
          type: string
        transformFunction:
          type: string
        defaultNullValue:
          type: object
          properties: {}
        singleValueField:
          type: boolean
        allowTrailingZeros:
          type: boolean
        maxLength:
          type: integer
          format: int32
        dataType:
          type: string
          enum:
            - INT
            - LONG
            - FLOAT
            - DOUBLE
            - BIG_DECIMAL
            - BOOLEAN
            - TIMESTAMP
            - STRING
            - JSON
            - BYTES
            - STRUCT
            - MAP
            - LIST
            - UNKNOWN
        name:
          type: string
        fieldType:
          type: string
          enum:
            - DIMENSION
            - METRIC
            - TIME
            - DATE_TIME
            - COMPLEX
      discriminator:
        propertyName: fieldType
    TimeGranularitySpec:
      type: object
      properties:
        timeType:
          type: string
          enum:
            - NANOSECONDS
            - MICROSECONDS
            - MILLISECONDS
            - SECONDS
            - MINUTES
            - HOURS
            - DAYS
        timeFormat:
          type: string
        timeUnitSize:
          type: integer
          format: int32
        dataType:
          type: string
          enum:
            - INT
            - LONG
            - FLOAT
            - DOUBLE
            - BIG_DECIMAL
            - BOOLEAN
            - TIMESTAMP
            - STRING
            - JSON
            - BYTES
            - STRUCT
            - MAP
            - LIST
            - UNKNOWN
        name:
          type: string
    StarTreeAggregationConfig:
      required:
        - aggregationFunction
        - columnName
      type: object
      properties:
        columnName:
          type: string
          readOnly: true
        aggregationFunction:
          type: string
          readOnly: true
        functionParameters:
          type: object
          additionalProperties:
            type: object
            properties: {}
          readOnly: true
        compressionCodec:
          type: string
          readOnly: true
          enum:
            - PASS_THROUGH
            - SNAPPY
            - ZSTANDARD
            - LZ4
            - GZIP
            - MV_ENTRY_DICT
            - CLP
            - CLPV2
            - CLPV2_ZSTD
            - CLPV2_LZ4
        deriveNumDocsPerChunk:
          type: boolean
          readOnly: true
        indexVersion:
          type: integer
          format: int32
          readOnly: true
        targetMaxChunkSize:
          type: string
          readOnly: true
        targetDocsPerChunk:
          type: integer
          format: int32
          readOnly: true
    ColumnPartitionConfig:
      required:
        - functionName
        - numPartitions
      type: object
      properties:
        functionName:
          type: string
          readOnly: true
        numPartitions:
          type: integer
          format: int32
          readOnly: true
        functionConfig:
          type: object
          additionalProperties:
            type: string
          readOnly: true
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
