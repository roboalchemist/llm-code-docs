# Source: https://docs.unifygtm.com/developers/intent-client/client-spec.md

# Intent Client Usage

> Learn how to send events using the Unify Intent Client.

<Tip>
  The Unify Intent Client can be used to log user activity across multiple subdomains of the
  same top-level domain. For example, if a user visits your marketing website at `www.yoursite.com`
  and then logs into your production web application at `app.yoursite.com`, the activity in both
  places will be attributed to the same person.
</Tip>

## Page View Events

Website page views are an indicator of buyer intent. You can log this information to the Unify platform
for usage with the `page` method.

There are two ways to collect page data with the Unify intent client:

1. Automatic monitoring of the current page
2. Manually via the client `page` method

Utilizing both of these methods when appropriate is recommended to take full advantage of intent data
within Unify.

### Automatic Page Monitoring

The Unify intent client is capable of automatically monitoring the user's current page to trigger
page events. This will happen by default when the client is installed via the [Unify Website tag](./website-tag).
If the client is installed via a package manager, you must pass the `autoPage` configuration option
when instantiating the client. See [Configuration](#configuration) below for more details.

<Check>Automatic page monitoring works in Single Page Apps, too!</Check>

In either case, this behavior can be enabled or disabled programmatically via the `startAutoPage`
and `stopAutoPage` methods on the client:

```ts  theme={null}
// Initialize the client and tell it to automatically monitor pages
const unify = new UnifyIntentClient(
  'YOUR_PUBLIC_WRITE_KEY',
  { autoPage: true },
);
unify.mount();

// Tell the client to stop monitoring pages
unify.stopAutoPage();

// Tell the client to start monitoring pages again
unify.startAutoPage();
```

### Manual Page Logging

You can also manually trigger a page event with the `page` method on the client. This is useful
when you do not want to trigger page events for every page.

```ts  theme={null}
const unify = new UnifyIntentClient('YOUR_PUBLIC_WRITE_KEY');
unify.mount();

// Trigger a page event for whatever page the user is currently on
unify.page();

// Trigger a page event for a custom page other than the current page
unify.page({ pathname: '/some-custom-page' });
```

## Identify Events

All intent data collected for users by Unify is anonymous by default. When intent events are
logged, Unify will attempt to automatically de-anonymize the IP address of a user to associate
them with a specific company, but their personal identity will remain anonymous until an
identify event is triggered for them.

There are two ways to collect identity data with the Unify intent client:

1. Automatic monitoring of email input elements
2. Manually via the client `identify` method

Utilizing both of these methods when appropriate is recommended to take full advantage of intent
data within Unify.

### Automatic Input Monitoring

The Unify intent client is capable of automatically monitoring text and email input elements on
the page to collect user identity. This will happen by default when the client is installed via
the Unify JavaScript tag. If the client is installed via a package manager, you must pass the
`autoIdentify` configuration option when instantiating the client. See [Configuration](#configuration)
below for more details.

In either case, this behavior can be enabled or disabled programmatically via the `startAutoIdentify`
and `stopAutoIdentify` methods on the client:

```ts  theme={null}
// Initialize the client and tell it to automatically monitor inputs
const unify = new UnifyIntentClient(
  'YOUR_PUBLIC_WRITE_KEY',
  { autoIdentify: true },
);
unify.mount();

// Tell the client to stop monitoring inputs for now
unify.stopAutoIdentify();

// Tell the client to start monitoring inputs again
unify.startAutoIdentify();
```

### Manual Identification

You can also manually trigger an identify event with the identify method on the client. This is
useful when users log-in with OAuth or SSO, for example, because they do not enter their email
into an input on the page.

```ts  theme={null}
const unify = new UnifyIntentClient('YOUR_PUBLIC_WRITE_KEY');
unify.mount();

// However you determine the currently logged-in user
const currentUser = getCurrentUser();

// Identify the current user
unify.identify(currentUser.emailAddress);
```

## Configuration

The following configuration options can be passed when initializing the client:

<ParamField body="autoPage" type="boolean" default={false}>
  <Note>If installed via the [Unify Website tag](./website-tag) then the `autoPage` config will default to `true`.</Note>

  Tells the client to automatically log page events whenever the current page changes.
  Works for static websites and Single Page Apps. Also logs a page event for the initial page.
</ParamField>

<ParamField body="autoIdentify" type="boolean" default={false}>
  <Note>If installed via the [Unify Website tag](./website-tag) then the `autoIdentify` config will default to `true`.</Note>

  Tells the client to automatically monitor text and email input elements on the
  page for changes. When the current user enters a valid email address into an input, the client
  will log an identify event for that email address.
</ParamField>
