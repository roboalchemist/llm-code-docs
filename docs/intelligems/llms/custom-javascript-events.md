# Source: https://docs.intelligems.io/analytics/custom-events/custom-javascript-events.md

# Custom JavaScript Events

If you want to track events that are not covered by Intelligems’ built-in custom event types, you can write any custom event using JavaScript. There are two ways to do this:

1. JavaScript custom event managed in Intelligems: this can be set up from the Events Manager. Make sure you leave the event name as-is in the generated code (`javascripteventGVYMQ` in this example):

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5c3f01e24f69fff0f62a37ea34ce8bcd3f229946%2Fimage.png?alt=media" alt="" width="332"><figcaption></figcaption></figure>
2. Events sent directly from your theme code: you can send events using JavaScript directly from your own site code, like this:

```html
<script>
   window.igEvents = window.igEvents || [];
   window.igEvents.push({"event": "myCustomEvent"});
</script>
```

This event will then appear in the Events Manager, where you must register it (acknowledging the event and giving it a name) before you can start using it in experiments.

{% hint style="info" %}
Custom event identifiers can be a maximum of 100 characters long
{% endhint %}
