# Source: https://mikro-orm.io/api/core/interface/LockOptions.md

# LockOptions<!-- -->

### Hierarchy

* [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)
  * *LockOptions*

## Index[**](#Index)

### Properties

* [**ctx](#ctx)
* [**lockMode](#lockMode)
* [**lockTableAliases](#lockTableAliases)
* [**lockVersion](#lockVersion)
* [**loggerContext](#loggerContext)
* [**logging](#logging)
* [**schema](#schema)

## Properties<!-- -->[**](#Properties)

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L289)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from DriverMethodOptions.ctx

### [**](#lockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L282)optionallockMode

**lockMode?

<!-- -->

: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)

### [**](#lockTableAliases)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L284)optionallockTableAliases

**lockTableAliases?

<!-- -->

: string\[]

### [**](#lockVersion)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L283)optionallockVersion

**lockVersion?

<!-- -->

: number | Date

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L291)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from DriverMethodOptions.loggerContext

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L285)optionallogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L290)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from DriverMethodOptions.schema
