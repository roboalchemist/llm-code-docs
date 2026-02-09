# Source: https://www.mintlify.com/docs/integrations/analytics/mixpanel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mixpanel

> Track product analytics and user behavior with Mixpanel.

Add the following to your `docs.json` file to send analytics to Mixpanel.

```json Analytics options in docs.json theme={null}
"integrations": {
    "mixpanel": {
        "projectToken": "YOUR_MIXPANEL_PROJECT_TOKEN"
    }
}
```

Replace `YOUR_MIXPANEL_PROJECT_TOKEN` with your Mixpanel project token. You can find this in your [Mixpanel project settings](https://mixpanel.com/settings/project).

## Tracked events

Mintlify automatically tracks the following user interactions:

* Page views
* Search queries
* Feedback submissions
* Context menu interactions
* Navigation clicks

If you're not seeing events in Mixpanel, ensure your project token is correct and that no content security policies are blocking the Mixpanel script.
