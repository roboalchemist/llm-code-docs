# Source: https://fastapi.tiangolo.com/advanced/dataclasses/

# Using Dataclasses[&para;](#using-dataclasses)

FastAPI is built on top of **Pydantic**, and I have been showing you how to use Pydantic models to declare requests and responses.

But FastAPI also supports using [`dataclasses`](https://docs.python.org/3/library/dataclasses.html) the same way:

Python 3.10+

🤓 Other versions and variants

Python 3.9+

This is still supported thanks to **Pydantic**, as it has [internal support for `dataclasses`](https://docs.pydantic.dev/latest/concepts/dataclasses/#use-of-stdlib-dataclasses-with-basemodel).

So, even with the code above that doesn't use Pydantic explicitly, FastAPI is using Pydantic to convert those standard dataclasses to Pydantic's own flavor of dataclasses.

And of course, it supports the same:

- data validation

- data serialization

- data documentation, etc.

This works the same way as with Pydantic models. And it is actually achieved in the same way underneath, using Pydantic.

Info

Keep in mind that dataclasses can't do everything Pydantic models can do.

So, you might still need to use Pydantic models.

But if you have a bunch of dataclasses laying around, this is a nice trick to use them to power a web API using FastAPI. 🤓

## Dataclasses in `response_model`[&para;](#dataclasses-in-response-model)

You can also use `dataclasses` in the `response_model` parameter:

Python 3.10+

🤓 Other versions and variants

Python 3.9+

The dataclass will be automatically converted to a Pydantic dataclass.

This way, its schema will show up in the API docs user interface:

## Dataclasses in Nested Data Structures[&para;](#dataclasses-in-nested-data-structures)

You can also combine `dataclasses` with other type annotations to make nested data structures.

In some cases, you might still have to use Pydantic's version of `dataclasses`. For example, if you have errors with the automatically generated API documentation.

In that case, you can simply swap the standard `dataclasses` with `pydantic.dataclasses`, which is a drop-in replacement:

Python 3.10+

🤓 Other versions and variants

Python 3.9+

- 

We still import `field` from standard `dataclasses`.

- 

`pydantic.dataclasses` is a drop-in replacement for `dataclasses`.

- 

The `Author` dataclass includes a list of `Item` dataclasses.

- 

The `Author` dataclass is used as the `response_model` parameter.

- 

You can use other standard type annotations with dataclasses as the request body.

In this case, it's a list of `Item` dataclasses.

- 

Here we are returning a dictionary that contains `items` which is a list of dataclasses.

FastAPI is still capable of serializing the data to JSON.

- 

Here the `response_model` is using a type annotation of a list of `Author` dataclasses.

Again, you can combine `dataclasses` with standard type annotations.

- 

Notice that this *path operation function* uses regular `def` instead of `async def`.

As always, in FastAPI you can combine `def` and `async def` as needed.

If you need a refresher about when to use which, check out the section *"In a hurry?"* in the docs about [`async` and `await`](../../async/#in-a-hurry).

- 

This *path operation function* is not returning dataclasses (although it could), but a list of dictionaries with internal data.

FastAPI will use the `response_model` parameter (that includes dataclasses) to convert the response.

You can combine `dataclasses` with other type annotations in many different combinations to form complex data structures.

Check the in-code annotation tips above to see more specific details.

## Learn More[&para;](#learn-more)

You can also combine `dataclasses` with other Pydantic models, inherit from them, include them in your own models, etc.

To learn more, check the [Pydantic docs about dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/).

## Version[&para;](#version)

This is available since FastAPI version `0.67.0`. 🔖