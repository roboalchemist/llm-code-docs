# Source: https://mikro-orm.io/api/core/function/defineEntity.md

# defineEntity<!-- -->

### Callable

* ****defineEntity**\<Properties, PK, Base>(meta): [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<Properties, PK>, Base>
* ****defineEntity**\<Entity, Base>(meta): [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<Entity, Base>

***

* #### Parameters

  * ##### meta: Omit\<Partial<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<Properties, PK>>>, properties | extends | primaryKeys | hooks> & { extends?<!-- -->: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Base>; hooks?<!-- -->: [DefineEntityHooks](https://mikro-orm.io/api/core/interface/DefineEntityHooks.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<Properties, PK>>; name: string; primaryKeys?<!-- -->: PK & [InferPrimaryKey](https://mikro-orm.io/api/core.md#InferPrimaryKey)\<Properties>\[]; properties: Properties | (properties) => Properties }

  #### Returns [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<Properties, PK>, Base>

## Index[**](#Index)

### Properties

* [**properties](#properties)

## Properties<!-- -->[**](#Properties)

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/defineEntity.ts#L757)properties

**properties: { array: \<T>(toJsValue, toDbValue) => UniversalPropertyOptionsBuilder\<T\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; bigint: \<Mode>(mode) => UniversalPropertyOptionsBuilder\<JSTypeByMode\<Mode> & {}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; blob: () => UniversalPropertyOptionsBuilder\<NonNullable\<null | Uint8Array\<ArrayBufferLike> | Buffer\<ArrayBufferLike>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; boolean: () => UniversalPropertyOptionsBuilder\<NonNullable\<undefined | null | boolean>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; character: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; date: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; datetime: (length) => UniversalPropertyOptionsBuilder\<Date, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; decimal: \<Mode>(mode) => UniversalPropertyOptionsBuilder\<NonNullable\<JSTypeByMode\<Mode>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; double: () => UniversalPropertyOptionsBuilder\<NonNullable\<string | number>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; embedded: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target extends T\[] ? T : Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEmbeddedOptions>; enum: \<T>(items) => UniversalPropertyOptionsBuilder\<T extends () => [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) ? ValueOf\<ReturnType\<T\<T>>> : T extends Value\[] ? Value : T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEnumOptions>; enumArray: () => UniversalPropertyOptionsBuilder<(string | number)\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; float: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; formula: \<T>(formula) => UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; integer: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; interval: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; json: \<T>() => UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; manyToMany: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:n }, IncludeKeysForManyToManyOptions>; manyToOne: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:1 }, IncludeKeysForManyToOneOptions>; mediumint: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; oneToMany: \<Target>(target) => OneToManyOptionsBuilderOnlyMappedBy<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>>; oneToOne: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: 1:1 }, IncludeKeysForOneToOneOptions>; smallint: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; string: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; text: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; time: (length) => UniversalPropertyOptionsBuilder\<any, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; tinyint: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; type: \<T>(type) => UniversalPropertyOptionsBuilder\<InferPropertyValueType\<T>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; uint8array: () => UniversalPropertyOptionsBuilder\<Uint8Array\<ArrayBufferLike>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; unknown: () => UniversalPropertyOptionsBuilder<{}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>; uuid: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty> }

#### Type declaration

* ##### array: \<T>(toJsValue, toDbValue) => UniversalPropertyOptionsBuilder\<T\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **\<T>(toJsValue, toDbValue): UniversalPropertyOptionsBuilder\<T\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Parameters

      * ##### toJsValue: (i) => T = <!-- -->...
      *
        ##### toDbValue: (i) => string = <!-- -->...


      #### Returns UniversalPropertyOptionsBuilder\<T\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### bigint: \<Mode>(mode) => UniversalPropertyOptionsBuilder\<JSTypeByMode\<Mode> & {}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **\<Mode>(mode): UniversalPropertyOptionsBuilder\<JSTypeByMode\<Mode> & {}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Parameters

      * ##### optionalmode: Mode

      #### Returns UniversalPropertyOptionsBuilder\<JSTypeByMode\<Mode> & {}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### blob: () => UniversalPropertyOptionsBuilder\<NonNullable\<null | Uint8Array\<ArrayBufferLike> | Buffer\<ArrayBufferLike>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<NonNullable\<null | Uint8Array\<ArrayBufferLike> | Buffer\<ArrayBufferLike>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<NonNullable\<null | Uint8Array\<ArrayBufferLike> | Buffer\<ArrayBufferLike>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### boolean: () => UniversalPropertyOptionsBuilder\<NonNullable\<undefined | null | boolean>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<NonNullable\<undefined | null | boolean>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<NonNullable\<undefined | null | boolean>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### character: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### date: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### datetime: (length) => UniversalPropertyOptionsBuilder\<Date, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(length): UniversalPropertyOptionsBuilder\<Date, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Parameters

      * ##### optionallength: number

      #### Returns UniversalPropertyOptionsBuilder\<Date, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### decimal: \<Mode>(mode) => UniversalPropertyOptionsBuilder\<NonNullable\<JSTypeByMode\<Mode>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **\<Mode>(mode): UniversalPropertyOptionsBuilder\<NonNullable\<JSTypeByMode\<Mode>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Parameters

      * ##### optionalmode: Mode

      #### Returns UniversalPropertyOptionsBuilder\<NonNullable\<JSTypeByMode\<Mode>>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### double: () => UniversalPropertyOptionsBuilder\<NonNullable\<string | number>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<NonNullable\<string | number>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<NonNullable\<string | number>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### embedded: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target extends T\[] ? T : Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEmbeddedOptions>

  * * **\<Target>(target): UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target extends T\[] ? T : Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEmbeddedOptions>

    - #### Parameters

      * ##### target: Target

      #### Returns UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target extends T\[] ? T : Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEmbeddedOptions>

* ##### enum: \<T>(items) => UniversalPropertyOptionsBuilder\<T extends () => [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) ? ValueOf\<ReturnType\<T\<T>>> : T extends Value\[] ? Value : T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEnumOptions>

  * * **\<T>(items): UniversalPropertyOptionsBuilder\<T extends () => [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) ? ValueOf\<ReturnType\<T\<T>>> : T extends Value\[] ? Value : T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEnumOptions>

    - #### Parameters

      * ##### optionalitems: T

      #### Returns UniversalPropertyOptionsBuilder\<T extends () => [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) ? ValueOf\<ReturnType\<T\<T>>> : T extends Value\[] ? Value : T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForEnumOptions>

* ##### enumArray: () => UniversalPropertyOptionsBuilder<(string | number)\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder<(string | number)\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder<(string | number)\[], [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### float: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### formula: \<T>(formula) => UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **\<T>(formula): UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Parameters

      * ##### formula: string | (alias) => string


      #### Returns UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### integer: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### interval: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### json: \<T>() => UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **\<T>(): UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<T, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### manyToMany: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:n }, IncludeKeysForManyToManyOptions>

  * * **\<Target>(target): UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:n }, IncludeKeysForManyToManyOptions>

    - #### Parameters

      * ##### target: Target

      #### Returns UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:n }, IncludeKeysForManyToManyOptions>

* ##### manyToOne: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:1 }, IncludeKeysForManyToOneOptions>

  * * **\<Target>(target): UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:1 }, IncludeKeysForManyToOneOptions>

    - #### Parameters

      * ##### target: Target

      #### Returns UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: m:1 }, IncludeKeysForManyToOneOptions>

* ##### mediumint: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### oneToMany: \<Target>(target) => OneToManyOptionsBuilderOnlyMappedBy<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>>

  * * **\<Target>(target): OneToManyOptionsBuilderOnlyMappedBy<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>>

    - #### Parameters

      * ##### target: Target

      #### Returns OneToManyOptionsBuilderOnlyMappedBy<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>>

* ##### oneToOne: \<Target>(target) => UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: 1:1 }, IncludeKeysForOneToOneOptions>

  * * **\<Target>(target): UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: 1:1 }, IncludeKeysForOneToOneOptions>

    - #### Parameters

      * ##### target: Target

      #### Returns UniversalPropertyOptionsBuilder<[InferEntity](https://mikro-orm.io/api/core.md#InferEntity)\<Target>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md) & { kind: 1:1 }, IncludeKeysForOneToOneOptions>

* ##### smallint: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### string: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### text: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### time: (length) => UniversalPropertyOptionsBuilder\<any, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(length): UniversalPropertyOptionsBuilder\<any, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Parameters

      * ##### optionallength: number

      #### Returns UniversalPropertyOptionsBuilder\<any, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### tinyint: () => UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<number, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### type: \<T>(type) => UniversalPropertyOptionsBuilder\<InferPropertyValueType\<T>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **\<T>(type): UniversalPropertyOptionsBuilder\<InferPropertyValueType\<T>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Parameters

      * ##### type: T

      #### Returns UniversalPropertyOptionsBuilder\<InferPropertyValueType\<T>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### uint8array: () => UniversalPropertyOptionsBuilder\<Uint8Array\<ArrayBufferLike>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<Uint8Array\<ArrayBufferLike>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<Uint8Array\<ArrayBufferLike>, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### unknown: () => UniversalPropertyOptionsBuilder<{}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder<{}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder<{}, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

* ##### uuid: () => UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

  * * **(): UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>

    - #### Returns UniversalPropertyOptionsBuilder\<string, [EmptyOptions](https://mikro-orm.io/api/core/interface/EmptyOptions.md), IncludeKeysForProperty>
