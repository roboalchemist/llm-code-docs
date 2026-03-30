# Source: https://tortoise.github.io/query.html

Title: Query API - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/query.html

Markdown Content:
This document describes how to use QuerySet to query the database.

Be sure to check [examples](https://github.com/tortoise/tortoise-orm/tree/master/examples).

Below is an example of a simple query that will return all events with a rating greater than 5:

```
await Event.filter(rating__gt=5)
```

There are several method on model itself to start query:

*   `filter(*args, **kwargs)` - create QuerySet with given filters

*   `exclude(*args, **kwargs)` - create QuerySet with given excluding filters

*   `all()` - create QuerySet without filters

*   `first()` - create QuerySet limited to one object and returning the first object

*   `annotate()` - create QuerySet with given annotation

The methods above return a `QuerySet` object, which supports chaining query operations.

The following methods can be used to create an object:

*   `create(**kwargs)` - creates an object with given kwargs

*   `get_or_create(defaults, **kwargs)` - gets an object for given kwargs, if not found create it with additional kwargs from defaults dict

The instance of a model has the following methods:

*   `save()` - update instance, or insert it, if it was never saved before

*   `delete()` - delete instance from db

*   `fetch_related(*args)` - fetches objects related to instance. It can fetch FK relation, Backward-FK relations and M2M relations. It also can fetch variable depth of related objects like this: `await team.fetch_related('events__tournament')` - this will fetch all events for team, and for each of this events their tournament will be prefetched too. After fetching objects they should be available normally like this: `team.events[0].tournament.name`

Another approach to work with related objects on instance is to query them explicitly with `async for`:

```
async for team in event.participants:
    print(team.name)
```

The related objects can be filtered:

```
await team.events.filter(name='First')
```

which will return you a QuerySet object with predefined filter.

You can also create related objects directly through the reverse ForeignKey relation:

```
# Create a related object automatically setting the foreign key
new_event = await team.events.create(name='New Event')
# Equivalent to:
# new_event = await Event.create(name='New Event', team=team)
```

QuerySet[¶](https://tortoise.github.io/query.html#queryset "Link to this heading")
----------------------------------------------------------------------------------

Once you have a QuerySet, you can perform the following operations with it:

_class_ tortoise.queryset.QuerySetSingle(_*[args](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle.\_\_init\_\_.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySetSingle)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "Link to this definition")
Awaiting on this will resolve a single instance of the Model object, and not a sequence.

_class_ tortoise.queryset.QuerySet(_[model](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet.\_\_init\_\_.model (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "Link to this definition") __getitem__ (_[key](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.\_\_getitem\_\_ "tortoise.queryset.QuerySet.\_\_getitem\_\_.key (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.__getitem__)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.__getitem__ "Link to this definition")
Query offset and limit for Queryset.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.__getitem__-raises "Permalink to this headline")
*   [**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – QuerySet indices must be slices.

*   [**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – Slice steps should be 1 or None.

*   [**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – Slice start should be non-negative number or None.

*   [**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – Slice stop should be non-negative number greater that slice start,

or None.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.__getitem__-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

all()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.all)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.all "Link to this definition")
Return the whole QuerySet. Essentially a no-op except as the only operation.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.all-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

annotate(_**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.annotate "tortoise.queryset.QuerySet.annotate.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.annotate)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.annotate "Link to this definition")
Annotate result with aggregation or function result.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.annotate-raises "Permalink to this headline")
**TypeError** – Value of kwarg is expected to be a `Function` instance.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.annotate-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

bulk_create(_[objects](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_create.objects "tortoise.queryset.QuerySet.bulk\_create.objects (Python parameter) — List of objects to bulk create")_, _[batch\_size](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_create.batch\_size "tortoise.queryset.QuerySet.bulk\_create.batch\_size (Python parameter) — How many objects are created in a single query")=`None`_, _[ignore\_conflicts](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_create.ignore\_conflicts "tortoise.queryset.QuerySet.bulk\_create.ignore\_conflicts (Python parameter) — Ignore conflicts when inserting")=`False`_, _[update\_fields](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_create.update\_fields "tortoise.queryset.QuerySet.bulk\_create.update\_fields (Python parameter) — Update fields when conflicts")=`None`_, _[on\_conflict](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_create.on\_conflict "tortoise.queryset.QuerySet.bulk\_create.on\_conflict (Python parameter) — On conflict index name")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.bulk_create)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create "Link to this definition")
This method inserts the provided list of objects into the database in an efficient manner (generally only 1 query, no matter how many objects there are).

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create-parameters "Permalink to this headline")on_conflict=`None`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create.on_conflict "Permalink to this definition")
On conflict index name

update_fields=`None`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create.update_fields "Permalink to this definition")
Update fields when conflicts

ignore_conflicts=`False`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create.ignore_conflicts "Permalink to this definition")
Ignore conflicts when inserting

objects[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create.objects "Permalink to this definition")
List of objects to bulk create

batch_size=`None`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create.batch_size "Permalink to this definition")
How many objects are created in a single query

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create-raises "Permalink to this headline")
**ValueError** – If params do not meet specifications

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_create-return-type "Permalink to this headline")
[`BulkCreateQuery`](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery (Python class) — Returns the SQL query that will be executed. By default, it will return the query with placeholders, but if you set params_inline=True, it will inline the parameters.")[Model]

bulk_update(_[objects](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_update.objects "tortoise.queryset.QuerySet.bulk\_update.objects (Python parameter) — List of objects to bulk create")_, _[fields](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_update.fields "tortoise.queryset.QuerySet.bulk\_update.fields (Python parameter) — The fields to update")_, _[batch\_size](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk\_update.batch\_size "tortoise.queryset.QuerySet.bulk\_update.batch\_size (Python parameter) — How many objects are created in a single query")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.bulk_update)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_update "Link to this definition")
Update the given fields in each of the given objects in the database.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_update-parameters "Permalink to this headline")objects[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_update.objects "Permalink to this definition")
List of objects to bulk create

fields[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_update.fields "Permalink to this definition")
The fields to update

batch_size=`None`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_update.batch_size "Permalink to this definition")
How many objects are created in a single query

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_update-raises "Permalink to this headline")
**ValueError** – If objects have no primary key set

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.bulk_update-return-type "Permalink to this headline")
[`BulkUpdateQuery`](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery (Python class) — Returns the SQL query that will be executed. By default, it will return the query with placeholders, but if you set params_inline=True, it will inline the parameters.")[Model]

count()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.count)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.count "Link to this definition")
Return count of objects in queryset instead of objects.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.count-return-type "Permalink to this headline")
[`CountQuery`](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery (Python class)")

delete()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.delete)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.delete "Link to this definition")
Delete all objects in QuerySet.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.delete-return-type "Permalink to this headline")
[`DeleteQuery`](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery (Python class)")

distinct()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.distinct)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.distinct "Link to this definition")
Make QuerySet distinct.

Only makes sense in combination with a `.values()` or `.values_list()` as it precedes all the fetched fields with a distinct.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.distinct-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

earliest(_*[orderings](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.earliest "tortoise.queryset.QuerySet.earliest.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.earliest)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.earliest "Link to this definition")
Returns the earliest object by ordering ascending on the specified field.

Params orderings:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.earliest-params-orderings "Permalink to this headline")
Fields to order by.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.earliest-raises "Permalink to this headline")
[**FieldError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.FieldError "tortoise.exceptions.FieldError (Python exception) — Bases: BaseORMException") – If unknown or no fields has been provided.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.earliest-return-type "Permalink to this headline")
[`QuerySetSingle`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[`Optional`[Model]]

exclude(_*[args](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.exclude "tortoise.queryset.QuerySet.exclude.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.exclude "tortoise.queryset.QuerySet.exclude.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.exclude)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.exclude "Link to this definition")
Same as .filter(), but with appends all args with NOT

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.exclude-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

exists()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.exists)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.exists "Link to this definition")
Return True/False whether queryset exists.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.exists-return-type "Permalink to this headline")
[`ExistsQuery`](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery (Python class)")

_async_ explain()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.explain)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.explain "Link to this definition")
Fetch and return information about the query execution plan.

This is done by executing an `EXPLAIN` query whose exact prefix depends on the database backend, as documented below.

*   PostgreSQL: `EXPLAIN (FORMAT JSON, VERBOSE) ...`

*   SQLite: `EXPLAIN QUERY PLAN ...`

*   MySQL: `EXPLAIN FORMAT=JSON ...`

Note

This is only meant to be used in an interactive environment for debugging and query optimization. **The output format may (and will) vary greatly depending on the database backend.**

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.explain-return-type "Permalink to this headline")
`Any`

filter(_*[args](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.filter "tortoise.queryset.QuerySet.filter.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.filter "tortoise.queryset.QuerySet.filter.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.filter)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.filter "Link to this definition")
Filters QuerySet by given kwargs. You can filter by related objects like this:

```
Team.filter(events__tournament__name='Test')
```

You can also pass Q objects to filters as args.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.filter-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

first()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.first)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.first "Link to this definition")
Limit queryset to one object and return one object instead of list.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.first-return-type "Permalink to this headline")
[`QuerySetSingle`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[`Optional`[Model]]

force_index(_*[index\_names](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.force\_index "tortoise.queryset.QuerySet.force\_index.index\_names (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.force_index)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.force_index "Link to this definition")
The FORCE INDEX hint acts like USE INDEX (index_list), with the addition that a table scan is assumed to be very expensive.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.force_index-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

get(_*[args](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get "tortoise.queryset.QuerySet.get.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get "tortoise.queryset.QuerySet.get.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.get)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get "Link to this definition")
Fetch exactly one object matching the parameters.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get-return-type "Permalink to this headline")
[`QuerySetSingle`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[Model]

get_or_none(_*[args](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get\_or\_none "tortoise.queryset.QuerySet.get\_or\_none.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get\_or\_none "tortoise.queryset.QuerySet.get\_or\_none.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.get_or_none)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get_or_none "Link to this definition")
Fetch exactly one object matching the parameters.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.get_or_none-return-type "Permalink to this headline")
[`QuerySetSingle`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[`Optional`[Model]]

group_by(_*[fields](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.group\_by "tortoise.queryset.QuerySet.group\_by.fields (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.group_by)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.group_by "Link to this definition")
Make QuerySet returns list of dict or tuple with group by.

Must call before .values() or .values_list()

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.group_by-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

_async_ in_bulk(_[id\_list](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.in\_bulk.id\_list "tortoise.queryset.QuerySet.in\_bulk.id\_list (Python parameter) — A list of field values")_, _[field\_name](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.in\_bulk.field\_name "tortoise.queryset.QuerySet.in\_bulk.field\_name (Python parameter) — Must be a unique field")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.in_bulk)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.in_bulk "Link to this definition")
Return a dictionary mapping each of the given IDs to the object with that ID. If id_list isn’t provided, evaluate the entire QuerySet.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.in_bulk-parameters "Permalink to this headline")id_list[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.in_bulk.id_list "Permalink to this definition")
A list of field values

field_name[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.in_bulk.field_name "Permalink to this definition")
Must be a unique field

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.in_bulk-return-type "Permalink to this headline")
`dict`

last()[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.last)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.last "Link to this definition")
Limit queryset to one object and return the last object instead of list.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.last-return-type "Permalink to this headline")
[`QuerySetSingle`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[`Optional`[Model]]

latest(_*[orderings](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.latest "tortoise.queryset.QuerySet.latest.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.latest)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.latest "Link to this definition")
Returns the most recent object by ordering descending on the providers fields.

Params orderings:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.latest-params-orderings "Permalink to this headline")
Fields to order by.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.latest-raises "Permalink to this headline")
[**FieldError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.FieldError "tortoise.exceptions.FieldError (Python exception) — Bases: BaseORMException") – If unknown or no fields has been provided.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.latest-return-type "Permalink to this headline")
[`QuerySetSingle`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[`Optional`[Model]]

limit(_[limit](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.limit "tortoise.queryset.QuerySet.limit.limit (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.limit)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.limit "Link to this definition")
Limits QuerySet to given length.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.limit-raises "Permalink to this headline")
[**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – Limit should be non-negative number.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.limit-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

offset(_[offset](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.offset "tortoise.queryset.QuerySet.offset.offset (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.offset)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.offset "Link to this definition")
Query offset for QuerySet.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.offset-raises "Permalink to this headline")
[**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – Offset should be non-negative number.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.offset-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

only(_*[fields\_for\_select](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.only "tortoise.queryset.QuerySet.only.fields\_for\_select (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.only)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.only "Link to this definition")
Fetch ONLY the specified fields to create a partial model.

Persisting changes on the model is allowed only when:

*   All the fields you want to update is specified in `<model>.save(update_fields=[...])`

*   You included the Model primary key in the .only(…)`

To protect against common mistakes we ensure that errors get raised:

*   If you access a field that is not specified, you will get an `AttributeError`.

*   If you do a `<model>.save()` a `IncompleteInstanceError` will be raised as the model is, as requested, incomplete.

*   If you do a `<model>.save(update_fields=[...])` and you didn’t include the primary key in the `.only(...)`, then `IncompleteInstanceError` will be raised indicating that updates can’t be done without the primary key being known.

*   If you do a `<model>.save(update_fields=[...])` and one of the fields in `update_fields` was not in the `.only(...)`, then `IncompleteInstanceError` as that field is not available to be updated.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.only-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

order_by(_*[orderings](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.order\_by "tortoise.queryset.QuerySet.order\_by.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.order_by)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.order_by "Link to this definition")
Accept args to filter by in format like this:

```
.order_by('name', '-tournament__name')
```

Supports ordering by related models too. A ‘-’ before the name will result in descending sort order, default is ascending.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.order_by-raises "Permalink to this headline")
[**FieldError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.FieldError "tortoise.exceptions.FieldError (Python exception) — Bases: BaseORMException") – If unknown field has been provided.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.order_by-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

Like `.fetch_related()` on instance, but works on all objects in QuerySet.

[**FieldError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.FieldError "tortoise.exceptions.FieldError (Python exception) — Bases: BaseORMException") – If the field to prefetch on is not a relation, or not found.

[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

raw(_[sql](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.raw "tortoise.queryset.QuerySet.raw.sql (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.raw)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.raw "Link to this definition")
Return the QuerySet from raw SQL

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.raw-return-type "Permalink to this headline")
[`RawSQLQuery`](https://tortoise.github.io/query.html#tortoise.queryset.RawSQLQuery "tortoise.queryset.RawSQLQuery (Python class)")

resolve_filters(_[fields\_for\_select](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve\_filters "tortoise.queryset.QuerySet.resolve\_filters.fields\_for\_select (Python parameter)")=`None`_)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_filters "Link to this definition")
Builds the common filters for a QuerySet.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_filters-return-type "Permalink to this headline")
`None`

resolve_ordering(_[model](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve\_ordering.model "tortoise.queryset.QuerySet.resolve\_ordering.model (Python parameter) — The Model this queryset is based on.")_, _[table](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve\_ordering.table "tortoise.queryset.QuerySet.resolve\_ordering.table (Python parameter) — pypika\_tortoise.Table to keep track of the virtual SQL table (to allow self referential joins)")_, _[orderings](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve\_ordering.orderings "tortoise.queryset.QuerySet.resolve\_ordering.orderings (Python parameter) — What columns/order to order by")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve\_ordering.annotations "tortoise.queryset.QuerySet.resolve\_ordering.annotations (Python parameter) — Annotations that may be ordered on")_, _[fields\_for\_select](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve\_ordering.fields\_for\_select "tortoise.queryset.QuerySet.resolve\_ordering.fields\_for\_select (Python parameter) — Contains fields that are selected in the SELECT clause if .only(), .values() or .values\_list() are used.")=`None`_)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering "Link to this definition")
Applies standard ordering to QuerySet.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering-parameters "Permalink to this headline")model[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering.model "Permalink to this definition")
The Model this queryset is based on.

table[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering.table "Permalink to this definition")
`pypika_tortoise.Table` to keep track of the virtual SQL table (to allow self referential joins)

orderings[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering.orderings "Permalink to this definition")
What columns/order to order by

annotations[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering.annotations "Permalink to this definition")
Annotations that may be ordered on

fields_for_select=`None`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering.fields_for_select "Permalink to this definition")
Contains fields that are selected in the SELECT clause if .only(), .values() or .values_list() are used.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering-raises "Permalink to this headline")
[**FieldError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.FieldError "tortoise.exceptions.FieldError (Python exception) — Bases: BaseORMException") – If a field provided does not exist in model.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.resolve_ordering-return-type "Permalink to this headline")
`None`

select_for_update(_[nowait](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select\_for\_update.nowait "tortoise.queryset.QuerySet.select\_for\_update.nowait (Python parameter) — If True, raise an error if the lock cannot be obtained immediately.")=`False`_, _[skip\_locked](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select\_for\_update.skip\_locked "tortoise.queryset.QuerySet.select\_for\_update.skip\_locked (Python parameter) — If True, skip rows that are already locked by other transactions instead of waiting.")=`False`_, _[of](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select\_for\_update.of "tortoise.queryset.QuerySet.select\_for\_update.of (Python parameter) — Specify the tables to lock when dealing with multiple related tables, e.g.")=`()`_, _[no\_key](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select\_for\_update.no\_key "tortoise.queryset.QuerySet.select\_for\_update.no\_key (Python parameter) — If True, use the lower SELECT ...")=`False`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.select_for_update)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select_for_update "Link to this definition")
Make QuerySet select for update.

Returns a queryset that will lock rows until the end of the transaction, generating a SELECT … FOR UPDATE SQL statement on supported databases.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select_for_update-parameters "Permalink to this headline")nowait=`False`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select_for_update.nowait "Permalink to this definition")
If True, raise an error if the lock cannot be obtained immediately.

skip_locked=`False`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select_for_update.skip_locked "Permalink to this definition")
If True, skip rows that are already locked by other transactions instead of waiting.

of=`()`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select_for_update.of "Permalink to this definition")
Specify the tables to lock when dealing with multiple related tables, e.g. when using select_related. Provide a tuple of table names to indicate which tables’ rows should be locked. By default, all fetched rows are locked.

no_key=`False`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select_for_update.no_key "Permalink to this definition")
If True, use the lower SELECT … FOR NO KEY UPDATE lock strength on PostgreSQL to allow creating or deleting rows in other tables that reference the locked rows via foreign keys. The parameter is ignored on other backends.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.select_for_update-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

Return a new QuerySet instance that will select related objects.

If fields are specified, they must be ForeignKey fields and only those related objects are included in the selection.

[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

sql(_[params\_inline](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.sql.params\_inline "tortoise.queryset.QuerySet.sql.params\_inline (Python parameter) — Whether to inline the parameters")=`False`_)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.sql "Link to this definition")
Returns the SQL query that will be executed. By default, it will return the query with placeholders, but if you set params_inline=True, it will inline the parameters.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.sql-parameters "Permalink to this headline")params_inline=`False`[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.sql.params_inline "Permalink to this definition")
Whether to inline the parameters

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.sql-return-type "Permalink to this headline")
`str`

update(_**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.update "tortoise.queryset.QuerySet.update.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.update)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.update "Link to this definition")
Update all objects in QuerySet with given kwargs.

Will instead of returning a resultset, update the data in the DB itself.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.update-return-type "Permalink to this headline")
[`UpdateQuery`](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery (Python class)")

use_index(_*[index\_names](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.use\_index "tortoise.queryset.QuerySet.use\_index.index\_names (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.use_index)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.use_index "Link to this definition")
The USE INDEX (index_list) hint tells MySQL to use only one of the named indexes to find rows in the table.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.use_index-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

using_db(_[\_db](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.using\_db "tortoise.queryset.QuerySet.using\_db.\_db (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.using_db)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.using_db "Link to this definition")
Executes query in provided db client. Useful for transactions workaround.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.using_db-return-type "Permalink to this headline")
[`QuerySet`](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Model]

values(_*[args](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values "tortoise.queryset.QuerySet.values.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values "tortoise.queryset.QuerySet.values.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.values)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values "Link to this definition")
Make QuerySet return dicts instead of objects.

If called after .get(), .get_or_none() or .first(), returns a dict instead of an object.

You can specify which fields to include by: - Passing field names as positional arguments - Using kwargs in the format field_name=’name_in_dict’ to customize the keys in the resulting dict

If no arguments are passed, it will default to a dict containing all fields.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values-raises "Permalink to this headline")
[**FieldError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.FieldError "tortoise.exceptions.FieldError (Python exception) — Bases: BaseORMException") – If duplicate key has been provided.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values-return-type "Permalink to this headline")
[`ValuesQuery`](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery (Python class)")[`Literal`[False]]

values_list(_*[fields\_](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values\_list "tortoise.queryset.QuerySet.values\_list.fields\_ (Python parameter)")_, _[flat](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values\_list "tortoise.queryset.QuerySet.values\_list.flat (Python parameter)")=`False`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#QuerySet.values_list)[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values_list "Link to this definition")
Make QuerySet returns list of tuples for given args instead of objects.

If call after .get(), .get_or_none() or .first() return tuples for given args instead of object.

If ``flat=True` and only one arg is passed can return flat list or just scalar.

If no arguments are passed it will default to a tuple containing all fields in order of declaration.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet.values_list-return-type "Permalink to this headline")
[`ValuesListQuery`](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery (Python class)")[`Literal`[False]]

_class_ tortoise.queryset.BulkCreateQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery.\_\_init\_\_.db (Python parameter)")_, _[objects](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery.\_\_init\_\_.objects (Python parameter)")_, _[batch\_size](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery.\_\_init\_\_.batch\_size (Python parameter)")=`None`_, _[ignore\_conflicts](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery.\_\_init\_\_.ignore\_conflicts (Python parameter)")=`False`_, _[update\_fields](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery.\_\_init\_\_.update\_fields (Python parameter)")=`None`_, _[on\_conflict](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery.\_\_init\_\_.on\_conflict (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#BulkCreateQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "Link to this definition")sql(_[params\_inline](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery.sql.params\_inline "tortoise.queryset.BulkCreateQuery.sql.params\_inline (Python parameter) — Whether to inline the parameters")=`False`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#BulkCreateQuery.sql)[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery.sql "Link to this definition")
Returns the SQL query that will be executed. By default, it will return the query with placeholders, but if you set params_inline=True, it will inline the parameters.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery.sql-parameters "Permalink to this headline")params_inline=`False`[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery.sql.params_inline "Permalink to this definition")
Whether to inline the parameters

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery.sql-return-type "Permalink to this headline")
`str`

_class_ tortoise.queryset.BulkUpdateQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.db (Python parameter)")_, _[q\_objects](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.q\_objects (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.annotations (Python parameter)")_, _[custom\_filters](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.custom\_filters (Python parameter)")_, _[limit](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.limit (Python parameter)")_, _[orderings](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.orderings (Python parameter)")_, _[objects](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.objects (Python parameter)")_, _[fields](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.fields (Python parameter)")_, _[batch\_size](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery.\_\_init\_\_.batch\_size (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#BulkUpdateQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "Link to this definition")sql(_[params\_inline](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery.sql.params\_inline "tortoise.queryset.BulkUpdateQuery.sql.params\_inline (Python parameter) — Whether to inline the parameters")=`False`_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#BulkUpdateQuery.sql)[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery.sql "Link to this definition")
Returns the SQL query that will be executed. By default, it will return the query with placeholders, but if you set params_inline=True, it will inline the parameters.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery.sql-parameters "Permalink to this headline")params_inline=`False`[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery.sql.params_inline "Permalink to this definition")
Whether to inline the parameters

Return type:[¶](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery.sql-return-type "Permalink to this headline")
`str`

_class_ tortoise.queryset.CountQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.db (Python parameter)")_, _[q\_objects](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.q\_objects (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.annotations (Python parameter)")_, _[custom\_filters](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.custom\_filters (Python parameter)")_, _[limit](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.limit (Python parameter)")_, _[offset](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.offset (Python parameter)")_, _[force\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.force\_indexes (Python parameter)")_, _[use\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "tortoise.queryset.CountQuery.\_\_init\_\_.use\_indexes (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#CountQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.CountQuery "Link to this definition")_class_ tortoise.queryset.DeleteQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery.\_\_init\_\_.db (Python parameter)")_, _[q\_objects](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery.\_\_init\_\_.q\_objects (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery.\_\_init\_\_.annotations (Python parameter)")_, _[custom\_filters](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery.\_\_init\_\_.custom\_filters (Python parameter)")_, _[limit](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery.\_\_init\_\_.limit (Python parameter)")_, _[orderings](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "tortoise.queryset.DeleteQuery.\_\_init\_\_.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#DeleteQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.DeleteQuery "Link to this definition")_class_ tortoise.queryset.ExistsQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery.\_\_init\_\_.db (Python parameter)")_, _[q\_objects](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery.\_\_init\_\_.q\_objects (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery.\_\_init\_\_.annotations (Python parameter)")_, _[custom\_filters](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery.\_\_init\_\_.custom\_filters (Python parameter)")_, _[force\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery.\_\_init\_\_.force\_indexes (Python parameter)")_, _[use\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery.\_\_init\_\_.use\_indexes (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#ExistsQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "Link to this definition")_class_ tortoise.queryset.FieldSelectQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.FieldSelectQuery "tortoise.queryset.FieldSelectQuery.\_\_init\_\_.model (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.FieldSelectQuery "tortoise.queryset.FieldSelectQuery.\_\_init\_\_.annotations (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#FieldSelectQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.FieldSelectQuery "Link to this definition")_class_ tortoise.queryset.RawSQLQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.RawSQLQuery "tortoise.queryset.RawSQLQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.RawSQLQuery "tortoise.queryset.RawSQLQuery.\_\_init\_\_.db (Python parameter)")_, _[sql](https://tortoise.github.io/query.html#tortoise.queryset.RawSQLQuery "tortoise.queryset.RawSQLQuery.\_\_init\_\_.sql (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#RawSQLQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.RawSQLQuery "Link to this definition")_class_ tortoise.queryset.UpdateQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.model (Python parameter)")_, _[update\_kwargs](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.update\_kwargs (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.db (Python parameter)")_, _[q\_objects](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.q\_objects (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.annotations (Python parameter)")_, _[custom\_filters](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.custom\_filters (Python parameter)")_, _[limit](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.limit (Python parameter)")_, _[orderings](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "tortoise.queryset.UpdateQuery.\_\_init\_\_.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#UpdateQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.UpdateQuery "Link to this definition")_class_ tortoise.queryset.ValuesListQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.db (Python parameter)")_, _[q\_objects](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.q\_objects (Python parameter)")_, _[single](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.single (Python parameter)")_, _[raise\_does\_not\_exist](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.raise\_does\_not\_exist (Python parameter)")_, _[fields\_for\_select\_list](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.fields\_for\_select\_list (Python parameter)")_, _[limit](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.limit (Python parameter)")_, _[offset](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.offset (Python parameter)")_, _[distinct](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.distinct (Python parameter)")_, _[orderings](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.orderings (Python parameter)")_, _[flat](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.flat (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.annotations (Python parameter)")_, _[custom\_filters](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.custom\_filters (Python parameter)")_, _[group\_bys](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.group\_bys (Python parameter)")_, _[force\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.force\_indexes (Python parameter)")_, _[use\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "tortoise.queryset.ValuesListQuery.\_\_init\_\_.use\_indexes (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#ValuesListQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.ValuesListQuery "Link to this definition")_class_ tortoise.queryset.ValuesQuery(_[model](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.model (Python parameter)")_, _[db](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.db (Python parameter)")_, _[q\_objects](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.q\_objects (Python parameter)")_, _[single](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.single (Python parameter)")_, _[raise\_does\_not\_exist](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.raise\_does\_not\_exist (Python parameter)")_, _[fields\_for\_select](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.fields\_for\_select (Python parameter)")_, _[limit](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.limit (Python parameter)")_, _[offset](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.offset (Python parameter)")_, _[distinct](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.distinct (Python parameter)")_, _[orderings](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.orderings (Python parameter)")_, _[annotations](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.annotations (Python parameter)")_, _[custom\_filters](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.custom\_filters (Python parameter)")_, _[group\_bys](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.group\_bys (Python parameter)")_, _[force\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.force\_indexes (Python parameter)")_, _[use\_indexes](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "tortoise.queryset.ValuesQuery.\_\_init\_\_.use\_indexes (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/queryset.html#ValuesQuery)[¶](https://tortoise.github.io/query.html#tortoise.queryset.ValuesQuery "Link to this definition")
QuerySet could be constructed, filtered and passed around without actually hitting the database. Only after you `await` QuerySet, it will execute the query.

Here are some common usage scenarios with QuerySet (we are using models defined in [Getting started](https://tortoise.github.io/getting_started.html#getting-started)):

Regular select into model instances:

```
await Event.filter(name__startswith='FIFA')
```

This query will get you all events with `name` starting with `FIFA`, where `name` is fields defined on model, and `startswith` is filter modifier. Take note, that modifiers should be separated by double underscore. You can read more on filter modifiers in `Filtering` section of this document.

It’s also possible to filter your queries with `.exclude()`:

```
await Team.exclude(name__icontains='junior')
```

As more interesting case, when you are working with related data, you could also build your query around related entities:

```
# getting all events, which tournament name is "World Cup"
await Event.filter(tournament__name='World Cup')

# Gets all teams participating in events with ids 1, 2, 3
await Team.filter(events__id__in=[1,2,3])

# Gets all tournaments where teams with "junior" in their name are participating
await Tournament.filter(event__participants__name__icontains='junior').distinct()
```

Usually you not only want to filter by related data, but also get that related data as well. You could do it using `.prefetch_related()`:

```
# This will fetch events, and for each of events ``.tournament`` field will be populated with
# corresponding ``Tournament`` instance
await Event.all().prefetch_related('tournament')

# This will fetch tournament with their events and teams for each event
tournament_list = await Tournament.all().prefetch_related('events__participants')

# Fetched result for m2m and backward fk relations are stored in list-like containe#r
for tournament in tournament_list:
    print([e.name for e in tournament.events])
```

General rule about how `prefetch_related()` works is that each level of depth of related models produces 1 additional query, so `.prefetch_related('events__participants')` will produce two additional queries to fetch your data.

Sometimes, when performance is crucial, you don’t want to make additional queries like this. In cases like this you could use `values()` or `values_list()` to produce more efficient query

```
# This will return list of dicts with keys 'id', 'name', 'tournament_name' and
# 'tournament_name' will be populated by name of related tournament.
# And it will be done in one query
events = await Event.filter(id__in=[1,2,3]).values('id', 'name', tournament_name='tournament__name')
```

QuerySet also supports aggregation and database functions through `.annotate()` method

```
from tortoise.functions import Count, Trim, Lower, Upper, Coalesce

# This query will fetch all tournaments with 10 or more events, and will
# populate filed `.events_count` on instances with corresponding value
await Tournament.annotate(events_count=Count('events')).filter(events_count__gte=10)
await Tournament.annotate(clean_name=Trim('name')).filter(clean_name='tournament')
await Tournament.annotate(name_upper=Upper('name')).filter(name_upper='TOURNAMENT')
await Tournament.annotate(name_lower=Lower('name')).filter(name_lower='tournament')
await Tournament.annotate(desc_clean=Coalesce('desc', '')).filter(desc_clean='')
```

Check [examples](https://github.com/tortoise/tortoise-orm/tree/master/examples) to see it all in work

Foreign Key[¶](https://tortoise.github.io/query.html#foreign-key "Link to this heading")
----------------------------------------------------------------------------------------

Tortoise ORM provides an API for working with FK relations

_class_ tortoise.fields.relational.ReverseRelation(_[remote\_model](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation "tortoise.fields.relational.ReverseRelation.\_\_init\_\_.remote\_model (Python parameter)")_, _[relation\_field](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation "tortoise.fields.relational.ReverseRelation.\_\_init\_\_.relation\_field (Python parameter)")_, _[instance](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation "tortoise.fields.relational.ReverseRelation.\_\_init\_\_.instance (Python parameter)")_, _[from\_field](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation "tortoise.fields.relational.ReverseRelation.\_\_init\_\_.from\_field (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ReverseRelation)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation "Link to this definition")
Relation container for [`ForeignKeyField()`](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField (Python function) — ForeignKey relation field.").

all()[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ReverseRelation.all)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.all "Link to this definition")
Returns a QuerySet with all related elements.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.all-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

_async_ create(_[using\_db](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create.using\_db "tortoise.fields.relational.ReverseRelation.create.using\_db (Python parameter) — Specific DB connection to use instead of default bound.")=`None`_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create.kwargs "tortoise.fields.relational.ReverseRelation.create.kwargs (Python parameter) — Model parameters for the new object.")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ReverseRelation.create)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create "Link to this definition")
Create a related record in the DB and returns the object, automatically setting the foreign key relationship to the parent instance.

```
tournament = await Tournament.create(name="...")
event = await tournament.events.create(...)
```

Equivalent to:

```
tournament = await Tournament.create(name="...")
event = await Event.create(tournament=tournament, ...)
```

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create-parameters "Permalink to this headline")using_db=`None`[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound.

**kwargs[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create.kwargs "Permalink to this definition")
Model parameters for the new object.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create-raises "Permalink to this headline")
[**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – If parent instance is not saved to the database.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.create-return-type "Permalink to this headline")
[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")

filter(_*[args](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.filter "tortoise.fields.relational.ReverseRelation.filter.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.filter "tortoise.fields.relational.ReverseRelation.filter.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ReverseRelation.filter)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.filter "Link to this definition")
Returns a QuerySet with related elements filtered by args/kwargs.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.filter-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

limit(_[limit](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.limit "tortoise.fields.relational.ReverseRelation.limit.limit (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ReverseRelation.limit)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.limit "Link to this definition")
Returns a QuerySet with at most «limit» related elements.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.limit-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

offset(_[offset](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.offset "tortoise.fields.relational.ReverseRelation.offset.offset (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ReverseRelation.offset)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.offset "Link to this definition")
Returns a QuerySet with all related elements offset by «offset».

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.offset-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

order_by(_*[orderings](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.order\_by "tortoise.fields.relational.ReverseRelation.order\_by.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ReverseRelation.order_by)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.order_by "Link to this definition")
Returns a QuerySet related elements in order.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ReverseRelation.order_by-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

tortoise.fields.relational.ForeignKeyNullableRelation[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ForeignKeyNullableRelation "Link to this definition")
Type hint for the result of accessing the [`ForeignKeyField()`](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField (Python function) — ForeignKey relation field.") field in the model when obtained model can be nullable.

alias of `ForeignKeyFieldInstance`[`MODEL`] | `None`

tortoise.fields.relational.ForeignKeyRelation[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ForeignKeyRelation "Link to this definition")
Type hint for the result of accessing the [`ForeignKeyField()`](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField (Python function) — ForeignKey relation field.") field in the model.

alias of `ForeignKeyFieldInstance`[`MODEL`]

One to One[¶](https://tortoise.github.io/query.html#one-to-one "Link to this heading")
--------------------------------------------------------------------------------------

tortoise.fields.relational.OneToOneNullableRelation[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.OneToOneNullableRelation "Link to this definition")
Type hint for the result of accessing the [`OneToOneField()`](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField (Python function) — OneToOne relation field.") field in the model when obtained model can be nullable.

alias of `OneToOneFieldInstance`[`MODEL`] | `None`

tortoise.fields.relational.OneToOneRelation[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.OneToOneRelation "Link to this definition")
Type hint for the result of accessing the [`OneToOneField()`](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField (Python function) — OneToOne relation field.") field in the model.

alias of `OneToOneFieldInstance`[`MODEL`]

Many to Many[¶](https://tortoise.github.io/query.html#many-to-many "Link to this heading")
------------------------------------------------------------------------------------------

Tortoise ORM provides an API for working with M2M relations

_class_ tortoise.fields.relational.ManyToManyRelation(_[instance](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation "tortoise.fields.relational.ManyToManyRelation.\_\_init\_\_.instance (Python parameter)")_, _[m2m\_field](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation "tortoise.fields.relational.ManyToManyRelation.\_\_init\_\_.m2m\_field (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ManyToManyRelation)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation "Link to this definition")
Many-to-many relation container for [`ManyToManyField()`](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField (Python function) — ManyToMany relation field.").

_async_ add(_*[instances](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.add "tortoise.fields.relational.ManyToManyRelation.add.instances (Python parameter)")_, _[using\_db](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.add "tortoise.fields.relational.ManyToManyRelation.add.using\_db (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ManyToManyRelation.add)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.add "Link to this definition")
Adds one or more of `instances` to the relation.

If it is already added, it will be silently ignored.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.add-raises "Permalink to this headline")
[**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – If Object to add is not saved.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.add-return-type "Permalink to this headline")
`None`

all()[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.all "Link to this definition")
Returns a QuerySet with all related elements.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.all-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

_async_ clear(_[using\_db](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.clear "tortoise.fields.relational.ManyToManyRelation.clear.using\_db (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ManyToManyRelation.clear)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.clear "Link to this definition")
Clears ALL relations.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.clear-return-type "Permalink to this headline")
`None`

_async_ create(_[using\_db](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create.using\_db "tortoise.fields.relational.ManyToManyRelation.create.using\_db (Python parameter) — Specific DB connection to use instead of default bound.")=`None`_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create.kwargs "tortoise.fields.relational.ManyToManyRelation.create.kwargs (Python parameter) — Model parameters for the new object.")_)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create "Link to this definition")
Create a related record in the DB and returns the object, automatically setting the foreign key relationship to the parent instance.

```
tournament = await Tournament.create(name="...")
event = await tournament.events.create(...)
```

Equivalent to:

```
tournament = await Tournament.create(name="...")
event = await Event.create(tournament=tournament, ...)
```

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create-parameters "Permalink to this headline")using_db=`None`[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound.

**kwargs[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create.kwargs "Permalink to this definition")
Model parameters for the new object.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create-raises "Permalink to this headline")
[**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – If parent instance is not saved to the database.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.create-return-type "Permalink to this headline")
[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")

filter(_*[args](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.filter "tortoise.fields.relational.ManyToManyRelation.filter.args (Python parameter)")_, _**[kwargs](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.filter "tortoise.fields.relational.ManyToManyRelation.filter.kwargs (Python parameter)")_)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.filter "Link to this definition")
Returns a QuerySet with related elements filtered by args/kwargs.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.filter-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

limit(_[limit](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.limit "tortoise.fields.relational.ManyToManyRelation.limit.limit (Python parameter)")_)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.limit "Link to this definition")
Returns a QuerySet with at most «limit» related elements.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.limit-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

offset(_[offset](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.offset "tortoise.fields.relational.ManyToManyRelation.offset.offset (Python parameter)")_)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.offset "Link to this definition")
Returns a QuerySet with all related elements offset by «offset».

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.offset-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

order_by(_*[orderings](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.order\_by "tortoise.fields.relational.ManyToManyRelation.order\_by.orderings (Python parameter)")_)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.order_by "Link to this definition")
Returns a QuerySet related elements in order.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.order_by-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[MODEL]

_async_ remove(_*[instances](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.remove "tortoise.fields.relational.ManyToManyRelation.remove.instances (Python parameter)")_, _[using\_db](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.remove "tortoise.fields.relational.ManyToManyRelation.remove.using\_db (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ManyToManyRelation.remove)[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.remove "Link to this definition")
Removes one or more of `instances` from the relation.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.remove-raises "Permalink to this headline")
[**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – remove() was called with no instances.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation.remove-return-type "Permalink to this headline")
`None`

You can use them like this:

```
await event.participants.add(participant_1, participant_2)
```

Filtering[¶](https://tortoise.github.io/query.html#filtering "Link to this heading")
------------------------------------------------------------------------------------

When using the `.filter()` method, you can apply various modifiers to field names to specify the desired lookup type. In the following example, we filter the Team model to find all teams whose names contain the string CON (case-insensitive):

```
teams = await Team.filter(name__icontains='CON')
```

The following lookup types are available:

*   `not`

*   `in` - checks if value of field is in passed list

*   `not_in`

*   `gte` - greater or equals than passed value

*   `gt` - greater than passed value

*   `lte` - lower or equals than passed value

*   `lt` - lower than passed value

*   `range` - between and given two values

*   `isnull` - field is null

*   `not_isnull` - field is not null

*   `contains` - field contains specified substring

*   `icontains` - case insensitive `contains`

*   `startswith` - if field starts with value

*   `istartswith` - case insensitive `startswith`

*   `endswith` - if field ends with value

*   `iendswith` - case insensitive `endswith`

*   `iexact` - case insensitive equals

*   `search` - full text search

For PostgreSQL, `__search` uses `plainto_tsquery` by default. Text and char fields are wrapped in `to_tsvector`, while `TSVectorField` values are queried directly. You can also pass a [`SearchQuery`](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.search.SearchQuery "tortoise.contrib.postgres.search.SearchQuery (Python class)") to control the search type and configuration.

```
from tortoise.contrib.postgres.search import SearchQuery

await Article.filter(title__search="fast search")
await Article.filter(search__search="fast search")
await Article.filter(
    search__search=SearchQuery("fast & search", search_type="raw", config="english")
)
```

For PostgreSQL and MySQL, the following date related lookup types are available:

*   `year` - e.g. `await Team.filter(created_at__year=2020)`

*   `quarter`

*   `month`

*   `week`

*   `day`

*   `hour`

*   `minute`

*   `second`

*   `microsecond`

In PostgreSQL and MYSQL, you can use the `contains`, `contained_by` and `filter` options in `JSONField`. The `filter` option allows you to filter the JSON object by its keys and values.

```
class JSONModel:
    data = fields.JSONField[list]()

await JSONModel.create(data=["text", 3, {"msg": "msg2"}])
obj = await JSONModel.filter(data__contains=[{"msg": "msg2"}]).first()

await JSONModel.create(data=["text"])
await JSONModel.create(data=["tortoise", "msg"])
await JSONModel.create(data=["tortoise"])

objects = await JSONModel.filter(data__contained_by=["text", "tortoise", "msg"])

await JSONModel.create(data={"breed": "labrador",
                             "owner": {
                                 "name": "Boby",
                                 "last": None,
                                 "other_pets": [
                                     {
                                         "name": "Fishy",
                                     }
                                 ],
                             },
                         })

obj1 = await JSONModel.filter(data__filter={"breed": "labrador"}).first()
obj2 = await JSONModel.filter(data__filter={"owner__name": "Boby"}).first()
obj3 = await JSONModel.filter(data__filter={"owner__other_pets__0__name": "Fishy"}).first()
obj4 = await JSONModel.filter(data__filter={"breed__not": "a"}).first()
obj5 = await JSONModel.filter(data__filter={"owner__name__isnull": True}).first()
obj6 = await JSONModel.filter(data__filter={"owner__last__not_isnull": False}).first()
```

In PostgreSQL and MySQL and SQLite, you can use `posix_regex` to make comparisons using POSIX regular expressions: On PostgreSQL, this uses the `~` operator, on MySQL and SQLite it uses the `REGEXP` operator. PostgreSQL and SQLite also support `iposix_regex`, which makes case insensive comparisons.

```
class DemoModel:
  demo_text = fields.TextField()

await DemoModel.create(demo_text="Hello World")
obj = await DemoModel.filter(demo_text__posix_regex="^Hello World$").first()
obj = await DemoModel.filter(demo_text__iposix_regex="^hello world$").first()
```

With PostgreSQL, for `JSONField`, `filter` supports additional lookup types:

*   `in` - `await JSONModel.filter(data__filter={"breed__in": ["labrador", "poodle"]}).first()`

*   `not_in`

*   `gte`

*   `gt`

*   `lte`

*   `lt`

*   `range` - `await JSONModel.filter(data__filter={"age__range": [1, 10]}).first()`

*   `startswith`

*   `endswith`

*   `iexact`

*   `icontains`

*   `istartswith`

*   `iendswith`

With PostgreSQL, `ArrayField` can be used with the following lookup types:

*   `contains` - `await ArrayFields.filter(array__contains=[1, 2, 3]).first()` which will use the `@>` operator

*   `contained_by` - will use the `<@` operator

*   `overlap` - will use the `&&` operator

*   `len` - will use the `array_length` function, e.g. `await ArrayFields.filter(array__len=3).first()`

Complex prefetch[¶](https://tortoise.github.io/query.html#complex-prefetch "Link to this heading")
--------------------------------------------------------------------------------------------------

Sometimes it is required to fetch only certain related records. You can achieve it with `Prefetch` object:

```
tournament_with_filtered = await Tournament.all().prefetch_related(
    Prefetch('events', queryset=Event.filter(name='First'))
).first()
```

You can view full example here: [Prefetching](https://tortoise.github.io/examples/basic.html#example-prefetching)

_class_ tortoise.query_utils.Prefetch(_[relation](https://tortoise.github.io/query.html#tortoise.query\_utils.Prefetch.\_\_init\_\_.relation "tortoise.query\_utils.Prefetch.\_\_init\_\_.relation (Python parameter) — Related field name.")_, _[queryset](https://tortoise.github.io/query.html#tortoise.query\_utils.Prefetch.\_\_init\_\_.queryset "tortoise.query\_utils.Prefetch.\_\_init\_\_.queryset (Python parameter) — Custom QuerySet to use for prefetching.")_, _[to\_attr](https://tortoise.github.io/query.html#tortoise.query\_utils.Prefetch.\_\_init\_\_.to\_attr "tortoise.query\_utils.Prefetch.\_\_init\_\_.to\_attr (Python parameter) — Sets the result of the prefetch operation to a custom attribute.")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/query_utils.html#Prefetch)[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch "Link to this definition")
Prefetcher container. One would directly use this when wanting to attach a custom QuerySet for specialised prefetching.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch-parameters "Permalink to this headline")relation : str[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.__init__.relation "Permalink to this definition")
Related field name.

queryset : [QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.__init__.queryset "Permalink to this definition")
Custom QuerySet to use for prefetching.

to_attr : str | None[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.__init__.to_attr "Permalink to this definition")
Sets the result of the prefetch operation to a custom attribute.

resolve_for_queryset(_[queryset](https://tortoise.github.io/query.html#tortoise.query\_utils.Prefetch.resolve\_for\_queryset.queryset "tortoise.query\_utils.Prefetch.resolve\_for\_queryset.queryset (Python parameter) — Custom QuerySet to use for prefetching.")_)[[source]](https://tortoise.github.io/_modules/tortoise/query_utils.html#Prefetch.resolve_for_queryset)[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.resolve_for_queryset "Link to this definition")
Called internally to generate prefetching query.

Parameters:[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.resolve_for_queryset-parameters "Permalink to this headline")queryset : [QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.resolve_for_queryset.queryset "Permalink to this definition")
Custom QuerySet to use for prefetching.

Raises:[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.resolve_for_queryset-raises "Permalink to this headline")
[**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – If field does not exist in model.

Return type:[¶](https://tortoise.github.io/query.html#tortoise.query_utils.Prefetch.resolve_for_queryset-return-type "Permalink to this headline")
None
