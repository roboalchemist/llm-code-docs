# Source: https://docs.firehydrant.com/docs/signals-shift-notifications.md

# Signals Shift Notifications

Want to notify a channel in Slack when a member of a team goes on-call? You're on the right guide.

If you are using FireHydrant's Signals product and need to notify a Slack channel when a user goes on call, you can achieve this by following the instructions on this page.

<Embed url="https://www.youtube.com/watch?v=4booshdMPqY" title="FireHydrant - Signals notifications in Slack" favicon="https://www.youtube.com/favicon.ico" provider="youtube.com" href="https://www.youtube.com/watch?v=4booshdMPqY" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Furl%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D4booshdMPqY%26type%3Dtext%252Fhtml%26schema%3Dyoutube%26display_name%3DYouTube%26src%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F4booshdMPqY%253Ffeature%253Doembed%22%20width%3D%22640%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

First, go to the team's Slack channel in your connected workspace. You can assign channels to teams using the FireHydrant UI, or, with the `/fh channel` command.

## Associating a team to a channel

You can run `/fh channel` from most channels (with the exception of incident channels) the FireHydrant bot is in. This command allows you to associate a team in your FireHydrant account to a Slack channel, it also allows you to configure [triage channels](https://docs.firehydrant.com/docs/triage-channels-in-slack).

### Choosing the schedules

Once you've associated a team to a channel, you **must** select the schedules you want to notify the channel about when the next shift begins. For example, you may have a "Primary On-Call" shift that you'd like to notify the channel about new user's going on-call.

<Image align="center" width="650px" src="https://files.readme.io/f06642307854d1c175f1febe78b39cf96e731c9c9725c25826cc27281b63d259-CleanShot_2025-01-07_at_18.36.102x.png" />

Once you've selected the schedule(s) you'd like to notify the channel. **Click Save.**

### That's it!

Now, when a user goes on-call for a schedule, the FireHydrant bot will post messages about the handoff.

<Image align="center" width="650px" src="https://files.readme.io/7d30c703a35d37ed430d84856e856dbfe34accddcaa6a8e02f2af3202dc50823-CleanShot_2025-01-07_at_18.37.472x.png" />