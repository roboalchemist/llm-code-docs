# Source: https://mikro-orm.io/api/core/class/BaseEntity.md

# abstractBaseEntity<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**assign](#assign)
* [**getSchema](#getSchema)
* [**init](#init)
* [**isInitialized](#isInitialized)
* [**isTouched](#isTouched)
* [**populate](#populate)
* [**populated](#populated)
* [**serialize](#serialize)
* [**setSchema](#setSchema)
* [**toObject](#toObject)
* [**toPOJO](#toPOJO)
* [**toReference](#toReference)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new BaseEntity**(): [BaseEntity](https://mikro-orm.io/api/core/class/BaseEntity.md)

- #### Returns [BaseEntity](https://mikro-orm.io/api/core/class/BaseEntity.md)

## Methods<!-- -->[**](#Methods)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L54)assign

* ****assign**\<Entity, Naked, Convert, Data>(data, options): [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof
  <!-- -->
  Data & string>

- #### Parameters

  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Naked>, Data>
  * ##### options: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<Convert> = <!-- -->{}

  #### Returns [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof<!-- --> Data & string>

### [**](#getSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L72)getSchema

* ****getSchema**(): undefined | string

- #### Returns undefined | string

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L63)init

* ****init**\<Entity, Hint, Fields, Excludes>(options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

- #### Parameters

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L11)isInitialized

* ****isInitialized**(): boolean

- #### Returns boolean

### [**](#isTouched)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L15)isTouched

* ****isTouched**(): boolean

- #### Returns boolean

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L23)populate

* ****populate**\<Entity, Hint>(populate, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

- #### Parameters

  * ##### populate: false | [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Hint, never, 9>\[]
  * ##### options: [EntityLoaderOptions](https://mikro-orm.io/api/core.md#EntityLoaderOptions)\<Entity> = <!-- -->{}

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L19)populated

* ****populated**(populated): void

- #### Parameters

  * ##### populated: boolean = <!-- -->true

  #### Returns void

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L45)serialize

* ****serialize**\<Entity, Naked, Hint, Exclude>(options): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Naked, Hint>>

- #### Parameters

  * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<Naked, Hint, Exclude>

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Naked, Hint>>

### [**](#setSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L76)setSchema

* ****setSchema**(schema): void

- #### Parameters

  * ##### optionalschema: string

  #### Returns void

### [**](#toObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L34)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L35)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L36)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L37)toObject

* ****toObject**\<Entity>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>
* ****toObject**\<Entity>(ignoreFields): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>
* ****toObject**\<Entity, Ignored>(ignoreFields): Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>, Ignored>

- #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

### [**](#toPOJO)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L41)toPOJO

* ****toPOJO**\<Entity>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

- #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

### [**](#toReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/BaseEntity.ts#L30)toReference

* ****toReference**\<Entity>(): [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>>>

- #### Returns [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>>>
