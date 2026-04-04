# Finding documents - Beanie Documentation

Source: https://beanie-odm.dev/tutorial/finding-documents/

![logo](../../assets/logo.svg)
![logo](../../assets/logo.svg)

# Finding documents

To populate the database, please run the examples from the [previous section of the tutorial](../inserting-into-the-database/)
as we will be using the same setup here.

## Finding documents

The basic syntax for finding multiple documents in the database is to call the class method `find()`
or it's synonym `find_many()` with some search criteria (see next section):

`find()`
`find_many()`
`findresult = Product.find(search_criteria)`

This returns a `FindMany` object, which can be used to access the results in different ways.
To loop through the results, use a `async for` loop:

`FindMany`
`async for`
`async for result in Product.find(search_criteria):
print(result)`

If you prefer a list of the results, then you can call `to_list()` method:

`to_list()`
`result = await Product.find(search_criteria).to_list()`

To get the first document, you can use `.first_or_none()` method.
It returns the first found document or `None`, if no documents were found.

`.first_or_none()`
`None`
`result = await Product.find(search_criteria).first_or_none()`

### Search criteria

As search criteria, Beanie supports Python-based syntax.
For comparisons Python comparison operators can be used on the class fields (and nested
fields):

`products = await Product.find(Product.price < 10).to_list()`

This is supported for the following operators: `==`, `>`, `>=`, `<`, `<=`, `!=`.
Other MongoDB query operators can be used with the included wrappers.
For example, the `$in` operator can be used as follows:

`==`
`>`
`>=`
`<`
`<=`
`!=`
`$in`
`from beanie.operators import In
products = await Product.find(
In(Product.category.name, ["Chocolate", "Fruits"])
).to_list()`

The whole list of the find query operators can be found [here](../../api-documentation/operators/find/).

For more complex cases native PyMongo syntax is also supported:

`products = await Product.find({"price": 1000}).to_list()`

## Finding single documents

Sometimes you will only need to find a single document.
If you are searching by `id`, then you can use the [get](../../api-documentation/document/#documentget) method:

`id`
`bar = await Product.get("608da169eb9e17281f0ab2ff")`

To find a single document via a single search criterion,
you can use the [find\_one](../../api-documentation/interfaces/#findinterfacefind_one) method:

`bar = await Product.find_one(Product.name == "Peanut Bar")`

## Syncing from the Database

If you wish to apply changes from the database to the document, utilize the [sync](../../api-documentation/document/#documentsync) method:

`await bar.sync()`

Two merging strategies are available: `local` and `remote`.

`local`
`remote`

### Remote Merge Strategy

The remote merge strategy replaces the local document with the one from the database, disregarding local changes:

```
from beanie import MergeStrategy

await bar.sync(merge_strategy=MergeStrategy.remote)

```

The remote merge strategy is the default.

`from beanie import MergeStrategy
await bar.sync(merge_strategy=MergeStrategy.remote)`

### Local Merge Strategy

The local merge strategy retains changes made locally to the document and updates other fields from the database.
**BE CAREFUL**: it may raise an `ApplyChangesException` in case of a merging conflict.

`ApplyChangesException`
`from beanie import MergeStrategy
await bar.sync(merge_strategy=MergeStrategy.local)`

## More complex queries

### Multiple search criteria

If you have multiple criteria to search against,
you can pass them as separate arguments to any of the `find` functions:

`find`
`chocolates = await Product.find(
Product.category.name == "Chocolate",
Product.price < 5
).to_list()`

Alternatively, you can chain `find` methods:

`find`
`chocolates = await Product
.find(Product.category.name == "Chocolate")
.find(Product.price < 5).to_list()`

### Sorting

Sorting can be done with the [sort](../../api-documentation/query/#findmanysort) method.

You can pass it one or multiple fields to sort by. You may optionally specify a `+` or `-`
(denoting ascending and descending respectively).

`+`
`-`
`chocolates = await Product.find(
Product.category.name == "Chocolate").sort(-Product.price,+Product.name).to_list()`

You can also specify fields as strings or as tuples:

`chocolates = await Product.find(
Product.category.name == "Chocolate").sort("-price","+name").to_list()
chocolates = await Product.find(
Product.category.name == "Chocolate").sort(
[
(Product.price, pymongo.DESCENDING),
(Product.name, pymongo.ASCENDING),
]
).to_list()`

### Skip and limit

To skip a certain number of documents, or limit the total number of elements returned,
the `skip` and `limit` methods can be used:

```
chocolates = await Product.find(
    Product.category.name == "Chocolate").skip(2).to_list()

chocolates = await Product.find(
    Product.category.name == "Chocolate").limit(2).to_list()

```

`skip`
`limit`
`chocolates = await Product.find(
Product.category.name == "Chocolate").skip(2).to_list()
chocolates = await Product.find(
Product.category.name == "Chocolate").limit(2).to_list()`

### Distinct

To get a list of distinct values for a specific field, use the `distinct()` method.
`distinct()` is available on `find()` / `find_many()` queries (not on `find_one()`):

`distinct()`
`distinct()`
`find()`
`find_many()`
`find_one()`
`categories = await Product.find(Product.price < 10).distinct("category.name")`

This also works with `fetch_links=True`, so you can filter by linked document fields:

`fetch_links=True`
`names = await Product.find(
Product.category.name == "Chocolate", fetch_links=True
).distinct("name")`

Note that `skip` and `limit` are ignored by `distinct()` since distinct values are unordered and MongoDB's distinct command does not support pagination.

`skip`
`limit`
`distinct()`

`distinct()` is a **terminal** method — it executes the query and returns a `list`, not a query object. Keep the following composition rules in mind:

`distinct()`
`list`

| Chain | Allowed | Rationale |
| --- | --- | --- |
| `Model.find(filter).distinct(field)` | Yes | Natural "distinct over filtered set". |
| `Model.find(filter).project(P).distinct(field)` | Yes | Projection does not affect distinct results. |
| `Model.find(filter).distinct(field).aggregate(...)` | No | `distinct()` is terminal and returns a list. |
| `Model.find(filter).aggregate(pipeline).distinct(field)` | No | Use `$group` / `$addToSet` inside the pipeline instead. |

`Model.find(filter).distinct(field)`
`Model.find(filter).project(P).distinct(field)`
`Model.find(filter).distinct(field).aggregate(...)`
`distinct()`
`Model.find(filter).aggregate(pipeline).distinct(field)`
`$group`
`$addToSet`

### Projections

When only a part of a document is required, projections can save a lot of database bandwidth and processing.
For simple projections we can just define a pydantic model with the required fields and pass it to `project()` method:

`project()`
`class ProductShortView(BaseModel):
name: str
price: float
chocolates = await Product.find(
Product.category.name == "Chocolate").project(ProductShortView).to_list()`

For more complex projections an inner `Settings` class with a `projection` field can be added:

`Settings`
`projection`
`class ProductView(BaseModel):
name: str
category: str
class Settings:
projection = {"name": 1, "category": "$category.name"}
chocolates = await Product.find(
Product.category.name == "Chocolate").project(ProductView).to_list()`

### Chaining `.find()` with `fetch_links=True`

`.find()`
`fetch_links=True`

You can now safely chain `.find()` calls and preserve the `fetch_links` flag automatically:

`.find()`
`fetch_links`
`query = Conversation.find(Conversation.user == user_id, fetch_links=True)
if updated_at_from is not None:
query = query.find(Conversation.updated_at >= updated_at_from)
conversations = await query.to_list()`

### Finding all documents

If you ever want to find all documents, you can use the `find_all()` class method. This is equivalent to `find({})`.

`find_all()`
`find({})`

---

