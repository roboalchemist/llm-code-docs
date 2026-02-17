# Set message priority

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

From Mattermost v7.7 and mobile v2.4, you can add a message priority
label to root messages to make important messages requiring timely
action or response more visible and less likely to be overlooked.

![Ensure important and urgent messages stand out clearly by adding priority labels to root messages.](../../images/MPA-Animated-GIF-Update-2023-08-15.gif){width="700px"}

To set the priority of a new root message:

1. Select the **Message Priority**
    [\|message-priority-icon\|](##SUBST##|message-priority-icon|) icon
    in the message formatting toolbar. Select from Standard, Important,
    or Urgent.
2. Select the priority for the message. Messages have a standard
    priority by default.
3. Select **Apply**

When you send a priority message, the priority label displays next to
your name in the channel, as well as the **Threads** view when others
reply to the thread.

## Send persistent notifications

From Mattermost v8.0, messages marked as urgent with a priority label
and containing an \@mention can trigger persistent notifications that
repeat until the recipient acknowledges, reacts, or replies.

To enable persistent notifications for a message:

1. Compose a root message with at least one \@mention.
2. Select the **Message Priority**
    [\|message-priority-icon\|](##SUBST##|message-priority-icon|) icon
    in the message formatting toolbar.
3. Select **Urgent**.
4. Select **Send persistent notifications**.
5. Select **Apply**.

:::: note
::: title
Note
:::

- \@channel, \@all and \@here mentions don\'t send persistent
  notifications.
- System admins can customize the maximum number of \@mentions
  permitted, how frequently and how many persistent notifications are
  sent, as well as disable persistent notifications for all users, if
  preferred. By default, users are notified every 5 minutes for a total
  of 30 minutes. See the
  `configuration <administration-guide/configure/site-configuration-settings:persistent notifications>`{.interpreted-text
  role="ref"} documentation for details.
::::

## Receive persistent notifications

You must have desktop and/or mobile push notifications enabled to
receive persistent notifications. How you\'re notified depends on your
`notifications preferences </end-user-guide/preferences/manage-your-notifications>`{.interpreted-text
role="doc"} for desktop and mobile push notifications. You won\'t be
notified when your availability is set to **Do Not Disturb**, or if
you\'re
`Out of Office <end-user-guide/preferences/set-your-status-availability:set your availability>`{.interpreted-text
role="ref"}. Learn more about managing and customizing how you receive
`Mattermost notifications </end-user-guide/preferences/manage-your-notifications>`{.interpreted-text
role="doc"}.

Urgent messages show a red mention badge which remains visibible until
you view the message. Selecting the **Acknowledge** icon (when present)
won\'t impact the urgent red mention badge.

![Example of the channel sidebar with both regular and urgent unread messages.](../../images/urgent-message.png)

To stop receiving persistent notifications, you can reply to the thread,
select the **Acknowlege** icon (when present), or react to the thread
with an emoji. Persistent notifications also stop if the original
message is deleted, or if the maximum number of persistent notifications
are sent.

## Request acknowledgements

You can additionally request that recipients actively acknowledge the
message to track that messages have been seen and actioned. By default,
marking a message as Urgent priority automatically requests an
acknowledgement.

When you request acknowlegement of a message, an **Acknowledge**
[\|acknowledge-button\|](##SUBST##|acknowledge-button|) button is added
below the sent message. You can mark message as acknowledged by
selecting the button, and you can hover over the **Acknowledged**
[\|acknowledge-button\|](##SUBST##|acknowledge-button|) icon to review
who has acknowledged the message.

:::: tip
::: title
Tip
:::

- When you have push notifications enabled on mobile, you\'ll be
  notified every five minutes until you acknowledge or reply to the
  message.
- After acknowledging a message, you have up to five minutes to change
  your mind. Select the **Acknowledged**
  [\|acknowledge-button\|](##SUBST##|acknowledge-button|) button again
  to remove your name from the list of acknowledged users.
::::
