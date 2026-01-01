# Source: https://mikro-orm.io/api/postgresql.md

# @mikro-orm/postgresql<!-- -->

## Index[**](#Index)

### References

* [**AbstractNamingStrategy](https://mikro-orm.io/api/postgresql.md#AbstractNamingStrategy)
* [**AbstractSchemaGenerator](https://mikro-orm.io/api/postgresql.md#AbstractSchemaGenerator)
* [**AbstractSqlConnection](https://mikro-orm.io/api/postgresql.md#AbstractSqlConnection)
* [**AbstractSqlDriver](https://mikro-orm.io/api/postgresql.md#AbstractSqlDriver)
* [**AbstractSqlPlatform](https://mikro-orm.io/api/postgresql.md#AbstractSqlPlatform)
* [**AfterCreate](https://mikro-orm.io/api/postgresql.md#AfterCreate)
* [**AfterDelete](https://mikro-orm.io/api/postgresql.md#AfterDelete)
* [**AfterUpdate](https://mikro-orm.io/api/postgresql.md#AfterUpdate)
* [**AfterUpsert](https://mikro-orm.io/api/postgresql.md#AfterUpsert)
* [**Alias](https://mikro-orm.io/api/postgresql.md#Alias)
* [**AnyEntity](https://mikro-orm.io/api/postgresql.md#AnyEntity)
* [**AnyString](https://mikro-orm.io/api/postgresql.md#AnyString)
* [**ARRAY\_OPERATORS](https://mikro-orm.io/api/postgresql.md#ARRAY_OPERATORS)
* [**ArrayCollection](https://mikro-orm.io/api/postgresql.md#ArrayCollection)
* [**ArrayType](https://mikro-orm.io/api/postgresql.md#ArrayType)
* [**assign](https://mikro-orm.io/api/postgresql.md#assign)
* [**AssignOptions](https://mikro-orm.io/api/postgresql.md#AssignOptions)
* [**AutoPath](https://mikro-orm.io/api/postgresql.md#AutoPath)
* [**BaseEntity](https://mikro-orm.io/api/postgresql.md#BaseEntity)
* [**BaseSqliteConnection](https://mikro-orm.io/api/postgresql.md#BaseSqliteConnection)
* [**BaseSqlitePlatform](https://mikro-orm.io/api/postgresql.md#BaseSqlitePlatform)
* [**BaseSqliteSchemaHelper](https://mikro-orm.io/api/postgresql.md#BaseSqliteSchemaHelper)
* [**BeforeCreate](https://mikro-orm.io/api/postgresql.md#BeforeCreate)
* [**BeforeDelete](https://mikro-orm.io/api/postgresql.md#BeforeDelete)
* [**BeforeUpdate](https://mikro-orm.io/api/postgresql.md#BeforeUpdate)
* [**BeforeUpsert](https://mikro-orm.io/api/postgresql.md#BeforeUpsert)
* [**BetterSqliteKnexDialect](https://mikro-orm.io/api/postgresql.md#BetterSqliteKnexDialect)
* [**BigIntType](https://mikro-orm.io/api/postgresql.md#BigIntType)
* [**BlobType](https://mikro-orm.io/api/postgresql.md#BlobType)
* [**BooleanType](https://mikro-orm.io/api/postgresql.md#BooleanType)
* [**CacheAdapter](https://mikro-orm.io/api/postgresql.md#CacheAdapter)
* [**Cascade](https://mikro-orm.io/api/postgresql.md#Cascade)
* [**Cast](https://mikro-orm.io/api/postgresql.md#Cast)
* [**ChangeSet](https://mikro-orm.io/api/postgresql.md#ChangeSet)
* [**ChangeSetComputer](https://mikro-orm.io/api/postgresql.md#ChangeSetComputer)
* [**ChangeSetPersister](https://mikro-orm.io/api/postgresql.md#ChangeSetPersister)
* [**ChangeSetType](https://mikro-orm.io/api/postgresql.md#ChangeSetType)
* [**CharacterType](https://mikro-orm.io/api/postgresql.md#CharacterType)
* [**Check](https://mikro-orm.io/api/postgresql.md#Check)
* [**CheckCallback](https://mikro-orm.io/api/postgresql.md#CheckCallback)
* [**CheckConstraintViolationException](https://mikro-orm.io/api/postgresql.md#CheckConstraintViolationException)
* [**CheckDef](https://mikro-orm.io/api/postgresql.md#CheckDef)
* [**CheckOptions](https://mikro-orm.io/api/postgresql.md#CheckOptions)
* [**ClearDatabaseOptions](https://mikro-orm.io/api/postgresql.md#ClearDatabaseOptions)
* [**Collection](https://mikro-orm.io/api/postgresql.md#Collection)
* [**Column](https://mikro-orm.io/api/postgresql.md#Column)
* [**ColumnDifference](https://mikro-orm.io/api/postgresql.md#ColumnDifference)
* [**compareArrays](https://mikro-orm.io/api/postgresql.md#compareArrays)
* [**compareBooleans](https://mikro-orm.io/api/postgresql.md#compareBooleans)
* [**compareBuffers](https://mikro-orm.io/api/postgresql.md#compareBuffers)
* [**compareObjects](https://mikro-orm.io/api/postgresql.md#compareObjects)
* [**Config](https://mikro-orm.io/api/postgresql.md#Config)
* [**Configuration](https://mikro-orm.io/api/postgresql.md#Configuration)
* [**Connection](https://mikro-orm.io/api/postgresql.md#Connection)
* [**ConnectionConfig](https://mikro-orm.io/api/postgresql.md#ConnectionConfig)
* [**ConnectionException](https://mikro-orm.io/api/postgresql.md#ConnectionException)
* [**ConnectionOptions](https://mikro-orm.io/api/postgresql.md#ConnectionOptions)
* [**ConnectionType](https://mikro-orm.io/api/postgresql.md#ConnectionType)
* [**ConstraintViolationException](https://mikro-orm.io/api/postgresql.md#ConstraintViolationException)
* [**Constructor](https://mikro-orm.io/api/postgresql.md#Constructor)
* [**CountOptions](https://mikro-orm.io/api/postgresql.md#CountOptions)
* [**CountQueryBuilder](https://mikro-orm.io/api/postgresql.md#CountQueryBuilder)
* [**CreateContextOptions](https://mikro-orm.io/api/postgresql.md#CreateContextOptions)
* [**CreateOptions](https://mikro-orm.io/api/postgresql.md#CreateOptions)
* [**CreateRequestContext](https://mikro-orm.io/api/postgresql.md#CreateRequestContext)
* [**CreateSchemaOptions](https://mikro-orm.io/api/postgresql.md#CreateSchemaOptions)
* [**createSqlFunction](https://mikro-orm.io/api/postgresql.md#createSqlFunction)
* [**Cursor](https://mikro-orm.io/api/postgresql.md#Cursor)
* [**CursorError](https://mikro-orm.io/api/postgresql.md#CursorError)
* [**DatabaseDriver](https://mikro-orm.io/api/postgresql.md#DatabaseDriver)
* [**DatabaseObjectExistsException](https://mikro-orm.io/api/postgresql.md#DatabaseObjectExistsException)
* [**DatabaseObjectNotFoundException](https://mikro-orm.io/api/postgresql.md#DatabaseObjectNotFoundException)
* [**DataloaderType](https://mikro-orm.io/api/postgresql.md#DataloaderType)
* [**DataloaderUtils](https://mikro-orm.io/api/postgresql.md#DataloaderUtils)
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
* [**DynamicPassword](https://mikro-orm.io/api/postgresql.md#DynamicPassword)
* [**EagerProps](https://mikro-orm.io/api/postgresql.md#EagerProps)
* [**Edge](https://mikro-orm.io/api/postgresql.md#Edge)
* [**Embeddable](https://mikro-orm.io/api/postgresql.md#Embeddable)
* [**EmbeddableOptions](https://mikro-orm.io/api/postgresql.md#EmbeddableOptions)
* [**Embedded](https://mikro-orm.io/api/postgresql.md#Embedded)
* [**EmbeddedOptions](https://mikro-orm.io/api/postgresql.md#EmbeddedOptions)
* [**EmbeddedPrefixMode](https://mikro-orm.io/api/postgresql.md#EmbeddedPrefixMode)
* [**EmptyOptions](https://mikro-orm.io/api/postgresql.md#EmptyOptions)
* [**EnsureDatabaseOptions](https://mikro-orm.io/api/postgresql.md#EnsureDatabaseOptions)
* [**EnsureRequestContext](https://mikro-orm.io/api/postgresql.md#EnsureRequestContext)
* [**Entity](https://mikro-orm.io/api/postgresql.md#Entity)
* [**EntityAssigner](https://mikro-orm.io/api/postgresql.md#EntityAssigner)
* [**EntityCaseNamingStrategy](https://mikro-orm.io/api/postgresql.md#EntityCaseNamingStrategy)
* [**EntityClass](https://mikro-orm.io/api/postgresql.md#EntityClass)
* [**EntityClassGroup](https://mikro-orm.io/api/postgresql.md#EntityClassGroup)
* [**EntityComparator](https://mikro-orm.io/api/postgresql.md#EntityComparator)
* [**EntityData](https://mikro-orm.io/api/postgresql.md#EntityData)
* [**EntityDataValue](https://mikro-orm.io/api/postgresql.md#EntityDataValue)
* [**EntityDictionary](https://mikro-orm.io/api/postgresql.md#EntityDictionary)
* [**EntityDTO](https://mikro-orm.io/api/postgresql.md#EntityDTO)
* [**EntityFactory](https://mikro-orm.io/api/postgresql.md#EntityFactory)
* [**EntityField](https://mikro-orm.io/api/postgresql.md#EntityField)
* [**EntityKey](https://mikro-orm.io/api/postgresql.md#EntityKey)
* [**EntityLoader](https://mikro-orm.io/api/postgresql.md#EntityLoader)
* [**EntityLoaderOptions](https://mikro-orm.io/api/postgresql.md#EntityLoaderOptions)
* [**EntityManager](https://mikro-orm.io/api/postgresql.md#EntityManager)
* [**EntityManagerType](https://mikro-orm.io/api/postgresql.md#EntityManagerType)
* [**EntityMetadata](https://mikro-orm.io/api/postgresql.md#EntityMetadata)
* [**EntityName](https://mikro-orm.io/api/postgresql.md#EntityName)
* [**EntityOptions](https://mikro-orm.io/api/postgresql.md#EntityOptions)
* [**EntityProperty](https://mikro-orm.io/api/postgresql.md#EntityProperty)
* [**EntityProps](https://mikro-orm.io/api/postgresql.md#EntityProps)
* [**EntityRef](https://mikro-orm.io/api/postgresql.md#EntityRef)
* [**EntityRepository](https://mikro-orm.io/api/postgresql.md#EntityRepository)
* [**EntityRepositoryType](https://mikro-orm.io/api/postgresql.md#EntityRepositoryType)
* [**EntitySchema](https://mikro-orm.io/api/postgresql.md#EntitySchema)
* [**EntitySchemaMetadata](https://mikro-orm.io/api/postgresql.md#EntitySchemaMetadata)
* [**EntitySchemaProperty](https://mikro-orm.io/api/postgresql.md#EntitySchemaProperty)
* [**EntitySerializer](https://mikro-orm.io/api/postgresql.md#EntitySerializer)
* [**EntityTransformer](https://mikro-orm.io/api/postgresql.md#EntityTransformer)
* [**EntityType](https://mikro-orm.io/api/postgresql.md#EntityType)
* [**EntityValidator](https://mikro-orm.io/api/postgresql.md#EntityValidator)
* [**EntityValue](https://mikro-orm.io/api/postgresql.md#EntityValue)
* [**Enum](https://mikro-orm.io/api/postgresql.md#Enum)
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
* [**FileCacheAdapter](https://mikro-orm.io/api/postgresql.md#FileCacheAdapter)
* [**Filter](https://mikro-orm.io/api/postgresql.md#Filter)
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
* [**Formula](https://mikro-orm.io/api/postgresql.md#Formula)
* [**FormulaOptions](https://mikro-orm.io/api/postgresql.md#FormulaOptions)
* [**FromEntityType](https://mikro-orm.io/api/postgresql.md#FromEntityType)
* [**GeneratedCacheAdapter](https://mikro-orm.io/api/postgresql.md#GeneratedCacheAdapter)
* [**GenerateOptions](https://mikro-orm.io/api/postgresql.md#GenerateOptions)
* [**GetReferenceOptions](https://mikro-orm.io/api/postgresql.md#GetReferenceOptions)
* [**GetRepository](https://mikro-orm.io/api/postgresql.md#GetRepository)
* [**GroupOperator](https://mikro-orm.io/api/postgresql.md#GroupOperator)
* [**Hidden](https://mikro-orm.io/api/postgresql.md#Hidden)
* [**HiddenProps](https://mikro-orm.io/api/postgresql.md#HiddenProps)
* [**Highlighter](https://mikro-orm.io/api/postgresql.md#Highlighter)
* [**Hydrator](https://mikro-orm.io/api/postgresql.md#Hydrator)
* [**IConfiguration](https://mikro-orm.io/api/postgresql.md#IConfiguration)
* [**ICriteriaNode](https://mikro-orm.io/api/postgresql.md#ICriteriaNode)
* [**ICriteriaNodeProcessOptions](https://mikro-orm.io/api/postgresql.md#ICriteriaNodeProcessOptions)
* [**IDatabaseDriver](https://mikro-orm.io/api/postgresql.md#IDatabaseDriver)
* [**IdentityMap](https://mikro-orm.io/api/postgresql.md#IdentityMap)
* [**IEntityGenerator](https://mikro-orm.io/api/postgresql.md#IEntityGenerator)
* [**IMigrationGenerator](https://mikro-orm.io/api/postgresql.md#IMigrationGenerator)
* [**IMigrator](https://mikro-orm.io/api/postgresql.md#IMigrator)
* [**ImportsResolver](https://mikro-orm.io/api/postgresql.md#ImportsResolver)
* [**Index](https://mikro-orm.io/api/postgresql.md#Index)
* [**IndexCallback](https://mikro-orm.io/api/postgresql.md#IndexCallback)
* [**IndexDef](https://mikro-orm.io/api/postgresql.md#IndexDef)
* [**IndexOptions](https://mikro-orm.io/api/postgresql.md#IndexOptions)
* [**InferEntity](https://mikro-orm.io/api/postgresql.md#InferEntity)
* [**InferEntityFromProperties](https://mikro-orm.io/api/postgresql.md#InferEntityFromProperties)
* [**InferPrimaryKey](https://mikro-orm.io/api/postgresql.md#InferPrimaryKey)
* [**InitCollectionOptions](https://mikro-orm.io/api/postgresql.md#InitCollectionOptions)
* [**InsertQueryBuilder](https://mikro-orm.io/api/postgresql.md#InsertQueryBuilder)
* [**IntegerType](https://mikro-orm.io/api/postgresql.md#IntegerType)
* [**IntervalType](https://mikro-orm.io/api/postgresql.md#IntervalType)
* [**InvalidFieldNameException](https://mikro-orm.io/api/postgresql.md#InvalidFieldNameException)
* [**IPrimaryKey](https://mikro-orm.io/api/postgresql.md#IPrimaryKey)
* [**IQueryBuilder](https://mikro-orm.io/api/postgresql.md#IQueryBuilder)
* [**ISchemaGenerator](https://mikro-orm.io/api/postgresql.md#ISchemaGenerator)
* [**ISeedManager](https://mikro-orm.io/api/postgresql.md#ISeedManager)
* [**IsolationLevel](https://mikro-orm.io/api/postgresql.md#IsolationLevel)
* [**IsSubset](https://mikro-orm.io/api/postgresql.md#IsSubset)
* [**IsUnknown](https://mikro-orm.io/api/postgresql.md#IsUnknown)
* [**IType](https://mikro-orm.io/api/postgresql.md#IType)
* [**IWrappedEntity](https://mikro-orm.io/api/postgresql.md#IWrappedEntity)
* [**JoinOptions](https://mikro-orm.io/api/postgresql.md#JoinOptions)
* [**JoinType](https://mikro-orm.io/api/postgresql.md#JoinType)
* [**JSON\_KEY\_OPERATORS](https://mikro-orm.io/api/postgresql.md#JSON_KEY_OPERATORS)
* [**JsonProperty](https://mikro-orm.io/api/postgresql.md#JsonProperty)
* [**JsonType](https://mikro-orm.io/api/postgresql.md#JsonType)
* [**KnexStringRef](https://mikro-orm.io/api/postgresql.md#KnexStringRef)
* [**LibSqlKnexDialect](https://mikro-orm.io/api/postgresql.md#LibSqlKnexDialect)
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
* [**ManyToMany](https://mikro-orm.io/api/postgresql.md#ManyToMany)
* [**ManyToManyOptions](https://mikro-orm.io/api/postgresql.md#ManyToManyOptions)
* [**ManyToOne](https://mikro-orm.io/api/postgresql.md#ManyToOne)
* [**ManyToOneOptions](https://mikro-orm.io/api/postgresql.md#ManyToOneOptions)
* [**MariaDbKnexDialect](https://mikro-orm.io/api/postgresql.md#MariaDbKnexDialect)
* [**MatchingOptions](https://mikro-orm.io/api/postgresql.md#MatchingOptions)
* [**MaybePromise](https://mikro-orm.io/api/postgresql.md#MaybePromise)
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
* [**MigrationObject](https://mikro-orm.io/api/postgresql.md#MigrationObject)
* [**MigrationResult](https://mikro-orm.io/api/postgresql.md#MigrationResult)
* [**MigrationRow](https://mikro-orm.io/api/postgresql.md#MigrationRow)
* [**MigrationsOptions](https://mikro-orm.io/api/postgresql.md#MigrationsOptions)
* [**MigratorEvent](https://mikro-orm.io/api/postgresql.md#MigratorEvent)
* [**MikroORMOptions](https://mikro-orm.io/api/postgresql.md#MikroORMOptions)
* [**ModifyContext](https://mikro-orm.io/api/postgresql.md#ModifyContext)
* [**ModifyHint](https://mikro-orm.io/api/postgresql.md#ModifyHint)
* [**MongoNamingStrategy](https://mikro-orm.io/api/postgresql.md#MongoNamingStrategy)
* [**MonkeyPatchable](https://mikro-orm.io/api/postgresql.md#MonkeyPatchable)
* [**MsSqlKnexDialect](https://mikro-orm.io/api/postgresql.md#MsSqlKnexDialect)
* [**MySqlConnection](https://mikro-orm.io/api/postgresql.md#MySqlConnection)
* [**MySqlExceptionConverter](https://mikro-orm.io/api/postgresql.md#MySqlExceptionConverter)
* [**MySqlIncrementOptions](https://mikro-orm.io/api/postgresql.md#MySqlIncrementOptions)
* [**MySqlKnexDialect](https://mikro-orm.io/api/postgresql.md#MySqlKnexDialect)
* [**MySqlPlatform](https://mikro-orm.io/api/postgresql.md#MySqlPlatform)
* [**MySqlSchemaHelper](https://mikro-orm.io/api/postgresql.md#MySqlSchemaHelper)
* [**MySqlTableBuilder](https://mikro-orm.io/api/postgresql.md#MySqlTableBuilder)
* [**NamingStrategy](https://mikro-orm.io/api/postgresql.md#NamingStrategy)
* [**NativeDeleteOptions](https://mikro-orm.io/api/postgresql.md#NativeDeleteOptions)
* [**NativeInsertUpdateManyOptions](https://mikro-orm.io/api/postgresql.md#NativeInsertUpdateManyOptions)
* [**NativeInsertUpdateOptions](https://mikro-orm.io/api/postgresql.md#NativeInsertUpdateOptions)
* [**New](https://mikro-orm.io/api/postgresql.md#New)
* [**Node](https://mikro-orm.io/api/postgresql.md#Node)
* [**NodeState](https://mikro-orm.io/api/postgresql.md#NodeState)
* [**NoInfer](https://mikro-orm.io/api/postgresql.md#NoInfer)
* [**NonUniqueFieldNameException](https://mikro-orm.io/api/postgresql.md#NonUniqueFieldNameException)
* [**NotFoundError](https://mikro-orm.io/api/postgresql.md#NotFoundError)
* [**NotNullConstraintViolationException](https://mikro-orm.io/api/postgresql.md#NotNullConstraintViolationException)
* [**NullCacheAdapter](https://mikro-orm.io/api/postgresql.md#NullCacheAdapter)
* [**NullHighlighter](https://mikro-orm.io/api/postgresql.md#NullHighlighter)
* [**ObjectBindingPattern](https://mikro-orm.io/api/postgresql.md#ObjectBindingPattern)
* [**ObjectHydrator](https://mikro-orm.io/api/postgresql.md#ObjectHydrator)
* [**ObjectQuery](https://mikro-orm.io/api/postgresql.md#ObjectQuery)
* [**OneToMany](https://mikro-orm.io/api/postgresql.md#OneToMany)
* [**OneToManyOptions](https://mikro-orm.io/api/postgresql.md#OneToManyOptions)
* [**OneToOne](https://mikro-orm.io/api/postgresql.md#OneToOne)
* [**OneToOneOptions](https://mikro-orm.io/api/postgresql.md#OneToOneOptions)
* [**OnInit](https://mikro-orm.io/api/postgresql.md#OnInit)
* [**OnLoad](https://mikro-orm.io/api/postgresql.md#OnLoad)
* [**Opt](https://mikro-orm.io/api/postgresql.md#Opt)
* [**OptimisticLockError](https://mikro-orm.io/api/postgresql.md#OptimisticLockError)
* [**OptionalProps](https://mikro-orm.io/api/postgresql.md#OptionalProps)
* [**OrderDefinition](https://mikro-orm.io/api/postgresql.md#OrderDefinition)
* [**p](https://mikro-orm.io/api/postgresql.md#p)
* [**parseJsonSafe](https://mikro-orm.io/api/postgresql.md#parseJsonSafe)
* [**PlainObject](https://mikro-orm.io/api/postgresql.md#PlainObject)
* [**Platform](https://mikro-orm.io/api/postgresql.md#Platform)
* [**PoolConfig](https://mikro-orm.io/api/postgresql.md#PoolConfig)
* [**Populate](https://mikro-orm.io/api/postgresql.md#Populate)
* [**PopulateHint](https://mikro-orm.io/api/postgresql.md#PopulateHint)
* [**PopulateOptions](https://mikro-orm.io/api/postgresql.md#PopulateOptions)
* [**PopulatePath](https://mikro-orm.io/api/postgresql.md#PopulatePath)
* [**PostgreSqlKnexDialect](https://mikro-orm.io/api/postgresql.md#PostgreSqlKnexDialect)
* [**Primary](https://mikro-orm.io/api/postgresql.md#Primary)
* [**PrimaryKey](https://mikro-orm.io/api/postgresql.md#PrimaryKey)
* [**PrimaryKeyOptions](https://mikro-orm.io/api/postgresql.md#PrimaryKeyOptions)
* [**PrimaryKeyProp](https://mikro-orm.io/api/postgresql.md#PrimaryKeyProp)
* [**Property](https://mikro-orm.io/api/postgresql.md#Property)
* [**PropertyOptions](https://mikro-orm.io/api/postgresql.md#PropertyOptions)
* [**QBField](https://mikro-orm.io/api/postgresql.md#QBField)
* [**QBField2](https://mikro-orm.io/api/postgresql.md#QBField2)
* [**QBFilterQuery](https://mikro-orm.io/api/postgresql.md#QBFilterQuery)
* [**QBQueryOrderMap](https://mikro-orm.io/api/postgresql.md#QBQueryOrderMap)
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
* [**raw](https://mikro-orm.io/api/postgresql.md#raw)
* [**RawQueryFragment](https://mikro-orm.io/api/postgresql.md#RawQueryFragment)
* [**ReadOnlyException](https://mikro-orm.io/api/postgresql.md#ReadOnlyException)
* [**ref](https://mikro-orm.io/api/postgresql.md#ref)
* [**Ref](https://mikro-orm.io/api/postgresql.md#Ref)
* [**Reference](https://mikro-orm.io/api/postgresql.md#Reference)
* [**ReferenceKind](https://mikro-orm.io/api/postgresql.md#ReferenceKind)
* [**ReferenceOptions](https://mikro-orm.io/api/postgresql.md#ReferenceOptions)
* [**ReflectMetadataProvider](https://mikro-orm.io/api/postgresql.md#ReflectMetadataProvider)
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
* [**SchemaComparator](https://mikro-orm.io/api/postgresql.md#SchemaComparator)
* [**SchemaDifference](https://mikro-orm.io/api/postgresql.md#SchemaDifference)
* [**SchemaGenerator](https://mikro-orm.io/api/postgresql.md#SchemaGenerator)
* [**SchemaHelper](https://mikro-orm.io/api/postgresql.md#SchemaHelper)
* [**SeederOptions](https://mikro-orm.io/api/postgresql.md#SeederOptions)
* [**Selected](https://mikro-orm.io/api/postgresql.md#Selected)
* [**SelectQueryBuilder](https://mikro-orm.io/api/postgresql.md#SelectQueryBuilder)
* [**SerializationContext](https://mikro-orm.io/api/postgresql.md#SerializationContext)
* [**serialize](https://mikro-orm.io/api/postgresql.md#serialize)
* [**SerializedPrimaryKey](https://mikro-orm.io/api/postgresql.md#SerializedPrimaryKey)
* [**SerializedPrimaryKeyOptions](https://mikro-orm.io/api/postgresql.md#SerializedPrimaryKeyOptions)
* [**SerializeOptions](https://mikro-orm.io/api/postgresql.md#SerializeOptions)
* [**ServerException](https://mikro-orm.io/api/postgresql.md#ServerException)
* [**Settings](https://mikro-orm.io/api/postgresql.md#Settings)
* [**SimpleColumnMeta](https://mikro-orm.io/api/postgresql.md#SimpleColumnMeta)
* [**SimpleLogger](https://mikro-orm.io/api/postgresql.md#SimpleLogger)
* [**SmallIntType](https://mikro-orm.io/api/postgresql.md#SmallIntType)
* [**sql](https://mikro-orm.io/api/postgresql.md#sql)
* [**SqlEntityManager](https://mikro-orm.io/api/postgresql.md#SqlEntityManager)
* [**SqlEntityRepository](https://mikro-orm.io/api/postgresql.md#SqlEntityRepository)
* [**SqliteKnexDialect](https://mikro-orm.io/api/postgresql.md#SqliteKnexDialect)
* [**SqliteTableCompiler](https://mikro-orm.io/api/postgresql.md#SqliteTableCompiler)
* [**SqlSchemaGenerator](https://mikro-orm.io/api/postgresql.md#SqlSchemaGenerator)
* [**StringType](https://mikro-orm.io/api/postgresql.md#StringType)
* [**SyncCacheAdapter](https://mikro-orm.io/api/postgresql.md#SyncCacheAdapter)
* [**SyntaxErrorException](https://mikro-orm.io/api/postgresql.md#SyntaxErrorException)
* [**t](https://mikro-orm.io/api/postgresql.md#t)
* [**Table](https://mikro-orm.io/api/postgresql.md#Table)
* [**TableDifference](https://mikro-orm.io/api/postgresql.md#TableDifference)
* [**TableExistsException](https://mikro-orm.io/api/postgresql.md#TableExistsException)
* [**TableNotFoundException](https://mikro-orm.io/api/postgresql.md#TableNotFoundException)
* [**TextType](https://mikro-orm.io/api/postgresql.md#TextType)
* [**TimeType](https://mikro-orm.io/api/postgresql.md#TimeType)
* [**TinyIntType](https://mikro-orm.io/api/postgresql.md#TinyIntType)
* [**Transaction](https://mikro-orm.io/api/postgresql.md#Transaction)
* [**Transactional](https://mikro-orm.io/api/postgresql.md#Transactional)
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
* [**UmzugMigration](https://mikro-orm.io/api/postgresql.md#UmzugMigration)
* [**UnboxArray](https://mikro-orm.io/api/postgresql.md#UnboxArray)
* [**UnderscoreNamingStrategy](https://mikro-orm.io/api/postgresql.md#UnderscoreNamingStrategy)
* [**Unique](https://mikro-orm.io/api/postgresql.md#Unique)
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
* [**wrap](https://mikro-orm.io/api/postgresql.md#wrap)
* [**WrappedEntity](https://mikro-orm.io/api/postgresql.md#WrappedEntity)

### Classes

* [**FullTextType](https://mikro-orm.io/api/postgresql/class/FullTextType.md)
* [**MikroORM](https://mikro-orm.io/api/postgresql/class/MikroORM.md)
* [**PostgreSqlConnection](https://mikro-orm.io/api/postgresql/class/PostgreSqlConnection.md)
* [**PostgreSqlDriver](https://mikro-orm.io/api/postgresql/class/PostgreSqlDriver.md)
* [**PostgreSqlExceptionConverter](https://mikro-orm.io/api/postgresql/class/PostgreSqlExceptionConverter.md)
* [**PostgreSqlPlatform](https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md)
* [**PostgreSqlSchemaHelper](https://mikro-orm.io/api/postgresql/class/PostgreSqlSchemaHelper.md)

### Type Aliases

* [**Options](https://mikro-orm.io/api/postgresql.md#Options)
* [**WeightedFullTextValue](https://mikro-orm.io/api/postgresql.md#WeightedFullTextValue)

### Functions

* [**defineConfig](https://mikro-orm.io/api/postgresql/function/defineConfig.md)

## References<!-- -->[**](#References)

### [**](#AbstractNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L6)AbstractNamingStrategy

Re-exports

<!-- -->

[AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)

### [**](#AbstractSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L17)AbstractSchemaGenerator

Re-exports

<!-- -->

[AbstractSchemaGenerator](https://mikro-orm.io/api/core/class/AbstractSchemaGenerator.md)

### [**](#AbstractSqlConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L28)AbstractSqlConnection

Re-exports

<!-- -->

[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)

### [**](#AbstractSqlDriver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L68)AbstractSqlDriver

Re-exports

<!-- -->

[AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)

### [**](#AbstractSqlPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L7)AbstractSqlPlatform

Re-exports

<!-- -->

[AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

### [**](#AfterCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L20)AfterCreate

Re-exports

<!-- -->

[AfterCreate](https://mikro-orm.io/api/core/function/AfterCreate.md)

### [**](#AfterDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L58)AfterDelete

Re-exports

<!-- -->

[AfterDelete](https://mikro-orm.io/api/core/function/AfterDelete.md)

### [**](#AfterUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L28)AfterUpdate

Re-exports

<!-- -->

[AfterUpdate](https://mikro-orm.io/api/core/function/AfterUpdate.md)

### [**](#AfterUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L36)AfterUpsert

Re-exports

<!-- -->

[AfterUpsert](https://mikro-orm.io/api/core/function/AfterUpsert.md)

### [**](#Alias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilderHelper.ts#L982)Alias

Re-exports

<!-- -->

[Alias](https://mikro-orm.io/api/knex/interface/Alias.md)

### [**](#AnyEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)AnyEntity

Re-exports

<!-- -->

[AnyEntity](https://mikro-orm.io/api/core.md#AnyEntity)

### [**](#AnyString)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)AnyString

Re-exports

<!-- -->

[AnyString](https://mikro-orm.io/api/core.md#AnyString)

### [**](#ARRAY_OPERATORS)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L55)ARRAY\_OPERATORS

Re-exports

<!-- -->

[ARRAY\_OPERATORS](https://mikro-orm.io/api/core.md#ARRAY_OPERATORS)

### [**](#ArrayCollection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L9)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L511)ArrayCollection

Re-exports

<!-- -->

[ArrayCollection](https://mikro-orm.io/api/core/class/ArrayCollection.md)

### [**](#ArrayType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)ArrayType

Re-exports

<!-- -->

[ArrayType](https://mikro-orm.io/api/core/class/ArrayType.md)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L311)assign

Re-exports

<!-- -->

[assign](https://mikro-orm.io/api/core/function/assign.md)

### [**](#AssignOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L313)AssignOptions

Re-exports

<!-- -->

[AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)

### [**](#AutoPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)AutoPath

Re-exports

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)

### [**](#BaseEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L9)BaseEntity

Re-exports

<!-- -->

[BaseEntity](https://mikro-orm.io/api/core/class/BaseEntity.md)

### [**](#BaseSqliteConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteConnection.ts#L7)BaseSqliteConnection

Re-exports

<!-- -->

[BaseSqliteConnection](https://mikro-orm.io/api/knex/class/BaseSqliteConnection.md)

### [**](#BaseSqlitePlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqlitePlatform.ts#L4)BaseSqlitePlatform

Re-exports

<!-- -->

[BaseSqlitePlatform](https://mikro-orm.io/api/knex/class/BaseSqlitePlatform.md)

### [**](#BaseSqliteSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L6)BaseSqliteSchemaHelper

Re-exports

<!-- -->

[BaseSqliteSchemaHelper](https://mikro-orm.io/api/knex/class/BaseSqliteSchemaHelper.md)

### [**](#BeforeCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L16)BeforeCreate

Re-exports

<!-- -->

[BeforeCreate](https://mikro-orm.io/api/core/function/BeforeCreate.md)

### [**](#BeforeDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L51)BeforeDelete

Re-exports

<!-- -->

[BeforeDelete](https://mikro-orm.io/api/core/function/BeforeDelete.md)

### [**](#BeforeUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L24)BeforeUpdate

Re-exports

<!-- -->

[BeforeUpdate](https://mikro-orm.io/api/core/function/BeforeUpdate.md)

### [**](#BeforeUpsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L32)BeforeUpsert

Re-exports

<!-- -->

[BeforeUpsert](https://mikro-orm.io/api/core/function/BeforeUpsert.md)

### [**](#BetterSqliteKnexDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BetterSqliteKnexDialect.ts#L4)BetterSqliteKnexDialect

Re-exports

<!-- -->

[BetterSqliteKnexDialect](https://mikro-orm.io/api/knex/class/BetterSqliteKnexDialect.md)

### [**](#BigIntType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)BigIntType

Re-exports

<!-- -->

[BigIntType](https://mikro-orm.io/api/core/class/BigIntType.md)

### [**](#BlobType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)BlobType

Re-exports

<!-- -->

[BlobType](https://mikro-orm.io/api/core/class/BlobType.md)

### [**](#BooleanType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)BooleanType

Re-exports

<!-- -->

[BooleanType](https://mikro-orm.io/api/core/class/BooleanType.md)

### [**](#CacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/CacheAdapter.ts#L1)CacheAdapter

Re-exports

<!-- -->

[CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

### [**](#Cascade)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L131)Cascade

Re-exports

<!-- -->

[Cascade](https://mikro-orm.io/api/core/enum/Cascade.md)

### [**](#Cast)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)Cast

Re-exports

<!-- -->

[Cast](https://mikro-orm.io/api/core.md#Cast)

### [**](#ChangeSet)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L6)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L67)ChangeSet

Re-exports

<!-- -->

[ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)

### [**](#ChangeSetComputer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetComputer.ts#L10)ChangeSetComputer

Re-exports

<!-- -->

[ChangeSetComputer](https://mikro-orm.io/api/core/class/ChangeSetComputer.md)

### [**](#ChangeSetPersister)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetPersister.ts#L13)ChangeSetPersister

Re-exports

<!-- -->

[ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

### [**](#ChangeSetType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L79)ChangeSetType

Re-exports

<!-- -->

[ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)

### [**](#CharacterType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)CharacterType

Re-exports

<!-- -->

[CharacterType](https://mikro-orm.io/api/core/class/CharacterType.md)

### [**](#Check)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Check.ts#L5)Check

Re-exports

<!-- -->

[Check](https://mikro-orm.io/api/core/function/Check.md)

### [**](#CheckCallback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)CheckCallback

Re-exports

<!-- -->

[CheckCallback](https://mikro-orm.io/api/core.md#CheckCallback)

### [**](#CheckConstraintViolationException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L70)CheckConstraintViolationException

Re-exports

<!-- -->

[CheckConstraintViolationException](https://mikro-orm.io/api/core/class/CheckConstraintViolationException.md)

### [**](#CheckDef)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L100)CheckDef

Re-exports

<!-- -->

[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)

### [**](#CheckOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Check.ts#L19)CheckOptions

Re-exports

<!-- -->

[CheckOptions](https://mikro-orm.io/api/core.md#CheckOptions)

### [**](#ClearDatabaseOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)ClearDatabaseOptions

Re-exports

<!-- -->

[ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

### [**](#Collection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L31)Collection

Re-exports

<!-- -->

[Collection](https://mikro-orm.io/api/core/class/Collection.md)

### [**](#Column)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L54)Column

Re-exports

<!-- -->

[Column](https://mikro-orm.io/api/knex/interface/Column.md)

### [**](#ColumnDifference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L107)ColumnDifference

Re-exports

<!-- -->

[ColumnDifference](https://mikro-orm.io/api/knex/interface/ColumnDifference.md)

### [**](#compareArrays)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L107)compareArrays

Re-exports

<!-- -->

[compareArrays](https://mikro-orm.io/api/core/function/compareArrays.md)

### [**](#compareBooleans)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L124)compareBooleans

Re-exports

<!-- -->

[compareBooleans](https://mikro-orm.io/api/core/function/compareBooleans.md)

### [**](#compareBuffers)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L131)compareBuffers

Re-exports

<!-- -->

[compareBuffers](https://mikro-orm.io/api/core/function/compareBuffers.md)

### [**](#compareObjects)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L49)compareObjects

Re-exports

<!-- -->

[compareObjects](https://mikro-orm.io/api/core/function/compareObjects.md)

### [**](#Config)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)Config

Re-exports

<!-- -->

[Config](https://mikro-orm.io/api/core.md#Config)

### [**](#Configuration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L46)Configuration

Re-exports

<!-- -->

[Configuration](https://mikro-orm.io/api/core/class/Configuration.md)

### [**](#Connection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L10)Connection

Re-exports

<!-- -->

[Connection](https://mikro-orm.io/api/core/class/Connection.md)

### [**](#ConnectionConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L182)ConnectionConfig

Re-exports

<!-- -->

[ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#ConnectionException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L27)ConnectionException

Re-exports

<!-- -->

[ConnectionException](https://mikro-orm.io/api/core/class/ConnectionException.md)

### [**](#ConnectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L513)ConnectionOptions

Re-exports

<!-- -->

[ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)

### [**](#ConnectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)ConnectionType

Re-exports

<!-- -->

[ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

### [**](#ConstraintViolationException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L37)ConstraintViolationException

Re-exports

<!-- -->

[ConstraintViolationException](https://mikro-orm.io/api/core/class/ConstraintViolationException.md)

### [**](#Constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)Constructor

Re-exports

<!-- -->

[Constructor](https://mikro-orm.io/api/core.md#Constructor)

### [**](#CountOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L243)CountOptions

Re-exports

<!-- -->

[CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)

### [**](#CountQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2031)CountQueryBuilder

Re-exports

<!-- -->

[CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)

### [**](#CreateContextOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RequestContext.ts#L72)CreateContextOptions

Re-exports

<!-- -->

[CreateContextOptions](https://mikro-orm.io/api/core/interface/CreateContextOptions.md)

### [**](#CreateOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/EntityManager.ts#L2406)CreateOptions

Re-exports

<!-- -->

[CreateOptions](https://mikro-orm.io/api/core/interface/CreateOptions.md)

### [**](#CreateRequestContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/CreateRequestContext.ts#L6)CreateRequestContext

Re-exports

<!-- -->

[CreateRequestContext](https://mikro-orm.io/api/core/function/CreateRequestContext.md)

### [**](#CreateSchemaOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)CreateSchemaOptions

Re-exports

<!-- -->

[CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

### [**](#createSqlFunction)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L253)createSqlFunction

Re-exports

<!-- -->

[createSqlFunction](https://mikro-orm.io/api/core/function/createSqlFunction.md)

### [**](#Cursor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L58)Cursor

Re-exports

<!-- -->

[Cursor](https://mikro-orm.io/api/core/class/Cursor.md)

### [**](#CursorError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/errors.ts#L138)CursorError

Re-exports

<!-- -->

[CursorError](https://mikro-orm.io/api/core/class/CursorError.md)

### [**](#DatabaseDriver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L40)DatabaseDriver

Re-exports

<!-- -->

[DatabaseDriver](https://mikro-orm.io/api/core/class/DatabaseDriver.md)

### [**](#DatabaseObjectExistsException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L46)DatabaseObjectExistsException

Re-exports

<!-- -->

[DatabaseObjectExistsException](https://mikro-orm.io/api/core/class/DatabaseObjectExistsException.md)

### [**](#DatabaseObjectNotFoundException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L55)DatabaseObjectNotFoundException

Re-exports

<!-- -->

[DatabaseObjectNotFoundException](https://mikro-orm.io/api/core/class/DatabaseObjectNotFoundException.md)

### [**](#DataloaderType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L149)DataloaderType

Re-exports

<!-- -->

[DataloaderType](https://mikro-orm.io/api/core/enum/DataloaderType.md)

### [**](#DataloaderUtils)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/DataloaderUtils.ts#L10)DataloaderUtils

Re-exports

<!-- -->

[DataloaderUtils](https://mikro-orm.io/api/core/class/DataloaderUtils.md)

### [**](#DateTimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)DateTimeType

Re-exports

<!-- -->

[DateTimeType](https://mikro-orm.io/api/core/class/DateTimeType.md)

### [**](#DateType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)DateType

Re-exports

<!-- -->

[DateType](https://mikro-orm.io/api/core/class/DateType.md)

### [**](#DeadlockException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L60)DeadlockException

Re-exports

<!-- -->

[DeadlockException](https://mikro-orm.io/api/core/class/DeadlockException.md)

### [**](#DecimalType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)DecimalType

Re-exports

<!-- -->

[DecimalType](https://mikro-orm.io/api/core/class/DecimalType.md)

### [**](#DeepPartial)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)DeepPartial

Re-exports

<!-- -->

[DeepPartial](https://mikro-orm.io/api/core.md#DeepPartial)

### [**](#DefaultLogger)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L5)DefaultLogger

Re-exports

<!-- -->

[DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

### [**](#DeferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L228)DeferMode

Re-exports

<!-- -->

[DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md)

### [**](#DefineConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)DefineConfig

Re-exports

<!-- -->

[DefineConfig](https://mikro-orm.io/api/core.md#DefineConfig)

### [**](#defineEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L702)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L712)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L720)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L757)defineEntity

Re-exports

<!-- -->

[defineEntity](https://mikro-orm.io/api/core/function/defineEntity.md)

### [**](#DefineEntityHooks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L760)DefineEntityHooks

Re-exports

<!-- -->

[DefineEntityHooks](https://mikro-orm.io/api/core/interface/DefineEntityHooks.md)

### [**](#DeleteOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L273)DeleteOptions

Re-exports

<!-- -->

[DeleteOptions](https://mikro-orm.io/api/core/interface/DeleteOptions.md)

### [**](#DeleteQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2043)DeleteQueryBuilder

Re-exports

<!-- -->

[DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)

### [**](#Dictionary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)Dictionary

Re-exports

<!-- -->

[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#DoubleType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)DoubleType

Re-exports

<!-- -->

[DoubleType](https://mikro-orm.io/api/core/class/DoubleType.md)

### [**](#DriverException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L6)DriverException

Re-exports

<!-- -->

[DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#DriverMethodOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L288)DriverMethodOptions

Re-exports

<!-- -->

[DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

### [**](#DropSchemaOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)DropSchemaOptions

Re-exports

<!-- -->

[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md)

### [**](#DynamicPassword)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L508)DynamicPassword

Re-exports

<!-- -->

[DynamicPassword](https://mikro-orm.io/api/core/interface/DynamicPassword.md)

### [**](#EagerProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)EagerProps

Re-exports

<!-- -->

[EagerProps](https://mikro-orm.io/api/core.md#EagerProps)

### [**](#Edge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/CommitOrderCalculator.ts#L16)Edge

Re-exports

<!-- -->

[Edge](https://mikro-orm.io/api/core/interface/Edge.md)

### [**](#Embeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Embeddable.ts#L4)Embeddable

Re-exports

<!-- -->

[Embeddable](https://mikro-orm.io/api/core/function/Embeddable.md)

### [**](#EmbeddableOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Embeddable.ts#L16)EmbeddableOptions

Re-exports

<!-- -->

[EmbeddableOptions](https://mikro-orm.io/api/core.md#EmbeddableOptions)

### [**](#Embedded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Embedded.ts#L7)Embedded

Re-exports

<!-- -->

[Embedded](https://mikro-orm.io/api/core/function/Embedded.md)

### [**](#EmbeddedOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Embedded.ts#L26)EmbeddedOptions

Re-exports

<!-- -->

[EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)

### [**](#EmbeddedPrefixMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Embedded.ts#L24)EmbeddedPrefixMode

Re-exports

<!-- -->

[EmbeddedPrefixMode](https://mikro-orm.io/api/core.md#EmbeddedPrefixMode)

### [**](#EmptyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L613)EmptyOptions

Re-exports

<!-- -->

[EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md)

### [**](#EnsureDatabaseOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)EnsureDatabaseOptions

Re-exports

<!-- -->

[EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

### [**](#EnsureRequestContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/CreateRequestContext.ts#L35)EnsureRequestContext

Re-exports

<!-- -->

[EnsureRequestContext](https://mikro-orm.io/api/core/function/EnsureRequestContext.md)

### [**](#Entity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Entity.ts#L6)Entity

Re-exports

<!-- -->

[Entity](https://mikro-orm.io/api/core/function/Entity.md)

### [**](#EntityAssigner)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityAssigner.ts#L28)EntityAssigner

Re-exports

<!-- -->

[EntityAssigner](https://mikro-orm.io/api/core/class/EntityAssigner.md)

### [**](#EntityCaseNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L6)EntityCaseNamingStrategy

Re-exports

<!-- -->

[EntityCaseNamingStrategy](https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md)

### [**](#EntityClass)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)EntityClass

Re-exports

<!-- -->

[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)

### [**](#EntityClassGroup)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)EntityClassGroup

Re-exports

<!-- -->

[EntityClassGroup](https://mikro-orm.io/api/core.md#EntityClassGroup)

### [**](#EntityComparator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/EntityComparator.ts#L25)EntityComparator

Re-exports

<!-- -->

[EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

### [**](#EntityData)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)EntityData

Re-exports

<!-- -->

[EntityData](https://mikro-orm.io/api/core.md#EntityData)

### [**](#EntityDataValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)EntityDataValue

Re-exports

<!-- -->

[EntityDataValue](https://mikro-orm.io/api/core.md#EntityDataValue)

### [**](#EntityDictionary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)EntityDictionary

Re-exports

<!-- -->

[EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)

### [**](#EntityDTO)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)EntityDTO

Re-exports

<!-- -->

[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)

### [**](#EntityFactory)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L47)EntityFactory

Re-exports

<!-- -->

[EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

### [**](#EntityField)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L94)EntityField

Re-exports

<!-- -->

[EntityField](https://mikro-orm.io/api/core.md#EntityField)

### [**](#EntityKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)EntityKey

Re-exports

<!-- -->

[EntityKey](https://mikro-orm.io/api/core.md#EntityKey)

### [**](#EntityLoader)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L55)EntityLoader

Re-exports

<!-- -->

[EntityLoader](https://mikro-orm.io/api/core/class/EntityLoader.md)

### [**](#EntityLoaderOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L36)EntityLoaderOptions

Re-exports

<!-- -->

[EntityLoaderOptions](https://mikro-orm.io/api/core.md#EntityLoaderOptions)

### [**](#EntityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/index.ts#L16)EntityManager

Re-exports

<!-- -->

[EntityManager](https://mikro-orm.io/api/knex/class/EntityManager.md)

### [**](#EntityManagerType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L16)EntityManagerType

Re-exports

<!-- -->

[EntityManagerType](https://mikro-orm.io/api/core.md#EntityManagerType)

### [**](#EntityMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)EntityMetadata

Re-exports

<!-- -->

[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)

### [**](#EntityName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)EntityName

Re-exports

<!-- -->

[EntityName](https://mikro-orm.io/api/core.md#EntityName)

### [**](#EntityOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Entity.ts#L18)EntityOptions

Re-exports

<!-- -->

[EntityOptions](https://mikro-orm.io/api/core.md#EntityOptions)

### [**](#EntityProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)EntityProperty

Re-exports

<!-- -->

[EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)

### [**](#EntityProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)EntityProps

Re-exports

<!-- -->

[EntityProps](https://mikro-orm.io/api/core.md#EntityProps)

### [**](#EntityRef)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)EntityRef

Re-exports

<!-- -->

[EntityRef](https://mikro-orm.io/api/core.md#EntityRef)

### [**](#EntityRepository)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/index.ts#L17)EntityRepository

Re-exports

<!-- -->

[EntityRepository](https://mikro-orm.io/api/knex/class/EntityRepository.md)

### [**](#EntityRepositoryType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)EntityRepositoryType

Re-exports

<!-- -->

[EntityRepositoryType](https://mikro-orm.io/api/core.md#EntityRepositoryType)

### [**](#EntitySchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L53)EntitySchema

Re-exports

<!-- -->

[EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)

### [**](#EntitySchemaMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L47)EntitySchemaMetadata

Re-exports

<!-- -->

[EntitySchemaMetadata](https://mikro-orm.io/api/core.md#EntitySchemaMetadata)

### [**](#EntitySchemaProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L38)EntitySchemaProperty

Re-exports

<!-- -->

[EntitySchemaProperty](https://mikro-orm.io/api/core.md#EntitySchemaProperty)

### [**](#EntitySerializer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L59)EntitySerializer

Re-exports

<!-- -->

[EntitySerializer](https://mikro-orm.io/api/core/class/EntitySerializer.md)

### [**](#EntityTransformer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntityTransformer.ts#L27)EntityTransformer

Re-exports

<!-- -->

[EntityTransformer](https://mikro-orm.io/api/core/class/EntityTransformer.md)

### [**](#EntityType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)EntityType

Re-exports

<!-- -->

[EntityType](https://mikro-orm.io/api/core.md#EntityType)

### [**](#EntityValidator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L8)EntityValidator

Re-exports

<!-- -->

[EntityValidator](https://mikro-orm.io/api/core/class/EntityValidator.md)

### [**](#EntityValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)EntityValue

Re-exports

<!-- -->

[EntityValue](https://mikro-orm.io/api/core.md#EntityValue)

### [**](#Enum)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Enum.ts#L7)Enum

Re-exports

<!-- -->

[Enum](https://mikro-orm.io/api/core/function/Enum.md)

### [**](#EnumArrayType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)EnumArrayType

Re-exports

<!-- -->

[EnumArrayType](https://mikro-orm.io/api/core/class/EnumArrayType.md)

### [**](#EnumOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Enum.ts#L22)EnumOptions

Re-exports

<!-- -->

[EnumOptions](https://mikro-orm.io/api/core/interface/EnumOptions.md)

### [**](#EnumType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)EnumType

Re-exports

<!-- -->

[EnumType](https://mikro-orm.io/api/core/class/EnumType.md)

### [**](#equals)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L150)equals

Re-exports

<!-- -->

[equals](https://mikro-orm.io/api/core/function/equals.md)

### [**](#EventArgs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L6)EventArgs

Re-exports

<!-- -->

[EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)

### [**](#EventManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L6)EventManager

Re-exports

<!-- -->

[EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

### [**](#EventSubscriber)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L22)EventSubscriber

Re-exports

<!-- -->

[EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)

### [**](#EventType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L175)EventType

Re-exports

<!-- -->

[EventType](https://mikro-orm.io/api/core/enum/EventType.md)

### [**](#EventTypeMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L197)EventTypeMap

Re-exports

<!-- -->

[EventTypeMap](https://mikro-orm.io/api/core.md#EventTypeMap)

### [**](#ExceptionConverter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/ExceptionConverter.ts#L4)ExceptionConverter

Re-exports

<!-- -->

[ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#ExecuteOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L51)ExecuteOptions

Re-exports

<!-- -->

[ExecuteOptions](https://mikro-orm.io/api/knex/interface/ExecuteOptions.md)

### [**](#ExpandHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)ExpandHint

Re-exports

<!-- -->

[ExpandHint](https://mikro-orm.io/api/core.md#ExpandHint)

### [**](#ExpandProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)ExpandProperty

Re-exports

<!-- -->

[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)

### [**](#ExpandQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)ExpandQuery

Re-exports

<!-- -->

[ExpandQuery](https://mikro-orm.io/api/core.md#ExpandQuery)

### [**](#ExpandScalar)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)ExpandScalar

Re-exports

<!-- -->

[ExpandScalar](https://mikro-orm.io/api/core.md#ExpandScalar)

### [**](#FactoryOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L30)FactoryOptions

Re-exports

<!-- -->

[FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md)

### [**](#Field)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L31)Field

Re-exports

<!-- -->

[Field](https://mikro-orm.io/api/knex.md#Field)

### [**](#FileCacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/FileCacheAdapter.ts#L8)FileCacheAdapter

Re-exports

<!-- -->

[FileCacheAdapter](https://mikro-orm.io/api/core/class/FileCacheAdapter.md)

### [**](#Filter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Filter.ts#L4)Filter

Re-exports

<!-- -->

[Filter](https://mikro-orm.io/api/core/function/Filter.md)

### [**](#FilterItemValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)FilterItemValue

Re-exports

<!-- -->

[FilterItemValue](https://mikro-orm.io/api/core.md#FilterItemValue)

### [**](#FilterKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)FilterKey

Re-exports

<!-- -->

[FilterKey](https://mikro-orm.io/api/core.md#FilterKey)

### [**](#FilterObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)FilterObject

Re-exports

<!-- -->

[FilterObject](https://mikro-orm.io/api/core.md#FilterObject)

### [**](#FilterOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L102)FilterOptions

Re-exports

<!-- -->

[FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#FilterQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)FilterQuery

Re-exports

<!-- -->

[FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)

### [**](#FilterValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)FilterValue

Re-exports

<!-- -->

[FilterValue](https://mikro-orm.io/api/core.md#FilterValue)

### [**](#FindAllOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L98)FindAllOptions

Re-exports

<!-- -->

[FindAllOptions](https://mikro-orm.io/api/core/interface/FindAllOptions.md)

### [**](#FindByCursorOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L204)FindByCursorOptions

Re-exports

<!-- -->

[FindByCursorOptions](https://mikro-orm.io/api/core/interface/FindByCursorOptions.md)

### [**](#FindOneOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L208)FindOneOptions

Re-exports

<!-- -->

[FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)

### [**](#FindOneOrFailOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L213)FindOneOrFailOptions

Re-exports

<!-- -->

[FindOneOrFailOptions](https://mikro-orm.io/api/core/interface/FindOneOrFailOptions.md)

### [**](#FindOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L115)FindOptions

Re-exports

<!-- -->

[FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)

### [**](#FlatQueryOrderMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L102)FlatQueryOrderMap

Re-exports

<!-- -->

[FlatQueryOrderMap](https://mikro-orm.io/api/core/interface/FlatQueryOrderMap.md)

### [**](#FloatType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)FloatType

Re-exports

<!-- -->

[FloatType](https://mikro-orm.io/api/core/class/FloatType.md)

### [**](#FlushEventArgs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L13)FlushEventArgs

Re-exports

<!-- -->

[FlushEventArgs](https://mikro-orm.io/api/core/interface/FlushEventArgs.md)

### [**](#FlushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L5)FlushMode

Re-exports

<!-- -->

[FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

### [**](#ForeignKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L76)ForeignKey

Re-exports

<!-- -->

[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)

### [**](#ForeignKeyConstraintViolationException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L65)ForeignKeyConstraintViolationException

Re-exports

<!-- -->

[ForeignKeyConstraintViolationException](https://mikro-orm.io/api/core/class/ForeignKeyConstraintViolationException.md)

### [**](#ForkOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/EntityManager.ts#L2434)ForkOptions

Re-exports

<!-- -->

[ForkOptions](https://mikro-orm.io/api/core/interface/ForkOptions.md)

### [**](#Formula)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Formula.ts#L7)Formula

Re-exports

<!-- -->

[Formula](https://mikro-orm.io/api/core/function/Formula.md)

### [**](#FormulaOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Formula.ts#L21)FormulaOptions

Re-exports

<!-- -->

[FormulaOptions](https://mikro-orm.io/api/core/interface/FormulaOptions.md)

### [**](#FromEntityType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)FromEntityType

Re-exports

<!-- -->

[FromEntityType](https://mikro-orm.io/api/core.md#FromEntityType)

### [**](#GeneratedCacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/GeneratedCacheAdapter.ts#L4)GeneratedCacheAdapter

Re-exports

<!-- -->

[GeneratedCacheAdapter](https://mikro-orm.io/api/core/class/GeneratedCacheAdapter.md)

### [**](#GenerateOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)GenerateOptions

Re-exports

<!-- -->

[GenerateOptions](https://mikro-orm.io/api/core/interface/GenerateOptions.md)

### [**](#GetReferenceOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L294)GetReferenceOptions

Re-exports

<!-- -->

[GetReferenceOptions](https://mikro-orm.io/api/core/interface/GetReferenceOptions.md)

### [**](#GetRepository)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)GetRepository

Re-exports

<!-- -->

[GetRepository](https://mikro-orm.io/api/core.md#GetRepository)

### [**](#GroupOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L24)GroupOperator

Re-exports

<!-- -->

[GroupOperator](https://mikro-orm.io/api/core/enum/GroupOperator.md)

### [**](#Hidden)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)Hidden

Re-exports

<!-- -->

[Hidden](https://mikro-orm.io/api/core.md#Hidden)

### [**](#HiddenProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)HiddenProps

Re-exports

<!-- -->

[HiddenProps](https://mikro-orm.io/api/core.md#HiddenProps)

### [**](#Highlighter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)Highlighter

Re-exports

<!-- -->

[Highlighter](https://mikro-orm.io/api/core/interface/Highlighter.md)

### [**](#Hydrator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/hydration/Hydrator.ts#L8)Hydrator

Re-exports

<!-- -->

[Hydrator](https://mikro-orm.io/api/core/class/Hydrator.md)

### [**](#IConfiguration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L6)IConfiguration

Re-exports

<!-- -->

[IConfiguration](https://mikro-orm.io/api/core/interface/IConfiguration.md)

### [**](#ICriteriaNode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L196)ICriteriaNode

Re-exports

<!-- -->

[ICriteriaNode](https://mikro-orm.io/api/knex/interface/ICriteriaNode.md)

### [**](#ICriteriaNodeProcessOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L187)ICriteriaNodeProcessOptions

Re-exports

<!-- -->

[ICriteriaNodeProcessOptions](https://mikro-orm.io/api/knex/interface/ICriteriaNodeProcessOptions.md)

### [**](#IDatabaseDriver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L18)IDatabaseDriver

Re-exports

<!-- -->

[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)

### [**](#IdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L3)IdentityMap

Re-exports

<!-- -->

[IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

### [**](#IEntityGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)IEntityGenerator

Re-exports

<!-- -->

[IEntityGenerator](https://mikro-orm.io/api/core/interface/IEntityGenerator.md)

### [**](#IMigrationGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)IMigrationGenerator

Re-exports

<!-- -->

[IMigrationGenerator](https://mikro-orm.io/api/core/interface/IMigrationGenerator.md)

### [**](#IMigrator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)IMigrator

Re-exports

<!-- -->

[IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#ImportsResolver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)ImportsResolver

Re-exports

<!-- -->

[ImportsResolver](https://mikro-orm.io/api/core.md#ImportsResolver)

### [**](#Index)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L21)Index

Re-exports

<!-- -->

[Index](https://mikro-orm.io/api/core/function/Index.md)

### [**](#IndexCallback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)IndexCallback

Re-exports

<!-- -->

[IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)

### [**](#IndexDef)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L87)IndexDef

Re-exports

<!-- -->

[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

### [**](#IndexOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L42)IndexOptions

Re-exports

<!-- -->

[IndexOptions](https://mikro-orm.io/api/core/interface/IndexOptions.md)

### [**](#InferEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L856)InferEntity

Re-exports

<!-- -->

[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)

### [**](#InferEntityFromProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L798)InferEntityFromProperties

Re-exports

<!-- -->

[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)

### [**](#InferPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L810)InferPrimaryKey

Re-exports

<!-- -->

[InferPrimaryKey](https://mikro-orm.io/api/core.md#InferPrimaryKey)

### [**](#InitCollectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L496)InitCollectionOptions

Re-exports

<!-- -->

[InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)

### [**](#InsertQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2039)InsertQueryBuilder

Re-exports

<!-- -->

[InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)

### [**](#IntegerType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)IntegerType

Re-exports

<!-- -->

[IntegerType](https://mikro-orm.io/api/core/class/IntegerType.md)

### [**](#IntervalType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)IntervalType

Re-exports

<!-- -->

[IntervalType](https://mikro-orm.io/api/core/class/IntervalType.md)

### [**](#InvalidFieldNameException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L75)InvalidFieldNameException

Re-exports

<!-- -->

[InvalidFieldNameException](https://mikro-orm.io/api/core/class/InvalidFieldNameException.md)

### [**](#IPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)IPrimaryKey

Re-exports

<!-- -->

[IPrimaryKey](https://mikro-orm.io/api/core.md#IPrimaryKey)

### [**](#IQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L147)IQueryBuilder

Re-exports

<!-- -->

[IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)

### [**](#ISchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)ISchemaGenerator

Re-exports

<!-- -->

[ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

### [**](#ISeedManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)ISeedManager

Re-exports

<!-- -->

[ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

### [**](#IsolationLevel)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L167)IsolationLevel

Re-exports

<!-- -->

[IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

### [**](#IsSubset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)IsSubset

Re-exports

<!-- -->

[IsSubset](https://mikro-orm.io/api/core.md#IsSubset)

### [**](#IsUnknown)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)IsUnknown

Re-exports

<!-- -->

[IsUnknown](https://mikro-orm.io/api/core.md#IsUnknown)

### [**](#IType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)IType

Re-exports

<!-- -->

[IType](https://mikro-orm.io/api/core.md#IType)

### [**](#IWrappedEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)IWrappedEntity

Re-exports

<!-- -->

[IWrappedEntity](https://mikro-orm.io/api/core/interface/IWrappedEntity.md)

### [**](#JoinOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L33)JoinOptions

Re-exports

<!-- -->

[JoinOptions](https://mikro-orm.io/api/knex/interface/JoinOptions.md)

### [**](#JoinType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/enums.ts#L11)JoinType

Re-exports

<!-- -->

[JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md)

### [**](#JSON_KEY_OPERATORS)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L67)JSON\_KEY\_OPERATORS

Re-exports

<!-- -->

[JSON\_KEY\_OPERATORS](https://mikro-orm.io/api/core.md#JSON_KEY_OPERATORS)

### [**](#JsonProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L40)JsonProperty

Re-exports

<!-- -->

[JsonProperty](https://mikro-orm.io/api/core.md#JsonProperty)

### [**](#JsonType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)JsonType

Re-exports

<!-- -->

[JsonType](https://mikro-orm.io/api/core/class/JsonType.md)

### [**](#KnexStringRef)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L25)KnexStringRef

Re-exports

<!-- -->

[KnexStringRef](https://mikro-orm.io/api/knex.md#KnexStringRef)

### [**](#LibSqlKnexDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/LibSqlKnexDialect.ts#L4)LibSqlKnexDialect

Re-exports

<!-- -->

[LibSqlKnexDialect](https://mikro-orm.io/api/knex/class/LibSqlKnexDialect.md)

### [**](#LoadCountOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L502)LoadCountOptions

Re-exports

<!-- -->

[LoadCountOptions](https://mikro-orm.io/api/core/interface/LoadCountOptions.md)

### [**](#Loaded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)Loaded

Re-exports

<!-- -->

[Loaded](https://mikro-orm.io/api/core.md#Loaded)

### [**](#LoadedCollection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)LoadedCollection

Re-exports

<!-- -->

[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)

### [**](#LoadedReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)LoadedReference

Re-exports

<!-- -->

[LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)

### [**](#LoadHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L104)LoadHint

Re-exports

<!-- -->

[LoadHint](https://mikro-orm.io/api/core/interface/LoadHint.md)

### [**](#LoadReferenceOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L301)LoadReferenceOptions

Re-exports

<!-- -->

[LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)

### [**](#LoadReferenceOrFailOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L305)LoadReferenceOrFailOptions

Re-exports

<!-- -->

[LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)

### [**](#LoadStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L143)LoadStrategy

Re-exports

<!-- -->

[LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md)

### [**](#LockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L156)LockMode

Re-exports

<!-- -->

[LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)

### [**](#LockOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L281)LockOptions

Re-exports

<!-- -->

[LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

### [**](#LockWaitTimeoutException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L80)LockWaitTimeoutException

Re-exports

<!-- -->

[LockWaitTimeoutException](https://mikro-orm.io/api/core/class/LockWaitTimeoutException.md)

### [**](#LogContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L36)LogContext

Re-exports

<!-- -->

[LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

### [**](#Logger)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L3)Logger

Re-exports

<!-- -->

[Logger](https://mikro-orm.io/api/core/interface/Logger.md)

### [**](#LoggerNamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L34)LoggerNamespace

Re-exports

<!-- -->

[LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

### [**](#LoggerOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L52)LoggerOptions

Re-exports

<!-- -->

[LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

### [**](#LoggingOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L69)LoggingOptions

Re-exports

<!-- -->

[LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#ManyToMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToMany.ts#L7)ManyToMany

Re-exports

<!-- -->

[ManyToMany](https://mikro-orm.io/api/core/function/ManyToMany.md)

### [**](#ManyToManyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToMany.ts#L23)ManyToManyOptions

Re-exports

<!-- -->

[ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)

### [**](#ManyToOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L7)ManyToOne

Re-exports

<!-- -->

[ManyToOne](https://mikro-orm.io/api/core/function/ManyToOne.md)

### [**](#ManyToOneOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/ManyToOne.ts#L22)ManyToOneOptions

Re-exports

<!-- -->

[ManyToOneOptions](https://mikro-orm.io/api/core/interface/ManyToOneOptions.md)

### [**](#MariaDbKnexDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MariaDbKnexDialect.ts#L3)MariaDbKnexDialect

Re-exports

<!-- -->

[MariaDbKnexDialect](https://mikro-orm.io/api/knex/class/MariaDbKnexDialect.md)

### [**](#MatchingOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L25)MatchingOptions

Re-exports

<!-- -->

[MatchingOptions](https://mikro-orm.io/api/core/interface/MatchingOptions.md)

### [**](#MaybePromise)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)MaybePromise

Re-exports

<!-- -->

[MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)

### [**](#MediumIntType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)MediumIntType

Re-exports

<!-- -->

[MediumIntType](https://mikro-orm.io/api/core/class/MediumIntType.md)

### [**](#MemoryCacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/MemoryCacheAdapter.ts#L3)MemoryCacheAdapter

Re-exports

<!-- -->

[MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md)

### [**](#MergeLoaded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)MergeLoaded

Re-exports

<!-- -->

[MergeLoaded](https://mikro-orm.io/api/core.md#MergeLoaded)

### [**](#MergeOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/EntityManager.ts#L2424)MergeOptions

Re-exports

<!-- -->

[MergeOptions](https://mikro-orm.io/api/core/interface/MergeOptions.md)

### [**](#MergeSelected)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)MergeSelected

Re-exports

<!-- -->

[MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)

### [**](#MetadataDiscovery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataDiscovery.ts#L43)MetadataDiscovery

Re-exports

<!-- -->

[MetadataDiscovery](https://mikro-orm.io/api/core/class/MetadataDiscovery.md)

### [**](#MetadataDiscoveryOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L577)MetadataDiscoveryOptions

Re-exports

<!-- -->

[MetadataDiscoveryOptions](https://mikro-orm.io/api/core/interface/MetadataDiscoveryOptions.md)

### [**](#MetadataError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/errors.ts#L172)MetadataError

Re-exports

<!-- -->

[MetadataError](https://mikro-orm.io/api/core/class/MetadataError.md)

### [**](#MetadataProcessor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)MetadataProcessor

Re-exports

<!-- -->

[MetadataProcessor](https://mikro-orm.io/api/core.md#MetadataProcessor)

### [**](#MetadataProvider)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L11)MetadataProvider

Re-exports

<!-- -->

[MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

### [**](#MetadataStorage)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L7)MetadataStorage

Re-exports

<!-- -->

[MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#MigrateOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)MigrateOptions

Re-exports

<!-- -->

[MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions)

### [**](#MigrationDiff)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)MigrationDiff

Re-exports

<!-- -->

[MigrationDiff](https://mikro-orm.io/api/core/interface/MigrationDiff.md)

### [**](#MigrationObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L9)MigrationObject

Re-exports

<!-- -->

[MigrationObject](https://mikro-orm.io/api/core/interface/MigrationObject.md)

### [**](#MigrationResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)MigrationResult

Re-exports

<!-- -->

[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)

### [**](#MigrationRow)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)MigrationRow

Re-exports

<!-- -->

[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)

### [**](#MigrationsOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L529)MigrationsOptions

Re-exports

<!-- -->

[MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

### [**](#MigratorEvent)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)MigratorEvent

Re-exports

<!-- -->

[MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)

### [**](#MikroORMOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L593)MikroORMOptions

Re-exports

<!-- -->

[MikroORMOptions](https://mikro-orm.io/api/core/interface/MikroORMOptions.md)

### [**](#ModifyContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L100)ModifyContext

Re-exports

<!-- -->

[ModifyContext](https://mikro-orm.io/api/knex.md#ModifyContext)

### [**](#ModifyHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L98)ModifyHint

Re-exports

<!-- -->

[ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)

### [**](#MongoNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/MongoNamingStrategy.ts#L3)MongoNamingStrategy

Re-exports

<!-- -->

[MongoNamingStrategy](https://mikro-orm.io/api/core/class/MongoNamingStrategy.md)

### [**](#MonkeyPatchable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/MonkeyPatchable.ts#L38)MonkeyPatchable

Re-exports

<!-- -->

[MonkeyPatchable](https://mikro-orm.io/api/knex.md#MonkeyPatchable)

### [**](#MsSqlKnexDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mssql/MsSqlKnexDialect.ts#L6)MsSqlKnexDialect

Re-exports

<!-- -->

[MsSqlKnexDialect](https://mikro-orm.io/api/knex/class/MsSqlKnexDialect.md)

### [**](#MySqlConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlConnection.ts#L5)MySqlConnection

Re-exports

<!-- -->

[MySqlConnection](https://mikro-orm.io/api/knex/class/MySqlConnection.md)

### [**](#MySqlExceptionConverter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlExceptionConverter.ts#L7)MySqlExceptionConverter

Re-exports

<!-- -->

[MySqlExceptionConverter](https://mikro-orm.io/api/knex/class/MySqlExceptionConverter.md)

### [**](#MySqlIncrementOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L213)MySqlIncrementOptions

Re-exports

<!-- -->

[MySqlIncrementOptions](https://mikro-orm.io/api/knex.md#MySqlIncrementOptions)

### [**](#MySqlKnexDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlKnexDialect.ts#L5)MySqlKnexDialect

Re-exports

<!-- -->

[MySqlKnexDialect](https://mikro-orm.io/api/knex/class/MySqlKnexDialect.md)

### [**](#MySqlPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L16)MySqlPlatform

Re-exports

<!-- -->

[MySqlPlatform](https://mikro-orm.io/api/knex/class/MySqlPlatform.md)

### [**](#MySqlSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L9)MySqlSchemaHelper

Re-exports

<!-- -->

[MySqlSchemaHelper](https://mikro-orm.io/api/knex/class/MySqlSchemaHelper.md)

### [**](#MySqlTableBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L215)MySqlTableBuilder

Re-exports

<!-- -->

[MySqlTableBuilder](https://mikro-orm.io/api/knex/interface/MySqlTableBuilder.md)

### [**](#NamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L3)NamingStrategy

Re-exports

<!-- -->

[NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#NativeDeleteOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L277)NativeDeleteOptions

Re-exports

<!-- -->

[NativeDeleteOptions](https://mikro-orm.io/api/core/interface/NativeDeleteOptions.md)

### [**](#NativeInsertUpdateManyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L227)NativeInsertUpdateManyOptions

Re-exports

<!-- -->

[NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)

### [**](#NativeInsertUpdateOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L218)NativeInsertUpdateOptions

Re-exports

<!-- -->

[NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)

### [**](#New)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)New

Re-exports

<!-- -->

[New](https://mikro-orm.io/api/core.md#New)

### [**](#Node)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/CommitOrderCalculator.ts#L10)Node

Re-exports

<!-- -->

[Node](https://mikro-orm.io/api/core/interface/Node.md)

### [**](#NodeState)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/CommitOrderCalculator.ts#L4)NodeState

Re-exports

<!-- -->

[NodeState](https://mikro-orm.io/api/core/enum/NodeState.md)

### [**](#NoInfer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)NoInfer

Re-exports

<!-- -->

[NoInfer](https://mikro-orm.io/api/core.md#NoInfer)

### [**](#NonUniqueFieldNameException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L85)NonUniqueFieldNameException

Re-exports

<!-- -->

[NonUniqueFieldNameException](https://mikro-orm.io/api/core/class/NonUniqueFieldNameException.md)

### [**](#NotFoundError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/errors.ts#L293)NotFoundError

Re-exports

<!-- -->

[NotFoundError](https://mikro-orm.io/api/core/class/NotFoundError.md)

### [**](#NotNullConstraintViolationException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L90)NotNullConstraintViolationException

Re-exports

<!-- -->

[NotNullConstraintViolationException](https://mikro-orm.io/api/core/class/NotNullConstraintViolationException.md)

### [**](#NullCacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/NullCacheAdapter.ts#L3)NullCacheAdapter

Re-exports

<!-- -->

[NullCacheAdapter](https://mikro-orm.io/api/core/class/NullCacheAdapter.md)

### [**](#NullHighlighter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/NullHighlighter.ts#L3)NullHighlighter

Re-exports

<!-- -->

[NullHighlighter](https://mikro-orm.io/api/core/class/NullHighlighter.md)

### [**](#ObjectBindingPattern)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L27)ObjectBindingPattern

Re-exports

<!-- -->

[ObjectBindingPattern](https://mikro-orm.io/api/core.md#ObjectBindingPattern)

### [**](#ObjectHydrator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/hydration/ObjectHydrator.ts#L12)ObjectHydrator

Re-exports

<!-- -->

[ObjectHydrator](https://mikro-orm.io/api/core/class/ObjectHydrator.md)

### [**](#ObjectQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)ObjectQuery

Re-exports

<!-- -->

[ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)

### [**](#OneToMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/index.ts#L7)OneToMany

Re-exports

<!-- -->

[OneToMany](https://mikro-orm.io/api/core/function/OneToMany.md)

### [**](#OneToManyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/index.ts#L7)OneToManyOptions

Re-exports

<!-- -->

[OneToManyOptions](https://mikro-orm.io/api/core/interface/OneToManyOptions.md)

### [**](#OneToOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/OneToOne.ts#L5)OneToOne

Re-exports

<!-- -->

[OneToOne](https://mikro-orm.io/api/core/function/OneToOne.md)

### [**](#OneToOneOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/OneToOne.ts#L15)OneToOneOptions

Re-exports

<!-- -->

[OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)

### [**](#OnInit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L40)OnInit

Re-exports

<!-- -->

[OnInit](https://mikro-orm.io/api/core/function/OnInit.md)

### [**](#OnLoad)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/hooks.ts#L44)OnLoad

Re-exports

<!-- -->

[OnLoad](https://mikro-orm.io/api/core/function/OnLoad.md)

### [**](#Opt)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)Opt

Re-exports

<!-- -->

[Opt](https://mikro-orm.io/api/core.md#Opt)

### [**](#OptimisticLockError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/errors.ts#L150)OptimisticLockError

Re-exports

<!-- -->

[OptimisticLockError](https://mikro-orm.io/api/core/class/OptimisticLockError.md)

### [**](#OptionalProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)OptionalProps

Re-exports

<!-- -->

[OptionalProps](https://mikro-orm.io/api/core.md#OptionalProps)

### [**](#OrderDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L96)OrderDefinition

Re-exports

<!-- -->

[OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)

### [**](#p)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L758)p

Re-exports

<!-- -->

[p](https://mikro-orm.io/api/core.md#p)

### [**](#parseJsonSafe)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L172)parseJsonSafe

Re-exports

<!-- -->

[parseJsonSafe](https://mikro-orm.io/api/core/function/parseJsonSafe.md)

### [**](#PlainObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L225)PlainObject

Re-exports

<!-- -->

[PlainObject](https://mikro-orm.io/api/core/class/PlainObject.md)

### [**](#Platform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L42)Platform

Re-exports

<!-- -->

[Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#PoolConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L557)PoolConfig

Re-exports

<!-- -->

[PoolConfig](https://mikro-orm.io/api/core/interface/PoolConfig.md)

### [**](#Populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)Populate

Re-exports

<!-- -->

[Populate](https://mikro-orm.io/api/core.md#Populate)

### [**](#PopulateHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L14)PopulateHint

Re-exports

<!-- -->

[PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md)

### [**](#PopulateOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)PopulateOptions

Re-exports

<!-- -->

[PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)

### [**](#PopulatePath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L19)PopulatePath

Re-exports

<!-- -->

[PopulatePath](https://mikro-orm.io/api/core/enum/PopulatePath.md)

### [**](#PostgreSqlKnexDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/postgresql/PostgreSqlKnexDialect.ts#L6)PostgreSqlKnexDialect

Re-exports

<!-- -->

[PostgreSqlKnexDialect](https://mikro-orm.io/api/knex/class/PostgreSqlKnexDialect.md)

### [**](#Primary)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)Primary

Re-exports

<!-- -->

[Primary](https://mikro-orm.io/api/core.md#Primary)

### [**](#PrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/PrimaryKey.ts#L19)PrimaryKey

Re-exports

<!-- -->

[PrimaryKey](https://mikro-orm.io/api/core/function/PrimaryKey.md)

### [**](#PrimaryKeyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/PrimaryKey.ts#L27)PrimaryKeyOptions

Re-exports

<!-- -->

[PrimaryKeyOptions](https://mikro-orm.io/api/core/interface/PrimaryKeyOptions.md)

### [**](#PrimaryKeyProp)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L7)PrimaryKeyProp

Re-exports

<!-- -->

[PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)

### [**](#Property)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L19)Property

Re-exports

<!-- -->

[Property](https://mikro-orm.io/api/core/function/Property.md)

### [**](#PropertyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L54)PropertyOptions

Re-exports

<!-- -->

[PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)

### [**](#QBField)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L114)QBField

Re-exports

<!-- -->

[QBField](https://mikro-orm.io/api/knex.md#QBField)

### [**](#QBField2)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L115)QBField2

Re-exports

<!-- -->

[QBField2](https://mikro-orm.io/api/knex.md#QBField2)

### [**](#QBFilterQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L8)QBFilterQuery

Re-exports

<!-- -->

[QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

### [**](#QBQueryOrderMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L100)QBQueryOrderMap

Re-exports

<!-- -->

[QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)

### [**](#QueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L138)QueryBuilder

Re-exports

<!-- -->

[QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)

### [**](#QueryFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L106)QueryFlag

Re-exports

<!-- -->

[QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

### [**](#QueryOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L29)QueryOperator

Re-exports

<!-- -->

[QueryOperator](https://mikro-orm.io/api/core/enum/QueryOperator.md)

### [**](#QueryOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L73)QueryOrder

Re-exports

<!-- -->

[QueryOrder](https://mikro-orm.io/api/core/enum/QueryOrder.md)

### [**](#QueryOrderKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L94)QueryOrderKeys

Re-exports

<!-- -->

[QueryOrderKeys](https://mikro-orm.io/api/core.md#QueryOrderKeys)

### [**](#QueryOrderKeysFlat)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L93)QueryOrderKeysFlat

Re-exports

<!-- -->

[QueryOrderKeysFlat](https://mikro-orm.io/api/core.md#QueryOrderKeysFlat)

### [**](#QueryOrderMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L96)QueryOrderMap

Re-exports

<!-- -->

[QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)

### [**](#QueryOrderNumeric)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L88)QueryOrderNumeric

Re-exports

<!-- -->

[QueryOrderNumeric](https://mikro-orm.io/api/core/enum/QueryOrderNumeric.md)

### [**](#QueryResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L174)QueryResult

Re-exports

<!-- -->

[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)

### [**](#QueryType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/enums.ts#L1)QueryType

Re-exports

<!-- -->

[QueryType](https://mikro-orm.io/api/knex/enum/QueryType.md)

### [**](#quote)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L279)quote

Re-exports

<!-- -->

[quote](https://mikro-orm.io/api/core/function/quote.md)

### [**](#raw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/index.ts#L9)raw

Re-exports

<!-- -->

[raw](https://mikro-orm.io/api/knex/function/raw.md)

### [**](#RawQueryFragment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L6)RawQueryFragment

Re-exports

<!-- -->

[RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

### [**](#ReadOnlyException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L95)ReadOnlyException

Re-exports

<!-- -->

[ReadOnlyException](https://mikro-orm.io/api/core/class/ReadOnlyException.md)

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L312)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L317)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L322)ref

Re-exports

<!-- -->

[ref](https://mikro-orm.io/api/core/function/ref.md)

### [**](#Ref)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)Ref

Re-exports

<!-- -->

[Ref](https://mikro-orm.io/api/core.md#Ref)

### [**](#Reference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L21)Reference

Re-exports

<!-- -->

[Reference](https://mikro-orm.io/api/core/class/Reference.md)

### [**](#ReferenceKind)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L122)ReferenceKind

Re-exports

<!-- -->

[ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

### [**](#ReferenceOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Property.ts#L331)ReferenceOptions

Re-exports

<!-- -->

[ReferenceOptions](https://mikro-orm.io/api/core/interface/ReferenceOptions.md)

### [**](#ReflectMetadataProvider)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/ReflectMetadataProvider.ts#L7)ReflectMetadataProvider

Re-exports

<!-- -->

[ReflectMetadataProvider](https://mikro-orm.io/api/core/class/ReflectMetadataProvider.md)

### [**](#RefreshDatabaseOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)RefreshDatabaseOptions

Re-exports

<!-- -->

[RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

### [**](#RegisterOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L1269)RegisterOptions

Re-exports

<!-- -->

[RegisterOptions](https://mikro-orm.io/api/core/interface/RegisterOptions.md)

### [**](#rel)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L349)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L354)rel

Re-exports

<!-- -->

[rel](https://mikro-orm.io/api/core/function/rel.md)

### [**](#Rel)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)Rel

Re-exports

<!-- -->

[Rel](https://mikro-orm.io/api/core.md#Rel)

### [**](#RequestContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RequestContext.ts#L8)RequestContext

Re-exports

<!-- -->

[RequestContext](https://mikro-orm.io/api/core/class/RequestContext.md)

### [**](#RequiredEntityData)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)RequiredEntityData

Re-exports

<!-- -->

[RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)

### [**](#RequiredNullable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)RequiredNullable

Re-exports

<!-- -->

[RequiredNullable](https://mikro-orm.io/api/core.md#RequiredNullable)

### [**](#RunQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2012)RunQueryBuilder

Re-exports

<!-- -->

[RunQueryBuilder](https://mikro-orm.io/api/knex/interface/RunQueryBuilder.md)

### [**](#Scalar)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)Scalar

Re-exports

<!-- -->

[Scalar](https://mikro-orm.io/api/core.md#Scalar)

### [**](#SCALAR_TYPES)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L120)SCALAR\_TYPES

Re-exports

<!-- -->

[SCALAR\_TYPES](https://mikro-orm.io/api/core.md#SCALAR_TYPES)

### [**](#ScalarRef)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)ScalarRef

Re-exports

<!-- -->

[ScalarRef](https://mikro-orm.io/api/core.md#ScalarRef)

### [**](#ScalarReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L215)ScalarReference

Re-exports

<!-- -->

[ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)

### [**](#SchemaComparator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L22)SchemaComparator

Re-exports

<!-- -->

[SchemaComparator](https://mikro-orm.io/api/knex/class/SchemaComparator.md)

### [**](#SchemaDifference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L135)SchemaDifference

Re-exports

<!-- -->

[SchemaDifference](https://mikro-orm.io/api/knex/interface/SchemaDifference.md)

### [**](#SchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L658)SchemaGenerator

Re-exports

<!-- -->

[SchemaGenerator](https://mikro-orm.io/api/knex.md#SchemaGenerator)

### [**](#SchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L16)SchemaHelper

Re-exports

<!-- -->

[SchemaHelper](https://mikro-orm.io/api/knex/class/SchemaHelper.md)

### [**](#SeederOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L548)SeederOptions

Re-exports

<!-- -->

[SeederOptions](https://mikro-orm.io/api/core/interface/SeederOptions.md)

### [**](#Selected)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)Selected

Re-exports

<!-- -->

[Selected](https://mikro-orm.io/api/core.md#Selected)

### [**](#SelectQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2018)SelectQueryBuilder

Re-exports

<!-- -->

[SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)

### [**](#SerializationContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L11)SerializationContext

Re-exports

<!-- -->

[SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L322)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L342)serialize

Re-exports

<!-- -->

[serialize](https://mikro-orm.io/api/core/function/serialize.md)

### [**](#SerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/PrimaryKey.ts#L23)SerializedPrimaryKey

Re-exports

<!-- -->

[SerializedPrimaryKey](https://mikro-orm.io/api/core/function/SerializedPrimaryKey.md)

### [**](#SerializedPrimaryKeyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/PrimaryKey.ts#L29)SerializedPrimaryKeyOptions

Re-exports

<!-- -->

[SerializedPrimaryKeyOptions](https://mikro-orm.io/api/core/interface/SerializedPrimaryKeyOptions.md)

### [**](#SerializeOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/EntitySerializer.ts#L287)SerializeOptions

Re-exports

<!-- -->

[SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)

### [**](#ServerException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L32)ServerException

Re-exports

<!-- -->

[ServerException](https://mikro-orm.io/api/core/class/ServerException.md)

### [**](#Settings)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/ConfigurationLoader.ts#L447)Settings

Re-exports

<!-- -->

[Settings](https://mikro-orm.io/api/core/interface/Settings.md)

### [**](#SimpleColumnMeta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L10)SimpleColumnMeta

Re-exports

<!-- -->

[SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)

### [**](#SimpleLogger)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/SimpleLogger.ts#L7)SimpleLogger

Re-exports

<!-- -->

[SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

### [**](#SmallIntType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)SmallIntType

Re-exports

<!-- -->

[SmallIntType](https://mikro-orm.io/api/core/class/SmallIntType.md)

### [**](#sql)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L244)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L261)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L262)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L263)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L264)sql

Re-exports

<!-- -->

[sql](https://mikro-orm.io/api/core/function/sql.md)

### [**](#SqlEntityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/SqlEntityManager.ts#L21)SqlEntityManager

Renames and re-exports

<!-- -->

[EntityManager](https://mikro-orm.io/api/knex/class/EntityManager.md)

### [**](#SqlEntityRepository)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/SqlEntityRepository.ts#L6)SqlEntityRepository

Renames and re-exports

<!-- -->

[EntityRepository](https://mikro-orm.io/api/knex/class/EntityRepository.md)

### [**](#SqliteKnexDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/SqliteKnexDialect.ts#L4)SqliteKnexDialect

Re-exports

<!-- -->

[SqliteKnexDialect](https://mikro-orm.io/api/knex/class/SqliteKnexDialect.md)

### [**](#SqliteTableCompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/SqliteTableCompiler.ts#L4)SqliteTableCompiler

Re-exports

<!-- -->

[SqliteTableCompiler](https://mikro-orm.io/api/knex/class/SqliteTableCompiler.md)

### [**](#SqlSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L21)SqlSchemaGenerator

Re-exports

<!-- -->

[SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

### [**](#StringType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)StringType

Re-exports

<!-- -->

[StringType](https://mikro-orm.io/api/core/class/StringType.md)

### [**](#SyncCacheAdapter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/CacheAdapter.ts#L30)SyncCacheAdapter

Re-exports

<!-- -->

[SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

### [**](#SyntaxErrorException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L100)SyntaxErrorException

Re-exports

<!-- -->

[SyntaxErrorException](https://mikro-orm.io/api/core/class/SyntaxErrorException.md)

### [**](#t)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L60)t

Re-exports

<!-- -->

[t](https://mikro-orm.io/api/core.md#t)

### [**](#Table)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L19)Table

Re-exports

<!-- -->

[Table](https://mikro-orm.io/api/knex/interface/Table.md)

### [**](#TableDifference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L114)TableDifference

Re-exports

<!-- -->

[TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)

### [**](#TableExistsException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L105)TableExistsException

Re-exports

<!-- -->

[TableExistsException](https://mikro-orm.io/api/core/class/TableExistsException.md)

### [**](#TableNotFoundException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L110)TableNotFoundException

Re-exports

<!-- -->

[TableNotFoundException](https://mikro-orm.io/api/core/class/TableNotFoundException.md)

### [**](#TextType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)TextType

Re-exports

<!-- -->

[TextType](https://mikro-orm.io/api/core/class/TextType.md)

### [**](#TimeType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)TimeType

Re-exports

<!-- -->

[TimeType](https://mikro-orm.io/api/core/class/TimeType.md)

### [**](#TinyIntType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L29)TinyIntType

Re-exports

<!-- -->

[TinyIntType](https://mikro-orm.io/api/core/class/TinyIntType.md)

### [**](#Transaction)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L191)Transaction

Re-exports

<!-- -->

[Transaction](https://mikro-orm.io/api/core.md#Transaction)

### [**](#Transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Transactional.ts#L15)Transactional

Re-exports

<!-- -->

[Transactional](https://mikro-orm.io/api/core/function/Transactional.md)

### [**](#TransactionContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionContext.ts#L4)TransactionContext

Re-exports

<!-- -->

[TransactionContext](https://mikro-orm.io/api/core/class/TransactionContext.md)

### [**](#TransactionEventArgs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L17)TransactionEventArgs

Re-exports

<!-- -->

[TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

### [**](#TransactionEventBroadcaster)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/TransactionEventBroadcaster.ts#L7)TransactionEventBroadcaster

Re-exports

<!-- -->

[TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

### [**](#TransactionEventType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L202)TransactionEventType

Re-exports

<!-- -->

[TransactionEventType](https://mikro-orm.io/api/core.md#TransactionEventType)

### [**](#TransactionManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionManager.ts#L12)TransactionManager

Re-exports

<!-- -->

[TransactionManager](https://mikro-orm.io/api/core/class/TransactionManager.md)

### [**](#TransactionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L214)TransactionOptions

Re-exports

<!-- -->

[TransactionOptions](https://mikro-orm.io/api/core/interface/TransactionOptions.md)

### [**](#TransactionPropagation)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L204)TransactionPropagation

Re-exports

<!-- -->

[TransactionPropagation](https://mikro-orm.io/api/core/enum/TransactionPropagation.md)

### [**](#TransactionStateError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/errors.ts#L305)TransactionStateError

Re-exports

<!-- -->

[TransactionStateError](https://mikro-orm.io/api/core/class/TransactionStateError.md)

### [**](#TransformContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)TransformContext

Re-exports

<!-- -->

[TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

### [**](#TruncateQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2045)TruncateQueryBuilder

Re-exports

<!-- -->

[TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)

### [**](#Type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)Type

Re-exports

<!-- -->

[Type](https://mikro-orm.io/api/core/class/Type.md)

### [**](#TypeConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L12)TypeConfig

Re-exports

<!-- -->

[TypeConfig](https://mikro-orm.io/api/core/interface/TypeConfig.md)

### [**](#types)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L33)types

Re-exports

<!-- -->

[types](https://mikro-orm.io/api/core.md#types)

### [**](#Uint8ArrayType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L28)Uint8ArrayType

Re-exports

<!-- -->

[Uint8ArrayType](https://mikro-orm.io/api/core/class/Uint8ArrayType.md)

### [**](#UmzugMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L11)UmzugMigration

Re-exports

<!-- -->

[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)

### [**](#UnboxArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)UnboxArray

Re-exports

<!-- -->

[UnboxArray](https://mikro-orm.io/api/core.md#UnboxArray)

### [**](#UnderscoreNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/UnderscoreNamingStrategy.ts#L3)UnderscoreNamingStrategy

Re-exports

<!-- -->

[UnderscoreNamingStrategy](https://mikro-orm.io/api/core/class/UnderscoreNamingStrategy.md)

### [**](#Unique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L25)Unique

Re-exports

<!-- -->

[Unique](https://mikro-orm.io/api/core/function/Unique.md)

### [**](#UniqueConstraintViolationException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/exceptions.ts#L115)UniqueConstraintViolationException

Re-exports

<!-- -->

[UniqueConstraintViolationException](https://mikro-orm.io/api/core/class/UniqueConstraintViolationException.md)

### [**](#UniqueOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/decorators/Indexed.ts#L38)UniqueOptions

Re-exports

<!-- -->

[UniqueOptions](https://mikro-orm.io/api/core/interface/UniqueOptions.md)

### [**](#UnitOfWork)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L32)UnitOfWork

Re-exports

<!-- -->

[UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)

### [**](#UniversalPropertyKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L35)UniversalPropertyKeys

Re-exports

<!-- -->

[UniversalPropertyKeys](https://mikro-orm.io/api/core.md#UniversalPropertyKeys)

### [**](#UnknownType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)UnknownType

Re-exports

<!-- -->

[UnknownType](https://mikro-orm.io/api/core/class/UnknownType.md)

### [**](#UpdateOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L267)UpdateOptions

Re-exports

<!-- -->

[UpdateOptions](https://mikro-orm.io/api/core/interface/UpdateOptions.md)

### [**](#UpdateQueryBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2041)UpdateQueryBuilder

Re-exports

<!-- -->

[UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)

### [**](#UpdateSchemaOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/index.ts#L13)UpdateSchemaOptions

Re-exports

<!-- -->

[UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)

### [**](#UpsertManyOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L239)UpsertManyOptions

Re-exports

<!-- -->

[UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)

### [**](#UpsertOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L231)UpsertOptions

Re-exports

<!-- -->

[UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)

### [**](#Utils)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L185)Utils

Re-exports

<!-- -->

[Utils](https://mikro-orm.io/api/core/class/Utils.md)

### [**](#UuidType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/types/index.ts#L30)UuidType

Re-exports

<!-- -->

[UuidType](https://mikro-orm.io/api/core/class/UuidType.md)

### [**](#ValidationError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/errors.ts#L4)ValidationError

Re-exports

<!-- -->

[ValidationError](https://mikro-orm.io/api/core/class/ValidationError.md)

### [**](#wrap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/wrap.ts#L6)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/wrap.ts#L11)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/wrap.ts#L17)wrap

Re-exports

<!-- -->

[wrap](https://mikro-orm.io/api/core/function/wrap.md)

### [**](#WrappedEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L39)WrappedEntity

Re-exports

<!-- -->

[WrappedEntity](https://mikro-orm.io/api/core/class/WrappedEntity.md)

## Type Aliases<!-- -->[**](<#Type Aliases>)

### [**](#Options)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlMikroORM.ts#L35)Options

**Options: [Options](https://mikro-orm.io/api/core.md#Options)<[PostgreSqlDriver](https://mikro-orm.io/api/postgresql/class/PostgreSqlDriver.md)>

### [**](#WeightedFullTextValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/types/FullTextType.ts#L11)WeightedFullTextValue

**WeightedFullTextValue: { \[ K in FullTextWeight ]?: string | null }
