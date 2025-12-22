# Source: https://fastapi.tiangolo.com/tutorial/extra-models/

# Extra Models[&para;](#extra-models)

Continuing with the previous example, it will be common to have more than one related model.

This is especially the case for user models, because:

- The **input model** needs to be able to have a password.

- The **output model** should not have a password.

- The **database model** would probably need to have a hashed password.

Danger

Never store user's plaintext passwords. Always store a "secure hash" that you can then verify.

If you don't know, you will learn what a "password hash" is in the [security chapters](../security/simple-oauth2/#password-hashing).

## Multiple models[&para;](#multiple-models)

Here's a general idea of how the models could look like with their password fields and the places where they are used:

Python 3.10+

🤓 Other versions and variants

Python 3.9+

### About `**user_in.model_dump()`[&para;](#about-user-in-model-dump)

#### Pydantic's `.model_dump()`[&para;](#pydantics-model-dump)

`user_in` is a Pydantic model of class `UserIn`.

Pydantic models have a `.model_dump()` method that returns a `dict` with the model's data.

So, if we create a Pydantic object `user_in` like:

`user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
`

and then we call:

`user_dict = user_in.model_dump()
`

we now have a `dict` with the data in the variable `user_dict` (it's a `dict` instead of a Pydantic model object).

And if we call:

`print(user_dict)
`

we would get a Python `dict` with:

`{
    'username': 'john',
    'password': 'secret',
    'email': 'john.doe@example.com',
    'full_name': None,
}
`

#### Unpacking a `dict`[&para;](#unpacking-a-dict)

If we take a `dict` like `user_dict` and pass it to a function (or class) with `**user_dict`, Python will "unpack" it. It will pass the keys and values of the `user_dict` directly as key-value arguments.

So, continuing with the `user_dict` from above, writing:

`UserInDB(**user_dict)
`

would result in something equivalent to:

`UserInDB(
    username="john",
    password="secret",
    email="john.doe@example.com",
    full_name=None,
)
`

Or more exactly, using `user_dict` directly, with whatever contents it might have in the future:

`UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
)
`

#### A Pydantic model from the contents of another[&para;](#a-pydantic-model-from-the-contents-of-another)

As in the example above we got `user_dict` from `user_in.model_dump()`, this code:

`user_dict = user_in.model_dump()
UserInDB(**user_dict)
`

would be equivalent to:

`UserInDB(**user_in.model_dump())
`

...because `user_in.model_dump()` is a `dict`, and then we make Python "unpack" it by passing it to `UserInDB` prefixed with `**`.

So, we get a Pydantic model from the data in another Pydantic model.

#### Unpacking a `dict` and extra keywords[&para;](#unpacking-a-dict-and-extra-keywords)

And then adding the extra keyword argument `hashed_password=hashed_password`, like in:

`UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
`

...ends up being like:

`UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    hashed_password = hashed_password,
)
`

Warning

The supporting additional functions `fake_password_hasher` and `fake_save_user` are just to demo a possible flow of the data, but they of course are not providing any real security.

## Reduce duplication[&para;](#reduce-duplication)

Reducing code duplication is one of the core ideas in **FastAPI**.

As code duplication increments the chances of bugs, security issues, code desynchronization issues (when you update in one place but not in the others), etc.

And these models are all sharing a lot of the data and duplicating attribute names and types.

We could do better.

We can declare a `UserBase` model that serves as a base for our other models. And then we can make subclasses of that model that inherit its attributes (type declarations, validation, etc).

All the data conversion, validation, documentation, etc. will still work as normally.

That way, we can declare just the differences between the models (with plaintext `password`, with `hashed_password` and without password):

Python 3.10+

🤓 Other versions and variants

Python 3.9+

## `Union` or `anyOf`[&para;](#union-or-anyof)

You can declare a response to be the `Union` of two or more types, that means, that the response would be any of them.

It will be defined in OpenAPI with `anyOf`.

To do that, use the standard Python type hint [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union):

Note

When defining a [`Union`](https://docs.pydantic.dev/latest/concepts/types/#unions), include the most specific type first, followed by the less specific type. In the example below, the more specific `PlaneItem` comes before `CarItem` in `Union[PlaneItem, CarItem]`.

Python 3.10+

🤓 Other versions and variants

Python 3.9+

### `Union` in Python 3.10[&para;](#union-in-python-3-10)

In this example we pass `Union[PlaneItem, CarItem]` as the value of the argument `response_model`.

Because we are passing it as a **value to an argument** instead of putting it in a **type annotation**, we have to use `Union` even in Python 3.10.

If it was in a type annotation we could have used the vertical bar, as:

`some_variable: PlaneItem | CarItem
`

But if we put that in the assignment `response_model=PlaneItem | CarItem` we would get an error, because Python would try to perform an **invalid operation** between `PlaneItem` and `CarItem` instead of interpreting that as a type annotation.

## List of models[&para;](#list-of-models)

The same way, you can declare responses of lists of objects.

For that, use the standard Python `typing.List` (or just `list` in Python 3.9 and above):

Python 3.9+

## Response with arbitrary `dict`[&para;](#response-with-arbitrary-dict)

You can also declare a response using a plain arbitrary `dict`, declaring just the type of the keys and values, without using a Pydantic model.

This is useful if you don't know the valid field/attribute names (that would be needed for a Pydantic model) beforehand.

In this case, you can use `typing.Dict` (or just `dict` in Python 3.9 and above):

Python 3.9+

## Recap[&para;](#recap)

Use multiple Pydantic models and inherit freely for each case.

You don't need to have a single data model per entity if that entity must be able to have different "states". As the case with the user "entity" with a state including `password`, `password_hash` and no password.