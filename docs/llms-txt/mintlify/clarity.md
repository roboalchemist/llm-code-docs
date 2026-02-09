# Source: https://www.mintlify.com/docs/integrations/analytics/clarity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

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
