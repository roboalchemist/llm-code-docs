# Source: https://docs.firehydrant.com/docs/triage-channels-in-slack.md

# Triage Channels in Slack

Triage channels allow your colleagues in Slack to ask if something is amiss. For example, your support team may ask the question "Hey, is production having issues with logging in users?" – If your engineering team is already working on this incident, and has an active FireHydrant incident open, then triage channels are for you.

## Enabling Triage Channels

<Embed url="https://www.youtube.com/watch?v=spus2mGwErY" title="FireHydrant - Slack Triage Channels" favicon="https://www.youtube.com/favicon.ico" image="https://i.ytimg.com/vi/spus2mGwErY/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=spus2mGwErY" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252Fspus2mGwErY%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253Dspus2mGwErY%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252Fspus2mGwErY%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22640%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

<br />

You can either create or use an existing Slack channel for triage channels. There are some prerequisites, though:

1. The FireHydrant Bot must be in the channel (type `/add app` in Slack and select "Add apps to this channel"
2. The channel must not be an incident channel
3. AI Summaries must be enabled in your FireHydrant account

### Steps to enable

Type `/fh channel` in the channel you'd like to enable automatic replies. For example `#is-it-down` may be where you instruct your entire company to ask if there are issues.

Once the modal opens, check the box for triage channels, and click **Save.**

### Steps to test

You'll need an active incident open on FireHydrant that has recent activity in the last day. To see what incidents are currently open on FireHydrant, you can type `/fh list`

If, for example, you have an incident opened with the name "SSL Errors" – you can experiment with your new triage channel by sending a message "Are there SSL errors right now?" and seeing the FireHydrant bot reply to you.