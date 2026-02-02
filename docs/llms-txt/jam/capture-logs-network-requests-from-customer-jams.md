# Capture logs, network requests from Customer Jams

{% hint style="info" %}
Note: This version of Jam.js is for our Intercom Integration. For installing Jam.JS with Recording Links, see [recording-links](https://jam.dev/docs/jam-for-customer-support/recording-links "mention").
{% endhint %}

Here’s a preview of what you’ll get with every support ticket:

![Jam Example GIF](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F6ol6fzRyWZkoCCYedqZP%2FJam-for-csup-example.gif?alt=media&#x26;token=c99ee82d-bf61-4537-8270-0e91872d15c1)

## How to set up Jam.js?

> *Installing Jam.js takes under 5 min guaranteed, and if it takes you a second longer, we'll buy you a pizza. 🍕*

### Step 1: Go to [jam.dev](http://jam.dev) and select the team where you want your Jams from Intercom to appear.

### Step 2: Copy the team ID from the URL

![Jam Team ID GIF](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2Fh1lCn3GssusL2ZyXMZqS%2Fjam-for-csup-team-id.gif?alt=media&#x26;token=a186aeb7-1113-4722-966f-a9c35b48d049)

### Step 3: Add the team ID to this code snippet

```javascript
<script async defer src="https://js.jam.dev/support/<team ID here>.js"></script>
```

### Step 4: Paste the snippet into your web app's codebase

In order to guarantee jam.js can properly capture console and network requests, it should be the first `<script>` tag on the page.

For example, here’s where the jam.js script would go in an example template HTML file for a Single Page App:

```html
<html>
    <head>
        <!-- PASTE JAM.JS SCRIPT TAG HERE -->
    </head>
    <body>
        <div id="root"></div>
        <script src="/app.js"></script>
    </body>
</html>
```

Because we include the `async` and `defer` tags within the script snippet, fetching the jam.js script will not impact page load times.

### Step 5: Modify CSP (if your site has this enabled)

*(If your site does not specify CSP directives, you can skip this step.)*

Some sites specify [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) directives via either a header or meta tag.

A frame-src or script-src directive that doesn't include `*.jam.dev` will block Jam.js from including console logs with your user's Jams.

To fix this, modify your CSP header or meta tag to allow `*.jam.dev` as both:

* `frame-src`
* `script-src`

## How to test jam.js?

Once jam.js is installed, every Jam your users create will have console logs and network requests attached.

To test this out, issue a screen recording request, and begin recording your web app.

Open devtools for your web app, and run the following test commands in console:

```javascript
console.log('test'); // this creates a console log
fetch('/test'); // this creates a network request
```

![Test Request GIF](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F6UR24Py01fEg9iQQEzm4%2Fimage.png?alt=media&#x26;token=c4c9f803-4ac3-429a-ab8c-08dee90384ea)

Now, you should have console and network events generated and captured for your recorded Jam.

To confirm, submit the Jam, then open its link and click on the **Console** and **Network** tabs. Your Jam should include at least 1 console and network event, each.

Here’s how this might look:

![Console and Network Events GIF](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FkoVBhbxiXFxAc8upMzWU%2Fimage.png?alt=media&#x26;token=623ccb8c-ec64-453e-ada6-6f97820ef712)

## **Jam.Metadata**

With one additional function call, `jam.metadata()`, you can ensure that every Jam submitted from your website includes the metadata you need to debug the bug. You can log anything in Jam.Metadata: simple static values like User ID, to any data like redux or react state. Whatever you need to debug, just send it to Jam.Metadata so it's always there for you in any ticket. More information can be found [here](https://jam.dev/docs/debug-a-jam/devtools/jam.metadata).

![Metadata GIF](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FGPfHwMV2EMFr1CMP7cWD%2Fimage.png?alt=media&#x26;token=b1ffff5f-93a2-45d5-965d-31694dc7ab7d)