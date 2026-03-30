# Source: https://posthog.com/docs/cdp/destinations/reddit-ads-pixel.md

# Send PostHog conversion events to Reddit Ads (Pixel) - Docs

You should be aware that this destination relies on creating third-party cookies. You'll also need access to the relevant Reddit Ads account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.

2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=reddit) tab.

3.  Search for **Reddit Pixel** and click **\+ Create**.

4.  Find your Pixel ID in the Reddit [Events manager](https://ads.reddit.com/events-manager). Make sure that the intended business is selected.

5.  Back in PostHog, add the Pixel ID to the destination configuration.

6.  Set up your event and property filters to remove unnecessary events. You only want to send events that are conversions. Filter out unrelated events or ones missing required data.

7.  Press **Create & enable**, test your destination, and then watch your conversions get sent to Snapchat Ads.

## Configuration

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/reddit/template_reddit_pixel.py) is available on GitHub.

### Who maintains this?

This is maintained by PostHog. If you have issues with it not functioning as intended, please [let us know](https://us.posthog.com/#panel=support%3Asupport%3Aapps%3A%3Atrue)!

### What if I have feedback on this destination?

We love feature requests and feedback. Please [tell us what you think](https://us.posthog.com/#panel=support%3Afeedback%3Aapps%3Alow%3Atrue).

### What if my question isn't answered above?

We love answering questions. Ask us anything via [our community forum](/questions.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better