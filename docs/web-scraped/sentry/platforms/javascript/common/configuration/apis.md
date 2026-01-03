---
---
title: APIs
description: "Learn more about APIs of the SDK."
---

This page shows all available top-level APIs of the SDK. You can use these APIs as the primary way to:

- Configure the SDK after initialization
- Manually capture different types of events
- Enrich events with additional data
- ... and more!

These APIs are functions that you can use as follows - they are all available on the top-level `Sentry` object:

```javascript
Sentry.setTag("tag", "value");
```

## Available APIs

## Core APIs

  Initialize the SDK with the given options. See{" "}
  Options for the
  options you can pass to `init`.

  Returns the currently active client.

  Make the given client the current client. You do not need this if you use
  `init()`, this is only necessary if you are manually setting up a client.

  Returns the ID of the last sent error event. Note that this does not guarantee
  that this event ID exists, as it may have been dropped along the way.

"
  parameters={[
    {
      name: "timeout",
      type: "number",
      description:
        "Maximum time in ms the client should wait to flush its event queue. Omitting this parameter will cause the client to wait until all events are sent before resolving the promise.",
    },
  ]}
>
  Flushes all pending events.

  Returns true if the SDK is initialized & enabled.

"
  parameters={[
    {
      name: "timeout",
      type: "number",
      description:
        "Maximum time in ms the client should wait to flush its event queue. Omitting this parameter will cause the client to wait until all events are sent before resolving the promise.",
    },
  ]}
>
Flushes all pending events and disables the SDK. Note that this does not
remove any listeners the SDK may have set up. After a call to `close`, the current client cannot be used anymore. It's
important to only call `close` immediately before shutting down the application.

Alternatively, the [`flush`](#flush) method drains the event queue while keeping the
client enabled for continued use.

 Event | null | Promise",
    },
  ]}
>
  Adds an event processor to the SDK. An event processor receives every event
  before it is sent to Sentry. It can either mutate the event (and return it) or
  return `null` to discard the event. Event processors can also return a
  promise, but it is recommended to use this only when necessary as it slows
  down event processing.

  Event processors added via `Sentry.addEventProcessor()` will be applied to all
  events in your application. If you want to add an event processor that only
  applies to certain events, you can also add one to a scope as follows:

    
    Event processors added via `Sentry.addEventProcessor()` will be applied to all events in your current request.

If you want to add an event processor that only applies to certain events, you can also add one to a scope as follows:

  

```javascript
Sentry.withScope((scope) => {
  scope.addEventProcessor((event) => {
    // this will only be applied to events captured within this scope
    return event;
  });

  Sentry.captureException(new Error("test"));
});
```

  
    `beforeSend` and `beforeSendTransaction` are guaranteed to be run last, after all other event processors, (which means they get the final version of the event right before it's sent, hence the name). Event processors added with `addEventProcessor` are run in an undetermined order, which means changes to the event may still be made after the event processor runs.

    There can only be a single `beforeSend` / `beforeSendTransaction` processor, but you can add multiple event processors via `addEventProcessor()`.

  

Adds an integration to the SDK. This can be used to conditionally add
integrations after `Sentry.init()` has been called. Note that it is
recommended to pass integrations to `init` instead of calling this method,
where possible.

See Integrations for
more information on how to use integrations.

" categorySupported={['browser']}>
  Lazy load an integration. This expects the name to be e.g. `replayIntegration`. It will load the script from the CDN, and return a promise that resolves to the integration, which can then be added to the SDK using `addIntegration`:

```javascript
Sentry.lazyLoadIntegration("replayIntegration")
  .then((integration) => {
    Sentry.addIntegration(integration);
  })
  .catch((error) => {
    // Make sure to handle errors here!
    // This rejects e.g. if the CDN bundle cannot be loaded
  });
```

If you use a bundler, using e.g. `const { replayIntegration } = await import('@sentry/browser')` is recommended instead.

See Integrations for
more information on how to use integrations.

## Capturing Events

",
            description:
              "Additional data that should be sent with the exception.",
          },
          {
            name: "tags",
            type: "Record<string, string>",
            description:
              "Additional tags that should be sent with the exception.",
          },
          { name: "contexts", type: "Record<string, Record<string, unknown>>" },
          { name: "fingerprint", type: "string[]" },
        ],
      },
      description: "Optional additional data to attach to the Sentry event.",
    },
  ]}
>
  Capture an exception event and send it to Sentry. Note that you can pass not
  only `Error` objects, but also other objects as `exception` - in that case,
  the SDK will attempt to serialize the object for you, and the stack trace will
  be generated by the SDK and may be less accurate.

",
          description:
            "Additional data that should be sent with the exception.",
        },
        {
          name: "tags",
          type: "Record<string, string>",
          description:
            "Additional tags that should be sent with the exception.",
        },
        { name: "contexts", type: "Record<string, Record<string, unknown>>" },
        { name: "fingerprint", type: "string[]" },
      ],
    },
    description: "Optional additional data to attach to the Sentry event.",
  },
]}
>
Capture a message event and send it to Sentry. Optionally, instead of a
`CaptureContext`, you can also pass a `SeverityLevel` as second argument, e.g.
`"error"` or `"warning"`.

Messages show up as issues on your issue stream, with the message as the issue name.

## Enriching Events

Set a tag to be sent with Sentry events.

- Tag keys have a maximum length of 32 characters and can contain only letters (`a-zA-Z`), numbers (`0-9`), underscores (`_`), periods (`.`), colons (`:`), and dashes (`-`).
- Tag values have a maximum length of 200 characters and they cannot contain the newline (`\n`) character.

): void"
  parameters={[]}
>
  Set multiple tags to be sent with Sentry events.

): void"
  parameters={[]}
>
  Set a context to be sent with Sentry events. Custom contexts allow you to attach arbitrary data to an event.
  You cannot search these, but they are viewable on the issue page - if you
  need to be able to filter for certain data, use [tags](./#setTag) instead.

There are no restrictions on context name. In the context object, all keys are allowed except for `type`, which is used internally.

By default, Sentry SDKs normalize nested structured context data up to three levels deep.
Any data beyond this depth will be trimmed and marked using its type instead.
To adjust this default, use the `normalizeDepth` SDK option.

Learn more about conventions for common contexts in the [contexts interface developer documentation](https://develop.sentry.dev/sdk/data-model/event-payloads/contexts/).

 
  Context data is structured and can contain any data you want:

```javascript
Sentry.setContext("character", {
  name: "Mighty Fighter",
  age: 19,
  attack_type: "melee",
});
```

  

  Set additional data to be sent with Sentry events.

): void"
  parameters={[]}
>
  Set multiple additional data entries to be sent with Sentry events.

  Set a user to be sent with Sentry events. Set to `null` to unset the user. In
  addition to the specified properties of the `User` object, you can also add
  additional arbitrary key/value pairs.

  
    
    On the server, the IP address will be inferred from the incoming HTTP request, if available.
    This is automatically done if you have configured `sendDefaultPii: true` in your SDK configuration.
    

    
    On the browser, if the users' `ip_address` is set to `"{{ auto }}"`, Sentry
    will infer the IP address from the connection between your app and Sentrys'
    server. `{{auto}}` is automatically set if you have configured `sendDefaultPii:
    true` in your SDK configuration.
    

    To ensure your users' IP addresses are never stored in your event data, you can go to your project settings, click on "Security & Privacy", and enable "Prevent Storing of IP Addresses" or use Sentry's [server-side data scrubbing](/security-legal-pii/scrubbing/) to remove `$user.ip_address`. Adding such a rule ultimately overrules any other logic.

  

  
    
    `Sentry.setUser()` will set the user for the currently active request - see Request Isolation for more information. For example, if you want to set the user for a single request, you can do this like this:
    
    

    Or if you want to set the user for all requests, you could use a middleware like this:

    

  

",
            description:
              "Additional data that should be sent with the breadcrumb.",
          },
        ],
      },
    },
    {
      name: "hint",
      type: "Record<string, unknown>",
      description:
        "A hint object containing additional information about the breadcrumb.",
    },
  ]}
>
  You can manually add breadcrumbs whenever something interesting happens. For
  example, you might manually record a breadcrumb if the user authenticates or
  another state change occurs.

## Tracing

(options: StartSpanOptions, callback: (span: Span) => T): T"
parameters={[
  {
    name: "options",
    required: true,
    type: {
      name: 'StartSpanOptions',
      properties: [
        { name: "name", type: "string", required: true },
        { name: 'attributes', type: 'Record<string, string | number | boolean | null | undefined>', description: 'Attributes to add to the span.' },
        { name: 'startTime', type: 'number', description: 'The timestamp to use for the span start. If not provided, the current time will be used.' },
        { name: 'op', type: 'string', description: 'The operation name for the span. This is used to group spans in the UI' },
        { name: 'forceTransaction', type: 'boolean', description: 'If true, the span will be forced to be sent as a transaction, even if it is not the root span.' },
        { name: 'parentSpan', type: 'Span | null', description: 'The parent span for the new span. If not provided, the current span will be used.' },
        { name: 'onlyIfParent', type: 'boolean', description: 'If true, the span will only be created if there is an active span.' },
      ]
    },
  },
  { name: "callback", type: "(span: Span) => T", required: true },
]}>
  Starts a new span, that is active in the provided callback.
  This span will be a child of the currently active span, if there is one.

Any spans created inside of the callback will be children of this span.

The started span will automatically be ended when the callback returns, and will thus measure the duration of the callback. The callback can also be an async function.

  
  ```javascript
  // Synchronous example
 Sentry.startSpan({ name: 'my-span' }, (span) => {
    measureThis();
  });

// Asynchronous example
const status = await Sentry.startSpan({ name: 'my-span' }, async (span) => {
const status = await doSomething();
return status;
});

````

See Tracing Instrumentation for more information on how to work with spans.

(options: StartSpanOptions): Span"
  parameters={[
  {
    name: "options",
    required: true,
    type: {
      name: 'StartSpanOptions',
      properties: [
        { name: "name", type: "string", required: true },
        { name: 'attributes', type: 'Record<string, string | number | boolean | null | undefined>', description: 'Attributes to add to the span.' },
        { name: 'startTime', type: 'number', description: 'The timestamp to use for the span start. If not provided, the current time will be used.' },
        { name: 'op', type: 'string', description: 'The operation name for the span. This is used to group spans in the UI' },
        { name: 'forceTransaction', type: 'boolean', description: 'If true, the span will be forced to be sent as a transaction, even if it is not the root span.' },
        { name: 'parentSpan', type: 'Span | null', description: 'The parent span for the new span. If not provided, the current span will be used.' },
        { name: 'onlyIfParent', type: 'boolean', description: 'If true, the span will only be created if there is an active span.' },
      ]
    },
  }
]}>
  Starts a new span. This span will be a child of the currently active span, if there is one.
  The returned span has to be ended manually via `span.end()` when the span is done.

  
  ```javascript
const span = Sentry.startInactiveSpan({ name: 'my-span' });
doSomething();
span.end();
````

See Tracing Instrumentation for more information on how to work with spans.

(options: StartSpanOptions, callback: (span: Span) => T): T"
 parameters={[
  {
    name: "options",
    required: true,
    type: {
      name: 'StartSpanOptions',
      properties: [
        { name: "name", type: "string", required: true },
        { name: 'attributes', type: 'Record<string, string | number | boolean | null | undefined>', description: 'Attributes to add to the span.' },
        { name: 'startTime', type: 'number', description: 'The timestamp to use for the span start. If not provided, the current time will be used.' },
        { name: 'op', type: 'string', description: 'The operation name for the span. This is used to group spans in the UI' },
        { name: 'forceTransaction', type: 'boolean', description: 'If true, the span will be forced to be sent as a transaction, even if it is not the root span.' },
        { name: 'parentSpan', type: 'Span | null', description: 'The parent span for the new span. If not provided, the current span will be used.' },
        { name: 'onlyIfParent', type: 'boolean', description: 'If true, the span will only be created if there is an active span.' },
      ]
    },
  },
  { name: "callback", type: "(span: Span) => T", required: true },
]}>
  Starts a new span, that is active in the provided callback.
  This span will be a child of the currently active span, if there is one.

Any spans created inside of the callback will be children of this span.

The started span will _not_ automatically end - you have to call `span.end()` when the span is done. Please note that the span will still only be the parent span of spans created inside of the callback, while the callback is active. In most cases, you will want to use `startSpan` or `startInactiveSpan` instead.

  
  ```javascript
const status = await Sentry.startSpanManual({ name: 'my-span' }, async (span) => {
const status = await doSomething();
span.end();
return status;
});
```

See Tracing Instrumentation for more information on how to work with spans.

  Sets the passed span as the active span on the current scope.
  You most likely don't need this functionality and should [use `startSpan`](#startSpan) 
  instead.
  However, in some situations, you might prefer a span being active outside of a callback. 
  In this case, the combination of [`startInactiveSpan`](#startInactiveSpan) with this function
  allows you to start a span, hold a reference to it and keep it active until you end it, without
  the active duration being bound to the callback (as opposed to [`startSpanManual`](#startSpanManual)).
  
  
  
  ```javascript
  let checkoutSpan;
  
  on('startCheckout', () => {
    checkoutSpan = Sentry.startInactiveSpan({name: 'checkout-flow'});
    Sentry.setActiveSpanInBrowser(checkoutSpan);
  })
  
  doSomeWork();
  
  on('endCheckout', () => {
    // Ending the span automatically removes it as the active span on the scope
    checkoutSpan.end();
  })
  ```

See Tracing Instrumentation for more information on how to work with spans.

(options: TraceOptions, callback: () => T): T"
  parameters={[
    {
      name: "options",
      type: {
        name: "TraceOptions",
        properties: [
          {
            name: "sentryTrace",
            type: "string",
            description: "The sentry-trace header.",
          },
          {
            name: "baggage",
            type: "string",
            description: "The baggage header.",
          },
        ],
      },
    },
    {
      name: "callback",
      type: "() => T",
      description: "The callback to continue the trace.",
    },
  ]}
>
  Continues a trace in the provided callback. Any spans created inside of the
  callback will be linked to the trace.

(callback: () => T): T"
>
  Ensure that all spans created inside of the provided callback are not sent to
  Sentry.

(callback: () => T): T"
>
  Start a new trace that is active in the provided callback.

  Start an pageload span that will be automatically ended when the page is
  considered idle. If a pageload/navigation span is currently ongoing, it will
  automatically be ended first. In most cases, you do not need to call this, as
  the `browserTracingIntegration` will automatically do that for you. However,
  if you opt-out of pageload spans, you can use this method to manually start
  such a span. Please note that this function will do nothing if
  `browserTracingIntegration` has not been enabled.

  Start an navigation span that will be automatically ended when the page is
  considered idle. If a pageload/navigation span is currently ongoing, it will
  automatically be ended first. In most cases, you do not need to call this, as
  the `browserTracingIntegration` will automatically do that for you. However,
  if you opt-out of navigation spans, you can use this method to manually start
  such a span. Please note that this function will do nothing if
  `browserTracingIntegration` has not been enabled.

  Signals to the Sentry SDK that the initial page was fully loaded.
  Requires the `enableReportPageLoaded` option in `browserTracingIntegration` to
  be set to `true`. Once called, the SDK ends the pageload span automatically,

  By default, the SDK takes care of ending the pageload span automatically, based on
  a period of inactivity where no new child spans are added to the pageload trace.
  You can alternatively use explicit pageload reporting if the inactivity heuristics of
  `browserTracingIntegration` don't work well for your use case.
  However, you must ensure that you call `reportPageLoaded` in every situation.
  If `reportPageLoaded` is not called, the pageload span will be ended after 30 seconds
  or whatever custom value is set on the `finalTimeout` option.

  
  ```javascript
  Sentry.init({
    // 1. Enable manual page load reporting:
    integrations: [browserTracingIntegration({ enableReportPageLoaded: true })]
  })

  // 2. Whenever you consider the page loaded:
  Sentry.reportPageLoaded();
  ```
  

## Tracing Utilities

These utilities can be used for more advanced tracing use cases.

  Convert a span to a JSON object.

  Update the name of a span. Use this over `span.updateName(name)` to ensure
  that the span is updated in all backends.

  Set the status of a span based on the given http status code.

  Get the currently active span.

  Get the root span of a span.

(span: Span | null, callback: () => T): T"
>
  Runs the provided callback with the given span as the active span. If `null`
  is provided, the callback will have no active span.

## Sessions

Sessions allow you to track the release health of your application.
See the Releases & Health page for more information.

  Starts a new session.

  Ends the current session (but does not send it to Sentry).

  Sends the current session on the scope to Sentry. Pass `true` as argument to
  end the session first.

## Scopes

See Scopes for more information on how to use scopes,
as well as for an explanation of the different types of scopes (current scope, isolation scope, and global scope).

 void): void"
>
  Forks the current scope and calls the callback with the forked scope.

 void): void"
>
  Forks the current isolation scope and calls the callback with the forked
  scope.

  Returns the current scope.

Note that in most cases you should not use this API, but instead use `withScope` to generate and access a local scope. There are no guarantees about the consistency of `getCurrentScope` across different parts of your application, as scope forking may happen under the hood at various points.

  Returns the current{" "}
  
    isolation scope
  
  .

  Returns the{" "}
  
    global scope
  
  .

## User Feedback

" },
        ],
      },
      description: "The feedback to capture.",
    },
    {
      name: "hint",
      type: {
        name: "Hint",
        properties: [
          {
            name: "captureContext",
            type: {
              name: "CaptureContext",
              properties: [
                {
                  name: "user",
                  type: {
                    name: "User",
                    properties: [
                      { name: "id", type: "string | number" },
                      { name: "email", type: "string" },
                      { name: "ip_address", type: "string" },
                      { name: "username", type: "string" },
                    ],
                  },
                },
                {
                  name: "level",
                  type: '"fatal" | "error" | "warning" | "log" | "info" | "debug"',
                },
                {
                  name: "extra",
                  type: "Record<string, unknown>",
                  description:
                    "Additional data that should be sent with the exception.",
                },
                {
                  name: "tags",
                  type: "Record<string, string>",
                  description:
                    "Additional tags that should be sent with the exception.",
                },
                {
                  name: "contexts",
                  type: "Record<string, Record<string, unknown>>",
                },
                { name: "fingerprint", type: "string[]" },
              ],
            },
            description:
              "Optional additional data to attach to the Sentry event.",
          },
        ],
      },
      description:
        "Optional hint object containing additional information about the feedback.",
    },
  ]}
>
  Send user feedback to Sentry.

 | undefined"
>
  Get the feedback integration, if it has been added. This can be used to access
  the feedback integration in a type-safe way.

"
  parameters={[
    {
      name: "feedback",
      type: {
        name: "Feedback",
        properties: [
          { name: "message", type: "string", required: true },
          { name: "name", type: "string" },
          { name: "email", type: "string" },
          { name: "url", type: "string" },
          { name: "source", type: "string" },
          {
            name: "associatedEventId",
            type: "string",
            description: "The event id that this feedback is associated with.",
          },
          { name: "tags", type: "Record<string, string>" },
        ],
      },
      description: "The feedback to capture.",
    },
    {
      name: "hint",
      type: {
        name: "Hint",
        properties: [
          {
            name: "captureContext",
            type: {
              name: "CaptureContext",
              properties: [
                {
                  name: "user",
                  type: {
                    name: "User",
                    properties: [
                      { name: "id", type: "string | number" },
                      { name: "email", type: "string" },
                      { name: "ip_address", type: "string" },
                      { name: "username", type: "string" },
                    ],
                  },
                },
                {
                  name: "level",
                  type: '"fatal" | "error" | "warning" | "log" | "info" | "debug"',
                },
                {
                  name: "extra",
                  type: "Record<string, unknown>",
                  description:
                    "Additional data that should be sent with the exception.",
                },
                {
                  name: "tags",
                  type: "Record<string, string>",
                  description:
                    "Additional tags that should be sent with the exception.",
                },
                {
                  name: "contexts",
                  type: "Record<string, Record<string, unknown>>",
                },
                { name: "fingerprint", type: "string[]" },
              ],
            },
            description:
              "Optional additional data to attach to the Sentry event.",
          },
        ],
      },
      description:
        "Optional hint object containing additional information about the feedback.",
    },
  ]}
>
  This method is similar to [`captureFeedback`](#capturefeedback), but it
  returns a promise that resolves only when the feedback was successfully sent
  to Sentry. It will reject if the feedback cannot be sent.

## Cron Monitoring

  Create a cron monitor check in and send it to Sentry.

 any,
monitorConfig?: MonitorConfig
): string`}
categorySupported={['server']}
parameters={[
{
  name: "monitorSlug",
  type: 'string',
  required: true,
},
 {
  name: "callback",
  type: '() => any',
  required: true,
},
{
  name: "monitorConfig",
  type: {
    name: "MonitorConfig",
    properties: [
      {
        name: "schedule",
        type: '{ type: "crontab", value: string } | { type: "interval", value: number, unit: "year" | "month" | "day" | "hour" | "minute" }',
        required: true,
      },
      { name: "checkinMargin", type: "number" },
      { name: "maxRuntime", type: "number" },
      { name: "timezone", type: "string" },
      { name: "failureIssueThreshold", type: "number" },
      { name: "recoveryThreshold", type: "number" },
    ],
  },
},
]}
>
Wraps a callback with a cron monitor check in. The check in will be sent to Sentry when the callback finishes.

## Instrumenting Load Functions

SvelteKit's universal and server `load` functions are instrumented automatically by default. If you don't want to use `load` auto-instrumentation, you can [disable it](/platforms/javascript/guides/sveltekit/configuration/build/#auto-instrumentation-options) and manually instrument specific `load` functions using the following function wrappers:

 any>(
  originalLoad: T
  ): T`}
>
Wraps a SvelteKit `load` function declared in `+page.(js|ts)` or `+layout.(js|ts)` with Sentry error and performance monitoring.

```javascript
export const load = wrapLoadWithSentry(({ fetch }) => {
    const res = await fetch("/api/data");
    const data = await res.json();
    return { data };
});
```

 any>(
  originalServerLoad: T
  ): T`}
>
Wraps a SvelteKit server-only `load` function declared in`+page.server.(js|ts)` or `+layout.server.(js|ts)` with Sentry error and performance monitoring.

```javascript
export const load = wrapServerLoadWithSentry(({ fetch }) => {
  const res = await fetch("/api/data");
  const data = await res.json();
  return { data };
});
```

## Instrumenting Server Routes 

(
  originalRouteHandler: (request: T) => Promise
  ): (requestEvent: T) => Promise`}
>
Wraps a SvelteKit [server route handler](https://kit.svelte.dev/docs/routing#server) registered in `+server.(js|ts)` with Sentry error and performance monitoring. This is useful if you have custom server routes that you want to trace or if you want to capture `error()` calls within your server routes.

```javascript
export const GET = wrapServerRouteWithSentry(async () => {
  // your endpoint logic
  return new Response("Hello World");
});
```

## Server Actions

>`}
>
  To instrument Next.js Server Actions, wrap their content in `withServerActionInstrumentation`, along with a name to describe your server action.
  You can optionally pass form data and headers to record them, and configure the wrapper to record the Server Action responses.

  
    ```tsx
    import * as Sentry from "@sentry/nextjs";
    import { headers } from "next/headers";

    export default function ServerComponent() {
        async function myServerAction(formData: FormData) {
            "use server";
            return await Sentry.withServerActionInstrumentation(
            "myServerAction", // The name you want to associate this Server Action with in Sentry
            {
                formData, // Optionally pass in the form data
                headers: await headers(), // Optionally pass in headers
                recordResponse: true, // Optionally record the server action response
            },
            async () => {
                // ... Your Server Action code

                return { name: "John Doe" };
            }
            );
        }

        return (
            <form action={myServerAction}>
            <input type="text" name="some-input-value" />
            <button type="submit">Run Action</button>
            </form>
        );
    }
    ```

  

## Route and Data Fetching Instrumentation

  Instrument the provided API route handler with Sentry for error and
  performance monitoring. This function wraps the handler exported from the
  user's API page route file (which may or may not already be wrapped with
  `withSentry`).

  Instrument a `getInitialProps` function with Sentry error and performance
  monitoring by creating and returning a wrapped version of the function.

  Instrument a `getServerSideProps` function with Sentry error and performance
  monitoring by creating and returning a wrapped version of the function.

,
  _parameterizedRoute: string
  ): GetStaticProps`}
>
  Instrument a `getStaticProps` function with Sentry error and performance
  monitoring by creating and returning a wrapped version of the function.

  Instrument a `getInitialProps` function in a custom error page (`_error.js`)
  with Sentry error and performance monitoring by creating and returning a
  wrapped version of the function.

  Instrument a `getInitialProps` function in a custom app (`_app.js`) with
  Sentry error and performance monitoring by creating and returning a wrapped
  version of the function.

  Instrument a `getInitialProps` function in a custom document (`_document.js`)
  with Sentry error and performance monitoring by creating and returning a
  wrapped version of the function.

