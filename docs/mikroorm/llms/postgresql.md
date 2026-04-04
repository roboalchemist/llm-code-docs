# Source: https://mikro-orm.io/api/postgresql.md

# @mikro-orm/postgresql<!-- -->

## Index[**](#index)

### References

* [**AbstractNamingStrategy](https://mikro-orm.io/api/postgresql.md#AbstractNamingStrategy)
* [**AbstractSqlConnection](https://mikro-orm.io/api/postgresql.md#AbstractSqlConnection)
* [**AbstractSqlDriver](https://mikro-orm.io/api/postgresql.md#AbstractSqlDriver)
* [**AbstractSqlPlatform](https://mikro-orm.io/api/postgresql.md#AbstractSqlPlatform)
* [**Alias](https://mikro-orm.io/api/postgresql.md#Alias)
* [**AliasedFilterCondition](https://mikro-orm.io/api/postgresql.md#AliasedFilterCondition)
* [**AnyEntity](https://mikro-orm.io/api/postgresql.md#AnyEntity)
* [**AnyQueryBuilder](https://mikro-orm.io/api/postgresql.md#AnyQueryBuilder)
* [**AnyString](https://mikro-orm.io/api/postgresql.md#AnyString)
* [**ARRAY\_OPERATORS](https://mikro-orm.io/api/postgresql.md#ARRAY_OPERATORS)
* [**ArrayType](https://mikro-orm.io/api/postgresql.md#ArrayType)
* [**assign](https://mikro-orm.io/api/postgresql.md#assign)
* [**AssignOptions](https://mikro-orm.io/api/postgresql.md#AssignOptions)
* [**AutoPath](https://mikro-orm.io/api/postgresql.md#AutoPath)
* [**BaseEntity](https://mikro-orm.io/api/postgresql.md#BaseEntity)
* [**BaseMySqlPlatform](https://mikro-orm.io/api/postgresql.md#BaseMySqlPlatform)
* [**BasePostgreSqlPlatform](https://mikro-orm.io/api/postgresql.md#BasePostgreSqlPlatform)
* [**BaseSqliteConnection](https://mikro-orm.io/api/postgresql.md#BaseSqliteConnection)
* [**BigIntType](https://mikro-orm.io/api/postgresql.md#BigIntType)
* [**BlobType](https://mikro-orm.io/api/postgresql.md#BlobType)
* [**BooleanType](https://mikro-orm.io/api/postgresql.md#BooleanType)
* [**CacheAdapter](https://mikro-orm.io/api/postgresql.md#CacheAdapter)
* [**Cascade](https://mikro-orm.io/api/postgresql.md#Cascade)
* [**Cast](https://mikro-orm.io/api/postgresql.md#Cast)
* [**ClearDatabaseOptions](https://mikro-orm.io/api/postgresql.md#ClearDatabaseOptions)
* [**CollationOptions](https://mikro-orm.io/api/postgresql.md#CollationOptions)
* [**Collection](https://mikro-orm.io/api/postgresql.md#Collection)
* [**Column](https://mikro-orm.io/api/postgresql.md#Column)
* [**ColumnDifference](https://mikro-orm.io/api/postgresql.md#ColumnDifference)
* [**compareArrays](https://mikro-orm.io/api/postgresql.md#compareArrays)
* [**compareBooleans](https://mikro-orm.io/api/postgresql.md#compareBooleans)
* [**compareBuffers](https://mikro-orm.io/api/postgresql.md#compareBuffers)
* [**compareObjects](https://mikro-orm.io/api/postgresql.md#compareObjects)
* [**CompiledFunctions](https://mikro-orm.io/api/postgresql.md#CompiledFunctions)
* [**Config](https://mikro-orm.io/api/postgresql.md#Config)
* [**Configuration](https://mikro-orm.io/api/postgresql.md#Configuration)
* [**Connection](https://mikro-orm.io/api/postgresql.md#Connection)
* [**ConnectionConfig](https://mikro-orm.io/api/postgresql.md#ConnectionConfig)
* [**ConnectionException](https://mikro-orm.io/api/postgresql.md#ConnectionException)
* [**ConnectionOptions](https://mikro-orm.io/api/postgresql.md#ConnectionOptions)
* [**ConnectionType](https://mikro-orm.io/api/postgresql.md#ConnectionType)
* [**ConstraintViolationException](https://mikro-orm.io/api/postgresql.md#ConstraintViolationException)
* [**Constructor](https://mikro-orm.io/api/postgresql.md#Constructor)
* [**ContextOrderByMap](https://mikro-orm.io/api/postgresql.md#ContextOrderByMap)
* [**CountOptions](https://mikro-orm.io/api/postgresql.md#CountOptions)
* [**CountQueryBuilder](https://mikro-orm.io/api/postgresql.md#CountQueryBuilder)
* [**CreateContextOptions](https://mikro-orm.io/api/postgresql.md#CreateContextOptions)
* [**CreateOptions](https://mikro-orm.io/api/postgresql.md#CreateOptions)
* [**CreateSchemaOptions](https://mikro-orm.io/api/postgresql.md#CreateSchemaOptions)
* [**createSqlFunction](https://mikro-orm.io/api/postgresql.md#createSqlFunction)
* [**CteOptions](https://mikro-orm.io/api/postgresql.md#CteOptions)
* [**Cursor](https://mikro-orm.io/api/postgresql.md#Cursor)
* [**CursorError](https://mikro-orm.io/api/postgresql.md#CursorError)
* [**DatabaseDriver](https://mikro-orm.io/api/postgresql.md#DatabaseDriver)
* [**DatabaseObjectExistsException](https://mikro-orm.io/api/postgresql.md#DatabaseObjectExistsException)
* [**DatabaseObjectNotFoundException](https://mikro-orm.io/api/postgresql.md#DatabaseObjectNotFoundException)
* [**DatabaseView](https://mikro-orm.io/api/postgresql.md#DatabaseView)
* [**DataloaderType](https://mikro-orm.io/api/postgresql.md#DataloaderType)
* [**DateTimeType](https://mikro-orm.io/api/postgresql.md#DateTimeType)
* [**DateType](https://mikro-orm.io/api/postgresql.md#DateType)
* [**DeadlockException](https://mikro-orm.io/api/postgresql.md#DeadlockException)
* [**DecimalType](https://mikro-orm.io/api/postgresql.md#DecimalType)
* [**DeepPartial](https://mikro-orm.io/api/postgresql.md#DeepPartial)
* [**DefaultLogger](https://mikro-orm.io/api/postgresql.md#DefaultLogger)
* [**DeferMode](https://mikro-orm.io/api/postgresql.md#DeferMode)
* [**DefineConfig](https://mikro-orm.io/api/postgresql.md#DefineConfig)
* [**defineEntity](https://mikro-orm.io/api/postgresql.md#defineEntity)
* [**DefineEntityHooks](https://mikro-orm.io/api/postgresql.md#DefineEntityHooks)
* [**DeleteOptions](https://mikro-orm.io/api/postgresql.md#DeleteOptions)
* [**DeleteQueryBuilder](https://mikro-orm.io/api/postgresql.md#DeleteQueryBuilder)
* [**Dictionary](https://mikro-orm.io/api/postgresql.md#Dictionary)
* [**DoubleType](https://mikro-orm.io/api/postgresql.md#DoubleType)
* [**DriverException](https://mikro-orm.io/api/postgresql.md#DriverException)
* [**DriverMethodOptions](https://mikro-orm.io/api/postgresql.md#DriverMethodOptions)
* [**DropSchemaOptions](https://mikro-orm.io/api/postgresql.md#DropSchemaOptions)
* [**EagerProps](https://mikro-orm.io/api/postgresql.md#EagerProps)
* [**Edge](https://mikro-orm.io/api/postgresql.md#Edge)
* [**EMBEDDABLE\_ARRAY\_OPS](https://mikro-orm.io/api/postgresql.md#EMBEDDABLE_ARRAY_OPS)
* [**EmbeddableOptions](https://mikro-orm.io/api/postgresql.md#EmbeddableOptions)
* [**EmbeddedOptions](https://mikro-orm.io/api/postgresql.md#EmbeddedOptions)
* [**EmbeddedPrefixMode](https://mikro-orm.io/api/postgresql.md#EmbeddedPrefixMode)
* [**EmptyOptions](https://mikro-orm.io/api/postgresql.md#EmptyOptions)
* [**EnsureDatabaseOptions](https://mikro-orm.io/api/postgresql.md#EnsureDatabaseOptions)
* [**EntityAssigner](https://mikro-orm.io/api/postgresql.md#EntityAssigner)
* [**EntityCaseNamingStrategy](https://mikro-orm.io/api/postgresql.md#EntityCaseNamingStrategy)
* [**EntityClass](https://mikro-orm.io/api/postgresql.md#EntityClass)
* [**EntityComparator](https://mikro-orm.io/api/postgresql.md#EntityComparator)
* [**EntityCtor](https://mikro-orm.io/api/postgresql.md#EntityCtor)
* [**EntityData](https://mikro-orm.io/api/postgresql.md#EntityData)
* [**EntityDataValue](https://mikro-orm.io/api/postgresql.md#EntityDataValue)
* [**EntityDictionary](https://mikro-orm.io/api/postgresql.md#EntityDictionary)
* [**EntityDTO](https://mikro-orm.io/api/postgresql.md#EntityDTO)
* [**EntityDTOProp](https://mikro-orm.io/api/postgresql.md#EntityDTOProp)
* [**EntityFactory](https://mikro-orm.io/api/postgresql.md#EntityFactory)
* [**EntityField](https://mikro-orm.io/api/postgresql.md#EntityField)
* [**EntityKey](https://mikro-orm.io/api/postgresql.md#EntityKey)
* [**EntityLoader](https://mikro-orm.io/api/postgresql.md#EntityLoader)
* [**EntityLoaderOptions](https://mikro-orm.io/api/postgresql.md#EntityLoaderOptions)
* [**EntityManagerType](https://mikro-orm.io/api/postgresql.md#EntityManagerType)
* [**EntityMetadata](https://mikro-orm.io/api/postgresql.md#EntityMetadata)
* [**EntityMetadataWithProperties](https://mikro-orm.io/api/postgresql.md#EntityMetadataWithProperties)
* [**EntityName](https://mikro-orm.io/api/postgresql.md#EntityName)
* [**EntityOptions](https://mikro-orm.io/api/postgresql.md#EntityOptions)
* [**EntityProperty](https://mikro-orm.io/api/postgresql.md#EntityProperty)
* [**EntityProps](https://mikro-orm.io/api/postgresql.md#EntityProps)
* [**EntityRef](https://mikro-orm.io/api/postgresql.md#EntityRef)
* [**EntityRepository](https://mikro-orm.io/api/postgresql.md#EntityRepository)
* [**EntityRepositoryType](https://mikro-orm.io/api/postgresql.md#EntityRepositoryType)
* [**EntitySerializer](https://mikro-orm.io/api/postgresql.md#EntitySerializer)
* [**EntitySchema](https://mikro-orm.io/api/postgresql.md#EntitySchema)
* [**EntitySchemaMetadata](https://mikro-orm.io/api/postgresql.md#EntitySchemaMetadata)
* [**EntitySchemaProperty](https://mikro-orm.io/api/postgresql.md#EntitySchemaProperty)
* [**EntitySchemaWithMeta](https://mikro-orm.io/api/postgresql.md#EntitySchemaWithMeta)
* [**EntityTransformer](https://mikro-orm.io/api/postgresql.md#EntityTransformer)
* [**EntityType](https://mikro-orm.io/api/postgresql.md#EntityType)
* [**EntityValue](https://mikro-orm.io/api/postgresql.md#EntityValue)
* [**EnumArrayType](https://mikro-orm.io/api/postgresql.md#EnumArrayType)
* [**EnumOptions](https://mikro-orm.io/api/postgresql.md#EnumOptions)
* [**EnumType](https://mikro-orm.io/api/postgresql.md#EnumType)
* [**equals](https://mikro-orm.io/api/postgresql.md#equals)
* [**EventArgs](https://mikro-orm.io/api/postgresql.md#EventArgs)
* [**EventManager](https://mikro-orm.io/api/postgresql.md#EventManager)
* [**EventSubscriber](https://mikro-orm.io/api/postgresql.md#EventSubscriber)
* [**EventType](https://mikro-orm.io/api/postgresql.md#EventType)
* [**EventTypeMap](https://mikro-orm.io/api/postgresql.md#EventTypeMap)
* [**ExceptionConverter](https://mikro-orm.io/api/postgresql.md#ExceptionConverter)
* [**ExecuteOptions](https://mikro-orm.io/api/postgresql.md#ExecuteOptions)
* [**ExpandHint](https://mikro-orm.io/api/postgresql.md#ExpandHint)
* [**ExpandProperty](https://mikro-orm.io/api/postgresql.md#ExpandProperty)
* [**ExpandQuery](https://mikro-orm.io/api/postgresql.md#ExpandQuery)
* [**ExpandScalar](https://mikro-orm.io/api/postgresql.md#ExpandScalar)
* [**FactoryOptions](https://mikro-orm.io/api/postgresql.md#FactoryOptions)
* [**Field](https://mikro-orm.io/api/postgresql.md#Field)
* [**FilterDef](https://mikro-orm.io/api/postgresql.md#FilterDef)
* [**FilterItemValue](https://mikro-orm.io/api/postgresql.md#FilterItemValue)
* [**FilterKey](https://mikro-orm.io/api/postgresql.md#FilterKey)
* [**FilterObject](https://mikro-orm.io/api/postgresql.md#FilterObject)
* [**FilterOptions](https://mikro-orm.io/api/postgresql.md#FilterOptions)
* [**FilterQuery](https://mikro-orm.io/api/postgresql.md#FilterQuery)
* [**FilterValue](https://mikro-orm.io/api/postgresql.md#FilterValue)
* [**FindAllOptions](https://mikro-orm.io/api/postgresql.md#FindAllOptions)
* [**FindByCursorOptions](https://mikro-orm.io/api/postgresql.md#FindByCursorOptions)
* [**FindOneOptions](https://mikro-orm.io/api/postgresql.md#FindOneOptions)
* [**FindOneOrFailOptions](https://mikro-orm.io/api/postgresql.md#FindOneOrFailOptions)
* [**FindOptions](https://mikro-orm.io/api/postgresql.md#FindOptions)
* [**FlatQueryOrderMap](https://mikro-orm.io/api/postgresql.md#FlatQueryOrderMap)
* [**FloatType](https://mikro-orm.io/api/postgresql.md#FloatType)
* [**FlushEventArgs](https://mikro-orm.io/api/postgresql.md#FlushEventArgs)
* [**FlushMode](https://mikro-orm.io/api/postgresql.md#FlushMode)
* [**ForeignKey](https://mikro-orm.io/api/postgresql.md#ForeignKey)
* [**ForeignKeyConstraintViolationException](https://mikro-orm.io/api/postgresql.md#ForeignKeyConstraintViolationException)
* [**ForkOptions](https://mikro-orm.io/api/postgresql.md#ForkOptions)
* [**FormulaCallback](https://mikro-orm.io/api/postgresql.md#FormulaCallback)
* [**FormulaTable](https://mikro-orm.io/api/postgresql.md#FormulaTable)
* [**FromEntityType](https://mikro-orm.io/api/postgresql.md#FromEntityType)
* [**FullTextType](https://mikro-orm.io/api/postgresql.md#FullTextType)
* [**GeneratedCacheAdapter](https://mikro-orm.io/api/postgresql.md#GeneratedCacheAdapter)
* [**GeneratedColumnCallback](https://mikro-orm.io/api/postgresql.md#GeneratedColumnCallback)
* [**GenerateOptions](https://mikro-orm.io/api/postgresql.md#GenerateOptions)
* [**GetKyselyOptions](https://mikro-orm.io/api/postgresql.md#GetKyselyOptions)
* [**GetReferenceOptions](https://mikro-orm.io/api/postgresql.md#GetReferenceOptions)
* [**GetRepository](https://mikro-orm.io/api/postgresql.md#GetRepository)
* [**GroupOperator](https://mikro-orm.io/api/postgresql.md#GroupOperator)
* [**Hidden](https://mikro-orm.io/api/postgresql.md#Hidden)
* [**HiddenProps](https://mikro-orm.io/api/postgresql.md#HiddenProps)
* [**Highlighter](https://mikro-orm.io/api/postgresql.md#Highlighter)
* [**Hydrator](https://mikro-orm.io/api/postgresql.md#Hydrator)
* [**ChangeSet](https://mikro-orm.io/api/postgresql.md#ChangeSet)
* [**ChangeSetComputer](https://mikro-orm.io/api/postgresql.md#ChangeSetComputer)
* [**ChangeSetPersister](https://mikro-orm.io/api/postgresql.md#ChangeSetPersister)
* [**ChangeSetType](https://mikro-orm.io/api/postgresql.md#ChangeSetType)
* [**CharacterType](https://mikro-orm.io/api/postgresql.md#CharacterType)
* [**CheckCallback](https://mikro-orm.io/api/postgresql.md#CheckCallback)
* [**CheckConstraint](https://mikro-orm.io/api/postgresql.md#CheckConstraint)
* [**CheckConstraintViolationException](https://mikro-orm.io/api/postgresql.md#CheckConstraintViolationException)
* [**CheckDef](https://mikro-orm.io/api/postgresql.md#CheckDef)
* [**IConfiguration](https://mikro-orm.io/api/postgresql.md#IConfiguration)
* [**ICriteriaNode](https://mikro-orm.io/api/postgresql.md#ICriteriaNode)
* [**ICriteriaNodeProcessOptions](https://mikro-orm.io/api/postgresql.md#ICriteriaNodeProcessOptions)
* [**IDatabaseDriver](https://mikro-orm.io/api/postgresql.md#IDatabaseDriver)
* [**IdentityMap](https://mikro-orm.io/api/postgresql.md#IdentityMap)
* [**IEntityGenerator](https://mikro-orm.io/api/postgresql.md#IEntityGenerator)
* [**IMigrationGenerator](https://mikro-orm.io/api/postgresql.md#IMigrationGenerator)
* [**IMigrator](https://mikro-orm.io/api/postgresql.md#IMigrator)
* [**ImportsResolver](https://mikro-orm.io/api/postgresql.md#ImportsResolver)
* [**IndexCallback](https://mikro-orm.io/api/postgresql.md#IndexCallback)
* [**IndexColumnOptions](https://mikro-orm.io/api/postgresql.md#IndexColumnOptions)
* [**IndexDef](https://mikro-orm.io/api/postgresql.md#IndexDef)
* [**IndexOptions](https://mikro-orm.io/api/postgresql.md#IndexOptions)
* [**InferClassEntityDB](https://mikro-orm.io/api/postgresql.md#InferClassEntityDB)
* [**InferDBFromKysely](https://mikro-orm.io/api/postgresql.md#InferDBFromKysely)
* [**InferEntity](https://mikro-orm.io/api/postgresql.md#InferEntity)
* [**InferEntityFromProperties](https://mikro-orm.io/api/postgresql.md#InferEntityFromProperties)
* [**InferEntityName](https://mikro-orm.io/api/postgresql.md#InferEntityName)
* [**InferEntityProperties](https://mikro-orm.io/api/postgresql.md#InferEntityProperties)
* [**InferKyselyDB](https://mikro-orm.io/api/postgresql.md#InferKyselyDB)
* [**InferKyselyTable](https://mikro-orm.io/api/postgresql.md#InferKyselyTable)
* [**InferPrimaryKey](https://mikro-orm.io/api/postgresql.md#InferPrimaryKey)
* [**InitCollectionOptions](https://mikro-orm.io/api/postgresql.md#InitCollectionOptions)
* [**InsertQueryBuilder](https://mikro-orm.io/api/postgresql.md#InsertQueryBuilder)
* [**IntegerType](https://mikro-orm.io/api/postgresql.md#IntegerType)
* [**IntervalType](https://mikro-orm.io/api/postgresql.md#IntervalType)
* [**InvalidFieldNameException](https://mikro-orm.io/api/postgresql.md#InvalidFieldNameException)
* [**IPrimaryKey](https://mikro-orm.io/api/postgresql.md#IPrimaryKey)
* [**IQueryBuilder](https://mikro-orm.io/api/postgresql.md#IQueryBuilder)
* [**ISeedManager](https://mikro-orm.io/api/postgresql.md#ISeedManager)
* [**ISchemaGenerator](https://mikro-orm.io/api/postgresql.md#ISchemaGenerator)
* [**IsolationLevel](https://mikro-orm.io/api/postgresql.md#IsolationLevel)
* [**isRaw](https://mikro-orm.io/api/postgresql.md#isRaw)
* [**IsSubset](https://mikro-orm.io/api/postgresql.md#IsSubset)
* [**IsUnknown](https://mikro-orm.io/api/postgresql.md#IsUnknown)
* [**IType](https://mikro-orm.io/api/postgresql.md#IType)
* [**IWrappedEntity](https://mikro-orm.io/api/postgresql.md#IWrappedEntity)
* [**JoinOptions](https://mikro-orm.io/api/postgresql.md#JoinOptions)
* [**JoinSelectField](https://mikro-orm.io/api/postgresql.md#JoinSelectField)
* [**JoinType](https://mikro-orm.io/api/postgresql.md#JoinType)
* [**JSON\_KEY\_OPERATORS](https://mikro-orm.io/api/postgresql.md#JSON_KEY_OPERATORS)
* [**JsonProperty](https://mikro-orm.io/api/postgresql.md#JsonProperty)
* [**JsonType](https://mikro-orm.io/api/postgresql.md#JsonType)
* [**Kysely](https://mikro-orm.io/api/postgresql.md#Kysely)
* [**LoadCountOptions](https://mikro-orm.io/api/postgresql.md#LoadCountOptions)
* [**Loaded](https://mikro-orm.io/api/postgresql.md#Loaded)
* [**LoadedCollection](https://mikro-orm.io/api/postgresql.md#LoadedCollection)
* [**LoadedReference](https://mikro-orm.io/api/postgresql.md#LoadedReference)
* [**LoadHint](https://mikro-orm.io/api/postgresql.md#LoadHint)
* [**LoadReferenceOptions](https://mikro-orm.io/api/postgresql.md#LoadReferenceOptions)
* [**LoadReferenceOrFailOptions](https://mikro-orm.io/api/postgresql.md#LoadReferenceOrFailOptions)
* [**LoadStrategy](https://mikro-orm.io/api/postgresql.md#LoadStrategy)
* [**LockMode](https://mikro-orm.io/api/postgresql.md#LockMode)
* [**LockOptions](https://mikro-orm.io/api/postgresql.md#LockOptions)
* [**LockWaitTimeoutException](https://mikro-orm.io/api/postgresql.md#LockWaitTimeoutException)
* [**LogContext](https://mikro-orm.io/api/postgresql.md#LogContext)
* [**Logger](https://mikro-orm.io/api/postgresql.md#Logger)
* [**LoggerNamespace](https://mikro-orm.io/api/postgresql.md#LoggerNamespace)
* [**LoggerOptions](https://mikro-orm.io/api/postgresql.md#LoggerOptions)
* [**LoggingOptions](https://mikro-orm.io/api/postgresql.md#LoggingOptions)
* [**ManyToManyOptions](https://mikro-orm.io/api/postgresql.md#ManyToManyOptions)
* [**ManyToOneOptions](https://mikro-orm.io/api/postgresql.md#ManyToOneOptions)
* [**MapTableName](https://mikro-orm.io/api/postgresql.md#MapTableName)
* [**MapValueAsTable](https://mikro-orm.io/api/postgresql.md#MapValueAsTable)
* [**MatchingOptions](https://mikro-orm.io/api/postgresql.md#MatchingOptions)
* [**MaybePromise](https://mikro-orm.io/api/postgresql.md#MaybePromise)
* [**MaybeReturnType](https://mikro-orm.io/api/postgresql.md#MaybeReturnType)
* [**MediumIntType](https://mikro-orm.io/api/postgresql.md#MediumIntType)
* [**MemoryCacheAdapter](https://mikro-orm.io/api/postgresql.md#MemoryCacheAdapter)
* [**MergeLoaded](https://mikro-orm.io/api/postgresql.md#MergeLoaded)
* [**MergeOptions](https://mikro-orm.io/api/postgresql.md#MergeOptions)
* [**MergeSelected](https://mikro-orm.io/api/postgresql.md#MergeSelected)
* [**MetadataDiscovery](https://mikro-orm.io/api/postgresql.md#MetadataDiscovery)
* [**MetadataDiscoveryOptions](https://mikro-orm.io/api/postgresql.md#MetadataDiscoveryOptions)
* [**MetadataError](https://mikro-orm.io/api/postgresql.md#MetadataError)
* [**MetadataProcessor](https://mikro-orm.io/api/postgresql.md#MetadataProcessor)
* [**MetadataProvider](https://mikro-orm.io/api/postgresql.md#MetadataProvider)
* [**MetadataStorage](https://mikro-orm.io/api/postgresql.md#MetadataStorage)
* [**MigrateOptions](https://mikro-orm.io/api/postgresql.md#MigrateOptions)
* [**MigrationDiff](https://mikro-orm.io/api/postgresql.md#MigrationDiff)
* [**MigrationInfo](https://mikro-orm.io/api/postgresql.md#MigrationInfo)
* [**MigrationObject](https://mikro-orm.io/api/postgresql.md#MigrationObject)
* [**MigrationResult](https://mikro-orm.io/api/postgresql.md#MigrationResult)
* [**MigrationRow](https://mikro-orm.io/api/postgresql.md#MigrationRow)
* [**MigrationsOptions](https://mikro-orm.io/api/postgresql.md#MigrationsOptions)
* [**MigratorEvent](https://mikro-orm.io/api/postgresql.md#MigratorEvent)
* [**MikroKyselyPlugin](https://mikro-orm.io/api/postgresql.md#MikroKyselyPlugin)
* [**MikroKyselyPluginOptions](https://mikro-orm.io/api/postgresql.md#MikroKyselyPluginOptions)
* [**ModifyContext](https://mikro-orm.io/api/postgresql.md#ModifyContext)
* [**ModifyFields](https://mikro-orm.io/api/postgresql.md#ModifyFields)
* [**ModifyHint](https://mikro-orm.io/api/postgresql.md#ModifyHint)
* [**MongoNamingStrategy](https://mikro-orm.io/api/postgresql.md#MongoNamingStrategy)
* [**MySqlSchemaHelper](https://mikro-orm.io/api/postgresql.md#MySqlSchemaHelper)
* [**NamingStrategy](https://mikro-orm.io/api/postgresql.md#NamingStrategy)
* [**NativeDeleteOptions](https://mikro-orm.io/api/postgresql.md#NativeDeleteOptions)
* [**NativeInsertUpdateManyOptions](https://mikro-orm.io/api/postgresql.md#NativeInsertUpdateManyOptions)
* [**NativeInsertUpdateOptions](https://mikro-orm.io/api/postgresql.md#NativeInsertUpdateOptions)
* [**New](https://mikro-orm.io/api/postgresql.md#New)
* [**Node](https://mikro-orm.io/api/postgresql.md#Node)
* [**NodeSqliteDialect](https://mikro-orm.io/api/postgresql.md#NodeSqliteDialect)
* [**NodeState](https://mikro-orm.io/api/postgresql.md#NodeState)
* [**NonUniqueFieldNameException](https://mikro-orm.io/api/postgresql.md#NonUniqueFieldNameException)
* [**NotFoundError](https://mikro-orm.io/api/postgresql.md#NotFoundError)
* [**NotNullConstraintViolationException](https://mikro-orm.io/api/postgresql.md#NotNullConstraintViolationException)
* [**NullCacheAdapter](https://mikro-orm.io/api/postgresql.md#NullCacheAdapter)
* [**NullHighlighter](https://mikro-orm.io/api/postgresql.md#NullHighlighter)
* [**ObjectHydrator](https://mikro-orm.io/api/postgresql.md#ObjectHydrator)
* [**ObjectQuery](https://mikro-orm.io/api/postgresql.md#ObjectQuery)
* [**OnConflictClause](https://mikro-orm.io/api/postgresql.md#OnConflictClause)
* [**OneToManyOptions](https://mikro-orm.io/api/postgresql.md#OneToManyOptions)
* [**OneToOneOptions](https://mikro-orm.io/api/postgresql.md#OneToOneOptions)
* [**Opt](https://mikro-orm.io/api/postgresql.md#Opt)
* [**OptimisticLockError](https://mikro-orm.io/api/postgresql.md#OptimisticLockError)
* [**OptionalProps](https://mikro-orm.io/api/postgresql.md#OptionalProps)
* [**OracleDialect](https://mikro-orm.io/api/postgresql.md#OracleDialect)
* [**OracleDialectConfig](https://mikro-orm.io/api/postgresql.md#OracleDialectConfig)
* [**OraclePool](https://mikro-orm.io/api/postgresql.md#OraclePool)
* [**OraclePoolConnection](https://mikro-orm.io/api/postgresql.md#OraclePoolConnection)
* [**OrderDefinition](https://mikro-orm.io/api/postgresql.md#OrderDefinition)
* [**p](https://mikro-orm.io/api/postgresql.md#p)
* [**parseJsonSafe](https://mikro-orm.io/api/postgresql.md#parseJsonSafe)
* [**PlainObject](https://mikro-orm.io/api/postgresql.md#PlainObject)
* [**Platform](https://mikro-orm.io/api/postgresql.md#Platform)
* [**PolymorphicRef](https://mikro-orm.io/api/postgresql.md#PolymorphicRef)
* [**PoolConfig](https://mikro-orm.io/api/postgresql.md#PoolConfig)
* [**Populate](https://mikro-orm.io/api/postgresql.md#Populate)
* [**PopulateHint](https://mikro-orm.io/api/postgresql.md#PopulateHint)
* [**PopulateHintOptions](https://mikro-orm.io/api/postgresql.md#PopulateHintOptions)
* [**PopulateOptions](https://mikro-orm.io/api/postgresql.md#PopulateOptions)
* [**PopulatePath](https://mikro-orm.io/api/postgresql.md#PopulatePath)
* [**PostgreSqlSchemaHelper](https://mikro-orm.io/api/postgresql.md#PostgreSqlSchemaHelper)
* [**Prefixes](https://mikro-orm.io/api/postgresql.md#Prefixes)
* [**Primary](https://mikro-orm.io/api/postgresql.md#Primary)
* [**PrimaryKeyOptions](https://mikro-orm.io/api/postgresql.md#PrimaryKeyOptions)
* [**PrimaryKeyProp](https://mikro-orm.io/api/postgresql.md#PrimaryKeyProp)
* [**PropertyBuilders](https://mikro-orm.io/api/postgresql.md#PropertyBuilders)
* [**PropertyChain](https://mikro-orm.io/api/postgresql.md#PropertyChain)
* [**PropertyOptions](https://mikro-orm.io/api/postgresql.md#PropertyOptions)
* [**QBField](https://mikro-orm.io/api/postgresql.md#QBField)
* [**QBFilterQuery](https://mikro-orm.io/api/postgresql.md#QBFilterQuery)
* [**QBStreamOptions](https://mikro-orm.io/api/postgresql.md#QBStreamOptions)
* [**QueryBuilder](https://mikro-orm.io/api/postgresql.md#QueryBuilder)
* [**QueryFlag](https://mikro-orm.io/api/postgresql.md#QueryFlag)
* [**QueryOperator](https://mikro-orm.io/api/postgresql.md#QueryOperator)
* [**QueryOrder](https://mikro-orm.io/api/postgresql.md#QueryOrder)
* [**QueryOrderKeys](https://mikro-orm.io/api/postgresql.md#QueryOrderKeys)
* [**QueryOrderKeysFlat](https://mikro-orm.io/api/postgresql.md#QueryOrderKeysFlat)
* [**QueryOrderMap](https://mikro-orm.io/api/postgresql.md#QueryOrderMap)
* [**QueryOrderNumeric](https://mikro-orm.io/api/postgresql.md#QueryOrderNumeric)
* [**QueryResult](https://mikro-orm.io/api/postgresql.md#QueryResult)
* [**QueryType](https://mikro-orm.io/api/postgresql.md#QueryType)
* [**quote](https://mikro-orm.io/api/postgresql.md#quote)
* [**Raw](https://mikro-orm.io/api/postgresql.md#Raw)
* [**RawQueryFragment](https://mikro-orm.io/api/postgresql.md#RawQueryFragment)
* [**RawQueryFragmentSymbol](https://mikro-orm.io/api/postgresql.md#RawQueryFragmentSymbol)
* [**ReadOnlyException](https://mikro-orm.io/api/postgresql.md#ReadOnlyException)
* [**ref](https://mikro-orm.io/api/postgresql.md#ref)
* [**Ref](https://mikro-orm.io/api/postgresql.md#Ref)
* [**Reference](https://mikro-orm.io/api/postgresql.md#Reference)
* [**ReferenceKind](https://mikro-orm.io/api/postgresql.md#ReferenceKind)
* [**ReferenceOptions](https://mikro-orm.io/api/postgresql.md#ReferenceOptions)
* [**RefreshDatabaseOptions](https://mikro-orm.io/api/postgresql.md#RefreshDatabaseOptions)
* [**RegisterOptions](https://mikro-orm.io/api/postgresql.md#RegisterOptions)
* [**rel](https://mikro-orm.io/api/postgresql.md#rel)
* [**Rel](https://mikro-orm.io/api/postgresql.md#Rel)
* [**RequestContext](https://mikro-orm.io/api/postgresql.md#RequestContext)
* [**RequiredEntityData](https://mikro-orm.io/api/postgresql.md#RequiredEntityData)
* [**RequiredNullable](https://mikro-orm.io/api/postgresql.md#RequiredNullable)
* [**RunQueryBuilder](https://mikro-orm.io/api/postgresql.md#RunQueryBuilder)
* [**Scalar](https://mikro-orm.io/api/postgresql.md#Scalar)
* [**SCALAR\_TYPES](https://mikro-orm.io/api/postgresql.md#SCALAR_TYPES)
* [**ScalarRef](https://mikro-orm.io/api/postgresql.md#ScalarRef)
* [**ScalarReference](https://mikro-orm.io/api/postgresql.md#ScalarReference)
* [**SeederObject](https://mikro-orm.io/api/postgresql.md#SeederObject)
* [**SeederOptions](https://mikro-orm.io/api/postgresql.md#SeederOptions)
* [**Selected](https://mikro-orm.io/api/postgresql.md#Selected)
* [**SelectQueryBuilder](https://mikro-orm.io/api/postgresql.md#SelectQueryBuilder)
* [**SerializationContext](https://mikro-orm.io/api/postgresql.md#SerializationContext)
* [**serialize](https://mikro-orm.io/api/postgresql.md#serialize)
* [**SerializedPrimaryKeyOptions](https://mikro-orm.io/api/postgresql.md#SerializedPrimaryKeyOptions)
* [**SerializeDTO](https://mikro-orm.io/api/postgresql.md#SerializeDTO)
* [**SerializeOptions](https://mikro-orm.io/api/postgresql.md#SerializeOptions)
* [**ServerException](https://mikro-orm.io/api/postgresql.md#ServerException)
* [**SchemaColumns](https://mikro-orm.io/api/postgresql.md#SchemaColumns)
* [**SchemaComparator](https://mikro-orm.io/api/postgresql.md#SchemaComparator)
* [**SchemaDifference](https://mikro-orm.io/api/postgresql.md#SchemaDifference)
* [**SchemaGenerator](https://mikro-orm.io/api/postgresql.md#SchemaGenerator)
* [**SchemaHelper](https://mikro-orm.io/api/postgresql.md#SchemaHelper)
* [**SchemaTable](https://mikro-orm.io/api/postgresql.md#SchemaTable)
* [**SimpleColumnMeta](https://mikro-orm.io/api/postgresql.md#SimpleColumnMeta)
* [**SimpleLogger](https://mikro-orm.io/api/postgresql.md#SimpleLogger)
* [**SmallIntType](https://mikro-orm.io/api/postgresql.md#SmallIntType)
* [**SnakeCase](https://mikro-orm.io/api/postgresql.md#SnakeCase)
* [**sql](https://mikro-orm.io/api/postgresql.md#sql)
* [**SqlEntityManager](https://mikro-orm.io/api/postgresql.md#SqlEntityManager)
* [**SqlEntityRepository](https://mikro-orm.io/api/postgresql.md#SqlEntityRepository)
* [**SqliteDriver](https://mikro-orm.io/api/postgresql.md#SqliteDriver)
* [**SqlitePlatform](https://mikro-orm.io/api/postgresql.md#SqlitePlatform)
* [**SqliteSchemaHelper](https://mikro-orm.io/api/postgresql.md#SqliteSchemaHelper)
* [**SqlSchemaGenerator](https://mikro-orm.io/api/postgresql.md#SqlSchemaGenerator)
* [**StreamOptions](https://mikro-orm.io/api/postgresql.md#StreamOptions)
* [**StringType](https://mikro-orm.io/api/postgresql.md#StringType)
* [**Subquery](https://mikro-orm.io/api/postgresql.md#Subquery)
* [**SyncCacheAdapter](https://mikro-orm.io/api/postgresql.md#SyncCacheAdapter)
* [**SyntaxErrorException](https://mikro-orm.io/api/postgresql.md#SyntaxErrorException)
* [**t](https://mikro-orm.io/api/postgresql.md#t)
* [**Table](https://mikro-orm.io/api/postgresql.md#Table)
* [**TableDifference](https://mikro-orm.io/api/postgresql.md#TableDifference)
* [**TableExistsException](https://mikro-orm.io/api/postgresql.md#TableExistsException)
* [**TableNotFoundException](https://mikro-orm.io/api/postgresql.md#TableNotFoundException)
* [**TableOptions](https://mikro-orm.io/api/postgresql.md#TableOptions)
* [**TextType](https://mikro-orm.io/api/postgresql.md#TextType)
* [**TimeType](https://mikro-orm.io/api/postgresql.md#TimeType)
* [**TinyIntType](https://mikro-orm.io/api/postgresql.md#TinyIntType)
* [**Transaction](https://mikro-orm.io/api/postgresql.md#Transaction)
* [**TransactionContext](https://mikro-orm.io/api/postgresql.md#TransactionContext)
* [**TransactionEventArgs](https://mikro-orm.io/api/postgresql.md#TransactionEventArgs)
* [**TransactionEventBroadcaster](https://mikro-orm.io/api/postgresql.md#TransactionEventBroadcaster)
* [**TransactionEventType](https://mikro-orm.io/api/postgresql.md#TransactionEventType)
* [**TransactionManager](https://mikro-orm.io/api/postgresql.md#TransactionManager)
* [**TransactionOptions](https://mikro-orm.io/api/postgresql.md#TransactionOptions)
* [**TransactionPropagation](https://mikro-orm.io/api/postgresql.md#TransactionPropagation)
* [**TransactionStateError](https://mikro-orm.io/api/postgresql.md#TransactionStateError)
* [**TransformContext](https://mikro-orm.io/api/postgresql.md#TransformContext)
* [**TruncateQueryBuilder](https://mikro-orm.io/api/postgresql.md#TruncateQueryBuilder)
* [**Type](https://mikro-orm.io/api/postgresql.md#Type)
* [**TypeConfig](https://mikro-orm.io/api/postgresql.md#TypeConfig)
* [**types](https://mikro-orm.io/api/postgresql.md#types)
* [**Uint8ArrayType](https://mikro-orm.io/api/postgresql.md#Uint8ArrayType)
* [**UnboxArray](https://mikro-orm.io/api/postgresql.md#UnboxArray)
* [**UnderscoreNamingStrategy](https://mikro-orm.io/api/postgresql.md#UnderscoreNamingStrategy)
* [**UniqueConstraintViolationException](https://mikro-orm.io/api/postgresql.md#UniqueConstraintViolationException)
* [**UniqueOptions](https://mikro-orm.io/api/postgresql.md#UniqueOptions)
* [**UnitOfWork](https://mikro-orm.io/api/postgresql.md#UnitOfWork)
* [**UniversalPropertyKeys](https://mikro-orm.io/api/postgresql.md#UniversalPropertyKeys)
* [**UnknownType](https://mikro-orm.io/api/postgresql.md#UnknownType)
* [**UpdateOptions](https://mikro-orm.io/api/postgresql.md#UpdateOptions)
* [**UpdateQueryBuilder](https://mikro-orm.io/api/postgresql.md#UpdateQueryBuilder)
* [**UpdateSchemaOptions](https://mikro-orm.io/api/postgresql.md#UpdateSchemaOptions)
* [**UpsertManyOptions](https://mikro-orm.io/api/postgresql.md#UpsertManyOptions)
* [**UpsertOptions](https://mikro-orm.io/api/postgresql.md#UpsertOptions)
* [**Utils](https://mikro-orm.io/api/postgresql.md#Utils)
* [**UuidType](https://mikro-orm.io/api/postgresql.md#UuidType)
* [**ValidationError](https://mikro-orm.io/api/postgresql.md#ValidationError)
* [**WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)
* [**wrap](https://mikro-orm.io/api/postgresql.md#wrap)
* [**WrappedEntity](https://mikro-orm.io/api/postgresql.md#WrappedEntity)

### Classes

* [**EntityManager](https://mikro-orm.io/api/postgresql/class/EntityManager.md)
* [**MikroORM](https://mikro-orm.io/api/postgresql/class/MikroORM.md)
* [**PostgreSqlConnection](https://mikro-orm.io/api/postgresql/class/PostgreSqlConnection.md)
* [**PostgreSqlDriver](https://mikro-orm.io/api/postgresql/class/PostgreSqlDriver.md)
* [**PostgreSqlPlatform](https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md)

### Type Aliases

* [**Options](https://mikro-orm.io/api/postgresql.md#Options)

### Functions

* [**defineConfig](https://mikro-orm.io/api/postgresql/function/defineConfig.md)
* [**raw](https://mikro-orm.io/api/postgresql/function/raw.md)

## References<!-- -->[**](#references)

### [**](#abstractnamingstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L6)AbstractNamingStrategy

Re-exports

<!-- -->

[AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)

### [**](#abstractsqlconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L21)AbstractSqlConnection

Re-exports

<!-- -->

[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

### [**](#abstractsqldriver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L72)AbstractSqlDriver

Re-exports

<!-- -->

[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)

### [**](#abstractsqlplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L21)AbstractSqlPlatform

Re-exports

<!-- -->

[AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1510)Alias

Re-exports

<!-- -->

[Alias](https://mikro-orm.io/api/sql/interface/Alias.md)

### [**](#aliasedfiltercondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L467)AliasedFilterCondition

Re-exports

<!-- -->

[AliasedFilterCondition](https://mikro-orm.io/api/sql.md#AliasedFilterCondition)

### [**](#anyentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L29)AnyEntity

Re-exports

<!-- -->

[AnyEntity](https://mikro-orm.io/api/core.md#AnyEntity)

### [**](#anyquerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4152)AnyQueryBuilder

Re-exports

<!-- -->

[AnyQueryBuilder](https://mikro-orm.io/api/sql.md#AnyQueryBuilder)

### [**](#anystring)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L96)AnyString

Re-exports

<!-- -->

[AnyString](https://mikro-orm.io/api/core.md#AnyString)

### [**](#array_operators)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L57)ARRAY\_OPERATORS

Re-exports

<!-- -->

[ARRAY\_OPERATORS](https://mikro-orm.io/api/core.md#ARRAY_OPERATORS)

### [**](#arraytype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L36)ArrayType

Re-exports

<!-- -->

[ArrayType](https://mikro-orm.io/api/core/class/ArrayType.md)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityAssigner.ts#L390)assign

Re-exports

<!-- -->

[assign](https://mikro-orm.io/api/core/function/assign.md)

### [**](#assignoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityAssigner.ts#L392)AssignOptions

Re-exports

<!-- -->

[AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)

### [**](#autopath)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L103)AutoPath

Re-exports

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)

### [**](#baseentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L22)BaseEntity

Re-exports

<!-- -->

[BaseEntity](https://mikro-orm.io/api/core/class/BaseEntity.md)

### [**](#basemysqlplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L18)BaseMySqlPlatform

Re-exports

<!-- -->

[BaseMySqlPlatform](https://mikro-orm.io/api/sql/class/BaseMySqlPlatform.md)

### [**](#basepostgresqlplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L20)BasePostgreSqlPlatform

Re-exports

<!-- -->

[BasePostgreSqlPlatform](https://mikro-orm.io/api/sql/class/BasePostgreSqlPlatform.md)

### [**](#basesqliteconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/sqlite/BaseSqliteConnection.ts#L5)BaseSqliteConnection

Re-exports

<!-- -->

[BaseSqliteConnection](https://mikro-orm.io/api/sql/class/BaseSqliteConnection.md)

### [**](#biginttype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L33)BigIntType

Re-exports

<!-- -->

[BigIntType](https://mikro-orm.io/api/core/class/BigIntType.md)

### [**](#blobtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L34)BlobType

Re-exports

<!-- -->

[BlobType](https://mikro-orm.io/api/core/class/BlobType.md)

### [**](#booleantype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L46)BooleanType

Re-exports

<!-- -->

[BooleanType](https://mikro-orm.io/api/core/class/BooleanType.md)

### [**](#cacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/CacheAdapter.ts#L1)CacheAdapter

Re-exports

<!-- -->

[CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

### [**](#cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L127)Cascade

Re-exports

<!-- -->

[Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)

### [**](#cast)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L45)Cast

Re-exports

<!-- -->

[Cast](https://mikro-orm.io/api/core.md#Cast)

### [**](#cleardatabaseoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L97)ClearDatabaseOptions

Re-exports

<!-- -->

[ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

### [**](#collationoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L489)CollationOptions

Re-exports

<!-- -->

[CollationOptions](https://mikro-orm.io/api/core/interface/CollationOptions.md)

### [**](#collection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L34)Collection

Re-exports

<!-- -->

[Collection](https://mikro-orm.io/api/core/class/Collection.md)

### [**](#column)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L59)Column

Re-exports

<!-- -->

[Column](https://mikro-orm.io/api/sql/interface/Column.md)

### [**](#columndifference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L136)ColumnDifference

Re-exports

<!-- -->

[ColumnDifference](https://mikro-orm.io/api/sql/interface/ColumnDifference.md)

### [**](#comparearrays)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L94)compareArrays

Re-exports

<!-- -->

[compareArrays](https://mikro-orm.io/api/core/function/compareArrays.md)

### [**](#comparebooleans)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L111)compareBooleans

Re-exports

<!-- -->

[compareBooleans](https://mikro-orm.io/api/core/function/compareBooleans.md)

### [**](#comparebuffers)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L118)compareBuffers

Re-exports

<!-- -->

[compareBuffers](https://mikro-orm.io/api/core/function/compareBuffers.md)

### [**](#compareobjects)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L36)compareObjects

Re-exports

<!-- -->

[compareObjects](https://mikro-orm.io/api/core/function/compareObjects.md)

### [**](#compiledfunctions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L16)CompiledFunctions

Re-exports

<!-- -->

[CompiledFunctions](https://mikro-orm.io/api/core.md#CompiledFunctions)

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L12)Config

Re-exports

<!-- -->

[Config](https://mikro-orm.io/api/core.md#Config)

### [**](#configuration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L168)Configuration

Re-exports

<!-- -->

[Configuration](https://mikro-orm.io/api/core/class/Configuration.md)

### [**](#connection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L10)Connection

Re-exports

<!-- -->

[Connection](https://mikro-orm.io/api/core/class/Connection.md)

### [**](#connectionconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L252)ConnectionConfig

Re-exports

<!-- -->

[ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#connectionexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L32)ConnectionException

Re-exports

<!-- -->

[ConnectionException](https://mikro-orm.io/api/core/class/ConnectionException.md)

### [**](#connectionoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L514)ConnectionOptions

Re-exports

<!-- -->

[ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)

### [**](#connectiontype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L18)ConnectionType

Re-exports

<!-- -->

[ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

### [**](#constraintviolationexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L42)ConstraintViolationException

Re-exports

<!-- -->

[ConstraintViolationException](https://mikro-orm.io/api/core/class/ConstraintViolationException.md)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L17)Constructor

Re-exports

<!-- -->

[Constructor](https://mikro-orm.io/api/core.md#Constructor)

### [**](#contextorderbymap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L318)ContextOrderByMap

Re-exports

<!-- -->

[ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)

### [**](#countoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L414)CountOptions

Re-exports

<!-- -->

[CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)

### [**](#countquerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4172)CountQueryBuilder

Re-exports

<!-- -->

[CountQueryBuilder](https://mikro-orm.io/api/sql/interface/CountQueryBuilder.md)

### [**](#createcontextoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L77)CreateContextOptions

Re-exports

<!-- -->

[CreateContextOptions](https://mikro-orm.io/api/core/interface/CreateContextOptions.md)

### [**](#createoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2810)CreateOptions

Re-exports

<!-- -->

[CreateOptions](https://mikro-orm.io/api/core/interface/CreateOptions.md)

### [**](#createschemaoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L98)CreateSchemaOptions

Re-exports

<!-- -->

[CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

### [**](#createsqlfunction)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L228)createSqlFunction

Re-exports

<!-- -->

[createSqlFunction](https://mikro-orm.io/api/core/function/createSqlFunction.md)

### [**](#cteoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/NativeQueryBuilder.ts#L13)CteOptions

Re-exports

<!-- -->

[CteOptions](https://mikro-orm.io/api/sql/interface/CteOptions.md)

### [**](#cursor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Cursor.ts#L58)Cursor

Re-exports

<!-- -->

[Cursor](https://mikro-orm.io/api/core/class/Cursor.md)

### [**](#cursorerror)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/errors.ts#L193)CursorError

Re-exports

<!-- -->

[CursorError](https://mikro-orm.io/api/core/class/CursorError.md)

### [**](#databasedriver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L48)DatabaseDriver

Re-exports

<!-- -->

[DatabaseDriver](https://mikro-orm.io/api/core/class/DatabaseDriver.md)

### [**](#databaseobjectexistsexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L51)DatabaseObjectExistsException

Re-exports

<!-- -->

[DatabaseObjectExistsException](https://mikro-orm.io/api/core/class/DatabaseObjectExistsException.md)

### [**](#databaseobjectnotfoundexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L60)DatabaseObjectNotFoundException

Re-exports

<!-- -->

[DatabaseObjectNotFoundException](https://mikro-orm.io/api/core/class/DatabaseObjectNotFoundException.md)

### [**](#databaseview)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L164)DatabaseView

Re-exports

<!-- -->

[DatabaseView](https://mikro-orm.io/api/sql/interface/DatabaseView.md)

### [**](#dataloadertype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L145)DataloaderType

Re-exports

<!-- -->

[DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

### [**](#datetimetype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L32)DateTimeType

Re-exports

<!-- -->

[DateTimeType](https://mikro-orm.io/api/core/class/DateTimeType.md)

### [**](#datetype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L30)DateType

Re-exports

<!-- -->

[DateType](https://mikro-orm.io/api/core/class/DateType.md)

### [**](#deadlockexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L65)DeadlockException

Re-exports

<!-- -->

[DeadlockException](https://mikro-orm.io/api/core/class/DeadlockException.md)

### [**](#decimaltype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L47)DecimalType

Re-exports

<!-- -->

[DecimalType](https://mikro-orm.io/api/core/class/DecimalType.md)

### [**](#deeppartial)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L43)DeepPartial

Re-exports

<!-- -->

[DeepPartial](https://mikro-orm.io/api/core.md#DeepPartial)

### [**](#defaultlogger)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L5)DefaultLogger

Re-exports

<!-- -->

[DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

### [**](#defermode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L232)DeferMode

Re-exports

<!-- -->

[DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md)

### [**](#defineconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L108)DefineConfig

Re-exports

<!-- -->

[DefineConfig](https://mikro-orm.io/api/core.md#DefineConfig)

### [**](#defineentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1237)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1255)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1273)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1313)defineEntity

Re-exports

<!-- -->

[defineEntity](https://mikro-orm.io/api/core/function/defineEntity.md)

### [**](#defineentityhooks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1318)DefineEntityHooks

Re-exports

<!-- -->

[DefineEntityHooks](https://mikro-orm.io/api/core/interface/DefineEntityHooks.md)

### [**](#deleteoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L456)DeleteOptions

Re-exports

<!-- -->

[DeleteOptions](https://mikro-orm.io/api/core/interface/DeleteOptions.md)

### [**](#deletequerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4191)DeleteQueryBuilder

Re-exports

<!-- -->

[DeleteQueryBuilder](https://mikro-orm.io/api/sql/interface/DeleteQueryBuilder.md)

### [**](#dictionary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L19)Dictionary

Re-exports

<!-- -->

[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#doubletype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L45)DoubleType

Re-exports

<!-- -->

[DoubleType](https://mikro-orm.io/api/core/class/DoubleType.md)

### [**](#driverexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L6)DriverException

Re-exports

<!-- -->

[DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#drivermethodoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L483)DriverMethodOptions

Re-exports

<!-- -->

[DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

### [**](#dropschemaoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L101)DropSchemaOptions

Re-exports

<!-- -->

[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md)

### [**](#eagerprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L10)EagerProps

Re-exports

<!-- -->

[EagerProps](https://mikro-orm.io/api/core.md#EagerProps)

### [**](#edge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/CommitOrderCalculator.ts#L18)Edge

Re-exports

<!-- -->

[Edge](https://mikro-orm.io/api/core/interface/Edge.md)

### [**](#embeddable_array_ops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/enums.ts#L12)EMBEDDABLE\_ARRAY\_OPS

Re-exports

<!-- -->

[EMBEDDABLE\_ARRAY\_OPS](https://mikro-orm.io/api/sql.md#EMBEDDABLE_ARRAY_OPS)

### [**](#embeddableoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L639)EmbeddableOptions

Re-exports

<!-- -->

[EmbeddableOptions](https://mikro-orm.io/api/core/interface/EmbeddableOptions.md)

### [**](#embeddedoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L631)EmbeddedOptions

Re-exports

<!-- -->

[EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)

### [**](#embeddedprefixmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L238)EmbeddedPrefixMode

Re-exports

<!-- -->

[EmbeddedPrefixMode](https://mikro-orm.io/api/core.md#EmbeddedPrefixMode)

### [**](#emptyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L973)EmptyOptions

Re-exports

<!-- -->

[EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md)

### [**](#ensuredatabaseoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L99)EnsureDatabaseOptions

Re-exports

<!-- -->

[EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

### [**](#entityassigner)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityAssigner.ts#L26)EntityAssigner

Re-exports

<!-- -->

[EntityAssigner](https://mikro-orm.io/api/core/class/EntityAssigner.md)

### [**](#entitycasenamingstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L6)EntityCaseNamingStrategy

Re-exports

<!-- -->

[EntityCaseNamingStrategy](https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md)

### [**](#entityclass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L30)EntityClass

Re-exports

<!-- -->

[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)

### [**](#entitycomparator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/EntityComparator.ts#L37)EntityComparator

Re-exports

<!-- -->

[EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

### [**](#entityctor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L116)EntityCtor

Re-exports

<!-- -->

[EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)

### [**](#entitydata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L26)EntityData

Re-exports

<!-- -->

[EntityData](https://mikro-orm.io/api/core.md#EntityData)

### [**](#entitydatavalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L79)EntityDataValue

Re-exports

<!-- -->

[EntityDataValue](https://mikro-orm.io/api/core.md#EntityDataValue)

### [**](#entitydictionary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L47)EntityDictionary

Re-exports

<!-- -->

[EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)

### [**](#entitydto)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L48)EntityDTO

Re-exports

<!-- -->

[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)

### [**](#entitydtoprop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L50)EntityDTOProp

Re-exports

<!-- -->

[EntityDTOProp](https://mikro-orm.io/api/core.md#EntityDTOProp)

### [**](#entityfactory)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L51)EntityFactory

Re-exports

<!-- -->

[EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

### [**](#entityfield)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L182)EntityField

Re-exports

<!-- -->

[EntityField](https://mikro-orm.io/api/core.md#EntityField)

### [**](#entitykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L77)EntityKey

Re-exports

<!-- -->

[EntityKey](https://mikro-orm.io/api/core.md#EntityKey)

### [**](#entityloader)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L61)EntityLoader

Re-exports

<!-- -->

[EntityLoader](https://mikro-orm.io/api/core/class/EntityLoader.md)

### [**](#entityloaderoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L38)EntityLoaderOptions

Re-exports

<!-- -->

[EntityLoaderOptions](https://mikro-orm.io/api/core/interface/EntityLoaderOptions.md)

### [**](#entitymanagertype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L41)EntityManagerType

Re-exports

<!-- -->

[EntityManagerType](https://mikro-orm.io/api/core.md#EntityManagerType)

### [**](#entitymetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L6)EntityMetadata

Re-exports

<!-- -->

[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)

### [**](#entitymetadatawithproperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1175)EntityMetadataWithProperties

Re-exports

<!-- -->

[EntityMetadataWithProperties](https://mikro-orm.io/api/core/interface/EntityMetadataWithProperties.md)

### [**](#entityname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L13)EntityName

Re-exports

<!-- -->

[EntityName](https://mikro-orm.io/api/core.md#EntityName)

### [**](#entityoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L23)EntityOptions

Re-exports

<!-- -->

[EntityOptions](https://mikro-orm.io/api/core.md#EntityOptions)

### [**](#entityproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L31)EntityProperty

Re-exports

<!-- -->

[EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)

### [**](#entityprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L85)EntityProps

Re-exports

<!-- -->

[EntityProps](https://mikro-orm.io/api/core.md#EntityProps)

### [**](#entityref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L71)EntityRef

Re-exports

<!-- -->

[EntityRef](https://mikro-orm.io/api/core.md#EntityRef)

### [**](#entityrepository)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/index.ts#L19)EntityRepository

Re-exports

<!-- -->

[EntityRepository](https://mikro-orm.io/api/sql/class/EntityRepository.md)

### [**](#entityrepositorytype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L8)EntityRepositoryType

Re-exports

<!-- -->

[EntityRepositoryType](https://mikro-orm.io/api/core.md#EntityRepositoryType)

### [**](#entityserializer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L71)EntitySerializer

Re-exports

<!-- -->

[EntitySerializer](https://mikro-orm.io/api/core/class/EntitySerializer.md)

### [**](#entityschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L71)EntitySchema

Re-exports

<!-- -->

[EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)

### [**](#entityschemametadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L58)EntitySchemaMetadata

Re-exports

<!-- -->

[EntitySchemaMetadata](https://mikro-orm.io/api/core.md#EntitySchemaMetadata)

### [**](#entityschemaproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L47)EntitySchemaProperty

Re-exports

<!-- -->

[EntitySchemaProperty](https://mikro-orm.io/api/core.md#EntitySchemaProperty)

### [**](#entityschemawithmeta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L111)EntitySchemaWithMeta

Re-exports

<!-- -->

[EntitySchemaWithMeta](https://mikro-orm.io/api/core/interface/EntitySchemaWithMeta.md)

### [**](#entitytransformer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntityTransformer.ts#L32)EntityTransformer

Re-exports

<!-- -->

[EntityTransformer](https://mikro-orm.io/api/core/class/EntityTransformer.md)

### [**](#entitytype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L81)EntityType

Re-exports

<!-- -->

[EntityType](https://mikro-orm.io/api/core.md#EntityType)

### [**](#entityvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L78)EntityValue

Re-exports

<!-- -->

[EntityValue](https://mikro-orm.io/api/core.md#EntityValue)

### [**](#enumarraytype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L37)EnumArrayType

Re-exports

<!-- -->

[EnumArrayType](https://mikro-orm.io/api/core/class/EnumArrayType.md)

### [**](#enumoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L651)EnumOptions

Re-exports

<!-- -->

[EnumOptions](https://mikro-orm.io/api/core/interface/EnumOptions.md)

### [**](#enumtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L38)EnumType

Re-exports

<!-- -->

[EnumType](https://mikro-orm.io/api/core/class/EnumType.md)

### [**](#equals)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L137)equals

Re-exports

<!-- -->

[equals](https://mikro-orm.io/api/core/function/equals.md)

### [**](#eventargs)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L7)EventArgs

Re-exports

<!-- -->

[EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)

### [**](#eventmanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L6)EventManager

Re-exports

<!-- -->

[EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

### [**](#eventsubscriber)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L23)EventSubscriber

Re-exports

<!-- -->

[EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)

### [**](#eventtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L171)EventType

Re-exports

<!-- -->

[EventType](https://mikro-orm.io/api/core/enum/EventType.md)

### [**](#eventtypemap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L193)EventTypeMap

Re-exports

<!-- -->

[EventTypeMap](https://mikro-orm.io/api/core.md#EventTypeMap)

### [**](#exceptionconverter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/ExceptionConverter.ts#L4)ExceptionConverter

Re-exports

<!-- -->

[ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#executeoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L66)ExecuteOptions

Re-exports

<!-- -->

[ExecuteOptions](https://mikro-orm.io/api/sql/interface/ExecuteOptions.md)

### [**](#expandhint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L91)ExpandHint

Re-exports

<!-- -->

[ExpandHint](https://mikro-orm.io/api/core.md#ExpandHint)

### [**](#expandproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L86)ExpandProperty

Re-exports

<!-- -->

[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)

### [**](#expandquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L89)ExpandQuery

Re-exports

<!-- -->

[ExpandQuery](https://mikro-orm.io/api/core.md#ExpandQuery)

### [**](#expandscalar)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L87)ExpandScalar

Re-exports

<!-- -->

[ExpandScalar](https://mikro-orm.io/api/core.md#ExpandScalar)

### [**](#factoryoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L29)FactoryOptions

Re-exports

<!-- -->

[FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md)

### [**](#field)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L297)Field

Re-exports

<!-- -->

[Field](https://mikro-orm.io/api/sql.md#Field)

### [**](#filterdef)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L115)FilterDef

Re-exports

<!-- -->

[FilterDef](https://mikro-orm.io/api/core.md#FilterDef)

### [**](#filteritemvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L88)FilterItemValue

Re-exports

<!-- -->

[FilterItemValue](https://mikro-orm.io/api/core.md#FilterItemValue)

### [**](#filterkey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L80)FilterKey

Re-exports

<!-- -->

[FilterKey](https://mikro-orm.io/api/core.md#FilterKey)

### [**](#filterobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L54)FilterObject

Re-exports

<!-- -->

[FilterObject](https://mikro-orm.io/api/core.md#FilterObject)

### [**](#filteroptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L219)FilterOptions

Re-exports

<!-- -->

[FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#filterquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L23)FilterQuery

Re-exports

<!-- -->

[FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)

### [**](#filtervalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L92)FilterValue

Re-exports

<!-- -->

[FilterValue](https://mikro-orm.io/api/core.md#FilterValue)

### [**](#findalloptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L189)FindAllOptions

Re-exports

<!-- -->

[FindAllOptions](https://mikro-orm.io/api/core/interface/FindAllOptions.md)

### [**](#findbycursoroptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L348)FindByCursorOptions

Re-exports

<!-- -->

[FindByCursorOptions](https://mikro-orm.io/api/core/interface/FindByCursorOptions.md)

### [**](#findoneoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L358)FindOneOptions

Re-exports

<!-- -->

[FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)

### [**](#findoneorfailoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L368)FindOneOrFailOptions

Re-exports

<!-- -->

[FindOneOrFailOptions](https://mikro-orm.io/api/core/interface/FindOneOrFailOptions.md)

### [**](#findoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L232)FindOptions

Re-exports

<!-- -->

[FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)

### [**](#flatqueryordermap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L88)FlatQueryOrderMap

Re-exports

<!-- -->

[FlatQueryOrderMap](https://mikro-orm.io/api/core/interface/FlatQueryOrderMap.md)

### [**](#floattype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L44)FloatType

Re-exports

<!-- -->

[FloatType](https://mikro-orm.io/api/core/class/FloatType.md)

### [**](#flusheventargs)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L14)FlushEventArgs

Re-exports

<!-- -->

[FlushEventArgs](https://mikro-orm.io/api/core/interface/FlushEventArgs.md)

### [**](#flushmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L5)FlushMode

Re-exports

<!-- -->

[FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

### [**](#foreignkey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L82)ForeignKey

Re-exports

<!-- -->

[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)

### [**](#foreignkeyconstraintviolationexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L70)ForeignKeyConstraintViolationException

Re-exports

<!-- -->

[ForeignKeyConstraintViolationException](https://mikro-orm.io/api/core/class/ForeignKeyConstraintViolationException.md)

### [**](#forkoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2837)ForkOptions

Re-exports

<!-- -->

[ForkOptions](https://mikro-orm.io/api/core/interface/ForkOptions.md)

### [**](#formulacallback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L63)FormulaCallback

Re-exports

<!-- -->

[FormulaCallback](https://mikro-orm.io/api/core.md#FormulaCallback)

### [**](#formulatable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L64)FormulaTable

Re-exports

<!-- -->

[FormulaTable](https://mikro-orm.io/api/core.md#FormulaTable)

### [**](#fromentitytype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L82)FromEntityType

Re-exports

<!-- -->

[FromEntityType](https://mikro-orm.io/api/core.md#FromEntityType)

### [**](#fulltexttype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/FullTextType.ts#L13)FullTextType

Re-exports

<!-- -->

[FullTextType](https://mikro-orm.io/api/sql/class/FullTextType.md)

### [**](#generatedcacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/GeneratedCacheAdapter.ts#L4)GeneratedCacheAdapter

Re-exports

<!-- -->

[GeneratedCacheAdapter](https://mikro-orm.io/api/core/class/GeneratedCacheAdapter.md)

### [**](#generatedcolumncallback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L114)GeneratedColumnCallback

Re-exports

<!-- -->

[GeneratedColumnCallback](https://mikro-orm.io/api/core.md#GeneratedColumnCallback)

### [**](#generateoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L53)GenerateOptions

Re-exports

<!-- -->

[GenerateOptions](https://mikro-orm.io/api/core/interface/GenerateOptions.md)

### [**](#getkyselyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/SqlEntityManager.ts#L23)GetKyselyOptions

Re-exports

<!-- -->

[GetKyselyOptions](https://mikro-orm.io/api/sql/interface/GetKyselyOptions.md)

### [**](#getreferenceoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L500)GetReferenceOptions

Re-exports

<!-- -->

[GetReferenceOptions](https://mikro-orm.io/api/core/interface/GetReferenceOptions.md)

### [**](#getrepository)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L41)GetRepository

Re-exports

<!-- -->

[GetRepository](https://mikro-orm.io/api/core.md#GetRepository)

### [**](#groupoperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L24)GroupOperator

Re-exports

<!-- -->

[GroupOperator](https://mikro-orm.io/api/core/enum/GroupOperator.md)

### [**](#hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L110)Hidden

Re-exports

<!-- -->

[Hidden](https://mikro-orm.io/api/core.md#Hidden)

### [**](#hiddenprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L11)HiddenProps

Re-exports

<!-- -->

[HiddenProps](https://mikro-orm.io/api/core.md#HiddenProps)

### [**](#highlighter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L27)Highlighter

Re-exports

<!-- -->

[Highlighter](https://mikro-orm.io/api/core/interface/Highlighter.md)

### [**](#hydrator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/hydration/Hydrator.ts#L8)Hydrator

Re-exports

<!-- -->

[Hydrator](https://mikro-orm.io/api/core/class/Hydrator.md)

### [**](#changeset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L6)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L66)ChangeSet

Re-exports

<!-- -->

[ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)

### [**](#changesetcomputer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetComputer.ts#L17)ChangeSetComputer

Re-exports

<!-- -->

[ChangeSetComputer](https://mikro-orm.io/api/core/class/ChangeSetComputer.md)

### [**](#changesetpersister)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetPersister.ts#L31)ChangeSetPersister

Re-exports

<!-- -->

[ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

### [**](#changesettype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L79)ChangeSetType

Re-exports

<!-- -->

[ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)

### [**](#charactertype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L53)CharacterType

Re-exports

<!-- -->

[CharacterType](https://mikro-orm.io/api/core/class/CharacterType.md)

### [**](#checkcallback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L61)CheckCallback

Re-exports

<!-- -->

[CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)

### [**](#checkconstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L113)CheckConstraint

Re-exports

<!-- -->

[CheckConstraint](https://mikro-orm.io/api/core/interface/CheckConstraint.md)

### [**](#checkconstraintviolationexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L75)CheckConstraintViolationException

Re-exports

<!-- -->

[CheckConstraintViolationException](https://mikro-orm.io/api/core/class/CheckConstraintViolationException.md)

### [**](#checkdef)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L129)CheckDef

Re-exports

<!-- -->

[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)

### [**](#iconfiguration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L9)IConfiguration

Re-exports

<!-- -->

[IConfiguration](https://mikro-orm.io/api/core/interface/IConfiguration.md)

### [**](#icriterianode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L248)ICriteriaNode

Re-exports

<!-- -->

[ICriteriaNode](https://mikro-orm.io/api/sql/interface/ICriteriaNode.md)

### [**](#icriterianodeprocessoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L238)ICriteriaNodeProcessOptions

Re-exports

<!-- -->

[ICriteriaNodeProcessOptions](https://mikro-orm.io/api/sql/interface/ICriteriaNodeProcessOptions.md)

### [**](#idatabasedriver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L43)IDatabaseDriver

Re-exports

<!-- -->

[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)

### [**](#identitymap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L3)IdentityMap

Re-exports

<!-- -->

[IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

### [**](#ientitygenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L56)IEntityGenerator

Re-exports

<!-- -->

[IEntityGenerator](https://mikro-orm.io/api/core/interface/IEntityGenerator.md)

### [**](#imigrationgenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L39)IMigrationGenerator

Re-exports

<!-- -->

[IMigrationGenerator](https://mikro-orm.io/api/core/interface/IMigrationGenerator.md)

### [**](#imigrator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L38)IMigrator

Re-exports

<!-- -->

[IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#importsresolver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L106)ImportsResolver

Re-exports

<!-- -->

[ImportsResolver](https://mikro-orm.io/api/core.md#ImportsResolver)

### [**](#indexcallback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L62)IndexCallback

Re-exports

<!-- -->

[IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)

### [**](#indexcolumnoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L668)IndexColumnOptions

Re-exports

<!-- -->

[IndexColumnOptions](https://mikro-orm.io/api/core/interface/IndexColumnOptions.md)

### [**](#indexdef)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L93)IndexDef

Re-exports

<!-- -->

[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

### [**](#indexoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L712)IndexOptions

Re-exports

<!-- -->

[IndexOptions](https://mikro-orm.io/api/core/interface/IndexOptions.md)

### [**](#inferclassentitydb)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L398)InferClassEntityDB

Re-exports

<!-- -->

[InferClassEntityDB](https://mikro-orm.io/api/sql.md#InferClassEntityDB)

### [**](#inferdbfromkysely)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L275)InferDBFromKysely

Re-exports

<!-- -->

[InferDBFromKysely](https://mikro-orm.io/api/sql.md#InferDBFromKysely)

### [**](#inferentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L112)InferEntity

Re-exports

<!-- -->

[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)

### [**](#inferentityfromproperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1419)InferEntityFromProperties

Re-exports

<!-- -->

[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)

### [**](#inferentityname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L25)InferEntityName

Re-exports

<!-- -->

[InferEntityName](https://mikro-orm.io/api/core.md#InferEntityName)

### [**](#inferentityproperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L267)InferEntityProperties

Re-exports

<!-- -->

[InferEntityProperties](https://mikro-orm.io/api/sql.md#InferEntityProperties)

### [**](#inferkyselydb)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L270)InferKyselyDB

Re-exports

<!-- -->

[InferKyselyDB](https://mikro-orm.io/api/sql.md#InferKyselyDB)

### [**](#inferkyselytable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L301)InferKyselyTable

Re-exports

<!-- -->

[InferKyselyTable](https://mikro-orm.io/api/sql.md#InferKyselyTable)

### [**](#inferprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1468)InferPrimaryKey

Re-exports

<!-- -->

[InferPrimaryKey](https://mikro-orm.io/api/core.md#InferPrimaryKey)

### [**](#initcollectionoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L984)InitCollectionOptions

Re-exports

<!-- -->

[InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)

### [**](#insertquerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4179)InsertQueryBuilder

Re-exports

<!-- -->

[InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)

### [**](#integertype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L40)IntegerType

Re-exports

<!-- -->

[IntegerType](https://mikro-orm.io/api/core/class/IntegerType.md)

### [**](#intervaltype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L52)IntervalType

Re-exports

<!-- -->

[IntervalType](https://mikro-orm.io/api/core/class/IntervalType.md)

### [**](#invalidfieldnameexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L80)InvalidFieldNameException

Re-exports

<!-- -->

[InvalidFieldNameException](https://mikro-orm.io/api/core/class/InvalidFieldNameException.md)

### [**](#iprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L21)IPrimaryKey

Re-exports

<!-- -->

[IPrimaryKey](https://mikro-orm.io/api/core.md#IPrimaryKey)

### [**](#iquerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L189)IQueryBuilder

Re-exports

<!-- -->

[IQueryBuilder](https://mikro-orm.io/api/sql/interface/IQueryBuilder.md)

### [**](#iseedmanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L57)ISeedManager

Re-exports

<!-- -->

[ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

### [**](#ischemagenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L72)ISchemaGenerator

Re-exports

<!-- -->

[ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

### [**](#isolationlevel)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L163)IsolationLevel

Re-exports

<!-- -->

[IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

### [**](#israw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L105)isRaw

Re-exports

<!-- -->

[isRaw](https://mikro-orm.io/api/core/function/isRaw.md)

### [**](#issubset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L84)IsSubset

Re-exports

<!-- -->

[IsSubset](https://mikro-orm.io/api/core.md#IsSubset)

### [**](#isunknown)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L46)IsUnknown

Re-exports

<!-- -->

[IsUnknown](https://mikro-orm.io/api/core.md#IsUnknown)

### [**](#itype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L27)IType

Re-exports

<!-- -->

[IType](https://mikro-orm.io/api/core.md#IType)

### [**](#iwrappedentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L24)IWrappedEntity

Re-exports

<!-- -->

[IWrappedEntity](https://mikro-orm.io/api/core/interface/IWrappedEntity.md)

### [**](#joinoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L38)JoinOptions

Re-exports

<!-- -->

[JoinOptions](https://mikro-orm.io/api/sql/interface/JoinOptions.md)

### [**](#joinselectfield)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L217)JoinSelectField

Re-exports

<!-- -->

[JoinSelectField](https://mikro-orm.io/api/sql.md#JoinSelectField)

### [**](#jointype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/enums.ts#L14)JoinType

Re-exports

<!-- -->

[JoinType](https://mikro-orm.io/api/sql/enum/JoinType.md)

### [**](#json_key_operators)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L59)JSON\_KEY\_OPERATORS

Re-exports

<!-- -->

[JSON\_KEY\_OPERATORS](https://mikro-orm.io/api/core.md#JSON_KEY_OPERATORS)

### [**](#jsonproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L55)JsonProperty

Re-exports

<!-- -->

[JsonProperty](https://mikro-orm.io/api/core.md#JsonProperty)

### [**](#jsontype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L39)JsonType

Re-exports

<!-- -->

[JsonType](https://mikro-orm.io/api/core/class/JsonType.md)

### [**](#kysely)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/index.ts#L5)Kysely

Re-exports

<!-- -->

[Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)

### [**](#loadcountoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L995)LoadCountOptions

Re-exports

<!-- -->

[LoadCountOptions](https://mikro-orm.io/api/core/interface/LoadCountOptions.md)

### [**](#loaded)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L34)Loaded

Re-exports

<!-- -->

[Loaded](https://mikro-orm.io/api/core.md#Loaded)

### [**](#loadedcollection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L37)LoadedCollection

Re-exports

<!-- -->

[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)

### [**](#loadedreference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L36)LoadedReference

Re-exports

<!-- -->

[LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)

### [**](#loadhint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L221)LoadHint

Re-exports

<!-- -->

[LoadHint](https://mikro-orm.io/api/core/interface/LoadHint.md)

### [**](#loadreferenceoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L358)LoadReferenceOptions

Re-exports

<!-- -->

[LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)

### [**](#loadreferenceorfailoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L367)LoadReferenceOrFailOptions

Re-exports

<!-- -->

[LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)

### [**](#loadstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L139)LoadStrategy

Re-exports

<!-- -->

[LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md)

### [**](#lockmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L152)LockMode

Re-exports

<!-- -->

[LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)

### [**](#lockoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L476)LockOptions

Re-exports

<!-- -->

[LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

### [**](#lockwaittimeoutexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L85)LockWaitTimeoutException

Re-exports

<!-- -->

[LockWaitTimeoutException](https://mikro-orm.io/api/core/class/LockWaitTimeoutException.md)

### [**](#logcontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L34)LogContext

Re-exports

<!-- -->

[LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

### [**](#logger)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L3)Logger

Re-exports

<!-- -->

[Logger](https://mikro-orm.io/api/core/interface/Logger.md)

### [**](#loggernamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L32)LoggerNamespace

Re-exports

<!-- -->

[LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

### [**](#loggeroptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L51)LoggerOptions

Re-exports

<!-- -->

[LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

### [**](#loggingoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L68)LoggingOptions

Re-exports

<!-- -->

[LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#manytomanyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L575)ManyToManyOptions

Re-exports

<!-- -->

[ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)

### [**](#manytooneoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L457)ManyToOneOptions

Re-exports

<!-- -->

[ManyToOneOptions](https://mikro-orm.io/api/core/interface/ManyToOneOptions.md)

### [**](#maptablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L285)MapTableName

Re-exports

<!-- -->

[MapTableName](https://mikro-orm.io/api/sql.md#MapTableName)

### [**](#mapvalueastable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L294)MapValueAsTable

Re-exports

<!-- -->

[MapValueAsTable](https://mikro-orm.io/api/sql.md#MapValueAsTable)

### [**](#matchingoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L28)MatchingOptions

Re-exports

<!-- -->

[MatchingOptions](https://mikro-orm.io/api/core/interface/MatchingOptions.md)

### [**](#maybepromise)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L28)MaybePromise

Re-exports

<!-- -->

[MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)

### [**](#maybereturntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L265)MaybeReturnType

Re-exports

<!-- -->

[MaybeReturnType](https://mikro-orm.io/api/sql.md#MaybeReturnType)

### [**](#mediuminttype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L43)MediumIntType

Re-exports

<!-- -->

[MediumIntType](https://mikro-orm.io/api/core/class/MediumIntType.md)

### [**](#memorycacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/MemoryCacheAdapter.ts#L3)MemoryCacheAdapter

Re-exports

<!-- -->

[MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md)

### [**](#mergeloaded)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L93)MergeLoaded

Re-exports

<!-- -->

[MergeLoaded](https://mikro-orm.io/api/core.md#MergeLoaded)

### [**](#mergeoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2828)MergeOptions

Re-exports

<!-- -->

[MergeOptions](https://mikro-orm.io/api/core/interface/MergeOptions.md)

### [**](#mergeselected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L94)MergeSelected

Re-exports

<!-- -->

[MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)

### [**](#metadatadiscovery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataDiscovery.ts#L29)MetadataDiscovery

Re-exports

<!-- -->

[MetadataDiscovery](https://mikro-orm.io/api/core/class/MetadataDiscovery.md)

### [**](#metadatadiscoveryoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L704)MetadataDiscoveryOptions

Re-exports

<!-- -->

[MetadataDiscoveryOptions](https://mikro-orm.io/api/core/interface/MetadataDiscoveryOptions.md)

### [**](#metadataerror)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/errors.ts#L230)MetadataError

Re-exports

<!-- -->

[MetadataError](https://mikro-orm.io/api/core/class/MetadataError.md)

### [**](#metadataprocessor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L105)MetadataProcessor

Re-exports

<!-- -->

[MetadataProcessor](https://mikro-orm.io/api/core.md#MetadataProcessor)

### [**](#metadataprovider)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L16)MetadataProvider

Re-exports

<!-- -->

[MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

### [**](#metadatastorage)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L15)MetadataStorage

Re-exports

<!-- -->

[MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#migrateoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L74)MigrateOptions

Re-exports

<!-- -->

[MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions)

### [**](#migrationdiff)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L52)MigrationDiff

Re-exports

<!-- -->

[MigrationDiff](https://mikro-orm.io/api/core/interface/MigrationDiff.md)

### [**](#migrationinfo)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L73)MigrationInfo

Re-exports

<!-- -->

[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)

### [**](#migrationobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L42)MigrationObject

Re-exports

<!-- -->

[MigrationObject](https://mikro-orm.io/api/core/interface/MigrationObject.md)

### [**](#migrationresult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L75)MigrationResult

Re-exports

<!-- -->

[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)

### [**](#migrationrow)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L76)MigrationRow

Re-exports

<!-- -->

[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)

### [**](#migrationsoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L574)MigrationsOptions

Re-exports

<!-- -->

[MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

### [**](#migratorevent)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L40)MigratorEvent

Re-exports

<!-- -->

[MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)

### [**](#mikrokyselyplugin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L58)MikroKyselyPlugin

Re-exports

<!-- -->

[MikroKyselyPlugin](https://mikro-orm.io/api/sql/class/MikroKyselyPlugin.md)

### [**](#mikrokyselypluginoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L25)MikroKyselyPluginOptions

Re-exports

<!-- -->

[MikroKyselyPluginOptions](https://mikro-orm.io/api/sql/interface/MikroKyselyPluginOptions.md)

### [**](#modifycontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L161)ModifyContext

Re-exports

<!-- -->

[ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)

### [**](#modifyfields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L237)ModifyFields

Re-exports

<!-- -->

[ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)

### [**](#modifyhint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L155)ModifyHint

Re-exports

<!-- -->

[ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)

### [**](#mongonamingstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/MongoNamingStrategy.ts#L3)MongoNamingStrategy

Re-exports

<!-- -->

[MongoNamingStrategy](https://mikro-orm.io/api/core/class/MongoNamingStrategy.md)

### [**](#mysqlschemahelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L8)MySqlSchemaHelper

Re-exports

<!-- -->

[MySqlSchemaHelper](https://mikro-orm.io/api/sql/class/MySqlSchemaHelper.md)

### [**](#namingstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L3)NamingStrategy

Re-exports

<!-- -->

[NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#nativedeleteoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L466)NativeDeleteOptions

Re-exports

<!-- -->

[NativeDeleteOptions](https://mikro-orm.io/api/core/interface/NativeDeleteOptions.md)

### [**](#nativeinsertupdatemanyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L394)NativeInsertUpdateManyOptions

Re-exports

<!-- -->

[NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)

### [**](#nativeinsertupdateoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L378)NativeInsertUpdateOptions

Re-exports

<!-- -->

[NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)

### [**](#new)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L35)New

Re-exports

<!-- -->

[New](https://mikro-orm.io/api/core.md#New)

### [**](#node)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/CommitOrderCalculator.ts#L12)Node

Re-exports

<!-- -->

[Node](https://mikro-orm.io/api/core/interface/Node.md)

### [**](#nodesqlitedialect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/sqlite/NodeSqliteDialect.ts#L20)NodeSqliteDialect

Re-exports

<!-- -->

[NodeSqliteDialect](https://mikro-orm.io/api/sql/class/NodeSqliteDialect.md)

### [**](#nodestate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/CommitOrderCalculator.ts#L4)NodeState

Re-exports

<!-- -->

[NodeState](https://mikro-orm.io/api/core/enum/NodeState.md)

### [**](#nonuniquefieldnameexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L90)NonUniqueFieldNameException

Re-exports

<!-- -->

[NonUniqueFieldNameException](https://mikro-orm.io/api/core/class/NonUniqueFieldNameException.md)

### [**](#notfounderror)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/errors.ts#L456)NotFoundError

Re-exports

<!-- -->

[NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)

### [**](#notnullconstraintviolationexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L95)NotNullConstraintViolationException

Re-exports

<!-- -->

[NotNullConstraintViolationException](https://mikro-orm.io/api/core/class/NotNullConstraintViolationException.md)

### [**](#nullcacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/NullCacheAdapter.ts#L3)NullCacheAdapter

Re-exports

<!-- -->

[NullCacheAdapter](https://mikro-orm.io/api/core/class/NullCacheAdapter.md)

### [**](#nullhighlighter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/NullHighlighter.ts#L3)NullHighlighter

Re-exports

<!-- -->

[NullHighlighter](https://mikro-orm.io/api/core/class/NullHighlighter.md)

### [**](#objecthydrator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/hydration/ObjectHydrator.ts#L23)ObjectHydrator

Re-exports

<!-- -->

[ObjectHydrator](https://mikro-orm.io/api/core/class/ObjectHydrator.md)

### [**](#objectquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L22)ObjectQuery

Re-exports

<!-- -->

[ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)

### [**](#onconflictclause)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1518)OnConflictClause

Re-exports

<!-- -->

[OnConflictClause](https://mikro-orm.io/api/sql/interface/OnConflictClause.md)

### [**](#onetomanyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L504)OneToManyOptions

Re-exports

<!-- -->

[OneToManyOptions](https://mikro-orm.io/api/core/interface/OneToManyOptions.md)

### [**](#onetooneoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L536)OneToOneOptions

Re-exports

<!-- -->

[OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)

### [**](#opt)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L109)Opt

Re-exports

<!-- -->

[Opt](https://mikro-orm.io/api/core.md#Opt)

### [**](#optimisticlockerror)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/errors.ts#L203)OptimisticLockError

Re-exports

<!-- -->

[OptimisticLockError](https://mikro-orm.io/api/core/class/OptimisticLockError.md)

### [**](#optionalprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L9)OptionalProps

Re-exports

<!-- -->

[OptionalProps](https://mikro-orm.io/api/core.md#OptionalProps)

### [**](#oracledialect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L246)OracleDialect

Re-exports

<!-- -->

[OracleDialect](https://mikro-orm.io/api/sql/class/OracleDialect.md)

### [**](#oracledialectconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L241)OracleDialectConfig

Re-exports

<!-- -->

[OracleDialectConfig](https://mikro-orm.io/api/sql/interface/OracleDialectConfig.md)

### [**](#oraclepool)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L26)OraclePool

Re-exports

<!-- -->

[OraclePool](https://mikro-orm.io/api/sql/interface/OraclePool.md)

### [**](#oraclepoolconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L34)OraclePoolConnection

Re-exports

<!-- -->

[OraclePoolConnection](https://mikro-orm.io/api/sql/interface/OraclePoolConnection.md)

### [**](#orderdefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L187)OrderDefinition

Re-exports

<!-- -->

[OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)

### [**](#p)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1314)p

Re-exports

<!-- -->

[p](https://mikro-orm.io/api/core.md#p)

### [**](#parsejsonsafe)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L159)parseJsonSafe

Re-exports

<!-- -->

[parseJsonSafe](https://mikro-orm.io/api/core/function/parseJsonSafe.md)

### [**](#plainobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L230)PlainObject

Re-exports

<!-- -->

[PlainObject](https://mikro-orm.io/api/core/class/PlainObject.md)

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L57)Platform

Re-exports

<!-- -->

[Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#polymorphicref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/PolymorphicRef.ts#L8)PolymorphicRef

Re-exports

<!-- -->

[PolymorphicRef](https://mikro-orm.io/api/core/class/PolymorphicRef.md)

### [**](#poolconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L691)PoolConfig

Re-exports

<!-- -->

[PoolConfig](https://mikro-orm.io/api/core/interface/PoolConfig.md)

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L33)Populate

Re-exports

<!-- -->

[Populate](https://mikro-orm.io/api/core.md#Populate)

### [**](#populatehint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L14)PopulateHint

Re-exports

<!-- -->

[PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md)

### [**](#populatehintoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L118)PopulateHintOptions

Re-exports

<!-- -->

[PopulateHintOptions](https://mikro-orm.io/api/core.md#PopulateHintOptions)

### [**](#populateoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L32)PopulateOptions

Re-exports

<!-- -->

[PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)

### [**](#populatepath)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L19)PopulatePath

Re-exports

<!-- -->

[PopulatePath](https://mikro-orm.io/api/core/enum/PopulatePath.md)

### [**](#postgresqlschemahelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts#L19)PostgreSqlSchemaHelper

Re-exports

<!-- -->

[PostgreSqlSchemaHelper](https://mikro-orm.io/api/sql/class/PostgreSqlSchemaHelper.md)

### [**](#prefixes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L119)Prefixes

Re-exports

<!-- -->

[Prefixes](https://mikro-orm.io/api/core.md#Prefixes)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L20)Primary

Re-exports

<!-- -->

[Primary](https://mikro-orm.io/api/core.md#Primary)

### [**](#primarykeyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L658)PrimaryKeyOptions

Re-exports

<!-- -->

[PrimaryKeyOptions](https://mikro-orm.io/api/core/interface/PrimaryKeyOptions.md)

### [**](#primarykeyprop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L7)PrimaryKeyProp

Re-exports

<!-- -->

[PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)

### [**](#propertybuilders)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1098)PropertyBuilders

Re-exports

<!-- -->

[PropertyBuilders](https://mikro-orm.io/api/core.md#PropertyBuilders)

### [**](#propertychain)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L90)PropertyChain

Re-exports

<!-- -->

[PropertyChain](https://mikro-orm.io/api/core/interface/PropertyChain.md)

### [**](#propertyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L83)PropertyOptions

Re-exports

<!-- -->

[PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)

### [**](#qbfield)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L278)QBField

Re-exports

<!-- -->

[QBField](https://mikro-orm.io/api/sql.md#QBField)

### [**](#qbfilterquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L479)QBFilterQuery

Re-exports

<!-- -->

[QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)

### [**](#qbstreamoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L71)QBStreamOptions

Re-exports

<!-- -->

[QBStreamOptions](https://mikro-orm.io/api/sql/interface/QBStreamOptions.md)

### [**](#querybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L557)QueryBuilder

Re-exports

<!-- -->

[QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)

### [**](#queryflag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L92)QueryFlag

Re-exports

<!-- -->

[QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

### [**](#queryoperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L29)QueryOperator

Re-exports

<!-- -->

[QueryOperator](https://mikro-orm.io/api/core/enum/QueryOperator.md)

### [**](#queryorder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L61)QueryOrder

Re-exports

<!-- -->

[QueryOrder](https://mikro-orm.io/api/core/enum/QueryOrder.md)

### [**](#queryorderkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L82)QueryOrderKeys

Re-exports

<!-- -->

[QueryOrderKeys](https://mikro-orm.io/api/core.md#QueryOrderKeys)

### [**](#queryorderkeysflat)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L81)QueryOrderKeysFlat

Re-exports

<!-- -->

[QueryOrderKeysFlat](https://mikro-orm.io/api/core.md#QueryOrderKeysFlat)

### [**](#queryordermap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L84)QueryOrderMap

Re-exports

<!-- -->

[QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)

### [**](#queryordernumeric)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L76)QueryOrderNumeric

Re-exports

<!-- -->

[QueryOrderNumeric](https://mikro-orm.io/api/core/enum/QueryOrderNumeric.md)

### [**](#queryresult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L244)QueryResult

Re-exports

<!-- -->

[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)

### [**](#querytype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/enums.ts#L1)QueryType

Re-exports

<!-- -->

[QueryType](https://mikro-orm.io/api/sql/enum/QueryType.md)

### [**](#quote)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L261)quote

Re-exports

<!-- -->

[quote](https://mikro-orm.io/api/core/function/quote.md)

### [**](#raw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L99)Raw

Re-exports

<!-- -->

[Raw](https://mikro-orm.io/api/core.md#Raw)

### [**](#rawqueryfragment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L10)RawQueryFragment

Re-exports

<!-- -->

[RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

### [**](#rawqueryfragmentsymbol)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L6)RawQueryFragmentSymbol

Re-exports

<!-- -->

[RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol)

### [**](#readonlyexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L100)ReadOnlyException

Re-exports

<!-- -->

[ReadOnlyException](https://mikro-orm.io/api/core/class/ReadOnlyException.md)

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L379)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L386)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L394)ref

Re-exports

<!-- -->

[ref](https://mikro-orm.io/api/core/function/ref.md)

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L69)Ref

Re-exports

<!-- -->

[Ref](https://mikro-orm.io/api/core.md#Ref)

### [**](#reference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L22)Reference

Re-exports

<!-- -->

[Reference](https://mikro-orm.io/api/core/class/Reference.md)

### [**](#referencekind)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L118)ReferenceKind

Re-exports

<!-- -->

[ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

### [**](#referenceoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L363)ReferenceOptions

Re-exports

<!-- -->

[ReferenceOptions](https://mikro-orm.io/api/core/interface/ReferenceOptions.md)

### [**](#refreshdatabaseoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L102)RefreshDatabaseOptions

Re-exports

<!-- -->

[RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

### [**](#registeroptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L1608)RegisterOptions

Re-exports

<!-- -->

[RegisterOptions](https://mikro-orm.io/api/core/interface/RegisterOptions.md)

### [**](#rel)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L424)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L429)rel

Re-exports

<!-- -->

[rel](https://mikro-orm.io/api/core/function/rel.md)

### [**](#rel)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L68)Rel

Re-exports

<!-- -->

[Rel](https://mikro-orm.io/api/core.md#Rel)

### [**](#requestcontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L8)RequestContext

Re-exports

<!-- -->

[RequestContext](https://mikro-orm.io/api/core/class/RequestContext.md)

### [**](#requiredentitydata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L60)RequiredEntityData

Re-exports

<!-- -->

[RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)

### [**](#requirednullable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L107)RequiredNullable

Re-exports

<!-- -->

[RequiredNullable](https://mikro-orm.io/api/core.md#RequiredNullable)

### [**](#runquerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4079)RunQueryBuilder

Re-exports

<!-- -->

[RunQueryBuilder](https://mikro-orm.io/api/sql/interface/RunQueryBuilder.md)

### [**](#scalar)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L90)Scalar

Re-exports

<!-- -->

[Scalar](https://mikro-orm.io/api/core.md#Scalar)

### [**](#scalar_types)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L107)SCALAR\_TYPES

Re-exports

<!-- -->

[SCALAR\_TYPES](https://mikro-orm.io/api/core.md#SCALAR_TYPES)

### [**](#scalarref)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L70)ScalarRef

Re-exports

<!-- -->

[ScalarRef](https://mikro-orm.io/api/core.md#ScalarRef)

### [**](#scalarreference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L237)ScalarReference

Re-exports

<!-- -->

[ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)

### [**](#seederobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L58)SeederObject

Re-exports

<!-- -->

[SeederObject](https://mikro-orm.io/api/core/interface/SeederObject.md)

### [**](#seederoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L652)SeederOptions

Re-exports

<!-- -->

[SeederOptions](https://mikro-orm.io/api/core/interface/SeederOptions.md)

### [**](#selected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L83)Selected

Re-exports

<!-- -->

[Selected](https://mikro-orm.io/api/core.md#Selected)

### [**](#selectquerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4154)SelectQueryBuilder

Re-exports

<!-- -->

[SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)

### [**](#serializationcontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L10)SerializationContext

Re-exports

<!-- -->

[SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L389)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L414)serialize

Re-exports

<!-- -->

[serialize](https://mikro-orm.io/api/core/function/serialize.md)

### [**](#serializedprimarykeyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L660)SerializedPrimaryKeyOptions

Re-exports

<!-- -->

[SerializedPrimaryKeyOptions](https://mikro-orm.io/api/core/interface/SerializedPrimaryKeyOptions.md)

### [**](#serializedto)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L51)SerializeDTO

Re-exports

<!-- -->

[SerializeDTO](https://mikro-orm.io/api/core.md#SerializeDTO)

### [**](#serializeoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/EntitySerializer.ts#L351)SerializeOptions

Re-exports

<!-- -->

[SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)

### [**](#serverexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L37)ServerException

Re-exports

<!-- -->

[ServerException](https://mikro-orm.io/api/core/class/ServerException.md)

### [**](#schemacolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L66)SchemaColumns

Re-exports

<!-- -->

[SchemaColumns](https://mikro-orm.io/api/core.md#SchemaColumns)

### [**](#schemacomparator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L22)SchemaComparator

Re-exports

<!-- -->

[SchemaComparator](https://mikro-orm.io/api/sql/class/SchemaComparator.md)

### [**](#schemadifference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L174)SchemaDifference

Re-exports

<!-- -->

[SchemaDifference](https://mikro-orm.io/api/sql/interface/SchemaDifference.md)

### [**](#schemagenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L699)SchemaGenerator

Re-exports

<!-- -->

[SchemaGenerator](https://mikro-orm.io/api/sql.md#SchemaGenerator)

### [**](#schemahelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L8)SchemaHelper

Re-exports

<!-- -->

[SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

### [**](#schematable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L65)SchemaTable

Re-exports

<!-- -->

[SchemaTable](https://mikro-orm.io/api/core.md#SchemaTable)

### [**](#simplecolumnmeta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L67)SimpleColumnMeta

Re-exports

<!-- -->

[SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)

### [**](#simplelogger)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/SimpleLogger.ts#L7)SimpleLogger

Re-exports

<!-- -->

[SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

### [**](#smallinttype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L41)SmallIntType

Re-exports

<!-- -->

[SmallIntType](https://mikro-orm.io/api/core/class/SmallIntType.md)

### [**](#snakecase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L349)SnakeCase

Re-exports

<!-- -->

[SnakeCase](https://mikro-orm.io/api/sql.md#SnakeCase)

### [**](#sql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L224)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L239)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L241)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L243)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L245)sql

Re-exports

<!-- -->

[sql](https://mikro-orm.io/api/core/function/sql.md)

### [**](#sqlentitymanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/SqlEntityManager.ts#L30)SqlEntityManager

Renames and re-exports

<!-- -->

[EntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)

### [**](#sqlentityrepository)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/SqlEntityRepository.ts#L5)SqlEntityRepository

Renames and re-exports

<!-- -->

[EntityRepository](https://mikro-orm.io/api/sql/class/EntityRepository.md)

### [**](#sqlitedriver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/sqlite/SqliteDriver.ts#L12)SqliteDriver

Re-exports

<!-- -->

[SqliteDriver](https://mikro-orm.io/api/sql/class/SqliteDriver.md)

### [**](#sqliteplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/sqlite/SqlitePlatform.ts#L7)SqlitePlatform

Re-exports

<!-- -->

[SqlitePlatform](https://mikro-orm.io/api/sql/class/SqlitePlatform.md)

### [**](#sqliteschemahelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/sqlite/SqliteSchemaHelper.ts#L23)SqliteSchemaHelper

Re-exports

<!-- -->

[SqliteSchemaHelper](https://mikro-orm.io/api/sql/class/SqliteSchemaHelper.md)

### [**](#sqlschemagenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L25)SqlSchemaGenerator

Re-exports

<!-- -->

[SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

### [**](#streamoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L198)StreamOptions

Re-exports

<!-- -->

[StreamOptions](https://mikro-orm.io/api/core/interface/StreamOptions.md)

### [**](#stringtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L48)StringType

Re-exports

<!-- -->

[StringType](https://mikro-orm.io/api/core/class/StringType.md)

### [**](#subquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L117)Subquery

Re-exports

<!-- -->

[Subquery](https://mikro-orm.io/api/core/interface/Subquery.md)

### [**](#synccacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/CacheAdapter.ts#L28)SyncCacheAdapter

Re-exports

<!-- -->

[SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

### [**](#syntaxerrorexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L105)SyntaxErrorException

Re-exports

<!-- -->

[SyntaxErrorException](https://mikro-orm.io/api/core/class/SyntaxErrorException.md)

### [**](#t)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L83)t

Re-exports

<!-- -->

[t](https://mikro-orm.io/api/core.md#t)

### [**](#table)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L29)Table

Re-exports

<!-- -->

[Table](https://mikro-orm.io/api/sql/interface/Table.md)

### [**](#tabledifference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L143)TableDifference

Re-exports

<!-- -->

[TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

### [**](#tableexistsexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L110)TableExistsException

Re-exports

<!-- -->

[TableExistsException](https://mikro-orm.io/api/core/class/TableExistsException.md)

### [**](#tablenotfoundexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L115)TableNotFoundException

Re-exports

<!-- -->

[TableNotFoundException](https://mikro-orm.io/api/core/class/TableNotFoundException.md)

### [**](#tableoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/NativeQueryBuilder.ts#L51)TableOptions

Re-exports

<!-- -->

[TableOptions](https://mikro-orm.io/api/sql/interface/TableOptions.md)

### [**](#texttype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L50)TextType

Re-exports

<!-- -->

[TextType](https://mikro-orm.io/api/core/class/TextType.md)

### [**](#timetype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L31)TimeType

Re-exports

<!-- -->

[TimeType](https://mikro-orm.io/api/core/class/TimeType.md)

### [**](#tinyinttype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L42)TinyIntType

Re-exports

<!-- -->

[TinyIntType](https://mikro-orm.io/api/core/class/TinyIntType.md)

### [**](#transaction)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L261)Transaction

Re-exports

<!-- -->

[Transaction](https://mikro-orm.io/api/core.md#Transaction)

### [**](#transactioncontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/TransactionContext.ts#L4)TransactionContext

Re-exports

<!-- -->

[TransactionContext](https://mikro-orm.io/api/core/class/TransactionContext.md)

### [**](#transactioneventargs)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L18)TransactionEventArgs

Re-exports

<!-- -->

[TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

### [**](#transactioneventbroadcaster)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/TransactionEventBroadcaster.ts#L5)TransactionEventBroadcaster

Re-exports

<!-- -->

[TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

### [**](#transactioneventtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L201)TransactionEventType

Re-exports

<!-- -->

[TransactionEventType](https://mikro-orm.io/api/core.md#TransactionEventType)

### [**](#transactionmanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/TransactionManager.ts#L15)TransactionManager

Re-exports

<!-- -->

[TransactionManager](https://mikro-orm.io/api/core/class/TransactionManager.md)

### [**](#transactionoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L219)TransactionOptions

Re-exports

<!-- -->

[TransactionOptions](https://mikro-orm.io/api/core/interface/TransactionOptions.md)

### [**](#transactionpropagation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L209)TransactionPropagation

Re-exports

<!-- -->

[TransactionPropagation](https://mikro-orm.io/api/core/enum/TransactionPropagation.md)

### [**](#transactionstateerror)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/errors.ts#L473)TransactionStateError

Re-exports

<!-- -->

[TransactionStateError](https://mikro-orm.io/api/core/class/TransactionStateError.md)

### [**](#transformcontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L27)TransformContext

Re-exports

<!-- -->

[TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

### [**](#truncatequerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4197)TruncateQueryBuilder

Re-exports

<!-- -->

[TruncateQueryBuilder](https://mikro-orm.io/api/sql/interface/TruncateQueryBuilder.md)

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L29)Type

Re-exports

<!-- -->

[Type](https://mikro-orm.io/api/core/class/Type.md)

### [**](#typeconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L95)TypeConfig

Re-exports

<!-- -->

[TypeConfig](https://mikro-orm.io/api/core/interface/TypeConfig.md)

### [**](#types)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L56)types

Re-exports

<!-- -->

[types](https://mikro-orm.io/api/core.md#types)

### [**](#uint8arraytype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L35)Uint8ArrayType

Re-exports

<!-- -->

[Uint8ArrayType](https://mikro-orm.io/api/core/class/Uint8ArrayType.md)

### [**](#unboxarray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L104)UnboxArray

Re-exports

<!-- -->

[UnboxArray](https://mikro-orm.io/api/core.md#UnboxArray)

### [**](#underscorenamingstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/UnderscoreNamingStrategy.ts#L3)UnderscoreNamingStrategy

Re-exports

<!-- -->

[UnderscoreNamingStrategy](https://mikro-orm.io/api/core/class/UnderscoreNamingStrategy.md)

### [**](#uniqueconstraintviolationexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/exceptions.ts#L120)UniqueConstraintViolationException

Re-exports

<!-- -->

[UniqueConstraintViolationException](https://mikro-orm.io/api/core/class/UniqueConstraintViolationException.md)

### [**](#uniqueoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L702)UniqueOptions

Re-exports

<!-- -->

[UniqueOptions](https://mikro-orm.io/api/core/interface/UniqueOptions.md)

### [**](#unitofwork)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L42)UnitOfWork

Re-exports

<!-- -->

[UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)

### [**](#universalpropertykeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L58)UniversalPropertyKeys

Re-exports

<!-- -->

[UniversalPropertyKeys](https://mikro-orm.io/api/core.md#UniversalPropertyKeys)

### [**](#unknowntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L51)UnknownType

Re-exports

<!-- -->

[UnknownType](https://mikro-orm.io/api/core/class/UnknownType.md)

### [**](#updateoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L446)UpdateOptions

Re-exports

<!-- -->

[UpdateOptions](https://mikro-orm.io/api/core/interface/UpdateOptions.md)

### [**](#updatequerybuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4185)UpdateQueryBuilder

Re-exports

<!-- -->

[UpdateQueryBuilder](https://mikro-orm.io/api/sql/interface/UpdateQueryBuilder.md)

### [**](#updateschemaoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/index.ts#L100)UpdateSchemaOptions

Re-exports

<!-- -->

[UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)

### [**](#upsertmanyoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L410)UpsertManyOptions

Re-exports

<!-- -->

[UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)

### [**](#upsertoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L398)UpsertOptions

Re-exports

<!-- -->

[UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)

### [**](#utils)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L173)Utils

Re-exports

<!-- -->

[Utils](https://mikro-orm.io/api/core/class/Utils.md)

### [**](#uuidtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/types/index.ts#L49)UuidType

Re-exports

<!-- -->

[UuidType](https://mikro-orm.io/api/core/class/UuidType.md)

### [**](#validationerror)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/errors.ts#L13)ValidationError

Re-exports

<!-- -->

[ValidationError](https://mikro-orm.io/api/core/class/ValidationError.md)

### [**](#weightedfulltextvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/FullTextType.ts#L11)WeightedFullTextValue

Re-exports

<!-- -->

[WeightedFullTextValue](https://mikro-orm.io/api/sql.md#WeightedFullTextValue)

### [**](#wrap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/wrap.ts#L6)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/wrap.ts#L11)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/wrap.ts#L17)wrap

Re-exports

<!-- -->

[wrap](https://mikro-orm.io/api/core/function/wrap.md)

### [**](#wrappedentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/WrappedEntity.ts#L41)WrappedEntity

Re-exports

<!-- -->

[WrappedEntity](https://mikro-orm.io/api/core/class/WrappedEntity.md)

## Type Aliases<!-- -->[**](<#Type Aliases>)

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/postgresql/src/PostgreSqlMikroORM.ts#L15)Options

**Options\<EM, Entities>: Partial<[Options](https://mikro-orm.io/api/core/interface/Options.md)<[PostgreSqlDriver](https://mikro-orm.io/api/postgresql/class/PostgreSqlDriver.md), EM, Entities>>

#### Type parameters

* **EM**: [PostgreSqlEntityManager](https://mikro-orm.io/api/postgresql/class/EntityManager.md) = [PostgreSqlEntityManager](https://mikro-orm.io/api/postgresql/class/EntityManager.md)
* **Entities**: (string | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[AnyEntity](https://mikro-orm.io/api/core.md#AnyEntity)> | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md))\[] = (string | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[AnyEntity](https://mikro-orm.io/api/core.md#AnyEntity)> | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md))\[]
