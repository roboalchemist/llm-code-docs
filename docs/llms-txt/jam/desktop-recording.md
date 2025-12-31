# Source: https://jam.dev/docs/record-a-jam/video-screen-recording/desktop-recording.md

# Desktop Recording

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FuuzHPpnseVP0Y70twd9j%2FCleanShot%202023-07-07%20at%2020.54.28%402x.png?alt=media\&token=13849922-3d3a-4b8d-b07d-60df58559fd2)

With Jam, you can record a single tab, an entire window, or your full desktop.&#x20;

When recording a window or your entire desktop, Jam captures console logs and network requests from every tab you interact with during the recording (as long as Jam is installed in that browser window). See steps here to enable Jam on incognito windows:

{% content-ref url="../incognito-sessions" %}
[incognito-sessions](https://jam.dev/docs/record-a-jam/incognito-sessions)
{% endcontent-ref %}

That means, if you're trying to demonstrate a bug that spans across multiple tabs or windows (like something updating in one place but not in another), Jam can record that in real-time. It simultaneously captures console logs and network requests from both tabs, giving engineers a holistic view of the bug even if it's not contained within a single tab.

That way engineers can track a bug through multiple sites, tabs and windows.

## Troubleshooting permissions on Mac

If you are using a Mac and are unable to record your desktop using Jam, follow these steps to fix it:

Step 1: Open your "System Preferences".

Step 2: Open your "Security & Privacy" settings.

Step 3: Click on the "Privacy" tab.

<figure><img src="https://jam.dev/docs/content/images/2023/03/Screen-Shot-2023-03-30-at-9.05.13-PM.png" alt=""><figcaption></figcaption></figure>

Step 4: Select "Screen Recording" from the list.

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FN8j1zBucNGP2kgSHdG6d%2Fimage.png?alt=media\&token=ae109a07-109d-41ef-8609-1554234d1176)

Step 5: If you don't see "Google Chrome" on the list, skip to Step 6. If you see "Google Chrome" on the list, carefully follow the next steps. Remove "Google Chrome" completely from the list. It's important that you completely remove it (not just uncheck the box next to "Google Chrome") using the minus icon.

Step 6: Add "Google Chrome" to the list by using the plus icon.

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FC3MWmvDAiL11Npb46aH9%2Fimage.png?alt=media\&token=1611bfa1-0f7f-46af-9e5c-45d1b1185c20)
