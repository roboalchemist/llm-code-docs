# Archive and unarchive channels

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

## Archive a channel

Delete
`public channels <end-user-guide/collaborate/channel-types:public channels>`{.interpreted-text
role="ref"} and
`private channels <end-user-guide/collaborate/channel-types:private channels>`{.interpreted-text
role="ref"} when they\'re no longer needed by archiving them. Archiving
channels removes them from the channel sidebar and marks them as
read-only. Anyone can archive a public or private channel they\'re a
member of, unless your system admin has
`disabled </administration-guide/onboard/advanced-permissions>`{.interpreted-text
role="doc"} your ability to do so.

:::: tip
::: title
Tip
:::

You can continue to access archived channels, unless your system admin
has
`disabled <administration-guide/configure/site-configuration-settings:allow users to view archived channels>`{.interpreted-text
role="ref"} your ability to do so.
::::

::: tab
Web/Desktop

To archive a channel, select the channel name at the top of the center
pane to access the drop-down menu, then select **Archive Channel**.
:::

::: tab
Mobile

To archive a channel:

1. Tap the channel you want to delete.

![Select a channel that you want to edit.](../../images/mobile-select-a-channel.jpg)

1. Tap the **More**
    [\|more-icon-vertical\|](##SUBST##|more-icon-vertical|) icon located
    in the top right corner of the app.

![Tap on More options to access available options for the channel.](../../images/mobile-select-more-options-for-a-channel.jpg)

1. Tap **View info**.

![Tap on View info to see the basic channel info.](../../images/mobile-select-view-info-for-a-channel.jpg)

1. Tap **Archive Channel**.

![Tap on Archive channel to archive the current channel.](../../images/mobile-edit-channel.jpg)

1. Tap **Yes** to confirm.

![Tap on Yes to confirm your choice.](../../images/mobile-confirm-archive-a-channel.jpg)
:::

:::: note
::: title
Note
:::

- When a Mattermost user is deactivated in the system, your
  `direct message channel <end-user-guide/collaborate/channel-types:direct message channels>`{.interpreted-text
  role="ref"} with that user are archived and marked as read-only. An
  **Archived** icon [\|file-box\|](##SUBST##|file-box|) displays next to
  archived channels.
- `Group message channels <end-user-guide/collaborate/channel-types:group message channels>`{.interpreted-text
  role="ref"} can\'t be archived, but they can be closed to hide them
  from the channel sidebar.
- The default **Town Square** channel can\'t be archived.
- System admins can archive channels without needing to be a channel
  member by using the System Console.
- Because a copy of the channel exists on the server, you can\'t reuse
  the URL of an archived channel when
  `creating a new channel </end-user-guide/collaborate/create-channels>`{.interpreted-text
  role="doc"}.
::::

## Unarchive a channel

System admins and Team admins can restore archived channels. When a
channel is unarchived, channel membership and all its content is
restored, unless messages and files have been deleted based on a
`data retention policy <administration-guide/configure/compliance-configuration-settings:data retention policies>`{.interpreted-text
role="ref"}.

::: tab
Web/Desktop

Search for the channel if required. Then, open the channel, select the
channel name at the top of the center pane to access the drop-down menu
and select **Unarchive Channel**.

![Unarchive a channel.](../../images/unarchive-channel.png)
:::

::: tab
Mobile

To unarchive a channel:

1. Tap the channel you want to unarchive.

![Select a channel that you want to edit.](../../images/mobile-select-a-channel.jpg)

1. Tap the **More**
    [\|more-icon-vertical\|](##SUBST##|more-icon-vertical|) icon located
    in the top right corner of the app.

![Tap on More options to access available options for the channel.](../../images/mobile-select-more-options-for-a-channel.jpg)

1. Tap **View info**.

![Tap on View info to see the basic channel info.](../../images/mobile-select-view-info-for-a-channel.jpg)

1. Tap **Unarchive Channel**.

![Tap on Unarchive channel to unarchive the current channel.](../../images/mobile-unarchive-a-channel.jpg)

1. Tap **Yes** to confirm.

![Tap on Yes to confirm your choice.](../../images/mobile-confirm-unarchive-a-channel.jpg)
:::

:::: tip
::: title
Tip
:::

Alternatively, system admins can unarchive channels
`via the mmctl <administration-guide/manage/mmctl-command-line-tool:mmctl channel unarchive>`{.interpreted-text
role="ref"}, and Team admins can unarchive channels [via the
API](https://api.mattermost.com/#operation/RestoreChannel).
::::
