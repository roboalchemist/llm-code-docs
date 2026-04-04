# Source: https://mikro-orm.io/api/core/interface/IConfiguration.md

# IConfiguration<!-- -->

## Index[**](#index)

### Methods

* [**get](#get)
* [**getLogger](#getlogger)
* [**getMetadataCacheAdapter](#getmetadatacacheadapter)
* [**getPlatform](#getplatform)

## Methods<!-- -->[**](#methods)

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L10)get

* ****get**(key, defaultValue): any

* #### Parameters

  * ##### key: string

  * ##### optionaldefaultValue: any

  #### Returns any

### [**](#getlogger)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L11)getLogger

* ****getLogger**(): [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

* #### Returns [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

### [**](#getmetadatacacheadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L12)getMetadataCacheAdapter

* ****getMetadataCacheAdapter**(): [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

* #### Returns [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

### [**](#getplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L13)getPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

* #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)
