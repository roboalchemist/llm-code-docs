# Source: https://momentic.ai/docs/request-mocking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Request mocking

Mocking network requests can be useful for a variety of use-cases, such as
testing your frontend without running a backend, overwriting feature flag
configurations, or testing error states.

## Mocking a route

In this example, we'll capture requests to our `/todos` endpoint, and return
fake data instead of hitting the production API server.

First, we'll create a new [mock route](./steps/mock-route) step, and set the URL
matcher to a regex that will capture requests to `GET /todos`.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/IZwgtsc3_EuhWkXP/images/network-mocking/todos.png?fit=max&auto=format&n=IZwgtsc3_EuhWkXP&q=85&s=7b2a8f2e439d4b94ccc9c0a25e4e5014" width="1130" height="522" data-path="images/network-mocking/todos.png" />
</Frame>

Then, we define a response generator to create fake data.

```javascript  theme={null}
const url = new URL(mock.request.url)

const fakeTodo = {
    id: url.searchParams.get("id"),
    name: "My todo item",
    done: false,
    description: "An item that I need to do",
}

return new Response(
    JSON.stringify([fakeTodo]),
    {
        status: 200,
        headers: {
            "content-type": "application/json"
        }
    }
)
```

## Modifying the original response from the server

Sometimes, it's easier to simply modify the original response from the server,
for example, in order to set a specific feature flag.

In order complete the initial request and pass the response to the mock
generator, you must first enable the "fetch real response" option. This will
allow us to access the response at `mock.response` inside our JavaScript code.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/wQe7tRDARWrbyaf4/images/network-mocking/fetch-real-response.png?fit=max&auto=format&n=wQe7tRDARWrbyaf4&q=85&s=b7b372e5acaec8bfe88e793a17a7e81a" width="1128" height="110" data-path="images/network-mocking/fetch-real-response.png" />
</Frame>

Now we can configure our mock to intercept feature flag requests.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/IZwgtsc3_EuhWkXP/images/network-mocking/feature-flags.png?fit=max&auto=format&n=IZwgtsc3_EuhWkXP&q=85&s=b7aecbb5c3fbeeca3bd1afd06c8c6587" width="1130" height="522" data-path="images/network-mocking/feature-flags.png" />
</Frame>

And define a response to overwrite one of the values.

```javascript  theme={null}
const originalJson = await mock.response.json()

return new Response(
  JSON.stringify({
    ...originalJson,
    flags: {
        ...originalJson.flags,
        momentic_test: true,
    }
  }),
  {
    status: mock.response.status,
    headers: mock.response.headers
  }
)
```

## Removing a mock

There are two ways to reference a mock in later steps:

1. By configuring a key in the [mock route](./steps/mock-route) step.
2. If no key is provided, a random one will be generated. You can still
   reference it later by saving the output of the step to an environment
   variable. The output of the [mock route](./steps/mock-route) step will have a
   `key` field containing the random string.

You can use a [remove route mock](./steps/remove-mock-route) step to remove a
mock by key, or remove all mocks if you omit the key.

## Updating a mock

You can update a mock by registering a different handler with the same key using
another [mock route](./steps/mock-route) step. Registering a mock with the same
URL matcher but a different key is not sufficient to replace the existing mock.

## Debugging mocked routes

Because network requests are handled asynchronously in a separate process, it
can be hard to investigate when something goes wrong.

If a response generator throws an error while handling a request, Momentic will
still respond to the request with a 500 server error status code, and the error
message in the body of the response. This makes it easy to figure out what's
going on either in your app's UI, or using the network logs.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/OPgCC7KYsAsTnGfr/images/network-mocking/network-viewer.png?fit=max&auto=format&n=OPgCC7KYsAsTnGfr&q=85&s=d8ea5fba98472deddbeb572390ca1254" width="2258" height="1010" data-path="images/network-mocking/network-viewer.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).