# Source: https://jam.dev/docs/jam-for-customer-support/recording-links/how-to-use-recording-links.md

# How to Use Recording Links

## Creating a Recording Link

#### From the Browser Extension

1. Click on the Jam strawberry to open the extension.\
   ![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2Fgkz0LkaFa2qqrY71hxZ2%2Fimage.png?alt=media\&token=2aa6b641-1c0a-49e9-9e58-ee1d6ae9692a)
2. Click "Create Link".\
   &#x20;![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FvLe56v4bCFDd7ydTfUrw%2Fimage.png?alt=media\&token=96715768-7e08-4f81-9e1f-330eac6beedd)
3. Optionally name your link or paste the URL of your customer conversation (from Zendesk, Hubspot, Jira, etc.).
4. Select "Reusable" if you want to enable multiple recordings from the same link.
5. Click "Create link", the link will be automatically copied to your clipboard, ready for sharing!

#### From the Jam Dashboard

1. Go to [jam.dev/s/recording-links](https://jam.dev/s/recording-links)
2. Click "+ New".
3. A pop-up appears, click "Create Link".
4. Optionally name your link or paste the URL of your customer conversation (for example, Zendesk, Hubspot, Jira).
5. The link will be automatically copied to your clipboard, ready for sharing!

## Sharing Recording Links

Recording links work anywhere you can paste a URL:

* **Email**: "Hi there, can you click this link and show us what you're experiencing? \[recording link]"
* **Support tickets**: Paste directly into Zendesk, Intercom, or HubSpot responses
* **Chat messages**: Slack, Teams, or any messaging platform
* **Customer forms**: Include in help documentation or contact forms

## What Recipients Experience

{% hint style="info" %}
The experience is designed to be accessible to anyone, regardless of their technical background.
{% endhint %}

When someone clicks your recording link:

1. **Instant access** - Opens directly in their browser, no downloads
2. **Simple interface** - Big "Start Recording" button, clear instructions
3. **One-click recording** - Captures their screen, showing the bug
4. **Submit Recording** - Recording uploads and notifies you immediately

## Viewing Recording Links Jams

Recordings from recording links appear in your Jam dashboard as regular Jams:

1. You'll receive an email notification when a Jam from your recording link is submitted
2. Find the recording in your team's Jam dashboard
3. All your integrations work normally - recordings route to Jira, Linear, etc.

## Reusable recording links

Recording links are reusable by default. Reusable recording links are perfect for ongoing customer support or QA workflows, feedback buttons, email signatures, pinned Slack messages, and more!

#### Setting the title of the Jam

You can choose the title of the Jam that is created from your link by adding `jam-title` to the query string.&#x20;

For example, if you want the title of the Jam to be "Shopping cart bug": `https://recorder.jam.dev/QrBnf3s?jam-title=Shopping+cart+bug`&#x20;

Or if it was for a same-domain Recording URL:\
`https://www.your.com/?jam-id=QrBnf3s&jam-title=Shopping+cart+bug`&#x20;

#### Setting other Jam parameters:

You can also use your Recording Link's URL querystring to adjust or override other Recording Links settings:

* `jam-folder=<FOLDER_ID>` — the folder to route the recorded Jam into. Use the 4-character *ID*, not the *name*—on a folder page, the URL looks like: `https://jam.dev/s/<TEAM-ID>/<FOLDER-ID>`
* `jam-reference=<URL_OR_EMAIL>` — a user identifier, or URL (e.g. to an issue tracker, helpdesk conversation, etc)

This is a great use case for when you want to customize link behavior with macros, text expanders, or custom link generators you build for your team.

## Send Recording Links from your own domain and collect console logs

{% content-ref url="../send-recording-links-from-your-own-domain-and-collect-console-logs" %}
[send-recording-links-from-your-own-domain-and-collect-console-logs](https://jam.dev/docs/jam-for-customer-support/send-recording-links-from-your-own-domain-and-collect-console-logs)
{% endcontent-ref %}

## Pro Tips

**Single-use recording links**: Recording links are reusable by default. If you prefer, you can create links that expire after a single use.

**Add a URL to your customer conversation** when you create a recording link, so you will always have know the context when a new recording comes in.

**Universal compatibility**: Recording Links are compatible with the desktop versions of Chrome, Edge, Firefox, and Safari.&#x20;
