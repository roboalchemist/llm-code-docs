# Source: https://mintlify.com/docs/integrations/analytics/plausible.md

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
          "domain": "required",
          "server": "optional"
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
