# Source: https://learn.microsoft.com/en-us/clarity/inline-player

Title: Inline Player

URL Source: https://learn.microsoft.com/en-us/clarity/inline-player

Published Time: Fri, 05 Dec 2025 18:51:05 GMT

Markdown Content:
Important

*   Clarity retains Recordings for 30 days from the time of recording. However, **Favorite** recordings and a randomly selected recording are retained for up to 13 months.
*   The timestamp in recordings is displayed in the time zone of the Clarity user.

Clarity offers an inline player for visualizing user behavior on your site. You can explore session recordings quickly without losing the context of user actions.

The inline player includes the following features:

1.   [Playback viewer](https://learn.microsoft.com/en-us/clarity/inline-player#playback-viewer)
2.   [Playback controls](https://learn.microsoft.com/en-us/clarity/inline-player#playback-controls)
3.   [Details tab](https://learn.microsoft.com/en-us/clarity/inline-player#view-details)

The playback viewer contains the inline player and several options for exploring further:

![Image 1: Playback viewer details.](https://learn.microsoft.com/en-us/clarity/media/inline-player.png)

*   **View highlights**: Quickly view highlights of the recording by surfacing key user interactions and multiple key events without needing to watch entire recording. [Learn more](https://learn.microsoft.com/en-us/clarity/inline-player#view-highlights).
*   **Summarize recordings**: Using generative AI, this feature [summarizes multiple session recordings](https://learn.microsoft.com/en-us/clarity/copilot/grouped-session-insights) at a time. You can generate these insights for custom selected recordings or for top 10 recordings.
*   **More details:** View the [details tab](https://learn.microsoft.com/en-us/clarity/inline-player#view-details) for this recording.
*   **Click and Area:** View the [click map](https://learn.microsoft.com/en-us/clarity/heatmaps/click-maps) and [Area map](https://learn.microsoft.com/en-us/clarity/heatmaps/area-maps) for this recording.
*   **Scroll:** View the [scroll map](https://learn.microsoft.com/en-us/clarity/heatmaps/scroll-maps) for this recording.
*   **Attention:** View the [attention map](https://learn.microsoft.com/en-us/clarity/heatmaps/attention-maps) for this recording.
*   **Favorite the session**: You can [favorite this session](https://learn.microsoft.com/en-us/clarity/session-recordings/session-list#favorite-the-sessions) from the inline player.
*   **Rate this recording**: Provide your feedback by rating the recording.
*   **Open in new tab**: Open the playback viewer in a new tab with [more details](https://learn.microsoft.com/en-us/clarity/inline-player#more-details), and other playback controls such as [add note](https://learn.microsoft.com/en-us/clarity/inline-player#add-note), [favorite](https://learn.microsoft.com/en-us/clarity/session-recordings/session-list#favorite-the-sessions), [share](https://learn.microsoft.com/en-us/clarity/setup-and-installation/share-clarity), and video settings.
*   **Share:**[Share](https://learn.microsoft.com/en-us/clarity/setup-and-installation/share-clarity) the recording.

Highlights break long session recordings into meaningful, digestible moments by surfacing key user interactions and events. Recordings are automatically converted into multiple highlights, making them easier to scan and analyze.

Events are prioritized to surface the most meaningful interactions, such as insights, navigational actions, and key user inputs, while filtering out less significant clicks:

*   **Clicks**: Actions on buttons, text areas, or images that indicate intent.
*   **JavaScript errors**: Specific error states or failed actions (configurable as smart events).
*   **Form inputs**: User engagement with forms, text fields, or submission actions.
*   **Smart events**: Context-aware triggers that capture meaningful interactions beyond simple clicks.

Note

In highlights mode, some options are not available such as: heatmaps, playback speed control, summarize recording, open in a new tab, or favoriting.

1.   Select **View highlights** for a recording.

![Image 2: Select view highlights.](https://learn.microsoft.com/en-us/clarity/media/select-view-highlights.png)

2.   The session opens to highlights, where:

Tip

For an optimal Highlights experience, enable Autoplay to view the session as a continuous feed. ![Image 3: Highlights in autoplay.](https://learn.microsoft.com/en-us/clarity/media/highlights-autoplay.gif) 
3.   Select **View full recording** to get back to the full recording from any highlight.

![Image 4: Highlights back view.](https://learn.microsoft.com/en-us/clarity/media/highlights-back-view.png)

With heatmaps, you can analyze user behavior in any recording. Select the Click button to see a [click map](https://learn.microsoft.com/en-us/clarity/heatmaps/click-maps) and [Area map](https://learn.microsoft.com/en-us/clarity/heatmaps/area-maps) for this recording. Select the Scroll button to view a [scroll map](https://learn.microsoft.com/en-us/clarity/heatmaps/scroll-maps) and find out how far the user scrolled on your page. Similarly, view the [attention maps](https://learn.microsoft.com/en-us/clarity/heatmaps/attention-maps). Dynamically view heatmaps for different page states in the session using the **forward by 30 seconds** and **rewind by 10 seconds** button.

![Image 5: Recordings to heat maps.](https://learn.microsoft.com/en-us/clarity/media/recordings-to-heatmaps.png)

**Note**:

*   While you view a click, scroll, attention, or area map, playback controls such as play, pause, skip inactivity, auto play, add note, summarize recordings, and speed are disabled.

![Image 6: Disabled play button in recordings.](https://learn.microsoft.com/en-us/clarity/media/disabled-play-button.gif)

*   Currently, click map, scroll map, attention map, and area map options are unavailable while viewing the recording in a new tab or when you share it.

![Image 7: Recordings in new tab with no heat maps.](https://learn.microsoft.com/en-us/clarity/media/recordings-in-new-tab.png)

When you select a card, you can view the session recording in the playback viewer. The viewer allows you to analyze and understand user interactions with your site.You can view:

*   User clicks throughout the session.
*   Insights such as excessive scrolling, rage clicks, dead clicks, and quick backs.
*   User cursor movements.
*   Pages hidden or visible to the user.
*   How and where users enter text on your site.
*   Which contexts are the users selecting.
*   Where users change the screen size.

![Image 8: Playback viewer.](https://learn.microsoft.com/en-us/clarity/media/playback-viewer.png)

Important

For privacy, Clarity masks the sensitive data by default before sending it to Clarity. To unmask or mask specific sections of your page, refer to [Masking content](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-masking).

While the masked content is shielded, third-party iFrame content is blocked on the playback viewer.

![Image 9: Playback controls.](https://learn.microsoft.com/en-us/clarity/media/playback-controls.png)

Playback controls provide you with the following options:

Here are the playback controls:

*   **Play / Pause**: Plays or pauses the recording.
*   **Rewind**: Rewind the recording by 10 seconds.
*   **Fast forward**: Fast forwards the recording by 30 seconds.
*   **Play previous**: Select to play the previous recording. This is disabled for the first recording.
*   **Play next**: Select to play the next recording. This is disabled for the last recording.
*   **Playback speed**: Available presets: 0.25X, 0.5X, Normal, 1.5X, 2X, 4X, 8X, and 12X.
*   **Time**: The current time / total time of recording.
*   **Add note**: Add a note directly to specific moments in a session recording. [Learn more](https://learn.microsoft.com/en-us/clarity/inline-player#add-note).
*   **Video settings**: The video settings include: 
    *   **Autoplay**: Learn more about [Autoplay](https://learn.microsoft.com/en-us/clarity/inline-player#autoplay).
    *   **Mute**: Mute or unmute the audio in a recording.
    *   **Skip inactivity**: When checked, periods of inactivity on the page are skipped.
    *   **View symbols and shortcuts**: Timeline events that describe events shown in the recordings timeline, along with keyboard shortcuts. ![Image 10: Timeline events.](https://learn.microsoft.com/en-us/clarity/media/timeline-events.png)

The Add note feature allows you to attach notes directly to specific moments in a session recording. It complements existing Favorites and Labeling capabilities, creating a unified, seamless experience without redundancy.

This feature addresses common pain points by:

*   Reducing time-consuming manual workflows of taking notes, screenshots, and timestamps.
*   Enhancing collaboration by providing clear context within the recording itself.
*   Improving team alignment by enabling direct discussions on specific moments.
*   Eliminating fragmented workflows caused by reliance on external tools.

*   While reviewing a session, you can add a note in two ways:

    *   Select the **Add note** option and enter the details.

![Image 11: Add note.](https://learn.microsoft.com/en-us/clarity/media/add-note.png)

    *   Hover over a point in the timeline and add a note directly from there.

![Image 12: Add note from a hover.](https://learn.microsoft.com/en-us/clarity/media/add-note-on-hover.png)

*   Once a note is added, the recording is automatically added to Favorites.

![Image 13: Note favorite.](https://learn.microsoft.com/en-us/clarity/media/note-favorite.png)

*   You can also filter recordings with notes labelled as **Note**.

![Image 14: Note label.](https://learn.microsoft.com/en-us/clarity/media/note-label.png)

*   You can edit or remove the note by selecting the **Edit icon** or **Delete icon** in the labels.

![Image 15: Edit note in label.](https://learn.microsoft.com/en-us/clarity/media/edit-delete-note-label.png)

*   You can also edit or remove the note by selecting the **Edit icon** or **Delete icon** in the playback controls.

![Image 16: Edit note in playback.](https://learn.microsoft.com/en-us/clarity/media/edit-delete-note-playback.png)

*   When replaying, notes appear at the exact points where they were added, making it easier to review and share key insights.

Go to **Video settings**. **Toggle** the **Autoplay** to automatically play the next recording in 5 seconds.

![Image 17: Autoplay in video settings.](https://learn.microsoft.com/en-us/clarity/media/autoplay-in-video-settings.gif)

If Autoplay is enabled, at the end of each recording, you can see the following controls:

![Image 18: Pop up seen if Autoplay is enabled.](https://learn.microsoft.com/en-us/clarity/media/autoplay-enabled-popup.png)

*   **Rate recording**: Provide feedback for this recording.
*   **Favorite**: [Favorite](https://learn.microsoft.com/en-us/clarity/session-recordings/session-list#favorite-the-sessions) this recording.
*   **Share**: [Share](https://learn.microsoft.com/en-us/clarity/setup-and-installation/share-clarity) this recording.
*   **Add labels**: Choose from the list of available [labels](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-labels) so you find this recording later.
*   **Cancel**: Cancel the timer that is running on **Play next** and **Exit** the pop-up window to return to the current recording.
*   **Play next**: Play the next recording before the timer ends.

If Autoplay is disabled, at the end of each recording, you can see the following controls:

![Image 19: Pop up seen if Autoplay is disabled.](https://learn.microsoft.com/en-us/clarity/media/autoplay-disabled-popup.png)

*   **Rate recording**: Provide feedback for this recording.
*   **Favorite**: [Favorite](https://learn.microsoft.com/en-us/clarity/session-recordings/session-list#favorite-the-sessions) this recording
*   **Share**: [Share](https://learn.microsoft.com/en-us/clarity/setup-and-installation/share-clarity) this recording.
*   **Add labels**: Choose from the list of available [labels](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-labels) so you find this recording later.
*   **Exit**: Exit the pop-up window and return to the current recording.
*   **Play next**: Play the next recording.

The details tab includes:

*   [Session list](https://learn.microsoft.com/en-us/clarity/session-recordings/session-list)
*   [More details](https://learn.microsoft.com/en-us/clarity/inline-player#more-details)

Select the **More details** button to view the summary, [Insights](https://learn.microsoft.com/en-us/clarity/copilot/session-insights) for your session, and the timeline of user events as shown:

![Image 20: More details viewer.](https://learn.microsoft.com/en-us/clarity/media/playback-viewer-details.png)

The summary includes:

1.   [Events](https://learn.microsoft.com/en-us/clarity/inline-player#events)
2.   [Session info](https://learn.microsoft.com/en-us/clarity/inline-player#session-info)
3.   [Insights](https://learn.microsoft.com/en-us/clarity/copilot/session-insights)

These events showcase the detailed time at which events occurred that includes page visits within a session. Each page has events associated with it.

For each event, select **Expand details** to view page visit, duration, load time, event count, LCP, INP, CLS, Performance score and more.

![Image 21: Events card.](https://learn.microsoft.com/en-us/clarity/media/events-card.png)

The supported event types are:

**Insights**:

*   **Rage clicks**: Check [Rage clicks](https://learn.microsoft.com/en-us/clarity/insights/semantic-metrics#rage-clicks) to learn more.
*   **Dead clicks**: Check [Dead clicks](https://learn.microsoft.com/en-us/clarity/insights/semantic-metrics#dead-clicks) to learn more.
*   **Excessive scrolling**: Check [Excessive scrolling](https://learn.microsoft.com/en-us/clarity/insights/semantic-metrics#excessive-scrolling) to learn more.
*   **Quick backs**: Check [Quick back](https://learn.microsoft.com/en-us/clarity/insights/semantic-metrics#quick-backs) to learn more.

**Actions**:

*   **Click**: This event is seen when a user clicks on a page.
*   **Scroll**: This event is seen when a user scrolls on a page.
*   **Area**: This event is seen when there are total clicks for all the elements within an area.
*   **Input**: This event is seen when a user inputs text into a form element. You can filter to this event with the "Entered text" filter.
*   **Refreshed page**: This event is seen when a user refreshes their browser on this page.
*   **Resize**: This event is seen when the user changes the size of their browser window or switches between landscape and portrait on mobile. You can filter this event with the "Resized page" filter.
*   **Selection**: This event is seen when a user selects text on the page. You can filter to this event with the "Selected text" filter.
*   **Smart events**: This event is seen when a smart event is identified automatically or when a user manually sets an event. Learn more about [smart events](https://learn.microsoft.com/en-us/clarity/setup-and-installation/smart-events).

**Page**:

*   **Page visible**: This event is seen when a user's attention is on your web page.
*   **Page hidden**: This event is seen when your web page is hidden behind other tabs or windows.
*   **JavaScript error**: This event is seen when a JavaScript error is detected. You can also see the error string in the timeline.

**Custom**:

*   **Custom page ID**: This event is seen when a user sets custom page ID through Clarity [Client API custom identifiers](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api#javascript-apis). You can filter to this event with the [Custom IDs](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#custom-ids).
*   **Custom tags**: This event is seen when a user sets custom tags. You can filter to this event with Custom tags filter.

![Image 22: Session information card.](https://learn.microsoft.com/en-us/clarity/media/session-info-card.png)

The session info contains the following information:

1.   Date and time stamp
2.   User ID
3.   The location in which the session is recorded
4.   Device details that include screen resolution, Browser, and Operating system with version
5.   Clicks, Page views, and User intent
6.   Entry and exit URLs
7.   Referrer
8.   [Custom user ID](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#custom-ids)
9.   [Custom session ID](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#custom-ids)
10.   [Custom page ID](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#custom-ids)
11.   [Labels](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-labels)

Note

Though Screen resolution and operating system's version are included in the session, filtering on based on these two details is currently not supported.

*   Some recordings might look broken or have missing images. This is because Clarity might have difficulty locating CSS, font, or images to display the site. To learn more, see [Troubleshoot Recordings](https://learn.microsoft.com/en-us/clarity/session-recordings/troubleshooting-recordings).

*   Clarity can't capture third-party iFrames and HTML Canvas elements. They appear in your recording as shown:

![Image 23: Third party iFrames.](https://learn.microsoft.com/en-us/clarity/media/third-party-iframe.png)

*   Clarity's inline player might have rendering issues if your website is on `http`. To mitigate layout issues and maximize Clarity functionality, consider migrating to `https`.

For more answers, refer to [Session Recordings FAQ](https://learn.microsoft.com/en-us/clarity/faq#session-recordings).
