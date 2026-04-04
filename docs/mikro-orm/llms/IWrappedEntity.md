# Source: https://mikro-orm.io/api/core/interface/IWrappedEntity.md

# IWrappedEntity<!-- --> \<Entity>

## Index[**](#Index)

### Methods

* [**assign](#assign)
* [**getSchema](#getSchema)
* [**init](#init)
* [**isInitialized](#isInitialized)
* [**isManaged](#isManaged)
* [**isTouched](#isTouched)
* [**populate](#populate)
* [**populated](#populated)
* [**serialize](#serialize)
* [**setSchema](#setSchema)
* [**setSerializationContext](#setSerializationContext)
* [**toJSON](#toJSON)
* [**toObject](#toObject)
* [**toPOJO](#toPOJO)
* [**toReference](#toReference)

## Methods<!-- -->[**](#Methods)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L256)assign

* ****assign**\<Naked, Convert, Data>(data, options): [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof
  <!-- -->
  Data & string>

- #### Parameters

  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Naked, Convert>, Data>
  * ##### optionaloptions: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<Convert>

  #### Returns [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof<!-- --> Data & string>

### [**](#getSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L261)getSchema

* ****getSchema**(): undefined | string

- #### Returns undefined | string

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L235)init

* ****init**\<Hint, Fields, Exclude>(options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Exclude>>

- #### Parameters

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<Entity, Hint, Fields, Exclude>

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Exclude>>

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L230)isInitialized

* ****isInitialized**(): boolean

- #### Returns boolean

### [**](#isManaged)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L232)isManaged

* ****isManaged**(): boolean

- #### Returns boolean

### [**](#isTouched)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L231)isTouched

* ****isTouched**(): boolean

- #### Returns boolean

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L234)populate

* ****populate**\<Hint>(populate, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*, never>>

- #### Parameters

  * ##### populate: false | [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Hint, never, 9>\[]
  * ##### optionaloptions: [EntityLoaderOptions](https://mikro-orm.io/api/core.md#EntityLoaderOptions)\<Entity>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*, never>>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L233)populated

* ****populated**(populated): void

- #### Parameters

  * ##### optionalpopulated: boolean

  #### Returns void

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L246)serialize

* ****serialize**\<Naked, Hint, Exclude>(options): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Naked, Hint, \*, never>, never>

- #### Parameters

  * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<Naked, Hint, Exclude>

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Naked, Hint, \*, never>, never>

### [**](#setSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L262)setSchema

* ****setSchema**(schema): void

- #### Parameters

  * ##### optionalschema: string

  #### Returns void

### [**](#setSerializationContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L251)setSerializationContext

* ****setSerializationContext**\<Hint, Fields, Exclude>(options): void

- #### Parameters

  * ##### options: [LoadHint](https://mikro-orm.io/api/core/interface/LoadHint.md)\<Entity, Hint, Fields, Exclude>

  #### Returns void

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L244)toJSON

* ****toJSON**(...args): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

- #### Parameters

  * ##### rest...args: any\[]

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

### [**](#toObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L241)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L242)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L243)toObject

* ****toObject**(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>
* ****toObject**(ignoreFields): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>
* ****toObject**\<Ignored>(ignoreFields): Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>, Ignored>

- #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

### [**](#toPOJO)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L245)toPOJO

* ****toPOJO**(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

- #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity, never>

### [**](#toReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L240)toReference

* ****toReference**(): [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>, \*, never>>

- #### Returns [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>, \*, never>>
