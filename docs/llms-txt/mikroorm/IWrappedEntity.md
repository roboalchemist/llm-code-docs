# Source: https://mikro-orm.io/api/core/interface/IWrappedEntity.md

# IWrappedEntity<!-- --> \<Entity>

## Index[**](#index)

### Methods

* [**assign](#assign)
* [**getSchema](#getschema)
* [**init](#init)
* [**isInitialized](#isinitialized)
* [**isManaged](#ismanaged)
* [**populate](#populate)
* [**populated](#populated)
* [**serialize](#serialize)
* [**setSerializationContext](#setserializationcontext)
* [**setSchema](#setschema)
* [**toJSON](#tojson)
* [**toObject](#toobject)
* [**toPOJO](#topojo)
* [**toReference](#toreference)

## Methods<!-- -->[**](#methods)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L401)assign

* ****assign**\<Naked, Convert, Data>(data, options): [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof
  <!-- -->
  Data & string>

* #### Parameters

  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Naked, Convert>, Data>

  * ##### optionaloptions: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<Convert>

  #### Returns [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof<!-- --> Data & string>

### [**](#getschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L411)getSchema

* ****getSchema**(): undefined | string

* #### Returns undefined | string

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L382)init

* ****init**\<Hint, Fields, Exclude>(options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Exclude>>

* #### Parameters

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<Entity, Hint, Fields, Exclude>

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Exclude>>

### [**](#isinitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L375)isInitialized

* ****isInitialized**(): boolean

* #### Returns boolean

### [**](#ismanaged)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L376)isManaged

* ****isManaged**(): boolean

* #### Returns boolean

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L378)populate

* ****populate**\<Hint, Fields>(populate, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*, never>>

* #### Parameters

  * ##### populate: false | readonly<!-- --> [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Hint, ALL, 9>\[]

  * ##### optionaloptions: [EntityLoaderOptions](https://mikro-orm.io/api/core/interface/EntityLoaderOptions.md)\<Entity, Fields, never>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*, never>>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L377)populated

* ****populated**(populated): void

* #### Parameters

  * ##### optionalpopulated: boolean

  #### Returns void

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L391)serialize

* ****serialize**\<Naked, Hint, Exclude>(options): [SerializeDTO](https://mikro-orm.io/api/core.md#SerializeDTO)\<Naked, Hint, Exclude, never>

* #### Parameters

  * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<Naked, Hint, Exclude>

  #### Returns [SerializeDTO](https://mikro-orm.io/api/core.md#SerializeDTO)\<Naked, Hint, Exclude, never>

### [**](#setserializationcontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L398)setSerializationContext

* ****setSerializationContext**\<Hint, Fields, Exclude>(options): void

* #### Parameters

  * ##### options: [LoadHint](https://mikro-orm.io/api/core/interface/LoadHint.md)\<Entity, Hint, Fields, Exclude>

  #### Returns void

### [**](#setschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L412)setSchema

* ****setSchema**(schema): void

* #### Parameters

  * ##### optionalschema: string

  #### Returns void

### [**](#tojson)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L389)toJSON

* ****toJSON**(...args): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

* #### Parameters

  * ##### rest...args: any\[]

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

### [**](#toobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L386)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L387)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L388)toObject

* ****toObject**(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>
* ****toObject**(ignoreFields): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>
* ****toObject**\<Ignored>(ignoreFields): Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>, Ignored>

* #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

### [**](#topojo)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L390)toPOJO

* ****toPOJO**(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

* #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

### [**](#toreference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L385)toReference

* ****toReference**(): [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>, \*, never>>

* #### Returns [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>, \*, never>>
