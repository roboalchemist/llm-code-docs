# Source: https://mikro-orm.io/api/core/interface/ConnectionOptions.md

# ConnectionOptions<!-- -->

### Hierarchy

* *ConnectionOptions*
  * [MikroORMOptions](https://mikro-orm.io/api/core/interface/MikroORMOptions.md)

## Index[**](#Index)

### Properties

* [**charset](#charset)
* [**clientUrl](#clientUrl)
* [**collate](#collate)
* [**dbName](#dbName)
* [**driverOptions](#driverOptions)
* [**host](#host)
* [**multipleStatements](#multipleStatements)
* [**name](#name)
* [**password](#password)
* [**pool](#pool)
* [**port](#port)
* [**schema](#schema)
* [**user](#user)

## Properties<!-- -->[**](#Properties)

### [**](#charset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L522)optionalcharset

**charset?

<!-- -->

: string

### [**](#clientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L517)optionalclientUrl

**clientUrl?

<!-- -->

: string

### [**](#collate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L523)optionalcollate

**collate?

<!-- -->

: string

### [**](#dbName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L514)optionaldbName

**dbName?

<!-- -->

: string

### [**](#driverOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L526)optionaldriverOptions

**driverOptions?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#host)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L518)optionalhost

**host?

<!-- -->

: string

### [**](#multipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L524)optionalmultipleStatements

**multipleStatements?

<!-- -->

: boolean

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L516)optionalname

**name?

<!-- -->

: string

### [**](#password)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L521)optionalpassword

**password?

<!-- -->

: string | () => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string> | [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)<[DynamicPassword](https://mikro-orm.io/api/core/interface/DynamicPassword.md)>

### [**](#pool)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L525)optionalpool

**pool?

<!-- -->

: [PoolConfig](https://mikro-orm.io/api/core/interface/PoolConfig.md)

### [**](#port)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L519)optionalport

**port?

<!-- -->

: number

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L515)optionalschema

**schema?

<!-- -->

: string

### [**](#user)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L520)optionaluser

**user?

<!-- -->

: string
