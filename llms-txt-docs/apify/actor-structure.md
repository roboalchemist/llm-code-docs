# Source: https://docs.apify.com/sdk/python/docs/overview/actor-structure.md

# Actor structure

Copy for LLM

All Python Actor templates follow the same structure.

The `.actor/` directory contains the [Actor configuration](https://docs.apify.com/platform/actors/development/actor-config), such as the Actor's definition and input schema, and the Dockerfile necessary to run the Actor on the Apify platform.

The Actor's runtime dependencies are specified in the `requirements.txt` file, which follows the [standard requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/).

The Actor's source code is in the `src/` folder. This folder contains two important files: `main.py`, which contains the main function of the Actor, and `__main__.py`, which is the entrypoint of the Actor package, setting up the Actor [logger](https://docs.apify.com/sdk/python/sdk/python/docs/concepts/logging.md) and executing the Actor's main function via [`asyncio.run`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run).

* \_\_main.py\_\_
* main.py

```
import asyncio

from .main import main

if __name__ == '__main__':
    asyncio.run(main())
```

```
from apify import Actor


async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input()
        Actor.log.info('Actor input: %s', actor_input)
        await Actor.set_value('OUTPUT', 'Hello, world!')
```

If you want to modify the Actor structure, you need to make sure that your Actor is executable as a module, via `python -m src`, as that is the command started by `apify run` in the Apify CLI. We recommend keeping the entrypoint for the Actor in the `src/__main__.py` file.
