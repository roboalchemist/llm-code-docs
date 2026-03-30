# Source: https://vincit.github.io/objection.js/api/objection/

Title: module objection | Objection.js

URL Source: https://vincit.github.io/objection.js/api/objection/

Markdown Content:
The objection module is what you get when you import objection. It has a bunch of properties that are listed below.

[#](https://vincit.github.io/objection.js/api/objection/#model) Model
---------------------------------------------------------------------

[The model class](https://vincit.github.io/objection.js/api/model/)

[#](https://vincit.github.io/objection.js/api/objection/#initialize) initialize
-------------------------------------------------------------------------------

For some queries objection needs to perform asynchronous operations in preparation, like fetch table metadata from the db. Objection does these preparations on-demand the first time such query is executed. However, some methods like `toKnexQuery` need these preparations to have been made so that the query can be built synchronously. In these cases you can use `initialize` to "warm up" the models and do all needed async preparations needed. You only need to call this function once if you choose to use it.

Calling this function is completely optional. If some method requires this to have been called, they will throw a clear error message asking you to do so. These cases are extremely rare, but this function is here for those cases.

You can also call this function if you want to be in control of when these async preparation operations get executed. It can be helpful for example in tests.

##### [#](https://vincit.github.io/objection.js/api/objection/#examples) Examples

If knex has been installed for the `Model` globally, you can omit the first argument.

[#](https://vincit.github.io/objection.js/api/objection/#transaction) transaction
---------------------------------------------------------------------------------

[The transaction function](https://vincit.github.io/objection.js/guide/transactions.html)

[#](https://vincit.github.io/objection.js/api/objection/#ref) ref
-----------------------------------------------------------------

Factory function that returns a [ReferenceBuilder](https://vincit.github.io/objection.js/api/types/#class-referencebuilder) instance, that makes it easier to refer to tables, columns, json attributes etc. [ReferenceBuilder](https://vincit.github.io/objection.js/api/types/#class-referencebuilder) can also be used to type cast and alias the references.

See [FieldExpression](https://vincit.github.io/objection.js/api/types/#type-fieldexpression) for more information about how to refer to json fields.

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-2) Examples

`withGraphJoined` and `joinRelated` methods also use `:` as a separator which can lead to ambiquous queries when combined with json references. For example:

Can mean two things:

1.   column `name` of the relation `jsonColumn.details`
2.   field `name` of the `details` object inside `jsonColumn` column

When used with `withGraphJoined` and `joinRelated` you can use the `from` method of the `ReferenceBuilder` to specify the table:

[#](https://vincit.github.io/objection.js/api/objection/#raw) raw
-----------------------------------------------------------------

Factory function that returns a [RawBuilder](https://vincit.github.io/objection.js/api/types/#class-rawbuilder) instance. [RawBuilder](https://vincit.github.io/objection.js/api/types/#class-rawbuilder) is a wrapper for knex raw method that doesn't depend on knex. Instances of [RawBuilder](https://vincit.github.io/objection.js/api/types/#class-rawbuilder) are converted to knex raw instances lazily when the query is executed.

Also see [the raw query recipe](https://vincit.github.io/objection.js/recipes/raw-queries.html).

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-3) Examples

When using raw SQL segments in queries, it's a good idea to use placeholders instead of adding user input directly to the SQL to avoid injection errors. Placeholders are sent to the database engine which then takes care of interpolating the SQL safely.

You can use `??` as a placeholder for identifiers (column names, aliases etc.) and `?` for values.

You can use `raw` in insert and update queries too:

You can also use named placeholders. `:someName:` for identifiers (column names, aliases etc.) and `:someName` for values.

You can nest `ref`, `raw`, `val` and query builders (both knex and objection) in `raw` calls

[#](https://vincit.github.io/objection.js/api/objection/#val) val
-----------------------------------------------------------------

Factory function that returns a [ValueBuilder](https://vincit.github.io/objection.js/api/types/#class-valuebuilder) instance. [ValueBuilder](https://vincit.github.io/objection.js/api/types/#class-valuebuilder) helps build values of different types.

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-4) Examples

[#](https://vincit.github.io/objection.js/api/objection/#fn) fn
---------------------------------------------------------------

Factory function that returns a [FunctionBuilder](https://vincit.github.io/objection.js/api/types/#class-functionbuilder) instance. `fn` helps calling SQL functions. The signature is:

For example:

The `fn` function also has shortcuts for most common functions:

All arguments are interpreted as values by default. Use `ref` to refer to columns. you can also pass `raw` instances, other `fn` instances, `QueryBuilders` knex builders, knex raw and anything else just like to any other objection method.

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-5) Examples

Note that it can often be cleaner to use `raw` or `whereRaw`:

[#](https://vincit.github.io/objection.js/api/objection/#mixin) mixin
---------------------------------------------------------------------

The mixin helper for applying multiple [plugins](https://vincit.github.io/objection.js/guide/plugins.html).

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-6) Examples

[#](https://vincit.github.io/objection.js/api/objection/#compose) compose
-------------------------------------------------------------------------

The compose helper for applying multiple [plugins](https://vincit.github.io/objection.js/guide/plugins.html).

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-7) Examples

[#](https://vincit.github.io/objection.js/api/objection/#snakecasemappers) snakeCaseMappers
-------------------------------------------------------------------------------------------

Function for adding snake_case to camelCase conversion to objection models. Better documented [here](https://vincit.github.io/objection.js/recipes/snake-case-to-camel-case-conversion.html). The `snakeCaseMappers` function accepts an options object. The available options are:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| upperCase | boolean | `false` | Set to `true` if your columns are UPPER_SNAKE_CASED. |
| underscoreBeforeDigits | boolean | `false` | When `true`, will place an underscore before digits (`foo1Bar2` becomes `foo_1_bar_2`). When `false`, `foo1Bar2` becomes `foo1_bar2`. |
| underscoreBetweenUppercaseLetters | boolean | `false` | When `true`, will place underscores between consecutive uppercase letters (`fooBAR` becomes `foo_b_a_r`). When `false`, `fooBAR` will become `foo_bar`. |

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-8) Examples

If your columns are UPPER_SNAKE_CASE

[#](https://vincit.github.io/objection.js/api/objection/#knexsnakecasemappers) knexSnakeCaseMappers
---------------------------------------------------------------------------------------------------

Function for adding a snake_case to camelCase conversion to `knex`. Better documented [here](https://vincit.github.io/objection.js/recipes/snake-case-to-camel-case-conversion.html). The `knexSnakeCaseMappers` function accepts an options object. The available options are:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| upperCase | boolean | `false` | Set to `true` if your columns are UPPER_SNAKE_CASED. |
| underscoreBeforeDigits | boolean | `false` | When `true`, will place an underscore before digits (`foo1Bar2` becomes `foo_1_bar_2`). When `false`, `foo1Bar2` becomes `foo1_bar2`. |
| underscoreBetweenUppercaseLetters | boolean | `false` | When `true`, will place underscores between consecutive uppercase letters (`fooBAR` becomes `foo_b_a_r`). When `false`, `fooBAR` will become `foo_bar`. |

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-9) Examples

If your columns are UPPER_SNAKE_CASE

For older nodes:

[#](https://vincit.github.io/objection.js/api/objection/#knexidentifiermapping) knexIdentifierMapping
-----------------------------------------------------------------------------------------------------

Like [knexSnakeCaseMappers](https://vincit.github.io/objection.js/api/objection/#knexsnakecasemappers), but can be used to make an arbitrary static mapping between column names and property names. In the examples, you would have identifiers `MyId`, `MyProp` and `MyAnotherProp` in the database and you would like to map them into `id`, `prop` and `anotherProp` in the code.

##### [#](https://vincit.github.io/objection.js/api/objection/#examples-10) Examples

Note that you can pretty easily define the conversions in some static property of your model. In this example we have added a property `column` to jsonSchema and use that to create the mapping object.

For older nodes:

[#](https://vincit.github.io/objection.js/api/objection/#validationerror) ValidationError
-----------------------------------------------------------------------------------------

The [ValidationError](https://vincit.github.io/objection.js/api/types/#class-validationerror) class.

[#](https://vincit.github.io/objection.js/api/objection/#notfounderror) NotFoundError
-------------------------------------------------------------------------------------

The [NotFoundError](https://vincit.github.io/objection.js/api/types/#class-notfounderror) class.

[#](https://vincit.github.io/objection.js/api/objection/#dberror) DBError
-------------------------------------------------------------------------

The [DBError(opens new window)](https://github.com/Vincit/db-errors#dberror) from [db-errors(opens new window)](https://github.com/Vincit/db-errors) library.

[#](https://vincit.github.io/objection.js/api/objection/#constraintviolationerror) ConstraintViolationError
-----------------------------------------------------------------------------------------------------------

The [ConstraintViolationError(opens new window)](https://github.com/Vincit/db-errors#constraintviolationerror) from [db-errors(opens new window)](https://github.com/Vincit/db-errors) library.

[#](https://vincit.github.io/objection.js/api/objection/#uniqueviolationerror) UniqueViolationError
---------------------------------------------------------------------------------------------------

The [UniqueViolationError(opens new window)](https://github.com/Vincit/db-errors#uniqueviolationerror) from [db-errors(opens new window)](https://github.com/Vincit/db-errors) library.

[#](https://vincit.github.io/objection.js/api/objection/#notnullviolationerror) NotNullViolationError
-----------------------------------------------------------------------------------------------------

The [NotNullViolationError(opens new window)](https://github.com/Vincit/db-errors#notnullviolationerror) from [db-errors(opens new window)](https://github.com/Vincit/db-errors) library.

[#](https://vincit.github.io/objection.js/api/objection/#foreignkeyviolationerror) ForeignKeyViolationError
-----------------------------------------------------------------------------------------------------------

The [ForeignKeyViolationError(opens new window)](https://github.com/Vincit/db-errors#foreignkeyviolationerror) from [db-errors(opens new window)](https://github.com/Vincit/db-errors) library.

[#](https://vincit.github.io/objection.js/api/objection/#checkviolationerror) CheckViolationError
-------------------------------------------------------------------------------------------------

The [CheckViolationError(opens new window)](https://github.com/Vincit/db-errors#checkviolationerror) from [db-errors(opens new window)](https://github.com/Vincit/db-errors) library.

[#](https://vincit.github.io/objection.js/api/objection/#dataerror) DataError
-----------------------------------------------------------------------------

The [DataError(opens new window)](https://github.com/Vincit/db-errors#dataerror) from [db-errors(opens new window)](https://github.com/Vincit/db-errors) library.
