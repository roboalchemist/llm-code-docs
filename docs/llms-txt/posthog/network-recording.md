# Source: https://posthog.com/docs/session-replay/network-recording.md

# Network performance recording - Docs

Session replay allows you to capture network requests and responses, providing insights into network performance and potential issues. This feature can be particularly useful for debugging and optimizing your application's network interactions.

## Web

PostHog can capture network requests that occur during the browser session, so you can see if your application is sending the expected requests and response, and check the effect of slow network requests or errors on the user experience.

You can enable network recording from your [project settings](https://app.posthog.com/project/settings):

![Enable network recording in your PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/session-replay/enable-session-replay-in-project-settings-light-mode.png)![Enable network recording in your PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/session-replay/enable-session-replay-in-project-settings-dark-mode.png)

When enabled PostHog always captures:

-   the network request URL,
-   [performance information](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEntry) about the request,

When request capture is enabled you can also enabled payload and body capture, this includes:

-   the request method
-   the response code
-   request & response headers (if enabled)
-   request & response body (if enabled)

## Sensitive information

We automatically scrub some sensitive information from network headers and payloads, but if your request or response payloads could contain sensitive data, you should provide a function to mask the captured data when you initialize PostHog.

We have a deny-list of headers that we will never capture (even if you provide a masking function).

-   authorization
-   x-forwarded-for
-   cookie
-   set-cookie
-   x-api-key
-   x-real-ip
-   remote-addr
-   forwarded
-   proxy-authorization
-   x-csrf-token
-   x-csrftoken
-   x-xsrf-token

And we redact bodies if we believe they contain

-   credit card numbers
-   social security numbers
-   password
-   secret
-   passwd
-   api\_key
-   apikey
-   auth
-   credentials
-   mysql\_pwd
-   privatekey
-   private\_key
-   token

> **Note:** If you provide a masking function to alter redaction of payloads it entirely replaces PostHog's automatic payload redaction.

## How to register a callback to inspect and redact each network request

Web

PostHog AI

```javascript
posthog.init('<ph_project_token>', {
    session_recording: {
        maskCapturedNetworkRequestFn: (request: CapturedNetworkRequest) => {
            // For example: ignoring a request entirely
            if (request.name.includes('example.com')) {
                return null
            }
            // ... or remove the query string from the URL
            request.name = request.name.split('?')[0]
            // ...redact the request or response body **however makes sense for your payloads**
            request.requestBody = request.requestBody?.replace(/"password":\s*"[^"]*"/g, '"password": "redacted-password"')
            request.responseBody = request.responseBody?.replace(/"password":\s*"[^"]*"/g, '"password": "redacted-password"')
            // ... or remove the request body
            request.requestBody = undefined
            // ... and more
            // finally return the request
            return request
        }
    }
})
```

## Troubleshooting

### Recording from localhost

Due to the very high volume of network requests that some tools can make (for example when running hot-reload during development) PostHog does not capture network requests when running on localhost

### Requests early in the page lifecycle don't capture all information

PostHog has to wrap `fetch` and `xhr` in order to capture network requests. If your application makes network requests before PostHog has had a chance to wrap them, then PostHog will not capture all information about the request.

### PostHog truncated the request or response body

In order to maintain service levels we truncate all request and response bodies at 1MB

### A network request says it was redacted

We are cautious in what we capture. If you think we're being too cautious you can override the masking function.

### I want to query the network performance data I capture

We'd love that too! It's not possible right now but watch this space. You can [subscribe for updates in GitHub](https://github.com/PostHog/posthog/issues/19686)

## Android

To capture network requests in your recordings, add `PostHogOkHttpInterceptor` to your `OkHttp Interceptor`.

Android

PostHog AI

```kotlin
import com.posthog.PostHogOkHttpInterceptor
import okhttp3.OkHttpClient
private val client = OkHttpClient.Builder()
    // Support for remote configuration
    // in the [session replay settings](https://app.posthog.com/settings/project-replay#replay-network)
    // requires SDK version 3.32.0 or higher.
    .addInterceptor(PostHogOkHttpInterceptor(captureNetworkTelemetry = true))
    .build()
```

> **Note:** Only metric-like data like speed, size, and response code are captured. No data is captured from the request or response body.

## iOS

In iOS, PostHog uses method swizzling on [URLSession](https://developer.apple.com/documentation/foundation/urlsession) methods, which allows for the out-of-the-box collection of network data.

However, URLSession’s async/await-powered APIs which are not exposed to the `objc` runtime and cannot be swizzled. As a result, network telemetry cannot be automatically captured.

For apps using async `URLSession` methods, PostHog provides wrapper functions that you can use to manually capture network logs.

Swift

PostHog AI

```swift
import PostHog
func fetchData(from url: URL) async throws -> Data {
   // let (data, _) = try await URLSession.shared.data(from: url)      // ⬅ replace this
   let (data, _) = try await URLSession.shared.postHogData(from: url)  // 🦔 with this
  // your logic here...
  return data
}
```

You can find a list of available methods to use manually in the [URLSession extension source](https://github.com/PostHog/posthog-ios/blob/main/PostHog/Replay/URLSessionExtension.swift).

> **Note:** Only metric-like data like speed, size, and response code are captured. No data is captured from the request or response body.

## React Native

To capture network requests in your recordings, add `captureNetworkTelemetry: true` to your PostHog Session replay configuration alongside any of your other configuration options:

> **Note:** Capture network requests is only available for iOS.

TypeScript

PostHog AI

```typescript
export const posthog = new PostHog(
  '<ph_project_token>',
  {
    // Enable session recording. Requires enabling in your project settings as well.
    // Default is false.
    enableSessionReplay: true,
    sessionReplayConfig: {
      // Whether network requests are captured in recordings. Default is true
      // Only metric-like data like speed, size, and response code are captured.
      // No data is captured from the request or response body.
      // iOS only
      // Remote configuration via project settings requires SDK version 4.35.0 or higher.
      captureNetworkTelemetry: true,
      ...
    },
  },
);
```

> **Note:** Only metric-like data like speed, size, and response code are captured. No data is captured from the request or response body.

## Performance considerations

Capturing network performance data can have an impact on your application's performance. Be mindful of the amount of data you're capturing and consider implementing sampling or other optimization techniques if you're dealing with high-volume network traffic.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better