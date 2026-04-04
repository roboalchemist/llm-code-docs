# Source: https://clickwrap-developer.ironcladapp.com/docs/troubleshooting-verifying-calls-are-being-made.md

# Troubleshooting ps.js API Calls

> 🚧 HTTPS is Required
>
> HTTPS is required to send events from the snippet to Ironclad Clickwrap. While developing locally, you'll need to ensure that your connection is over SSL in order to see test activity in your Ironclad Clickwrap Site.

## Testing Ironclad Clickwrap calls in PS.js with Console

To ensure your PS.js calls are going through, you can easily pop open your Developer Console to see calls happening in real-time. There are two types of ways you can interact with PS.js to track what's happening:

* Easily enable debugging using \_ps.debug = true; (outlined [here](https://clickwrap-developer.ironcladapp.com/docs/debugging-the-javascript-in-pactsafe))
* Use one of the [Triggered Events](https://clickwrap-developer.ironcladapp.com/reference/triggered-events-1) to send notifications/arguments to your console like so:

```javascript
_ps.on('all', function(){
  // will log all Ironclad Clickwrap events to your console
  // with the arguments from each
  console.log(arguments);
});
```

Will yield some awesome debugging results you can see from your Dev Console:

<Image title="Screen Recording 2017-12-19 at 04.22 PM.gif" alt={956} src="https://files.readme.io/74c28f9-Screen_Recording_2017-12-19_at_04.22_PM.gif">
  See details of every event fired from Ironclad Clickwrap's PS.js so you can integrate it exactly like you want to.
</Image>

Here's the updated JSFiddle with exactly what you need to see:

## Testing Ironclad Clickwrap calls using the Network pane of Chrome Developer Tools

When testing that your page is actually interacting with the Ironclad Clickwrap API, you can pop open your developer tools and head to the Network panel to inspect calls being made in real-time to [https://pactsafe.io.](https://pactsafe.io.) You'll see a couple of calls being made:

When the Signer ID is set, you'll see two calls being made to Ironclad Clickwrap:

* a call to `/retrieve` which [grabs the version IDs](https://clickwrap-developer.ironcladapp.com/docs/get-the-latest-versions-signed) for contracts in your Group accepted for a Signer.
* a call to `/send` which automatically send a `displayed` event to Ironclad Clickwrap to track that a particular Signer has, in fact, seen the agreement/click-through checkbox.

<Image title="CloudApp Annotation 2017-12-19 at 2.59.15 PM.png.png" alt={2560} src="https://files.readme.io/0e60655-CloudApp_Annotation_2017-12-19_at_2.59.15_PM.png.png">
  You can easily explore the Network pane of your console to track what's being sent to Ironclad Clickwrap in real-time.
</Image>

> 📘 When are events sent to Ironclad Clickwrap?
>
> Unless you use `disable_sending: true` in your `_ps('create')` call, events will be sent to Ironclad Clickwrap when:
>
> * Signer ID is set (by either listening to a field `<input>` or using `_ps('set', 'signer_id', email);` — a `displayed` event should be sent as well as a retrieve will be done to get contract IDs and version IDs of contracts already accepted by the Signer (`null` if they haven't been accepted yet).
> * When checking the box, an `agreed` event will be sent to Ironclad Clickwrap using [https://pactsafe.io/send](https://pactsafe.io/send) as outlined [here](https://clickwrap-developer.ironcladapp.com/docs/send-contracts-signedaccepted-by-signer)
> * Optionally, you can choose to send a `disagreed` event when a Signer *unchecks* your click-through agreement.