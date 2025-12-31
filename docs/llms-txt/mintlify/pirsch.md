# Source: https://mintlify.com/docs/integrations/analytics/pirsch.md

# Pirsch

> Track privacy-focused analytics with Pirsch.

Add the following to your `docs.json` file to send analytics to Pirsch.

You can get your site ID from Settings > Developer > Identification Code.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "pirsch": {
          "id": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "pirsch": {
          "id": "8Kw7OKxBfswOjnKGZa7P9Day8JmVYwTp"
      }
  }
  ```
</CodeGroup>
