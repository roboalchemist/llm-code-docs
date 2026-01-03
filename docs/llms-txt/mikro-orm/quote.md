# Source: https://mikro-orm.io/api/core/function/quote.md

# quote<!-- -->

### Callable

* ****quote**(expParts, ...values): any

***

* Tag function providing quoting of db identifiers (table name, columns names, index names, ...).

  Within the template literal on which the tag function is applied, all placeholders are considered to be database identifiers, and will thus be quoted as so according to the database in use.

  ```
  // On postgres, will produce: create index "index custom_idx_on_name" on "library.author" ("name")
  // On mysql, will produce: create index `index custom_idx_on_name` on `library.author` (`name`)
  @Index({ name: 'custom_idx_on_name', expression: (table, columns) => quote`create index ${'custom_idx_on_name'} on ${table} (${columns.name})` })
  @Entity({ schema: 'library' })
  export class Author { ... }
  ```

  ***

  #### Parameters

  * ##### expParts: readonly<!-- --> string\[]
  * ##### rest...values: (string | { toString: any })\[]

  #### Returns any
