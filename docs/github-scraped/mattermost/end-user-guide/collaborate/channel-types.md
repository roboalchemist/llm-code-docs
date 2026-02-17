# Channel types

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

Channels are used to organize conversations across different topics. The
channels you\'re a member of display in the left pane. Learn how to
create channels by visiting the
`create channels </end-user-guide/collaborate/create-channels>`{.interpreted-text
role="doc"} documentation.

There are 5 types of channels in Mattermost:

- [Public channels](#public-channels)
- [Private channels](#private-channels)
- [Direct message channels](#direct-message-channels)
- [Group message channels](#group-message-channels)
- [Archived channels](#archived-channels)

:::: tip
::: title
Tip
:::

Enterprise customers can additionally configure
`read-only <administration-guide/onboard/advanced-permissions:read-only channels>`{.interpreted-text
role="ref"} broadcast channels.
::::

## Public channels

Public channels are open to everyone on a team and are identified with a
**Globe** [\|globe\|](##SUBST##|globe|) icon. New team members are
automatically added to the **Town Square** channel.

See the
`Join and leave channels </end-user-guide/collaborate/join-leave-channels>`{.interpreted-text
role="doc"} documentation for details on discovering, joining, and
leaving other channels.

## Private channels

Private channels are channels for sensitive topics and are only visible
to selected team members. Private channels are identified with a
**Lock** [\|lock\|](##SUBST##|lock|) icon. Channel members can choose to
leave private channels at any time.

:::: note
::: title
Note
:::

- Mattermost Enterprise and Professional customers can restrict channel
  management to system and channel admins.
- In a Mattermost Team Edition instance, any member of a private channel
  can add or remove other members from private channels.
::::

## Direct message channels

Direct message channels are for conversations between 2 people. Only
members of the conversation can see direct messages and channel heading
information, including the last active status of the other user.

You can start a direct message with people on other teams
`unless the system admin has disabled your ability to do so <administration-guide/configure/site-configuration-settings:enable users to open direct message channels with>`{.interpreted-text
role="ref"}.

Direct messages update the numbered badge count and trigger a
notification unless the direct message is muted, or your notifications
are disabled. See the
`notification documentation </end-user-guide/preferences/manage-your-notifications>`{.interpreted-text
role="doc"} for details on customizing notifications based on your
preferences.

:::: note
::: title
Note
:::

- From Mattermost v10, when sending a direct message, Mattermost warns
  you that the recipient\'s availability is set to
  `Do Not Disturb <end-user-guide/preferences/set-your-status-availability:set your availability>`{.interpreted-text
  role="ref"}, and when the recipient\'s local time is outside of
  regular business hours (between 10PM and 6AM). This warning displays
  directly above the message text field.
- When a Mattermost user is deactivated in the system, your
  `direct message channel <end-user-guide/collaborate/channel-types:direct message channels>`{.interpreted-text
  role="ref"} with that user are [archived](#archived-channels) and
  marked as read-only. An **Archived** icon
  [\|file-box\|](##SUBST##|file-box|) displays next to archived
  channels.
::::

## Group message channels

Group message channels are for conversations between 3 to 7 people. Only
members of the conversation can see group messages. Group messages
always display a new message badge.

Want to have a group conversation with more than 7 people?
`Create a private channel </end-user-guide/collaborate/create-channels>`{.interpreted-text
role="doc"}. Alternatively, from Mattermost v9.1, you can
`convert group messages to a private channel </end-user-guide/collaborate/convert-group-messages>`{.interpreted-text
role="doc"}.

:::: note
::: title
Note
:::

- You can start a group message with people on other teams when
  `unless the system admin has disabled your ability to do so <administration-guide/configure/site-configuration-settings:enable users to open direct message channels with>`{.interpreted-text
  role="ref"}.
- From Mattermost v9.1, group messages increase the numbered badge count
  and trigger a notification unless the direct message is muted, or your
  notifications are disabled. Control how you\'re notified about group
  message conversations by going to **Settings \> Notifications**. See
  the
  `notification documentation </end-user-guide/preferences/manage-your-notifications>`{.interpreted-text
  role="doc"} to learn more.
- Any group message history you have with a deactivated user remains
  available
  `unless your system admin disables your ability to do so <administration-guide/configure/site-configuration-settings:allow users to view archived channels>`{.interpreted-text
  role="ref"}.
::::

## Archived channels

Archived channels are deactivated public, private, direct message, or
group message channels that are no longer used. Archived channels are
identified with a **File Box** [\|file-box\|](##SUBST##|file-box|) icon.

`Archiving a channel <end-user-guide/collaborate/archive-unarchive-channels:archive a channel>`{.interpreted-text
role="ref"} marks it read-only to prevent new messages from being sent
and preserve channel history. You can continue to access archived
channels, unless your system admin has
`disabled <administration-guide/configure/site-configuration-settings:allow users to view archived channels>`{.interpreted-text
role="ref"} your ability to do so.
