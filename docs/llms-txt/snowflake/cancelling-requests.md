# Source: https://docs.snowflake.com/en/developer-guide/sql-api/cancelling-requests.md

# Canceling the execution of a SQL statement

To cancel the execution of a statement, send a `POST` request to the cancel endpoint. See
[POST /api/v2/statements/{statementHandle}/cancel](reference.md) for details.

```none
POST /api/v2/statements/{statementHandle}/cancel
```

The following flow chart illustrates the steps that you take to cancel a request.
