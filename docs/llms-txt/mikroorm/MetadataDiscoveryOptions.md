# Source: https://mikro-orm.io/api/core/interface/MetadataDiscoveryOptions.md

# MetadataDiscoveryOptions<!-- -->

Configuration options for metadata discovery.

* **@see**

  <https://mikro-orm.io/docs/configuration#entity-discovery>

## Index[**](#index)

### Properties

* [**afterDiscovered](#afterDiscovered)
* [**getMappedType](#getMappedType)
* [**checkDuplicateFieldNames](#checkDuplicateFieldNames)
* [**checkDuplicateTableNames](#checkDuplicateTableNames)
* [**checkNonPersistentCompositeProps](#checkNonPersistentCompositeProps)
* [**inferDefaultValues](#inferDefaultValues)
* [**onMetadata](#onMetadata)
* [**tsConfigPath](#tsConfigPath)
* [**warnWhenNoEntities](#warnWhenNoEntities)

## Properties<!-- -->[**](#properties)

### [**](#afterDiscovered)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L753)optionalafterDiscovered

**afterDiscovered?

<!-- -->

: (storage, platform) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

Hook called after all entities are discovered. Can be used to access and modify all metadata at once.

***

#### Type declaration

* * **(storage, platform): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  * #### Parameters

    * ##### storage: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

    * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L742)optionalgetMappedType

**getMappedType?

<!-- -->

: (type, platform) => undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

Custom callback to override default type mapping. Allows customizing how property types are mapped to database column types.

* **@example**

  ```
  getMappedType(type, platform) {
    if (type === 'string') {
      return Type.getType(TextType);
    }
    return platform.getDefaultMappedType(type);
  }
  ```

***

#### Type declaration

* * **(type, platform): undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  * #### Parameters

    * ##### type: string

    * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    #### Returns undefined | [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#checkDuplicateFieldNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L719)optionalcheckDuplicateFieldNames

**checkDuplicateFieldNames?

<!-- -->

: boolean = true

Check for duplicate field names and throw an error if found.

### [**](#checkDuplicateTableNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L714)optionalcheckDuplicateTableNames

**checkDuplicateTableNames?

<!-- -->

: boolean = true

Check for duplicate table names and throw an error if found.

### [**](#checkNonPersistentCompositeProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L724)optionalcheckNonPersistentCompositeProps

**checkNonPersistentCompositeProps?

<!-- -->

: boolean = true

Check for composite primary keys marked as `persist: false` and throw an error if found.

### [**](#inferDefaultValues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L730)optionalinferDefaultValues

**inferDefaultValues?

<!-- -->

: boolean = true

Infer default values from property initializers when possible (if the constructor can be invoked without parameters).

### [**](#onMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L748)optionalonMetadata

**onMetadata?

<!-- -->

: (meta, platform) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

Hook called for each entity metadata during discovery. Can be used to modify metadata dynamically before defaults are filled in. The hook can be async when using `MikroORM.init()`.

***

#### Type declaration

* * **(meta, platform): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  * #### Parameters

    * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

    * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

    #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

### [**](#tsConfigPath)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L755)optionaltsConfigPath

**tsConfigPath?

<!-- -->

: string

Path to the TypeScript configuration file for ts-morph metadata provider.

### [**](#warnWhenNoEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L709)optionalwarnWhenNoEntities

**warnWhenNoEntities?

<!-- -->

: boolean = true

Throw an error when no entities are discovered.
