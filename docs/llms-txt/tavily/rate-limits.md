# Source: https://docs.tavily.com/documentation/rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits

> Learn about Tavily's API rate limits for both  development and production environments.

We offer two types of rate limits based on the environment associated with your API key.

<Card icon="key" href="https://app.tavily.com" title="Get your API key" horizontal>
  Create your Development or Production API keys.
</Card>

<table style={{ textAlign: "left", padding: "8px", width: "100%", borderCollapse: "collapse" }}>
  <thead>
    <tr>
      <th style={{ textAlign: "left", padding: "8px", borderBottom: "1px solid #ddd" }}>Environment</th>
      <th style={{ textAlign: "left", padding: "8px", borderBottom: "1px solid #ddd" }}>Requests per minute (RPM)</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}><code>Development</code></td>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}>100</td>
    </tr>

    <tr>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}><code>Production</code></td>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}>1,000</td>
    </tr>
  </tbody>
</table>

## Crawl Endpoint Rate Limits

The crawl endpoint has a separate rate limit that applies to both development and production keys:

<table style={{ textAlign: "left", padding: "8px", width: "100%", borderCollapse: "collapse" }}>
  <thead>
    <tr>
      <th style={{ textAlign: "left", padding: "8px", borderBottom: "1px solid #ddd" }}>Environment</th>
      <th style={{ textAlign: "left", padding: "8px", borderBottom: "1px solid #ddd" }}>Requests per minute (RPM)</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}><code>Development</code></td>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}>100</td>
    </tr>

    <tr>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}><code>Production</code></td>
      <td style={{ padding: "8px", borderBottom: "1px solid #ddd" }}>100</td>
    </tr>
  </tbody>
</table>

<Tip>
  1. Access to production keys requires either an active **Paid Plan** or **PAYGO** enabled. More information can be found [here](/guides/api-credits).
  2. When using the REST API, ensure you include your API key in the header to apply the correct rate limits.
</Tip>
