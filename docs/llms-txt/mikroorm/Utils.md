# Source: https://mikro-orm.io/api/core/class/Utils.md

# Utils<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**PK\_SEPARATOR](#PK_SEPARATOR)

### Methods

* [**asArray](#asArray)
* [**callCompiledFunction](#callCompiledFunction)
* [**className](#className)
* [**copy](#copy)
* [**createFunction](#createFunction)
* [**defaultValue](#defaultValue)
* [**detectTypeScriptSupport](#detectTypeScriptSupport)
* [**dropUndefinedProperties](#dropUndefinedProperties)
* [**entries](#entries)
* [**equals](#equals)
* [**extractEnumValues](#extractEnumValues)
* [**extractChildElements](#extractChildElements)
* [**extractPK](#extractPK)
* [**findDuplicates](#findDuplicates)
* [**flatten](#flatten)
* [**getCompositeKeyHash](#getCompositeKeyHash)
* [**getCompositeKeyValue](#getCompositeKeyValue)
* [**getConstructorParams](#getConstructorParams)
* [**getObjectKeysSize](#getObjectKeysSize)
* [**getObjectQueryKeys](#getObjectQueryKeys)
* [**getObjectType](#getObjectType)
* [**getOrderedPrimaryKeys](#getOrderedPrimaryKeys)
* [**getORMVersion](#getORMVersion)
* [**getPrimaryKeyCond](#getPrimaryKeyCond)
* [**getPrimaryKeyCondFromArray](#getPrimaryKeyCondFromArray)
* [**getPrimaryKeyHash](#getPrimaryKeyHash)
* [**getPrimaryKeyValues](#getPrimaryKeyValues)
* [**hash](#hash)
* [**hasNestedKey](#hasNestedKey)
* [**hasObjectKeys](#hasObjectKeys)
* [**isCollection](#isCollection)
* [**isEmpty](#isEmpty)
* [**isEntity](#isEntity)
* [**isIterable](#isIterable)
* [**isObject](#isObject)
* [**isOperator](#isOperator)
* [**isPlainObject](#isPlainObject)
* [**isPrimaryKey](#isPrimaryKey)
* [**isScalarReference](#isScalarReference)
* [**keys](#keys)
* [**mapFlatCompositePrimaryKey](#mapFlatCompositePrimaryKey)
* [**merge](#merge)
* [**mergeConfig](#mergeConfig)
* [**primaryKeyToObject](#primaryKeyToObject)
* [**randomInt](#randomInt)
* [**removeDuplicates](#removeDuplicates)
* [**renameKey](#renameKey)
* [**runIfNotEmpty](#runIfNotEmpty)
* [**runSerial](#runSerial)
* [**setPayloadProperty](#setPayloadProperty)
* [**splitPrimaryKeys](#splitPrimaryKeys)
* [**tryImport](#tryImport)
* [**unique](#unique)
* [**unwrapProperty](#unwrapProperty)
* [**values](#values)
* [**xor](#xor)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new Utils**(): [Utils](https://mikro-orm.io/api/core/class/Utils.md)

* #### Returns [Utils](https://mikro-orm.io/api/core/class/Utils.md)

## Properties<!-- -->[**](#properties)

### [**](#PK_SEPARATOR)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L174)staticreadonlyPK\_SEPARATOR

**PK\_SEPARATOR: \~\~\~ =

<!-- -->

'\~\~\~'

## Methods<!-- -->[**](#methods)

### [**](#asArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L321)staticasArray

* ****asArray**\<T>(data, strict): T\[]

* Normalize the argument to always be an array.

  ***

  #### Parameters

  * ##### optionaldata: T | readonly<!-- --> T\[] | Iterable\<T, any, any>

  * ##### strict: boolean = <!-- -->false

  #### Returns T\[]

### [**](#callCompiledFunction)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L919)staticcallCompiledFunction

* ****callCompiledFunction**\<T, R>(fn, ...args): R

* #### Parameters

  * ##### fn: (...args) => R

  *

    ##### rest...args: T

  #### Returns R

### [**](#className)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L698)staticclassName

* ****className**\<T>(classOrName): string

* Gets string name of given class.

  ***

  #### Parameters

  * ##### classOrName: string | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns string

### [**](#copy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L314)staticcopy

* ****copy**\<T>(entity, respectCustomCloneMethod): T

* Creates deep copy of given object.

  ***

  #### Parameters

  * ##### entity: T

  * ##### respectCustomCloneMethod: boolean = <!-- -->true

  #### Returns T

### [**](#createFunction)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L898)staticcreateFunction

* ****createFunction**(context, code, compiledFunctions, key): any

* #### Parameters

  * ##### context: Map\<string, any>

  * ##### code: string

  * ##### optionalcompiledFunctions: [CompiledFunctions](https://mikro-orm.io/api/core.md#CompiledFunctions)

  * ##### optionalkey: string

  #### Returns any

### [**](#defaultValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L813)staticdefaultValue

* ****defaultValue**\<T>(prop, option, defaultValue): void

* #### Parameters

  * ##### prop: T

  * ##### option: keyof<!-- --> T

  * ##### defaultValue: any

  #### Returns void

### [**](#detectTypeScriptSupport)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L715)staticdetectTypeScriptSupport

* ****detectTypeScriptSupport**(): boolean

* Tries to detect TypeScript support.

  ***

  #### Returns boolean

### [**](#dropUndefinedProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L187)staticdropUndefinedProperties

* ****dropUndefinedProperties**(o, value, visited): void

* Removes `undefined` properties (recursively) so they are not saved as nulls

  ***

  #### Parameters

  * ##### o: any

  * ##### optionalvalue: null

  * ##### visited: Set\<unknown> = <!-- -->

  #### Returns void

### [**](#entries)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1085)staticentries

* ****entries**\<T>(obj): \[keyof
  <!-- -->
  T, T\[keyof
  <!-- -->
  T]]\[]

* #### Parameters

  * ##### obj: T

  #### Returns \[keyof<!-- --> T, T\[keyof<!-- --> T]]\[]

### [**](#equals)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L245)staticequals

* ****equals**(a, b): boolean

* Checks if arguments are deeply (but not strictly) equal.

  ***

  #### Parameters

  * ##### a: any

  * ##### b: any

  #### Returns boolean

### [**](#extractEnumValues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L843)staticextractEnumValues

* ****extractEnumValues**(target): (string | number)\[]

* Extracts all possible values of a TS enum. Works with both string and numeric enums.

  ***

  #### Parameters

  * ##### target: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns (string | number)\[]

### [**](#extractChildElements)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L706)staticextractChildElements

* ****extractChildElements**(items, prefix, allSymbol): string\[]

* #### Parameters

  * ##### items: string\[]

  * ##### prefix: string

  * ##### optionalallSymbol: string

  #### Returns string\[]

### [**](#extractPK)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L428)staticextractPK

* ****extractPK**\<T>(data, meta, strict): null | string | (T extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : T extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : T extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : T)

* Extracts primary key from `data`. Accepts objects or primary keys directly.

  ***

  #### Parameters

  * ##### data: any

  * ##### optionalmeta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### strict: boolean = <!-- -->false

  #### Returns null | string | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)

### [**](#findDuplicates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L817)staticfindDuplicates

* ****findDuplicates**\<T>(items): T\[]

* #### Parameters

  * ##### items: T\[]

  #### Returns T\[]

### [**](#flatten)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L866)staticflatten

* ****flatten**\<T>(arrays, deep): T\[]

* #### Parameters

  * ##### arrays: T\[]\[]

  * ##### optionaldeep: boolean

  #### Returns T\[]

### [**](#getCompositeKeyHash)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L481)staticgetCompositeKeyHash

* ****getCompositeKeyHash**\<T>(data, meta, convertCustomTypes, platform, flat): string

* #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### convertCustomTypes: boolean = <!-- -->false

  * ##### optionalplatform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### flat: boolean = <!-- -->false

  #### Returns string

### [**](#getCompositeKeyValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L458)staticgetCompositeKeyValue

* ****getCompositeKeyValue**\<T>(data, meta, convertCustomTypes, platform): [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

* #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### convertCustomTypes: boolean | convertToDatabaseValue | convertToJSValue = <!-- -->false

  * ##### optionalplatform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

### [**](#getConstructorParams)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L360)staticgetConstructorParams

* ****getConstructorParams**(func): undefined | string\[]

* Returns array of functions argument names. Uses basic regex for source code analysis, might not work with advanced syntax.

  ***

  #### Parameters

  * ##### func: { toString: any }

    * ##### toString

  #### Returns undefined | string\[]

### [**](#getObjectKeysSize)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L216)staticgetObjectKeysSize

* ****getObjectKeysSize**(object): number

* Returns the number of properties on `obj`. This is 20x faster than Object.keys(obj).length.

  * **@see**

    <https://github.com/deepkit/deepkit-framework/blob/master/packages/core/src/core.ts>

  ***

  #### Parameters

  * ##### object: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns number

### [**](#getObjectQueryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1111)staticgetObjectQueryKeys

* ****getObjectQueryKeys**\<T, K>(obj): (K | [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol))\[]

* #### Parameters

  * ##### obj: T

  #### Returns (K | [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol))\[]

### [**](#getObjectType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L740)staticgetObjectType

* ****getObjectType**(value): string

* Gets the type of the argument.

  ***

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#getOrderedPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L624)staticgetOrderedPrimaryKeys

* ****getOrderedPrimaryKeys**\<T>(id, meta, platform, convertCustomTypes, allowScalar): [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>\[]

* #### Parameters

  * ##### id: [Primary](https://mikro-orm.io/api/core.md#Primary)\<T> | Record\<string, [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### optionalplatform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  * ##### convertCustomTypes: boolean = <!-- -->false

  * ##### allowScalar: boolean = <!-- -->false

  #### Returns [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>\[]

### [**](#getORMVersion)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L894)staticgetORMVersion

* ****getORMVersion**(): string

* #### Returns string

### [**](#getPrimaryKeyCond)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L569)staticgetPrimaryKeyCond

* ****getPrimaryKeyCond**\<T>(entity, primaryKeys): null | Record\<string, [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>>

* #### Parameters

  * ##### entity: T

  * ##### primaryKeys: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

  #### Returns null | Record\<string, [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>>

### [**](#getPrimaryKeyCondFromArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L609)staticgetPrimaryKeyCondFromArray

* ****getPrimaryKeyCondFromArray**\<T>(pks, meta): Record\<string, T extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : T extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : T extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : T>

* #### Parameters

  * ##### pks: (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)\[]

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns Record\<string, T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T>

### [**](#getPrimaryKeyHash)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L497)staticgetPrimaryKeyHash

* ****getPrimaryKeyHash**(pks): string

* #### Parameters

  * ##### pks: (string | Date | Buffer\<ArrayBufferLike>)\[]

  #### Returns string

### [**](#getPrimaryKeyValues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L517)staticgetPrimaryKeyValues

* ****getPrimaryKeyValues**\<T>(entity, meta, allowScalar, convertCustomTypes): any

* #### Parameters

  * ##### entity: T

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### allowScalar: boolean = <!-- -->false

  * ##### convertCustomTypes: boolean = <!-- -->false

  #### Returns any

### [**](#hash)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L790)statichash

* ****hash**(data, length): string

* #### Parameters

  * ##### data: string

  * ##### optionallength: number

  #### Returns string

### [**](#hasNestedKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L878)statichasNestedKey

* ****hasNestedKey**(object, key): boolean

* #### Parameters

  * ##### object: unknown

  * ##### key: string

  #### Returns boolean

### [**](#hasObjectKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L232)statichasObjectKeys

* ****hasObjectKeys**(object): boolean

* Returns true if `obj` has at least one property. This is 20x faster than Object.keys(obj).length.

  * **@see**

    <https://github.com/deepkit/deepkit-framework/blob/master/packages/core/src/core.ts>

  ***

  #### Parameters

  * ##### object: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns boolean

### [**](#isCollection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L785)staticisCollection

* ****isCollection**\<T, O>(item): item is [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

* #### Parameters

  * ##### item: any

  #### Returns item is [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

### [**](#isEmpty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L683)staticisEmpty

* ****isEmpty**(data): boolean

* Checks whether the argument is empty (array without items, object without keys or falsy value).

  ***

  #### Parameters

  * ##### data: any

  #### Returns boolean

### [**](#isEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L661)staticisEntity

* ****isEntity**\<T>(data, allowReference): data is T & {}

* Checks whether given object is an entity instance.

  ***

  #### Parameters

  * ##### data: any

  * ##### allowReference: boolean = <!-- -->false

  #### Returns data is T & {}

### [**](#isIterable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L336)staticisIterable

* ****isIterable**\<T>(value): value is Iterable\<T, any, any>

* Checks if the value is iterable, but considers strings and buffers as not iterable.

  ***

  #### Parameters

  * ##### value: unknown

  #### Returns value is Iterable\<T, any, any>

### [**](#isObject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L180)staticisObject

* ****isObject**\<T>(o): o is T

* Checks if the argument is instance of `Object`. Returns false for arrays.

  ***

  #### Parameters

  * ##### o: any

  #### Returns o is T

### [**](#isOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L870)staticisOperator

* ****isOperator**(key, includeGroupOperators): boolean

* #### Parameters

  * ##### key: PropertyKey

  * ##### includeGroupOperators: boolean = <!-- -->true

  #### Returns boolean

### [**](#isPlainObject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L760)staticisPlainObject

* ****isPlainObject**\<T>(value): value is T

* Checks whether the value is POJO (e.g. `{ foo: 'bar' }`, and not instance of `Foo`)

  ***

  #### Parameters

  * ##### value: any

  #### Returns value is T

### [**](#isPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L403)staticisPrimaryKey

* ****isPrimaryKey**\<T>(key, allowComposite): key is [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

* Checks whether the argument looks like primary key (string, number or ObjectId).

  ***

  #### Parameters

  * ##### key: any

  * ##### allowComposite: boolean = <!-- -->false

  #### Returns key is [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

### [**](#isScalarReference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L676)staticisScalarReference

* ****isScalarReference**\<T>(data, allowReference): data is [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<any>

* Checks whether given object is a scalar reference.

  ***

  #### Parameters

  * ##### data: any

  * ##### allowReference: boolean = <!-- -->false

  #### Returns data is [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<any>

### [**](#keys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1077)statickeys

* ****keys**\<T>(obj): keyof
  <!-- -->
  T\[]

* #### Parameters

  * ##### obj: T

  #### Returns keyof<!-- --> T\[]

### [**](#mapFlatCompositePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L585)staticmapFlatCompositePrimaryKey

* ****mapFlatCompositePrimaryKey**(fk, prop, fieldNames, idx): any

* Maps nested FKs from `[1, 2, 3]` to `[1, [2, 3]]`.

  ***

  #### Parameters

  * ##### fk: any\[]

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### fieldNames: string\[] = <!-- -->prop.fieldNames

  * ##### idx: number = <!-- -->0

  #### Returns any

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L263)staticmerge

* ****merge**(target, ...sources): any

* Merges all sources into the target recursively.

  ***

  #### Parameters

  * ##### target: any

  * ##### rest...sources: any\[]

  #### Returns any

### [**](#mergeConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L270)staticmergeConfig

* ****mergeConfig**\<T>(target, ...sources): T

* Merges all sources into the target recursively. Ignores `undefined` values.

  ***

  #### Parameters

  * ##### target: T

  * ##### rest...sources: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\[]

  #### Returns T

### [**](#primaryKeyToObject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1089)staticprimaryKeyToObject

* ****primaryKeyToObject**\<T>(meta, primaryKey, visible): T

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### primaryKey: T | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

  * ##### optionalvisible: keyof<!-- --> T\[]

  #### Returns T

### [**](#randomInt)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L836)staticrandomInt

* ****randomInt**(min, max): number

* #### Parameters

  * ##### min: number

  * ##### max: number

  #### Returns number

### [**](#removeDuplicates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L823)staticremoveDuplicates

* ****removeDuplicates**\<T>(items): T\[]

* #### Parameters

  * ##### items: T\[]

  #### Returns T\[]

### [**](#renameKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L347)staticrenameKey

* ****renameKey**\<T>(payload, from, to): void

* Renames object key, keeps order of properties.

  ***

  #### Parameters

  * ##### payload: T

  * ##### from: string | keyof<!-- --> T

  * ##### to: string

  #### Returns void

### [**](#runIfNotEmpty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L807)staticrunIfNotEmpty

* ****runIfNotEmpty**(clause, data): void

* #### Parameters

  * ##### clause: () => any

  *

    ##### data: any

  #### Returns void

### [**](#runSerial)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L775)staticrunSerial

* ****runSerial**\<T, U>(items, cb): Promise\<T\[]>

* Executes the `cb` promise serially on every element of the `items` array and returns array of resolved values.

  ***

  #### Parameters

  * ##### items: Iterable\<U, any, any>

  * ##### cb: (item) => Promise\<T>

  #### Returns Promise\<T\[]>

### [**](#setPayloadProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1002)staticsetPayloadProperty

* ****setPayloadProperty**\<T>(entity, meta, prop, value, idx): void

* #### Parameters

  * ##### entity: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  * ##### value: unknown

  * ##### idx: number\[]

  #### Returns void

### [**](#splitPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L513)staticsplitPrimaryKeys

* ****splitPrimaryKeys**\<T>(key): [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

* #### Parameters

  * ##### key: string

  #### Returns [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

### [**](#tryImport)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1050)statictryImport

* ****tryImport**\<T>(\_\_namedParameters): Promise\<undefined | T>

* #### Parameters

  * ##### \_\_namedParameters: { module: string; warning?<!-- -->: string }

    * ##### module: string

    * ##### optionalwarning: string

  #### Returns Promise\<undefined | T>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L252)staticunique

* ****unique**\<T>(items): T\[]

* Gets array without duplicates.

  ***

  #### Parameters

  * ##### items: T\[]

  #### Returns T\[]

### [**](#unwrapProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L948)staticunwrapProperty

* ****unwrapProperty**\<T>(entity, meta, prop, payload): \[unknown, number\[]]\[]

* #### Parameters

  * ##### entity: T

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  * ##### payload: boolean = <!-- -->false

  #### Returns \[unknown, number\[]]\[]

### [**](#values)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1081)staticvalues

* ****values**\<T>(obj): T\[keyof
  <!-- -->
  T]\[]

* #### Parameters

  * ##### obj: T

  #### Returns T\[keyof<!-- --> T]\[]

### [**](#xor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Utils.ts#L1073)staticxor

* ****xor**(a, b): boolean

* #### Parameters

  * ##### a: boolean

  * ##### b: boolean

  #### Returns boolean
