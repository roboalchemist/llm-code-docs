# Source: https://www.mintlify.com/docs/integrations/analytics/fathom.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fathom

> Track documentation analytics with Fathom.

Add the following to your `docs.json` file to send analytics to Fathom.

You can get the `siteId` from your script settings.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "fathom": {
          "siteId": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "fathom": {
          "siteId": "YSVMSDAY"
      }
  }
  ```
</CodeGroup>
