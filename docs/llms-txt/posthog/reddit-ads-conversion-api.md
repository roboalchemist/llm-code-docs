# Source: https://posthog.com/docs/cdp/destinations/reddit-ads-conversion-api.md

# Send PostHog conversion events to Reddit Ads (Conversions API) - Docs

You'll also need access to the relevant Reddit Ads account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.

2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=reddit) tab.

3.  Search for **Reddit Conversions API** and click **\+ Create**.

4.  Find your Reddit Ads Account id on the [Reddit Ads dashboard](https://ads.reddit.com/).

    1.  Click the business name in the top-left
    2.  Click the copy icon next to the Account ID
5.  Back in PostHog, add the Account ID to the destination configuration.

6.  Create a Reddit [Conversion Access Token](https://business.reddithelp.com/s/article/conversion-access-token)

7.  Back in PostHog, add the Conversion Access Token to the destination configuration.

8.  Set up your event and property filters to remove unnecessary events. You only want to send events that are conversions. Filter out unrelated events or ones missing required data.

9.  Press **Create & enable**, test your destination, and then watch your conversions get sent to Snapchat Ads.

## Configuration

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/reddit/template_reddit_conversions_api.py) is available on GitHub.

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