---
---
title: Limiting Trace Propagation
---

By default, trace information (`sentry-trace` and `baggage` headers) will be added to all outgoing HTTP requests. If you want to limit the URLs where trace information is added, you can specify that using the `trace_propagation_targets` option:

In the example above, trace information will be added to all requests to URLs that contain `myproject.org` and to all sub domains of `otherservice.org`, like `https://api.otherservice.org/something/` and `https://payment.otherservice.org/something/`.

See our config options documentation for more information about the `trace_propagation_targets` option.
