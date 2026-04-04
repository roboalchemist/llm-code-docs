# Share files in messages

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

With file attachments, you can share additional information that helps
your team to visually understand your ideas. Sharing videos, voice
recordings, screenshots, and photos can make your messages more
effective and clear.

::::::: {.tab parse-titles=""}
Web/Desktop

You can share files with other Mattermost users or entire channels by:

- Dragging and dropping files into channels.
- Selecting the **Attachment**
  [\|attachments-icon\|](##SUBST##|attachments-icon|) icon in the
  message input box.
- Pasting from the clipboard.

## Share public links

Public links allow you to share message attachments with anyone outside
your Mattermost
`workspace </end-user-guide/end-user-guide-index>`{.interpreted-text
role="doc"}. To share an attachment, select the thumbnail of an
attachment, then select **Get Public Link**.

:::: tip
::: title
Tip
:::

If **Get Public Link** is not visible in the file previewer, ask your
system admin to enable the feature from the System Console under **Site
Configuration \> Public Links**.
::::

## Download files

You can download an attached file by selecting the **Download**
[\|download-icon\|](##SUBST##|download-icon|) icon next to the file
thumbnail.

:::: tip
::: title
Tip
:::

From Mattermost desktop app v5.2, you can review download status, access
downloads, and clear the list of downloads from a new **Downloads**
[\|desktop-download-icon\|](##SUBST##|desktop-download-icon|) option
located in the top-right corner of the desktop app window.
::::

## Access files

Access all files shared in a channel by selecting the **Channel files**
[\|channel-files-icon\|](##SUBST##|channel-files-icon|) icon in the
channel header.
:::::::

::: {.tab parse-titles=""}
Mobile

You can share files with other Mattermost users or entire channels by
tapping the **Attachment**
[\|attachments-icon\|](##SUBST##|attachments-icon|) icon under the
message input box when composing a message.

From Mattermost v10.7 and mobile v2.27, you can play and download audio
files directly from the message thread.

![Tap on attachment icon to attach a file and send it in the channel.](../../images/mobile-attach-a-file-to-send-in-a-channel.gif)

## Access files on mobile

1. Tap the channel name at the top of the screen.

![Click on the channel name to explore available options.](../../images/mobile-channel-name-click.jpg)

1. Tap **Files**.

![Tap on Files to explore the available file attachments in the channel.](../../images/mobile-edit-channel.jpg)

1. Tap a file to download it, open it, or copy a public link to the
    file.

![Tap on a file to download and open it.](../../images/mobile-tap-a-file-name-to-download.jpg)

Or you can also click on [\|more-icon\|](##SUBST##|more-icon|) to
download the file or open it in the channel.

![You can also use more options to download ot view the file in the channel.](../../images/mobile-more-options-to-download-or-view-a-file.jpg)
:::

## Attachment limits and sizes

Up to 10 files can be attached per post. The default maximum file size
is 100 MB, but this can be changed by the system admin. See our
`Configuration Settings <administration-guide/configure/environment-configuration-settings:maximum file size>`{.interpreted-text
role="ref"} product documentation for details.

Image files can be a maximum size of 7680 pixels x 4320 pixels, with a
maximum image resolution of 33 MP (mega pixels) or 8K resolution, and a
maximum raw image file size of approximately 253 MB. System admins can
customize the maximum image resolution size within the `config.json`
file. See our
`Configuration Settings <administration-guide/configure/experimental-configuration-settings:maximum image resolution>`{.interpreted-text
role="ref"} product documentation for details.

## Preview file attachments

Mattermost has a built-in file previewer that you can use to:

- Download files
- Share public links
- View media

Select the thumbnail of an attached file to open it in the file
previewer.

### View media

The following media formats are supported on most browsers:

- Images: BMP, GIF, JPG, JPEG, PNG, SVG, WEBP
- Video: browser supported video formats, including but not limited to
  MP4 and MOV
- Audio: MP3, M4A
- Files: PDF, TXT

Other document previews (such as Word, Excel, or PPT) are not yet
supported.
