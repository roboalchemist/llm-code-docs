# Source: https://mikro-orm.io/api/core/interface/GenerateOptions.md

# GenerateOptions<!-- -->

## Index[**](#Index)

### Properties

* [**bidirectionalRelations](#bidirectionalRelations)
* [**coreImportsPrefix](#coreImportsPrefix)
* [**customBaseEntityName](#customBaseEntityName)
* [**entityDefinition](#entityDefinition)
* [**entitySchema](#entitySchema)
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

## Properties<!-- -->[**](#Properties)

### [**](#bidirectionalRelations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L935)optionalbidirectionalRelations

**bidirectionalRelations?

<!-- -->

: boolean

### [**](#coreImportsPrefix)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L951)optionalcoreImportsPrefix

**coreImportsPrefix?

<!-- -->

: string

### [**](#customBaseEntityName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L949)optionalcustomBaseEntityName

**customBaseEntityName?

<!-- -->

: string

### [**](#entityDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L937)optionalentityDefinition

**entityDefinition?

<!-- -->

: decorators | defineEntity | entitySchema

### [**](#entitySchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L955)optionalentitySchema

**entitySchema?

<!-- -->

: boolean

* **@deprecated**

  use `entityDefinition: 'entitySchema'` instead

### [**](#enumMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L939)optionalenumMode

**enumMode?

<!-- -->

: ts-enum | union-type | dictionary

### [**](#esmImport)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L940)optionalesmImport

**esmImport?

<!-- -->

: boolean

### [**](#extraImports)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L945)optionalextraImports

**extraImports?

<!-- -->

: (basePath, originFileName) => undefined | string\[]

#### Type declaration

* * **(basePath, originFileName): undefined | string\[]

  - #### Parameters

    * ##### basePath: string
    * ##### originFileName: string

    #### Returns undefined | string\[]

### [**](#fileName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L943)optionalfileName

**fileName?

<!-- -->

: (className) => string

#### Type declaration

* * **(className): string

  - #### Parameters

    * ##### className: string

    #### Returns string

### [**](#forceUndefined)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L933)optionalforceUndefined

**forceUndefined?

<!-- -->

: boolean

### [**](#identifiedReferences)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L936)optionalidentifiedReferences

**identifiedReferences?

<!-- -->

: boolean

### [**](#inferEntityType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L938)optionalinferEntityType

**inferEntityType?

<!-- -->

: boolean

### [**](#onImport)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L944)optionalonImport

**onImport?

<!-- -->

: [ImportsResolver](https://mikro-orm.io/api/core.md#ImportsResolver)

### [**](#onInitialMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L952)optionalonInitialMetadata

**onInitialMetadata?

<!-- -->

: [MetadataProcessor](https://mikro-orm.io/api/core.md#MetadataProcessor)

### [**](#onlyPurePivotTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L946)optionalonlyPurePivotTables

**onlyPurePivotTables?

<!-- -->

: boolean

### [**](#onProcessedMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L953)optionalonProcessedMetadata

**onProcessedMetadata?

<!-- -->

: [MetadataProcessor](https://mikro-orm.io/api/core.md#MetadataProcessor)

### [**](#outputPurePivotTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L947)optionaloutputPurePivotTables

**outputPurePivotTables?

<!-- -->

: boolean

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L927)optionalpath

**path?

<!-- -->

: string

### [**](#readOnlyPivotTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L948)optionalreadOnlyPivotTables

**readOnlyPivotTables?

<!-- -->

: boolean

### [**](#save)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L928)optionalsave

**save?

<!-- -->

: boolean

### [**](#scalarPropertiesForRelations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L942)optionalscalarPropertiesForRelations

**scalarPropertiesForRelations?

<!-- -->

: always | never | smart

### [**](#scalarTypeInDecorator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L941)optionalscalarTypeInDecorator

**scalarTypeInDecorator?

<!-- -->

: boolean

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L929)optionalschema

**schema?

<!-- -->

: string

### [**](#skipColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L932)optionalskipColumns

**skipColumns?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>

### [**](#skipTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L931)optionalskipTables

**skipTables?

<!-- -->

: (string | RegExp)\[]

### [**](#takeTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L930)optionaltakeTables

**takeTables?

<!-- -->

: (string | RegExp)\[]

### [**](#undefinedDefaults)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L934)optionalundefinedDefaults

**undefinedDefaults?

<!-- -->

: boolean

### [**](#useCoreBaseEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L950)optionaluseCoreBaseEntity

**useCoreBaseEntity?

<!-- -->

: boolean
