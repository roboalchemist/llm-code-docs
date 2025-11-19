# Source: https://docs.apify.com/sdk/python/docs/concepts/actor-input.md

# Actor input

Copy for LLM

The Actor gets its [input](https://docs.apify.com/platform/actors/running/input) from the input record in its default [key-value store](https://docs.apify.com/platform/storage/key-value-store).

To access it, instead of reading the record manually, you can use the [`Actor.get_input`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md#get_input) convenience method. It will get the input record key from the Actor configuration, read the record from the default key-value store,and decrypt any [secret input fields](https://docs.apify.com/platform/actors/development/secret-input).

For example, if an Actor received a JSON input with two fields, `{ "firstNumber": 1, "secondNumber": 2 }`, this is how you might process it:

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3JcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICBhY3Rvcl9pbnB1dCA9IGF3YWl0IEFjdG9yLmdldF9pbnB1dCgpIG9yIHt9XFxuICAgICAgICBmaXJzdF9udW1iZXIgPSBhY3Rvcl9pbnB1dC5nZXQoJ2ZpcnN0TnVtYmVyJywgMClcXG4gICAgICAgIHNlY29uZF9udW1iZXIgPSBhY3Rvcl9pbnB1dC5nZXQoJ3NlY29uZE51bWJlcicsIDApXFxuICAgICAgICBBY3Rvci5sb2cuaW5mbygnU3VtOiAlcycsIGZpcnN0X251bWJlciArIHNlY29uZF9udW1iZXIpXFxuXFxuXFxuaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzpcXG4gICAgYXN5bmNpby5ydW4obWFpbigpKVxcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.CF_KyX6EAMxLr_mlIpVnOD9pKv7wI53qxf1HWTha69g\&asrc=run_on_apify)

```
import asyncio

from apify import Actor


async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input() or {}
        first_number = actor_input.get('firstNumber', 0)
        second_number = actor_input.get('secondNumber', 0)
        Actor.log.info('Sum: %s', first_number + second_number)


if __name__ == '__main__':
    asyncio.run(main())
```
