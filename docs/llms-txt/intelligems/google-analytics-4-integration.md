# Source: https://docs.intelligems.io/integrations/google-analytics-4-integration.md

# Google Analytics 4 Integration

## Overview

The Intelligems Google Analytics integration allows you to analyze experiment results within GA4. Once enabled, we’ll send an event to GA on each page load indicating the active experiment(s) and test group(s) for the visitor. You can then use this dimension to segment users in GA4.

## How it Works

Once you’ve enabled the Intelligems GA4 integration, Intelligems will begin sending an event called `experience_impression` to GA4 on each page load, with one event for each active experiment. Intelligems attaches a dimension to the event, `Experience - variant ID`, which contains the name of the experiment and test group this visitor was in, in the following format:

```
IG - <Experiment Name> - <Test Group Name>
```

## Enabling the Intelligems <> GA4 Integration

Enabling the integration takes only 1-2 minutes:

1. In the Intelligems app, click on the “Integrations” tab in the lower left section of the side nav, or navigate [to the integrations page](https://app.intelligems.io/integrations) directly in your browser.
2. Within the “Google Analytics 4” section, click “Sign in with Google.” You’ll need to sign in with a Google account that has access to your GA4 account, and sufficient permissions to authorize Intelligems.\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-d462ae7aa4da9e367d9d0bc4e941c11f4e3076f5%2Fsign_in_with_google.png?alt=media" alt=""><figcaption></figcaption></figure>
3. In the new Google window, click “Allow.” You may see a checkbox asking if you’d like to enable specific permissions - if so, check it off.\
   \
   ![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bdb99c396070abb32f637ec39eeb3e30851a53d9%2Fgoogle_popup.png?alt=media)\\
4. Choose the stream you’d like Intelligems to send the data to. If you're unsure, follow the steps [here](#finding-your-ga4-measurement-id) to find your measurement ID.

## Analyzing Experiments in GA4

To analyze experiment data within GA4, create a segment for each test group:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0f873c3a68a6b81704cc622ff77e80d31ca37d45%2FGA4%20Segment.gif?alt=media" alt=""><figcaption><p>Creating a user segment in GA4</p></figcaption></figure>

1. [Create a new segment](https://support.google.com/analytics/answer/9304353?hl=en#zippy=%2Cin-this-article). From within an exploration, click the “+” button next to Segments.
2. Choose “User Segment”.
3. Add a dimension to condition on, and choose “Experience - variant ID”.
4. Choose “contains,” and find the test group you’re interested in analyzing (the pattern will follow the one detailed in the “How it Works” section above, and should autocomplete). Check off “at any point in time”.
5. Click "Save and Apply" to save the segment. You can also create an Audience from the segment so that you can re-use it in other reports.

## Additional Settings

If you would like Intelligems to add the event to the `window.dataLayer` instead of using `window.gtag`, add this snippet above the Intelligems script in your `theme.liquid`:

```html
<script>
  window.igSettings = {
    useDataLayer: true
  }
</script>
```

If you choose to use this mode, you will most likely need to route the Intelligems GA4 event to GA4 using a Google Tag Manager tag. Follow our step-by-step instructions to set that up [here](https://docs.intelligems.io/integrations/google-analytics-4-integration/integrating-with-ga4-using-google-tag-manager).

## Troubleshooting

### There is not any Intelligems data in GA4

* Make sure the GA4 integration is enabled in the [Intelligems app](https://app.intelligems.io/integrations)
* Note that data is sent only for active experiments, and only after the integration has been enabled. **Data won't be sent retroactively for experiments** that have already ended when the integration was first enabled
* Make sure Intelligems and your Google Analytics scripts are both being loaded
* Ensure [window.gtag](https://developers.google.com/tag-platform/gtagjs) is available on your store. Intelligems uses GA's gtag API to send events. You can check this by loading your store in your browser and checking for window\.gtag in the console
* Make sure the stream and property chosen in the integration was correct (see above for instructions on how to check this)

### There are fewer visitors tracked in my GA4 segments than in Intelligems analytics

Not every visitor to the experiment may be tagged with their test group in Google Analytics. Intelligems triggers the `experience_impression` event almost immediately after loading, but GA often delays sending it to its server for a few seconds. This causes visitors who bounce quickly to be tracked in Intelligems, but not to be tagged in GA with their test group. It's common to see the number of visitors in GA4 segments \~80-90% of the number in Intelligems analytics. If you're seeing fewer than that, here are some things to check:

* Ensure you've [installed Intelligems directly](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) rather than using the Shopify app embed. The app embed loads Intelligems asynchronously, which may delay the triggering of the `experience_impression` GA event
* Check the users that are not tagged with an Intelligems test group, and make sure they are real users by checking browsing behavior, time on site, and attributed revenue and orders. There are a number of different reasons GA will "make up" visitors
* If you use the measurement ID in your Google tag is not the same as the one you've chosen in Intelligems, it may help to initialize that measurement ID directly. For example, if your GA4 measurement ID is `G-1234567890` and your Google tag looks like:\\

  <pre class="language-html" data-full-width="true"><code class="lang-html">  &#x3C;!-- Google tag (gtag.js) -->
    &#x3C;script async src="https://www.googletagmanager.com/gtag/js?id=AW-987654321">&#x3C;/script>
    &#x3C;script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

  <strong>    gtag('config', 'AW-987654321');
  </strong>  &#x3C;/script>
  </code></pre>

  \
  Adding a `config` line for your measurement ID `G-1234567890` may help ensure Intelligems events are sent successfully:\\

  <pre class="language-html" data-full-width="true"><code class="lang-html">  &#x3C;!-- Google tag (gtag.js) -->
    &#x3C;script async src="https://www.googletagmanager.com/gtag/js?id=AW-987654321">&#x3C;/script>
    &#x3C;script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

  <strong>    gtag('config', 'AW-987654321');
  </strong><strong>    gtag('config', 'G-1234567890');
  </strong>  &#x3C;/script>
  </code></pre>

### There are too many or too few orders & revenue compared to Intelligems analytics

Intelligems' order data comes directly from Shopify through server-side events. When order totals and revenue differ significantly between Intelligems and GA4, this is usually a problem with how your Shopify <> GA4 integration is configured. To diagnose the issue, you can download order exports from the Intelligems dashboard, and compare the included orders to order IDs In Google Analytics, by creating a GA4 report with order ID as a dimension.

We also recommend reaching out to a tracking specialist who can take a look at your GA4 setup. You can visit or [partners page](https://www.intelligems.io/company/partnerships) for experts.

## Finding your GA4 Measurement ID

1. Go to Google Analytics and navigate to the Admin section.\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-007a17b7b380e2e47d5c2ae050e33f7cf81ff401%2Fga41.png?alt=media" alt="" width="532"><figcaption></figcaption></figure>
2. In the menu under “Property Settings,” choose “Data Streams”.\
   ![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-4e1526d37e666f70c5a00e5ff654e28dd67ab4ba%2Fga42.png?alt=media)\\
3. Click on the stream associated with your online store. In many cases, there may be only one stream.\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-08358aab30dc915e02327bdd27d0243a770203eb%2Fga43.png?alt=media" alt=""><figcaption></figcaption></figure>
4. The measurement ID will appear in the drawer. It usually starts with “G-”.\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f2989868f0a64d5b7ea4e8daeacbbf962b2f9ea7%2Fga44.png?alt=media" alt=""><figcaption></figcaption></figure>

####
