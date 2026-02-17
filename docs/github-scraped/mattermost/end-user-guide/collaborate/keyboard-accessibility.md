# Keyboard accessibility

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

Navigational keyboard shortcuts help you use Mattermost in a web browser
or the desktop app without needing a mouse. Below is a list of supported
accessibility shortcuts.

+-----------------------------+--------------------------------------------+
| Keyboard shortcut           | Description                                |
+=============================+============================================+
| | Desktop App:              | | Move focus to the next section           |
|   `F6`{.interpreted-text    | |                                          |
|   role="kbd"}               |                                            |
| | Browser:                  |                                            |
|   `Ctrl`{.interpreted-text  |                                            |
|   role="kbd"}               |                                            |
|   `F6`{.interpreted-text    |                                            |
|   role="kbd"}               |                                            |
+-----------------------------+--------------------------------------------+
| | Desktop App:              | | Move focus to the previous section       |
|   `Shift`{.interpreted-text |                                            |
|   role="kbd"}               |                                            |
|   `F6`{.interpreted-text    |                                            |
|   role="kbd"}               |                                            |
| | Browser:                  |                                            |
|   `Ctrl`{.interpreted-text  |                                            |
|   role="kbd"}               |                                            |
|   `Shift`{.interpreted-text |                                            |
|   role="kbd"}               |                                            |
|   `F6`{.interpreted-text    |                                            |
|   role="kbd"}               |                                            |
+-----------------------------+--------------------------------------------+
| `Tab`{.interpreted-text     | Move focus to the next element             |
| role="kbd"}                 |                                            |
+-----------------------------+--------------------------------------------+
| `Shift`{.interpreted-text   | Move focus to the previous element         |
| role="kbd"}                 |                                            |
| `Tab`{.interpreted-text     |                                            |
| role="kbd"}                 |                                            |
+-----------------------------+--------------------------------------------+
| `↑`{.interpreted-text       | Move focus between messages in the post    |
| role="kbd"} or              | list or sections in the channel sidebar    |
| `↓`{.interpreted-text       |                                            |
| role="kbd"}                 |                                            |
+-----------------------------+--------------------------------------------+
| `Enter`{.interpreted-text   | Take action on the focused element         |
| role="kbd"}                 |                                            |
+-----------------------------+--------------------------------------------+

## Region navigation

Mattermost has eight regions that can be focused for navigation. Use
`F6`{.interpreted-text role="kbd"} in the desktop app, or use
`Ctrl`{.interpreted-text role="kbd"} `F6`{.interpreted-text role="kbd"}
in a browser repeatedly to move focus and loop through the regions in
this order:

1. Message list region
2. Message input region
3. Right-hand side message list region
4. Right-hand side message input region
5. Team menu region
6. Channel sidebar region
7. Channel header region
8. Search

![Navigate through the sections of Mattermost using a keyboard.](../../images/navigation.gif)

## Message navigation

When the message list region is focused, use the `↑`{.interpreted-text
role="kbd"} or `↓`{.interpreted-text role="kbd"} arrow keys to navigate
through messages and reply threads. Press `Tab`{.interpreted-text
role="kbd"} to navigate through message actions.

![Navigate through Mattermost messages using a keyboard.](../../images/message-navigation.gif)

### Message composition

Mattermost is compatible with most popular screen readers, such as
[Apple VoiceOver](https://www.apple.com/ca/accessibility/vision/) or
[JAWS for
Windows](https://www.freedomscientific.com/products/software/jaws/). A
custom readout is composed for each message by combining the message
elements and reading them together in full sentences. Message elements
will read in the following order:

1. Header: Author, timestamp, message type (i.e. parent post or reply)
2. Main Content: The message content typed by the author
3. Attachments: The number of attachments (if applicable)
4. Emoji Reactions: The number of unique emoji reactions (if
    applicable)
5. Saves/Pins: If a message is saved or pinned (if applicable)

For example, a message read by a screen reader may sound like the
following:

``` text
Eric Sethna at 12:57pm Thursday June 13th wrote a reply "Thanks for the review", 3 attachments, 2 reactions, message is saved and pinned.
```

## Channel sidebar navigation

When the channel sidebar region is focused, use the
`↑`{.interpreted-text role="kbd"} or `↓`{.interpreted-text role="kbd"}
arrow keys to focus individual sidebar sections, such as Insights,
Threads, Favorites, custom categories, public channels, private
channels, and direct messages. Press `Tab`{.interpreted-text role="kbd"}
to navigate through channels or other buttons within a sidebar section.

![Navigate the Mattermost channel sidebar using a keyboard.](../../images/channel-sidebar-navigation.gif)
