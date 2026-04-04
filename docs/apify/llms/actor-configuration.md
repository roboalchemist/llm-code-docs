# Source: https://docs.apify.com/sdk/python/docs/concepts/actor-configuration.md

# Actor configuration

Copy for LLM

The [`Actor`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md) class gets configured using the [`Configuration`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md) class, which initializes itself based on the provided environment variables.

If you're using the Apify SDK in your Actors on the Apify platform, or Actors running locally through the Apify CLI, you don't need to configure the `Actor` class manually,unless you have some specific requirements, everything will get configured automatically.

If you need some special configuration, you can adjust it either through the `Configuration` class directly,or by setting environment variables when running the Actor locally.

To see the full list of configuration options, check the `Configuration` class or the list of environment variables that the Actor understands.

## Configuring from code[](#configuring-from-code)

This will cause the Actor to persist its state every 10 seconds:

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuZnJvbSBkYXRldGltZSBpbXBvcnQgdGltZWRlbHRhXFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3IsIENvbmZpZ3VyYXRpb24sIEV2ZW50XFxuXFxuXFxuYXN5bmMgZGVmIG1haW4oKSAtPiBOb25lOlxcbiAgICBjb25maWd1cmF0aW9uID0gQ29uZmlndXJhdGlvbihcXG4gICAgICAgIHBlcnNpc3Rfc3RhdGVfaW50ZXJ2YWw9dGltZWRlbHRhKHNlY29uZHM9MTApXFxuICAgICAgICAjIFNldCBvdGhlciBjb25maWd1cmF0aW9uIG9wdGlvbnMgaGVyZSBhcyBuZWVkZWQuXFxuICAgIClcXG5cXG4gICAgYXN5bmMgd2l0aCBBY3Rvcihjb25maWd1cmF0aW9uPWNvbmZpZ3VyYXRpb24pOlxcbiAgICAgICAgIyBEZWZpbmUgYSBoYW5kbGVyIHRoYXQgd2lsbCBiZSBjYWxsZWQgZm9yIGV2ZXJ5IHBlcnNpc3Qgc3RhdGUgZXZlbnQuXFxuICAgICAgICBhc3luYyBkZWYgc2F2ZV9zdGF0ZSgpIC0-IE5vbmU6XFxuICAgICAgICAgICAgYXdhaXQgQWN0b3Iuc2V0X3ZhbHVlKCdTVEFURScsICdIZWxsbywgd29ybGQhJylcXG5cXG4gICAgICAgICMgVGhlIHNhdmVfc3RhdGUgaGFuZGxlciB3aWxsIGJlIGNhbGxlZCBldmVyeSAxMCBzZWNvbmRzIG5vdy5cXG4gICAgICAgIEFjdG9yLm9uKEV2ZW50LlBFUlNJU1RfU1RBVEUsIHNhdmVfc3RhdGUpXFxuXFxuXFxuaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzpcXG4gICAgYXN5bmNpby5ydW4obWFpbigpKVxcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.jrbhGRjqB5tlMvKvW2uCKjDF8hWmIkTe9A28UQseo78\&asrc=run_on_apify)

```
import asyncio
from datetime import timedelta

from apify import Actor, Configuration, Event


async def main() -> None:
    configuration = Configuration(
        persist_state_interval=timedelta(seconds=10)
        # Set other configuration options here as needed.
    )

    async with Actor(configuration=configuration):
        # Define a handler that will be called for every persist state event.
        async def save_state() -> None:
            await Actor.set_value('STATE', 'Hello, world!')

        # The save_state handler will be called every 10 seconds now.
        Actor.on(Event.PERSIST_STATE, save_state)


if __name__ == '__main__':
    asyncio.run(main())
```

## Configuring via environment variables[](#configuring-via-environment-variables)

All the configuration options can be set via environment variables. The environment variables are prefixed with `APIFY_`, and the configuration options are in uppercase, with underscores as separators. See the [`Configuration`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md) API reference for the full list of configuration options.

This Actor run will not persist its local storages to the filesystem:

```
APIFY_PERSIST_STORAGE=0 apify run
```
