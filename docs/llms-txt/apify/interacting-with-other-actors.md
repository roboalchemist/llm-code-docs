# Source: https://docs.apify.com/sdk/python/docs/concepts/interacting-with-other-actors.md

# Interacting with other Actors

Copy for LLM

There are several methods that interact with other Actors and Actor tasks on the Apify platform.

## Actor start[](#actor-start)

The [`Actor.start`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md#start) method starts another Actor on the Apify platform, and immediately returns the details of the started Actor run.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3JcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIFN0YXJ0IHlvdXIgb3duIEFjdG9yIG5hbWVkICdteS1mYW5jeS1hY3RvcicuXFxuICAgICAgICBhY3Rvcl9ydW4gPSBhd2FpdCBBY3Rvci5zdGFydChcXG4gICAgICAgICAgICBhY3Rvcl9pZD0nfm15LWZhbmN5LWFjdG9yJyxcXG4gICAgICAgICAgICBydW5faW5wdXQ9eydmb28nOiAnYmFyJ30sXFxuICAgICAgICApXFxuXFxuICAgICAgICAjIExvZyB0aGUgQWN0b3IgcnVuIElELlxcbiAgICAgICAgQWN0b3IubG9nLmluZm8oZidBY3RvciBydW4gSUQ6IHthY3Rvcl9ydW4uaWR9JylcXG5cXG5cXG5pZiBfX25hbWVfXyA9PSAnX19tYWluX18nOlxcbiAgICBhc3luY2lvLnJ1bihtYWluKCkpXFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.OZwyqz2jbWOpDGJBr-KQx6Jnp1-dBrbV7peOD9O_dlA\&asrc=run_on_apify)

```
import asyncio

from apify import Actor


async def main() -> None:
    async with Actor:
        # Start your own Actor named 'my-fancy-actor'.
        actor_run = await Actor.start(
            actor_id='~my-fancy-actor',
            run_input={'foo': 'bar'},
        )

        # Log the Actor run ID.
        Actor.log.info(f'Actor run ID: {actor_run.id}')


if __name__ == '__main__':
    asyncio.run(main())
```

## Actor call[](#actor-call)

The [`Actor.call`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md#call) method starts another Actor on the Apify platform, and waits for the started Actor run to finish.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3JcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIFN0YXJ0IHRoZSBhcGlmeS9zY3JlZW5zaG90LXVybCBBY3Rvci5cXG4gICAgICAgIGFjdG9yX3J1biA9IGF3YWl0IEFjdG9yLmNhbGwoXFxuICAgICAgICAgICAgYWN0b3JfaWQ9J2FwaWZ5L3NjcmVlbnNob3QtdXJsJyxcXG4gICAgICAgICAgICBydW5faW5wdXQ9eyd1cmwnOiAnaHR0cDovL2V4YW1wbGUuY29tJywgJ2RlbGF5JzogMTAwMDB9LFxcbiAgICAgICAgKVxcblxcbiAgICAgICAgaWYgYWN0b3JfcnVuIGlzIE5vbmU6XFxuICAgICAgICAgICAgcmFpc2UgUnVudGltZUVycm9yKCdBY3RvciB0YXNrIGZhaWxlZCB0byBzdGFydC4nKVxcblxcbiAgICAgICAgIyBXYWl0IGZvciB0aGUgQWN0b3IgcnVuIHRvIGZpbmlzaC5cXG4gICAgICAgIHJ1bl9jbGllbnQgPSBBY3Rvci5hcGlmeV9jbGllbnQucnVuKGFjdG9yX3J1bi5pZClcXG4gICAgICAgIGF3YWl0IHJ1bl9jbGllbnQud2FpdF9mb3JfZmluaXNoKClcXG5cXG4gICAgICAgICMgR2V0IHRoZSBBY3RvciBvdXRwdXQgZnJvbSB0aGUga2V5LXZhbHVlIHN0b3JlLlxcbiAgICAgICAga3ZzX2NsaWVudCA9IHJ1bl9jbGllbnQua2V5X3ZhbHVlX3N0b3JlKClcXG4gICAgICAgIG91dHB1dCA9IGF3YWl0IGt2c19jbGllbnQuZ2V0X3JlY29yZCgnT1VUUFVUJylcXG4gICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnQWN0b3Igb3V0cHV0OiB7b3V0cHV0fScpXFxuXFxuXFxuaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzpcXG4gICAgYXN5bmNpby5ydW4obWFpbigpKVxcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.I-hil0WZXcah3NI4F3WSgQPkqFkqWbTuJ76k9RWofC8\&asrc=run_on_apify)

```
import asyncio

from apify import Actor


async def main() -> None:
    async with Actor:
        # Start the apify/screenshot-url Actor.
        actor_run = await Actor.call(
            actor_id='apify/screenshot-url',
            run_input={'url': 'http://example.com', 'delay': 10000},
        )

        if actor_run is None:
            raise RuntimeError('Actor task failed to start.')

        # Wait for the Actor run to finish.
        run_client = Actor.apify_client.run(actor_run.id)
        await run_client.wait_for_finish()

        # Get the Actor output from the key-value store.
        kvs_client = run_client.key_value_store()
        output = await kvs_client.get_record('OUTPUT')
        Actor.log.info(f'Actor output: {output}')


if __name__ == '__main__':
    asyncio.run(main())
```

## Actor call task[](#actor-call-task)

The [`Actor.call_task`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md#call_task) method starts an [Actor task](https://docs.apify.com/platform/actors/tasks) on the Apify platform, and waits for the started Actor run to finish.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3JcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIFN0YXJ0IHRoZSBBY3RvciB0YXNrIGJ5IGl0cyBJRC5cXG4gICAgICAgIGFjdG9yX3J1biA9IGF3YWl0IEFjdG9yLmNhbGxfdGFzayh0YXNrX2lkPSdaM202RlBTajBHWVoyNXJRYycpXFxuXFxuICAgICAgICBpZiBhY3Rvcl9ydW4gaXMgTm9uZTpcXG4gICAgICAgICAgICByYWlzZSBSdW50aW1lRXJyb3IoJ0FjdG9yIHRhc2sgZmFpbGVkIHRvIHN0YXJ0LicpXFxuXFxuICAgICAgICAjIFdhaXQgZm9yIHRoZSB0YXNrIHJ1biB0byBmaW5pc2guXFxuICAgICAgICBydW5fY2xpZW50ID0gQWN0b3IuYXBpZnlfY2xpZW50LnJ1bihhY3Rvcl9ydW4uaWQpXFxuICAgICAgICBhd2FpdCBydW5fY2xpZW50LndhaXRfZm9yX2ZpbmlzaCgpXFxuXFxuICAgICAgICAjIEdldCB0aGUgdGFzayBydW4gZGF0YXNldCBpdGVtc1xcbiAgICAgICAgZGF0YXNldF9jbGllbnQgPSBydW5fY2xpZW50LmRhdGFzZXQoKVxcbiAgICAgICAgaXRlbXMgPSBhd2FpdCBkYXRhc2V0X2NsaWVudC5saXN0X2l0ZW1zKClcXG4gICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnVGFzayBydW4gZGF0YXNldCBpdGVtczoge2l0ZW1zfScpXFxuXFxuXFxuaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzpcXG4gICAgYXN5bmNpby5ydW4obWFpbigpKVxcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.GlXlYKy7w-LMyvCLVTLXknpcJet1M9A_cLc2xwd2LyE\&asrc=run_on_apify)

```
import asyncio

from apify import Actor


async def main() -> None:
    async with Actor:
        # Start the Actor task by its ID.
        actor_run = await Actor.call_task(task_id='Z3m6FPSj0GYZ25rQc')

        if actor_run is None:
            raise RuntimeError('Actor task failed to start.')

        # Wait for the task run to finish.
        run_client = Actor.apify_client.run(actor_run.id)
        await run_client.wait_for_finish()

        # Get the task run dataset items
        dataset_client = run_client.dataset()
        items = await dataset_client.list_items()
        Actor.log.info(f'Task run dataset items: {items}')


if __name__ == '__main__':
    asyncio.run(main())
```

## Actor metamorph[](#actor-metamorph)

The [`Actor.metamorph`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md#metamorph) operation transforms an Actor run into a run of another Actor with a new input. This feature is useful if you want to use another Actor to finish the work of your current Actor, instead of internally starting a new Actor run and waiting for its finish. With metamorph, you can easily create new Actors on top of existing ones, and give your users nicer input structure and user interface for the final Actor. For the users of your Actors, the metamorph operation is completely transparent; they will just see your Actor got the work done.

Internally, the system stops the container corresponding to the original Actor run and starts a new container using a different container image. All the default storages are preserved,and the new Actor input is stored under the `INPUT-METAMORPH-1` key in the same default key-value store.

To make you Actor compatible with the metamorph operation, use [`Actor.get_input`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md#get_input) instead of [`Actor.get_value('INPUT')`](https://docs.apify.com/sdk/python/sdk/python/reference/class/Actor.md#get_value) to read your Actor input. This method will fetch the input using the right key in a case of metamorphed run.

For example, imagine you have an Actor that accepts a hotel URL on input, and then internally uses the [`apify/web-scraper`](https://apify.com/apify/web-scraper) public Actor to scrape all the hotel reviews. The metamorphing code would look as follows:

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3JcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIEdldCB0aGUgb3JpZ2luYWwgQWN0b3IgaW5wdXQuXFxuICAgICAgICBhY3Rvcl9pbnB1dCA9IGF3YWl0IEFjdG9yLmdldF9pbnB1dCgpIG9yIHt9XFxuICAgICAgICBob3RlbF91cmwgPSBhY3Rvcl9pbnB1dC5nZXQoJ2hvdGVsX3VybCcpXFxuXFxuICAgICAgICAjIENyZWF0ZSBuZXcgaW5wdXQgZm9yIGFwaWZ5L3dlYi1zY3JhcGVyIEFjdG9yLlxcbiAgICAgICAgd2ViX3NjcmFwZXJfaW5wdXQgPSB7XFxuICAgICAgICAgICAgJ3N0YXJ0VXJscyc6IFt7J3VybCc6IGhvdGVsX3VybH1dLFxcbiAgICAgICAgICAgICdwYWdlRnVuY3Rpb24nOiBcXFwiXFxcIlxcXCJhc3luYyBmdW5jdGlvbiBwYWdlRnVuY3Rpb24oY29udGV4dCkge1xcbiAgICAgICAgICAgICAgICAvLyBIZXJlIHlvdSBwYXNzIHRoZSBKYXZhU2NyaXB0IHBhZ2UgZnVuY3Rpb25cXG4gICAgICAgICAgICAgICAgLy8gdGhhdCBzY3JhcGVzIGFsbCB0aGUgcmV2aWV3cyBmcm9tIHRoZSBob3RlbCdzIFVSTFxcbiAgICAgICAgICAgIH1cXFwiXFxcIlxcXCIsXFxuICAgICAgICB9XFxuXFxuICAgICAgICAjIE1ldGFtb3JwaCB0aGUgQWN0b3IgcnVuIHRvIGBhcGlmeS93ZWItc2NyYXBlcmAgd2l0aCB0aGUgbmV3IGlucHV0LlxcbiAgICAgICAgYXdhaXQgQWN0b3IubWV0YW1vcnBoKCdhcGlmeS93ZWItc2NyYXBlcicsIHdlYl9zY3JhcGVyX2lucHV0KVxcblxcbiAgICAgICAgIyBUaGlzIGNvZGUgd2lsbCBub3QgYmUgY2FsbGVkLCBzaW5jZSB0aGUgYG1ldGFtb3JwaGAgYWN0aW9uIHRlcm1pbmF0ZXNcXG4gICAgICAgICMgdGhlIGN1cnJlbnQgQWN0b3IgcnVuIGNvbnRhaW5lci5cXG4gICAgICAgIEFjdG9yLmxvZy5pbmZvKCdZb3Ugd2lsbCBub3Qgc2VlIHRoaXMhJylcXG5cXG5cXG5pZiBfX25hbWVfXyA9PSAnX19tYWluX18nOlxcbiAgICBhc3luY2lvLnJ1bihtYWluKCkpXFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.7gaZdkSgrQM-KPC6t1yEiLF1pExuMvFwZo_uVxQo2Do\&asrc=run_on_apify)

```
import asyncio

from apify import Actor


async def main() -> None:
    async with Actor:
        # Get the original Actor input.
        actor_input = await Actor.get_input() or {}
        hotel_url = actor_input.get('hotel_url')

        # Create new input for apify/web-scraper Actor.
        web_scraper_input = {
            'startUrls': [{'url': hotel_url}],
            'pageFunction': """async function pageFunction(context) {
                // Here you pass the JavaScript page function
                // that scrapes all the reviews from the hotel's URL
            }""",
        }

        # Metamorph the Actor run to `apify/web-scraper` with the new input.
        await Actor.metamorph('apify/web-scraper', web_scraper_input)

        # This code will not be called, since the `metamorph` action terminates
        # the current Actor run container.
        Actor.log.info('You will not see this!')


if __name__ == '__main__':
    asyncio.run(main())
```
