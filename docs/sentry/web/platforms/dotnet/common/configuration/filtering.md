---
---
title: Filtering
description: "Learn more about how to configure your SDK to filter events reported to Sentry."
---

When you add Sentry to your app, you get a lot of valuable information about errors and performance. And lots of information is good -- as long as it's the right information, at a reasonable volume.

The Sentry SDKs have several configuration options to help you filter out events.

We also offer [Inbound Filters](/concepts/data-management/filtering/) to filter events in sentry.io. We recommend filtering at the client level though, because it removes the overhead of sending events you don't actually want. Learn more about the [fields available in an event](https://develop.sentry.dev/sdk/data-model/event-payloads/).

## Filtering Error Events

To prevent certain errors from being reported to Sentry, use the  or  configuration options, which allows you to evaluate whether to send an error or now. Alternatively, you can also control the behaviour by enabling, or disabling integrations.

### Using 

All Sentry SDKs support the  callback method. Because it's called immediately before the event is sent to the server, this is your last chance to decide not to send data or to edit it.  receives the event object as a parameter, which you can use to either modify the event’s data or drop it completely by returning `null`, based on custom logic and the data available on the event.

Note also that breadcrumbs can be filtered, as discussed in [our Breadcrumbs documentation](/product/error-monitoring/breadcrumbs/).

### Using  and 

The SDK also allows you to provide your own, custom exception filters. These have to inherit from 

```csharp
public class MyExceptionFilter : IExceptionFilter
{
    public bool Filter(Exception ex)
    {
        // TODO: Add your filtering logic
    }
}
```

and can then be provided to the options during initialization.

```csharp
options.AddExceptionFilter(new MyExceptionFilter());
```

Exception types provided via  automatically get filtered and prevented from being set to Sentry.

```csharp
options.AddExceptionFilterForType();
```

## Filtering Transaction Events

To prevent certain transactions from being reported to Sentry, use the  or  configuration option, which allows you to provide a function to evaluate the current transaction and drop it if it's not one you want.

### Using 

**Note:** The  and  config options are mutually exclusive. If you define a  to filter out certain transactions, you must also handle the case of non-filtered transactions by returning the rate at which you'd like them sampled.

In its simplest form, used just for filtering the transaction, it looks like this:

It also allows you to sample different transactions at different rates.

If the transaction currently being processed has a parent transaction (from an upstream service calling this service), the parent (upstream) sampling decision will always be included in the sampling context data, so that your  can choose whether and when to inherit that decision. In most cases, inheritance is the right choice, to avoid breaking distributed traces. A broken trace will not include all your services. See Inheriting the parent sampling decision to learn more.

Learn more about configuring the sample rate.

### Using 

