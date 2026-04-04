# Source: https://docs.datadoghq.com/error_tracking/frontend/browser.md

---
title: Browser Error Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Error Tracking > Frontend Error Tracking > Browser Error Tracking
---

# Browser Error Tracking

## Overview{% #overview %}

[Error Tracking](https://docs.datadoghq.com/error_tracking/) processes errors collected from the browser by the Browser SDK. Whenever a [source](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/data_collected/?tab=error#source-errors), [custom](https://docs.datadoghq.com/error_tracking/frontend/collecting_browser_errors/), [report](https://docs.datadoghq.com/error_tracking/frontend/collecting_browser_errors/?tab=npm#error-sources), or [console](https://docs.datadoghq.com/error_tracking/frontend/collecting_browser_errors/?tab=npm#error-sources) error containing a stack trace is collected, Error Tracking processes and groups it under an issue, or group of similar errors to be found in the [Error Tracking Explorer](https://docs.datadoghq.com/error_tracking/explorer).

## Prerequisites{% #prerequisites %}

Download the latest version of the [Browser SDK](https://www.npmjs.com/package/@datadog/browser-rum).

## Setup{% #setup %}

To start sending Error Tracking data from your browser application to Datadog, follow the [in-app setup instructions](https://app.datadoghq.com/error-tracking/settings/setup/client) or follow the steps below.

### Step 1 - Create the application{% #step-1---create-the-application %}

1. In Datadog, navigate to the [**Errors > Settings > Browser and Mobile > Add an Application**](https://app.datadoghq.com/error-tracking/settings/setup/client) page and select the JavaScript (JS) application type.
1. Enter a name for your application, then click **Create Application**. This generates a `clientToken` and an `applicationId` for your application.

### Step 2 - Choose the right installation method{% #step-2---choose-the-right-installation-method %}

Choose the installation type for the Browser SDK.

{% tab title="npm" %}
Installing through npm (Node Package Manager) is recommended for modern web applications. The Browser SDK is packaged with the rest of your frontend JavaScript code. It has no impact on page load performance. However, the SDK may miss errors, resources, and user actions triggered before the SDK is initialized. Datadog recommends using a matching version with the Browser Logs SDK.

Add [`@datadog/browser-rum`](https://www.npmjs.com/package/@datadog/browser-rum) to your `package.json` file, then initialize it with:

```javascript
import { datadogRum } from '@datadog/browser-rum';

datadogRum.init({

   applicationId: '<APP_ID>',
   clientToken: '<CLIENT_TOKEN>',
   service: '<SERVICE>',
   env: '<ENV_NAME>',
   // site: '<SITE>',
   // version: '1.0.0',
   trackUserInteractions: true,
   trackResources: true
});
```

The `trackUserInteractions` parameter enables the automatic collection of user clicks in your application. **Sensitive and private data** contained in your pages may be included to identify the elements interacted with.
{% /tab %}

{% tab title="CDN async" %}
Installing through CDN async is recommended for web applications with performance targets. The Browser SDK loads from Datadog's CDN asynchronously, ensuring the SDK download does not impact page load performance. However, the SDK may miss errors, resources, and user actions triggered before the SDK is initialized.

Add the generated code snippet to the head tag of every HTML page you want to monitor in your application. For the **** [site](https://docs.datadoghq.com/getting_started/site/):

```javascript
<script>
  (function(h,o,u,n,d) {
    h=h[d]=h[d]||{q:[],onReady:function(c){h.q.push(c)}}
    d=o.createElement(u);d.async=1;d.src=n
    n=o.getElementsByTagName(u)[0];n.parentNode.insertBefore(d,n)
  })(window,document,'script','https://www.datadoghq-browser-agent.com/us1/v6/datadog-rum.js','DD_RUM')
  window.DD_RUM.onReady(function() {
    window.DD_RUM.init({
      clientToken: '<CLIENT_TOKEN>',
      applicationId: '<APP_ID>',
      // site: '<SITE>',
      service: '<APP_ID>',
      env: '<ENV_NAME>',
      // version: '1.0.0'
    });
  })
</script>
```

The `trackUserInteractions` parameter enables the automatic collection of user clicks in your application. **Sensitive and private data** contained in your pages may be included to identify the elements interacted with.
{% /tab %}

{% tab title="CDN sync" %}
Installing through CDN sync is recommended for collecting all events. The Browser SDK loads from Datadog's CDN synchronously, ensuring the SDK loads first and collects all errors, resources, and user actions. This method may impact page load performance.

Add the generated code snippet to the head tag (in front of any other script tags) of every HTML page you want to monitor in your application. Placing the script tag higher and loading it synchronously ensures Datadog RUM can collect all performance data and errors. For the **** [site](https://docs.datadoghq.com/getting_started/site/):

```javascript
<script
    src="https://www.datadoghq-browser-agent.com/us1/v6/datadog-rum.js"
    type="text/javascript">
</script>
<script>
    window.DD_RUM && window.DD_RUM.init({
      clientToken: '<CLIENT_TOKEN>',
      applicationId: '<APP_ID>',
      // site: '<SITE>',
      service: '<APP_ID>',
      env: '<ENV_NAME>',
      // version: '1.0.0'
    });
</script>
```

The `trackUserInteractions` parameter enables the automatic collection of user clicks in your application. **Sensitive and private data** contained in your pages may be included to identify the elements interacted with.
{% /tab %}

#### TypeScript (optional){% #typescript-optional %}

If you are initializing the SDK in a TypeScript project, use the code snippet below. Types are compatible with TypeScript >= 3.8.2.

{% alert level="info" %}
For earlier versions of TypeScript, import JavaScript sources and use global variables to avoid any compilation issues.
{% /alert %}

```javascript
import '@datadog/browser-rum/bundle/datadog-rum'

window.DD_RUM.init({
  applicationId: 'XXX',
  clientToken: 'XXX',
  site: 'datadoghq.com',
  trackUserInteractions: true,
  trackResources: true,
  ...
})
```

### Step 3 - Configure environment and settings{% #step-3---configure-environment-and-settings %}

1. In the Environment field, define the environment (`env`) for your application to use [unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/).
1. In the Service field, define the service (`service`) for your application to use [unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/).
1. Set the privacy level for user input. See [Session Replay Browser Privacy Options](https://docs.datadoghq.com/session_replay/browser/privacy_options#mask-action-names) for more details.
1. Set a version number (`version`) for your deployed application in the initialization snippet. For more information, see Tagging.
1. Configure additional parameters as needed. See the Configuration reference section below for all available options.

### Step 4 - Deploy your application{% #step-4---deploy-your-application %}

Deploy the changes to your application. After your deployment is live, Datadog collects events from your users' browsers.

### Step 5 - Upload source maps (optional but recommended){% #step-5---upload-source-maps-optional-but-recommended %}

Upload your JavaScript source maps to access unminified stack traces. See the [source map upload guide](https://docs.datadoghq.com/real_user_monitoring/guide/upload-javascript-source-maps).

### Step 6 - Visualize your data{% #step-6---visualize-your-data %}

Now that you've completed the basic setup for Browser Error Tracking, your application is collecting browser errors and you can start monitoring and debugging issues in real-time.

Visualize the [data collected](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/data_collected/) in [dashboards](https://docs.datadoghq.com/real_user_monitoring/platform/dashboards/errors/) or create a search query in Error Tracking.

Until Datadog starts receiving data, your application appears as `pending` on the **Applications** page.

### Step 7 - Link errors with your source code (optional){% #step-7---link-errors-with-your-source-code-optional %}

In addition to sending source maps, the [Datadog CLI](https://github.com/DataDog/datadog-ci/tree/master/packages/datadog-ci/src/commands/sourcemaps#sourcemaps-command) reports Git information such as the commit hash, repository URL, and a list of tracked file paths in the code repository.

Error Tracking can use this information to correlate errors with your [source code](https://docs.datadoghq.com/integrations/guide/source-code-integration/), allowing you to pivot from any stack trace frame to the related line of code in [GitHub](https://github.com), [GitLab](https://about.gitlab.com) and [Bitbucket](https://bitbucket.org/product).

{% alert level="info" %}
Linking from stack frames to source code is supported in the [Datadog CLI](https://github.com/DataDog/datadog-ci/tree/master/packages/datadog-ci/src/commands/sourcemaps#sourcemaps-command) version `0.12.0` and later.
{% /alert %}

For more information, see the [Datadog Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/).

## Tagging for Error Tracking{% #tagging-for-error-tracking %}

These tags (configured in step 3 above) power Error Tracking functionality:

- Filtering and faceting issues by `service` and `env`
- Cross-product correlation with RUM, Logs, and APM for the same `service`/`env`
- Matching uploaded source maps through the same `service` and `version` you configure during upload

A service is an independent, deployable code repository that maps to a set of pages:

- If your browser application was constructed as a monolith, your Datadog application has one service name for the application.
- If your browser application was constructed as separate repositories for multiple pages, edit the default service names throughout the lifecycle of your application.

Learn more about [tagging](https://docs.datadoghq.com/getting_started/tagging/) in Datadog.

## Configuration reference{% #configuration-reference %}

Refer to the [Browser SDK API Reference](https://datadoghq.dev/browser-sdk/interfaces/_datadog_browser-rum.RumInitConfiguration.html) for the full list of available configuration options.

## Next steps{% #next-steps %}

You can monitor unhandled exceptions, unhandled promise rejections, handled exceptions, handled promise rejections, and other errors that the Browser SDK does not automatically track. Learn more about [Collecting Browser Errors](https://docs.datadoghq.com/error_tracking/frontend/collecting_browser_errors/).

## Further reading{% #further-reading %}

- [datadog-ci Source code](https://github.com/DataDog/datadog-ci/tree/master/packages/datadog-ci/src/commands/sourcemaps)
- [Upload JavaScript source maps](https://docs.datadoghq.com/real_user_monitoring/guide/upload-javascript-source-maps)
- [Learn about the Error Tracking Explorer](https://docs.datadoghq.com/error_tracking/explorer)
