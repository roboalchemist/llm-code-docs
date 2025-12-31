# Source: https://docs.apify.com/sdk/python/docs/concepts/logging.md

# Source: https://docs.apify.com/api/client/python/docs/concepts/logging.md

# Source: https://docs.apify.com/sdk/python/docs/concepts/logging.md

# Source: https://docs.apify.com/api/client/python/docs/concepts/logging.md

# Source: https://docs.apify.com/sdk/python/docs/concepts/logging.md

# Source: https://docs.apify.com/api/client/python/docs/concepts/logging.md

# Source: https://docs.apify.com/sdk/python/docs/concepts/logging.md

# Source: https://docs.apify.com/api/client/python/docs/concepts/logging.md

# Logging

Copy for LLM

The library logs useful debug information to the `apify_client` logger whenever it sends requests to the Apify API. You can configure this logger to print debug information to the standard output by adding a handler:

```
import logging

# Configure the Apify client logger
apify_client_logger = logging.getLogger('apify_client')
apify_client_logger.setLevel(logging.DEBUG)
apify_client_logger.addHandler(logging.StreamHandler())
```

The log records include additional properties, provided via the extra argument, which can be helpful for debugging. Some of these properties are:

* `attempt` - Number of retry attempts for the request.
* `status_code` - HTTP status code of the response.
* `url` - URL of the API endpoint being called.
* `client_method` - Method name of the client that initiated the request.
* `resource_id` - Identifier of the resource being accessed.

To display these additional properties in the log output, you need to use a custom log formatter. Here's a basic example:

```
import logging

# Configure the Apify client logger
apify_client_logger = logging.getLogger('apify_client')
apify_client_logger.setLevel(logging.DEBUG)
apify_client_logger.addHandler(logging.StreamHandler())

# Create a custom logging formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s - '
    '%(attempt)s - %(status_code)s - %(url)s'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
apify_client_logger.addHandler(handler)
```

For more information on creating and using custom log formatters, refer to the official Python [logging documentation](https://docs.python.org/3/howto/logging.html#formatters).
