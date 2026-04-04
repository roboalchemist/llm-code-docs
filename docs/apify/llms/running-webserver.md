# Source: https://docs.apify.com/sdk/python/docs/concepts/running-webserver.md

# Running webserver in your Actor

Copy for LLM

Each Actor run on the Apify platform is assigned a unique hard-to-guess URL (for example `https://8segt5i81sokzm.runs.apify.net`), which enables HTTP access to an optional web server running inside the Actor run's container.

The URL is available in the following places:

* In Apify Console, on the Actor run details page as the **Container URL** field.
* In the API as the `container_url` property of the [Run object](https://docs.apify.com/api/v2#/reference/actors/run-object/get-run).
* In the Actor as the `Actor.configuration.container_url` property.

The web server running inside the container must listen at the port defined by the `Actor.configuration.container_port` property. When running Actors locally, the port defaults to `4321`, so the web server will be accessible at `http://localhost:4321`.

## Example[](#example)

The following example demonstrates how to start a simple web server in your Actor,which will respond to every GET request with the number of items that the Actor has processed so far:

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuZnJvbSBodHRwLnNlcnZlciBpbXBvcnQgQmFzZUhUVFBSZXF1ZXN0SGFuZGxlciwgVGhyZWFkaW5nSFRUUFNlcnZlclxcblxcbmZyb20gYXBpZnkgaW1wb3J0IEFjdG9yXFxuXFxucHJvY2Vzc2VkX2l0ZW1zID0gMFxcbmh0dHBfc2VydmVyID0gTm9uZVxcblxcblxcbiMgSnVzdCBhIHNpbXBsZSBoYW5kbGVyIHRoYXQgd2lsbCBwcmludCB0aGUgbnVtYmVyIG9mIHByb2Nlc3NlZCBpdGVtcyBzbyBmYXJcXG4jIG9uIGV2ZXJ5IEdFVCByZXF1ZXN0LlxcbmNsYXNzIFJlcXVlc3RIYW5kbGVyKEJhc2VIVFRQUmVxdWVzdEhhbmRsZXIpOlxcbiAgICBkZWYgZG9fZ2V0KHNlbGYpIC0-IE5vbmU6XFxuICAgICAgICBzZWxmLmxvZ19yZXF1ZXN0KClcXG4gICAgICAgIHNlbGYuc2VuZF9yZXNwb25zZSgyMDApXFxuICAgICAgICBzZWxmLmVuZF9oZWFkZXJzKClcXG4gICAgICAgIHNlbGYud2ZpbGUud3JpdGUoYnl0ZXMoZidQcm9jZXNzZWQgaXRlbXM6IHtwcm9jZXNzZWRfaXRlbXN9JywgZW5jb2Rpbmc9J3V0Zi04JykpXFxuXFxuXFxuZGVmIHJ1bl9zZXJ2ZXIoKSAtPiBOb25lOlxcbiAgICAjIFN0YXJ0IHRoZSBIVFRQIHNlcnZlciBvbiB0aGUgcHJvdmlkZWQgcG9ydCxcXG4gICAgIyBhbmQgc2F2ZSBhIHJlZmVyZW5jZSB0byB0aGUgc2VydmVyLlxcbiAgICBnbG9iYWwgaHR0cF9zZXJ2ZXJcXG4gICAgd2l0aCBUaHJlYWRpbmdIVFRQU2VydmVyKFxcbiAgICAgICAgKCcnLCBBY3Rvci5jb25maWd1cmF0aW9uLndlYl9zZXJ2ZXJfcG9ydCksIFJlcXVlc3RIYW5kbGVyXFxuICAgICkgYXMgc2VydmVyOlxcbiAgICAgICAgQWN0b3IubG9nLmluZm8oZidTZXJ2ZXIgcnVubmluZyBvbiB7QWN0b3IuY29uZmlndXJhdGlvbi53ZWJfc2VydmVyX3BvcnR9JylcXG4gICAgICAgIGh0dHBfc2VydmVyID0gc2VydmVyXFxuICAgICAgICBzZXJ2ZXIuc2VydmVfZm9yZXZlcigpXFxuXFxuXFxuYXN5bmMgZGVmIG1haW4oKSAtPiBOb25lOlxcbiAgICBnbG9iYWwgcHJvY2Vzc2VkX2l0ZW1zXFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIFN0YXJ0IHRoZSBIVFRQIHNlcnZlciBpbiBhIHNlcGFyYXRlIHRocmVhZC5cXG4gICAgICAgIHJ1bl9zZXJ2ZXJfdGFzayA9IGFzeW5jaW8uZ2V0X3J1bm5pbmdfbG9vcCgpLnJ1bl9pbl9leGVjdXRvcihOb25lLCBydW5fc2VydmVyKVxcblxcbiAgICAgICAgIyBTaW11bGF0ZSBkb2luZyBzb21lIHdvcmsuXFxuICAgICAgICBmb3IgXyBpbiByYW5nZSgxMDApOlxcbiAgICAgICAgICAgIGF3YWl0IGFzeW5jaW8uc2xlZXAoMSlcXG4gICAgICAgICAgICBwcm9jZXNzZWRfaXRlbXMgKz0gMVxcbiAgICAgICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnUHJvY2Vzc2VkIGl0ZW1zOiB7cHJvY2Vzc2VkX2l0ZW1zfScpXFxuXFxuICAgICAgICBpZiBodHRwX3NlcnZlciBpcyBOb25lOlxcbiAgICAgICAgICAgIHJhaXNlIFJ1bnRpbWVFcnJvcignSFRUUCBzZXJ2ZXIgbm90IHN0YXJ0ZWQnKVxcblxcbiAgICAgICAgIyBTaWduYWwgdGhlIEhUVFAgc2VydmVyIHRvIHNodXQgZG93biwgYW5kIHdhaXQgZm9yIGl0IHRvIGZpbmlzaC5cXG4gICAgICAgIGh0dHBfc2VydmVyLnNodXRkb3duKClcXG4gICAgICAgIGF3YWl0IHJ1bl9zZXJ2ZXJfdGFza1xcblxcblxcbmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6XFxuICAgIGFzeW5jaW8ucnVuKG1haW4oKSlcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.DruEhD2qKUMx-1nr4q3EGXW0mkJQPJKcxv-cv24Ihuo\&asrc=run_on_apify)

```
import asyncio
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from apify import Actor

processed_items = 0
http_server = None


# Just a simple handler that will print the number of processed items so far
# on every GET request.
class RequestHandler(BaseHTTPRequestHandler):
    def do_get(self) -> None:
        self.log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(f'Processed items: {processed_items}', encoding='utf-8'))


def run_server() -> None:
    # Start the HTTP server on the provided port,
    # and save a reference to the server.
    global http_server
    with ThreadingHTTPServer(
        ('', Actor.configuration.web_server_port), RequestHandler
    ) as server:
        Actor.log.info(f'Server running on {Actor.configuration.web_server_port}')
        http_server = server
        server.serve_forever()


async def main() -> None:
    global processed_items
    async with Actor:
        # Start the HTTP server in a separate thread.
        run_server_task = asyncio.get_running_loop().run_in_executor(None, run_server)

        # Simulate doing some work.
        for _ in range(100):
            await asyncio.sleep(1)
            processed_items += 1
            Actor.log.info(f'Processed items: {processed_items}')

        if http_server is None:
            raise RuntimeError('HTTP server not started')

        # Signal the HTTP server to shut down, and wait for it to finish.
        http_server.shutdown()
        await run_server_task


if __name__ == '__main__':
    asyncio.run(main())
```
