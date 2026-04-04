# Source: https://www.mintlify.com/docs/integrations/analytics/segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment

> Send analytics events to Segment and downstream tools.

Add your Segment write key to your `docs.json` file to send analytics to Segment.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "segment": {
          "key": "required",
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "segment": {
          "key": "nqJxiRG15Y6M594P8Sb8ESEciU3VC2"
      }
  }
  ```
</CodeGroup>
