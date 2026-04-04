# Source: https://posthog.com/docs/libraries/google-tag-manager.md

# Google Tag Manager - Docs

[Google Tag Manager](https://marketingplatform.google.com/about/tag-manager/) helps you add code snippets or tracking pixels to your website in a low-code way to send data to services like marketing and analytics tools.

It is an easy way to integrate PostHog into your website without having to update your codebase.

## How to add PostHog to Google Tag Manager

1.  Get your [PostHog snippet](/docs/getting-started/install?tab=snippet.md) with your project token and instance address from [your project settings](https://us.posthog.com/settings/project).

2.  Assuming you have already set up Google Tag Manager, go to your [dashboard](https://tagmanager.google.com/) and navigate to the desired account/container that is integrated with the website you want to add PostHog tracking to.

3.  Click to add a new tag:

4.  Under **Tag Configuration**, choose **Custom HTML** and add your PostHog snippet.

5.  For the trigger, select the default **All Pages - Page View** trigger and then click **Save**.

6.  Back on the main dashboard, click **Submit** to update your website with the new PostHog tag.

7.  You're done! PostHog is now added to your site and autocapturing data like pageviews and clicks.

> To confirm PostHog is configured correctly, visit your website and then check if the events from your session appear in [the activity tab](https://us.posthog.com/activity/explore). It may take a few minutes for events to appear.

## Using all the features of PostHog via Google Tag Manager

PostHog works the same via Google Tag Manager as it does via our snippet directly. This means you can use all of the features like session replays, surveys, and more without additional setup.

Some of these do require calling PostHog, which you can do by checking for the window's `posthog` object and calling any of its methods. For example, you can capture a custom event like this:

HTML

PostHog AI

```html
<script>
  (function waitForPosthog() {
    if (window.posthog) {
      window.posthog.capture('hello');
    } else {
      setTimeout(waitForPosthog, 100);
    }
  })();
</script>
```

You can find the full list of methods in our [JavaScript Web docs](/docs/libraries/js/features.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better