# Source: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/

# Path Operation Configuration[&para;](#path-operation-configuration)

There are several parameters that you can pass to your *path operation decorator* to configure it.

Warning

Notice that these parameters are passed directly to the *path operation decorator*, not to your *path operation function*.

## Response Status Code[&para;](#response-status-code)

You can define the (HTTP) `status_code` to be used in the response of your *path operation*.

You can pass directly the `int` code, like `404`.

But if you don't remember what each number code is for, you can use the shortcut constants in `status`:

Python 3.10+

🤓 Other versions and variants

Python 3.9+

That status code will be used in the response and will be added to the OpenAPI schema.

Technical Details

You could also use `from starlette import status`.

**FastAPI** provides the same `starlette.status` as `fastapi.status` just as a convenience for you, the developer. But it comes directly from Starlette.

## Tags[&para;](#tags)

You can add tags to your *path operation*, pass the parameter `tags` with a `list` of `str` (commonly just one `str`):

Python 3.10+

🤓 Other versions and variants

Python 3.9+

They will be added to the OpenAPI schema and used by the automatic documentation interfaces:

### Tags with Enums[&para;](#tags-with-enums)

If you have a big application, you might end up accumulating **several tags**, and you would want to make sure you always use the **same tag** for related *path operations*.

In these cases, it could make sense to store the tags in an `Enum`.

**FastAPI** supports that the same way as with plain strings:

Python 3.9+

## Summary and description[&para;](#summary-and-description)

You can add a `summary` and `description`:

Python 3.10+

🤓 Other versions and variants

Python 3.9+

## Description from docstring[&para;](#description-from-docstring)

As descriptions tend to be long and cover multiple lines, you can declare the *path operation* description in the function docstring and **FastAPI** will read it from there.

You can write [Markdown](https://en.wikipedia.org/wiki/Markdown) in the docstring, it will be interpreted and displayed correctly (taking into account docstring indentation).

Python 3.10+

🤓 Other versions and variants

Python 3.9+

It will be used in the interactive docs:

## Response description[&para;](#response-description)

You can specify the response description with the parameter `response_description`:

Python 3.10+

🤓 Other versions and variants

Python 3.9+

Info

Notice that `response_description` refers specifically to the response, the `description` refers to the *path operation* in general.

Check

OpenAPI specifies that each *path operation* requires a response description.

So, if you don't provide one, **FastAPI** will automatically generate one of "Successful response".

## Deprecate a *path operation*[&para;](#deprecate-a-path-operation)

If you need to mark a *path operation* as deprecated, but without removing it, pass the parameter `deprecated`:

Python 3.9+

It will be clearly marked as deprecated in the interactive docs:

Check how deprecated and non-deprecated *path operations* look like:

## Recap[&para;](#recap)

You can configure and add metadata for your *path operations* easily by passing parameters to the *path operation decorators*.