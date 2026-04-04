# Source: https://mikro-orm.io/api/core/class/Utils.md

# Utils<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**PK\_SEPARATOR](#PK_SEPARATOR)

### Methods

* [**absolutePath](#absolutePath)
* [**asArray](#asArray)
* [**callCompiledFunction](#callCompiledFunction)
* [**className](#className)
* [**copy](#copy)
* [**createFunction](#createFunction)
* [**defaultValue](#defaultValue)
* [**detectTsNode](#detectTsNode)
* [**diff](#diff)
* [**dropUndefinedProperties](#dropUndefinedProperties)
* [**dynamicImport](#dynamicImport)
* [**dynamicImportProvider](#dynamicImportProvider)
* [**entries](#entries)
* [**equals](#equals)
* [**extractChildElements](#extractChildElements)
* [**extractEnumValues](#extractEnumValues)
* [**extractPK](#extractPK)
* [**fileURLToPath](#fileURLToPath)
* [**findDuplicates](#findDuplicates)
* [**flatten](#flatten)
* [**getCompositeKeyHash](#getCompositeKeyHash)
* [**getCompositeKeyValue](#getCompositeKeyValue)
* [**getGlobalStorage](#getGlobalStorage)
* [**getObjectKeysSize](#getObjectKeysSize)
* [**getObjectType](#getObjectType)
* [**getOrderedPrimaryKeys](#getOrderedPrimaryKeys)
* [**getORMVersion](#getORMVersion)
* [**getParamNames](#getParamNames)
* [**getPrimaryKeyCond](#getPrimaryKeyCond)
* [**getPrimaryKeyCondFromArray](#getPrimaryKeyCondFromArray)
* [**getPrimaryKeyHash](#getPrimaryKeyHash)
* [**getPrimaryKeyValues](#getPrimaryKeyValues)
* [**getRootEntity](#getRootEntity)
* [**hash](#hash)
* [**hasNestedKey](#hasNestedKey)
* [**hasObjectKeys](#hasObjectKeys)
* [**isArrayOperator](#isArrayOperator)
* [**isCollection](#isCollection)
* [**isDefined](#isDefined)
* [**isEmpty](#isEmpty)
* [**isEntity](#isEntity)
* [**isGroupOperator](#isGroupOperator)
* [**isIterable](#isIterable)
* [**isJsonKeyOperator](#isJsonKeyOperator)
* [**isNotObject](#isNotObject)
* [**isNumber](#isNumber)
* [**isObject](#isObject)
* [**isObjectID](#isObjectID)
* [**isOperator](#isOperator)
* [**isPlainObject](#isPlainObject)
* [**isPrimaryKey](#isPrimaryKey)
* [**isRawSql](#isRawSql)
* [**isScalarReference](#isScalarReference)
* [**isString](#isString)
* [**keys](#keys)
* [**lookupPathFromDecorator](#lookupPathFromDecorator)
* [**mapFlatCompositePrimaryKey](#mapFlatCompositePrimaryKey)
* [**merge](#merge)
* [**mergeConfig](#mergeConfig)
* [**normalizePath](#normalizePath)
* [**parseArgs](#parseArgs)
* [**pathExists](#pathExists)
* [**primaryKeyToObject](#primaryKeyToObject)
* [**propertyDecoratorReturnValue](#propertyDecoratorReturnValue)
* [**randomInt](#randomInt)
* [**relativePath](#relativePath)
* [**removeDuplicates](#removeDuplicates)
* [**renameKey](#renameKey)
* [**requireFrom](#requireFrom)
* [**resolveModulePath](#resolveModulePath)
* [**runIfNotEmpty](#runIfNotEmpty)
* [**runSerial](#runSerial)
* [**setDynamicImportProvider](#setDynamicImportProvider)
* [**setPayloadProperty](#setPayloadProperty)
* [**splitPrimaryKeys](#splitPrimaryKeys)
* [**stripRelativePath](#stripRelativePath)
* [**tokenize](#tokenize)
* [**tryRequire](#tryRequire)
* [**unique](#unique)
* [**unwrapProperty](#unwrapProperty)
* [**values](#values)
* [**xor](#xor)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new Utils**(): [Utils](https://mikro-orm.io/api/core/class/Utils.md)

- #### Returns [Utils](https://mikro-orm.io/api/core/class/Utils.md)

## Properties<!-- -->[**](#Properties)

### [**](#PK_SEPARATOR)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L187)staticreadonlyPK\_SEPARATOR

**PK\_SEPARATOR: \~\~\~ =

<!-- -->

'\~\~\~'

## Methods<!-- -->[**](#Methods)

### [**](#absolutePath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L989)staticabsolutePath

* ****absolutePath**(path, baseDir): string

- Computes the absolute path to for the given path relative to the provided base directory. If either `path` or `baseDir` are `file:` URLs, they are converted to local paths.

  ***

  #### Parameters

  * ##### path: string
  * ##### baseDir: string = <!-- -->...

  #### Returns string

### [**](#asArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L430)staticasArray

* ****asArray**\<T>(data, strict): T\[]

- Normalize the argument to always be an array.

  ***

  #### Parameters

  * ##### optionaldata: T | readonly<!-- --> T\[] | Iterable\<T, any, any>
  * ##### strict: boolean = <!-- -->false

  #### Returns T\[]

### [**](#callCompiledFunction)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1203)staticcallCompiledFunction

* ****callCompiledFunction**\<T, R>(fn, ...args): R

- #### Parameters

  * ##### fn: (...args) => R
  *
    ##### rest...args: T

  #### Returns R

### [**](#className)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L805)staticclassName

* ****className**\<T>(classOrName): string

- Gets string name of given class.

  ***

  #### Parameters

  * ##### classOrName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns string

### [**](#copy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L423)staticcopy

* ****copy**\<T>(entity, respectCustomCloneMethod): T

- Creates deep copy of given object.

  ***

  #### Parameters

  * ##### entity: T
  * ##### respectCustomCloneMethod: boolean = <!-- -->true

  #### Returns T

### [**](#createFunction)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1192)staticcreateFunction

* ****createFunction**(context, code): any

- #### Parameters

  * ##### context: Map\<string, any>
  * ##### code: string

  #### Returns any

### [**](#defaultValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1018)staticdefaultValue

* ****defaultValue**\<T>(prop, option, defaultValue): void

- #### Parameters

  * ##### prop: T
  * ##### option: keyof<!-- --> T
  * ##### defaultValue: any

  #### Returns void

### [**](#detectTsNode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L822)staticdetectTsNode

* ****detectTsNode**(): boolean

- Tries to detect `ts-node` runtime.

  ***

  #### Returns boolean

### [**](#diff)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L406)staticdiff

* ****diff**(a, b): Record\<string | number, any>

- Computes difference between two objects, ignoring items missing in `b`.

  ***

  #### Parameters

  * ##### a: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)
  * ##### b: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns Record\<string | number, any>

### [**](#dropUndefinedProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L247)staticdropUndefinedProperties

* ****dropUndefinedProperties**\<T>(o, value, visited): void

- Removes `undefined` properties (recursively) so they are not saved as nulls

  ***

  #### Parameters

  * ##### o: any
  * ##### optionalvalue: null
  * ##### visited: Set\<unknown> = <!-- -->...

  #### Returns void

### [**](#dynamicImport)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1151)staticdynamicImport

* ****dynamicImport**\<T>(id): Promise\<T>

- #### Parameters

  * ##### id: string

  #### Returns Promise\<T>

### [**](#dynamicImportProvider)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L190)staticdynamicImportProvider

* ****dynamicImportProvider**(id): Promise\<any>

- #### Parameters

  * ##### id: string

  #### Returns Promise\<any>

### [**](#entries)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1386)staticentries

* ****entries**\<T>(obj): \[keyof
  <!-- -->
  T, T\[keyof
  <!-- -->
  T]]\[]

- #### Parameters

  * ##### obj: T

  #### Returns \[keyof<!-- --> T, T\[keyof<!-- --> T]]\[]

### [**](#equals)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L321)staticequals

* ****equals**(a, b): boolean

- Checks if arguments are deeply (but not strictly) equal.

  ***

  #### Parameters

  * ##### a: any
  * ##### b: any

  #### Returns boolean

### [**](#extractChildElements)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L813)staticextractChildElements

* ****extractChildElements**(items, prefix, allSymbol): string\[]

- #### Parameters

  * ##### items: string\[]
  * ##### prefix: string
  * ##### optionalallSymbol: string

  #### Returns string\[]

### [**](#extractEnumValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1057)staticextractEnumValues

* ****extractEnumValues**(target): (string | number)\[]

- Extracts all possible values of a TS enum. Works with both string and numeric enums.

  ***

  #### Parameters

  * ##### target: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns (string | number)\[]

### [**](#extractPK)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L552)staticextractPK

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

- Extracts primary key from `data`. Accepts objects or primary keys directly.

  ***

  #### Parameters

  * ##### data: any
  * ##### optionalmeta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### strict: boolean = <!-- -->false

  #### Returns null | string | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)

### [**](#fileURLToPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L932)staticfileURLToPath

* ****fileURLToPath**(url): string

- #### Parameters

  * ##### url: string | URL

  #### Returns string

### [**](#findDuplicates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1022)staticfindDuplicates

* ****findDuplicates**\<T>(items): T\[]

- #### Parameters

  * ##### items: T\[]

  #### Returns T\[]

### [**](#flatten)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1073)staticflatten

* ****flatten**\<T>(arrays): T\[]

- #### Parameters

  * ##### arrays: T\[]\[]

  #### Returns T\[]

### [**](#getCompositeKeyHash)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L605)staticgetCompositeKeyHash

* ****getCompositeKeyHash**\<T>(data, meta, convertCustomTypes, platform, flat): string

- #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### convertCustomTypes: boolean = <!-- -->false
  * ##### optionalplatform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### flat: boolean = <!-- -->false

  #### Returns string

### [**](#getCompositeKeyValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L582)staticgetCompositeKeyValue

* ****getCompositeKeyValue**\<T>(data, meta, convertCustomTypes, platform): [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

- #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### convertCustomTypes: boolean | convertToDatabaseValue | convertToJSValue = <!-- -->false
  * ##### optionalplatform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

### [**](#getGlobalStorage)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1113)staticgetGlobalStorage

* ****getGlobalStorage**(namespace): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

- #### Parameters

  * ##### namespace: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#getObjectKeysSize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L276)staticgetObjectKeysSize

* ****getObjectKeysSize**(object): number

- Returns the number of properties on `obj`. This is 20x faster than Object.keys(obj).length.

  * **@see**

    <https://github.com/deepkit/deepkit-framework/blob/master/packages/core/src/core.ts>

  ***

  #### Parameters

  * ##### object: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns number

### [**](#getObjectType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L884)staticgetObjectType

* ****getObjectType**(value): string

- Gets the type of the argument.

  ***

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#getOrderedPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L730)staticgetOrderedPrimaryKeys

* ****getOrderedPrimaryKeys**\<T>(id, meta, platform, convertCustomTypes, allowScalar): [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>\[]

- #### Parameters

  * ##### id: [Primary](https://mikro-orm.io/api/core.md#Primary)\<T> | Record\<string, [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### optionalplatform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### convertCustomTypes: boolean = <!-- -->false
  * ##### allowScalar: boolean = <!-- -->false

  #### Returns [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>\[]

### [**](#getORMVersion)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1174)staticgetORMVersion

* ****getORMVersion**(): string

- #### Returns string

### [**](#getParamNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L485)staticgetParamNames

* ****getParamNames**(func, methodName): string\[]

- Returns array of functions argument names. Uses `esprima` for source code analysis.

  ***

  #### Parameters

  * ##### func: string | { toString: any } | { type: string; value: string }\[]
  * * ##### toString:
    ##### optionalmethodName: string

  #### Returns string\[]

### [**](#getPrimaryKeyCond)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L683)staticgetPrimaryKeyCond

* ****getPrimaryKeyCond**\<T>(entity, primaryKeys): null | Record\<string, [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>>

- #### Parameters

  * ##### entity: T
  * ##### primaryKeys: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

  #### Returns null | Record\<string, [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>>

### [**](#getPrimaryKeyCondFromArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L718)staticgetPrimaryKeyCondFromArray

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

- #### Parameters

  * ##### pks: (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)\[]
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns Record\<string, T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T>

### [**](#getPrimaryKeyHash)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L615)staticgetPrimaryKeyHash

* ****getPrimaryKeyHash**(pks): string

- #### Parameters

  * ##### pks: (string | Date | Buffer\<ArrayBufferLike>)\[]

  #### Returns string

### [**](#getPrimaryKeyValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L634)staticgetPrimaryKeyValues

* ****getPrimaryKeyValues**\<T>(entity, primaryKeys, allowScalar, convertCustomTypes): any

- #### Parameters

  * ##### entity: T
  * ##### primaryKeys: string\[] | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### allowScalar: boolean = <!-- -->false
  * ##### convertCustomTypes: boolean = <!-- -->false

  #### Returns any

### [**](#getRootEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L387)staticgetRootEntity

* ****getRootEntity**(metadata, meta): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

- #### Parameters

  * ##### metadata: IMetadataStorage
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

### [**](#hash)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1001)statichash

* ****hash**(data, length, algorithm): string

- #### Parameters

  * ##### data: string
  * ##### optionallength: number
  * ##### optionalalgorithm: md5 | sha256

  #### Returns string

### [**](#hasNestedKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1097)statichasNestedKey

* ****hasNestedKey**(object, key): boolean

- #### Parameters

  * ##### object: unknown
  * ##### key: string

  #### Returns boolean

### [**](#hasObjectKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L293)statichasObjectKeys

* ****hasObjectKeys**(object): boolean

- Returns true if `obj` has at least one property. This is 20x faster than Object.keys(obj).length.

  * **@see**

    <https://github.com/deepkit/deepkit-framework/blob/master/packages/core/src/core.ts>

  ***

  #### Parameters

  * ##### object: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns boolean

### [**](#isArrayOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1089)staticisArrayOperator

* ****isArrayOperator**(key): boolean

- #### Parameters

  * ##### key: PropertyKey

  #### Returns boolean

### [**](#isCollection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L928)staticisCollection

* ****isCollection**\<T, O>(item): item is [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

- #### Parameters

  * ##### item: any

  #### Returns item is [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

### [**](#isDefined)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L195)staticisDefined

* ****isDefined**\<T>(data): data is T

- Checks if the argument is not undefined

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is T

### [**](#isEmpty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L790)staticisEmpty

* ****isEmpty**(data): boolean

- Checks whether the argument is empty (array without items, object without keys or falsy value).

  ***

  #### Parameters

  * ##### data: any

  #### Returns boolean

### [**](#isEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L761)staticisEntity

* ****isEntity**\<T>(data, allowReference): data is T & {}

- Checks whether given object is an entity instance.

  ***

  #### Parameters

  * ##### data: any
  * ##### allowReference: boolean = <!-- -->false

  #### Returns data is T & {}

### [**](#isGroupOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1085)staticisGroupOperator

* ****isGroupOperator**(key): boolean

- #### Parameters

  * ##### key: PropertyKey

  #### Returns boolean

### [**](#isIterable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L445)staticisIterable

* ****isIterable**\<T>(value): value is Iterable\<T, any, any>

- Checks if the value is iterable, but considers strings and buffers as not iterable.

  ***

  #### Parameters

  * ##### value: unknown

  #### Returns value is Iterable\<T, any, any>

### [**](#isJsonKeyOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1093)staticisJsonKeyOperator

* ****isJsonKeyOperator**(key): boolean

- #### Parameters

  * ##### key: PropertyKey

  #### Returns boolean

### [**](#isNotObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L240)staticisNotObject

* ****isNotObject**\<T>(o, not): o is T

- Checks if the argument is instance of `Object`, but not one of the blacklisted types. Returns false for arrays.

  ***

  #### Parameters

  * ##### o: any
  * ##### not: any\[]

  #### Returns o is T

### [**](#isNumber)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L314)staticisNumber

* ****isNumber**\<T>(s): s is T

- Checks if the argument is number

  ***

  #### Parameters

  * ##### s: any

  #### Returns s is T

### [**](#isObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L202)staticisObject

* ****isObject**\<T>(o): o is T

- Checks if the argument is instance of `Object`. Returns false for arrays.

  ***

  #### Parameters

  * ##### o: any

  #### Returns o is T

### [**](#isObjectID)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L783)staticisObjectID

* ****isObjectID**(key): boolean

- Checks whether the argument is ObjectId instance

  ***

  #### Parameters

  * ##### key: any

  #### Returns boolean

### [**](#isOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1077)staticisOperator

* ****isOperator**(key, includeGroupOperators): boolean

- #### Parameters

  * ##### key: PropertyKey
  * ##### includeGroupOperators: boolean = <!-- -->true

  #### Returns boolean

### [**](#isPlainObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L904)staticisPlainObject

* ****isPlainObject**\<T>(value): value is T

- Checks whether the value is POJO (e.g. `{ foo: 'bar' }`, and not instance of `Foo`)

  ***

  #### Parameters

  * ##### value: any

  #### Returns value is T

### [**](#isPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L528)staticisPrimaryKey

* ****isPrimaryKey**\<T>(key, allowComposite): key is [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

- Checks whether the argument looks like primary key (string, number or ObjectId).

  ***

  #### Parameters

  * ##### key: any
  * ##### allowComposite: boolean = <!-- -->false

  #### Returns key is [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

### [**](#isRawSql)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1390)staticisRawSql

* ****isRawSql**\<T>(value): value is T

- #### Parameters

  * ##### value: unknown

  #### Returns value is T

### [**](#isScalarReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L776)staticisScalarReference

* ****isScalarReference**\<T>(data, allowReference): data is [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<any>

- Checks whether given object is a scalar reference.

  ***

  #### Parameters

  * ##### data: any
  * ##### allowReference: boolean = <!-- -->false

  #### Returns data is [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<any>

### [**](#isString)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L307)staticisString

* ****isString**(s): s is string

- Checks if the argument is string

  ***

  #### Parameters

  * ##### s: any

  #### Returns s is string

### [**](#keys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1378)statickeys

* ****keys**\<T>(obj): keyof
  <!-- -->
  T\[]

- #### Parameters

  * ##### obj: T

  #### Returns keyof<!-- --> T\[]

### [**](#lookupPathFromDecorator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L842)staticlookupPathFromDecorator

* ****lookupPathFromDecorator**(name, stack): string

- Uses some dark magic to get source path to caller where decorator is used. Analyses stack trace of error created inside the function call.

  ***

  #### Parameters

  * ##### name: string
  * ##### optionalstack: string\[]

  #### Returns string

### [**](#mapFlatCompositePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L699)staticmapFlatCompositePrimaryKey

* ****mapFlatCompositePrimaryKey**(fk, prop, fieldNames, idx): any

- Maps nested FKs from `[1, 2, 3]` to `[1, [2, 3]]`.

  ***

  #### Parameters

  * ##### fk: any\[]
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### fieldNames: string\[] = <!-- -->prop.fieldNames
  * ##### idx: number = <!-- -->0

  #### Returns any

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L339)staticmerge

* ****merge**(target, ...sources): any

- Merges all sources into the target recursively.

  ***

  #### Parameters

  * ##### target: any
  * ##### rest...sources: any\[]

  #### Returns any

### [**](#mergeConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L346)staticmergeConfig

* ****mergeConfig**(target, ...sources): any

- Merges all sources into the target recursively. Ignores `undefined` values.

  ***

  #### Parameters

  * ##### target: any
  * ##### rest...sources: any\[]

  #### Returns any

### [**](#normalizePath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L944)staticnormalizePath

* ****normalizePath**(...parts): string

- Resolves and normalizes a series of path parts relative to each preceding part. If any part is a `file:` URL, it is converted to a local path. If any part is an absolute path, it replaces preceding paths (similar to `path.resolve` in NodeJS). Trailing directory separators are removed, and all directory separators are converted to POSIX-style separators (`/`).

  ***

  #### Parameters

  * ##### rest...parts: string\[]

  #### Returns string

### [**](#parseArgs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1356)staticparseArgs

* ****parseArgs**\<T>(): T

- simple process.argv parser, supports only properties with long names, prefixed with `--`

  ***

  #### Returns T

### [**](#pathExists)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1045)staticpathExists

* ****pathExists**(path, options): Promise\<boolean>

- #### Parameters

  * ##### path: string
  * ##### options: GlobbyOptions = <!-- -->{}

  #### Returns Promise\<boolean>

### [**](#primaryKeyToObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1394)staticprimaryKeyToObject

* ****primaryKeyToObject**\<T>(meta, primaryKey, visible): T

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### primaryKey: T | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>
  * ##### optionalvisible: keyof<!-- --> T\[]

  #### Returns T

### [**](#propertyDecoratorReturnValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1234)staticpropertyDecoratorReturnValue

* ****propertyDecoratorReturnValue**(): any

- - **@see**

    <https://github.com/mikro-orm/mikro-orm/issues/840>

  ***

  #### Returns any

### [**](#randomInt)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1041)staticrandomInt

* ****randomInt**(min, max): number

- #### Parameters

  * ##### min: number
  * ##### max: number

  #### Returns number

### [**](#relativePath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L969)staticrelativePath

* ****relativePath**(path, relativeTo): string

- Determines the relative path between two paths. If either path is a `file:` URL, it is converted to a local path.

  ***

  #### Parameters

  * ##### path: string
  * ##### relativeTo: string

  #### Returns string

### [**](#removeDuplicates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1028)staticremoveDuplicates

* ****removeDuplicates**\<T>(items): T\[]

- #### Parameters

  * ##### items: T\[]

  #### Returns T\[]

### [**](#renameKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L456)staticrenameKey

* ****renameKey**\<T>(payload, from, to): void

- Renames object key, keeps order of properties.

  ***

  #### Parameters

  * ##### payload: T
  * ##### from: string | keyof<!-- --> T
  * ##### to: string

  #### Returns void

### [**](#requireFrom)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1125)staticrequireFrom

* ****requireFrom**\<T>(id, from): T

- Require a module from a specific location

  ***

  #### Parameters

  * ##### id: string

    The module to require

  * ##### optionalfrom: string = <!-- -->...

    Location to start the node resolution

  #### Returns T

### [**](#resolveModulePath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1138)staticresolveModulePath

* ****resolveModulePath**(id, from): string

- Resolve path to a module.

  ***

  #### Parameters

  * ##### id: string

    The module to require

  * ##### optionalfrom: string = <!-- -->...

    Location to start the node resolution

  #### Returns string

### [**](#runIfNotEmpty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1012)staticrunIfNotEmpty

* ****runIfNotEmpty**(clause, data): void

- #### Parameters

  * ##### clause: () => any
  *
    ##### data: any

  #### Returns void

### [**](#runSerial)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L918)staticrunSerial

* ****runSerial**\<T, U>(items, cb): Promise\<T\[]>

- Executes the `cb` promise serially on every element of the `items` array and returns array of resolved values.

  ***

  #### Parameters

  * ##### items: Iterable\<U, any, any>
  * ##### cb: (item) => Promise\<T>


  #### Returns Promise\<T\[]>

### [**](#setDynamicImportProvider)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1170)staticsetDynamicImportProvider

* ****setDynamicImportProvider**(provider): void

- #### Parameters

  * ##### provider: (id) => Promise\<unknown>


  #### Returns void

### [**](#setPayloadProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1289)staticsetPayloadProperty

* ****setPayloadProperty**\<T>(entity, meta, prop, value, idx): void

- #### Parameters

  * ##### entity: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>
  * ##### value: unknown
  * ##### idx: number\[]

  #### Returns void

### [**](#splitPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L629)staticsplitPrimaryKeys

* ****splitPrimaryKeys**\<T>(key): [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

- #### Parameters

  * ##### key: string

  #### Returns [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

### [**](#stripRelativePath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1349)staticstripRelativePath

* ****stripRelativePath**(str): string

- #### Parameters

  * ##### str: string

  #### Returns string

### [**](#tokenize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L469)statictokenize

* ****tokenize**(func): { type: string; value: string }\[]

- Returns array of functions argument names. Uses `esprima` for source code analysis.

  ***

  #### Parameters

  * ##### func: string | { toString: any } | { type: string; value: string }\[]
    * ##### toString:

  #### Returns { type: string; value: string }\[]

### [**](#tryRequire)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1331)statictryRequire

* ****tryRequire**\<T>(\_\_namedParameters): undefined | T

- #### Parameters

  * ##### \_\_namedParameters: { allowError?<!-- -->: string; from?<!-- -->: string; module: string; warning: string }
    * ##### optionalallowError: string
    * ##### optionalfrom: string
    * ##### module: string
    * ##### warning: string

  #### Returns undefined | T

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L328)staticunique

* ****unique**\<T>(items): T\[]

- Gets array without duplicates.

  ***

  #### Parameters

  * ##### items: T\[]

  #### Returns T\[]

### [**](#unwrapProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1240)staticunwrapProperty

* ****unwrapProperty**\<T>(entity, meta, prop, payload): \[unknown, number\[]]\[]

- #### Parameters

  * ##### entity: T
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>
  * ##### payload: boolean = <!-- -->false

  #### Returns \[unknown, number\[]]\[]

### [**](#values)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1382)staticvalues

* ****values**\<T>(obj): T\[keyof
  <!-- -->
  T]\[]

- #### Parameters

  * ##### obj: T

  #### Returns T\[keyof<!-- --> T]\[]

### [**](#xor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Utils.ts#L1374)staticxor

* ****xor**(a, b): boolean

- #### Parameters

  * ##### a: boolean
  * ##### b: boolean

  #### Returns boolean
