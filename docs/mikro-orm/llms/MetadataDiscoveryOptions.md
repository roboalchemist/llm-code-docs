# Source: https://mikro-orm.io/api/core/interface/MetadataDiscoveryOptions.md

# MetadataDiscoveryOptions<!-- -->

## Index[**](#Index)

### Properties

* [**afterDiscovered](#afterDiscovered)
* [**alwaysAnalyseProperties](#alwaysAnalyseProperties)
* [**checkDuplicateEntities](#checkDuplicateEntities)
* [**checkDuplicateFieldNames](#checkDuplicateFieldNames)
* [**checkDuplicateTableNames](#checkDuplicateTableNames)
* [**checkNonPersistentCompositeProps](#checkNonPersistentCompositeProps)
* [**disableDynamicFileAccess](#disableDynamicFileAccess)
* [**getMappedType](#getMappedType)
* [**inferDefaultValues](#inferDefaultValues)
* [**onMetadata](#onMetadata)
* [**requireEntitiesArray](#requireEntitiesArray)
* [**tsConfigPath](#tsConfigPath)
* [**warnWhenNoEntities](#warnWhenNoEntities)

## Properties<!-- -->[**](#Properties)

### [**](#afterDiscovered)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L589)optionalafterDiscovered

**afterDiscovered?

<!-- -->

: (storage, platform) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

#### Type declaration

* * **(storage, platform): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  - #### Parameters

    * ##### storage: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)
    * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

### [**](#alwaysAnalyseProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L584)optionalalwaysAnalyseProperties

**alwaysAnalyseProperties?

<!-- -->

: boolean

### [**](#checkDuplicateEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L582)optionalcheckDuplicateEntities

**checkDuplicateEntities?

<!-- -->

: boolean

### [**](#checkDuplicateFieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L581)optionalcheckDuplicateFieldNames

**checkDuplicateFieldNames?

<!-- -->

: boolean

### [**](#checkDuplicateTableNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L580)optionalcheckDuplicateTableNames

**checkDuplicateTableNames?

<!-- -->

: boolean

### [**](#checkNonPersistentCompositeProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L583)optionalcheckNonPersistentCompositeProps

**checkNonPersistentCompositeProps?

<!-- -->

: boolean

### [**](#disableDynamicFileAccess)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L585)optionaldisableDynamicFileAccess

**disableDynamicFileAccess?

<!-- -->

: boolean

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L587)optionalgetMappedType

**getMappedType?

<!-- -->

: (type, platform) => undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

#### Type declaration

* * **(type, platform): undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  - #### Parameters

    * ##### type: string
    * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    #### Returns undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#inferDefaultValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L586)optionalinferDefaultValues

**inferDefaultValues?

<!-- -->

: boolean

### [**](#onMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L588)optionalonMetadata

**onMetadata?

<!-- -->

: (meta, platform) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

#### Type declaration

* * **(meta, platform): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  - #### Parameters

    * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>
    * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

### [**](#requireEntitiesArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L579)optionalrequireEntitiesArray

**requireEntitiesArray?

<!-- -->

: boolean

### [**](#tsConfigPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L590)optionaltsConfigPath

**tsConfigPath?

<!-- -->

: string

### [**](#warnWhenNoEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L578)optionalwarnWhenNoEntities

**warnWhenNoEntities?

<!-- -->

: boolean
