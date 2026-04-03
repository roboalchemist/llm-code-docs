# Source: https://python.useinstructor.com/concepts/iterable/index.md

# Multi-Task and Streaming

Using an `Iterable` lets you extract multiple structured objects from a single LLM call, streaming them as they arrive. This is useful for entity extraction, multi-task outputs, and more.

**We recommend using the `create_iterable` method for most use cases.** It's simpler and less error-prone than manually specifying `Iterable[...]` and `stream=True`.

Here's a simple example showing how to extract multiple users from a single sentence. You can use either the recommended `create_iterable` method or the `create` method with `Iterable[User]`:

```python
import instructor
from pydantic import BaseModel

client = instructor.from_provider("openai/gpt-4.1-mini")


class User(BaseModel):
    name: str
    age: int


resp = client.create_iterable(
    messages=[
        {
            "role": "user",
            "content": "Ivan is 28, lives in Moscow and his friends are Alex, John and Mary who are 25, 30 and 27 respectively",
        }
    ],
    response_model=User,
)

for user in resp:
    print(user)
    #> name='Ivan' age=28
    #> name='Alex' age=25
    #> name='John' age=30
    #> name='Mary' age=27
```

*Recommended for most use cases. Handles streaming and iteration for you.*

```python
import instructor
from pydantic import BaseModel
from typing import Iterable

client = instructor.from_provider("openai/gpt-4.1-mini")


class User(BaseModel):
    name: str
    age: int


resp = client.create(
    messages=[
        {
            "role": "user",
            "content": "Ivan is 28, lives in Moscow and his friends are Alex, John and Mary who are 25, 30 and 27 respectively",
        }
    ],
    response_model=Iterable[User],
)

for user in resp:
    print(user)
    #> name='Ivan' age=28
    #> name='Alex' age=25
    #> name='John' age=30
    #> name='Mary' age=27
```

*Use this if you need more manual control or compatibility with legacy code.*

______________________________________________________________________

We also support more complex extraction patterns such as Unions as you'll see below out of the box.

Warning

Unions don't work with Gemini because the AnyOf is not supported in the current response schema.

## Synchronous Usage

```python
import instructor
from typing import Iterable, Union, Literal
from pydantic import BaseModel


class Weather(BaseModel):
    location: str
    units: Literal["imperial", "metric"]


class GoogleSearch(BaseModel):
    query: str


client = instructor.from_provider("openai/gpt-4.1-mini", mode=instructor.Mode.TOOLS)

results = client.create(
    messages=[
        {"role": "system", "content": "You must always use tools"},
        {
            "role": "user",
            "content": "What is the weather in toronto and dallas and who won the super bowl?",
        },
    ],
    response_model=Iterable[Union[Weather, GoogleSearch]],
    stream=True,
)

for item in results:
    print(item)
    #> location='Toronto' units='metric'
    #> location='Dallas' units='imperial'
    #> query='Super Bowl winner'
```

```python
import instructor
from typing import Union, Literal
from pydantic import BaseModel


class Weather(BaseModel):
    location: str
    units: Literal["imperial", "metric"]


class GoogleSearch(BaseModel):
    query: str


client = instructor.from_provider("openai/gpt-4.1-mini", mode=instructor.Mode.TOOLS)

results = client.create_iterable(
    messages=[
        {"role": "system", "content": "You must always use tools"},
        {
            "role": "user",
            "content": "What is the weather in toronto and dallas and who won the super bowl?",
        },
    ],
    response_model=Union[Weather, GoogleSearch],
)

for item in results:
    print(item)
    #> location='Toronto' units='metric'
    #> location='Dallas' units='imperial'
    #> query='Super Bowl winner'
```

______________________________________________________________________

## See Also

- [Streaming Lists](https://python.useinstructor.com/concepts/lists/index.md) - Similar functionality with different API
- [Streaming Partial](https://python.useinstructor.com/concepts/partial/index.md) - Stream partially completed objects
- [List Extraction Tutorial](https://python.useinstructor.com/learning/patterns/list_extraction/index.md) - Step-by-step guide
- [Streaming Basics](https://python.useinstructor.com/learning/streaming/basics/index.md) - Introduction to streaming

## Asynchronous Usage

```python
import instructor
from typing import Iterable, Union, Literal
from pydantic import BaseModel
import asyncio


class Weather(BaseModel):
    location: str
    units: Literal["imperial", "metric"]


class GoogleSearch(BaseModel):
    query: str


aclient = instructor.from_provider(
    "openai/gpt-4.1-mini", async_client=True, mode=instructor.Mode.TOOLS
)


async def main():
    results = await aclient.create(
        messages=[
            {"role": "system", "content": "You must always use tools"},
            {
                "role": "user",
                "content": "What is the weather in toronto and dallas and who won the super bowl?",
            },
        ],
        response_model=Iterable[Union[Weather, GoogleSearch]],
        stream=True,
    )
    async for item in results:
        print(item)
        #> location='Toronto' units='metric'
        #> location='Dallas' units='imperial'
        #> query='Super Bowl winner'


asyncio.run(main())
```

```python
import asyncio
from typing import Literal, Union

import instructor
from pydantic import BaseModel


class Weather(BaseModel):
    location: str
    units: Literal["imperial", "metric"]


class GoogleSearch(BaseModel):
    query: str


aclient = instructor.from_provider(
    "openai/gpt-4.1-mini", async_client=True, mode=instructor.Mode.TOOLS
)


async def iter_results():
    async for item in aclient.create_iterable(
        messages=[
            {"role": "system", "content": "You must always use tools"},
            {
                "role": "user",
                "content": "What is the weather in toronto and dallas and who won the super bowl?",
            },
        ],
        response_model=Union[Weather, GoogleSearch],
    ):
        yield item


async def main():
    async for item in iter_results():
        print(item)
        #> location='Toronto' units='metric'
        #> location='Dallas' units='imperial'
        #> query='Super Bowl winner'


asyncio.run(main())
```
