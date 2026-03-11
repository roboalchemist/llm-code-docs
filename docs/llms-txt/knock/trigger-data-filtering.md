# Source: https://docs.knock.app/api-reference/overview/trigger-data-filtering.md

# Trigger data filtering

Some V1 API endpoints that return lists of message data accept a `trigger_data` parameter. Knock uses this parameter to scope results it returns down to messages generated with the trigger data you provide.

The trigger data that Knock filters against is the _**combined and truncated data from the time the message was generated**_.

If a batch step preceded the creation of your message, the trigger data available for filtering will be the combined data for all the workflow triggers bundled into your batch. If a fetch step preceded, then the filterable data will include any data pulled in via the fetch step request.

Knock truncates trigger data for filtering to ensure it can efficiently process your request. The current data truncation rules are:

- Nested data structures (objects and arrays) are removed. Trigger data for filtering will be a JSON object with a single level of key-value pairs.
- Supported values are the JSON scalars string, number, boolean, and `null`.
- String values are limited to 256 characters in length. Strings that exceed this limit are truncated to the maximum.
