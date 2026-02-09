# Source: https://docs.datadoghq.com/error_tracking/frontend/collecting_browser_errors.md

---
title: Collecting Browser Errors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Error Tracking > Frontend Error Tracking > Collecting Browser Errors
---

# Collecting Browser Errors

## Overview{% #overview %}

Front-end errors are collected with Browser SDK. The error message and stack trace are included when available.

## Error sources{% #error-sources %}

Front-end errors come from several different sources:

- **agent**: From the SDK execution
- **console**: From `console.error()` API calls
- **custom**: Sent with the `addError` API
- **report**: From the `ReportingObserver` API
- **source**: From unhandled exceptions or unhandled promise rejections in the source code

## Error attributes{% #error-attributes %}

For information about the default attributes for all event types, see [Data Collected](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/data_collected/). For information about configuring for sampling or global context see [Modifying Data and Context](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/advanced_configuration/).

| Attribute       | Type                                                                                                                                     | Description                                                                                                                                                                                                                                                                           |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `error.source`  | string                                                                                                                                   | Where the error originates from (for example, `console`).                                                                                                                                                                                                                             |
| `error.type`    | string                                                                                                                                   | The error type (or error code in some cases).                                                                                                                                                                                                                                         |
| `error.message` | string                                                                                                                                   | A concise, human-readable, one-line message explaining the event.                                                                                                                                                                                                                     |
| `error.stack`   | string                                                                                                                                   | The stack trace or complementary information about the error.                                                                                                                                                                                                                         |
| `error.causes`  | [Array](https://github.com/DataDog/rum-events-format/blob/69147431d689b3e59bff87e15bb0088a9bb319a9/lib/esm/generated/rum.d.ts#L185-L203) | An optional list of errors providing additional context. This attribute is used to display errors separately and enhance formatting. For more information, see the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause). |

### Source errors{% #source-errors %}

Source errors include code-level information about the error. More information about the different error types can be found in [the MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error).

| Attribute    | Type   | Description                                   |
| ------------ | ------ | --------------------------------------------- |
| `error.type` | string | The error type (or error code in some cases). |

## Collect errors manually{% #collect-errors-manually %}

Monitor handled exceptions, handled promise rejections, and other errors not tracked automatically by the Browser SDK with the `addError()` API:

```javascript
addError(
    error: unknown,
    context?: Context
);
```

**Note**: [Error Tracking](https://docs.datadoghq.com/real_user_monitoring/error_tracking) processes errors that are sent with the source set to `custom`, `source`, `report` or `console`, and contain a stack trace. Errors sent with any other source (such as `network`) or sent from browser extensions are not processed by Error Tracking.

{% tab title="NPM" %}

```javascript
import { datadogRum } from '@datadog/browser-rum';

// Send a custom error with context
const error = new Error('Something wrong occurred.');

datadogRum.addError(error, {
    pageStatus: 'beta',
});

// Send a network error
fetch('<SOME_URL>').catch(function(error) {
    datadogRum.addError(error);
})

// Send a handled exception error
try {
    //Some code logic
} catch (error) {
    datadogRum.addError(error);
}
```

{% /tab %}

{% tab title="CDN async" %}

```javascript
// Send a custom error with context
const error = new Error('Something wrong occurred.');

window.DD_RUM.onReady(function() {
    window.DD_RUM.addError(error, {
        pageStatus: 'beta',
    });
});

// Send a network error
fetch('<SOME_URL>').catch(function(error) {
    window.DD_RUM.onReady(function() {
        window.DD_RUM.addError(error);
    });
})

// Send a handled exception error
try {
    //Some code logic
} catch (error) {
    window.DD_RUM.onReady(function() {
        window.DD_RUM.addError(error);
    })
}
```

{% /tab %}

{% tab title="CDN sync" %}

```javascript
// Send a custom error with context
const error = new Error('Something wrong occurred.');

window.DD_RUM && window.DD_RUM.addError(error, {
    pageStatus: 'beta',
});

// Send a network error
fetch('<SOME_URL>').catch(function(error) {
    window.DD_RUM && window.DD_RUM.addError(error);
})

// Send a handled exception error
try {
    //Some code logic
} catch (error) {
    window.DD_RUM && window.DD_RUM.addError(error);
}
```

{% /tab %}

### React error boundaries instrumentation{% #react-error-boundaries-instrumentation %}

You can instrument the React [error boundaries](https://legacy.reactjs.org/docs/error-boundaries.html) to monitor React rendering errors using the RUM Browser SDK `addError()` API.

The collected rendering errors contain a component stack, which is unminified like any other error stack traces after you [upload sourcemaps](https://docs.datadoghq.com/real_user_monitoring/guide/upload-javascript-source-maps/?tab=webpackjs#upload-your-source-maps).

To instrument React error boundaries for monitoring, use the following:

{% tab title="NPM" %}

```javascript
import { datadogRum } from '@datadog/browser-rum';

class ErrorBoundary extends React.Component {
  ...

  componentDidCatch(error, info) {
    const renderingError = new Error(error.message);
    renderingError.name = `ReactRenderingError`;
    renderingError.stack = info.componentStack;
    renderingError.cause = error;

    datadogRum.addError(renderingError);
  }

  ...
}
```

{% /tab %}

{% tab title="CDN async" %}

```javascript
class ErrorBoundary extends React.Component {
  ...

  componentDidCatch(error, info) {
    const renderingError = new Error(error.message);
    renderingError.name = `ReactRenderingError`;
    renderingError.stack = info.componentStack;
    renderingError.cause = error;

    DD_RUM.onReady(function() {
       DD_RUM.addError(renderingError);
    });
  }

  ...
}
```

{% /tab %}

{% tab title="CDN sync" %}

```javascript
class ErrorBoundary extends React.Component {
  ...

  componentDidCatch(error, info) {
    const renderingError = new Error(error.message);
    renderingError.name = `ReactRenderingError`;
    renderingError.stack = info.componentStack;
    renderingError.cause = error;

     window.DD_RUM &&
       window.DD_RUM.addError(renderingError);

  }

  ...
}
```

{% /tab %}

## Troubleshooting{% #troubleshooting %}

### Script error{% #script-error %}

For security reasons, browsers hide details from errors triggered by cross-origin scripts. When this happens, the Error Details tab shows an error with the minimal message "Script error."

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/browser/script-error.dfdff0a12b190a805c3a6e8b965ec41d.png?auto=format"
   alt="Real User Monitoring script error example" /%}

For more information about cross-origin scripts and why details are hidden, see [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) and [this Note on Global Event Handlers](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onerror#notes). Some possible reasons for this error include:

- Your JavaScript files are hosted on a different hostname (for instance, `example.com` includes assets from `static.example.com`).
- Your website includes JavaScript libraries hosted on a CDN.
- Your website includes third-party JavaScript libraries hosted on the provider's servers.

Get visibility into cross-origin scripts by following these two steps:

1. Call JavaScript libraries with [`crossorigin="anonymous"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin).

With `crossorigin="anonymous"`, the request to fetch the script is performed securely. No sensitive data is forwarded through cookies or HTTP authentication.

1. Configure the [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) HTTP response header:

   - `Access-Control-Allow-Origin: *` to allow all origins to fetch the resource.
   - `Access-Control-Allow-Origin: example.com` to specify a single allowed origin. If the server supports clients from multiple origins, it must return the origin for the specific client making the request.

## Further Reading{% #further-reading %}

- [Explore your Errors within Datadog](https://docs.datadoghq.com/error_tracking/explorer/)
- [Proactively alert on impactful issues](https://docs.datadoghq.com/error_tracking/monitors/)
- [Measure performance and user impact](https://docs.datadoghq.com/real_user_monitoring)
