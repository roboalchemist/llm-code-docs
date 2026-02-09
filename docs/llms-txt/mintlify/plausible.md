# Source: https://www.mintlify.com/docs/integrations/analytics/plausible.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plausible

> Track simple, privacy-respecting analytics with Plausible.

Add your site's domain to `docs.json` to send analytics to Plausible.

<Info>
  Do not include `https://` for the domain or server.
</Info>

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "plausible": {
          "domain": "required - your documentation domain",
          "server": "optional - your self-hosted Plausible server URL"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "plausible": {
          "domain": "docs.domain.com"
      }
  }
  ```
</CodeGroup>
