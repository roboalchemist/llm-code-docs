# Source: https://docs.datadoghq.com/security/application_security/setup/go/sdk.md

---
title: App and API Protection SDK for Go
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Enabling App and API Protection for Go > App and API Protection
  SDK for Go
---

# App and API Protection SDK for Go

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

If you need flexibility and features beyond those available when instrumenting your application automatically using [Orchestrion](https://github.com/DataDog/orchestrion), Datadog provides an App and API Protection API located at [github.com/DataDog/dd-trace-go/v2/appsec](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec). This API improves flexibility and offers additional features.

## Error event handling{% #error-event-handling %}

The API error type [`events.BlockingSecurityEvent`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec/events#BlockingSecurityEvent) is returned when a blocking event occurs, such blocking a user, IP, or request.

**Do not write any response to the client when you receive a `BlockingSecurityEvent` error**. A response could potentially send sensitive information to an attacker. To safely detect this type of error, use the helper function [events.IsSecurityError](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec/events#IsSecurityError).

When a `BlockingSecurityEvent` is returned, the SDK automatically sends a blocking response for you, typically an HTTP 403 Forbidden.

Customizing this behavior is possible. See the [Customize response to blocked requests](https://docs.datadoghq.com/security/application_security/policies/#customize-protection-behavior) section.

## HTTP body monitoring{% #http-body-monitoring %}

By default, a lot of Go HTTP Frameworks are not high level enough to provide parsed HTTP request and response bodies. Consequently, the App and API Protection SDK provides a way to monitor the HTTP request and response bodies manually:

- [`appsec.MonitorParsedHTTPBody`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec#MonitorParsedHTTPBody) to monitor the parsed request body.
- [`appsec.MonitorHTTPResponseBody`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec#MonitorHTTPResponseBody) to monitor the response body.

These functions automatically block the current request if the [Protection](https://docs.datadoghq.com/security/application_security/how-it-works/#built-in-protection) feature is enabled, and return a `BlockingSecurityEvent` error.

## User tracking{% #user-tracking %}

User login events can be tracked and blocked using the [track and block login requests](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info?tab=go#adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability) feature from these functions:

- [`appsec.TrackUserLoginSuccess`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec#TrackUserLoginSuccess) tracks a successful login event on your login endpoint. This function also calls [`appsec.SetUser`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec#SetUser) internally to associate the user with the current request.
- [`appsec.TrackUserLoginFailure`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec#TrackUserLoginFailure) tracks a failed login event on your login endpoint.
- [`appsec.SetUser`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec#SetUser) can be used on all authenticated requests to report users to Datadog and enable user blocking.

These functions automatically block the current request if the [Protection](https://docs.datadoghq.com/security/application_security/how-it-works/#built-in-protection) feature is enabled, and return a `BlockingSecurityEvent` error.

## Custom event tracking{% #custom-event-tracking %}

You can track [Business logic events](https://docs.datadoghq.com/security/application_security/policies/custom_rules/#business-logic-abuse-detection-rule) like user login success/failure using the [`appsec.TrackCustomEvent`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec#TrackCustomEvent) function. This function sets custom event data as service entry span tags, which triggers backend event monitoring, and can ultimately block IP addresses and/or associated user IDs.

## Example{% #example %}

Here's a concise example showing how to integrate the App and API Protection SDK into a standard `net/http` web application:

In the `main.go` file:

```go
package main

import (
    "encoding/json"
    "log"
    "net/http"
    "strings"

    "github.com/DataDog/dd-trace-go/v2/appsec"
    "github.com/DataDog/dd-trace-go/v2/appsec/events"
    "github.com/DataDog/dd-trace-go/v2/contrib/net/http/v2"
    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

type LoginRequest struct {
    Username string `json:"username"`
    Password string `json:"password"`
}

type User struct {
    Name     string `json:name`
    Username string `json:username`
    Email    string `json:email`
    password string
}

var users = []User{
    {
        Name: "John Doe",
        Username: "realjoe",
        Email: "john@gmail.com",
        password: "not-my-birthday",
    }
}

func main() {
    tracer.Start(tracer.WithService("my-web-app"), tracer.WithAppsecEnabled(true))
    defer tracer.Stop()

    mux := httptrace.NewServeMux()
    mux.HandleFunc("/login", loginHandler)
    mux.HandleFunc("/profile", authMiddleware(profileHandler))

    log.Fatal(http.ListenAndServe(":8080", mux))
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
    var req LoginRequest
    json.NewDecoder(r.Body).Decode(&req)

    // Monitor parsed request body
    if err := appsec.MonitorParsedHTTPBody(r.Context(), req); err != nil {
        if events.IsSecurityError(err) {
            return // AppSec handles the blocking response
        }
    }

    for _, user := range users {
        if req.Username == user.Username && req.Password == user.Password {
            metadata := map[string]string{"login_method": "password"}
            if err := appsec.TrackUserLoginSuccess(r.Context(), req.Username, "user123", metadata); err != nil && events.IsSecurityError(err) {
                return // User is blocked
            }

            response := map[string]string{"token": "<token_created>", "status": "success"}

            // Monitor response body
            appsec.MonitorHTTPResponseBody(r.Context(), response)

            w.Header().Set("Content-Type", "application/json")
            json.NewEncoder(w).Encode(response)
            return
        }
    }

    // Track failed login
    appsec.TrackUserLoginFailure(r.Context(), req.Username, true, metadata)
    http.Error(w, "Invalid credentials", http.StatusUnauthorized)
}

func authMiddleware(next http.HandlerFunc) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        user := "<username>" // Do real authentification here

        // Set user context on all authenticated requests
        if err := appsec.SetUser(r.Context(), user); err != nil && events.IsSecurityError(err) {
            return // User is blocked
        }

        next.ServeHTTP(w, r)
    }
}

func profileHandler(w http.ResponseWriter, r *http.Request) {
    // Track access to sensitive data
    appsec.TrackCustomEvent(r.Context(), "profile.access", map[string]string{
        "data_type": "personal_info",
    })

    userAsked := r.Query().Get("user")
    user := users[0] // Search for the user

    // Monitor response body
    appsec.MonitorHTTPResponseBody(r.Context(), user);
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(user)
}
```

This example demonstrates:

- **Body Monitoring**: `MonitorParsedHTTPBody` and `MonitorHTTPResponseBody` for request/response security
- **User Tracking**: `TrackUserLoginSuccess`/`TrackUserLoginFailure` for login events, `SetUser` for authentication
- **Custom Events**: `TrackCustomEvent` for business logic monitoring
- **Error Handling**: Proper `BlockingSecurityEvent` handling with `IsSecurityError`

Key points:

- Always check `IsSecurityError(err)` and return without writing responses when blocked
- Use `SetUser` on authenticated requests to enable user blocking capabilities
- Track important business events that could indicate suspicious activity

## Further Reading{% #further-reading %}

- [Go Security API docs](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/appsec)
- [Sample application used for exhaustive SDK testing](https://github.com/DataDog/appsec-go-test-app)
- [Adding user information to traces](https://docs.datadoghq.com/security/application_security/add-user-info/)
- [Troubleshooting App and API Protection](https://docs.datadoghq.com/security/application_security/troubleshooting)
