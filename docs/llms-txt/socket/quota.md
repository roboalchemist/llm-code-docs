# Source: https://docs.socket.dev/reference/quota.md

# Quota

This page explains how Socket API quota works

Each API endpoint has a **quota** and each API token has a **maximum quota** that can use **per hour**. This is used to prevent an abuse of expensive API calls.

If the maximum quota of an API token has been exceeded, the API will return a `429` error and the `Retry-After` header will contain the number of seconds until you can call that same endpoint successfully (ie. have enough quota for that endpoint).