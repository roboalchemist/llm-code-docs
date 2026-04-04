# Source: https://docs.zapier.com/platform/build-cli/core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Core reference

> Reference for `zapier-platform-core`

Most functions get called with `(z, bundle)`. This document is a reference for how to use these objects.

> If you use TypeScript, you can import `ZObject`, `Bundle<InputFields>` and `PerformFunction<InputFields>` from `zapier-platform-core`.

## `z` Object

We provide several methods off of the `z` object, which is provided as the first argument to all function calls in your integration.

> The `z` object is passed into your functions as the first argument - IE: `perform: (z) => {}`.

### `z.request([url], options)`

`z.request([url], options)` is a promise based HTTP client with some Zapier-specific goodies. See [Making HTTP Requests](/platform/build-cli/overview#making-http-requests). `z.request()` will [percent-encode](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding) non-ascii characters and these reserved characters: ``:$/?#[]@$&+,;=^@`\``. Use [`skipEncodingChars`](https://github.com/zapier/zapier-platform/blob/main/packages/schema/docs/build/schema.md#requestschema) to modify this behaviour.

### `z.console`

`z.console.log(message)` is a logging console, similar to Node.js `console` but logs remotely, as well as to stdout in tests. See [Log Statements](/platform/build-cli/overview#console-logging)

### `z.dehydrate(func, inputData)`

`z.dehydrate(func, inputData)` is used to lazily evaluate a function, perfect to avoid API calls during polling or for reuse. See [Dehydration](/platform/build-cli/overview#dehydration).

### `z.dehydrateFile(func, inputData)`

`z.dehydrateFile` is used to lazily download a file, perfect to avoid API calls during polling or for reuse. See [File Dehydration](/platform/build-cli/overview#file-dehydration).

### `z.stashFile(bufferStringStream, [knownLength], [filename], [contentType])`

`z.stashFile(bufferStringStream, [knownLength], [filename], [contentType])` is a promise based file stasher that returns a URL file pointer. See [Stashing Files](/platform/build-cli/overview#stashing-files).

### `z.JSON`

`z.JSON` is similar to the JSON built-in like `z.JSON.parse('...')`, but catches errors and produces nicer tracebacks.

### `z.hash()`

`z.hash()` is a crypto tool for doing things like `z.hash('sha256', 'my password')`

### `z.errors`

`z.errors` is a collection error classes that you can throw in your code, like `throw new z.errors.HaltedError('...')`.

The available errors are:

* `Error` (*added in v9.3.0*) - Stops the current operation, allowing for (auto) replay. Read more on [General Errors](/platform/build-cli/overview#general-errors)

* `HaltedError` - Stops current operation, but will never turn off Zap. Read more on [Halting Execution](/platform/build-cli/overview#halting-execution)

* `ExpiredAuthError` - Stops the current operation and emails user to manually reconnect. Read more on [Stale Authentication Credentials](/platform/build-cli/overview#stale-authentication-credentials)

* `RefreshAuthError` - (OAuth2 or Session Auth) Tells Zapier to refresh credentials and retry operation. Read more on [Stale Authentication Credentials](/platform/build-cli/overview#stale-authentication-credentials)

* `ThrottledError` (*new in v11.2.0*) - Tells Zapier to retry the current operation after a delay specified in seconds. Read more on [Handling Throttled Requests](/platform/build-cli/overview#handling-throttled-requests)

For more details on error handling in general, see [here](/platform/build-cli/overview#error-handling).

### `z.cursor`

The `z.cursor` object exposes two methods:

* `z.cursor.get(): Promise<string|null>`

* `z.cursor.set(string): Promise<null>`

Any data you `set` will be available to that Zap for about an hour (or until it's overwritten). For more information, see: [paging](/platform/build-cli/overview#paging).

### `z.generateCallbackUrl()`

The `z.generateCallbackUrl()` will return a callback URL your app can `POST` to later for handling long running tasks (like transcription or encoding jobs). In the meantime, the Zap and Task will wait for your response and the user will see the Task marked as waiting.

For example, in your `perform` you might do:

```js  theme={null}
const perform = async (z, bundle) => {
  // something like this url:
  // https://zapier.com/hooks/callback/123/abcdef01-2345-6789-abcd-ef0123456789/abcdef0123456789abcdef0123456789abcdef01/
  // consider checking bundle.meta.isLoadingSample to determine if this is a test run or real run!
  const callbackUrl = z.generateCallbackUrl();
  await z.request({
    url: "https://example.com/api/slow-job",
    method: "POST",
    body: {
      // ... whatever your integration needs
      url: callbackUrl,
    },
  });
  return { hello: "world" }; // available later in bundle.outputData
};
```

And in your own `/api/slow-job` view (or more likely, an async job) you'd make this request to Zapier when the long-running job completes to populate `bundle.cleanedRequest`:

```http  theme={null}
POST /hooks/callback/123/abcdef01-2345-6789-abcd-ef0123456789/abcdef0123456789abcdef0123456789abcdef01/ HTTP/1.1
Host: zapier.com
Content-Type: application/json

{"foo":"bar"}
```

> Callbacks are fully supported during sample testing in the Zap Editor, including `performResume` execution. However, when possible, it's preferable to avoid using callbacks during sampling (check `bundle.meta.isLoadingSample`) for a better testing experience.

By default the payload `POST`ed to the callback URL will augment the data returned from the initial `perform` to compose the final value.

If you need to customize what the final value should be you can define a `performResume` method that receives three bundle properties:

* `bundle.outputData` is `{"hello": "world"}`, the data returned from the initial `perform`

* `bundle.cleanedRequest` is `{"foo": "bar"}`, the payload from the callback URL

* `bundle.rawRequest` is the full request object corresponding to `bundle.cleanedRequest`

```js  theme={null}
const performResume = async (z, bundle) => {
  // this will give a final value of: {"hello": "world", "foo": "bar"}
  // which is the default behavior when a custom `performResume` is not
  // defined.
  return { ...bundle.outputData, ...bundle.cleanedRequest };
};
```

> The app will have a maximum of 30 days to `POST` to the callback URL. If a user deletes or modifies the Zap or Task in the meantime, we will not resume the task.

Some considerations:

* `performResume` is not supported by the Platform UI at the moment. It can only be used by integrations built with the CLI.

* In a search-or-write step, if the search part fails and proceeds to the write part, the callback URL generated for the write step might not be recognized or waited for. This can result in the `performResume` operation not being executed, leading to issues in the task flow.

* When migrating actions that use `performResume`, it is important to ensure that the `performResume` code for the new API is backward compatible. This ensures that if a migration occurs while a run is waiting for a callback, it will succeed after being migrated

## `bundle` Object

This object holds the user's auth details and the data for the API requests.

> The `bundle` object is passed into your functions as the second argument - IE: `perform: (z, bundle) => {}`.

### `bundle.authData`

`bundle.authData` is user-provided authentication data, like `api_key` or `access_token`. [Read more on authentication.](/platform/build-cli/overview#authentication)

### `bundle.inputData`

`bundle.inputData` is user-provided data for this particular run of the trigger/search/create, as defined by the [`inputFields`](/platform/build-cli/input-fields). For example:

```js  theme={null}
{
  createdBy: 'his name is Bobby Flay',
  style: 'he cooks mediterranean',
  scheduledAt: "2021-09-09T09:00:00-07:00"
}
```

### `bundle.inputDataRaw`

`bundle.inputDataRaw` is like `bundle.inputData`, but before processing such as interpreting friendly datetimes and rendering `{{curlies}}`:

```js  theme={null}
{
  createdBy: 'his name is {{123__chef_name}}',
  style: 'he cooks {{456__style}}',
  scheduledAt: "today"
}
```

> "curlies" represent data mapped in from previous steps. They take the form `{{NODE_ID__key_name}}`.

You'll usually want to use `bundle.inputData` instead.

### `bundle.meta`

`bundle.meta` contains extra information useful for doing advanced behaviors depending on what the user is doing. It has the following options:

| key                        | default     | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isLoadingSample`          | `false`     | If true, this run was initiated manually via the Zap Editor                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `isFillingDynamicDropdown` | `false`     | If true, this poll is being used to populate a dynamic dropdown. You only need to return the fields you specified (such as `id` and `name`), though returning everything is fine too                                                                                                                                                                                                                                                                                                                  |
| `isPopulatingDedupe`       | `false`     | If true, the results of this poll will be used to initialize the deduplication list rather than trigger a zap. You should grab as many items as possible. See also: [deduplication](/platform/build/deduplication)                                                                                                                                                                                                                                                                                    |
| `limit`                    | `-1`        | The number of items you should fetch. `-1` indicates there's no limit. Build this into your calls insofar as you are able                                                                                                                                                                                                                                                                                                                                                                             |
| `page`                     | `0`         | Used in [paging](/platform/build-cli/faqs#whats-the-deal-with-pagination-when-is-it-used-and-how-does-it-work) to uniquely identify which page of results should be returned                                                                                                                                                                                                                                                                                                                          |
| `timezone`                 | `null`      | The timezone the user has configured for their account or specfic automation. Received as [TZ identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), such as "America/New\_York".                                                                                                                                                                                                                                                                                                 |
| `isTestingAuth`            | `false`     | (legacy property) If true, the poll was triggered by a user testing their account (via [clicking "test"](https://cdn.zapier.com/storage/photos/5c94c304ce11b02c073a973466a7b846.png) or during setup). We use this data to populate the auth label, but it's mostly used to verify we made a successful authenticated request                                                                                                                                                                         |
| `withSearch`               | `undefined` | When a create is called as part of a search-or-create step, `withSearch` will be the key of the search.                                                                                                                                                                                                                                                                                                                                                                                               |
| `inputFields`              | `{}`        | Contains extra input field context if one or more input fields define this data via their respective `meta` property. If defined, then this object's keys are the respective input field `key` values, and the values for each `key` are an object corresponding to that input field's `meta` object value. See the [FieldSchema reference](https://github.com/zapier/zapier-platform/blob/main/packages/schema/docs/build/schema.md#fieldschema) for more details on how to define input field meta. |

> Before v8.0.0, the information in `bundle.meta` was different. See [the old docs](https://github.com/zapier/zapier-platform-cli/blob/a058e6d538a75d215d2e0c52b9f49a97218640c4/README.md#bundlemeta) for the previous values and [the wiki](https://github.com/zapier/zapier-platform/wiki/bundle.meta-changes) for a mapping of old values to new.

Here's an example of a polling trigger that is also used to power a dynamic dropdown:

```js  theme={null}
const perform = async (z, bundle) => {
  const params = { per_page: 100 }; // poll for the most recent 100 teams

  if (bundle.meta.isFillingDynamicDropdown) {
    // dynamic dropdowns support pagination
    params.per_page = 30;
    params.offset = params.per_page * bundle.meta.page;
  }

  const response = await z.request({
    url: `${API_BASE_URL}/teams`,
    params,
  });

  return response.json;
};
// ...
```

### `bundle.rawRequest`

> `bundle.rawRequest` is only available in the `perform` for webhooks, `getAccessToken` for OAuth authentication methods, and `performResume` in a callback action.

`bundle.rawRequest` holds raw information about the HTTP request that triggered the `perform` method or that represents the user's browser request that triggered the `getAccessToken` call:

```
{
  method: 'POST',
  querystring: 'foo=bar&baz=qux',
  headers: {
    'Content-Type': 'application/json'
  },
  content: '{"hello": "world"}'
}
```

In `bundle.rawRequest`, headers other than `Content-Length` and `Content-Type` will be prefixed with `Http-`, and all headers will be named in Camel-Case. For example, the header `X-Time-GMT` would become `Http-X-Time-Gmt`.

### `bundle.cleanedRequest`

> `bundle.cleanedRequest` is only available in the `perform` for webhooks, `getAccessToken` for OAuth authentication methods, and `performResume` in a callback action.

`bundle.cleanedRequest` will return a formatted and parsed version of the request. Some or all of the following will be available:

```
{
  method: 'POST',
  querystring: {
    foo: 'bar',
    baz: 'qux'
  },
  headers: {
    'Content-Type': 'application/json'
  },
  content: {
    hello: 'world'
  }
}
```

### `bundle.outputData`

> `bundle.outputData` is only available in the `performResume` in a callback action.

`bundle.outputData` will return a whatever data you originally returned in the `perform`, allowing you to mix that with `bundle.rawRequest` or `bundle.cleanedRequest`.

### `bundle.targetUrl`

> `bundle.targetUrl` is only available in the `performSubscribe` and `performUnsubscribe` methods for webhooks.

This the URL to which you should send hook data. It'll look something like [`https://hooks.zapier.com/1234/abcd`.](https://hooks.zapier.com/1234/abcd.) We provide it so you can make a POST request to your server. Your server should store this URL and use is as a destination when there's new data to report.

For example:

```js  theme={null}
const subscribeHook = async (z, bundle) => {
  const options = {
    url: "https://57b20fb546b57d1100a3c405.mockapi.io/api/hooks",
    method: "POST",
    body: {
      url: bundle.targetUrl, // bundle.targetUrl has the Hook URL this app should call
    },
  };

  const response = await z.request(options);
  return response.data; // or response.json if you're using core v9 or older
};

module.exports = {
  // ...
  performSubscribe: subscribeHook,
  // ...
};
```

Read more in the [REST hook example](https://github.com/zapier/zapier-platform/blob/main/example-apps/rest-hooks/triggers/recipe.js).

### `bundle.subscribeData`

> `bundle.subscribeData` is available in the `perform` and `performUnsubscribe` method for webhooks.

This is an object that contains the data you returned from the `performSubscribe` function. It should contain whatever information you need send a `DELETE` request to your server to stop sending webhooks to Zapier.

Read more in the [REST hook example](https://github.com/zapier/zapier-platform/blob/main/example-apps/rest-hooks/triggers/recipe.js).

## `bufferedBundle` Object

*Added in v15.15.0.*

This object holds a user's auth details (`bufferedBundle.authData`) and the buffered data (`bufferedBundle.buffer`) for the API requests. It is used only with a `create` action's `performBuffer` function.

> The `bufferedBundle` object is passed into the `performBuffer` function as the second argument - IE: `performBuffer: async (z, bufferedBundle) => {}`.

### `bufferedBundle.authData`

It is a user-provided authentication data, like `api_key` or `access_token`. [Read more on authentication.](/platform/build-cli/overview#authentication)

### `bufferedBundle.groupedBy`

It is a user-provided data for a set of selected [`inputFields`](/platform/build-cli/input-fields) to group the multiple runs of a `create` action by.

### `bufferedBundle.buffer`

It is an array of objects of user-provided data and some meta data to allow multiple runs of a `create` action be processed in a single API request.

#### `bufferedBundle.buffer[].inputData`

It is a user-provided data for a particular run of a `create` action in the buffer, as defined by the [`inputFields`](/platform/build-cli/input-fields).

#### `bufferedBundle.buffer[].meta`

It contains an idempotency `id` provided to the `create` action to identify each run's data in the buffered data.
