# Source: https://fastapi.tiangolo.com/tutorial/cookie-params/

# Cookie Parameters[&para;](#cookie-parameters)

You can define Cookie parameters the same way you define `Query` and `Path` parameters.

## Import `Cookie`[&para;](#import-cookie)

First import `Cookie`:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

`from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
`

`from typing import Union

from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}
`

## Declare `Cookie` parameters[&para;](#declare-cookie-parameters)

Then declare the cookie parameters using the same structure as with `Path` and `Query`.

You can define the default value as well as all the extra validation or annotation parameters:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

`from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
`

`from typing import Union

from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}
`

Technical Details

`Cookie` is a "sister" class of `Path` and `Query`. It also inherits from the same common `Param` class.

But remember that when you import `Query`, `Path`, `Cookie` and others from `fastapi`, those are actually functions that return special classes.

Info

To declare cookies, you need to use `Cookie`, because otherwise the parameters would be interpreted as query parameters.

Info

Have in mind that, as **browsers handle cookies** in special ways and behind the scenes, they **don't** easily allow **JavaScript** to touch them.

If you go to the **API docs UI** at `/docs` you will be able to see the **documentation** for cookies for your *path operations*.

But even if you **fill the data** and click "Execute", because the docs UI works with **JavaScript**, the cookies won't be sent, and you will see an **error** message as if you didn't write any values.

## Recap[&para;](#recap)

Declare cookies with `Cookie`, using the same common pattern as `Query` and `Path`.