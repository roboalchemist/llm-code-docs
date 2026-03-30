# Source: https://developers.webflow.com/browser/custom-goals/on-site-conversions.mdx

***

title: On-site conversions
slug: custom-goals/on-site-conversions
description: Track custom conversions that happen on your Webflow site
hidden: false
'og:title': On-site conversions
'og:description': Track custom conversions that happen on your Webflow site
---------------------------------------------------------------------------

On-site conversions track actions that happen on your Webflow site. Use them to measure third party form submissions, dynamic interactions, or any custom user action that other goal types don't capture.

## How on-site conversions work

On-site conversions use the [`wf.sendEvent()`](/browser/custom-goals/on-site-conversions/sendEvent) API to trigger a goal event. When a visitor performs the action you're tracking, the event is recorded and attributed to your optimization.

```javascript
wf.ready(function() {
    wf.sendEvent('demo_form_submitted');
});
```

## Prerequisites

Before tracking on-site conversions, you need to [create a custom goal in Webflow.](https://help-optimize.webflow.com/hc/en-us/articles/41355869779347-Create-or-edit-a-custom-goal)

## Example: HubSpot form submissions

In this example, a visitor fills out a form on your site to request a demo. Assumes you've created a custom goal in Webflow with the event name `demo_form_submitted`.

```html
<!-- Add this to your Page settings Custom Code – before the </body> tag,
     or to an existing trigger in Google Tag Manager -->
<script>
window.addEventListener("message", function (event) {
    if (event.data.type === "hsFormCallback" && event.data.eventName === "onFormSubmitted") {
        window.wf.ready(function() {
            window.wf.sendEvent('demo_form_submitted');
        });
    }
});
</script>
```

## Example: Calendly meeting bookings

In this example, a visitor books a meeting through an embedded Calendly widget. Assumes you've created a custom goal in Webflow with the event name `meeting_booked`.

```html
<!-- Add this to your Page settings Custom Code – before the </body> tag,
     or to an existing trigger in Google Tag Manager -->
<script>
window.addEventListener("message", function (event) {
    if (event.data.event === "calendly.event_scheduled") {
        window.wf.ready(function() {
            window.wf.sendEvent('meeting_booked');
        });
    }
});
</script>
```

## API reference

<Card
  title="sendEvent()"
  href="/browser/custom-goals/on-site-conversions/sendEvent"
  icon={
        <>
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Test.svg" alt="" className="hidden dark:block" />
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Test.svg" alt="" className="block dark:hidden" />
        </>
    }
>
  Client-side API for triggering on-site conversion goals
</Card>
