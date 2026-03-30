# Source: https://docs.logrocket.com/docs/using-logrocket-live.md

# Using LogRocket Live

For users who are currently active within your app, LogRocket offers you the option to fast forward to a live view within session playback. This can be especially helpful with chat or phone support, as well as an alternative option for screen sharing during conference calls.

## Using LogRocket Live

Sessions that are actively recording and sending events to LogRocket will see a "Go Live" button appear at the bottom of the session page.

<Image title="Screen Shot 2017-09-20 at 2.29.36 PM.png" alt={354} align="center" src="https://files.readme.io/066fdb96b70a89c69f1de1fc8960ecbf0d165a91befe87540671f4dee4949ca5-Screen_Shot_2024-09-25_at_2.18.04_PM.png">
  Click this button to enable LogRocket Live
</Image>

Once you click the button, the timeline will jump to the most recent part of the session. When new events are received, the entire timeline updates. The developer tab will also receive new log entries and network requests as they happen. The latency is typically under 10 seconds for live recordings.

We also let you know the current status of the session's user in an indicator message shown to the right of the "Go Live" button.

**User is Active** will be shown when the user is currently in the tab and performing actions that are sent to LogRocket. In this state, the video will be playing and the developer tab will be updating with new information.

**User is Inactive** will be shown when the user isn't active on the tab or they have gone inactive (or LogRocket is otherwise not receiving events).

After fifteen minutes of inactivity, LogRocket Live will be disabled.

## Which sessions have LogRocket Live?

Sessions that ended more than fifteen minutes ago will not have LogRocket Live enabled. If a user becomes active again after fifteen minutes they will be recorded in a new session, which would then have LogRocket Live enabled.