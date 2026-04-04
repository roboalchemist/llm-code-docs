# Source: https://grafbase.com/docs/gateway/telemetry/sanitization.md

# Sanitization

The operation query string is part of the OpenTelemetry metrics & traces attributes. To avoid leaking any sensitive data it's sanitized to remove any constant data:

- Strings are replaced with `""`
- Numbers with `0`.
- Boolean and enums are kept as is.
- Lists are replaced with `[]`.
- Object structure is kept, but their field values are sanitized. So a `{ id: "890", rows: [{a: "1"}]}` becomes `{id: "", rows: []}`