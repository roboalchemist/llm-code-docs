# Source: https://dev.writer.com/api-reference/rate-limits.md

# Understand rate limits

> Understand API rate limits for Writer endpoints. Learn about RPM and TPM limits, best practices, and retry strategies for optimal performance.

<Info>
  For custom rate limits, **[contact Sales](https://go.writer.com/contact-sales)**.
</Info>

To ensure optimal service performance and fairness in resource allocation, our endpoints enforce the following rate limits.

1. **RPM (requests per minute)**: 400
2. **TPM (token per min)**: 25,000

## Best practices

<AccordionGroup>
  <Accordion title="Monitor request rates" icon="monitor-waveform">
    Implement mechanisms in your applications to track and regulate the
    frequency of your requests to stay within the prescribed limits.
  </Accordion>

  <Accordion title="Adaptive retry strategies" icon="rotate-right">
    In cases where you exceed these limits, employ adaptive retry strategies
    with exponential backoff to handle retries efficiently and reduce the
    likelihood of consecutive limit breaches.
  </Accordion>

  <Accordion title="Response to HTTP 429 status codes" icon="code">
    Prepare to handle HTTP 429 (too many requests) responses by pausing or
    slowing down request rates.
  </Accordion>
</AccordionGroup>
