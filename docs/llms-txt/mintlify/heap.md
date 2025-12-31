# Source: https://mintlify.com/docs/integrations/analytics/heap.md

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
