# Source: https://jam.dev/docs/record-a-jam/video-screen-recording.md

# Video Screen Recording

You can use Jam to quickly record a video of your screen – along with all the technical details engineers need to troubleshoot and fix bugs.

Unlike other screen recording tools, Jam's video recorder is purpose-built for product, engineering, support, and QA teams to aid in capturing bugs while automatically including all the technical details engineers require to address and fix them.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FO1048cQEYtyOSjBDB48o%2FTab-recording.gif?alt=media&#x26;token=38c17188-c178-497d-9a69-c729a6fa687e" alt=""><figcaption></figcaption></figure>

When you record a video of your screen with Jam, Jam captures the following technical diagnostics and auto-includes them to help your engineers debug faster:

* Console logs
* Fully inspectable network requests
* URL
* Timestamp & country
* Device, OS, Browser
* Viewport size
* Network speed

And packages it all into one easy link to be shared with an engineer or pasted into a ticket.

## Voiceover Recording

When you record a video with Jam, you can optionally choose to record a voiceover for your videos. This helps in providing real-time explanations and context for the activities happening on the screen.

Then you can mute and un-mute your microphone and choose which microphone Jam should use to record your audio.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FSNWQvm5BdQppM30UP2rq%2FMic-controls.gif?alt=media&#x26;token=44ab7be5-9b36-49c9-ad34-e56c6d82e76a" alt=""><figcaption></figcaption></figure>

### Microphone permission

To use the microphone, you will need to have the correct permissions in your browser. You will be prompted to grant access the first time you try to use microphone.

If you have previously denied microphone access, you can modify it in the browser extension settings:

1. Go to extension site settings - copy and paste this URL in your search bar: <kbd>chrome://settings/content/siteDetails?site=chrome-extension://iohjgamcilhbgmhbnllfolmkmmekfmci</kbd>
2. In the permission list, select “Allow” for microphone permission

## Tab vs Desktop Recording

With Jam, you can record a single tab, an entire window, or your full desktop.&#x20;

<div align="left" data-full-width="false"><figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FoQuHkqZfbdP2yknXFr1a%2FTabvsDesktop.gif?alt=media&#x26;token=0f385753-e91d-4bf1-91d6-a3dfe28fdfdf" alt=""><figcaption><p>Switching between tab and desktop recording</p></figcaption></figure></div>

When you record a single tab, Jam only captures what's literally in that tab. That means Jam does not capture the browser URL bar, or any new windows (e.g. for login flows) that pop up external to the tab.

When you record a window or your entire desktop with the "Record desktop" option, Jam records the full scope of that window/monitor – including the browser URL bar.

Because Jam is purpose-built to help engineers understand bug reports at a glance, when you choose the "Record desktop" option, Jam will auto-include console logs and network requests from every tab you interact with during the recording (as long as Jam is installed in that browser window).&#x20;

That means, if you're trying to demonstrate a bug that spans across multiple tabs or windows (like something updating in one place but not in another), Jam can record that in real-time, and give engineers a holistic view of the bug even if it's not contained within a single tab. That way engineers can track a bug through multiple sites, tabs and windows.&#x20;

### Recording incognito tabs

Jam offers full support for incognito. See steps here to enable Jam on incognito windows:

{% content-ref url="incognito-sessions" %}
[incognito-sessions](https://jam.dev/docs/record-a-jam/incognito-sessions)
{% endcontent-ref %}
