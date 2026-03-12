# Source: https://vincit.github.io/objection.js/guide/hooks.html

Title: Hooks | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/hooks.html

Markdown Content:
Hooks are model methods that allow you too hook into different stages of objection queries. There are three different kinds of hooks

1.   [instance query hooks](https://vincit.github.io/objection.js/guide/hooks.html#instance-query-hooks)
2.   [static query hooks](https://vincit.github.io/objection.js/guide/hooks.html#static-query-hooks)
3.   [model data lifecycle hooks](https://vincit.github.io/objection.js/guide/hooks.html#model-data-lifecycle-hooks)

Each hook type serve a different purpose. We'll go through the different types in the following chapters.

[#](https://vincit.github.io/objection.js/guide/hooks.html#instance-query-hooks) Instance query hooks
-----------------------------------------------------------------------------------------------------

These hooks are executed in different stages of each query type (find, update, insert, delete) for **model instances**. The following hooks exist:

*   [$beforeInsert](https://vincit.github.io/objection.js/api/model/instance-methods.html#beforeinsert)
*   [$afterInsert](https://vincit.github.io/objection.js/api/model/instance-methods.html#afterinsert)
*   [$beforeUpdate](https://vincit.github.io/objection.js/api/model/instance-methods.html#beforeupdate)
*   [$afterUpdate](https://vincit.github.io/objection.js/api/model/instance-methods.html#afterupdate)
*   [$beforeDelete](https://vincit.github.io/objection.js/api/model/instance-methods.html#beforedelete)
*   [$afterDelete](https://vincit.github.io/objection.js/api/model/instance-methods.html#afterdelete)
*   [$afterFind](https://vincit.github.io/objection.js/api/model/instance-methods.html#afterfind)

All of these are instance methods on a model. Therefore you can access the model instance's properties through `this`.

Instance hooks can be async. It allows you, among other things, to execute queries. If you do fire off queries from instance hooks, it's important to always make sure they are fired inside any existing transaction. You can access the transaction through the `context`:

WARNING

Warning!

Running queries and other async operations inside instance hooks can lead to very unpredictable performance because the instance hooks are run for each model instance. For example, consider a query that returns 1000 items. If you have an `$afterFind` hook that executes a query, you'd be executing 1000 queries! The [static query hooks](https://vincit.github.io/objection.js/guide/hooks.html#static-query-hooks) are better suited for that kind of thing.

Because the instance hooks are executed for model instances, they cannot be executed when there are no model instances available. Not all hooks can be implemented and some hooks are only executed in certain situations. There's no `$beforeFind` hook, because we don't have any model instances before the query is executed. There's nothing to call the hook for. `$beforeDelete` and `$afterDelete` are also a bit strange for this reason. They are **only** executed when you run an instance query like this:

Objection could fetch the items from the database and call the hooks for those model instances, but that would lead to unpredicable performance, and that's something objection tries to avoid. If you need to do something like this, you can do it using [the static query hooks](https://vincit.github.io/objection.js/guide/hooks.html#static-query-hooks).

Another thing that may cause confusion with the instance hooks is that the insert and update hooks are always executed for the **input** items:

Each instance hook is passed the [context](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#context) object as the only argument. The context contains whatever data you have installed using either the [context](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#context) or the [mergeContext](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#mergecontext) method. In addition to that, it always contains the `transaction` property that holds the parent query's transaction.

TIP

Note!

If you use 3rd party plugins, it's very usual that they use the hooks to perform their magic. If any plugins are used, it's a good idea to always call the `super` implementation if you implement any of the hooks:

[#](https://vincit.github.io/objection.js/guide/hooks.html#static-query-hooks) Static query hooks
-------------------------------------------------------------------------------------------------

Static hooks are executed in different stages of each query type (find, update, insert, delete). Unlike the [instance query hooks](https://vincit.github.io/objection.js/guide/hooks.html#instance-query-hooks), static hooks are executed once per query. Static hooks are always executed and there are no corner cases like the `$beforeDelete`/`$afterDelete` issue with instance hooks. The following hooks are available:

*   [beforeInsert](https://vincit.github.io/objection.js/api/model/static-methods.html#static-beforeinsert)
*   [afterInsert](https://vincit.github.io/objection.js/api/model/static-methods.html#static-afterinsert)
*   [beforeUpdate](https://vincit.github.io/objection.js/api/model/static-methods.html#static-beforeupdate)
*   [afterUpdate](https://vincit.github.io/objection.js/api/model/static-methods.html#static-afterupdate)
*   [beforeDelete](https://vincit.github.io/objection.js/api/model/static-methods.html#static-beforedelete)
*   [afterDelete](https://vincit.github.io/objection.js/api/model/static-methods.html#static-afterdelete)
*   [beforeFind](https://vincit.github.io/objection.js/api/model/static-methods.html#static-beforefind)
*   [afterFind](https://vincit.github.io/objection.js/api/model/static-methods.html#static-afterfind)

The static hooks are passed one argument of type [StaticHookArguments](https://vincit.github.io/objection.js/api/types/#type-statichookarguments). The most interesting of all properties of that object is the `asFindQuery` parameter that allows you to fetch the items that were/would be affected by the query. For example the following example would fetch the identifiers of all people that would get deleted by the query being executed:

The beauty of `asFindQuery` and the static hooks is that they work in all cases, no matter how complex your query is.

WARNING

Warning!

Even though the static hooks are only executed once per query, and `asFindQuery` only executes one additional query, it can still lead to bad performance. For example, consider this query that deletes all items in a table:

If `Person` has a hook that uses `asFindQuery` to fetch all items that will get deleted, the hook ends up fetching the whole table! Even if you simply select the `id`, the amount of data can be huge.

Be careful with `asFindQuery`!

Another interesting argument is the `cancelQuery` function. It allows you to cancel the query being executed. Used in conjunction with the `asFindQuery`, you can do stuff like this:

The example above turns all delete queries into updates that set the `deleted` property to true. These two lines implement a simple version of a "soft delete" feature.

You can also access the model instances for which the query is started, the input model instances and the relation. The next example should explain what each of them mean:

In `afterDelete`, `afterUpdate`, `afterInsert` and `afterFind` hooks, the `result` property of the input argument contains the result of the query. You can change the result by returning a non-undefined value from the hook:

TIP

Note!

If you use 3rd party plugins, it's very usual that they use the hooks to perform their magic. If any plugins are used, it's a good idea to always call the `super` implementation if you implement any of the hooks:

[#](https://vincit.github.io/objection.js/guide/hooks.html#model-data-lifecycle-hooks) Model data lifecycle hooks
-----------------------------------------------------------------------------------------------------------------

For the purposes of this explanation, let’s define three data layouts:

1.   `database`: The data layout returned by the database.
2.   `internal`: The data layout of a model instance.
3.   `external`: The data layout after calling model.toJSON().

Whenever data is converted from one layout to another a data lifecycle hook is called:

1.   `database` ->[$parseDatabaseJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#parsedatabasejson) ->`internal`
2.   `internal` ->[$formatDatabaseJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#formatdatabasejson) ->`database`
3.   `external` ->[$parseJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#parsejson) ->`internal`
4.   `internal` ->[$formatJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#formatjson) ->`external`

So for example when the results of a query are read from the database the data goes through the [$parseDatabaseJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#parsedatabasejson) method. When data is written to database it goes through the [$formatDatabaseJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#formatdatabasejson) method.

Similarly when you give data for a query (for example [`query().insert(req.body)`](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insert)) or create a model explicitly using [`Model.fromJson(obj)`](https://vincit.github.io/objection.js/api/model/static-methods.html#static-fromjson) the [$parseJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#parsejson) method is invoked. When you call [`model.toJSON()`](https://vincit.github.io/objection.js/api/model/instance-methods.html#tojson) or [`model.$toJson()`](https://vincit.github.io/objection.js/api/model/instance-methods.html#tojson) the [$formatJson](https://vincit.github.io/objection.js/api/model/instance-methods.html#formatjson) is called.

Note: Most libraries like [express(opens new window)](http://expressjs.com/en/index.html) and [koa(opens new window)](https://koajs.com/) automatically call the [toJSON](https://vincit.github.io/objection.js/api/model/instance-methods.html#tojson) method when you pass the model instance to methods like `response.json(model)`. You rarely need to call [toJSON()](https://vincit.github.io/objection.js/api/model/instance-methods.html#tojson) or [$toJson()](https://vincit.github.io/objection.js/api/model/instance-methods.html#tojson) explicitly. This is because `JSON.stringify` calls the `toJSON` method and basically all libraries that create JSON strings use `JSON.stringify` under the hood.

Data lifecycle hooks are always synchronous. They cannot be `async` or return promises.

Fore example, here's a hook that converts date strings to `moment` instances when read from the database, and back to date strings when written to database:
