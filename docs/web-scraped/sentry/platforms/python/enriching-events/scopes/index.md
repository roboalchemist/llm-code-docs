---
---
title: Scopes
description: "The SDK will in most cases automatically manage the scopes for you in the framework integrations. Learn what a scope is and how you can use it to your advantage."
---

Scopes store extra data that the SDK adds to your event when sending the event to Sentry. While the SDKs typically manage the scope automatically, understanding how scopes work and how you can manage them manually can be helpful.

## What is a Scope?

A scope manages an event's data. For instance, the SDK stores [contexts](../context/) and [breadcrumbs](../breadcrumbs/) on the scope.

There are three types of scopes. Exactly one scope of each type will be active at a specific point in time.

- *Global scope*: A single globally-shared scope storing data relevant for the whole app (such as the release).
- *Isolation scope*: Thread-local scope created for each request-response lifecycle to store data relevant to the request.
- *Current scope*: Thread-local scope created for each span to store data relevant to the span.

The SDK and the SDK's built-in integrations automatically manage the scopes. For example, web framework integrations create an isolation scope for each request handled. When you call a top-level API function, such as , the SDK determines the correct scope on which to operate.

When sending an event to Sentry, the final data applied to the event is the result of merging the three scopes, applying data from each in turn. The global scope is applied first, followed by the isolation scope, and then the current scope.

## Changing the Scope

We generally recommend using the top-level API to manage your scopes, since the SDK's automatic scope management handles most use cases.

However, if your use case requires direct access to the scope object, you can use the  context manager.  forks the current scope, allows you to modify the new scope while the context manager is active, and restores the original scope afterwards. Using  allows you to send data for only one specific event, such as [modifying the context](../context/). It is roughly equivalent to the  context manager in earlier (1.x) versions of the SDK.

Avoid calling top-level APIs inside the  context manager. The top-level API might interact with a different scope from what  yields, causing unintended results. While within the  context manager, please call methods directly on the scope that  yields!

Using  allows you to attach additional information, such as adding custom tags.

To learn what useful information can be associated with scopes see
[the context documentation](../context/).
