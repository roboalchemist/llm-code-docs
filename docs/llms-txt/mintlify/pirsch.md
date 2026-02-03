# Source: https://www.mintlify.com/docs/integrations/analytics/pirsch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

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
