# Source: https://mikro-orm.io/api/core/interface/GenerateOptions.md

# GenerateOptions<!-- -->

## Index[**](#index)

### Properties

* [**bidirectionalRelations](#bidirectionalRelations)
* [**coreImportsPrefix](#coreImportsPrefix)
* [**customBaseEntityName](#customBaseEntityName)
* [**decorators](#decorators)
* [**entityDefinition](#entityDefinition)
* [**enumMode](#enumMode)
* [**esmImport](#esmImport)
* [**extraImports](#extraImports)
* [**fileName](#fileName)
* [**forceUndefined](#forceUndefined)
* [**identifiedReferences](#identifiedReferences)
* [**inferEntityType](#inferEntityType)
* [**onImport](#onImport)
* [**onInitialMetadata](#onInitialMetadata)
* [**onlyPurePivotTables](#onlyPurePivotTables)
* [**onProcessedMetadata](#onProcessedMetadata)
* [**outputPurePivotTables](#outputPurePivotTables)
* [**path](#path)
* [**readOnlyPivotTables](#readOnlyPivotTables)
* [**save](#save)
* [**scalarPropertiesForRelations](#scalarPropertiesForRelations)
* [**scalarTypeInDecorator](#scalarTypeInDecorator)
* [**schema](#schema)
* [**skipColumns](#skipColumns)
* [**skipTables](#skipTables)
* [**takeTables](#takeTables)
* [**undefinedDefaults](#undefinedDefaults)
* [**useCoreBaseEntity](#useCoreBaseEntity)

## Properties<!-- -->[**](#properties)

### [**](#bidirectionalRelations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1396)optionalbidirectionalRelations

**bidirectionalRelations?

<!-- -->

: boolean

### [**](#coreImportsPrefix)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1413)optionalcoreImportsPrefix

**coreImportsPrefix?

<!-- -->

: string

### [**](#customBaseEntityName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1411)optionalcustomBaseEntityName

**customBaseEntityName?

<!-- -->

: string

### [**](#decorators)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1399)optionaldecorators

**decorators?

<!-- -->

: es | legacy

### [**](#entityDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1398)optionalentityDefinition

**entityDefinition?

<!-- -->

: decorators | defineEntity | entitySchema

### [**](#enumMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1401)optionalenumMode

**enumMode?

<!-- -->

: ts-enum | union-type | dictionary

### [**](#esmImport)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1402)optionalesmImport

**esmImport?

<!-- -->

: boolean

### [**](#extraImports)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1407)optionalextraImports

**extraImports?

<!-- -->

: (basePath, originFileName) => undefined | string\[]

#### Type declaration

* * **(basePath, originFileName): undefined | string\[]

  * #### Parameters

    * ##### basePath: string

    * ##### originFileName: string

    #### Returns undefined | string\[]

### [**](#fileName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1405)optionalfileName

**fileName?

<!-- -->

: (className) => string

#### Type declaration

* * **(className): string

  * #### Parameters

    * ##### className: string

    #### Returns string

### [**](#forceUndefined)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1394)optionalforceUndefined

**forceUndefined?

<!-- -->

: boolean

### [**](#identifiedReferences)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1397)optionalidentifiedReferences

**identifiedReferences?

<!-- -->

: boolean

### [**](#inferEntityType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1400)optionalinferEntityType

**inferEntityType?

<!-- -->

: boolean

### [**](#onImport)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1406)optionalonImport

**onImport?

<!-- -->

: [ImportsResolver](https://mikro-orm.io/api/core.md#ImportsResolver)

### [**](#onInitialMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1414)optionalonInitialMetadata

**onInitialMetadata?

<!-- -->

: [MetadataProcessor](https://mikro-orm.io/api/core.md#MetadataProcessor)

### [**](#onlyPurePivotTables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1408)optionalonlyPurePivotTables

**onlyPurePivotTables?

<!-- -->

: boolean

### [**](#onProcessedMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1415)optionalonProcessedMetadata

**onProcessedMetadata?

<!-- -->

: [MetadataProcessor](https://mikro-orm.io/api/core.md#MetadataProcessor)

### [**](#outputPurePivotTables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1409)optionaloutputPurePivotTables

**outputPurePivotTables?

<!-- -->

: boolean

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1388)optionalpath

**path?

<!-- -->

: string

### [**](#readOnlyPivotTables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1410)optionalreadOnlyPivotTables

**readOnlyPivotTables?

<!-- -->

: boolean

### [**](#save)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1389)optionalsave

**save?

<!-- -->

: boolean

### [**](#scalarPropertiesForRelations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1404)optionalscalarPropertiesForRelations

**scalarPropertiesForRelations?

<!-- -->

: always | never | smart

### [**](#scalarTypeInDecorator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1403)optionalscalarTypeInDecorator

**scalarTypeInDecorator?

<!-- -->

: boolean

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1390)optionalschema

**schema?

<!-- -->

: string

### [**](#skipColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1393)optionalskipColumns

**skipColumns?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>

### [**](#skipTables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1392)optionalskipTables

**skipTables?

<!-- -->

: (string | RegExp)\[]

### [**](#takeTables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1391)optionaltakeTables

**takeTables?

<!-- -->

: (string | RegExp)\[]

### [**](#undefinedDefaults)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1395)optionalundefinedDefaults

**undefinedDefaults?

<!-- -->

: boolean

### [**](#useCoreBaseEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1412)optionaluseCoreBaseEntity

**useCoreBaseEntity?

<!-- -->

: boolean
