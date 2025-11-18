# Source: https://mintlify.com/docs/integrations/analytics/clarity.md

# Clarity

> Track user sessions with Microsoft Clarity analytics.

Add the following to your `docs.json` file to send analytics to Microsoft Clarity.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "clarity": {
          "projectId": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "clarity": {
          "projectId": "abc123xyz"
      }
  }
  ```
</CodeGroup>

## Get your project ID

1. Create a [Clarity account](https://clarity.microsoft.com/projects).
2. Click **Get tracking code.**
3. Copy your project ID from the tracking code.
