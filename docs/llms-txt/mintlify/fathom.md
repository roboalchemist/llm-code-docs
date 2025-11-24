# Source: https://mintlify.com/docs/integrations/analytics/fathom.md

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
