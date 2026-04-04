# Source: https://mikro-orm.io/api/core/class/BaseEntity.md

# abstractBaseEntity<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**assign](#assign)
* [**getSchema](#getschema)
* [**init](#init)
* [**isInitialized](#isinitialized)
* [**populate](#populate)
* [**populated](#populated)
* [**serialize](#serialize)
* [**setSchema](#setschema)
* [**toObject](#toobject)
* [**toPOJO](#topojo)
* [**toReference](#toreference)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new BaseEntity**(): [BaseEntity](https://mikro-orm.io/api/core/class/BaseEntity.md)

* #### Returns [BaseEntity](https://mikro-orm.io/api/core/class/BaseEntity.md)

## Methods<!-- -->[**](#methods)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L125)assign

* ****assign**\<Entity, Naked, Convert, Data>(data, options): [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof
  <!-- -->
  Data & string>

* #### Parameters

  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Naked>, Data>

  * ##### options: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<Convert> = <!-- -->{}

  #### Returns [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof<!-- --> Data & string>

### [**](#getschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L148)getSchema

* ****getSchema**(): undefined | string

* #### Returns undefined | string

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L139)init

* ****init**\<Entity, Hint, Fields, Excludes>(options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

* #### Parameters

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

### [**](#isinitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L23)isInitialized

* ****isInitialized**(): boolean

* #### Returns boolean

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L31)populate

* ****populate**\<Entity, Hint, Fields>(populate, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

* #### Parameters

  * ##### populate: false | [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Hint, ALL, 9>\[]

  * ##### options: [EntityLoaderOptions](https://mikro-orm.io/api/core/interface/EntityLoaderOptions.md)\<Entity, Fields, never> = <!-- -->{}

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L27)populated

* ****populated**(populated): void

* #### Parameters

  * ##### populated: boolean = <!-- -->true

  #### Returns void

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L116)serialize

* ****serialize**\<Entity, Naked, Hint, Exclude>(options): [SerializeDTO](https://mikro-orm.io/api/core.md#SerializeDTO)\<Naked, Hint, Exclude, never>

* #### Parameters

  * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<Naked, Hint, Exclude>

  #### Returns [SerializeDTO](https://mikro-orm.io/api/core.md#SerializeDTO)\<Naked, Hint, Exclude, never>

### [**](#setschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L152)setSchema

* ****setSchema**(schema): void

* #### Parameters

  * ##### optionalschema: string

  #### Returns void

### [**](#toobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L61)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L81)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L103)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L106)toObject

* ****toObject**\<Entity>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>
* ****toObject**\<Entity>(ignoreFields): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>
* ****toObject**\<Entity, Ignored>(ignoreFields): Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>, Ignored>

* Converts the entity to a plain object representation.

  **Note on typing with `Loaded` entities:** When called on a `Loaded<Entity, 'relation'>` type, the return type will be `EntityDTO<Entity>` (with relations as primary keys), not `EntityDTO<Loaded<Entity, 'relation'>>` (with loaded relations as nested objects). This is a TypeScript limitation - the `this` type resolves to the class, not the `Loaded` wrapper.

  For correct typing that reflects loaded relations, use `wrap()`:

  ```
  const result = await em.find(User, {}, { populate: ['profile'] });
  // Type: EntityDTO<User> (profile is number)
  const obj1 = result[0].toObject();
  // Type: EntityDTO<Loaded<User, 'profile'>> (profile is nested object)
  const obj2 = wrap(result[0]).toObject();
  ```

  Runtime values are correct in both cases - only the static types differ.

  ***

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

### [**](#topojo)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L112)toPOJO

* ****toPOJO**\<Entity>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

* #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

### [**](#toreference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/BaseEntity.ts#L38)toReference

* ****toReference**\<Entity>(): [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>>>

* #### Returns [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>>>
