---
---
title: Custom Instrumentation
description: "Learn how to capture performance data on any action in your app."
---

To capture transactions and spans customized to your organization's needs, you must first set up tracing.

## Adding Span & Transaction Data Attributes

You can capture data attributes along with your spans and transactions. You can set data attributes when starting a span or transaction:

```rust
use serde_json::json;

// Create a transaction and assign data attributes...
let tx_ctx = sentry::TransactionContext::new("Example Transaction", "http.server");
let transaction = sentry::start_transaction(tx_ctx);
transaction.set_data("attribute_1", "hello".into());
transaction.set_data("attribute_2", 42.into());

// ... or create a span and assign data attributes
let span = transaction.start_child("http.client", "Example span");
span.set_data("is_ok", true.into());
span.set_data("other_data", json!({ "an": "object" }));
```

Or you can add data attributes to an existing span:

```rust
let span = Hub::current().configure_scope(|scope| scope.get_span());
if let Some(span) = span {
    span.set_data("hello", "world".into());
}
```
