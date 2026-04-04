# Source: https://mikro-orm.io/api/core/interface/ConnectionOptions.md

# ConnectionOptions<!-- -->

Connection configuration options for database connections.

* **@see**

  <https://mikro-orm.io/docs/configuration#connection>

### Hierarchy

* *ConnectionOptions*
  * [Options](https://mikro-orm.io/api/core/interface/Options.md)

## Index[**](#index)

### Properties

* [**attachDatabases](#attachDatabases)
* [**clientUrl](#clientUrl)
* [**collate](#collate)
* [**dbName](#dbName)
* [**driverOptions](#driverOptions)
* [**host](#host)
* [**charset](#charset)
* [**multipleStatements](#multipleStatements)
* [**name](#name)
* [**onCreateConnection](#onCreateConnection)
* [**password](#password)
* [**pool](#pool)
* [**port](#port)
* [**schema](#schema)
* [**user](#user)

## Properties<!-- -->[**](#properties)

### [**](#attachDatabases)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L567)optionalattachDatabases

**attachDatabases?

<!-- -->

: { name: string; path: string }\[]

SQLite/libSQL: databases to attach on connection. Each attached database acts as a schema, accessible via `schema.table` syntax. Entities can reference attached databases via `@Entity({ schema: 'db_name' })`. Note: Not supported for remote libSQL connections.

* **@example**

  ```
  attachDatabases: [
    { name: 'users_db', path: './users.db' },
    { name: 'logs_db', path: '/var/data/logs.db' },
  ]
  ```

### [**](#clientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L522)optionalclientUrl

**clientUrl?

<!-- -->

: string

Full client connection URL. Overrides individual connection options.

### [**](#collate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L539)optionalcollate

**collate?

<!-- -->

: string

Collation for the connection.

### [**](#dbName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L516)optionaldbName

**dbName?

<!-- -->

: string

Name of the database to connect to.

### [**](#driverOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L553)optionaldriverOptions

**driverOptions?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

Additional driver-specific options. The object will be deeply merged with internal driver options.

### [**](#host)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L524)optionalhost

**host?

<!-- -->

: string

Database server hostname.

### [**](#charset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L537)optionalcharset

**charset?

<!-- -->

: string

Character set for the connection.

### [**](#multipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L546)optionalmultipleStatements

**multipleStatements?

<!-- -->

: boolean = false

Enable multiple statements in a single query. Required for importing database dump files. Should be disabled in production for security.

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L520)optionalname

**name?

<!-- -->

: string

Name of the connection (used for logging when replicas are used).

### [**](#onCreateConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L555)optionalonCreateConnection

**onCreateConnection?

<!-- -->

: (connection) => Promise\<void>

Callback to execute when a new connection is created.

***

#### Type declaration

* * **(connection): Promise\<void>

  * #### Parameters

    * ##### connection: unknown

    #### Returns Promise\<void>

### [**](#password)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L535)optionalpassword

**password?

<!-- -->

: string | () => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string>

Database password. Can be a string or a callback function that returns the password. The callback is useful for short-lived tokens from cloud providers.

* **@example**

  ```
  password: async () => someCallToGetTheToken()
  ```

### [**](#pool)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L548)optionalpool

**pool?

<!-- -->

: [PoolConfig](https://mikro-orm.io/api/core/interface/PoolConfig.md)

Connection pool configuration.

### [**](#port)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L526)optionalport

**port?

<!-- -->

: number

Database server port number.

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L518)optionalschema

**schema?

<!-- -->

: string

Default database schema to use.

### [**](#user)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L528)optionaluser

**user?

<!-- -->

: string

Database user name.
