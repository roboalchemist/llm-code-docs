# Source: https://jam.dev/docs/record-a-jam/instant-replay/privacy.md

# Privacy

## How does Instant Replay work?

Instant Replay keeps track of HTML changes in the website you are on, by periodically snapshotting the DOM.

The snapshots are stored locally on your computer until you create a Jam. At that point, Jam stitches together the DOM snapshots to look like a video (but if you inspect it, you'll find it's just replaying HTML inside an iframe).

It's actually not a video recording - just HTML. That way, Jam Instant Replay is not recording a video of your screen, just keeping track of the HTML changes of webpages and then re-rendering the HTML to create a "video". This is just like how the browser saves a snapshot of web pages you visit in local storage so they are faster to open if you visit them again. So there's no video recording even locally on your computer.

## How does Instant Replay preserve my privacy?

Instant Replay is built for privacy first - everything is done locally on your computer, nothing leaves unless you explicitly share it, and the local buffer is permanently deleted every 120 seconds.&#x20;

The snapshots are stored on your computer in your browser's local storage until you create a Jam. Only once you explicitly click "Create" and create a Jam, the snapshots are uploaded to our infrastructure so that you can share your rewind as a link or ticket. All of the snapshots and computing is done offline, locally in your computer browser’s local storage, until you explicitly choose to share.

## How to disable Instant Replay

You can remove Instant Replay from Jam anytime from the extension settings:

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2Fw8K5HLo7JSXdLcx8BRqW%2Fdisable-ir.gif?alt=media\&token=0336e48d-d8da-4a1c-9b42-8a9b0d681de6)

You can also turn off Instant Replay for specific websites:

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FNRdIPObyTR4MMrb81a23%2Fdisable-ir-site.gif?alt=media\&token=c46198f9-e13a-473c-a84e-f0c816bf4f44)
