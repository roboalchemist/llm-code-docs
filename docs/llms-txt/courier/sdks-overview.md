# Source: https://www.courier.com/docs/sdk-libraries/sdks-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Started with Courier SDKs

> Courier provides server-side SDKs for sending notifications and client-side SDKs for embedding in-app experiences like Inbox and Toast.

Courier SDKs let you send notifications from your server, embed an in-app inbox in your app, and manage user preferences programmatically. Choose based on where you're integrating:

* **Server-side SDKs** wrap the Courier REST API for sending messages, managing users, templates, tenants, and more
* **Client-side SDKs** provide UI components (Inbox, Toast) and client-side authentication for web and mobile apps

If you prefer raw HTTP, the full [API Reference](/reference/get-started) documents every endpoint with request/response examples. You can also use the [CLI](/tools/cli) for quick operations from the terminal, or connect AI coding agents via the [MCP server](/tools/mcp).

## Server-side SDKs

These SDKs are thin wrappers around the [REST API](/reference/get-started). Use them to send notifications, manage profiles, and configure templates from your backend.

| Language                        | Package               | Install                                            |
| ------------------------------- | --------------------- | -------------------------------------------------- |
| [Node.js](/sdk-libraries/node)  | `@trycourier/courier` | `npm install @trycourier/courier`                  |
| [Python](/sdk-libraries/python) | `trycourier`          | `pip install trycourier`                           |
| [Ruby](/sdk-libraries/ruby)     | `trycourier`          | `gem install trycourier`                           |
| [Go](/sdk-libraries/go)         | `courier-go`          | `go get github.com/trycourier/courier-go/v4`       |
| [Java](/sdk-libraries/java)     | `courier-java`        | `implementation("com.courier:courier-java:4.9.1")` |
| [PHP](/sdk-libraries/php)       | `courier-php`         | `composer require trycourier/courier`              |
| [C#](/sdk-libraries/csharp)     | `Courier`             | `dotnet add package Courier`                       |

## Client-side SDKs

These SDKs provide pre-built UI components and client-side APIs for embedding notification experiences in your app.

### Web

All three web packages are published from the [`courier-web`](https://github.com/trycourier/courier-web) monorepo:

| Package                                                               | What it provides                                                          |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [`@trycourier/courier-react`](/sdk-libraries/courier-react-web)       | Inbox, Toast, Preferences components + `useCourier()` hook (React 17/18+) |
| [`@trycourier/courier-ui-inbox`](/sdk-libraries/courier-ui-inbox-web) | Framework-agnostic Inbox and Toast web components                         |
| [`@trycourier/courier-js`](/sdk-libraries/courier-js-web)             | Headless browser API client for custom UIs                                |

### Mobile

| Platform                                    | Package                            | What it provides                                              |
| ------------------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| [React Native](/sdk-libraries/react-native) | `@trycourier/courier-react-native` | Inbox, push notifications, and preferences for React Native   |
| [iOS](/sdk-libraries/ios)                   | `Courier_iOS`                      | Inbox, push notifications, and preferences for Swift/SwiftUI  |
| [Android](/sdk-libraries/android)           | `courier-android`                  | Inbox, push notifications, and preferences for Kotlin/Compose |
| [Flutter](/sdk-libraries/flutter)           | `courier_flutter`                  | Inbox, push notifications, and preferences for Flutter        |

<CardGroup cols={2}>
  <Card title="Node.js SDK" icon="node-js" href="/sdk-libraries/node">
    The most popular server-side SDK for sending notifications.
  </Card>

  <Card title="React SDK" icon="react" href="/sdk-libraries/courier-react-web">
    Embed Inbox, Toast, and Preferences in your React app.
  </Card>

  <Card title="API Reference" icon="code" href="/reference/get-started">
    Full REST API docs with request/response examples.
  </Card>

  <Card title="CLI & MCP" icon="terminal" href="/tools/cli">
    Use Courier from the command line or connect AI coding agents.
  </Card>
</CardGroup>
