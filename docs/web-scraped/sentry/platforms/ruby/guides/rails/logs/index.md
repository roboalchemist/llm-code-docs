---
---
title: Set Up Logs
description: "Structured logs allow you to send, view and query logs sent from your Rails applications within Sentry."
---

With Sentry Structured Logs, you can send text-based log information from your Rails applications to Sentry. Once in Sentry, these logs can be viewed alongside relevant errors, searched by text-string, or searched using their individual attributes.

## Requirements

## Setup

## Usage

## Options

## Default Attributes

## Troubleshooting

If logs aren't appearing in Sentry:

**Verify configuration:**
```ruby
Sentry.init do |config|
  config.enable_logs = true  # Must be set
end
```

**Test your setup:**

```ruby
Sentry.logger.info("Test log message")
Sentry.get_current_client.flush
```

Then verify if the log appears in Sentry.

**Enable debug mode:**
```ruby
config.debug = true  # See SDK diagnostic output
```
