# Source: https://www.inngest.com/docs-markdown/reference/python/client/overview

# Inngest client

The Inngest client is used to configure your application and send events outside of Inngest functions.

```py
import inngest

inngest_client = inngest.Inngest(
    app_id="flask_example",
)
```

***

## Configuration

- `api_base_url` (str): Override the default base URL for our REST API (https\://api.inngest.com/). See also the INNGEST\_EVENT\_API\_BASE\_URL environment variable.

* `app_id` (str): A unique identifier for your application. We recommend a hyphenated slug.

- `env` (str): The environment name. Required only when using Branch Environments.

* `event_api_base_url` (str): Override the default base URL for sending events (https\://inn.gs/). See also the INNGEST\_EVENT\_API\_BASE\_URL environment variable.

- `event_key` (str): An Inngest event key. Alternatively, set the INNGEST\_EVENT\_KEY environment variable.

* `is_production` (bool): Whether the SDK should run in production mode. See also the INNGEST\_DEV environment variable.

- `logger` (logging.Logger | logging.LoggerAdapter): A logger object derived from logging.Logger or logging.LoggerAdapter. Defaults to using logging.getLogger(\_\_name\_\_) if not provided.

* `middleware` (list): A list of middleware to add to the client. Read more in our middleware docs.

- `signing_key` (str): The Inngest signing key. Alternatively, set the INNGEST\_SIGNING\_KEY environment variable.