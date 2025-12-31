# Source: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/warp-drive-on-the-web.md

# Warp Drive on the Web

## What is Warp Drive on the Web?

Warp now gives developers the ability to view their drives and shared sessions on the browser.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-52d21001e932c73386278e1b2620eab6d6458e3f%2FScreenshot%202024-07-23%20at%2012.54.16%E2%80%AFPM.png?alt=media&#x26;token=c5fd5e2f-5670-4861-beae-d12a8c019924" alt="" width="375"><figcaption><p>A web-based rendering of a Team Workflow</p></figcaption></figure>

## Accessing Warp Drive on the Web

Warp's web-based viewing experience can currently be accessed via:

* The [`app.warp.dev/app` homepage](https://app.warp.dev/app)
* [Drive Object](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/..#sharing-your-drive-objects) Links
* [Session Sharing](https://docs.warp.dev/session-sharing#how-to-allow-access-to-collaborators-in-your-session) Links

{% hint style="warning" %}
You should be able to edit and view web-based objects and session as normal. The one exception is executing a command from a workflow or notebook since there is no shell session running on the web.
{% endhint %}

## Managing Your View Preferences - Web or Desktop

If the Warp app is installed, links will open on the desktop by default. You can manage whether Warp links open in Warp's desktop app or the browser in multiple ways:

{% hint style="info" %}
The desktop option is only presented if Warp's web service is able to detect the Warp app installed locally. Warp desktop opens localhost port 9277 to accomplish this detection. This is done in a separate process that does not have access to your terminal contents.\
\
If you would like to use Warp locally and do not have it installed, please visit our [installation guide.](https://docs.warp.dev/getting-started/readme)
{% endhint %}

1. The first time you follow a link, if Warp is not installed, you will be prompted to download it. You can dismiss the popup to stay on the web.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-6c15d2ac9052fa75752d817b0a66102fd511537b%2FScreenshot%202024-07-11%20at%2010.07.22%E2%80%AFAM.png?alt=media&#x26;token=af7e48ac-8d2b-4ec2-98d8-f94a3cd49102" alt="" width="563"><figcaption></figcaption></figure>

2. This preference can be changed at any point in *Settings > Features > General > Open links in desktop app.* Note that this setting is only available while on the web-based version of Warp.

   <figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-b94827a5b83e6d43952114c6914880293523040d%2FScreenshot%202024-07-23%20at%201.09.06%E2%80%AFPM.png?alt=media&#x26;token=69d7080f-8545-4294-a8e1-788ee3f75acc" alt="" width="563"><figcaption><p>Setting managing how to open links</p></figcaption></figure>
3. You can always switch between web and desktop views on a case-by-case basis.
   1. To switch from a web-view to Desktop for a given object, open the *overflow menu > Open link on Desktop.*

      <figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-2d8b447362bf1656dc81ae9fb8e5773ad6990423%2FScreenshot%202024-07-23%20at%201.10.58%E2%80%AFPM.png?alt=media&#x26;token=a9c0cf0e-c280-4f86-86a5-7f70b9f2a05b" alt="" width="563"><figcaption></figcaption></figure>
   2. To stay on the web for a given object despite a global Desktop preference, follow the *View on the web* option that is part of the redirect screen to Desktop.

      <figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-43d213d98c824a9f6282d57dd026329fee7cf746%2FScreenshot%202024-07-23%20at%201.11.20%E2%80%AFPM.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

## Supported Browsers

Modern browser support currently includes

* Chrome
* Firefox
* Safari
