# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-12-08-ai-redact-ga.md

# Dec 08, 2025: AI_REDACT for automated redaction of PII (*General availability*)

The AI_REDACT function, now generally available, detects and redacts personally identifiable information (PII) from
unstructured text data using a large language model (LLM). AI_REDACT automatically recognizes various categories of PII
(name, address, and so on, including partial PII such as first or last name) and replaces them with placeholders.

For example, passing the following string to AI_REDACT:

> “John Smith’s email is [jsmith@example.com](mailto:jsmith%40example.com) and he lives in San Francisco.”

Results in the following output:

> “[NAME]’s email is [EMAIL] and he lives in [ADDRESS].”

For more information, see [Detect and redact personally identifiable information (PII)](../../../user-guide/snowflake-cortex/redact-pii.md) and [AI_REDACT](../../../sql-reference/functions/ai_redact.md).
