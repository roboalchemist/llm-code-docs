# Source: https://www.mintlify.com/docs/integrations/analytics/heap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Heap

> Track user interactions with Heap analytics.

Add the following to your `docs.json` file to send analytics to Heap.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "heap": {
          "appId": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "heap": {
          "appId": "1234567890"
      }
  }
  ```
</CodeGroup>
