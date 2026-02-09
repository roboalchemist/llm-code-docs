# Source: https://docs.turso.tech/api-reference/response-codes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Errors

The Turso API will respond with an HTTP status code, and in the event of an error, return an error message in the response body.

| Code  | Description                                                      |
| ----- | ---------------------------------------------------------------- |
| `200` | `OK` — Successful request                                        |
| `401` | `Unauthorized` — Invalid or expired auth token                   |
| `402` | `Payment required` — Check you have an active subscription       |
| `403` | `Forbidden` — You do not have permission to access this resource |
| `409` | `Conflict` — Resource already exists                             |
