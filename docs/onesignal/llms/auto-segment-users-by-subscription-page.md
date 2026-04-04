# Source: https://documentation.onesignal.com/docs/en/auto-segment-users-by-subscription-page.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Track web push subscriptions by page topic

> Learn how to automatically tag Web Push subscribers based on the page they opted in from and use those tags to create segments or trigger automated messaging campaigns in OneSignal.

## Automatically tag and target Web Push subscribers by page

You can deliver more personalized and timely push notifications by tagging users based on the specific page or content they subscribed from. In this guide, you'll learn how to:

* Use the [`subscriptionChange`](./web-sdk-reference#addeventlistener-push-subscription) event to detect Web Push opt-ins
* Apply [custom data tags](./add-user-data-tags) when a user subscribes
* Segment users by tag for targeted campaigns
* Automate messaging sequences based on tag and timing

***

## Setup

### 1. Tag users with page-specific metadata

Once a user subscribes to push notifications, you can tag them with contextual data—such as the page type or topic they were viewing. This enables targeted follow-ups based on what the user showed interest in.

```javascript  theme={null}
// Example: Tag users subscribing on a sports-related page
let page_topic = 'sports'; // You can also dynamically extract this from DOM or metadata

OneSignal.push(function() {
  OneSignal.on('subscriptionChange', function(isSubscribed) {
    if (isSubscribed === true) {
      console.log('The user subscription state is now:', isSubscribed);

      // Example: Extract "gaming" from "/gaming/article-123"
      var pathArray = window.location.pathname.split('/');

      OneSignal.User.addTags({
        "subscription_page": pathArray[1],
        "subscription_page_topic": page_topic,
      }).then(function(tagsSent) {
        console.log('Tags sent:', tagsSent);
      });
    }
  });
});

```

**How this works:**

* The `subscriptionChange` event fires when a user's subscription status changes.
* If `isSubscribed === true`, the user has just opted in.
* `window.location.pathname.split('/')[1]` captures the first segment of the page path as the subscription context.
* `page_topic` can be dynamically set based on your page’s metadata or content.

Example: If the URL is `https://example.com/gaming/article123`, the `subscription_page` tag will be `gaming`.

### 2. Segment users by tag

Once tags are applied, you can use [Segments](./segmentation) or [API Filters](/reference/create-message#filters) to target users based on those tags.

For example:

* Send a campaign to users where `subscription_page` is "gaming"
* Create dynamic segments based on tag values and timing (e.g., hours since first session)

### 3. Automate follow-up messaging

You can build drip-style campaigns that trigger messages based on when the user subscribed and what content they subscribed under.

**Example**: Drip campaign for gaming subscribers

| Segment Name | Filters                                                           | Description                             |
| ------------ | ----------------------------------------------------------------- | --------------------------------------- |
| Gaming 1     | `subscription_page` = `gaming` AND First Session > 2h AND \< 24h  | Reach out 2–24 hours after subscription |
| Gaming 2     | `subscription_page` = `gaming` AND First Session > 24h AND \< 48h | Follow up 1 day later                   |
| Gaming 3     | `subscription_page` = `gaming` AND First Session > 72h AND \< 96h | Final check-in after 3 days             |

<Info>
  Use upper time limits (`<`) to prevent users from lingering in segments once the messaging window has passed.
</Info>

***

### 4. Combine segments with message templates

Once segments are created:

* Build [Templates](./templates) for each stage in the campaign (e.g., intro, reminder, promo).
* Use [Journeys](./journeys-overview) to send these messages when users enter the appropriate segment.

**Example message ideas:**

* Invite to a gaming community or social group
* Recommend trending articles related to their topic
* Send an exclusive offer or discount code

***

## Best practices and gotchas

* Use meaningful tag names and values that reflect actual user intent
* Extract tag values dynamically if possible, e.g.:

```javascript  theme={null}
let page_topic = document.querySelector('meta[name="article-topic"]')?.content || 'general';
```

* Monitor tagging success via `console.log()` or browser dev tools

Avoid:

* Re-tagging users unnecessarily on every page load (only tag when subscription is new)
* Including PII in tags (e.g., name, email)
* Hardcoding tag values across your entire site

***

<Check>
  Congrats on enriching your user data with contextual information!
  Additional resources:

* [Data Tags](./add-user-data-tags)
* [Web SDK Reference](./web-sdk-reference)
* [Journeys](./journeys-overview)
* [Segments](./segmentation)
</Check>

***

Built with [Mintlify](https://mintlify.com).
