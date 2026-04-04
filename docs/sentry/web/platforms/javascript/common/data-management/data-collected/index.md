---
---
title: Data Collected
description: "See what data is collected by the Sentry SDK."
---

Sentry takes data privacy very seriously and has default settings in place that prioritize data safety, especially when it comes to personally identifiable information (PII) data. When you add the Sentry SDK to your application, you allow it to collect data and send it to Sentry during the runtime and build time of your application.

The category types and amount of data collected vary, depending on the integrations you've enabled in the Sentry SDK. This page lists data categories that the Sentry JavaScript SDK collects.

Many of the categories listed here require you to enable the sendDefaultPii option.

## HTTP Headers

By default, the Sentry SDK sends HTTP response or request headers.

## Cookies

By default, the Sentry SDK doesn't send cookies.

If you want to send cookies, set `sendDefaultPii: true` in the `Sentry.init()` call. This will send the cookie headers `Cookie` and `Set-Cookie` from fetch and XHR requests.

## Information About Logged-in User

By default, the Sentry SDK doesn't send any information about the logged-in user, such as email address, user ID, or username.

The type of logged-in user information you'll be able to send depends on the integrations you enable in Sentry's SDK. Most integrations won't send any user information. Some integrations (e.g. User Feedback) make it possible to send data like the user ID, username, and email address.

  ### Local Device User
  
  By default, the Sentry SDK doesn't send any information about the user currently logged-in to the device where the app is running. However, you should exercise caution when logging file system errors as paths may contain the current username.

## Users' IP Address and Location

By default, the Sentry SDK doesn't send the user's IP address.

To enable sending the user's IP address and infer the location, set `sendDefaultPii: true`. In some integrations such as `handleRequest` in Astro, you can send the user's IP address by enabling `trackClientIp`.

If sending the IP address is enabled we will try to infer the IP address or use the IP address provided by `ip_address` in `Sentry.setUser()`. If you set `ip_address: null`, the IP address won't be inferred.

## Request URL

The full request URL of outgoing and incoming HTTP requests is **always sent to Sentry**. Depending on your application, this could contain PII data. For example, a URL like `/users/1234/details`, where `1234` is a user id (which may be considered PII).

## Request Query String

The full request query string of outgoing and incoming HTTP requests is **always sent to Sentry**. Depending on your application, this could contain PII data. For example, a query string like `?user_id=1234`, where `1234` is a user id (which may be considered PII).

However, Sentry has some default [server-side data scrubbing](/security-legal-pii/scrubbing/server-side-scrubbing/) in place to remove sensitive data from the query string. For example, the `apiKey` and `token` query parameters are removed by default.

## Request Body

By default, Sentry sends the size of the body content of incoming HTTP requests. This is inferred from the `content-length` header. Sentry does not send the request body itself on the client-side.

  On the server-side, the incoming request body is captured by default. You can disable sending the incoming request body by configuring `ignoreIncomingRequestBody` in the HTTP Integration.

  If `sendDefaultPii` is enabled, you can send Form Data with `captureActionFormDataKeys` in the Remix server-side configuration.

## Response Body

By default, the Sentry SDK doesn't send the body content of responses received from outgoing requests. By default, the SDK will send the response body size based on the `content-length` header.

## Source Context

By default, SDKs set up by the Sentry CLI Wizard (`@sentry/wizard`) will enable uploading source maps to Sentry.

To disable source map upload, see the Source Maps documentation.

## Local Variables In Stack Trace

The Sentry SDK does not send local variables in the error stack trace in client-side JavaScript SDKs.

  You can enable sending local variables by setting `includeLocalVariables: true` in the `Sentry.init()` call. This activates the Local Variables Integration. The integration is added by default in Node.js-based runtimes.

## Device, Browser, OS and Runtime Information

By default, the Sentry SDK sends information about the device and runtime to Sentry.

  In browser environments, this information is obtained by the User Agent string. The User Agent string contains information about the browser, operating system, and device type.

  In server-side environments, the Sentry SDK uses the `os` module to get information about the operating system and architecture.

  The Sentry Electron SDK collects information about the device, such as the platform, architecture, available memory and version and build of your operating system or Linux distribution. 
  
  By default, the Additional Context Integration collects dimensions and resolution of the device screen. It can optionally collect the device's manufacturer and model name if the `deviceModelManufacturer` option is enabled. 
  
  By default, the GPU Context Integration collects GPU information. It can optionally collect more detailed information if the `infoLevel` option is set to `complete`.
  
  

  
    ## Session Replay

    By default, our Session Replay SDK masks all text content, images, web views, and user input. This helps ensure that no sensitive data is exposed. You can find more details in the Session Replay documentation.

    Session Replay also captures basic information about all outgoing fetch and XHR requests in your application. This includes the URL, request and response body size, method, and status code. If `networkDetailAllowUrls` are defined, the request and response body will be sent to Sentry as well. This can include PII data if the request or response body contains PII information.

    Console messages are also captured by default in Session Replay. To scrub console messages, you can use the `beforeAddRecordingEvent` option to filter console messages before they are sent to Sentry.
  

  ## Console Logs

  By default, the Sentry SDK sends JS console logs to Sentry as breadcrumbs which may contain PII data.

  To disable sending console messages, set `console: false` in your `Sentry.breadcrumbsIntegration` config, see the Breadcrumbs documentation.

  
    ## Referrer URL

    By default, the Sentry SDK sends the referrer URL to Sentry. This is the URL of the page that linked to the current page.
  

  
    ## Stack Trace Context Lines

    By default, the Context Lines Integration is enabled. This integration sends the surrounding lines of code for each frame in the stack trace. This can include PII data if the code contains PII information.
  

  
    ## LLM Inputs And Responses

    When using the Vercel AI Integration, the used prompt is sent to Sentry along with meta data like model ID and used tokens. Check out the full list of attributes [in the code](https://github.com/getsentry/sentry-javascript/blob/master/packages/node/src/integrations/tracing/vercelai/index.ts).

    ## Database Queries

    By default, the Sentry SDK sends SQL queries to Sentry. The SQL queries can include PII information if the statement is not parametrized.

    MongoDB queries are sent as well, but the Sentry SDK will not send the full MongoDB query. Instead, it will send a parameterized version of the query.

  

  ## tRPC Context

  By default, the Sentry SDK doesn't send tRPC input from the tRPC context.

  If you want to send the tRPC input you can enable it by setting `sendDefaultPii: true` in the `Sentry.init()` call or by setting `attachRpcInput: true` in the `Sentry.trpcMiddleware()` options.

  ## Window Titles
  
  The Electron Breadcrumbs Integration can optionally capture the window titles for breadcrumbs related to windows events. These can potentially contain PII so are disabled by default but can be enabled via the `captureWindowTitles` option.

  ## Native Crashes
  
  At the time of a native crash, the stack of each thread is collected and sent to Sentry as part of the Minidump snapshot. This information is sent to Sentry by default, but dropped after processing the event in the backend.

  These files are not stored by default, but you can [enable Minidump Storage](/platforms/native/guides/minidumps/enriching-events/attachments/#store-minidumps-as-attachments) in the Sentry organization or project settings.

