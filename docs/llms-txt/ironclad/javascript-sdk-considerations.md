# Source: https://clickwrap-developer.ironcladapp.com/docs/javascript-sdk-considerations.md

# General Considerations

Before getting started with implementing the Ironclad Clickwrap JavaScript SDK, you may want to consider some of the following topics outlined on this page.

While we aim to make our JavaScript SDK as easy to use for integrating standardized terms, there are some special considerations you should know before you begin implementation.

## Asynchronous Sending

This is an **extremely important** consideration when implementing our library in workflows where contracts absolutely need to be accepted before a person(s) moves forward in your workflow. In short, you'll need to implement features to ensure that Ironclad Clickwrap receives acceptance if your workflow requires it.

While we won't cover the concept of asynchronous vs. synchronous in JavaScript within this guide, there are many wonderful (and highly detailed) resources on the Internet explaining when and how to use it. One example can be found here: [https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous).

That being said, during your implementation of the Ironclad Clickwrap JavaScript SDK, be sure to utilize the callback feature available on all `send` calls or use the `valid` or `invalid` triggered events.

### Callback Method

For example, when sending acceptance, I might use something like the following in my implementation:

```javascript
// Where my Clickwrap group key is example-group
_ps('example-group:send', 'agreed', {
  event_callback: function() {
    console.log('Finished sending!');
  }
});
```

### Sent Event

Our JavaScript Library also provides a `sent` event notification when a send call is made. You can check the `eventType` to see the type of event that was sent and handle it accordingly.

One thing to keep in mind, the `sent` event can be triggered regardless if the API call is made or not. When you disable automatic sending by setting `disable_sending` to `true` when configuring the Site or Group objects, then the `sent` will still be triggered even though the API doesn't receive the event.

```javascript
_ps.on('sent', function(eventType, params, context, payload, batchId) {
  if(eventType === 'agreed') console.log('An agreed event occurred!');
});
```

## Client-side Data Capture and Server-side Sending

The Ironclad Clickwrap JavaScript SDK can make embedding terms much easier into your environment, especially with the pre-built styling and available customizations we offer. But, we know some customers want greater control of sending acceptance data from their own backend, which may be beneficial depending on your volume and security needs.

Accomplishing this is relatively easy with a couple of methods available in the SDK and using our Activity API.

For example, once the user has accepted the terms (perhaps you know this with the `valid` triggered event offered), you can grab the payload typically sent from the SDK with the following:

```javascript
// Assuming we have one Clickwrap Site and one group loaded
// as there are multiple ways of getting the payload.

// Simple call to get URL Encoded parameters.
const myPayload = _ps.site.group.getPayload();

// Now that I have the params from the previous payload,
// I can send an Agreed event with associated data to the API.
fetch('https://pactsafe.io/send?et=agreed' + '&' +  myPayload)
  .then(response => response.json())
  .then(data => console.log(data));
```

More detailed information on achieving this can be located on the [Using PS.js with back-end API calls](https://clickwrap-developer.ironcladapp.com/docs/using-psjs-with-back-end-api-calls) page.