# Source: https://docs.aurelio.ai/semantic-router/user-guide/guides/configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration

# Configuration

This guide covers various configuration options available in semantic-router.

## Logging Configuration

Semantic-router uses Python's logging module for debugging and monitoring. You can control the verbosity of logs using environment variables.

### Setting Log Levels

You can configure the log level in two ways:

1. **Using the semantic-router specific variable (recommended):**
   ```bash  theme={null}
   export SEMANTIC_ROUTER_LOG_LEVEL=DEBUG
   ```

2. **Using the general LOG\_LEVEL variable:**
   ```bash  theme={null}
   export LOG_LEVEL=WARNING
   ```

The library checks for `SEMANTIC_ROUTER_LOG_LEVEL` first, then falls back to `LOG_LEVEL`. If neither is set, it defaults to `INFO`.

### Available Log Levels

* `DEBUG`: Detailed information for diagnosing problems
* `INFO`: General informational messages (default)
* `WARNING`: Warning messages for potentially problematic situations
* `ERROR`: Error messages for serious problems
* `CRITICAL`: Critical messages for very serious errors

### Example Usage

```python  theme={null}
import os
# Set before importing semantic-router
os.environ["SEMANTIC_ROUTER_LOG_LEVEL"] = "DEBUG"

from semantic_router import Route, SemanticRouter
# Your debug logs will now be visible
```

This is particularly useful when:

* Debugging encoder or index issues
* Monitoring route matching decisions
* Troubleshooting performance problems
* Understanding the library's internal behavior


Built with [Mintlify](https://mintlify.com).