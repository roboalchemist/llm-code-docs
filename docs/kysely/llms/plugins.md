# Source: https://kysely.dev/docs/plugins.md

# Plugin system

Plugins are classes that implement [KyselyPlugin](https://kysely-org.github.io/kysely-apidoc/interfaces/KyselyPlugin.html). Plugins are then added to the `Kysely` instance as follows:

```
const db = new Kysely<Database>({
  dialect: new PostgresDialect({
    database: 'kysely_test',
    host: 'localhost',
  }),
  plugins: [new CamelCasePlugin()],
})
```

## Built-in plugins[​](#built-in-plugins "Direct link to Built-in plugins")

### Camel case plugin[​](#camel-case-plugin "Direct link to Camel case plugin")

A plugin that converts snake\_case identifiers in the database into camelCase in the JavaScript side. [Learn more](https://kysely-org.github.io/kysely-apidoc/classes/CamelCasePlugin.html).

### Deduplicate joins plugin[​](#deduplicate-joins-plugin "Direct link to Deduplicate joins plugin")

A plugin that removes duplicate joins from queries. You can read more about it in the [examples](https://kysely.dev/docs/recipes/deduplicate-joins.md) section or check the [API docs](https://kysely-org.github.io/kysely-apidoc/classes/DeduplicateJoinsPlugin.html).

### Handle `in ()` and `not in ()` plugin[​](#handle-in--and-not-in--plugin "Direct link to handle-in--and-not-in--plugin")

A plugin that allows handling `in ()` and `not in ()` with a chosen strategy. [Learn more](https://kysely-org.github.io/kysely-apidoc/classes/HandleEmptyInListsPlugin.html).
