# Source: https://www.mintlify.com/docs/integrations/analytics/google-tag-manager.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Tag Manager

> Manage analytics tags and events with Google Tag Manager.

Add your tag ID to `docs.json` file and we'll inject the Google Tag Manager script to all your pages.

You are responsible for setting up cookie consent banners with Google Tag Manager if you need them.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "gtm": {
          "tagId": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "gtm": {
          "tagId": "GTM-MGBL4PW"
      }
  }
  ```
</CodeGroup>
