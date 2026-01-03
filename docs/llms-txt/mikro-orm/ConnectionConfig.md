# Source: https://mikro-orm.io/api/core/interface/ConnectionConfig.md

# ConnectionConfig<!-- -->

## Index[**](#Index)

### Properties

* [**database](#database)
* [**host](#host)
* [**password](#password)
* [**port](#port)
* [**schema](#schema)
* [**user](#user)

## Properties<!-- -->[**](#Properties)

### [**](#database)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L187)optionaldatabase

**database?

<!-- -->

: string

### [**](#host)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L183)optionalhost

**host?

<!-- -->

: string

### [**](#password)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L186)optionalpassword

**password?

<!-- -->

: string | () => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string> | [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)<[DynamicPassword](https://mikro-orm.io/api/core/interface/DynamicPassword.md)>

### [**](#port)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L184)optionalport

**port?

<!-- -->

: number

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L188)optionalschema

**schema?

<!-- -->

: string

### [**](#user)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L185)optionaluser

**user?

<!-- -->

: string
